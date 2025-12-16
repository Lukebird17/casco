#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Auto-CoT提示词构建器（从Casco移植）
自动生成包含思维链示例的提示词
"""

import json
import os
from typing import List, Dict


class AutoCotPromptBuilder:
    """Auto-CoT提示词构建器（从Casco完全移植）"""
    
    def __init__(self, demo_path: str = None):
        """
        初始化Auto-CoT构建器
        
        Args:
            demo_path: CoT示例文件路径
        """
        if demo_path is None:
            # 默认使用当前目录的auto_cot_demos.json
            demo_path = os.path.join(os.path.dirname(__file__), "auto_cot_demos.json")
        
        with open(demo_path, 'r', encoding='utf-8') as f:
            self.examples: List[Dict[str, str]] = json.load(f)
        
        print(f"✅ 加载了 {len(self.examples)} 个CoT示例")
    
    def _select_one_example_per_type(self, max_examples: int = 3) -> List[Dict[str, str]]:
        """
        按"问题类型"每类选一个示例
        
        Args:
            max_examples: 最多选择的示例数量
            
        Returns:
            选中的示例列表
        """
        if not self.examples:
            return []
        
        # 检查是否有 type 字段
        has_type_field = any("type" in ex for ex in self.examples)
        
        # 没有 type，直接取前 max_examples 个
        if not has_type_field:
            return self.examples[:max_examples]
        
        # 有 type：按 type 聚合，每个 type 拿一个代表
        per_type: Dict[str, Dict[str, str]] = {}
        for ex in self.examples:
            t = ex.get("type", "未分类")
            # 每个类型只保留第一个出现的示例
            if t not in per_type:
                per_type[t] = ex
        
        # 将每个 type 的一个代表收集出来
        selected = list(per_type.values())
        
        # 如果类型太多，限制数量
        if len(selected) > max_examples:
            selected = selected[:max_examples]
        
        return selected
    
    def build_prompt(self, query: str, context: str, max_examples: int = 3) -> str:
        """
        构造最终提示词（从Casco完全移植）
        
        包含：
        1. 每种问题类型各 1 个 CoT 示例
        2. 当前问题，提示"让我们一步一步思考"
        3. 可选的文档上下文
        
        Args:
            query: 用户问题
            context: 检索到的上下文
            max_examples: 最多使用的示例数量
            
        Returns:
            完整的提示词
        """
        prompt_parts: List[str] = []
        
        # 1. 选出要用的 few-shot 示例（多类型，每类一个）
        selected_examples = self._select_one_example_per_type(max_examples=max_examples)
        
        if selected_examples:
            prompt_parts.append("下面是一些问题及其详细思考过程示例，请学习这种推理方式：\n")
            for ex in selected_examples:
                q_demo = ex.get("question", "").strip()
                r_demo = ex.get("rationale", "").strip()
                type_info = ex.get("type", "").strip()
                
                if type_info:
                    prompt_parts.append(f"【示例 - {type_info}】")
                else:
                    prompt_parts.append("【示例】")
                
                prompt_parts.append(f"Q: {q_demo}\nA:\n{r_demo}\n")
        
        # 2. 当前问题
        prompt_parts.append("\n现在请你参考上述示例的思考方式，回答下面的问题：\n")
        prompt_parts.append(f"Q: {query}")
        prompt_parts.append("A: 让我们一步一步地进行推理，然后给出答案。\n")
        
        # 3. 文档上下文（RAG 检索结果）
        if context:
            prompt_parts.append("\n【可参考的课程材料】")
            prompt_parts.append(context)
            prompt_parts.append("")  # 结尾换行
        
        return "\n".join(prompt_parts)
    
    def build_simple_prompt(self, query: str, context: str) -> str:
        """
        构造简单提示词（不含CoT示例）
        
        Args:
            query: 用户问题
            context: 检索到的上下文
            
        Returns:
            简单提示词
        """
        prompt_parts = []
        prompt_parts.append(f"请基于以下课程材料回答问题：\n")
        prompt_parts.append(context)
        prompt_parts.append(f"\n问题：{query}\n")
        prompt_parts.append("请给出准确、完整的回答：")
        
        return "\n".join(prompt_parts)


if __name__ == "__main__":
    # 测试Auto-CoT
    print("=== 测试Auto-CoT提示词构建器 ===\n")
    
    builder = AutoCotPromptBuilder()
    
    query = "什么是词向量？"
    context = """
【课程材料】
词向量是词的连续向量表示，也称为分布式表达...
"""
    
    # 构建带CoT示例的提示词
    prompt = builder.build_prompt(query, context, max_examples=2)
    
    print("构建的提示词：")
    print("="*60)
    print(prompt)
    print("="*60)

