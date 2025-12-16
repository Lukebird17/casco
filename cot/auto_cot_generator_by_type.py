# auto_cot_generator_by_type.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
from typing import List, Dict
from LLM import OpenAIChat

# === 通用推理链模板 ===
COT_TEMPLATE = """
你是一名铁路领域专家。请对下面的问题写出清晰、结构化、逐步推理链（Chain-of-Thought）。

推理链必须遵守以下规则：

【排序类问题】
- 明确范围
- 列出候选项
- 提取排序参数
- 排序
- 得出位置

【比较类问题】
- 对齐对象（如字段、结构、条款）
- 找出相同点
- 找出不同点
- 说明差异原因或影响

【影响因素类问题】
- 确定影响指标
- 列出所有影响因素
- 说明每个因素的作用路径
- 判断整体影响趋势

【结构解析类问题】
- 使用 key 作为字段名
- 使用 value 作为内容
- 若 value 是列表，逐项展开
- 若存在层级（如第 2 层，第 3 层），逐层解释

【流程分析类问题】
- 指明流程起点
- 指明输入数据
- 指明处理步骤
- 指明输出结果
- 将步骤串联成机制

输出格式：

【思考过程】
1. ...
2. ...
3. ...

【最终结论】
这是该问题的推理链，不需要给最终答案。

问题：{question}
"""


class AutoCotByType:
    def __init__(self, llm=None):
        self.llm = llm or OpenAIChat()

    def generate_cot(self, question: str) -> str:
        prompt = COT_TEMPLATE.format(question=question)
        try:
            resp = self.llm.get_completion(prompt).strip()
            return resp
        except Exception as e:
            print(f"❌ CoT 生成失败: {e}")
            return "无法生成推理链。"

    def build_demos(self, classified: List[Dict]) -> List[Dict]:
        demos = []
        by_type = {}

        # 按类型分组
        for item in classified:
            t = item.get("type", "未分类")
            by_type.setdefault(t, []).append(item)

        # 每种类型选择 1–2 个问题生成 CoT
        for t, group in by_type.items():
            if t == "未分类":
                continue

            reps = group[:2]  # 选择前两个代表即可

            for rep in reps:
                q = rep["question"]
                coT = self.generate_cot(q)

                demos.append({
                    "type": t,
                    "question": q,
                    "rationale": coT
                })

                print(f"✅ [{t}] 示例生成成功: {q}")

        return demos

    def save(self, demos: List[Dict], path="./cot/auto_cot_demos.json"):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(demos, f, ensure_ascii=False, indent=2)
        print(f"💾 Auto-CoT 示例已保存到: {path}")


if __name__ == "__main__":
    classified_path = "./cot/classified_reasoning_questions.json"

    with open(classified_path, "r", encoding="utf-8") as f:
        classified = json.load(f)

    generator = AutoCotByType()
    demos = generator.build_demos(classified)
    generator.save(demos)
