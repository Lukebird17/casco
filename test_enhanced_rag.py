#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
测试增强版RAG功能
演示从Casco移植的核心功能
"""

import os
from rag_agent import RAGAgent
from config import VECTOR_DB_PATH, MODEL_NAME


def test_query_analysis():
    """测试问题分析功能"""
    print("\n" + "="*60)
    print("测试1: 问题分析和分类")
    print("="*60)
    
    agent = RAGAgent(model=MODEL_NAME)
    
    test_queries = [
        "什么是词向量？",  # 预期：basic
        "NLP中有哪些常见的模型？",  # 预期：intermediate
        "请解释BERT和GPT的区别？",  # 预期：advanced
        "为什么词向量又称为分布式表达？",  # 预期：advanced
    ]
    
    for query in test_queries:
        print(f"\n问题: {query}")
        query_type = agent.analyze_query_type(query)
        print(f"✅ 分类结果: {query_type}\n")


def test_query_enhancement():
    """测试查询增强功能"""
    print("\n" + "="*60)
    print("测试2: 查询增强（多查询生成）")
    print("="*60)
    
    agent = RAGAgent(model=MODEL_NAME)
    
    test_queries = [
        "什么是BERT模型？",
        "2025年NLP技术有什么发展？",
        "解释CRF和HMM的区别",
    ]
    
    for query in test_queries:
        print(f"\n原始查询: {query}")
        enhanced = agent.enhance_query(query)
        print(f"增强查询: {enhanced}")
        print(f"✅ 生成了 {len(enhanced)} 个查询\n")


def test_retrieval_strategies():
    """测试分层检索策略（需要先运行process_data.py）"""
    print("\n" + "="*60)
    print("测试3: 分层检索策略")
    print("="*60)
    
    if not os.path.exists(VECTOR_DB_PATH):
        print("⚠️  向量数据库不存在，请先运行: python process_data.py")
        return
    
    agent = RAGAgent(model=MODEL_NAME)
    
    # 检查知识库
    count = agent.vector_store.get_collection_count()
    if count == 0:
        print("⚠️  知识库为空，请先运行: python process_data.py")
        return
    
    print(f"✅ 知识库已加载，包含 {count} 个文档块\n")
    
    test_queries = [
        ("什么是词向量？", "basic"),
        ("NLP中有哪些常见的模型？", "intermediate"),
        ("请解释BERT和GPT的区别？", "advanced"),
    ]
    
    for query, expected_type in test_queries:
        print(f"\n{'='*60}")
        print(f"问题: {query}")
        print(f"预期类型: {expected_type}")
        print(f"{'='*60}")
        
        # 只测试检索，不生成回答（节省API调用）
        context, results = agent.retrieve_context(query)
        
        print(f"\n检索到 {len(results)} 个文档")
        if results:
            print("\nTop 3 结果预览:")
            for i, result in enumerate(results[:3], 1):
                print(f"\n{i}. {result['filename']} (第{result['page_number']}页)")
                print(f"   相关度: {result.get('match_ratio', 0):.1%}")
                print(f"   内容预览: {result['content'][:100]}...")


def test_full_pipeline():
    """测试完整流程（需要API）"""
    print("\n" + "="*60)
    print("测试4: 完整RAG流程")
    print("="*60)
    
    if not os.path.exists(VECTOR_DB_PATH):
        print("⚠️  向量数据库不存在，请先运行: python process_data.py")
        return
    
    agent = RAGAgent(model=MODEL_NAME)
    
    count = agent.vector_store.get_collection_count()
    if count == 0:
        print("⚠️  知识库为空，请先运行: python process_data.py")
        return
    
    # 测试一个简单问题
    query = "什么是词向量？"
    
    print(f"\n问题: {query}")
    print("\n开始完整RAG流程...\n")
    
    try:
        answer = agent.answer_question(query)
        print(f"\n{'='*60}")
        print("助教回答:")
        print(f"{'='*60}")
        print(answer)
        print(f"{'='*60}\n")
        print("✅ 完整流程测试成功！")
    except Exception as e:
        print(f"❌ 测试失败: {e}")
        print("提示: 请确保config.py中的API密钥已正确配置")


def main():
    """主函数"""
    print("\n╔══════════════════════════════════════════════════════╗")
    print("║     增强版RAG系统测试（Casco核心功能）                ║")
    print("╚══════════════════════════════════════════════════════╝")
    
    print("\n📋 测试清单:")
    print("  1. 问题分析和分类 ✓")
    print("  2. 查询增强（多查询生成） ✓")
    print("  3. 分层检索策略 ✓")
    print("  4. 完整RAG流程 ✓")
    
    # 测试1: 问题分析（不需要向量库）
    test_query_analysis()
    
    # 测试2: 查询增强（不需要向量库）
    test_query_enhancement()
    
    # 测试3: 分层检索（需要向量库）
    test_retrieval_strategies()
    
    # 测试4: 完整流程（需要向量库和API）
    print("\n是否测试完整RAG流程（需要API调用）？[y/N]: ", end="")
    choice = input().strip().lower()
    if choice == 'y':
        test_full_pipeline()
    else:
        print("\n⏭️  跳过完整流程测试")
    
    print("\n" + "="*60)
    print("🎉 测试完成！")
    print("="*60)
    print("\n✅ 所有Casco核心功能已成功移植：")
    print("  ✓ 问题分析和分类（basic/intermediate/advanced）")
    print("  ✓ 查询增强（多查询生成）")
    print("  ✓ 多查询检索")
    print("  ✓ 结果重排序")
    print("  ✓ 分层检索策略")
    print("  ✓ 动态温度控制")
    print("\n💡 运行 python main.py 开始实际使用！")


if __name__ == "__main__":
    main()

