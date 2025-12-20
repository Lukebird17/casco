#!/bin/bash
# RAG-Agent 一键安装脚本

set -e  # 遇到错误立即退出

echo "🚀 RAG-Agent 一键安装脚本"
echo "============================================================"
echo ""

# 颜色定义
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 进入项目目录
cd /home/honglianglu/hdd/rag-agent

echo "📍 当前目录: $(pwd)"
echo ""

# ========================================
# 第一步：检查Python版本
# ========================================
echo -e "${BLUE}[1/4] 检查Python环境${NC}"
echo "----------------------------------------"

if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python3 未安装${NC}"
    echo "请先安装 Python 3.10 或更高版本"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | awk '{print $2}')
echo -e "${GREEN}✅ Python 版本: $PYTHON_VERSION${NC}"

# 检查pip
if ! command -v pip3 &> /dev/null; then
    echo -e "${RED}❌ pip3 未安装${NC}"
    exit 1
fi
echo -e "${GREEN}✅ pip3 已安装${NC}"
echo ""

# ========================================
# 第二步：安装Python依赖
# ========================================
echo -e "${BLUE}[2/4] 安装Python依赖${NC}"
echo "----------------------------------------"

echo "正在安装核心依赖..."
pip3 install -q --upgrade pip

# 核心依赖
echo "  • 安装 FastAPI & Uvicorn..."
pip3 install -q fastapi uvicorn[standard] python-multipart

echo "  • 安装 OpenAI..."
pip3 install -q openai

echo "  • 安装 ChromaDB..."
pip3 install -q chromadb sentence-transformers

echo "  • 安装文档处理库..."
pip3 install -q pypdf2 pymupdf python-docx python-pptx markdown beautifulsoup4 pillow

echo "  • 安装中文NLP..."
pip3 install -q jieba rank-bm25

echo "  • 安装其他工具..."
pip3 install -q requests tiktoken numpy pandas tqdm

echo -e "${GREEN}✅ 核心依赖安装完成${NC}"
echo ""

# 可选依赖
echo "正在安装可选依赖（可能需要几分钟）..."
echo "  • 安装 DeepEval（质量评估）..."
pip3 install -q deepeval 2>/dev/null || echo -e "${YELLOW}⚠️  DeepEval 安装失败（可选）${NC}"

echo "  • 安装 LlamaIndex（知识图谱）..."
pip3 install -q llama-index llama-index-llms-openai llama-index-embeddings-openai llama-index-vector-stores-chroma 2>/dev/null || echo -e "${YELLOW}⚠️  LlamaIndex 安装失败（可选）${NC}"

echo "  • 安装网络可视化..."
pip3 install -q networkx 2>/dev/null || echo -e "${YELLOW}⚠️  NetworkX 安装失败（可选）${NC}"

echo "  • 安装性能优化..."
pip3 install -q uvloop 2>/dev/null || echo -e "${YELLOW}⚠️  uvloop 安装失败（可选）${NC}"

echo -e "${GREEN}✅ Python依赖安装完成${NC}"
echo ""

# ========================================
# 第三步：安装前端依赖
# ========================================
echo -e "${BLUE}[3/4] 安装前端依赖${NC}"
echo "----------------------------------------"

if ! command -v npm &> /dev/null; then
    echo -e "${YELLOW}⚠️  npm 未安装，跳过前端依赖安装${NC}"
    echo "请手动安装 Node.js 和 npm，然后运行："
    echo "  cd frontend && npm install"
else
    NPM_VERSION=$(npm --version)
    echo -e "${GREEN}✅ npm 版本: $NPM_VERSION${NC}"
    
    cd frontend
    echo "正在安装前端依赖（可能需要几分钟）..."
    npm install
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ 前端依赖安装完成${NC}"
    else
        echo -e "${YELLOW}⚠️  前端依赖安装失败${NC}"
    fi
    cd ..
fi
echo ""

# ========================================
# 第四步：验证安装
# ========================================
echo -e "${BLUE}[4/4] 验证安装${NC}"
echo "----------------------------------------"

# 验证Python模块
echo "验证Python模块..."
python3 << EOF
import sys
success = True

modules = {
    'fastapi': 'FastAPI',
    'uvicorn': 'Uvicorn',
    'openai': 'OpenAI',
    'chromadb': 'ChromaDB',
    'jieba': 'Jieba',
    'rank_bm25': 'BM25',
    'pymupdf': 'PyMuPDF',
}

for module, name in modules.items():
    try:
        __import__(module)
        print(f"  ✅ {name}")
    except ImportError:
        print(f"  ❌ {name}")
        success = False

# 可选模块
optional = {
    'deepeval': 'DeepEval',
    'llama_index': 'LlamaIndex',
    'networkx': 'NetworkX',
}

for module, name in optional.items():
    try:
        __import__(module)
        print(f"  ✅ {name} (可选)")
    except ImportError:
        print(f"  ⚠️  {name} (可选，未安装)")

if success:
    print("\n✅ 核心模块验证通过")
else:
    print("\n❌ 部分核心模块缺失")
    sys.exit(1)
EOF

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Python模块验证失败${NC}"
    exit 1
fi

echo ""
echo "验证前端依赖..."
if [ -d "frontend/node_modules" ]; then
    if [ -d "frontend/node_modules/recharts" ]; then
        echo -e "  ${GREEN}✅ recharts${NC}"
    else
        echo -e "  ${YELLOW}⚠️  recharts 未安装${NC}"
    fi
    
    if [ -d "frontend/node_modules/react" ]; then
        echo -e "  ${GREEN}✅ React${NC}"
    else
        echo -e "  ${YELLOW}⚠️  React 未安装${NC}"
    fi
else
    echo -e "  ${YELLOW}⚠️  前端依赖未安装${NC}"
fi

echo ""
echo "============================================================"
echo -e "${GREEN}🎉 安装完成！${NC}"
echo "============================================================"
echo ""

# ========================================
# 显示下一步操作
# ========================================
echo "📝 下一步操作："
echo ""
echo "1️⃣  配置API密钥（如果还没配置）："
echo "   编辑 config.py，设置你的 OPENAI_API_KEY"
echo ""
echo "2️⃣  启动系统："
echo "   # 终端1 - 启动后端"
echo "   ./start_backend.sh"
echo ""
echo "   # 终端2 - 启动前端"
echo "   ./start_frontend.sh"
echo ""
echo "3️⃣  访问系统："
echo "   前端: http://localhost:5173"
echo "   后端: http://localhost:8000"
echo "   API文档: http://localhost:8000/docs"
echo ""
echo "============================================================"
echo ""

# 检查是否需要提示配置
if grep -q "your-api-key-here" config.py 2>/dev/null; then
    echo -e "${YELLOW}⚠️  提醒：请先配置 API 密钥再启动系统${NC}"
    echo ""
fi

echo "✨ 完成！祝使用愉快！"
echo ""

