#!/bin/bash
# 使用 uv 创建虚拟环境并安装依赖（推荐方式）

set -e  # 遇到错误立即退出

# 颜色定义
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}======================================"
echo "使用 uv 创建 RAG 问答环境"
echo "======================================${NC}"

# 获取脚本所在目录（agent 目录）
AGENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
# 项目根目录
PROJECT_ROOT="$(dirname "$AGENT_DIR")"

echo -e "${BLUE}Agent 目录: $AGENT_DIR${NC}"
echo -e "${BLUE}项目根目录: $PROJECT_ROOT${NC}"

# 检查 Python 版本
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo -e "${GREEN}✓ Python 版本: $python_version${NC}"

# 设置 uv 路径
UV_PATH="$PROJECT_ROOT/uv-x86_64-unknown-linux-gnu/uv"

# 检查 uv
echo ""
echo -e "${BLUE}检查 uv 包管理器...${NC}"
if [ -f "$UV_PATH" ]; then
    echo -e "${GREEN}✓ 找到本地 uv: $UV_PATH${NC}"
    export PATH="$(dirname $UV_PATH):$PATH"
elif command -v uv &> /dev/null; then
    echo -e "${GREEN}✓ 找到系统 uv${NC}"
    UV_PATH="uv"
else
    echo -e "${YELLOW}⚠ 未找到 uv，正在安装...${NC}"
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.cargo/bin:$PATH"
    UV_PATH="uv"
fi

# 验证 uv
uv_version=$($UV_PATH --version 2>&1)
echo -e "${GREEN}✓ uv 版本: $uv_version${NC}"

# 切换到 agent 目录
cd "$AGENT_DIR"

# 创建虚拟环境
echo ""
echo -e "${BLUE}步骤 1/5: 创建 Python 虚拟环境...${NC}"
if [ -d ".venv" ]; then
    echo -e "${YELLOW}⚠ 虚拟环境已存在，跳过创建${NC}"
else
    $UV_PATH venv .venv
    echo -e "${GREEN}✓ 虚拟环境创建完成${NC}"
fi

# 激活虚拟环境
echo ""
echo -e "${BLUE}激活虚拟环境...${NC}"
source .venv/bin/activate
echo -e "${GREEN}✓ 虚拟环境已激活${NC}"

# 安装 RAG-Anything
echo ""
echo -e "${BLUE}步骤 2/5: 安装 RAG-Anything（使用 uv）...${NC}"
cd "$PROJECT_ROOT/RAG-Anything"
$UV_PATH pip install -e .
echo -e "${GREEN}✓ RAG-Anything 安装完成${NC}"
cd "$AGENT_DIR"

# 安装基础依赖
echo ""
echo -e "${BLUE}步骤 3/5: 安装基础依赖...${NC}"
$UV_PATH pip install python-dotenv openai
echo -e "${GREEN}✓ 基础依赖安装完成${NC}"

# 安装 LangChain
echo ""
echo -e "${BLUE}步骤 4/5: 安装 LangChain...${NC}"
$UV_PATH pip install langchain langchain-openai langchain-core
echo -e "${GREEN}✓ LangChain 安装完成${NC}"

# 安装其他工具
echo ""
echo -e "${BLUE}步骤 5/5: 安装其他工具...${NC}"
$UV_PATH pip install tiktoken numpy
echo -e "${GREEN}✓ 其他工具安装完成${NC}"

# 完成
echo ""
echo -e "${GREEN}======================================"
echo "✅ 安装完成！"
echo "======================================${NC}"
echo ""
echo -e "${BLUE}虚拟环境位置:${NC} $AGENT_DIR/.venv"
echo -e "${BLUE}激活命令:${NC} source $AGENT_DIR/.venv/bin/activate"
echo ""
echo -e "${YELLOW}下一步：${NC}"
echo "1. 激活虚拟环境:"
echo "   ${GREEN}source .venv/bin/activate${NC}"
echo ""
echo "2. 配置环境变量:"
echo "   ${GREEN}cp env_example.sh env.sh${NC}"
echo "   ${GREEN}nano env.sh  # 编辑填入 API Key${NC}"
echo "   ${GREEN}source env.sh${NC}"
echo ""
echo "3. 运行程序:"
echo "   ${GREEN}python quick_start.py${NC}"
echo "   ${GREEN}# 或${NC}"
echo "   ${GREEN}./run.sh${NC}"
echo ""
echo -e "${BLUE}======================================"
echo "💡 提示："
echo "- uv 比 pip 快 10-100 倍"
echo "- 虚拟环境会自动隔离依赖"
echo "- 每次使用前记得激活环境"
echo "- 所有路径已自动适配"
echo "======================================${NC}"
