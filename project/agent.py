#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   agent.py
@Time    :   2025/11/15
@Desc    :   智能体核心逻辑 - 支持多级推理和跨文档分析
'''

import json
import re
from typing import List, Dict, Tuple
from VectorBase import VectorStore
from LLM import OpenAIChat
from Embeddings import OpenAIEmbedding
import os

class RAGAgent:
    """
    智能体主类，支持多级检索和推理
    """
    def __init__(self, vector_store: VectorStore, llm: OpenAIChat, embedding: OpenAIEmbedding):
        self.vector_store = vector_store
        self.llm = llm
        self.embedding = embedding
        
    def analyze_query_type(self, query: str) -> str:
        """
        分析问题类型：基础/中级/高级
        """
        # 高级题特征：多文档、对比、版本、演变
        advanced_keywords = ['对比', '演变', '版本', '分别', '不同', 'baseline', '变化']
        # 中级题特征：排名、列出、完整、所有
        intermediate_keywords = ['排第几', '排名', '列出', '完整', '所有', '分别是']
        
        for keyword in advanced_keywords:
            if keyword.lower() in query.lower():
                return 'advanced'
        
        for keyword in intermediate_keywords:
            if keyword.lower() in query.lower():
                return 'intermediate'
                
        return 'basic'
    
    def enhance_query(self, query: str) -> List[str]:
        """
        查询增强：生成多个检索查询
        """
        queries = [query]
        
        # 提取关键实体和数字
        # 例如：提取年份、公司名、标准号等
        year_pattern = r'\d{4}'
        years = re.findall(year_pattern, query)
        
        # 为包含年份的查询生成变体
        if years:
            for year in years:
                queries.append(year)
        
        # 提取专业术语
        technical_terms = self.extract_technical_terms(query)
        queries.extend(technical_terms)
        
        return list(set(queries))  # 去重
    
    def extract_technical_terms(self, query: str) -> List[str]:
        """
        提取专业术语
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
        多查询检索：使用增强后的查询进行检索并合并结果
        """
        queries = self.enhance_query(query)
        all_results = []
        seen_contents = set()
        
        for q in queries:
            results = self.vector_store.query(q, self.embedding, k=k)
            for result in results:
                # 去重
                if result not in seen_contents:
                    seen_contents.add(result)
                    all_results.append({
                        'content': result,
                        'query': q,
                        'relevance': 1.0  # 可以后续添加相关性评分
                    })
        
        return all_results[:k*2]  # 返回前k*2个结果
    
    def rerank_results(self, query: str, results: List[Dict]) -> List[Dict]:
        """
        重排序：基于查询和结果的相关性重新排序
        可以使用更复杂的重排序模型，这里使用简单的关键词匹配
        """
        query_keywords = set(query.lower().split())
        
        for result in results:
            content_lower = result['content'].lower()
            # 计算关键词匹配度
            match_count = sum(1 for keyword in query_keywords if keyword in content_lower)
            result['relevance'] = match_count / len(query_keywords) if query_keywords else 0
        
        # 按相关性排序
        results.sort(key=lambda x: x['relevance'], reverse=True)
        return results
    
    def basic_retrieve(self, query: str) -> Tuple[List[Dict], str]:
        """
        基础检索：适用于简单的"大海捞针"问题
        """
        # 使用较少的召回数
        results = self.multi_query_retrieve(query, k=3)
        results = self.rerank_results(query, results)
        
        # 构建上下文
        context = "\n\n---\n\n".join([f"[文档片段 {i+1}]\n{r['content']}" 
                                       for i, r in enumerate(results)])
        
        return results, context
    
    def intermediate_retrieve(self, query: str) -> Tuple[List[Dict], str]:
        """
        中级检索：需要更多上下文和多段落综合
        """
        # 增加召回数量
        results = self.multi_query_retrieve(query, k=8)
        results = self.rerank_results(query, results)
        
        context = "\n\n---\n\n".join([f"[文档片段 {i+1}]\n{r['content']}" 
                                       for i, r in enumerate(results)])
        
        return results, context
    
    def advanced_retrieve(self, query: str) -> Tuple[List[Dict], str]:
        """
        高级检索：支持多轮检索和跨文档分析
        """
        # 第一轮：广泛检索
        results_round1 = self.multi_query_retrieve(query, k=10)
        results_round1 = self.rerank_results(query, results_round1)
        
        # 第二轮：基于第一轮结果提取关键信息，进行细化检索
        # 可以通过LLM提取第一轮结果中的关键实体，然后进行第二轮检索
        top_results = results_round1[:5]
        
        # 构建分层上下文
        context = self.build_structured_context(top_results, query)
        
        return top_results, context
    
    def build_structured_context(self, results: List[Dict], query: str) -> str:
        """
        构建结构化上下文，特别适合对比和演变分析
        """
        context_parts = []
        context_parts.append("=== 检索到的相关文档片段 ===\n")
        
        for i, result in enumerate(results):
            context_parts.append(f"\n【片段 {i+1}】")
            context_parts.append(result['content'])
            context_parts.append("\n")
        
        return "\n".join(context_parts)
    
    def generate_answer(self, query: str, context: str, query_type: str) -> str:
        """
        根据问题类型生成答案
        """
        # 根据不同类型使用不同的提示词
        if query_type == 'basic':
            prompt = self.get_basic_prompt(query, context)
        elif query_type == 'intermediate':
            prompt = self.get_intermediate_prompt(query, context)
        else:  # advanced
            prompt = self.get_advanced_prompt(query, context)
        
        answer = self.llm.chat(prompt, [], context)
        return answer
    
    def get_basic_prompt(self, query: str, context: str) -> str:
        """基础题提示词"""
        return f"""请仔细阅读以下文档内容，准确回答问题。

问题：{query}

要求：
1. 直接从文档中提取准确的答案
2. 如果答案是数字、日期或具体名称，请确保完全准确
3. 如果文档中没有明确答案，请说明"文档中未找到相关信息"
4. 回答要简洁准确，不要添加额外解释

请基于上述文档内容回答问题。"""
    
    def get_intermediate_prompt(self, query: str, context: str) -> str:
        """中级题提示词"""
        return f"""请仔细分析以下多个文档片段，综合回答问题。

问题：{query}

要求：
1. 需要综合多个片段中的信息
2. 如果需要排序或对比，请仔细分析所有相关数据
3. 完整列出所有要求的内容，不要遗漏
4. 保持答案的结构化和条理性
5. 如果信息不完整，请说明缺少哪些关键信息

请基于上述文档内容详细回答问题。"""
    
    def get_advanced_prompt(self, query: str, context: str) -> str:
        """高级题提示词"""
        return f"""请深入分析以下文档，进行跨文档的对比和推理。

问题：{query}

要求：
1. 识别不同文档或版本之间的关键差异
2. 进行逻辑推理和演变分析
3. 如果涉及多个标准或版本，请明确指出来源
4. 结构化呈现对比结果
5. 提供清晰的推理过程

请基于上述文档内容进行深入分析并回答。"""
    
    def query_with_retry(self, query: str, max_retries: int = 2) -> Dict:
        """
        带重试机制的查询，如果第一次答案质量不高，可以调整策略重试
        """
        query_type = self.analyze_query_type(query)
        
        for attempt in range(max_retries):
            # 根据类型选择检索策略
            if query_type == 'basic':
                results, context = self.basic_retrieve(query)
            elif query_type == 'intermediate':
                results, context = self.intermediate_retrieve(query)
            else:
                results, context = self.advanced_retrieve(query)
            
            # 生成答案
            answer = self.generate_answer(query, context, query_type)
            
            # 简单的答案质量检查
            if self.check_answer_quality(answer, query):
                return {
                    'query': query,
                    'query_type': query_type,
                    'results': results,
                    'answer': answer,
                    'attempt': attempt + 1
                }
            
            # 如果质量不够，下一轮增加召回数量
            if attempt < max_retries - 1:
                query_type = 'advanced'  # 升级为高级检索
        
        # 返回最后一次尝试的结果
        return {
            'query': query,
            'query_type': query_type,
            'results': results,
            'answer': answer,
            'attempt': max_retries
        }
    
    def check_answer_quality(self, answer: str, query: str) -> bool:
        """
        简单的答案质量检查
        """
        # 检查是否为空或过短
        if not answer or len(answer.strip()) < 10:
            return False
        
        # 检查是否包含"不知道"、"未找到"等否定词
        negative_phrases = ['不知道', '未找到', '没有找到', '无法回答', '数据库中没有']
        if any(phrase in answer for phrase in negative_phrases):
            return False
        
        return True
    
    def format_output(self, result: Dict) -> Dict:
        """
        格式化输出，符合示例模板要求
        """
        output = {
            "query": result['query']
        }
        
        # 格式化召回结果
        formatted_results = []
        for i, r in enumerate(result['results'][:10]):  # 最多返回10个结果
            formatted_results.append({
                "position": i + 1,
                "content": r['content']
            })
        
        output["result"] = formatted_results
        output["answer"] = result['answer']
        
        return output


def run_agent_on_query(query: str, vector_store_path: str = 'storage') -> Dict:
    """
    运行智能体处理单个问题
    """
    # 加载向量数据库
    vector_store = VectorStore()
    vector_store.load_vector(vector_store_path)
    
    # 初始化模型
    embedding = OpenAIEmbedding()
    llm = OpenAIChat()
    
    # 创建智能体
    agent = RAGAgent(vector_store, llm, embedding)
    
    # 执行查询
    result = agent.query_with_retry(query)
    
    # 格式化输出
    output = agent.format_output(result)
    
    return output


if __name__ == "__main__":
    # 测试示例
    query = "2024 年，株洲中车时代电气股份有限公司中标金额是多少？"
    
    result = run_agent_on_query(query)
    
    # 打印结果
    print(json.dumps(result, ensure_ascii=False, indent=2))

