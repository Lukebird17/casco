"""
质量评估模块
使用简化的评估方法生成雷达图数据
不依赖 DeepEval 库，避免复杂依赖
"""

from typing import Dict, List, Tuple
import re
import asyncio
from openai import OpenAI
from config import OPENAI_API_KEY, OPENAI_API_BASE, TEXT_MODEL_NAME  # ✅ 改用TEXT_MODEL_NAME


class QualityEvaluator:
    """答案质量评估器"""
    
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY, base_url=OPENAI_API_BASE)
        self.model = TEXT_MODEL_NAME  # ✅ 使用纯文本模型，而不是多模态模型
        print(f"✅ QualityEvaluator初始化，使用模型: {self.model}")
    
    def evaluate_answer(
        self,
        question: str,
        answer: str,
        context_docs: List[Dict],
        chat_history: List[Dict] = None
    ) -> Dict:
        """
        评估答案质量，生成雷达图数据（同步版本）
        
        参数:
            question: 用户问题
            answer: AI 回答
            context_docs: 检索到的上下文文档
            chat_history: 聊天历史
        
        返回:
            {
                "overall_score": 0.85,  # 总分 0-1
                "radar_data": [
                    {"subject": "准确性", "A": 90},
                    {"subject": "相关性", "A": 88},
                    ...
                ],
                "details": {
                    "faithfulness": "分析说明...",
                    "context_relevancy": "分析说明...",
                    ...
                }
            }
        """
        
        # 1. 提取上下文文本
        context_text = self._format_context(context_docs)
        
        # 2. 使用 LLM 进行多维度评估
        evaluation_prompt = f"""你是答案质量评估专家。请评估以下AI回答的质量。

【用户问题】
{question}

【参考资料】（前1500字符）
{context_text[:1500]}

【AI回答】
{answer[:1000]}

请从5个维度评估（0-100分），用JSON格式返回：

1. 准确性：事实是否正确
2. 相关性：是否回答问题
3. 完整性：信息是否全面
4. 忠实度：是否基于参考资料
5. 清晰度：表述是否清晰

返回格式（只返回JSON）：
{{
  "准确性": {{"score": 85, "reason": "简短理由"}},
  "相关性": {{"score": 90, "reason": "简短理由"}},
  "完整性": {{"score": 80, "reason": "简短理由"}},
  "忠实度": {{"score": 88, "reason": "简短理由"}},
  "清晰度": {{"score": 85, "reason": "简短理由"}}
}}
"""
        
        try:
            print(f"🔍 开始LLM评估，模型: {self.model}")
            # 调用 LLM 评估
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "你是专业的答案质量评估专家，用JSON格式返回评估结果。"},
                    {"role": "user", "content": evaluation_prompt}
                ],
                temperature=0.1,  # ✅ 降低温度，使输出更稳定
                max_tokens=800,   # ✅ 减少max_tokens，加快速度
                timeout=30.0      # ✅ 设置30秒超时
            )
            
            result_text = response.choices[0].message.content.strip()
            print(f"✅ LLM评估完成，结果长度: {len(result_text)}")
            
            # 提取 JSON
            if '```json' in result_text:
                result_text = result_text.split('```json')[1].split('```')[0].strip()
            elif '```' in result_text:
                result_text = result_text.split('```')[1].split('```')[0].strip()
            
            # 解析评估结果
            import json
            scores_dict = json.loads(result_text)
            
            # 转换为雷达图格式
            radar_data = []
            total_score = 0
            details = {}
            
            for dimension, data in scores_dict.items():
                score = data.get('score', 0)
                reason = data.get('reason', '')
                
                radar_data.append({
                    "subject": dimension,
                    "A": score,
                    "fullMark": 100  # ✅ 添加fullMark字段，与前端兼容
                })
                
                total_score += score
                details[dimension] = reason
            
            # 计算总分（0-1范围）
            overall_score = total_score / (len(scores_dict) * 100) if scores_dict else 0
            
            return {
                "overall_score": round(overall_score, 2),
                "radar_data": radar_data,
                "details": details
            }
            
        except Exception as e:
            print(f"⚠️  质量评估失败: {e}")
            # 返回默认值
            return self._get_default_evaluation()
    
    async def evaluate(
        self,
        query: str,
        answer: str,
        retrieved_context: List[Dict],
        chat_history: List[Dict] = None
    ) -> Dict:
        """
        异步评估接口（与AdvancedQualityEvaluator兼容）
        
        参数:
            query: 用户问题
            answer: AI回答
            retrieved_context: 检索到的上下文文档
            chat_history: 聊天历史
        
        返回:
            与evaluate_answer相同的格式
        """
        # 在线程池中运行同步的evaluate_answer
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(
            None, 
            self.evaluate_answer,
            query,
            answer,
            retrieved_context,
            chat_history
        )
    
    def _format_context(self, context_docs: List[Dict]) -> str:
        """格式化上下文文档"""
        if not context_docs:
            return "（无参考资料）"
        
        context_parts = []
        for i, doc in enumerate(context_docs[:3], 1):  # 只取前3个
            content = doc.get("content", "")
            filename = doc.get("filename") or doc.get("metadata", {}).get("filename", "未知")
            page = doc.get("page_number") or doc.get("metadata", {}).get("page", "")
            
            if page:
                context_parts.append(f"[文档{i}: {filename}, 第{page}页]\n{content[:500]}")
            else:
                context_parts.append(f"[文档{i}: {filename}]\n{content[:500]}")
        
        return "\n\n".join(context_parts)
    
    def _get_default_evaluation(self) -> Dict:
        """返回默认评估结果（评估失败时使用）"""
        default_score = 75  # 默认75分
        
        return {
            "overall_score": 0.75,
            "radar_data": [
                {"subject": "准确性", "A": default_score, "fullMark": 100},
                {"subject": "相关性", "A": default_score, "fullMark": 100},
                {"subject": "完整性", "A": default_score - 5, "fullMark": 100},
                {"subject": "忠实度", "A": default_score + 5, "fullMark": 100},
                {"subject": "清晰度", "A": default_score, "fullMark": 100},
            ],
            "details": {
                "准确性": "评估失败，使用默认值",
                "相关性": "评估失败，使用默认值",
                "完整性": "评估失败，使用默认值",
                "忠实度": "评估失败，使用默认值",
                "清晰度": "评估失败，使用默认值",
            }
        }


# 示例使用
if __name__ == "__main__":
    evaluator = QualityEvaluator()
    
    test_question = "什么是隐马尔可夫模型？"
    test_answer = "隐马尔可夫模型（HMM）是一种统计模型，用于描述含有隐藏状态的马尔可夫过程..."
    test_context = [
        {
            "content": "隐马尔可夫模型是一种重要的统计模型...",
            "filename": "test.pdf",
            "page_number": 1
        }
    ]
    
    result = evaluator.evaluate_answer(test_question, test_answer, test_context)
    
    print("📊 评估结果：")
    print(f"   总分: {result['overall_score']}")
    print(f"\n📈 雷达图数据:")
    for item in result['radar_data']:
        print(f"   {item['subject']}: {item['A']}分")
    print(f"\n📝 详细说明:")
    for dim, reason in result['details'].items():
        print(f"   {dim}: {reason}")

