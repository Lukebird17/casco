#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
置信度计算器
计算答案的置信度分数
"""

from typing import List, Dict, Tuple
import re


class ConfidenceCalculator:
    """置信度计算器"""
    
    # 置信度等级
    LEVELS = [
        {"name": "极高", "min": 0.85, "color": "#10B981", "emoji": "🟢"},
        {"name": "高", "min": 0.70, "color": "#3B82F6", "emoji": "🔵"},
        {"name": "中", "min": 0.50, "color": "#F59E0B", "emoji": "🟡"},
        {"name": "低", "min": 0.30, "color": "#EF4444", "emoji": "🔴"},
        {"name": "极低", "min": 0.0, "color": "#7F1D1D", "emoji": "⚫"},
    ]
    
    def __init__(self):
        pass
    
    def calculate(
        self, 
        query: str,
        answer: str,
        retrieved_docs: List[Dict],
        query_type: str = "basic"
    ) -> Dict:
        """
        计算置信度
        
        Args:
            query: 用户问题
            answer: 生成的答案
            retrieved_docs: 检索到的文档
            query_type: 问题类型
            
        Returns:
            {
                "score": 0.85,  # 0-1之间
                "level": "极高",
                "color": "#10B981",
                "emoji": "🟢",
                "factors": {
                    "retrieval_quality": 0.9,
                    "answer_completeness": 0.8,
                    "source_reliability": 0.85,
                    "consistency": 0.9
                },
                "explanation": "检索质量excellent，答案完整..."
            }
        """
        # 1. 检索质量 (0-1)
        retrieval_score = self._calculate_retrieval_quality(query, retrieved_docs)
        
        # 2. 答案完整性 (0-1)
        completeness_score = self._calculate_answer_completeness(answer)
        
        # 3. 来源可靠性 (0-1)
        reliability_score = self._calculate_source_reliability(retrieved_docs)
        
        # 4. 一致性 (0-1)
        consistency_score = self._calculate_consistency(answer, retrieved_docs)
        
        # 加权计算总分
        weights = {
            "retrieval_quality": 0.35,
            "answer_completeness": 0.25,
            "source_reliability": 0.20,
            "consistency": 0.20
        }
        
        total_score = (
            retrieval_score * weights["retrieval_quality"] +
            completeness_score * weights["answer_completeness"] +
            reliability_score * weights["source_reliability"] +
            consistency_score * weights["consistency"]
        )
        
        # 根据问题类型调整
        if query_type == "advanced":
            total_score *= 0.9  # 复杂问题降低置信度
        
        # 确定等级
        level_info = self._get_level(total_score)
        
        # 生成解释
        explanation = self._generate_explanation(
            retrieval_score, completeness_score, 
            reliability_score, consistency_score
        )
        
        return {
            "score": round(total_score, 3),
            "level": level_info["name"],
            "color": level_info["color"],
            "emoji": level_info["emoji"],
            "factors": {
                "retrieval_quality": round(retrieval_score, 3),
                "answer_completeness": round(completeness_score, 3),
                "source_reliability": round(reliability_score, 3),
                "consistency": round(consistency_score, 3)
            },
            "explanation": explanation
        }
    
    def _calculate_retrieval_quality(self, query: str, docs: List[Dict]) -> float:
        """计算检索质量"""
        if not docs:
            return 0.0
        
        # 1. 文档数量 (有足够的上下文)
        doc_count_score = min(len(docs) / 5.0, 1.0)  # 5个文档为满分
        
        # 2. 平均相似度 (如果有)
        similarity_scores = []
        for doc in docs:
            metadata = doc.get('metadata', {})
            if 'distance' in metadata:
                # ChromaDB的距离转换为相似度 (距离越小越好)
                similarity = 1.0 / (1.0 + metadata['distance'])
                similarity_scores.append(similarity)
        
        if similarity_scores:
            avg_similarity = sum(similarity_scores) / len(similarity_scores)
        else:
            avg_similarity = 0.7  # 默认值
        
        # 3. 内容丰富度
        total_length = sum(len(doc.get('content', '')) for doc in docs)
        richness_score = min(total_length / 2000, 1.0)  # 2000字符为满分
        
        # 综合评分
        return (doc_count_score * 0.3 + avg_similarity * 0.4 + richness_score * 0.3)
    
    def _calculate_answer_completeness(self, answer: str) -> float:
        """计算答案完整性"""
        if not answer:
            return 0.0
        
        # 1. 长度合理性
        length = len(answer)
        if length < 20:
            length_score = 0.3
        elif length < 50:
            length_score = 0.5
        elif length < 100:
            length_score = 0.7
        elif length < 500:
            length_score = 0.9
        else:
            length_score = 1.0
        
        # 2. 结构性 (是否有分点、标题等)
        structure_score = 0.5
        if re.search(r'[1-9][\.\、]', answer):  # 有编号
            structure_score += 0.2
        if re.search(r'【.*?】|##', answer):  # 有标题
            structure_score += 0.2
        if '\n' in answer and len(answer.split('\n')) >= 3:  # 有段落
            structure_score += 0.1
        
        # 3. 是否有明确答案 (没有"不知道"等)
        negative_phrases = ['不知道', '未找到', '无法回答', '没有信息', '不确定']
        has_negative = any(phrase in answer for phrase in negative_phrases)
        certainty_score = 0.3 if has_negative else 1.0
        
        return (length_score * 0.4 + structure_score * 0.3 + certainty_score * 0.3)
    
    def _calculate_source_reliability(self, docs: List[Dict]) -> float:
        """计算来源可靠性"""
        if not docs:
            return 0.5
        
        # 1. 文档来源的多样性
        sources = set()
        for doc in docs:
            metadata = doc.get('metadata', {})
            source = metadata.get('source', metadata.get('filename', 'unknown'))
            sources.add(source)
        
        diversity_score = min(len(sources) / 3.0, 1.0)  # 3个不同来源为满分
        
        # 2. 是否有页码信息 (有页码说明来源明确)
        has_page = sum(1 for doc in docs if doc.get('metadata', {}).get('page'))
        page_score = has_page / len(docs) if docs else 0
        
        return (diversity_score * 0.5 + page_score * 0.5)
    
    def _calculate_consistency(self, answer: str, docs: List[Dict]) -> float:
        """计算答案与检索文档的一致性"""
        if not docs or not answer:
            return 0.5
        
        # 简单的关键词重叠度检查
        answer_words = set(answer.lower().split())
        
        overlaps = []
        for doc in docs:
            content = doc.get('content', '')
            if not content:
                continue
            
            doc_words = set(content.lower().split())
            if doc_words:
                overlap = len(answer_words & doc_words) / len(answer_words)
                overlaps.append(overlap)
        
        if overlaps:
            return min(sum(overlaps) / len(overlaps) * 2, 1.0)  # *2放大效果
        return 0.5
    
    def _get_level(self, score: float) -> Dict:
        """根据分数获取等级"""
        for level in self.LEVELS:
            if score >= level["min"]:
                return level
        return self.LEVELS[-1]
    
    def _generate_explanation(
        self, 
        retrieval: float, 
        completeness: float, 
        reliability: float,
        consistency: float
    ) -> str:
        """生成置信度解释"""
        def score_text(score: float) -> str:
            if score >= 0.85:
                return "优秀"
            elif score >= 0.70:
                return "良好"
            elif score >= 0.50:
                return "一般"
            else:
                return "较差"
        
        parts = [
            f"检索质量{score_text(retrieval)}({retrieval:.0%})",
            f"答案完整性{score_text(completeness)}({completeness:.0%})",
            f"来源可靠性{score_text(reliability)}({reliability:.0%})",
            f"一致性{score_text(consistency)}({consistency:.0%})"
        ]
        
        return "、".join(parts) + "。"


