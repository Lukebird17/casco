#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   rebuild_vectors.py
@Desc    :   从现有的doecment.json重新生成vectors.json
'''

import json
import os
from VectorBase import VectorStore
from my_BGE_embedding import BGEEmbedding
from tqdm import tqdm

def rebuild_vectors_for_storage(storage_path: str = './storage'):
    """
    为指定的存储路径重新生成vectors.json
    
    Args:
        storage_path: 存储路径，默认为'./storage'
    """
    print(f"\n🔧 开始为 {storage_path} 重新生成vectors.json...")
    
    # 1. 检查doecment.json是否存在
    doc_path = f"{storage_path}/doecment.json"
    if not os.path.exists(doc_path):
        print(f"❌ 错误: {doc_path} 不存在！")
        return False
    
    # 2. 加载文档
    print(f"📂 加载文档: {doc_path}")
    with open(doc_path, 'r', encoding='utf-8') as f:
        documents = json.load(f)
    print(f"✅ 已加载 {len(documents)} 个文档片段")
    
    # 3. 初始化BGE嵌入模型
    print("🤖 初始化BGE嵌入模型...")
    embedding_model = BGEEmbedding()
    print("✅ 模型初始化完成")
    
    # 4. 创建向量存储并生成向量
    print("⚡ 开始生成向量 (这可能需要几分钟，取决于文档数量)...")
    vector_store = VectorStore(documents)
    vector_store.get_vector(embedding_model)
    print("✅ 向量生成完成")
    
    # 5. 只保存vectors.json (doecment.json已经存在)
    print(f"💾 保存vectors.json到 {storage_path}...")
    vectors_path = f"{storage_path}/vectors.json"
    with open(vectors_path, 'w', encoding='utf-8') as f:
        json.dump(vector_store.vectors, f)
    
    print(f"✅ 成功！vectors.json已保存至: {vectors_path}")
    print(f"📊 向量数量: {len(vector_store.vectors)}")
    
    return True

def main():
    """主函数"""
    print("╔══════════════════════════════════════════════════════╗")
    print("║         重建vectors.json工具                         ║")
    print("╚══════════════════════════════════════════════════════╝")
    
    # 重建storage目录的vectors.json
    success = rebuild_vectors_for_storage('./storage')
    
    if success:
        print("\n✅ 重建完成！现在可以运行 docker compose up 了。")
    else:
        print("\n❌ 重建失败，请检查错误信息。")

if __name__ == "__main__":
    main()

