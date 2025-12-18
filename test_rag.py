#!/usr/bin/env python3
"""RAG 系统诊断脚本"""

print("=" * 60)
print("🔍 RAG 系统诊断")
print("=" * 60)

# 1. 检查向量数据库
print("\n1️⃣ 检查向量数据库...")
from vector_store import VectorStore
vs = VectorStore()
count = vs.collection.count()
print(f"   ✅ 文档数量: {count}")

# 2. 获取一个样本
print("\n2️⃣ 检查样本文档...")
results = vs.collection.get(limit=1, include=['documents', 'metadatas'])
if results['documents']:
    print(f"   样本文档: {results['documents'][0][:100]}...")
    print(f"   ✅ 有文档内容")
else:
    print(f"   ❌ 没有文档！")

# 3. 测试查询 embedding
print("\n3️⃣ 测试查询 embedding...")
test_query = "内存分配"
query_embedding = vs.get_embedding(test_query)
if query_embedding:
    print(f"   ✅ 查询 embedding 维度: {len(query_embedding)}")
else:
    print(f"   ❌ 查询 embedding 失败！")

# 4. 直接测试 ChromaDB 查询
print("\n4️⃣ 测试直接 ChromaDB 查询...")
try:
    results = vs.collection.query(
        query_texts=[test_query],
        n_results=3
    )
    num_results = len(results['ids'][0]) if results['ids'] else 0
    print(f"   找到 {num_results} 个结果")
    
    if num_results > 0:
        print(f"   ✅ 第一个结果:")
        print(f"      距离: {results['distances'][0][0]:.4f}")
        print(f"      内容: {results['documents'][0][0][:150]}...")
    else:
        print(f"   ❌ 没有找到任何结果！")
        print(f"   这说明 ChromaDB 查询本身有问题")
except Exception as e:
    print(f"   ❌ 查询失败: {e}")
    import traceback
    traceback.print_exc()

# 5. 测试 VectorStore.search 方法
print("\n5️⃣ 测试 VectorStore.search 方法...")
try:
    search_results = vs.search(test_query, top_k=3)
    print(f"   找到 {len(search_results)} 个结果")
    
    if search_results:
        print(f"   ✅ 第一个结果:")
        print(f"      内容: {search_results[0].get('content', '')[:150]}...")
        if 'distance' in search_results[0]:
            print(f"      距离: {search_results[0]['distance']:.4f}")
    else:
        print(f"   ❌ search 方法返回空！")
        print(f"   这说明 VectorStore.search 实现有问题")
except Exception as e:
    print(f"   ❌ search 失败: {e}")
    import traceback
    traceback.print_exc()

# 6. 测试 HybridRetriever
print("\n6️⃣ 测试 HybridRetriever...")
try:
    from hybrid_retriever import HybridRetriever
    retriever = HybridRetriever(text_store=vs)
    
    results = retriever.search(test_query, top_k=3)
    num_results = len(results.get('results', []))
    print(f"   找到 {num_results} 个结果")
    
    if num_results > 0:
        print(f"   ✅ 第一个结果:")
        result = results['results'][0]
        print(f"      类型: {result.get('type', 'unknown')}")
        print(f"      内容: {result.get('content', '')[:150]}...")
    else:
        print(f"   ❌ HybridRetriever 返回空！")
        print(f"   这说明 HybridRetriever 实现有问题")
except Exception as e:
    print(f"   ❌ HybridRetriever 失败: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 60)
print("诊断完成！")
print("=" * 60)

