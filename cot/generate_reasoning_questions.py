# generate_reasoning_questions.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
import random
from typing import List
from LLM import OpenAIChat  # 你已有的封装
from VectorBase import VectorStore

class ReasoningQuestionGenerator:
    def __init__(self, llm=None):
        self.llm = llm or OpenAIChat()

    def build_prompt(self, passage: str) -> str:
        return f"""
你是铁路工程领域的专业智能问答助手，擅长根据标准文档、事故报告和技术资料构造“需要推理的问题”。

【你的任务】
请根据以下内容，提出一个必须经过推理、比较或归纳才能回答的问题。

【问题类型可以包括】（任选其一）：
1. 根据技术文档内容，分析某个子系统的工作流程或控制逻辑
2. 综合多个规范条款或版本，比较差异并提出设计考量
3. 从描述中归纳出影响因素或条件，并判断系统行为
4. 结合描述内容进行排序、分类或条件归属判断
5. 引导用户从多个信息点中整合推导出结论

【输入内容】
---
{passage}
---

【输出要求】
- 只输出一个问题
- 问题应具体、清晰、包含推理必要性
- 不要提出能直接复制原文就能回答的问题
- 问题风格应接近如下示例（不照搬）：

【问题示例】
- 南京地铁 S7 号线的运营里程，在江苏省内已运营地铁长度中排第几？
- ATO 子系统是如何形成轨迹并将其传递给列控设备的？
- CBTC 的自动控制功能在哪些文档中体现，测试需求编号分别是什么？
- SUBSET-026 标准中，牵引数据包的字段定义在不同版本之间有何变化？
- 哪些因素会影响列车检测系统在电磁干扰环境下的可靠性？

【请生成的问题】
"""
    def get_context_chunks(self, passages: List[dict], index: int, window_size: int = 2) -> str:
        """获取指定索引chunk及其前后相邻的chunk"""
        start_idx = max(0, index - window_size)
        end_idx = min(len(passages), index + window_size + 1)
        
        context_parts = []
        for i in range(start_idx, end_idx):
            content = passages[i].get("content", "").strip()
            if content:
                context_parts.append(content)
        
        return "\n\n".join(context_parts)
    
    def generate(self, passages: List[dict], top_n: int = 100) -> List[dict]:
        results = []
        
        # 创建可用的索引列表（排除边界情况）
        available_indices = list(range(len(passages)))
        
        # 随机选择top_n个索引
        if len(available_indices) <= top_n:
            selected_indices = available_indices
        else:
            selected_indices = random.sample(available_indices, top_n)
        
        for i, idx in enumerate(selected_indices):
            try:
                # 获取当前chunk及其前后相邻的chunk
                context_content = self.get_context_chunks(passages, idx, window_size=2)
                
                if not context_content or len(context_content.strip()) < 50:
                    print(f"⚠️ 跳过内容过少的索引 {idx}")
                    continue
                
                prompt = self.build_prompt(context_content)
                question = self.llm.get_completion(prompt).strip()

                # 获取原始chunk信息用于显示
                original_content = passages[idx].get("content", "").strip()
                
                print(f"✅ [问题 {i+1}/{top_n}] 索引 {idx} 已生成: {question[:100]}...")
                
                results.append({
                    "index": idx,
                    "source_text": original_content[:200] + "..." if len(original_content) > 200 else original_content,
                    "context_text": context_content[:300] + "..." if len(context_content) > 300 else context_content,
                    "question": question
                })

            except Exception as e:
                print(f"❌ 生成失败 [索引 {idx}]: {e}")
        
        return results
    # def generate(self, passages: List[dict], top_n: int = 10) -> List[dict]:
    #     results = []
    #     for i, chunk in enumerate(passages[:top_n]):
    #         try:
    #             content = chunk.get("content", "").strip()

    #             if not content or len(content) < 20:
    #                 continue  # 跳过空段落或无效内容
                
    #             prompt = self.build_prompt(content)
    #             question = self.llm.get_completion(prompt).strip()

    #             print(f"✅ [问题 {i+1}] 已生成: {question}")
    #             results.append({
    #                 "source_text": content[:200] + "..." if len(content) > 200 else content,
    #                 "question": question
    #             })

    #         except Exception as e:
    #             print(f"❌ 生成失败 [{i+1}]: {e}")
    #     return results

    def save(self, data: List[dict], path="./cot/generated_reasoning_questions.json"):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"\n💾 共保存 {len(data)} 条推理型问题到: {path}")


if __name__ == "__main__":
    # 1. 加载你已有的向量库
    vector_store = VectorStore()
    vector_store.load_vector('./storage_bge_hierarchical')  # 根据你的路径修改

    # 2. 实例化生成器
    generator = ReasoningQuestionGenerator()

    # 3. 从文档生成问题
    generated = generator.generate(vector_store.document, top_n=100)

    # 4. 保存结果
    generator.save(generated)
