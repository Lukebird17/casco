#!/bin/bash

echo "================================================"
echo "🔧 修复目录结构"
echo "================================================"
echo ""

cd /home/honglianglu/hdd/rag-agent

# 1. 确保目录存在
echo "1️⃣ 创建目录结构..."
mkdir -p data/default
mkdir -p vector_db/default

# 2. 移动data/下的文件到data/default/
echo ""
echo "2️⃣ 整理文件..."

# 统计data/下直接存在的文件
file_count=0
for file in data/*; do
    if [ -f "$file" ]; then
        filename=$(basename "$file")
        echo "   移动: $filename → data/default/"
        mv "$file" "data/default/"
        file_count=$((file_count + 1))
    fi
done

if [ $file_count -eq 0 ]; then
    echo "   ✅ data/ 下没有需要移动的文件"
else
    echo "   ✅ 已移动 $file_count 个文件到 data/default/"
fi

# 3. 验证结构
echo ""
echo "3️⃣ 验证目录结构..."

if [ -d "data/default" ]; then
    default_files=$(find data/default -type f | wc -l)
    echo "   ✅ data/default/ 包含 $default_files 个文件"
    ls -lh data/default/ | head -10
else
    echo "   ❌ data/default/ 不存在"
fi

echo ""
if [ -d "vector_db/default" ]; then
    if [ -f "vector_db/default/chroma.sqlite3" ]; then
        size=$(du -h vector_db/default/chroma.sqlite3 | cut -f1)
        echo "   ✅ vector_db/default/chroma.sqlite3 存在 ($size)"
    else
        echo "   ⚠️  vector_db/default/ 存在但无数据库文件"
    fi
else
    echo "   ❌ vector_db/default/ 不存在"
fi

# 4. 检查其他知识库
echo ""
echo "4️⃣ 检测其他知识库..."

kb_count=0
for kb_dir in vector_db/*/; do
    if [ -d "$kb_dir" ]; then
        kb_name=$(basename "$kb_dir")
        kb_count=$((kb_count + 1))
        
        # 确保对应的data目录存在
        if [ ! -d "data/$kb_name" ]; then
            echo "   ⚠️  创建缺失的 data/$kb_name/"
            mkdir -p "data/$kb_name"
        fi
        
        echo "   ✓ $kb_name"
    fi
done

echo "   总共 $kb_count 个知识库"

echo ""
echo "================================================"
echo "✅ 目录结构修复完成！"
echo "================================================"
echo ""
echo "📌 新的目录结构："
echo "   data/"
echo "   └── default/          ← 默认知识库的原文件"
echo "   vector_db/"
echo "   └── default/          ← 默认知识库的向量"
echo ""
echo "💡 现在可以重启后端："
echo "   cd /home/honglianglu/hdd/rag-agent"
echo "   ./start_backend.sh"
echo ""



