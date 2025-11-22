#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   enhanced_agent.py
@Time    :   2025/11/16
@Desc    :   增强版智能体 - 集成Token追踪、推理链、高级文档处理
'''

import json
import re
from typing import List, Dict, Tuple, Optional,Union, Any
from VectorBase import VectorStore
from LLM import OpenAIChat
from Embeddings import OpenAIEmbedding
from token_tracker import TokenTracker, TokenOptimizer
from reasoning_chain import ReasoningChain
from advanced_document_processor import VersionComparator, AdvancedTableExtractor
import os
from LLM import OpenAIChat
from auto_cot_prompting import AutoCotPromptBuilder

PROMPT_TEMPLATES = {
    'basic': """请基于以下文档内容，准确回答问题。总是使用中文回答。

文档内容：{context}

问题：{query}

要求：
1. 直接从文档中提取准确答案
2. 如果是数字、日期、名称，必须完全准确
3. 不要添加文档中没有的信息
4. 回答简洁准确

请基于上述文档回答：""",
    
    'intermediate': """请综合分析以下多个文档片段，完整回答问题。总是使用中文回答。

文档内容：{context}

问题：{query}

要求：
1. 综合多个片段的信息
2. 如需排序或对比，仔细分析所有数据
3. 完整列出所有相关内容
4. 保持答案结构化

请基于上述文档详细回答：""",
    
    'advanced': """请深入分析以下文档，进行跨文档推理和对比。总是使用中文回答。

文档内容：{context}

问题：{query}

要求：
1. 识别不同文档/版本间的关键差异
2. 进行逻辑推理和演变分析
3. 明确指出信息来源
4. 结构化呈现对比结果
5. 提供清晰的推理过程

请基于上述文档进行深入分析：""",

    'default': """请基于以下文档内容，回答问题。总是使用中文回答。

文档内容：{context}

问题：{query}

要求：
1. 直接从文档中提取准确答案
2. 如果是数字、日期、名称，必须完全准确
3. 不要添加文档中没有的信息
4. 回答简洁准确

请基于上述文档回答："""
  
}
class QuestionDifficultyClassifier:
    """
    基于规则的问题难度分类器
    通过分析问题的语言特征来判断难度等级
    """
    
    def __init__(self):
        # ==================== 高级题特征（优先级最高）====================
        # 特征：需要结合多个文档进行回答、跨文档对比、演变追溯、跨规范体系
        self.advanced_patterns = [
            # 版本对比类
            r'比较.*版本',
            r'对比.*版本',
            r'比较.*Baseline',
            r'Baseline\s*\d+.*Baseline\s*\d+',  # 如 "Baseline 3 和 Baseline 4"
            r'v\d+\.\d+.*v\d+\.\d+',  # 如 "v3.4.0 和 v4.0.0"
            r'版本.*差异',
            r'版本.*变化',
            
            # 演变追溯类
            r'演变',
            r'追溯',
            r'发展.*过程',
            r'历史.*变化',
            
            # 多文档引用类
            r'《[^》]+》.*《[^》]+》',  # 两个或以上书名号
            r'在《[^》]+》.*在《[^》]+》',  # "在《文档A》...在《文档B》..."
            r'在.*中.*[，。].*并.*在.*中',  # "在A中...并在B中..."
            r'在.*[规范|标准|文档|报告].*在.*[规范|标准|文档|报告]',
            
            # 跨规范体系类
            r'分配归属.*并.*体现',
            r'在.*系统.*在.*测试',
            r'归属于.*体现在',
            
            # 差异对比类
            r'差异',
            r'不同.*之间',
            r'区别.*与',
            r'对比.*定义',
            r'比较.*内容',
            
            # 多文档综合分析
            r'结合.*和.*',  # 需要结合多个来源
            r'综合.*多个',
        ]
        
        # ==================== 中级题特征 ====================
        # 特征：在一个文档中的多个位置，结合检索结果，综合回答
        self.intermediate_patterns = [
            # 排名对比类（需要在单文档内对比多个数据）
            r'排第几',
            r'排名',
            r'排序',
            r'位列第',
            r'居第',
            r'在.*中.*排',
            
            # 完整列举类（需要汇总多处信息）
            r'完整列出',
            r'完整列举',
            r'全部列出',
            r'所有.*分别',
            r'都有哪些',
            r'包括哪些',
            r'有哪几',
            
            # 多层级结构类（需要理解并提取多层信息）
            r'第\s*\d+\s*层.*第\s*\d+\s*层',  # "第2层...第3层"
            r'第[一二三四五]层.*第[一二三四五]层',
            r'层级.*结构',
            r'分层.*定义',
            
            # 过程阐述类（需要综合多个步骤）
            r'如何实现',
            r'如何.*的',
            r'怎样.*实现',
            r'请阐述.*如何',
            r'描述.*过程',
            r'说明.*方式',
            
            # 多方面综合类
            r'请阐述.*以及',
            r'如何.*以及.*如何',
            r'.*和.*分别',
            r'需.*完整',
            r'详细说明',
            r'具体阐述',
            
            # 关系分析类（单文档内多个实体关系）
            r'之间.*关系',
            r'相互.*作用',
            r'如何.*传递',
            r'从.*到',
        ]
        
        # ==================== 基础题特征 ====================
        # 特征：直接能在给定的材料中检索出结果，考察"大海捞针"的能力
        self.basic_patterns = [
            # 数值查询类（单一数值）
            r'^[^？?]*是多少[？?]?$',
            r'金额是多少',
            r'数量是多少',
            r'里程.*多少',
            r'长度.*多少',
            r'达到多少',
            r'百分比',
            r'百分之',
            r'占.*比',
            
            # 时间日期类（单一时间点）
            r'何时.*发生',
            r'什么时候',
            r'日期.*时间',
            r'在.*年',
            r'哪一天',
            r'^.*年.*月.*日',
            
            # 状态描述类（单一状态）
            r'处于什么状态',
            r'被假定.*什么状态',
            r'状态是',
            r'被定义为',
            r'被描述为',
            
            # 定义查询类（单一定义）
            r'^.*的定义是',
            r'^什么是',
            r'^.*是什么',
            r'定义.*为',
            r'含义是',
            
            # 单一属性查询类
            r'^根据.*是多少',
            r'^根据.*达到多少',
            r'目标进度.*应达到',
            r'标准是',
            r'要求是',
            r'规定.*为',
            
            # 事实查询类（直接检索可得）
            r'^.*有多少',
            r'名称是',
            r'编号是',
            r'型号是',
            r'代号是',
            r'简称是',
        ]
        
        # 文档数量判断关键词（用于辅助判断）
        self.multi_doc_keywords = [
            '比较', '对比', '演变', '版本', 'baseline', 'Baseline',
            '分别', '不同文档', '多个文档', '差异', '变化',
            '归属于', '体现在', '规范体系'
        ]
        
        # 单文档多位置关键词
        self.multi_position_keywords = [
            '排名', '排第几', '完整列出', '所有', '如何实现',
            '阐述', '层级', '分别是', '详细说明'
        ]
        
        # 单一事实关键词
        self.single_fact_keywords = [
            '是多少', '何时', '什么状态', '定义', '是什么',
            '金额', '数量', '日期', '时间'
        ]
    
    def classify(self, question: str) -> str:
        """
        分类问题难度
        Args:
            question: 待分类的问题
        Returns:
            难度等级: 'basic', 'intermediate', 'advanced'
        """
        
        # 1. 首先检查高级题特征（优先级最高）
        for pattern in self.advanced_patterns:
            if re.search(pattern, question, re.IGNORECASE):
                return 'advanced'
        
        # 2. 检查中级题特征
        intermediate_score = 0
        for pattern in self.intermediate_patterns:
            if re.search(pattern, question):
                return 'intermediate'
        
        return 'basic'
    
    def classify_with_details(self, question: str) -> Dict[str, Any]:
        """
        返回分类及详细信息
        Args:
            question: 待分类的问题
        Returns:
            包含分类、置信度、匹配特征等信息的字典
        """
        classification = self.classify(question)
        
        # 统计各类特征匹配数
        advanced_matches = sum(1 for p in self.advanced_patterns if re.search(p, question, re.IGNORECASE))
        intermediate_matches = sum(1 for p in self.intermediate_patterns if re.search(p, question))
        basic_matches = sum(1 for p in self.basic_patterns if re.search(p, question))
        
        # 计算置信度
        if classification == 'advanced':
            confidence = min(0.7 + advanced_matches * 0.1, 0.95)
        elif classification == 'intermediate':
            confidence = min(0.6 + intermediate_matches * 0.15, 0.9)
        else:
            confidence = 0.5 if basic_matches == 0 else min(0.6 + basic_matches * 0.1, 0.85)
        
        # 提取匹配的特征
        matched_features = []
        if advanced_matches > 0:
            matched_features.append(f"高级特征: {advanced_matches}个")
        if intermediate_matches > 0:
            matched_features.append(f"中级特征: {intermediate_matches}个")
        if basic_matches > 0:
            matched_features.append(f"基础特征: {basic_matches}个")
        
        return {
            'difficulty': classification,
            'confidence': confidence,
            'advanced_matches': advanced_matches,
            'intermediate_matches': intermediate_matches,
            'basic_matches': basic_matches,
            'matched_features': matched_features,
            'reasoning': self._get_reasoning(classification, question)
        }
    
    
    



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
        
        # self.classifier_mode = classifier_mode
        self.question_classifier = QuestionDifficultyClassifier()
        # if classifier_mode == 'rule':
        #     self.question_classifier = QuestionDifficultyClassifier()
        # elif classifier_mode == 'llm':
        #     self.question_classifier = LLMQuestionClassifier(llm)
        # else:  # hybrid (default)
        #     self.question_classifier = HybridQuestionClassifier(llm, confidence_threshold=0.7)
        

        # 当前推理链
        self.current_reasoning_chain: Optional[ReasoningChain] = None
        
        # 统计信息
        self.query_count = 0
        self.cache = {}  # 简单的查询缓存
        self.classification_stats = {
            'basic': 0,
            'intermediate': 0,
            'advanced': 0
        }
        self.temp_map = {
            'basic': 0.3,         # 事实提取，要求精确
            'intermediate': 0.5,  # 综合分析，允许轻微推理
            'advanced': 0.7,      # 深度推理/创造性分析，允许更高探索性
            'default': 0.3        # 默认值
        }

        # 加载auto cot示例
        self.auto_cot_prompt_builder = AutoCotPromptBuilder(
            demo_path=os.path.join(os.path.dirname(__file__), "cot", "auto_cot_demos.json")
        )
    
    def analyze_query_type(self, query: str) -> str:
        """
        分析问题类型：基础/中级/高级
        Args:
            query: 用户问题
        Returns:
            问题类型
        """
        return self.question_classifier.classify(query)
    
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
    
    def multi_query_retrieve(self, query: str, k: int = 5) -> List[Dict[str, Union[str, float]]]:
        """
        多查询检索（已集成多语言查询翻译依赖）
        Args:
            query: 查询问题
            k: 每个查询的检索数量
        Returns:
            检索结果列表 (List[Dict] 包含 content, score/relevance, lang 等)
        """
        queries = self.enhance_query(query)
        all_results: List[Dict[str, Union[str, float]]] = []
        seen_contents = set()
        
        # 追踪Embedding消耗
        if self.token_tracker:
            # 追踪的是增强后的所有查询的 embedding 消耗
            self.token_tracker.track_embedding(queries)
        
        for q in queries:
            
            ### 核心修改：集成查询翻译依赖 ###
            # 假设 VectorStore.query 已经修改，可以接受 LLM 类和实例，并在内部执行翻译
            # 同时假设它现在返回 List[Dict]，包含 'content', 'score' 和 'lang' 字段
            results_with_metadata = self.vector_store.query(
                query=q,
                EmbeddingModel=self.embedding,
                llm_translator_class=OpenAIChat, # LLM 类本身 (用于调用静态翻译方法)
                llm_instance=self.llm,          # LLM 实例 (用于执行翻译)
                k=k
            )
            
            for result in results_with_metadata:
                content_key = result['content'] # 用内容作为去重键
                if content_key not in seen_contents:
                    seen_contents.add(content_key)
                    
                    # 重新组装结果，确保格式一致，并包含语言信息
                    all_results.append({
                        'content': result['content'],
                        # 使用 score 作为初始 relevance，后续 rerank 会更新
                        'relevance': result.get('score', 1.0),
                        'lang': result.get('lang', 'unknown'), # 确保包含语言信息
                        'query': q, # 记录是哪个增强查询找到的
                    })
        
        # 原代码中的去重和限制总数逻辑
        return all_results[:k*2] # 限制总数
    
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
    
    def _perform_multi_query_and_lingual_retrieval(self, query: str, k: int) -> List[Dict]:
        """
        统一的检索执行函数：
        1. 生成增强查询 (Multi-Query)。
        2. 对每个查询，调用支持动态翻译的 vector_store.query 进行多语言检索。
        3. 合并和去重结果。
        """
        final_results = [] # ❗ 关键修复：提供默认值

        # 1. 生成增强查询 (Multi-Query)
        # 假设 self.enhance_query(query) 返回一个查询字符串列表
        queries = self.enhance_query(query)
        if not queries:
            queries = [query] # 至少使用原始查询
            
        all_results = []
        
        if self.current_reasoning_chain:
            self.current_reasoning_chain.add_retrieval_step(
                f"检索完成，原始召回 {len(all_results)} 条。", # description
            f"去重后保留 {len(final_results)} 条，进行重排序。"  # evidence
            )

        # 2. 遍历所有生成的查询并进行多语言检索
        for q in queries:
            # ❗ 调用已修改的 vector_store.query，并传入翻译依赖
            results = self.vector_store.query(
                query=q,
                EmbeddingModel=self.embedding,
                k=k,
                llm_translator_class=OpenAIChat, # 传入 LLM 类 (用于调用 translate_query 静态方法)
                llm_instance=self.llm           # 传入 LLM 实例 (用于执行翻译 API 调用)
            )
            all_results.extend(results)
        
        # 3. 结果去重 (基于 content) 和排序 (基于 similarity)
        if all_results: # 只有当有结果时才进行去重和排序
            # 注意：这里使用 content 去重是为了避免不同查询召回相同片段，并保留相似度最高的
            unique_results = {r['content']: r for r in all_results}
            final_results = sorted(
                unique_results.values(), 
                key=lambda x: x.get('similarity', 0.0), 
                reverse=True
            )
        if self.current_reasoning_chain:
            self.current_reasoning_chain.add_retrieval_step(
                f"检索完成，原始召回 {len(all_results)} 条。", # description
            f"去重后保留 {len(final_results)} 条，进行重排序。"  # evidence
            )
            
        return final_results

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
        
        results = self._perform_multi_query_and_lingual_retrieval(query, k=3)
        results = self.rerank_results(query, results)
        langs = set(r.get('lang', 'unknown') for r in results)
        reasoning_chain.add_retrieval_step(
            f"检索到{len(results)}个相关文档片段",
            f"来源查询: {len(self.enhance_query(query))}个, 涉及语言: {', '.join(langs)}"
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
        
        results = self._perform_multi_query_and_lingual_retrieval(query, k=8)
        results = self.rerank_results(query, results)
        langs = set(r.get('lang', 'unknown') for r in results)
        reasoning_chain.add_retrieval_step(
            f"检索到{len(results)}个文档片段，进行综合分析",
            f"重排序后保留前{min(len(results), 8)}个最相关片段, 涉及语言: {', '.join(langs)}"
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
        results_r1 = self._perform_multi_query_and_lingual_retrieval(query, k=10)
        results_r1 = self.rerank_results(query, results_r1)
        langs = set(r.get('lang', 'unknown') for r in results_r1)
        reasoning_chain.add_retrieval_step(
            f"第一轮检索完成，获得{len(results_r1)}个文档片段",
            f"覆盖多个文档源, 涉及语言: {', '.join(langs)}"
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
            lang_info = f" (语言: {result.get('lang', 'unknown')})" if 'lang' in result else ""
            context_parts.append(f"\n【文档片段 {i+1}】{lang_info}")
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
            context = self.token_tracker.optimize_context(context, max_tokens=30000)
            
            if len(context) < original_len:
                reasoning_chain.add_step(
                    "优化",
                    f"上下文过长，优化至{self.token_tracker.count_tokens(context)} tokens",
                    f"原始: {original_len}字符 -> 优化后: {len(context)}字符"
                )
        
        # 追踪检索上下文消耗
        if self.token_tracker:
            self.token_tracker.track_retrieval(context)
        
        # 2. 选择 Prompt 模板
        prompt_template = PROMPT_TEMPLATES.get(query_type, PROMPT_TEMPLATES['default'])
        # prompt = prompt_template.format(context=context, query=query)
        # !!!
        # 若使用cot,替换上一行！！
        if query_type in ['intermediate', 'advanced']:
            prompt = self.auto_cot_prompt_builder.build_prompt(query, context)
            reasoning_chain.add_step(
                "Auto-CoT提示词构造",
                f"注入了 {len(self.auto_cot_prompt_builder.examples)} 个推理示例",
                "启用 few-shot prompting"
            )
        else:
            prompt = prompt_template.format(context=context, query=query)
        # 3. 获取对应的温度
        temperature = self.temp_map.get(query_type, self.temp_map['default'])
        
        reasoning_chain.add_step(
            "生成",
            f"使用{query_type}题型的提示词模板生成答案",
            f"提示词长度: {len(prompt)}字符"
        )
        
        # 4. 调用 LLM 生成答案
        answer = self.llm.chat(
            prompt, 
            [], 
            context,
            temperature=temperature # <-- 传入对应的温度
        )
        
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
        template = PROMPT_TEMPLATES.get(query_type, PROMPT_TEMPLATES['basic'])
        # 模板中同时包含 {query} 和 {context} 占位符
        return template.format(query=query, context=context)
    
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
            'reasoning_chain': str(reasoning_chain) if reasoning_chain else None,  
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
    rule_classifier = QuestionDifficultyClassifier()
    
    test_questions = [
        # 基础题
        "2024 年，株洲中车时代电气股份有限公司中标金额是多少？",
        "根据欧洲铁路局 2025-2027 年单一规划文件，机构注册系统迁移到知识图谱（knowledge graph）方法的目标进度在 2025 年底应达到多少百分比？",
        
        # 中级题
        "南京地铁 S7 号线的运营里程，在江苏省内已运营地铁长度中排第几？",
        "车辆外部移动实体的场景要素：根据 GB/T 43267—2023（预期功能安全），在场景要素结构中，可移动实体的第 2 层要素和第 3 层要素分别是什么？（需完整列出第 3 层中所有实体类型）。",
        
        # 高级题
        "在 CBTC 互联互通规范体系中，关于列车启动、加速、巡航和制动的自动控制功能，其在《系统总体要求》中的分配归属于哪个子系统？并在《CBTC 部分测试及验证》中体现在哪个功能的测试中，测试需求编号是什么？",
        "比较 SUBSET-026 Baseline 3 (v3.4.0) 和 Baseline 4 (v4.0.0) 版本中 Validated Train Data (Packet 11) 的内容定义",
    ]
    difficulty_counts = {'basic': 0, 'intermediate': 0, 'advanced': 0}
    for question in test_questions:
        difficulty = rule_classifier.classify(question)
        difficulty_counts[difficulty] += 1
    print(f"总问题数: {len(test_questions)}")
    print(f"  • 基础题: {difficulty_counts['basic']}")
    print(f"  • 中级题: {difficulty_counts['intermediate']}")
    print(f"  • 高级题: {difficulty_counts['advanced']}")
    
    print("\n" + "=" * 60)
    print("【测试3】实际使用示例")
    print("-" * 60)