#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
强制重建知识图谱（使用新的8字规则）
"""

import sys
import os

# 添加路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from knowledge_graph import KnowledgeGraph
from vector_store import VectorStore
from config import *

def rebuild_knowledge_graph():
    """从向量库重建知识图谱"""
    
    print("🔄 正在重建知识图谱...\n")
    
    # 1. 删除旧文件
    if os.path.exists("knowledge_graph.json"):
        os.remove("knowledge_graph.json")
        print("✅ 已删除旧的 knowledge_graph.json\n")
    
    # 2. 初始化知识图谱
    kg = KnowledgeGraph()
    print("📊 初始化知识图谱完成\n")
    
    # 3. 从向量库提取
    try:
        print("📚 连接向量库...")
        vector_store = VectorStore()
        
        # 获取所有文档
        print("📖 获取文档内容...")
        results = vector_store.collection.get(
            limit=500,  # 获取更多文档
            include=['documents', 'metadatas']
        )
        
        if not results or not results.get('documents'):
            print("❌ 向量库中没有文档")
            return
        
        documents = results['documents']
        metadatas = results.get('metadatas', [])
        
        print(f"✅ 找到 {len(documents)} 个文档片段\n")
        
        # 4. 按文档分组处理
        doc_groups = {}
        for doc, meta in zip(documents, metadatas):
            filename = meta.get('filename', '未知')
            if filename not in doc_groups:
                doc_groups[filename] = []
            doc_groups[filename].append(doc)
        
        print(f"📂 共 {len(doc_groups)} 个文档\n")
        
        # 5. 逐个文档提取知识图谱
        total_entities = 0
        total_relations = 0
        
        for i, (filename, texts) in enumerate(doc_groups.items(), 1):
            # 合并同一文档的所有片段
            full_text = ' '.join(texts)
            
            # 限制长度（避免太长）
            if len(full_text) > 8000:
                full_text = full_text[:8000]
            
            print(f"📄 [{i}/{len(doc_groups)}] 处理: {filename}")
            print(f"   文本长度: {len(full_text)} 字符")
            
            try:
                num_e, num_r = kg.add_entities_and_relations(full_text, filename)
                print(f"   ✅ 提取了 {num_e} 个实体, {num_r} 个关系")
                total_entities += num_e
                total_relations += num_r
            except Exception as e:
                print(f"   ⚠️  提取失败: {e}")
            
            print()
        
        # 6. 显示结果
        print("=" * 60)
        print(f"🎉 重建完成！")
        print(f"📊 总计: {len(kg.entities)} 个实体, {len(kg.relationships)} 个关系")
        print("=" * 60)
        
        # 7. 显示实体示例（按字数排序）
        print(f"\n📝 实体示例（按字数排序，前20个）：\n")
        entities_sorted = sorted(kg.entities.items(), key=lambda x: len(x[0]), reverse=True)
        
        for i, (name, info) in enumerate(entities_sorted[:20], 1):
            char_count = len(name)
            entity_type = info.get('type', '未知')
            freq = info.get('frequency', 0)
            
            # 高亮显示长实体
            if char_count >= 5:
                mark = "✨"
            else:
                mark = "  "
            
            print(f"   {mark} {i:2d}. {name} ({char_count}字) - {entity_type} - 出现{freq}次")
        
        print("\n" + "=" * 60)
        print("💡 提示：")
        print("   - 如果看到5字以上的完整术语（如'隐马尔可夫模型'），说明成功！")
        print("   - 如果仍然只有4字词，请检查代码中是否还有 {2,4} 的正则")
        print("=" * 60)
        
    except Exception as e:
        print(f"❌ 错误: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    rebuild_knowledge_graph()

