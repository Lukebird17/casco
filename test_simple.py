#!/usr/bin/env python3
"""简单快速的RAG测试"""

from vector_store import VectorStore

print("测试查询...")
vs = VectorStore()

# 测试直接查询
test_query = "内存分配"
print(f"\n查询: {test_query}")

# 方法1: 直接用 ChromaDB
results = vs.collection.query(query_texts=[test_query], n_results=3)
print(f"ChromaDB 查询结果: {len(results['ids'][0]) if results['ids'] else 0} 个")

# 方法2: 用 VectorStore.search
search_results = vs.search(test_query, top_k=3)
print(f"VectorStore.search 结果: {len(search_results)} 个")

if search_results:
    print(f"\n第一个结果:")
    print(f"  {search_results[0].get('content', '')[:200]}")
else:
    print("\n❌ VectorStore.search 返回空!")
    print("让我检查 search 方法...")
    
print("\n完成!")





