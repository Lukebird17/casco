#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
简单的问答示例
演示如何使用 RAG 问答智能体
"""

import asyncio
import os
from rag_qa_agent import RAGQAAgent


async def simple_example():
    """简单示例：处理单个文档并查询"""
    
    # 1. 初始化智能体
    agent = RAGQAAgent(
        working_dir="./rag_storage",
        parser="mineru",
        parse_method="auto"
    )
    
    # 2. 处理单个文档
    pdf_path = "/home/honglianglu/ssd/casco/data/事故报告/2023_北京地铁昌平线"12·14"列车追尾事故调查报告.pdf"
    
    if os.path.exists(pdf_path):
        print("正在处理文档...")
        await agent.process_document(
            file_path=pdf_path,
            output_dir="./output"
        )
    else:
        print(f"文档不存在: {pdf_path}")
        return
    
    # 3. 进行查询
    questions = [
        "这份报告的主要内容是什么？",
        "事故发生的时间和地点？",
        "事故的主要原因是什么？"
    ]
    
    results = []
    for question in questions:
        result = await agent.query(question, mode="hybrid")
        results.append(result)
    
    # 4. 保存结果
    agent.save_results(results, "simple_qa_results.json")
    
    print("\n完成！")


async def batch_example():
    """批量示例：处理多个文档并查询"""
    
    # 1. 初始化智能体
    agent = RAGQAAgent(
        working_dir="./rag_storage",
        parser="mineru",
        parse_method="auto"
    )
    
    # 2. 批量处理事故报告目录
    data_dir = "/home/honglianglu/ssd/casco/data/事故报告"
    
    if os.path.exists(data_dir):
        print("正在批量处理文档...")
        await agent.process_folder(
            folder_path=data_dir,
            output_dir="./output",
            file_extensions=[".pdf"],
            recursive=False,  # 不递归子目录
            max_workers=2
        )
    else:
        print(f"目录不存在: {data_dir}")
        return
    
    # 3. 批量查询
    questions = [
        "所有事故报告中，常见的事故原因有哪些？",
        "不同事故的应急响应措施有什么共同点？",
        "从这些事故中可以总结出哪些安全建议？"
    ]
    
    results = await agent.query_batch(questions, mode="hybrid")
    
    # 4. 保存结果
    agent.save_results(results, "batch_qa_results.json")
    
    print("\n完成！")


async def custom_query_example():
    """自定义查询示例"""
    
    # 初始化智能体（假设文档已经处理过）
    agent = RAGQAAgent(
        working_dir="./rag_storage",
        parser="mineru",
        parse_method="auto"
    )
    
    # 确保 RAG 已初始化
    await agent.initialize()
    
    # 进行自定义查询
    print("\n请输入您的问题（输入 'quit' 退出）：")
    
    while True:
        question = input("\n问题: ").strip()
        
        if question.lower() in ['quit', 'exit', 'q', '退出']:
            break
        
        if not question:
            continue
        
        # 查询
        result = await agent.query(question, mode="hybrid")
        print(f"\n答案: {result['answer']}")


if __name__ == "__main__":
    import sys
    
    print("选择运行模式：")
    print("1. 简单示例（单个文档）")
    print("2. 批量示例（多个文档）")
    print("3. 自定义查询（交互式）")
    
    choice = input("\n请选择 (1/2/3): ").strip()
    
    if choice == "1":
        asyncio.run(simple_example())
    elif choice == "2":
        asyncio.run(batch_example())
    elif choice == "3":
        asyncio.run(custom_query_example())
    else:
        print("无效的选择！")

