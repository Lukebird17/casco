#!/bin/bash

echo "================================================"
echo "📦 数据结构迁移脚本"
echo "================================================"
echo ""
echo "⚠️  此脚本会重构现有的数据结构："
echo "   - data/ → data/default/"
echo "   - vector_db/ → vector_db/default/"
echo ""
read -p "确认继续？(yes/no): " confirm

if [ "$confirm" != "yes" ]; then
    echo "❌ 已取消迁移"
    exit 1
fi

cd /home/honglianglu/hdd/rag-agent

echo ""
echo "1️⃣ 备份现有数据..."
if [ -d "data" ] && [ ! -d "data_backup" ]; then
    cp -r data data_backup
    echo "   ✅ 备份 data → data_backup"
fi

if [ -d "vector_db" ] && [ ! -d "vector_db_backup" ]; then
    cp -r vector_db vector_db_backup
    echo "   ✅ 备份 vector_db → vector_db_backup"
fi

echo ""
echo "2️⃣ 创建新目录结构..."

# 创建新的data结构
if [ -d "data" ] && [ ! -d "data/default" ]; then
    echo "   📁 重构 data 目录..."
    mkdir -p data_new/default
    
    # 移动所有文件到default目录
    find data -maxdepth 1 -type f -exec mv {} data_new/default/ \;
    
    # 移动所有子目录的文件
    for dir in data/*/; do
        if [ -d "$dir" ]; then
            find "$dir" -type f -exec mv {} data_new/default/ \;
        fi
    done
    
    # 替换旧目录
    rm -rf data
    mv data_new data
    
    echo "   ✅ data → data/default/"
fi

# 创建新的vector_db结构
if [ -d "vector_db" ] && [ ! -d "vector_db/default" ]; then
    echo "   📁 重构 vector_db 目录..."
    mkdir -p vector_db_new/default
    
    # 移动所有文件到default目录
    mv vector_db/* vector_db_new/default/ 2>/dev/null
    
    # 替换旧目录
    rm -rf vector_db
    mv vector_db_new vector_db
    
    echo "   ✅ vector_db → vector_db/default/"
fi

echo ""
echo "3️⃣ 验证新结构..."

if [ -d "data/default" ]; then
    file_count=$(find data/default -type f | wc -l)
    echo "   ✅ data/default/ 包含 $file_count 个文件"
else
    echo "   ❌ data/default/ 不存在"
fi

if [ -d "vector_db/default" ]; then
    if [ -f "vector_db/default/chroma.sqlite3" ]; then
        size=$(du -h vector_db/default/chroma.sqlite3 | cut -f1)
        echo "   ✅ vector_db/default/chroma.sqlite3 ($size)"
    else
        echo "   ⚠️  vector_db/default/ 存在但无数据库文件"
    fi
else
    echo "   ❌ vector_db/default/ 不存在"
fi

echo ""
echo "================================================"
echo "✅ 迁移完成！"
echo "================================================"
echo ""
echo "📌 新的目录结构："
echo "   rag-agent/"
echo "   ├── data/"
echo "   │   └── default/          ← 默认知识库的原文件"
echo "   └── vector_db/"
echo "       └── default/          ← 默认知识库的向量库"
echo ""
echo "📌 备份位置："
echo "   - data_backup/"
echo "   - vector_db_backup/"
echo ""
echo "💡 如果一切正常，可以删除备份："
echo "   rm -rf data_backup vector_db_backup"
echo ""



