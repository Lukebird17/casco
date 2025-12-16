#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
验证多模态 RAG Agent 修复
"""

# 模拟混合检索结果（包含文本和图片）
mock_results = [
    {
        'type': 'text',
        'content': 'slab 分配器是一种内存分配机制...',
        'filename': 'OS-08 pm-manage.pdf',
        'page_number': 28,
        'distance': 0.15,
    },
    {
        'type': 'image',
        'image_path': '.mineru_output/xxx/images/slab_diagram.jpg',
        'description': '图片来源: OS-08 pm-manage.pdf, 第28页\nSlab分配示意图',
        'filename': 'OS-08 pm-manage.pdf',
        'page_number': 28,
        'distance': 0.20,
        'metadata': {
            'filename': 'OS-08 pm-manage.pdf',
            'page_number': 28,
            'context': 'Next_free 指向下一个空闲对象...',
        }
    }
]

def test_rerank():
    """测试重排序是否支持多模态"""
    print("=" * 60)
    print("测试1: 重排序方法（多模态）")
    print("=" * 60)
    
    from rag_agent import RAGAgent
    
    agent = RAGAgent(use_multimodal=False)  # 先不启用混合检索，只测试重排序
    
    query = "第28页的slab示意图中的Next_free"
    
    try:
        reranked = agent.rerank_results(query, mock_results.copy())
        print("✅ 重排序成功!")
        print(f"   结果数量: {len(reranked)}")
        for i, result in enumerate(reranked, 1):
            print(f"   {i}. 类型: {result.get('type', 'text')}")
            print(f"      匹配率: {result.get('match_ratio', 0):.1%}")
            print(f"      重排分数: {result.get('rerank_score', 0):.3f}")
    except Exception as e:
        print(f"❌ 重排序失败: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True

def test_format_context():
    """测试上下文格式化是否支持多模态"""
    print("\n" + "=" * 60)
    print("测试2: 上下文格式化（多模态）")
    print("=" * 60)
    
    from rag_agent import RAGAgent
    
    agent = RAGAgent(use_multimodal=False)
    
    # 添加 match_ratio（重排序后会有）
    results_with_scores = []
    for r in mock_results:
        r_copy = r.copy()
        r_copy['match_ratio'] = 0.5
        results_with_scores.append(r_copy)
    
    try:
        context = agent._format_context(results_with_scores)
        print("✅ 格式化成功!")
        print("\n生成的上下文:")
        print("-" * 60)
        print(context[:500])
        if len(context) > 500:
            print("...(省略)")
        print("-" * 60)
    except Exception as e:
        print(f"❌ 格式化失败: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True

def test_structured_context():
    """测试结构化上下文是否支持多模态"""
    print("\n" + "=" * 60)
    print("测试3: 结构化上下文（多模态）")
    print("=" * 60)
    
    from rag_agent import RAGAgent
    
    agent = RAGAgent(use_multimodal=False)
    
    # 添加 match_ratio
    results_with_scores = []
    for r in mock_results:
        r_copy = r.copy()
        r_copy['match_ratio'] = 0.5
        results_with_scores.append(r_copy)
    
    try:
        context = agent._build_structured_context(results_with_scores, "slab示意图")
        print("✅ 格式化成功!")
        print("\n生成的结构化上下文:")
        print("-" * 60)
        print(context[:500])
        if len(context) > 500:
            print("...(省略)")
        print("-" * 60)
    except Exception as e:
        print(f"❌ 格式化失败: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True

if __name__ == "__main__":
    print("\n🧪 验证多模态 RAG Agent 修复\n")
    
    all_passed = True
    
    # 测试1
    if not test_rerank():
        all_passed = False
    
    # 测试2
    if not test_format_context():
        all_passed = False
    
    # 测试3
    if not test_structured_context():
        all_passed = False
    
    # 总结
    print("\n" + "=" * 60)
    if all_passed:
        print("✅ 所有测试通过！系统已支持多模态检索")
    else:
        print("❌ 部分测试失败，请检查错误信息")
    print("=" * 60)

