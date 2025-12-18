#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
智能测验生成器
基于文档内容自动生成测试题目
"""

import json
from typing import List, Dict
from openai import OpenAI
from config import OPENAI_API_KEY, OPENAI_API_BASE, MODEL_NAME


class QuizGenerator:
    """测验生成器"""
    
    def __init__(self, model: str = MODEL_NAME):
        self.client = OpenAI(api_key=OPENAI_API_KEY, base_url=OPENAI_API_BASE)
        self.model = model
    
    def generate_quiz(self, context: str, num_questions: int = 5, 
                     difficulty: str = "medium", question_types: List[str] = None) -> List[Dict]:
        """
        生成测验题目
        
        参数:
            context: 基于的文档内容
            num_questions: 题目数量
            difficulty: 难度 (easy/medium/hard)
            question_types: 题目类型列表 ['choice', 'true_false', 'short_answer']
        
        返回:
            题目列表
        """
        if question_types is None:
            question_types = ['choice', 'true_false', 'short_answer']
        
        difficulty_desc = {
            'easy': '简单（基础概念理解）',
            'medium': '中等（应用和分析）',
            'hard': '困难（综合和创新）'
        }
        
        prompt = f"""基于以下内容，生成 {num_questions} 道测试题目。

难度等级：{difficulty_desc.get(difficulty, '中等')}

题目要求：
1. 涵盖不同题型：选择题、判断题、简答题
2. 题目要清晰、准确
3. 答案要有详细解释
4. 难度适中，符合学习目标

内容：
{context[:3000]}

请以JSON格式返回，格式如下：
[
  {{
    "type": "choice",
    "question": "问题内容",
    "options": ["A. 选项1", "B. 选项2", "C. 选项3", "D. 选项4"],
    "correct_answer": "A",
    "explanation": "答案解释"
  }},
  {{
    "type": "true_false",
    "question": "判断题内容",
    "correct_answer": "true",
    "explanation": "答案解释"
  }},
  {{
    "type": "short_answer",
    "question": "简答题内容",
    "correct_answer": "参考答案",
    "explanation": "评分要点"
  }}
]

现在开始生成题目："""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "你是一位专业的教育测评专家，擅长根据教学内容设计高质量的测试题目。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=2000
            )
            
            result_text = response.choices[0].message.content.strip()
            
            # 尝试解析JSON
            try:
                # 提取JSON部分（可能包含markdown代码块）
                if '```json' in result_text:
                    result_text = result_text.split('```json')[1].split('```')[0].strip()
                elif '```' in result_text:
                    result_text = result_text.split('```')[1].split('```')[0].strip()
                
                questions = json.loads(result_text)
                return questions[:num_questions]
            except json.JSONDecodeError as e:
                print(f"JSON解析失败: {e}")
                print(f"原始响应: {result_text}")
                return []
                
        except Exception as e:
            print(f"生成测验失败: {e}")
            return []
    
    def grade_answer(self, question: Dict, user_answer: str) -> Dict:
        """
        评分用户答案
        
        参数:
            question: 题目信息
            user_answer: 用户答案
        
        返回:
            评分结果
        """
        question_type = question.get('type', 'choice')
        correct_answer = question.get('correct_answer', '')
        
        if question_type in ['choice', 'true_false']:
            # 选择题和判断题直接对比
            is_correct = user_answer.strip().upper() == correct_answer.strip().upper()
            return {
                'is_correct': is_correct,
                'score': 100 if is_correct else 0,
                'feedback': question.get('explanation', ''),
                'correct_answer': correct_answer
            }
        else:
            # 简答题使用AI评分
            return self._grade_short_answer(question, user_answer)
    
    def _grade_short_answer(self, question: Dict, user_answer: str) -> Dict:
        """使用AI评分简答题"""
        prompt = f"""作为教师，请评分以下学生答案：

题目：{question['question']}

参考答案：{question['correct_answer']}

学生答案：{user_answer}

评分要点：{question.get('explanation', '无')}

请提供：
1. 分数（0-100）
2. 是否正确（基本正确得80分以上）
3. 反馈意见

请以JSON格式返回：
{{
  "score": 分数,
  "is_correct": true/false,
  "feedback": "反馈内容"
}}
"""
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "你是一位严谨公正的教师。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=500
            )
            
            result_text = response.choices[0].message.content.strip()
            
            # 提取JSON
            if '```json' in result_text:
                result_text = result_text.split('```json')[1].split('```')[0].strip()
            elif '```' in result_text:
                result_text = result_text.split('```')[1].split('```')[0].strip()
            
            result = json.loads(result_text)
            result['correct_answer'] = question['correct_answer']
            return result
            
        except Exception as e:
            print(f"简答题评分失败: {e}")
            return {
                'score': 0,
                'is_correct': False,
                'feedback': f'评分失败: {str(e)}',
                'correct_answer': question['correct_answer']
            }


if __name__ == "__main__":
    # 测试
    generator = QuizGenerator()
    
    test_context = """
    操作系统的内存管理主要包括：
    1. 内存分配与回收
    2. 地址映射
    3. 内存保护
    4. 虚拟内存
    
    虚拟内存是一种内存管理技术，它使得应用程序认为它拥有连续可用的内存。
    """
    
    print("生成测验...")
    questions = generator.generate_quiz(test_context, num_questions=3)
    
    for i, q in enumerate(questions, 1):
        print(f"\n题目 {i}:")
        print(json.dumps(q, ensure_ascii=False, indent=2))
