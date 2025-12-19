#!/bin/bash

# 清理知识图谱缓存脚本

echo "🗑️  正在清理知识图谱缓存..."

# 清理知识图谱JSON文件
if [ -f "knowledge_graph.json" ]; then
    rm -f knowledge_graph.json
    echo "✅ 已删除 knowledge_graph.json"
fi

# 清理测试文件
if [ -f "test_kg.json" ]; then
    rm -f test_kg.json
    echo "✅ 已删除 test_kg.json"
fi

if [ -f "test_kg.html" ]; then
    rm -f test_kg.html
    echo "✅ 已删除 test_kg.html"
fi

# 清理Python缓存
echo "🧹 清理Python缓存..."
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
find . -type f -name "*.pyc" -delete 2>/dev/null
echo "✅ Python缓存已清理"

echo ""
echo "🎉 清理完成！"
echo ""
echo "📝 下一步操作："
echo "1. 重启系统: ./restart_all.sh"
echo "2. 重新上传文档（让系统重新提取知识图谱）"
echo "3. 点击'知识图谱'查看新结果"
echo ""

