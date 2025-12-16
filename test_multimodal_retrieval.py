#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
测试多模态检索功能
"""

from hybrid_retriever import HybridRetriever

def test_text_query():
    """测试纯文本查询"""
    print("=" * 60)
    print("测试1: 纯文本查询")
    print("=" * 60)
    
    retriever = HybridRetriever()
    
    # 测试查询
    queries = [
        "虚拟内存的页表结构",
        "物理内存分配",
        "操作系统内存管理",
    ]
    
    for query in queries:
        print(f"\n查询: {query}")
        print("-" * 40)
        
        results = retriever.search(query, top_k=5)
        
        print(f"文本结果: {len(results['text_results'])} 个")
        print(f"图片结果: {len(results['image_results'])} 张")
        print(f"合并结果: {len(results['combined'])} 个")
        
        print("\n前3个结果:")
        for i, item in enumerate(results['combined'][:3], 1):
            if item['type'] == 'text':
                print(f"  {i}. [文本] {item.get('content', '')[:50]}...")
                print(f"     来源: {item.get('filename', 'N/A')} (页{item.get('page_number', 0)})")
            elif item['type'] == 'image':
                print(f"  {i}. [图片] {item.get('image_path', 'N/A').split('/')[-1]}")
                print(f"     来源: {item.get('filename', 'N/A')} (页{item.get('page_number', 0)})")
            print(f"     相似度: {1-item.get('distance', 1):.2%}")


def test_context_formatting():
    """测试 Context 格式化"""
    print("\n" + "=" * 60)
    print("测试2: Context 格式化（用于 LLM）")
    print("=" * 60)
    
    retriever = HybridRetriever()
    
    query = "虚拟内存页表"
    print(f"\n查询: {query}")
    print("-" * 40)
    
    results = retriever.search(query, top_k=5)
    context = retriever.format_context_for_llm(results, max_length=2000)
    
    print(f"\n生成的 Context 项数: {len(context)}")
    
    for i, item in enumerate(context, 1):
        print(f"\n{i}. 类型: {item['type']}")
        if item['type'] == 'text':
            print(f"   内容: {item['content'][:80]}...")
        elif item['type'] == 'image':
            print(f"   路径: {item['path']}")
            print(f"   描述: {item.get('description', '')[:80]}...")
        print(f"   来源: {item.get('source', 'N/A')}")


def test_stats():
    """测试统计信息"""
    print("\n" + "=" * 60)
    print("测试3: 系统统计")
    print("=" * 60)
    
    retriever = HybridRetriever()
    stats = retriever.get_stats()
    
    print(f"\n文本文档数: {stats['text_documents']}")
    print(f"图片数量: {stats['images']}")
    print(f"文本权重: {stats['text_weight']:.1%}")
    print(f"图片权重: {stats['image_weight']:.1%}")


if __name__ == "__main__":
    try:
        # 测试1: 纯文本查询
        test_text_query()
        
        # 测试2: Context 格式化
        test_context_formatting()
        
        # 测试3: 统计信息
        test_stats()
        
        print("\n" + "=" * 60)
        print("✅ 所有测试完成")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()

