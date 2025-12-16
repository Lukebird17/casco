# question_classifier.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
from typing import List, Dict
from LLM import OpenAIChat

class QuestionClassifier:
    def __init__(self, llm=None):
        self.llm = llm or OpenAIChat()

    def classify_prompt(self, question: str) -> str:
        return f"""
你是一名铁路领域智能系统的“问题类型分类器”。
请将下面的问题分类为以下五类之一：

1. 排序类（排序、排第几、最大/最小、优先级、排名）
2. 比较类（差异、版本变化、比较两个对象）
3. 影响因素类（哪些因素影响X？在某条件下会怎样？）
4. 结构解析类（分类、层级结构、组成、要素列表）
5. 流程分析类（流程、机制、怎么实现、步骤、控制逻辑）

请只输出 JSON，不要解释。

示例输出：
{{
  "type": "排序类"
}}

问题：{question}
"""

    def classify(self, questions: List[Dict]) -> List[Dict]:
        classified = []

        for item in questions:
            q = item["question"]
            prompt = self.classify_prompt(q)

            try:
                resp = self.llm.get_completion(prompt).strip()
                data = json.loads(resp)

                item["type"] = data["type"]
                print(f"✅ 分类成功: {q} -> {data['type']}")

            except Exception as e:
                print(f"❌ 分类失败: {q}, 错误: {e}")
                item["type"] = "未分类"

            classified.append(item)

        return classified

    def save(self, data: List[Dict], path="./cot/classified_reasoning_questions.json"):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"\n💾 已保存分类结果到: {path}")


if __name__ == "__main__":
    input_path = "./cot/generated_reasoning_questions.json"
    with open(input_path, 'r', encoding='utf-8') as f:
        questions = json.load(f)

    classifier = QuestionClassifier()
    classified = classifier.classify(questions)
    classifier.save(classified)
