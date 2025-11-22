#!/bin/bash
# 使用 Conda 创建环境并安装依赖

set -e  # 遇到错误立即退出

# 颜色定义
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}======================================"
echo "使用 Conda 创建 RAG 问答环境"
echo "======================================${NC}"

# 获取脚本所在目录（agent 目录）
AGENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
# 项目根目录
PROJECT_ROOT="$(dirname "$AGENT_DIR")"

echo -e "${BLUE}Agent 目录: $AGENT_DIR${NC}"
echo -e "${BLUE}项目根目录: $PROJECT_ROOT${NC}"

# 检查 conda 是否安装
echo ""
echo -e "${BLUE}检查 Conda...${NC}"
if ! command -v conda &> /dev/null; then
    echo -e "${RED}❌ 未找到 Conda${NC}"
    echo ""
    echo "请先安装 Conda："
    echo "  https://docs.conda.io/en/latest/miniconda.html"
    exit 1
fi

conda_version=$(conda --version 2>&1)
echo -e "${GREEN}✓ Conda 已安装: $conda_version${NC}"

# 切换到 agent 目录
cd "$AGENT_DIR"

# 检查环境是否已存在
ENV_NAME="casco_rag"
if conda env list | grep -q "^${ENV_NAME} "; then
    echo ""
    echo -e "${YELLOW}⚠ 环境 '$ENV_NAME' 已存在${NC}"
    read -p "是否删除并重新创建？(y/n): " choice
    if [ "$choice" == "y" ] || [ "$choice" == "Y" ]; then
        echo -e "${BLUE}删除现有环境...${NC}"
        conda env remove -n $ENV_NAME -y
    else
        echo -e "${GREEN}使用现有环境${NC}"
    fi
fi

# 创建 conda 环境
echo ""
echo -e "${BLUE}步骤 1/5: 创建 Conda 环境...${NC}"
if ! conda env list | grep -q "^${ENV_NAME} "; then
    # 创建基础环境
    conda create -n $ENV_NAME python=3.10 -y
    echo -e "${GREEN}✓ Conda 环境创建完成${NC}"
else
    echo -e "${YELLOW}⚠ 环境已存在，跳过创建${NC}"
fi

# 激活环境
echo ""
echo -e "${BLUE}激活环境...${NC}"
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate $ENV_NAME
echo -e "${GREEN}✓ 环境已激活: $ENV_NAME${NC}"

# 安装 uv（在 conda 环境中）
echo ""
echo -e "${BLUE}步骤 2/6: 在 conda 环境中安装 uv...${NC}"
pip install uv
echo -e "${GREEN}✓ uv 安装完成${NC}"

# 安装基础依赖
echo ""
echo -e "${BLUE}步骤 3/6: 安装基础依赖...${NC}"
pip install python-dotenv openai tiktoken numpy
echo -e "${GREEN}✓ 基础依赖安装完成${NC}"

# 安装 LangChain
echo ""
echo -e "${BLUE}步骤 4/6: 安装 LangChain...${NC}"
pip install langchain langchain-openai langchain-core
echo -e "${GREEN}✓ LangChain 安装完成${NC}"

# 安装 RAG-Anything（使用 uv）
echo ""
echo -e "${BLUE}步骤 5/6: 安装 RAG-Anything（使用 uv）...${NC}"
cd "$PROJECT_ROOT/RAG-Anything"
# 先安装依赖
uv pip install -r requirements.txt
# 然后安装 RAG-Anything
uv pip install -e .
echo -e "${GREEN}✓ RAG-Anything 安装完成${NC}"
cd "$AGENT_DIR"

# 验证安装
echo ""
echo -e "${BLUE}步骤 6/6: 验证安装...${NC}"
python -c "import raganything; print('✓ raganything')" && \
python -c "import lightrag; print('✓ lightrag')" && \
python -c "import openai; print('✓ openai')" && \
python -c "import langchain; print('✓ langchain')" && \
echo -e "${GREEN}✓ 所有依赖验证通过${NC}"

# 完成
echo ""
echo -e "${GREEN}======================================"
echo "✅ Conda 环境安装完成！"
echo "======================================${NC}"
echo ""
echo -e "${BLUE}环境名称:${NC} $ENV_NAME"
echo -e "${BLUE}激活命令:${NC} conda activate $ENV_NAME"
echo -e "${BLUE}退出命令:${NC} conda deactivate"
echo ""
echo -e "${YELLOW}下一步：${NC}"
echo ""
echo "1. 激活环境:"
echo "   ${GREEN}conda activate $ENV_NAME${NC}"
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
echo "- 使用 'conda activate $ENV_NAME' 激活环境"
echo "- 使用 'conda deactivate' 退出环境"
echo "- 使用 'conda env list' 查看所有环境"
echo "- 使用 'conda env remove -n $ENV_NAME' 删除环境"
echo "======================================${NC}"
echo ""
echo -e "${YELLOW}快速开始：${NC}"
echo "conda activate $ENV_NAME"
echo "source env.sh"
echo "python quick_start.py"

