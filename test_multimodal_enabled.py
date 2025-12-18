#!/usr/bin/env python3
"""测试启用多模态时的检索"""

from rag_agent import RAGAgent

print("=" * 60)
print("🔍 测试 RAGAgent (use_multimodal=True)")
print("=" * 60)

print("\n正在初始化 RAGAgent (这可能需要一些时间加载CLIP模型)...")

# 初始化 RAGAgent，启用多模态
agent = RAGAgent(
    model="Qwen/Qwen2.5-72B-Instruct",
    enable_tracking=False,
    enable_cot=False,
    use_multimodal=True  # 启用多模态
)

print("✅ RAGAgent 初始化完成")

test_query = "slub"
print(f"\n查询: {test_query}")

# 调用 multi_query_retrieve
print("\n📚 测试 multi_query_retrieve...")
results = agent.multi_query_retrieve(test_query, k=3)

print(f"\n找到 {len(results)} 个结果")

if results:
    print(f"\n前3个结果:")
    for i, result in enumerate(results[:3]):
        print(f"\n结果 {i+1}:")
        print(f"  类型: {result.get('type', 'text')}")
        print(f"  文件: {result.get('filename', 'N/A')}")
        if result.get('type') == 'image':
            print(f"  描述: {result.get('description', '')[:100]}")
        else:
            print(f"  内容: {result.get('content', '')[:150]}")
else:
    print("\n❌ 没有找到任何结果！")
    print("问题在 use_multimodal=True 时")

print("\n" + "=" * 60)





