# auto_cot_prompting.py
import json
import os
from typing import List, Dict


class AutoCotPromptBuilder:
    def __init__(self, demo_path: str):
        """
        demo_path 通常是: ./cot/auto_cot_demos.json

        支持两种结构：
        1）带类型字段：
        [
            {
                "type": "排序类",
                "question": "...",
                "rationale": "..."
            },
            ...
        ]

        2）不带类型字段：
        [
            {
                "question": "...",
                "rationale": "..."
            },
            ...
        ]
        """
        with open(demo_path, 'r', encoding='utf-8') as f:
            self.examples: List[Dict[str, str]] = json.load(f)

    def _select_one_example_per_type(self, max_examples: int = 5) -> List[Dict[str, str]]:
        """
        按“问题类型”每类选一个示例：
        - 如果有 'type' 字段：每个 type 选一个
        - 如果没有 'type' 字段：退化为简单取前 max_examples 个
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

    def build_prompt(self, query: str, context: str, max_examples: int = 5) -> str:
        """
        构造最终提示词：
        1. 每种问题类型各 1 个 CoT 示例（如果有 type 字段）
        2. 当前问题，提示“让我们一步一步思考”
        3. 可选的文档上下文

        ✅ 注意：不需要 query_type，让模型自己看多种示例，模仿合适的思考方式。
        """
        prompt_parts: List[str] = []

        # 1. 选出要用的 few-shot 示例（多类型，每类一个）
        selected_examples = self._select_one_example_per_type(max_examples=max_examples)

        if selected_examples:
            prompt_parts.append("下面是若干铁路领域问题及其详细思考过程示例，请学习它们的推理方式：\n")
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
        prompt_parts.append("现在请你参考上述示例的思考方式，回答下面的问题：\n")
        prompt_parts.append(f"Q: {query}")
        prompt_parts.append("A: 让我们一步一步地进行推理，然后给出答案。\n")

        # 3. 文档上下文（RAG 检索结果）
        if context:
            prompt_parts.append("【可参考的文档内容】")
            prompt_parts.append(context)
            prompt_parts.append("")  # 结尾换行

        return "\n".join(prompt_parts)
