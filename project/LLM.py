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
from pydantic import BaseModel # 确保 BaseModel 在这里导入


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
        # 确保基类中的方法不返回 None
        raise NotImplementedError("Subclass must implement load_model method.")

class OpenAIChat(BaseModel):
    # 核心新增：类级别的缓存字典，用于存储翻译结果
    _translation_cache: Dict[Tuple[str, str], str] = {}

    def __init__(self, model: str = "deepseek") -> None:
        self.model = model

    # 新增：辅助方法，用于初始化 LangChain 客户端
    def load_model(self, temperature: float = 0.0):
        """返回 LangChain 的 ChatOpenAI 实例。"""
        llm = ChatOpenAI(
            model_name= os.getenv("CLOUD_MODEL"),
            openai_api_key=os.getenv("CLOUD_API_KEY"),
            openai_api_base=os.getenv("CLOUD_BASE_URL"),
            temperature=temperature
        )
        return llm
    
    def get_completion(self, prompt: str) -> str:
        """
        一个简单的单轮调用方法，用于语言推断等纯文本生成任务。
        """
        
        llm_client = self.load_model(temperature=0.0)
        
        # 直接调用 LangChain 的 invoke 方法，将 prompt 包装为 HumanMessage
        response = llm_client.invoke([HumanMessage(content=prompt)])
        
        return response.content

    def chat(self, prompt: str, history: List[dict], content: str, temperature: float = 0.7) -> str:
        llm = ChatOpenAI(
            model_name= os.getenv("CLOUD_MODEL"),
            openai_api_key=os.getenv("CLOUD_API_KEY"),
            openai_api_base=os.getenv("CLOUD_BASE_URL"),
            callbacks=[StdOutCallbackHandler()],  # 实时打印生成内容
            temperature=temperature
        )
        # 创建一个聊天消息
        history.append({'role': 'user', 'content': RAG_PROMPT_TEMPLATE.format(question=prompt, context=content)})
        
        # 使用LangChain进行对话
        response = llm.invoke([HumanMessage(content=message['content']) for message in history])

        return response.content
    
    @classmethod
    def translate_query(cls, llm_instance: 'OpenAIChat', text: str, target_lang: str) -> str:
        """使用LLM将文本翻译为目标语言"""
        # 1. 缓存检查
        cache_key = (text, target_lang)
        if cache_key in cls._translation_cache:
            print(f"✅ 翻译缓存命中: '{text}' -> {target_lang}")
            return cls._translation_cache[cache_key]
        if target_lang == 'zh':
            cls._translation_cache[cache_key] = text
            return text
        
        lang_map = {'en': '英文', 'es': '西班牙语', 'fr': '法语', 'zh': '中文', 'ja': '日文', 'ko': '韩文'}
        target_lang_name = lang_map.get(target_lang, '目标语言')
        
        # 构造翻译任务的 Prompt
        prompt = f"""
        【任务】请将以下RAG查询问题从中文翻译成**{target_lang_name}**。
        
        【要求】
        1. 保持翻译的准确性，特别是专业名词。
        2. 只返回翻译结果，不要添加任何解释性文字。
        3. 如果无法准确翻译，则保留原文。
        
        【待翻译文本】
        ---
        {text}
        ---
        
        【译文】
        """
        
        # ❗ 核心：调用 LLM 实例进行翻译
        # 由于是单轮任务，不需要 history 或 content
        
        # 我们可以复用 llm_instance 的 chat 逻辑，但需要调整参数
        # 简单起见，我们直接构造一个消息列表给 LangChain/OpenAI
        
        # 注意：llm_instance.chat 的签名是 (self, prompt: str, history: List[dict], content: str)
        # 这里的 chat 方法主要用于 RAG 生成，不适用于纯翻译任务。
        # 
        # 最佳实践是为纯翻译/工具调用创建新的方法或使用更简单的 API 调用。
        
        # 如果坚持使用 llm_instance.chat，您可能需要传入一个空的 history 和 content：
        # translation_result = llm_instance.chat(prompt, [], "") # 假设 chat 接受这种方式
        
        # 考虑到 chat 方法设计用于 RAG 填充 RAG_PROMPT_TEMPLATE，
        # 我们在这里直接使用 LangChain 的 ChatOpenAI 实例进行纯文本生成。

        try:
            # 重新初始化一个 LLM 实例用于纯翻译（
            # 核心修正：使用 get_completion 进行简单 API 调用
            translated_text = llm_instance.get_completion(prompt).strip()

            # 清理 LLM 可能添加的前后空格或引号
            if translated_text.startswith('【译文】'):
                 translated_text = translated_text.replace('【译文】', '').strip()

            # 翻译失败或返回空时，使用原文
            if not translated_text:
                 translated_text = text

            # 2. 存储到缓存并返回
            cls._translation_cache[cache_key] = translated_text
            lang_map = {'en': '英语', 'es': '西班牙语', 'fr': '法语', 'zh': '中文', 'ja': '日语', 'ko': '韩语'}
            target_lang_name = lang_map.get(target_lang, '目标语言')
            print(f"✅ 查询已成功翻译为 '{target_lang_name}'。")
            return translated_text
            
        except Exception as e:
            # LLM API 调用失败的错误处理
            print(f"❌ 翻译失败，保留原文。目标语言: {target_lang_name}, 错误: {e}")
            
            # 翻译失败时，将原始文本存入缓存 (避免重复尝试失败的查询)
            cls._translation_cache[cache_key] = text 
            return text


if __name__ == "__main__":
    model = OpenAIChat()
    response = model.chat("中国的首都是哪里？", [], "中国的首都是北京。")
    print(response)
