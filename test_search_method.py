#!/usr/bin/env python3
"""测试 VectorStore.search 方法"""

from vector_store import VectorStore

print("=" * 60)
print("🔍 测试 VectorStore.search 方法")
print("=" * 60)

vs = VectorStore()

test_query = "slub"
print(f"\n查询: {test_query}")

# 测试 search 方法
results = vs.search(test_query, top_k=5)

print(f"\n找到 {len(results)} 个结果")

if results:
    for i, result in enumerate(results):
        print(f"\n结果 {i+1}:")
        print(f"  文件: {result.get('filename', 'N/A')}")
        print(f"  页码: {result.get('page_number', 'N/A')}")
        print(f"  距离: {result.get('distance', 'N/A')}")
        print(f"  内容: {result.get('content', '')[:200]}...")
else:
    print("\n❌ 没有找到任何结果")

print("\n" + "=" * 60)


