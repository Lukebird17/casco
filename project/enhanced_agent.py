#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   enhanced_agent.py
@Time    :   2025/11/16
@Desc    :   增强版智能体 - 集成Token追踪、推理链、高级文档处理
'''

import json
import re
from typing import List, Dict, Tuple, Optional
from VectorBase import VectorStore
from LLM import OpenAIChat
from Embeddings import OpenAIEmbedding
from token_tracker import TokenTracker, TokenOptimizer
from reasoning_chain import ReasoningChain
from advanced_document_processor import VersionComparator, AdvancedTableExtractor
import os


class EnhancedRAGAgent:
    """
    增强版RAG智能体
    集成了Token追踪、推理链记录、高级文档处理等功能
    """
    
    def __init__(self, vector_store: VectorStore, llm: OpenAIChat, 
                 embedding: OpenAIEmbedding, enable_tracking: bool = True):
        """
        初始化增强版智能体
        Args:
            vector_store: 向量存储
            llm: 大语言模型
            embedding: 向量模型
            enable_tracking: 是否启用Token追踪
        """
        self.vector_store = vector_store
        self.llm = llm
        self.embedding = embedding
        
        # 功能模块
        self.token_tracker = TokenTracker() if enable_tracking else None
        self.token_optimizer = TokenOptimizer()
        self.version_comparator = VersionComparator()
        self.table_extractor = AdvancedTableExtractor()
        
        # 当前推理链
        self.current_reasoning_chain: Optional[ReasoningChain] = None
        
        # 统计信息
        self.query_count = 0
        self.cache = {}  # 简单的查询缓存
    
    def analyze_query_type(self, query: str) -> str:
        """
        分析问题类型：基础/中级/高级
        Args:
            query: 用户问题
        Returns:
            问题类型
        """
        # 高级题特征：多文档、对比、版本、演变
        advanced_keywords = ['对比', '演变', '版本', '分别', '不同', 'baseline', '变化', '差异']
        # 中级题特征：排名、列出、完整、所有
        intermediate_keywords = ['排第几', '排名', '列出', '完整', '所有', '分别是']
        
        query_lower = query.lower()
        
        for keyword in advanced_keywords:
            if keyword.lower() in query_lower:
                return 'advanced'
        
        for keyword in intermediate_keywords:
            if keyword in query:
                return 'intermediate'
        
        return 'basic'
    
    def enhance_query(self, query: str) -> List[str]:
        """
        查询增强：生成多个检索查询
        Args:
            query: 原始查询
        Returns:
            增强后的查询列表
        """
        queries = [query]
        
        # 提取年份
        years = re.findall(r'\b(19|20)\d{2}\b', query)
        queries.extend(years)
        
        # 提取专业术语
        technical_terms = self.extract_technical_terms(query)
        queries.extend(technical_terms)
        
        return list(set(queries))  # 去重
    
    def extract_technical_terms(self, query: str) -> List[str]:
        """
        提取专业术语
        Args:
            query: 查询文本
        Returns:
            专业术语列表
        """
        terms = []
        
        # 提取大写缩写（如CBTC, ERTMS, IEEE等）
        abbreviations = re.findall(r'\b[A-Z]{2,}[\w\-\.]*\b', query)
        terms.extend(abbreviations)
        
        # 提取标准号模式（如GB/T 12345-2023）
        standard_patterns = re.findall(r'[A-Z]{2,}[\/\s]*[A-Z]*\s*\d+[\.\-]\d+[\-\d]*', query)
        terms.extend(standard_patterns)
        
        return terms
    
    def multi_query_retrieve(self, query: str, k: int = 5) -> List[Dict]:
        """
        多查询检索
        Args:
            query: 查询问题
            k: 每个查询的检索数量
        Returns:
            检索结果列表
        """
        queries = self.enhance_query(query)
        all_results = []
        seen_contents = set()
        
        # 追踪Embedding消耗
        if self.token_tracker:
            self.token_tracker.track_embedding(queries)
        
        for q in queries:
            results = self.vector_store.query(q, self.embedding, k=k)
            for result in results:
                if result not in seen_contents:
                    seen_contents.add(result)
                    all_results.append({
                        'content': result,
                        'query': q,
                        'relevance': 1.0
                    })
        
        return all_results[:k*2]  # 限制总数
    
    def rerank_results(self, query: str, results: List[Dict]) -> List[Dict]:
        """
        重排序检索结果
        Args:
            query: 原始查询
            results: 检索结果
        Returns:
            重排序后的结果
        """
        query_keywords = set(query.lower().split())
        
        for result in results:
            content_lower = result['content'].lower()
            match_count = sum(1 for keyword in query_keywords if keyword in content_lower)
            result['relevance'] = match_count / len(query_keywords) if query_keywords else 0
        
        results.sort(key=lambda x: x['relevance'], reverse=True)
        return results
    
    def basic_retrieve(self, query: str, reasoning_chain: ReasoningChain) -> Tuple[List[Dict], str]:
        """
        基础检索策略
        Args:
            query: 查询问题
            reasoning_chain: 推理链
        Returns:
            (检索结果, 上下文文本)
        """
        # 记录推理步骤
        reasoning_chain.add_analysis_step(
            "识别为基础题，使用精确检索策略",
            f"检索数量: k=3"
        )
        
        results = self.multi_query_retrieve(query, k=3)
        results = self.rerank_results(query, results)
        
        reasoning_chain.add_retrieval_step(
            f"检索到{len(results)}个相关文档片段",
            f"来源查询: {len(self.enhance_query(query))}个"
        )
        
        context = "\n\n---\n\n".join([f"[文档片段 {i+1}]\n{r['content']}" 
                                       for i, r in enumerate(results)])
        
        return results, context
    
    def intermediate_retrieve(self, query: str, reasoning_chain: ReasoningChain) -> Tuple[List[Dict], str]:
        """
        中级检索策略
        Args:
            query: 查询问题
            reasoning_chain: 推理链
        Returns:
            (检索结果, 上下文文本)
        """
        reasoning_chain.add_analysis_step(
            "识别为中级题，需要综合多个文档片段",
            f"检索数量: k=8"
        )
        
        results = self.multi_query_retrieve(query, k=8)
        results = self.rerank_results(query, results)
        
        reasoning_chain.add_retrieval_step(
            f"检索到{len(results)}个文档片段，进行综合分析",
            f"重排序后保留前{min(len(results), 8)}个最相关片段"
        )
        
        context = "\n\n---\n\n".join([f"[文档片段 {i+1}]\n{r['content']}" 
                                       for i, r in enumerate(results)])
        
        return results, context
    
    def advanced_retrieve(self, query: str, reasoning_chain: ReasoningChain) -> Tuple[List[Dict], str]:
        """
        高级检索策略（支持多轮检索和版本对比）
        Args:
            query: 查询问题
            reasoning_chain: 推理链
        Returns:
            (检索结果, 上下文文本)
        """
        reasoning_chain.add_analysis_step(
            "识别为高级题，使用多轮检索和跨文档分析",
            f"检索数量: k=10, 支持版本对比"
        )
        
        # 第一轮：广泛检索
        results_r1 = self.multi_query_retrieve(query, k=10)
        results_r1 = self.rerank_results(query, results_r1)
        
        reasoning_chain.add_retrieval_step(
            f"第一轮检索完成，获得{len(results_r1)}个文档片段",
            f"覆盖多个文档源"
        )
        
        # 检测是否为版本对比问题
        if self._is_version_comparison(query):
            reasoning_chain.add_step(
                "对比",
                "检测到版本对比需求，提取版本信息",
                "尝试识别不同版本的文档"
            )
            
            # 尝试提取版本信息
            version_docs = self._extract_version_documents(results_r1)
            if len(version_docs) >= 2:
                reasoning_chain.add_step(
                    "对比",
                    f"找到{len(version_docs)}个版本的文档",
                    "准备进行版本差异分析"
                )
        
        # 构建结构化上下文
        context = self._build_structured_context(results_r1[:10], query)
        
        return results_r1[:10], context
    
    def _is_version_comparison(self, query: str) -> bool:
        """判断是否为版本对比问题"""
        comparison_keywords = ['对比', '比较', '差异', '演变', 'baseline', '版本']
        return any(kw in query.lower() for kw in comparison_keywords)
    
    def _extract_version_documents(self, results: List[Dict]) -> List[Dict]:
        """从检索结果中提取不同版本的文档"""
        version_docs = []
        seen_versions = set()
        
        for result in results:
            content = result['content']
            # 提取版本信息
            version_info = self.version_comparator.extract_version_info(content)
            
            version_key = version_info.get('version_number') or version_info.get('baseline')
            if version_key and version_key not in seen_versions:
                seen_versions.add(version_key)
                version_docs.append({
                    'version': version_key,
                    'content': content,
                    'info': version_info
                })
        
        return version_docs
    
    def _build_structured_context(self, results: List[Dict], query: str) -> str:
        """构建结构化上下文"""
        context_parts = []
        context_parts.append("=== 检索到的相关文档 ===\n")
        
        for i, result in enumerate(results):
            context_parts.append(f"\n【文档片段 {i+1}】")
            context_parts.append(result['content'])
            context_parts.append("")
        
        return "\n".join(context_parts)
    
    def generate_answer_with_reasoning(self, query: str, context: str, 
                                       query_type: str, reasoning_chain: ReasoningChain) -> str:
        """
        生成答案（带推理链记录）
        Args:
            query: 问题
            context: 上下文
            query_type: 问题类型
            reasoning_chain: 推理链
        Returns:
            生成的答案
        """
        # 优化上下文长度
        if self.token_tracker:
            original_len = len(context)
            context = self.token_tracker.optimize_context(context, max_tokens=3000)
            
            if len(context) < original_len:
                reasoning_chain.add_step(
                    "优化",
                    f"上下文过长，优化至{self.token_tracker.count_tokens(context)} tokens",
                    f"原始: {original_len}字符 -> 优化后: {len(context)}字符"
                )
        
        # 追踪检索上下文消耗
        if self.token_tracker:
            self.token_tracker.track_retrieval(context)
        
        # 构建提示词
        prompt = self._build_prompt(query, context, query_type)
        
        reasoning_chain.add_step(
            "生成",
            f"使用{query_type}题型的提示词模板生成答案",
            f"提示词长度: {len(prompt)}字符"
        )
        
        # 调用LLM生成答案
        answer = self.llm.chat(prompt, [], context)
        
        # 追踪LLM消耗
        if self.token_tracker:
            token_usage = self.token_tracker.track_llm(prompt, answer)
            reasoning_chain.add_step(
                "统计",
                f"Token消耗: 输入{token_usage['input']}, 输出{token_usage['output']}",
                f"总计: {token_usage['total']} tokens"
            )
        
        return answer
    
    def _build_prompt(self, query: str, context: str, query_type: str) -> str:
        """构建提示词"""
        prompts = {
            'basic': """请基于以下文档内容，准确回答问题。

问题：{query}

要求：
1. 直接从文档中提取准确答案
2. 如果是数字、日期、名称，必须完全准确
3. 不要添加文档中没有的信息
4. 回答简洁准确

请基于上述文档回答：""",
            
            'intermediate': """请综合分析以下多个文档片段，完整回答问题。

问题：{query}

要求：
1. 综合多个片段的信息
2. 如需排序或对比，仔细分析所有数据
3. 完整列出所有相关内容
4. 保持答案结构化

请基于上述文档详细回答：""",
            
            'advanced': """请深入分析以下文档，进行跨文档推理和对比。

问题：{query}

要求：
1. 识别不同文档/版本间的关键差异
2. 进行逻辑推理和演变分析
3. 明确指出信息来源
4. 结构化呈现对比结果
5. 提供清晰的推理过程

请基于上述文档进行深入分析："""
        }
        
        template = prompts.get(query_type, prompts['basic'])
        return template.format(query=query)
    
    def check_answer_quality(self, answer: str, query: str) -> bool:
        """
        检查答案质量
        Args:
            answer: 生成的答案
            query: 原始问题
        Returns:
            质量是否合格
        """
        # 检查长度
        if not answer or len(answer.strip()) < 10:
            return False
        
        # 检查否定词
        negative_phrases = ['不知道', '未找到', '无法回答', '没有找到', '数据库中没有']
        if any(phrase in answer for phrase in negative_phrases):
            return False
        
        return True
    
    def query_with_full_features(self, query: str, max_retries: int = 2) -> Dict:
        """
        完整功能的查询（集成所有增强特性）
        Args:
            query: 用户问题
            max_retries: 最大重试次数
        Returns:
            完整的查询结果
        """
        self.query_count += 1
        
        # 创建推理链
        reasoning_chain = ReasoningChain(query)
        self.current_reasoning_chain = reasoning_chain
        
        # 分析问题类型
        query_type = self.analyze_query_type(query)
        reasoning_chain.add_analysis_step(
            f"问题分类为{query_type}类型",
            f"关键特征: {self.extract_technical_terms(query)}"
        )
        
        # 尝试生成答案
        for attempt in range(max_retries):
            # 选择检索策略
            if query_type == 'basic':
                results, context = self.basic_retrieve(query, reasoning_chain)
            elif query_type == 'intermediate':
                results, context = self.intermediate_retrieve(query, reasoning_chain)
            else:  # advanced
                results, context = self.advanced_retrieve(query, reasoning_chain)
            
            # 生成答案
            answer = self.generate_answer_with_reasoning(
                query, context, query_type, reasoning_chain
            )
            
            # 质量检查
            if self.check_answer_quality(answer, query):
                reasoning_chain.add_verification_step(
                    "答案质量检查通过",
                    f"答案长度: {len(answer)}字符"
                )
                reasoning_chain.set_final_answer(answer)
                break
            else:
                # 质量不够，升级策略
                reasoning_chain.add_step(
                    "重试",
                    f"第{attempt+1}次尝试质量不够，升级检索策略",
                    "增加检索范围和深度",
                    confidence=0.5
                )
                query_type = 'advanced'
        
        reasoning_chain.add_conclusion_step(
            f"查询完成，共{len(reasoning_chain.steps)}个推理步骤"
        )
        
        # 记录日志
        if self.token_tracker:
            self.token_tracker.log_query(
                query, answer, query_type, len(results),
                self.token_tracker.usage
            )
        
        return {
            'query': query,
            'query_type': query_type,
            'answer': answer,
            'results': results,
            'reasoning_chain': reasoning_chain,
            'token_usage': self.token_tracker.get_summary() if self.token_tracker else None,
            'attempt': attempt + 1
        }
    
    # 文件: enhanced_agent.py (在 EnhancedRAGAgent 类内部)

    def format_output(self, result: Dict, include_reasoning: bool = False) -> Dict:
        """
        格式化输出（完全符合示例模板.json的要求）
        Args:
            result: 查询结果 (包含 'query', 'answer', 'results')
            include_reasoning: 是否包含推理链（模板不要求，但调试有用）
        Returns:
            格式化的输出
        """
        
        # 1. 提取纯文本列表，符合 "retrieved_contexts": [ "内容1", "内容2" ] 的要求
        # 限制最多返回 OUTPUT_CONFIG['max_retrieval_results'] (默认为 10)
        context_list = [r['content'] for r in result['results'][:10]] 
        
        output = {
            "question": result['query'],        # 字段名修正：'query' -> 'question'
            "retrieved_contexts": context_list, # 字段名修正：'result' -> 'retrieved_contexts'
            "answer": result['answer']
        }
        
        # 可选：包含推理链和token统计（不属于模板要求，但有助于内部调试）
        if include_reasoning and result.get('reasoning_chain'):
            output["reasoning"] = result['reasoning_chain'].to_dict()
        if result.get('token_usage'):
            output["token_usage"] = result['token_usage']
            
        return output
    
    def get_performance_report(self) -> str:
        """获取性能报告"""
        report = []
        
        report.append("╔══════════════════════════════════════════════════════╗")
        report.append("║           智能体性能报告                             ║")
        report.append("╚══════════════════════════════════════════════════════╝")
        report.append("")
        report.append(f"【查询统计】")
        report.append(f"  • 总查询数: {self.query_count}")
        report.append("")
        
        if self.token_tracker:
            report.append(self.token_tracker.get_report())
        
        return "\n".join(report)
    
    def save_reports(self, output_dir: str = "reports"):
        """保存所有报告"""
        import os
        os.makedirs(output_dir, exist_ok=True)
        
        # 保存Token使用报告
        if self.token_tracker:
            self.token_tracker.save_report(
                os.path.join(output_dir, "token_usage.json")
            )
        
        # 保存性能报告
        with open(os.path.join(output_dir, "performance_report.txt"), 'w', encoding='utf-8') as f:
            f.write(self.get_performance_report())
        
        print(f"✅ 报告已保存到: {output_dir}")


if __name__ == "__main__":
    # 测试代码
    print("=== 增强版智能体测试 ===\n")
    
    # 注意：实际使用时需要先加载向量数据库
    print("提示：这是一个示例框架")
    print("实际使用需要:")
    print("1. 加载向量数据库")
    print("2. 初始化LLM和Embedding模型")
    print("3. 创建EnhancedRAGAgent实例")
    print("4. 调用query_with_full_features()方法")

