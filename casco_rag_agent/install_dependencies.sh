#!/bin/bash
# 安装依赖脚本（使用 uv 包管理器）

echo "======================================"
echo "安装 RAG 问答系统依赖（使用 uv）"
echo "======================================"

# 检查 Python 版本
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "检测到 Python 版本: $python_version"

# 检查 uv 是否可用
echo ""
echo "检查 uv 包管理器..."
UV_PATH="/home/honglianglu/ssd/casco/uv-x86_64-unknown-linux-gnu/uv"

if [ -f "$UV_PATH" ]; then
    echo "✅ 找到 uv: $UV_PATH"
    export PATH="/home/honglianglu/ssd/casco/uv-x86_64-unknown-linux-gnu:$PATH"
elif command -v uv &> /dev/null; then
    echo "✅ 找到系统 uv"
    UV_PATH="uv"
else
    echo "❌ 未找到 uv，正在安装..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.cargo/bin:$PATH"
    UV_PATH="uv"
fi

# 验证 uv
$UV_PATH --version || {
    echo "❌ uv 不可用"
    exit 1
}

# 进入 RAG-Anything 目录
echo ""
echo "步骤 1/4: 使用 uv 安装 RAG-Anything..."
cd /home/honglianglu/ssd/casco/RAG-Anything || exit 1

# 使用 uv pip 安装
$UV_PATH pip install -e . || {
    echo "❌ RAG-Anything 安装失败"
    exit 1
}

# 返回项目根目录
cd /home/honglianglu/ssd/casco || exit 1

# 安装基础依赖
echo ""
echo "步骤 2/4: 使用 uv 安装基础依赖..."
$UV_PATH pip install python-dotenv openai || {
    echo "❌ 基础依赖安装失败"
    exit 1
}

# 安装 LangChain 相关
echo ""
echo "步骤 3/4: 使用 uv 安装 LangChain 依赖..."
$UV_PATH pip install langchain langchain-openai langchain-core || {
    echo "❌ LangChain 依赖安装失败"
    exit 1
}

# 安装其他工具
echo ""
echo "步骤 4/4: 使用 uv 安装其他工具..."
$UV_PATH pip install tiktoken numpy || {
    echo "❌ 其他工具安装失败"
    exit 1
}

echo ""
echo "======================================"
echo "✅ 所有依赖安装完成（使用 uv）！"
echo "======================================"
echo ""
echo "下一步："
echo "1. 配置环境变量:"
echo "   cp env_example.sh env.sh"
echo "   # 编辑 env.sh 填入您的 API Key"
echo "   source env.sh"
echo ""
echo "2. 运行快速启动脚本:"
echo "   python quick_start.py"
echo ""
echo "或者直接运行主程序:"
echo "   python rag_qa_agent.py"
echo ""
echo "💡 提示: 本系统使用 uv 包管理器，速度更快！"
echo "======================================"

