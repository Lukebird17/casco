#!/usr/bin/env python3
"""测试 HybridRetriever"""

from vector_store import VectorStore
from hybrid_retriever import HybridRetriever

print("=" * 60)
print("🔍 测试 HybridRetriever")
print("=" * 60)

vs = VectorStore()
retriever = HybridRetriever(text_store=vs)

test_query = "slub"
print(f"\n查询: {test_query}")

# 测试 HybridRetriever
results = retriever.search(test_query, top_k=5, include_images=True)

print(f"\n文本结果: {len(results['text_results'])} 个")
print(f"图片结果: {len(results['image_results'])} 个")
print(f"合并结果: {len(results['combined'])} 个")

if results['combined']:
    print(f"\n前3个合并结果:")
    for i, result in enumerate(results['combined'][:3]):
        print(f"\n结果 {i+1}:")
        print(f"  类型: {result.get('type', 'text')}")
        print(f"  文件: {result.get('filename', 'N/A')}")
        if result.get('type') == 'image':
            print(f"  描述: {result.get('description', '')[:100]}")
        else:
            print(f"  内容: {result.get('content', '')[:100]}")
else:
    print("\n❌ combined 为空!")

print("\n" + "=" * 60)





