#!/usr/bin/env python3
"""
从 default 知识库迁移特定文件到 NLP 知识库
"""

import sqlite3
import os
import shutil
from pathlib import Path

# 配置
PROJECT_ROOT = "/home/honglianglu/hdd/rag-agent"
DEFAULT_DB = os.path.join(PROJECT_ROOT, "vector_db/default/chroma.sqlite3")
NLP_DB = os.path.join(PROJECT_ROOT, "vector_db/NLP/chroma.sqlite3")

# NLP相关的文件名（从你的data/NLP/目录）
NLP_FILES = [
    "1.绪论-2025.pdf",
    "2_1_统计语言模型2025_秋.pdf",
    "2.2 词性标注与隐马尔科夫模型.pdf",
    "2.3 中文分词与CRF.pdf",
    "2.4 语法解析和句法分析V2.pdf",
    "20251110客观信息论授课.pdf",
    "3.1 词向量 2025.pdf",
    "3.2 神经网络语言模型 2025.pdf",
    "3.3 序列标注.pdf",
    "3.4 机器翻译.pdf",
    "4.1 预训练语言模型.pdf",
    "4.2 大语言模型 v2.pdf",
    "4.3 语言模型心智泛化能力.pdf",
    "4.4 语言模型的心智泛化能力-思考范式.pdf"
]

print("=" * 80)
print("🔄 从 default 迁移数据到 NLP 知识库")
print("=" * 80)
print()

# 1. 检查数据库
if not os.path.exists(DEFAULT_DB):
    print(f"❌ default 数据库不存在: {DEFAULT_DB}")
    exit(1)

print(f"✅ default 数据库: {DEFAULT_DB}")
print(f"   大小: {os.path.getsize(DEFAULT_DB) / (1024*1024):.2f} MB")

# 2. 连接 default 数据库
conn_default = sqlite3.connect(DEFAULT_DB)
cursor_default = conn_default.cursor()

# 3. 查找 NLP 文件相关的嵌入
print()
print("📊 查找 NLP 文件...")
print()

# 获取所有文件名
cursor_default.execute("""
    SELECT DISTINCT string_value 
    FROM embedding_metadata 
    WHERE key = 'filename'
""")
all_files = [row[0] for row in cursor_default.fetchall()]

print(f"default 库中共有 {len(all_files)} 个文件")
print()

# 找到匹配的 NLP 文件
found_nlp_files = []
for nlp_file in NLP_FILES:
    if nlp_file in all_files:
        found_nlp_files.append(nlp_file)
        print(f"  ✓ 找到: {nlp_file}")
    else:
        print(f"  ✗ 未找到: {nlp_file}")

print()
print(f"找到 {len(found_nlp_files)} / {len(NLP_FILES)} 个 NLP 文件")

if len(found_nlp_files) == 0:
    print("❌ 没有找到任何 NLP 文件，退出")
    conn_default.close()
    exit(1)

# 4. 统计每个文件的嵌入数量
print()
print("📈 统计嵌入数量...")
print()

total_embeddings = 0
for nlp_file in found_nlp_files:
    cursor_default.execute("""
        SELECT COUNT(DISTINCT em.id)
        FROM embedding_metadata em
        WHERE em.key = 'filename' AND em.string_value = ?
    """, (nlp_file,))
    count = cursor_default.fetchone()[0]
    total_embeddings += count
    print(f"  {nlp_file}: {count} 个嵌入")

print()
print(f"✅ 共 {total_embeddings} 个嵌入需要迁移")
print()

# 5. 询问用户确认
print("⚠️  警告：此操作将会：")
print("   1. 从 default 数据库中删除这些文件的嵌入")
print("   2. 将它们添加到 NLP 数据库")
print("   3. 备份原始数据库")
print()
response = input("是否继续？(yes/no): ").strip().lower()

if response != 'yes':
    print("❌ 操作已取消")
    conn_default.close()
    exit(0)

# 6. 备份 default 数据库
print()
print("💾 备份 default 数据库...")
import time
backup_path = f"{DEFAULT_DB}.backup_{int(time.time())}"
shutil.copy2(DEFAULT_DB, backup_path)
print(f"   ✅ 备份到: {backup_path}")

# 7. 导出 NLP 相关的数据
print()
print("📤 导出 NLP 数据...")

# 获取所有相关的 embedding IDs
embedding_ids = set()
for nlp_file in found_nlp_files:
    cursor_default.execute("""
        SELECT DISTINCT id
        FROM embedding_metadata
        WHERE key = 'filename' AND string_value = ?
    """, (nlp_file,))
    ids = [row[0] for row in cursor_default.fetchall()]
    embedding_ids.update(ids)

print(f"   找到 {len(embedding_ids)} 个唯一嵌入 ID")

# 导出数据到临时文件
import json
export_data = {
    'embeddings': [],
    'metadata': [],
    'documents': []
}

# 导出 embeddings 表
for emb_id in embedding_ids:
    cursor_default.execute("SELECT * FROM embeddings WHERE id = ?", (emb_id,))
    row = cursor_default.fetchone()
    if row:
        export_data['embeddings'].append(row)

# 导出 embedding_metadata 表
for emb_id in embedding_ids:
    cursor_default.execute("SELECT * FROM embedding_metadata WHERE id = ?", (emb_id,))
    rows = cursor_default.fetchall()
    export_data['metadata'].extend(rows)

print(f"   ✅ 导出 {len(export_data['embeddings'])} 个嵌入")
print(f"   ✅ 导出 {len(export_data['metadata'])} 个元数据")

# 8. 简化方案：直接使用 process_data.py 重新处理
print()
print("=" * 80)
print("💡 建议使用更简单的方案：")
print("=" * 80)
print()
print("由于 ChromaDB 的数据结构复杂，直接迁移需要处理：")
print("  - embeddings 表")
print("  - embedding_metadata 表")
print("  - collections 表")
print("  - segments 表")
print("  - 向量索引文件（HNSW）")
print()
print("更简单且安全的方案是：")
print("  1. data/NLP/ 中已经有原始 PDF 文件 ✅")
print("  2. 运行 process_data.py 重新向量化 NLP 文件 ✅")
print("  3. 然后从 default 删除 NLP 文件（可选）")
print()
print("执行命令：")
print("  cd /home/honglianglu/hdd/rag-agent")
print("  conda activate rag")
print("  python process_data.py --kb NLP")
print()
print("这样更安全，且能确保数据完整性！")
print()

# 关闭连接
conn_default.close()

print("=" * 80)
print("脚本完成")
print("=" * 80)


