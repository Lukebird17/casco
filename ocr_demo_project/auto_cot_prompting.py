# auto_cot_prompting.py
import json
import os
from typing import List, Dict

class AutoCotPromptBuilder:
    def __init__(self, demo_path: str):
        with open(demo_path, 'r', encoding='utf-8') as f:
            self.examples: List[Dict[str, str]] = json.load(f)

    def build_prompt(self, query: str, context: str, max_examples: int = 5) -> str:
        prompt_parts = []

        # 添加 Few-shot 示例
        for ex in self.examples[:max_examples]:
            prompt_parts.append(f"Q: {ex['question']}\nA: {ex['rationale']}\n")

        # 添加当前问题作为最后一项
        prompt_parts.append(f"Q: {query}\nA: Let's think step by step.\n")

        # 拼接上下文（可选）
        if context:
            prompt_parts.append(f"\n【文档内容】\n{context}\n")

        return "\n".join(prompt_parts)