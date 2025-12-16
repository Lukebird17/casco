#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
图片向量存储（使用 CLIP 模型）
支持图片的向量化存储和检索
"""

import os
from typing import List, Dict, Optional
from pathlib import Path
import base64

import chromadb
from chromadb.config import Settings
from PIL import Image
from tqdm import tqdm

from config import VECTOR_DB_PATH


class ImageVectorStore:
    """
    图片向量存储类
    使用 CLIP 模型对图片进行编码，支持图片检索
    """
    
    def __init__(
        self,
        db_path: str = VECTOR_DB_PATH,
        collection_name: str = "image_documents",
        use_local_clip: bool = True,
    ):
        """
        初始化图片向量存储
        
        Args:
            db_path: 数据库路径
            collection_name: Collection 名称
            use_local_clip: 是否使用本地 CLIP 模型（True）或 API（False）
        """
        self.db_path = db_path
        self.collection_name = collection_name
        self.use_local_clip = use_local_clip
        
        # 初始化 CLIP 模型
        self._init_clip_model()
        
        # 初始化 ChromaDB
        os.makedirs(db_path, exist_ok=True)
        self.chroma_client = chromadb.PersistentClient(
            path=db_path, 
            settings=Settings(anonymized_telemetry=False)
        )
        
        # 获取或创建 collection
        self.collection = self.chroma_client.get_or_create_collection(
            name=collection_name,
            metadata={"description": "图片向量数据库"}
        )
    
    def _init_clip_model(self):
        """初始化 CLIP 模型
        
        支持的模型：
        1. openai/clip-vit-base-patch32：原版 CLIP，英文强，中文也可以（推荐）
        2. openai/clip-vit-large-patch14：更大更强，中英文都好
        3. OFA-Sys/chinese-clip-vit-base-patch16：中文优化，英文一般
        """
        if self.use_local_clip:
            try:
                from transformers import CLIPProcessor, CLIPModel
                import torch
                
                print("🔧 加载 CLIP 模型...")
                
                # 模型选择（根据需求选择）
                # 推荐：原版 CLIP 对中英文都有较好支持
                model_name = "openai/clip-vit-base-patch32"  # 推荐：中英文混合
                # model_name = "openai/clip-vit-large-patch14"  # 更强但更大
                # model_name = "OFA-Sys/chinese-clip-vit-base-patch16"  # 纯中文场景
                
                print(f"   模型: {model_name}")
                print(f"   说明: 此模型对中英文都有良好支持")
                
                self.clip_model = CLIPModel.from_pretrained(model_name)
                self.clip_processor = CLIPProcessor.from_pretrained(model_name)
                
                # 使用 GPU（如果可用）
                self.device = "cuda" if torch.cuda.is_available() else "cpu"
                self.clip_model.to(self.device)
                self.clip_model.eval()
                
                print(f"✅ CLIP 模型加载完成（设备: {self.device}）")
                
            except Exception as e:
                print(f"⚠️  加载本地 CLIP 失败: {e}")
                print("💡 请安装: pip install transformers torch pillow")
                raise
        else:
            # 使用 API（暂时不支持，需要后续实现）
            print("⚠️  API 模式暂未实现，请使用本地 CLIP")
            self.use_local_clip = True
            self._init_clip_model()
    
    def get_image_embedding(self, image_input) -> Optional[List[float]]:
        """
        获取图片的向量表示
        
        Args:
            image_input: 图片路径（str）或 PIL.Image 对象
            
        Returns:
            图片向量（512维）
        """
        try:
            # 加载图片
            if isinstance(image_input, str):
                if not os.path.exists(image_input):
                    print(f"⚠️  图片不存在: {image_input}")
                    return None
                image = Image.open(image_input).convert("RGB")
            else:
                image = image_input
            
            # 使用 CLIP 编码
            if self.use_local_clip:
                import torch
                
                inputs = self.clip_processor(
                    images=image, 
                    return_tensors="pt"
                ).to(self.device)
                
                with torch.no_grad():
                    image_features = self.clip_model.get_image_features(**inputs)
                    # 归一化
                    image_features = image_features / image_features.norm(dim=-1, keepdim=True)
                
                return image_features.cpu().numpy().flatten().tolist()
            
        except Exception as e:
            print(f"⚠️  获取图片 embedding 失败: {e}")
            return None
    
    def get_text_embedding(self, text: str) -> Optional[List[float]]:
        """
        获取文本的图像语义向量（用于图文匹配）
        
        Args:
            text: 文本内容
            
        Returns:
            文本向量（与图片向量在同一空间）
        """
        try:
            if self.use_local_clip:
                import torch
                
                inputs = self.clip_processor(
                    text=[text], 
                    return_tensors="pt",
                    padding=True
                ).to(self.device)
                
                with torch.no_grad():
                    text_features = self.clip_model.get_text_features(**inputs)
                    # 归一化
                    text_features = text_features / text_features.norm(dim=-1, keepdim=True)
                
                return text_features.cpu().numpy().flatten().tolist()
                
        except Exception as e:
            print(f"⚠️  获取文本 embedding 失败: {e}")
            return None
    
    def add_images(self, image_data: List[Dict]) -> None:
        """
        添加图片到向量数据库
        
        Args:
            image_data: 图片数据列表，每个元素包含：
                - image_path: 图片路径
                - filename: 源文件名
                - page_number: 页码
                - context: 上下文文本（可选）
                - caption: 图片描述（可选）
        """
        print(f"\n开始向量化并存储 {len(image_data)} 张图片...")
        
        skipped_count = 0
        batch_size = 10
        
        for i in tqdm(range(0, len(image_data), batch_size), desc="添加图片"):
            batch_data = image_data[i:i + batch_size]
            
            ids = []
            embeddings = []
            metadatas = []
            documents = []  # 存储图片描述文本
            
            for idx, img_info in enumerate(batch_data):
                # 获取图片 embedding
                embedding = self.get_image_embedding(img_info['image_path'])
                
                if embedding is None:
                    skipped_count += 1
                    continue
                
                # 生成唯一 ID
                img_id = f"{img_info['filename']}_page{img_info.get('page_number', 0)}_img{i+idx}"
                ids.append(img_id)
                embeddings.append(embedding)
                
                # 构建文档内容（用于展示）
                doc_text = f"图片来源: {img_info['filename']}, 第{img_info.get('page_number', 0)}页"
                if img_info.get('caption'):
                    doc_text += f"\n描述: {img_info['caption']}"
                if img_info.get('context'):
                    doc_text += f"\n上下文: {img_info['context'][:200]}..."
                documents.append(doc_text)
                
                # 元数据
                metadata = {
                    'filename': img_info['filename'],
                    'image_path': img_info['image_path'],
                    'page_number': img_info.get('page_number', 0),
                    'caption': img_info.get('caption', ''),
                    'context': img_info.get('context', '')[:500],  # 限制长度
                }
                metadatas.append(metadata)
            
            # 如果批次为空，跳过
            if not ids:
                continue
            
            # 批量添加到 ChromaDB
            try:
                self.collection = self.chroma_client.get_or_create_collection(
                    name=self.collection_name,
                    metadata={"description": "图片向量数据库"}
                )
                
                self.collection.add(
                    ids=ids,
                    embeddings=embeddings,
                    metadatas=metadatas,
                    documents=documents
                )
            except Exception as e:
                print(f"❌ 添加批次失败: {e}")
                skipped_count += len(ids)
        
        success_count = len(image_data) - skipped_count
        print(f"✅ 成功添加 {success_count} 张图片到向量数据库")
        if skipped_count > 0:
            print(f"⚠️  跳过 {skipped_count} 张图片（embedding 失败）")
    
    def search_by_text(self, query: str, top_k: int = 5) -> List[Dict]:
        """
        使用文本查询图片
        
        Args:
            query: 查询文本
            top_k: 返回结果数量
            
        Returns:
            图片结果列表
        """
        try:
            # 获取文本的图像语义向量
            query_embedding = self.get_text_embedding(query)
            
            if query_embedding is None:
                return []
            
            # 搜索
            results = self.collection.query(
                query_embeddings=[query_embedding],
                n_results=top_k,
                include=['documents', 'metadatas', 'distances']
            )
            
            # 格式化结果
            formatted_results = []
            
            if results and results['documents'] and len(results['documents']) > 0:
                documents = results['documents'][0]
                metadatas = results['metadatas'][0]
                distances = results['distances'][0]
                
                for doc, metadata, distance in zip(documents, metadatas, distances):
                    formatted_results.append({
                        'type': 'image',
                        'image_path': metadata.get('image_path', ''),
                        'description': doc,
                        'metadata': metadata,
                        'distance': distance,
                        'filename': metadata.get('filename', 'unknown'),
                        'page_number': metadata.get('page_number', 0),
                    })
            
            return formatted_results
            
        except Exception as e:
            print(f"❌ 图片搜索失败: {e}")
            return []
    
    def search_by_image(self, image_path: str, top_k: int = 5) -> List[Dict]:
        """
        使用图片查询相似图片
        
        Args:
            image_path: 查询图片路径
            top_k: 返回结果数量
            
        Returns:
            图片结果列表
        """
        try:
            # 获取图片向量
            query_embedding = self.get_image_embedding(image_path)
            
            if query_embedding is None:
                return []
            
            # 搜索
            results = self.collection.query(
                query_embeddings=[query_embedding],
                n_results=top_k,
                include=['documents', 'metadatas', 'distances']
            )
            
            # 格式化结果（与 search_by_text 相同）
            formatted_results = []
            
            if results and results['documents'] and len(results['documents']) > 0:
                documents = results['documents'][0]
                metadatas = results['metadatas'][0]
                distances = results['distances'][0]
                
                for doc, metadata, distance in zip(documents, metadatas, distances):
                    formatted_results.append({
                        'type': 'image',
                        'image_path': metadata.get('image_path', ''),
                        'description': doc,
                        'metadata': metadata,
                        'distance': distance,
                        'filename': metadata.get('filename', 'unknown'),
                        'page_number': metadata.get('page_number', 0),
                    })
            
            return formatted_results
            
        except Exception as e:
            print(f"❌ 图片搜索失败: {e}")
            return []
    
    def clear_collection(self) -> None:
        """清空 collection"""
        self.chroma_client.delete_collection(name=self.collection_name)
        self.collection = self.chroma_client.create_collection(
            name=self.collection_name,
            metadata={"description": "图片向量数据库"}
        )
        print("图片向量数据库已清空")
    
    def get_collection_count(self) -> int:
        """获取 collection 中的图片数量"""
        return self.collection.count()


if __name__ == "__main__":
    # 测试代码
    print("=== 测试图片向量存储 ===\n")
    
    store = ImageVectorStore()
    
    # 测试文本查询
    print("\n测试：文本查询图片")
    results = store.search_by_text("页表结构", top_k=3)
    print(f"找到 {len(results)} 个结果")

