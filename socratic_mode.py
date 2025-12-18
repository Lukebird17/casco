#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
苏格拉底式引导模式
通过反问和线索引导学生自主思考
"""

from typing import List, Dict, Optional
from openai import OpenAI
from config import OPENAI_API_KEY, OPENAI_API_BASE, TEXT_MODEL_NAME


class SocraticMode:
    """苏格拉底式引导教学模式"""
    
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY, base_url=OPENAI_API_BASE)
        self.model = TEXT_MODEL_NAME
        self.enabled = False
        
        # 苏格拉底式系统提示词
        self.system_prompt = """你是一位采用苏格拉底教学法的智慧导师。你的目标是通过提问引导学生自己思考和发现答案，而不是直接告诉他们。

**核心原则**:
1. 永远不要直接给出答案
2. 通过层层递进的问题引导思考
3. 鼓励学生表达自己的想法
4. 指出思维中的矛盾或不足
5. 提供线索而非结论

**你的回应应该包含**:
- 🤔 反问：让学生重新审视问题
- 💡 线索：指向可能的思考方向
- 🎯 引导：帮助分解复杂问题
- ✨ 鼓励：肯定正确的思考路径

**避免**:
- ❌ 直接说出答案
- ❌ "答案是..."、"正确的是..."
- ❌ 过于简单的是/否回答

**举例**:
学生问："什么是操作系统的进程？"
不好的回答："进程是程序的执行实例。"
好的回答："🤔 让我们先思考一下：当你运行一个程序时，计算机需要做什么？程序本身和正在运行的程序，它们有什么区别吗？💡 提示：想想程序的代码和运行时的状态..."
"""
    
    def toggle_mode(self) -> bool:
        """切换模式"""
        self.enabled = not self.enabled
        return self.enabled
    
    def is_enabled(self) -> bool:
        """检查是否启用"""
        return self.enabled
    
    def generate_socratic_response(
        self,
        question: str,
        context: str,
        chat_history: Optional[List[Dict]] = None
    ) -> Dict:
        """
        生成苏格拉底式回应
        
        Args:
            question: 学生问题
            context: 检索到的相关内容
            chat_history: 对话历史
            
        Returns:
            {
                "response": "引导性回应",
                "hints": ["线索1", "线索2", ...],
                "follow_up_questions": ["后续问题1", ...]
            }
        """
        
        # 构建消息
        messages = [{"role": "system", "content": self.system_prompt}]
        
        if chat_history:
            messages.extend(chat_history[-6:])  # 只保留最近3轮对话
        
        user_message = f"""学生问题：{question}

参考材料（不要直接引用，用它来设计引导性问题）：
{context[:1000]}

请生成苏格拉底式回应，包括：
1. 主要回应（反问和引导）
2. 3-5个思考线索
3. 1-2个后续引导问题
"""
        
        messages.append({"role": "user", "content": user_message})
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.8,  # 更高的创造性
                max_tokens=800
            )
            
            result_text = response.choices[0].message.content
            
            # 解析回应（尝试提取线索和后续问题）
            hints = self._extract_hints(result_text)
            follow_ups = self._extract_follow_ups(result_text)
            
            return {
                "response": result_text,
                "hints": hints,
                "follow_up_questions": follow_ups,
                "mode": "socratic"
            }
            
        except Exception as e:
            return {
                "response": f"❌ 生成引导失败: {str(e)}",
                "hints": [],
                "follow_up_questions": [],
                "mode": "socratic",
                "error": str(e)
            }
    
    def _extract_hints(self, text: str) -> List[str]:
        """从回应中提取线索"""
        hints = []
        
        # 查找线索标记
        import re
        hint_patterns = [
            r'💡\s*线索[:：]?\s*(.+?)(?=\n|$)',
            r'💡\s*提示[:：]?\s*(.+?)(?=\n|$)',
            r'💡\s*(.+?)(?=\n|$)',
        ]
        
        for pattern in hint_patterns:
            matches = re.findall(pattern, text, re.MULTILINE)
            hints.extend(matches)
        
        # 如果没找到，尝试提取带💡的句子
        if not hints:
            lines = text.split('\n')
            hints = [line.strip() for line in lines if '💡' in line]
        
        return hints[:5]  # 最多5个
    
    def _extract_follow_ups(self, text: str) -> List[str]:
        """从回应中提取后续问题"""
        follow_ups = []
        
        import re
        # 查找问句
        questions = re.findall(r'[？?]([^？?]+[？?])', text)
        
        if not questions:
            # 查找以问号结尾的句子
            lines = text.split('\n')
            follow_ups = [
                line.strip() 
                for line in lines 
                if line.strip().endswith('？') or line.strip().endswith('?')
            ]
        else:
            follow_ups = questions
        
        return follow_ups[:3]  # 最多3个
    
    def generate_hint_progression(
        self,
        question: str,
        context: str,
        difficulty_level: int = 1
    ) -> str:
        """
        生成渐进式线索
        
        Args:
            question: 问题
            context: 参考内容
            difficulty_level: 难度等级（1-5，越大越明显）
            
        Returns:
            线索文本
        """
        hint_levels = {
            1: "最隐晦的线索，只是指明思考方向",
            2: "稍微具体一点的提示",
            3: "比较明确的提示",
            4: "非常接近答案的提示",
            5: "几乎就是答案了（但还是不直接说）"
        }
        
        level_desc = hint_levels.get(difficulty_level, hint_levels[3])
        
        prompt = f"""学生问题：{question}

