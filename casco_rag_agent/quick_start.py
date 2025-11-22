#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
快速启动脚本
用于快速配置和运行 RAG 问答系统
"""

import os
import sys
import asyncio
from pathlib import Path


def check_env_vars():
    """检查环境变量配置"""
    required_vars = [
        ("CLOUD_API_KEY", "LLM API Key"),
        ("CLOUD_BASE_URL", "LLM Base URL"),
        ("OPENAI_API_KEY", "Embedding API Key"),
    ]
    
    missing_vars = []
    for var_name, description in required_vars:
        if not os.getenv(var_name):
            missing_vars.append((var_name, description))
    
    if missing_vars:
        print("❌ 缺少以下环境变量：\n")
        for var_name, description in missing_vars:
            print(f"  - {var_name} ({description})")
        print("\n请设置环境变量后重试。")
        print("\n示例：")
        print("  export CLOUD_API_KEY='your_api_key'")
        print("  export CLOUD_BASE_URL='https://api.deepseek.com/v1'")
        print("  export OPENAI_API_KEY='your_api_key'")
        return False
    
    return True


def show_menu():
    """显示菜单"""
    print("\n" + "="*60)
    print("RAG 问答智能体 - 快速启动")
    print("="*60)
    print("\n请选择操作：")
    print("1. 处理单个文档")
    print("2. 批量处理文档（事故报告）")
    print("3. 批量处理所有文档")
    print("4. 仅查询（假设文档已处理）")
    print("5. 交互式问答")
    print("6. 运行完整示例（处理+查询）")
    print("0. 退出")
    print("="*60)


async def process_single_document():
    """处理单个文档"""
    from rag_qa_agent import RAGQAAgent
    
    print("\n可用的文档示例：")
    print("1. 2023_北京地铁昌平线\"12·14\"列车追尾事故调查报告.pdf")
    print("2. 2024_地铁昌平线\"7·25\"列车脱轨事故调查报告.pdf")
    print("3. 自定义路径")
    
    choice = input("\n请选择 (1/2/3): ").strip()
    
    base_path = "/home/honglianglu/ssd/casco/data/事故报告/"
    
    if choice == "1":
        file_path = base_path + "2023_北京地铁昌平线\"12·14\"列车追尾事故调查报告.pdf"
    elif choice == "2":
        file_path = base_path + "2024_地铁昌平线\"7·25\"列车脱轨事故调查报告.pdf"
    elif choice == "3":
        file_path = input("请输入文档路径: ").strip()
    else:
        print("无效的选择！")
        return
    
    if not os.path.exists(file_path):
        print(f"❌ 文件不存在: {file_path}")
        return
    
    agent = RAGQAAgent()
    await agent.process_document(file_path)
    print("\n✅ 文档处理完成！")


async def process_accident_reports():
    """批量处理事故报告"""
    from rag_qa_agent import RAGQAAgent
    
    folder_path = "/home/honglianglu/ssd/casco/data/事故报告"
    
    if not os.path.exists(folder_path):
        print(f"❌ 目录不存在: {folder_path}")
        return
    
    agent = RAGQAAgent()
    await agent.process_folder(
        folder_path=folder_path,
        output_dir="./output",
        file_extensions=[".pdf"],
        recursive=False,
        max_workers=2
    )
    print("\n✅ 事故报告处理完成！")


async def process_all_documents():
    """批量处理所有文档"""
    from rag_qa_agent import RAGQAAgent
    
    folder_path = "/home/honglianglu/ssd/casco/data"
    
    print("⚠️  警告：这将处理所有文档，可能需要较长时间。")
    confirm = input("是否继续？(y/n): ").strip().lower()
    
    if confirm != 'y':
        print("已取消。")
        return
    
    agent = RAGQAAgent()
    await agent.process_folder(
        folder_path=folder_path,
        output_dir="./output",
        file_extensions=[".pdf"],
        recursive=True,
        max_workers=2
    )
    print("\n✅ 所有文档处理完成！")


async def query_only():
    """仅查询"""
    from rag_qa_agent import RAGQAAgent
    
    print("\n示例问题：")
    print("1. 文档中提到的主要安全规范有哪些？")
    print("2. CBTC系统的核心组成部分是什么？")
    print("3. 2023年北京地铁昌平线事故的主要原因是什么？")
    print("4. 自定义问题")
    
    choice = input("\n请选择 (1/2/3/4): ").strip()
    
    questions = {
        "1": "文档中提到的主要安全规范有哪些？",
        "2": "CBTC系统的核心组成部分是什么？",
        "3": "2023年北京地铁昌平线事故的主要原因是什么？"
    }
    
    if choice == "4":
        question = input("请输入您的问题: ").strip()
    elif choice in questions:
        question = questions[choice]
    else:
        print("无效的选择！")
        return
    
    if not question:
        print("问题不能为空！")
        return
    
    agent = RAGQAAgent()
    result = await agent.query(question, mode="hybrid")
    
    print("\n" + "="*60)
    print("查询结果：")
    print("="*60)
    print(f"\n问题: {result['question']}")
    print(f"\n答案:\n{result['answer']}")
    print("\n" + "="*60)


async def interactive_qa():
    """交互式问答"""
    from rag_qa_agent import RAGQAAgent
    
    print("\n进入交互式问答模式...")
    print("提示：输入 'quit' 或 'exit' 退出\n")
    
    agent = RAGQAAgent()
    await agent.initialize()
    
    while True:
        question = input("\n❓ 请输入问题: ").strip()
        
        if question.lower() in ['quit', 'exit', 'q', '退出']:
            print("退出交互式问答。")
            break
        
        if not question:
            continue
        
        try:
            result = await agent.query(question, mode="hybrid")
            print(f"\n💡 答案:\n{result['answer']}")
        except Exception as e:
            print(f"❌ 查询失败: {e}")


async def run_complete_example():
    """运行完整示例"""
    from rag_qa_agent import RAGQAAgent
    
    print("\n运行完整示例（处理事故报告 + 示例查询）...\n")
    
    # 1. 处理文档
    folder_path = "/home/honglianglu/ssd/casco/data/事故报告"
    
    agent = RAGQAAgent()
    
    print("步骤 1/3: 处理文档...")
    await agent.process_folder(
        folder_path=folder_path,
        output_dir="./output",
        file_extensions=[".pdf"],
        recursive=False,
        max_workers=2
    )
    
    # 2. 查询
    print("\n步骤 2/3: 执行查询...")
    questions = [
        "文档中提到的主要事故类型有哪些？",
        "这些事故报告中常见的事故原因是什么？",
        "从这些事故中可以总结出哪些安全建议？"
    ]
    
    results = await agent.query_batch(questions, mode="hybrid")
    
    # 3. 保存结果
    print("\n步骤 3/3: 保存结果...")
    output_file = "/home/honglianglu/ssd/casco/qa_results.json"
    agent.save_results(results, output_file)
    
    print("\n" + "="*60)
    print("✅ 完整示例运行完成！")
    print(f"📄 结果已保存到: {output_file}")
    print("="*60)


async def main():
    """主函数"""
    # 检查环境变量
    if not check_env_vars():
        sys.exit(1)
    
    while True:
        show_menu()
        choice = input("\n请选择 (0-6): ").strip()
        
        if choice == "0":
            print("\n再见！")
            break
        elif choice == "1":
            await process_single_document()
        elif choice == "2":
            await process_accident_reports()
        elif choice == "3":
            await process_all_documents()
        elif choice == "4":
            await query_only()
        elif choice == "5":
            await interactive_qa()
        elif choice == "6":
            await run_complete_example()
        else:
            print("\n❌ 无效的选择，请重试。")
        
        input("\n按 Enter 继续...")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n程序已中断。")
    except Exception as e:
        print(f"\n❌ 发生错误: {e}")
        import traceback
        traceback.print_exc()

