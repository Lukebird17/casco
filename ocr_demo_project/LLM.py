#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   LLM.py
@Time    :   2025/11/10
@Ref   :   不要葱姜蒜
'''
import os
from typing import Dict, List, Optional, Tuple, Union
from openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_core.messages.human import HumanMessage
from langchain_core.callbacks import StdOutCallbackHandler
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

RAG_PROMPT_TEMPLATE="""
使用以上下文来回答用户的问题。如果你不知道答案，就说你不知道。总是使用中文回答。
问题: {question}
可参考的上下文：
···
{context}
···
如果给定的上下文无法让你做出回答，请回答数据库中没有这个内容，你不知道。
有用的回答:
"""


class BaseModel:
    def __init__(self, model) -> None:
        self.model = model

    def chat(self, prompt: str, history: List[dict], content: str) -> str:
        pass

    def load_model(self):
        pass

class OpenAIChat(BaseModel):
    def __init__(self, model: str = "deepseek") -> None:
        self.model = model

    def chat(self, prompt: str, history: List[dict], content: str) -> str:
        # 限制 context 长度，避免超过 token 限制
        max_context_length = 30000  # 字符数限制
        if len(content) > max_context_length:
            print(f"⚠️ 上下文过长 ({len(content)} 字符)，截断到 {max_context_length} 字符")
            content = content[:max_context_length] + "\n...(内容已截断)"
        
        llm = ChatOpenAI(
            model_name= os.getenv("CLOUD_MODEL"),
            openai_api_key=os.getenv("CLOUD_API_KEY"),
            openai_api_base=os.getenv("CLOUD_BASE_URL"),
            callbacks=[StdOutCallbackHandler()],  # 实时打印生成内容
            temperature=0.7,
            max_tokens=4096,  # 限制输出长度
            timeout=120,  # 设置超时时间为120秒
            max_retries=2  # 自动重试2次
        )
        
        # 创建一个聊天消息
        history.append({'role': 'user', 'content': RAG_PROMPT_TEMPLATE.format(question=prompt, context=content)})
        messages = [HumanMessage(content=message['content']) for message in history]
        
        # 添加错误处理
        try:
            response = llm.invoke(messages)
            return response.content
        except Exception as e:
            error_msg = str(e)
            print(f"❌ API 调用失败: {error_msg}")
            # 如果是 token 限制问题，尝试更短的上下文
            if "token" in error_msg.lower() or "length" in error_msg.lower():
                print("🔄 检测到 token 限制问题，尝试使用更短的上下文...")
                content = content[:15000] + "\n...(内容已大幅截断)"
                history[-1]['content'] = RAG_PROMPT_TEMPLATE.format(question=prompt, context=content)
                messages = [HumanMessage(content=message['content']) for message in history]
                response = llm.invoke(messages)
                return response.content
            else:
                raise


if __name__ == "__main__":
    model = OpenAIChat()
    response = model.chat("中国的首都是哪里？", [], "中国的首都是北京。")
    print(response)
