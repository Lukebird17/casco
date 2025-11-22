#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
RAG-Anything 问答智能体
基于官方示例严格实现
"""

import asyncio
import json
import os
from pathlib import Path
from typing import List, Dict, Any
from dotenv import load_dotenv, find_dotenv
from tqdm import tqdm
import logging

from raganything import RAGAnything, RAGAnythingConfig
from lightrag.llm.openai import openai_complete_if_cache, openai_embed
from lightrag.utils import EmbeddingFunc

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# 加载环境变量
load_dotenv(find_dotenv())


class RAGQAAgent:
    """基于 RAG-Anything 的问答智能体"""
    
    @staticmethod
    def _get_embedding_dim(model_name: str) -> int:
        """根据模型名称获取 embedding 维度"""
        dim_map = {
            'text-embedding-3-large': 3072,
            'text-embedding-3-small': 1536,
            'text-embedding-ada-002': 1536,
            'bge-m3': 1024,
            'bge-large': 1024,
            'bge-base': 768,
            'bge-small': 512,
        }
        
        # 精确匹配
        if model_name in dim_map:
            return dim_map[model_name]
        
        # 模糊匹配
        model_lower = model_name.lower()
        for key, dim in dim_map.items():
            if key in model_lower:
                return dim
        
        # 默认返回最常用的维度
        logger.warning(f"未知的 embedding 模型: {model_name}，使用默认维度 1536")
        return 1536
    
    def __init__(
        self,
        working_dir: str = "./rag_storage",
        parser: str = "mineru",
        parse_method: str = "auto"
    ):
        """
        初始化 RAG 问答智能体
        
        Args:
            working_dir: RAG 存储目录
            parser: 解析器选择 (mineru 或 docling)
            parse_method: 解析方法 (auto, ocr 或 txt)
        """
        # LLM API 配置
        self.llm_api_key = os.getenv("CLOUD_API_KEY")
        self.llm_base_url = os.getenv("CLOUD_BASE_URL")
        self.llm_model = os.getenv("CLOUD_MODEL", "gpt-4o-mini")
        print("print",self.llm_model)
        # Vision Model 配置（用于处理图像、表格等多模态内容）
        # 如果不设置，默认使用 LLM 的配置
        self.vision_model = os.getenv("VISION_MODEL") or self.llm_model
        self.vision_api_key = os.getenv("VISION_API_KEY") or self.llm_api_key
        self.vision_base_url = os.getenv("VISION_BASE_URL") or self.llm_base_url
        
        # Embedding API 配置（可能与 LLM 不同）
        self.embedding_api_key = os.getenv("OPENAI_API_KEY")
        self.embedding_base_url = os.getenv("OPENAI_BASE_URL")
        self.embedding_model = os.getenv("OPENAI_API_MODEL", "text-embedding-3-large")
        
        # Embedding 维度配置（根据模型自动设置）
        self.embedding_dim = self._get_embedding_dim(self.embedding_model)
        
        if not self.llm_api_key:
            raise ValueError("未找到 LLM API Key，请设置 CLOUD_API_KEY 环境变量")
        
        if not self.embedding_api_key:
            raise ValueError("未找到 Embedding API Key，请设置 OPENAI_API_KEY 环境变量")
        
        # 创建 RAGAnything 配置
        self.config = RAGAnythingConfig(
            working_dir=working_dir,
            parser=parser,
            parse_method=parse_method,
            enable_image_processing=True,
            enable_table_processing=True,
            enable_equation_processing=True,
        )
        
        # 初始化 RAG
        self.rag = None
        
    def _get_llm_model_func(self):
        """创建 LLM 模型函数（pickle-safe）"""
        # 捕获变量到局部作用域，避免 pickle 问题
        llm_model = self.llm_model
        llm_api_key = self.llm_api_key
        llm_base_url = self.llm_base_url
        
        def llm_model_func(prompt, system_prompt=None, history_messages=[], **kwargs):
            """LLM 模型函数 - 独立函数，可以被 pickle"""
            return openai_complete_if_cache(
                llm_model,
                prompt,
                system_prompt=system_prompt,
                history_messages=history_messages,
                api_key=llm_api_key,
                base_url=llm_base_url,
                **kwargs,
            )
        
        return llm_model_func
    
    def _get_vision_model_func(self):
        """创建视觉模型函数（pickle-safe）"""
        # 捕获变量到局部作用域
        vision_model = self.vision_model
        vision_api_key = self.vision_api_key
        vision_base_url = self.vision_base_url
        llm_model_func = self._get_llm_model_func()  # 获取 LLM 函数
        
        def vision_model_func(
            prompt,
            system_prompt=None,
            history_messages=[],
            image_data=None,
            messages=None,
            **kwargs
        ):
            """视觉模型函数 - 独立函数，可以被 pickle"""
            # 如果提供了messages格式（用于多模态VLM增强查询），直接使用
            if messages:
                return openai_complete_if_cache(
                    vision_model,
                    "",
                    system_prompt=None,
                    history_messages=[],
                    messages=messages,
                    api_key=vision_api_key,
                    base_url=vision_base_url,
                    **kwargs,
                )
            # 传统单图片格式
            elif image_data:
                return openai_complete_if_cache(
                    vision_model,
                    "",
                    system_prompt=None,
                    history_messages=[],
                    messages=[
                        {"role": "system", "content": system_prompt}
                        if system_prompt
                        else None,
                        {
                            "role": "user",
                            "content": [
                                {"type": "text", "text": prompt},
                                {
                                    "type": "image_url",
                                    "image_url": {
                                        "url": f"data:image/jpeg;base64,{image_data}"
                                    },
                                },
                            ],
                        }
                        if image_data
                        else {"role": "user", "content": prompt},
                    ],
                    api_key=vision_api_key,
                    base_url=vision_base_url,
                    **kwargs,
                )
            # 纯文本格式
            else:
                return llm_model_func(prompt, system_prompt, history_messages, **kwargs)
        
        return vision_model_func
    
    def _get_embedding_func(self):
        """创建嵌入函数 - 使用独立的 Embedding API 配置"""
        logger.info(f"配置 Embedding API:")
        logger.info(f"  Base URL: {self.embedding_base_url}")
        logger.info(f"  Model: {self.embedding_model}")
        logger.info(f"  Dimension: {self.embedding_dim}")
        logger.info(f"  API Key: {self.embedding_api_key[:10]}..." if self.embedding_api_key else "  API Key: 未设置")
        
        return EmbeddingFunc(
            embedding_dim=self.embedding_dim,  # 使用自动检测的维度
            max_token_size=8192,
            func=lambda texts: openai_embed(
                texts,
                model=self.embedding_model,
                api_key=self.embedding_api_key,  # 使用 Embedding 专用的 API Key
                base_url=self.embedding_base_url,  # 使用 Embedding 专用的 Base URL
            ),
        )
    
    async def initialize(self):
        """初始化 RAG 系统"""
        logger.info("🚀 初始化 RAG-Anything 系统...")
        logger.info(f"LLM API: {self.llm_base_url} / {self.llm_model}")
        logger.info(f"Vision API: {self.vision_base_url} / {self.vision_model}")
        logger.info(f"Embedding API: {self.embedding_base_url} / {self.embedding_model} ({self.embedding_dim}维)")
        
        # 检查是否存在旧数据且维度可能不匹配
        storage_path = Path(self.config.working_dir)
        if storage_path.exists():
            kv_files = list(storage_path.glob("vdb_*.json"))
            if kv_files:
                logger.warning("⚠️  检测到已存在的向量数据库")
                logger.warning(f"   如果遇到维度不匹配错误，请运行:")
                logger.warning(f"   rm -rf {self.config.working_dir}")
                logger.warning(f"   mkdir -p {self.config.working_dir}")
        
        # 初始化 RAGAnything
        # 注意：必须使用独立函数而不是类方法，因为 LightRAG 使用多进程需要 pickle
        self.rag = RAGAnything(
            config=self.config,
            llm_model_func=self._get_llm_model_func(),  # 返回独立函数
            vision_model_func=self._get_vision_model_func(),  # 返回独立函数
            embedding_func=self._get_embedding_func(),
        )
        
        logger.info("✅ RAG-Anything 系统初始化完成")
    
    async def process_document(
        self,
        file_path: str,
        output_dir: str = "./output",
        parse_method: str = None,
        show_progress: bool = True,
    ):
        """
        处理单个文档
        
        Args:
            file_path: 文档路径
            output_dir: 输出目录
            parse_method: 解析方法 (可选)
            show_progress: 是否显示进度条
            device: 使用的设备 ("cpu", "cuda", "mps" 等)
        """
        if not self.rag:
            await self.initialize()
        
        file_name = Path(file_path).name
        logger.info(f"📄 开始处理: {file_name} (设备: {device})")
        
        if show_progress:
            with tqdm(total=100, desc=f"处理 {file_name[:50]}", ncols=100, 
                     bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]') as pbar:
                # 解析阶段
                pbar.set_description(f"解析 {file_name[:50]}")
                pbar.update(30)
                
                # 处理文档（明确指定使用 CPU）
                await self.rag.process_document_complete(
                    file_path=file_path,
                    output_dir=output_dir,
                    parse_method=parse_method or self.config.parse_method,
                )
                
                # 完成
                pbar.set_description(f"完成 {file_name[:50]}")
                pbar.update(70)
        else:
            await self.rag.process_document_complete(
                file_path=file_path,
                output_dir=output_dir,
                parse_method=parse_method or self.config.parse_method,
            )
        
        logger.info(f"✅ 处理完成: {file_name}")
    
    async def process_folder(
        self,
        folder_path: str,
        output_dir: str = "./output",
        file_extensions: List[str] = None,
        recursive: bool = True,
        max_workers: int = 4,
        show_progress: bool = True
    ):
        """
        批量处理文件夹中的文档
        
        Args:
            folder_path: 文件夹路径
            output_dir: 输出目录
            file_extensions: 支持的文件扩展名列表
            recursive: 是否递归处理子文件夹
            max_workers: 最大并行处理数
            show_progress: 是否显示进度条
        """
        if not self.rag:
            await self.initialize()
        
        logger.info(f"📁 扫描文件夹: {folder_path}")
        
        if file_extensions is None:
            file_extensions = [".pdf", ".docx", ".pptx"]
        
        # 先统计文件数量
        folder_path_obj = Path(folder_path)
        if recursive:
            files = []
            for ext in file_extensions:
                files.extend(list(folder_path_obj.rglob(f"*{ext}")))
        else:
            files = []
            for ext in file_extensions:
                files.extend(list(folder_path_obj.glob(f"*{ext}")))
        
        total_files = len(files)
        logger.info(f"📊 找到 {total_files} 个文件待处理")
        
        if total_files == 0:
            logger.warning("⚠️  未找到匹配的文件")
            return
        
        # 显示文件列表
        logger.info("文件列表:")
        for i, f in enumerate(files[:10], 1):
            logger.info(f"  {i}. {f.name}")
        if total_files > 10:
            logger.info(f"  ... 还有 {total_files - 10} 个文件")
        
        # 处理多个文档（带总进度条）
        if show_progress:
            print(f"\n{'='*80}")
            print(f"开始批量处理 {total_files} 个文件 (并行数: {max_workers})")
            print(f"{'='*80}\n")
            
            # 创建一个大的进度条显示整体进度
            with tqdm(total=total_files, desc="总体进度", unit="文件", 
                     ncols=100, position=0, leave=True,
                     bar_format='{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]') as main_pbar:
                
                # 记录已处理文件数
                processed_count = 0
                
                # 逐个处理文件
                for file_path in files:
                    try:
                        # 更新当前处理的文件名
                        file_name = file_path.name
                        main_pbar.set_description(f"处理中: {file_name[:40]}")
                        
                        # 处理文档
                        await self.rag.process_document_complete(
                            file_path=str(file_path),
                            output_dir=output_dir,
                            parse_method=self.config.parse_method
                        )
                        
                        processed_count += 1
                        main_pbar.update(1)
                        main_pbar.set_description(f"完成 {processed_count}/{total_files}")
                        
                    except Exception as e:
                        logger.error(f"❌ 处理失败: {file_name} - {e}")
                        main_pbar.update(1)
                        continue
                
                main_pbar.set_description(f"✅ 全部完成")
        else:
            await self.rag.process_folder_complete(
                folder_path=folder_path,
                output_dir=output_dir,
                file_extensions=file_extensions,
                recursive=recursive,
                max_workers=max_workers
            )
        
        logger.info(f"✅ 文件夹处理完成: {folder_path}")
        logger.info(f"✅ 共处理 {total_files} 个文件")
    
    async def query(
        self,
        question: str,
        mode: str = "hybrid",
        return_context: bool = True,
        show_progress: bool = True
    ) -> Dict[str, Any]:
        """
        查询 RAG 系统
        
        Args:
            question: 问题
            mode: 查询模式 (hybrid, local, global, naive)
            return_context: 是否返回检索上下文
            show_progress: 是否显示进度
            
        Returns:
            包含问题、上下文和答案的字典
        """
        if not self.rag:
            await self.initialize()
        
        logger.info(f"❓ 问题: {question}")
        logger.info(f"🔍 查询模式: {mode}")
        
        # 执行查询
        if show_progress:
            with tqdm(total=100, desc="查询中", ncols=100,
                     bar_format='{l_bar}{bar}| [{elapsed}<{remaining}]') as pbar:
                pbar.set_description("检索相关内容")
                pbar.update(30)
                
                result = await self.rag.aquery(
                    question,
                    mode=mode
                )
                
                pbar.set_description("生成答案")
                pbar.update(40)
                
                pbar.set_description("完成")
                pbar.update(30)
        else:
            result = await self.rag.aquery(
                question,
                mode=mode
            )
        
        # 构造返回结果
        response = {
            "question": question,
            "answer": result
        }
        
        # 如果需要返回上下文，可以从结果中提取
        if return_context:
            # 注意：这里的 retrieved_contexts 是示例，
            # 实际的上下文提取需要根据 RAG-Anything 的具体实现来调整
            response["retrieved_contexts"] = []
        
        # 显示答案（截断过长的答案）
        answer_preview = result[:200] + "..." if len(result) > 200 else result
        logger.info(f"💡 答案: {answer_preview}")
        
        return response
    
    async def query_batch(
        self,
        questions: List[str],
        mode: str = "hybrid",
        show_progress: bool = True
    ) -> List[Dict[str, Any]]:
        """
        批量查询
        
        Args:
            questions: 问题列表
            mode: 查询模式
            show_progress: 是否显示进度
            
        Returns:
            结果列表
        """
        results = []
        logger.info(f"📝 开始批量查询 {len(questions)} 个问题")
        
        if show_progress:
            for question in tqdm(questions, desc="批量查询进度", ncols=100):
                result = await self.query(question, mode=mode, show_progress=False)
                results.append(result)
        else:
            for i, question in enumerate(questions, 1):
                logger.info(f"\n{'='*60}")
                logger.info(f"处理问题 {i}/{len(questions)}")
                result = await self.query(question, mode=mode, show_progress=False)
                results.append(result)
        
        logger.info(f"✅ 批量查询完成，共 {len(results)} 个结果")
        return results
    
    def save_results(
        self,
        results: List[Dict[str, Any]],
        output_file: str = "qa_results.json"
    ):
        """
        保存结果到 JSON 文件（按照示例模板格式）
        
        Args:
            results: 结果列表
            output_file: 输出文件路径
        """
        # 按照示例模板格式构造输出
        output_data = {
            "items": results
        }
        
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)
        
        print(f"\n💾 结果已保存到: {output_file}")


async def main():
    """主函数"""
    # 初始化 RAG 问答智能体
    agent = RAGQAAgent(
        working_dir="./rag_storage",
        parser="mineru",
        parse_method="auto"
    )
    
    # 1. 处理文档（批量处理 data 目录下的所有 PDF）
    data_dir = "/home/honglianglu/ssd/casco/data"
    print("=" * 60)
    print("开始处理文档...")
    print("=" * 60)
    
    await agent.process_folder(
        folder_path=data_dir,
        output_dir="./output",
        file_extensions=[".pdf"],
        recursive=True,
        max_workers=2  # 根据您的系统资源调整
    )
    
    # 2. 示例查询
    print("\n" + "=" * 60)
    print("开始问答测试...")
    print("=" * 60)
    
    questions = [
        "文档中提到的主要安全规范有哪些？",
        "CBTC系统的核心组成部分是什么？",
        "2023年北京地铁昌平线事故的主要原因是什么？",
    ]
    
    # 批量查询
    results = await agent.query_batch(questions, mode="hybrid")
    
    # 3. 保存结果
    agent.save_results(
        results,
        output_file="/home/honglianglu/ssd/casco/qa_results.json"
    )
    
    print("\n" + "=" * 60)
    print("✅ 所有任务完成！")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())

