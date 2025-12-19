#!/bin/bash

echo "🦙 LlamaIndex 知识图谱 - 一键安装脚本"
echo "============================================================"
echo ""

# 检测 Python 环境
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误：未找到 python3"
    exit 1
fi

echo "📦 正在安装 LlamaIndex..."
echo ""

# 安装 LlamaIndex
pip install llama-index>=0.9.0 llama-index-core>=0.9.0 llama-index-llms-openai>=0.1.0

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ LlamaIndex 安装成功！"
    echo ""
else
    echo ""
    echo "❌ LlamaIndex 安装失败"
    echo "请手动运行：pip install llama-index llama-index-core llama-index-llms-openai"
    exit 1
fi

# 清理旧数据
echo "🧹 清理旧的知识图谱数据..."
if [ -f "knowledge_graph.json" ]; then
    rm -f knowledge_graph.json
    echo "✅ 已删除 knowledge_graph.json"
fi

echo ""
echo "============================================================"
echo "🎉 安装完成！"
echo "============================================================"
echo ""
echo "📝 下一步操作："
echo "1. 重启服务: ./restart_all.sh"
echo "2. 查看日志，确认看到:"
echo "   ✅ LlamaIndex 知识图谱可用"
echo "   ✅ 使用 LlamaIndex 知识图谱"
echo "3. 重新上传文档"
echo "4. 查看知识图谱（应该看到完整的实体名称）"
echo ""
echo "📚 详细文档: LLAMAINDEX_KG_GUIDE.md"
echo ""

