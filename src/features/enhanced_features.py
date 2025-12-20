#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
增强功能模块
================
这个文件包含可选的增强功能，用于提升RAG系统的性能
参考了casco项目的优秀设计

可选的增强方向：
1. 多查询检索（Multi-Query）
2. 重排序（Rerank）
3. 混合检索（BM25 + 向量检索）
4. Token追踪和优化
"""

import re
from typing import List, Dict, Tuple
from collections import Counter


class QueryEnhancer:
    """查询增强器：生成多个检索查询以提高召回率"""
    
    @staticmethod
    def enhance_query(query: str) -> List[str]:
        """
        从原始查询生成多个检索查询
        
        策略：
        1. 原始查询
        2. 提取的专业术语
        3. 提取的关键词
        """
        queries = [query]
        
        # 提取专业术语（大写缩写，如NLP, RAG等）
        abbreviations = re.findall(r'\b[A-Z]{2,}[\w\-]*\b', query)
        queries.extend(abbreviations)
        
        # 提取数字和日期
        numbers = re.findall(r'\b\d+\b', query)
        queries.extend(numbers)
        
        # 去重
        return list(set(queries))
    
    @staticmethod
    def extract_keywords(query: str, top_k: int = 3) -> List[str]:
        """提取关键词（简单的基于长度和频率）"""
        # 简单分词（按空格和标点）
        words = re.findall(r'\b\w+\b', query)
        
        # 过滤停用词（简化版）
        stopwords = {'的', '了', '是', '在', '有', '和', '就', '不', '人', '都', '一', '什么', '为什么', '怎么'}
        words = [w for w in words if w not in stopwords and len(w) > 1]
        
        # 按长度排序（长词通常更重要）
        words.sort(key=len, reverse=True)
        
        return words[:top_k]


class ResultReranker:
    """结果重排序器：基于关键词匹配度重新排序检索结果"""
    
    @staticmethod
    def rerank_by_keyword_match(query: str, results: List[Dict]) -> List[Dict]:
        """
        基于关键词匹配度重新排序
        
        参数:
            query: 原始查询
            results: 检索结果列表
            
        返回:
            重排序后的结果
        """
        # 提取查询关键词
        query_keywords = set(re.findall(r'\b\w+\b', query.lower()))
        
        # 计算每个结果的匹配分数
        for result in results:
            content = result['content'].lower()
            
            # 计算关键词匹配数
            match_count = sum(1 for kw in query_keywords if kw in content)
            
            # 计算匹配率
            match_ratio = match_count / len(query_keywords) if query_keywords else 0
            
            # 原始距离分数（越小越好）
            original_score = result.get('distance', 1.0)
            
            # 综合分数：距离分数 * 0.6 + 匹配分数 * 0.4
            result['rerank_score'] = original_score * 0.6 - match_ratio * 0.4
        
        # 按综合分数排序（分数越小越好）
        results.sort(key=lambda x: x.get('rerank_score', 1.0))
        
        return results


class TokenCounter:
    """Token计数器：追踪和优化Token使用"""
    
    def __init__(self):
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.query_count = 0
    
    def estimate_tokens(self, text: str) -> int:
        """
        估算文本的token数量
        简化版：中文约1.5字符/token，英文约4字符/token
        """
        chinese_chars = sum(1 for c in text if '\u4e00' <= c <= '\u9fff')
        other_chars = len(text) - chinese_chars
        
        estimated = int(chinese_chars / 1.5 + other_chars / 4)
        return estimated
    
    def track_query(self, prompt: str, response: str):
        """追踪一次查询的token消耗"""
        input_tokens = self.estimate_tokens(prompt)
        output_tokens = self.estimate_tokens(response)
        
        self.total_input_tokens += input_tokens
        self.total_output_tokens += output_tokens
        self.query_count += 1
    
    def get_summary(self) -> Dict:
        """获取统计摘要"""
        return {
            'total_input_tokens': self.total_input_tokens,
            'total_output_tokens': self.total_output_tokens,
            'total_tokens': self.total_input_tokens + self.total_output_tokens,
            'query_count': self.query_count,
            'avg_tokens_per_query': (self.total_input_tokens + self.total_output_tokens) / max(1, self.query_count)
        }
    
    def print_summary(self):
        """打印统计摘要"""
        summary = self.get_summary()
        print("\n" + "="*50)
        print("Token使用统计")
        print("="*50)
        print(f"总查询次数: {summary['query_count']}")
        print(f"总输入tokens: {summary['total_input_tokens']:,}")
        print(f"总输出tokens: {summary['total_output_tokens']:,}")
        print(f"总tokens: {summary['total_tokens']:,}")
        print(f"平均每次查询: {summary['avg_tokens_per_query']:.0f} tokens")
        print("="*50)


class HybridRetriever:
    """混合检索器：结合BM25和向量检索（概念示例）"""
    
    def __init__(self):
        """
        混合检索的思路：
        1. BM25（稀疏检索）：基于关键词匹配
        2. 向量检索（密集检索）：基于语义相似度
        3. 融合两种结果
        
        实现需要额外的库：rank_bm25
        """
        pass
    
    @staticmethod
    def simple_bm25_score(query: str, document: str) -> float:
        """
        简化的BM25评分（仅作演示）
        真实实现需要使用rank_bm25库
        """
        query_words = set(query.lower().split())
        doc_words = document.lower().split()
        
        # 简单的TF计数
        tf_scores = []
        for qw in query_words:
            count = doc_words.count(qw)
            if count > 0:
                tf_scores.append(count)
        
        return sum(tf_scores) / (len(doc_words) + 1)


# 使用示例
if __name__ == "__main__":
    print("增强功能模块示例\n")
    
    # 1. 查询增强
    print("【1. 多查询增强】")
    enhancer = QueryEnhancer()
    query = "什么是NLP中的词向量表示？"
    enhanced_queries = enhancer.enhance_query(query)
    print(f"原始查询: {query}")
    print(f"增强查询: {enhanced_queries}\n")
    
    # 2. 关键词提取
    print("【2. 关键词提取】")
    keywords = enhancer.extract_keywords(query)
    print(f"提取的关键词: {keywords}\n")
    
    # 3. Token追踪
    print("【3. Token追踪】")
    tracker = TokenCounter()
    tracker.track_query("这是一个测试问题", "这是一个测试回答")
    tracker.print_summary()
    
    print("\n💡 提示：这些增强功能可以选择性地集成到rag_agent.py中")