参考内容：{context[:500]}

请给出一个{level_desc}。

要求：
- 简短（1-2句话）
- 启发性强
- 不直接给答案
- 使用 💡 开头
"""
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "你是苏格拉底式导师，善于给出恰到好处的提示。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=150
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"💡 尝试从基础概念出发思考这个问题"
    
    def render_socratic_ui(self, response: Dict) -> str:
        """渲染苏格拉底模式的特殊 UI"""
        
        html = '''
        <div style="background: linear-gradient(135deg, #a78bfa 0%, #ec4899 100%); 
                    padding: 25px; border-radius: 12px; color: white;">
            <div style="display: flex; align-items: center; margin-bottom: 15px;">
                <div style="font-size: 32px; margin-right: 10px;">🧙‍♂️</div>
                <div>
                    <div style="font-weight: bold; font-size: 18px;">苏格拉底模式已启用</div>
                    <div style="font-size: 12px; opacity: 0.9;">我会通过提问引导你思考，而不是直接给答案</div>
                </div>
            </div>
        '''
        
        # 主要回应
        main_response = response.get('response', '')
        html += f'''
        <div style="background: rgba(255,255,255,0.15); padding: 15px; border-radius: 8px; margin-bottom: 15px;">
            <div style="line-height: 1.8; white-space: pre-wrap;">
                {main_response}
            </div>
        </div>
        '''
        
        # 思考线索
        hints = response.get('hints', [])
        if hints:
            html += '''
            <div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 8px; margin-bottom: 15px;">
                <div style="font-weight: 600; margin-bottom: 10px; font-size: 14px;">
                    💡 思考线索
                </div>
            '''
            
            for i, hint in enumerate(hints[:3], 1):
                html += f'''
                <div style="padding: 8px 12px; margin: 6px 0; background: rgba(255,255,255,0.2); 
                            border-left: 3px solid #fbbf24; border-radius: 4px; font-size: 13px;">
                    {i}. {hint}
                </div>
                '''
            
            html += '</div>'
        
        # 后续思考问题
        follow_ups = response.get('follow_up_questions', [])
        if follow_ups:
            html += '''
            <div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 8px;">
                <div style="font-weight: 600; margin-bottom: 10px; font-size: 14px;">
                    🎯 继续思考
                </div>
            '''
            
            for i, question in enumerate(follow_ups[:2], 1):
                html += f'''
                <div style="padding: 8px 12px; margin: 6px 0; background: rgba(255,255,255,0.2); 
                            border-left: 3px solid #60a5fa; border-radius: 4px; font-size: 13px;">
                    {i}. {question}
                </div>
                '''
            
            html += '</div>'
        
        html += '''
        <div style="text-align: center; margin-top: 15px; font-size: 12px; opacity: 0.9;">
            💬 继续提问或回答上面的引导问题，我会帮助你逐步找到答案
        </div>
        </div>
        '''
        
        return html


