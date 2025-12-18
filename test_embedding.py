#!/usr/bin/env python3
"""测试 embedding 维度"""

from openai import OpenAI
from config import OPENAI_API_KEY, OPENAI_API_BASE, OPENAI_EMBEDDING_MODEL

print("=" * 60)
print("🔍 测试 Embedding API")
print("=" * 60)

print(f"\nAPI Base: {OPENAI_API_BASE}")
print(f"Model: {OPENAI_EMBEDDING_MODEL}")

client = OpenAI(api_key=OPENAI_API_KEY, base_url=OPENAI_API_BASE)

test_text = "测试文本"
print(f"\n测试文本: {test_text}")

try:
    response = client.embeddings.create(
        input=test_text,
        model=OPENAI_EMBEDDING_MODEL
    )
    
    embedding = response.data[0].embedding
    print(f"\n✅ Embedding 维度: {len(embedding)}")
    print(f"   前5个值: {embedding[:5]}")
    
except Exception as e:
    print(f"\n❌ 错误: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 60)


