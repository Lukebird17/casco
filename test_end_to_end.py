#!/usr/bin/env python3
"""端到端测试"""

from rag_agent import RAGAgent

print("=" * 60)
print("🔍 端到端测试 RAGAgent")
print("=" * 60)

# 初始化 RAGAgent（不使用多模态以避免CLIP加载）
agent = RAGAgent(
    model="Qwen/Qwen2.5-72B-Instruct",
    enable_tracking=False,
    enable_cot=False,
    use_multimodal=False  # 关闭多模态以加快测试
)

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
        print(f"  文件: {result.get('filename', 'N/A')}")
        print(f"  页码: {result.get('page_number', 'N/A')}")
        print(f"  内容: {result.get('content', '')[:150]}...")
else:
    print("\n❌ 没有找到任何结果！")
    print("问题可能在 RAGAgent.multi_query_retrieve 或 enhance_query")

print("\n" + "=" * 60)





