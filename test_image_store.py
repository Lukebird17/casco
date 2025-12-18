#!/usr/bin/env python3
"""测试 ImageVectorStore"""

print("=" * 60)
print("🔍 测试 ImageVectorStore")
print("=" * 60)

print("\n尝试导入 ImageVectorStore...")
try:
    from image_vector_store import ImageVectorStore
    print("✅ 导入成功")
except Exception as e:
    print(f"❌ 导入失败: {e}")
    import traceback
    traceback.print_exc()
    exit(1)

print("\n尝试初始化 ImageVectorStore (会加载CLIP模型，可能需要一些时间)...")
try:
    image_store = ImageVectorStore()
    print("✅ 初始化成功")
except Exception as e:
    print(f"❌ 初始化失败: {e}")
    import traceback
    traceback.print_exc()
    exit(1)

print("\n尝试文本搜索图片...")
try:
    results = image_store.search_by_text("slub", top_k=3)
    print(f"✅ 搜索成功，找到 {len(results)} 个结果")
except Exception as e:
    print(f"❌ 搜索失败: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 60)


