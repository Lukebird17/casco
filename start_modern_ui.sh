#!/bin/bash

# RAG Agent 现代化UI启动脚本

echo "=================================="
echo "  RAG Agent - 现代化UI"
echo "=================================="
echo ""

# 检查conda环境
if ! conda info --envs | grep -q "rag"; then
    echo "❌ 错误: conda环境'rag'不存在"
    echo "请先创建环境: conda create -n rag python=3.10"
    exit 1
fi

# 激活环境
echo "🔄 激活conda环境..."
source $(conda info --base)/etc/profile.d/conda.sh
conda activate rag

# 检查必要的包
echo "🔍 检查依赖..."
python -c "import gradio" 2>/dev/null || {
    echo "❌ Gradio未安装，正在安装..."
    pip install gradio
}

# 启动应用
echo ""
echo "🚀 启动现代化UI..."
echo "=================================="
echo ""
echo "📱 访问地址: http://localhost:7860"
echo "💡 提示: 按 Ctrl+C 退出"
echo ""
echo "=================================="
echo ""

python app_modern.py

