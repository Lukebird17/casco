#!/bin/bash
# 最终修复方案：完全重装依赖

set -e

echo "=========================================="
echo "最终修复方案"
echo "=========================================="
echo ""

# 激活环境
source ~/.bashrc
conda activate casco

cd /home/honglianglu/ssd/casco/casco_rag_agent

echo "1. 当前版本:"
python -c "import openai, httpx; print(f'  openai: {openai.__version__}'); print(f'  httpx: {httpx.__version__}')"

echo ""
echo "2. 卸载并重装 RAG-Anything..."
pip uninstall -y raganything lightrag 2>/dev/null || true

echo ""
echo "3. 安装兼容的依赖组合..."
# 使用 openai 1.50.2 + httpx 0.27.2
pip install "openai==1.50.2" "httpx==0.27.2" -q

echo ""
echo "4. 重新安装 RAG-Anything..."
cd /home/honglianglu/ssd/casco
if [ -d "RAG-Anything" ]; then
    cd RAG-Anything
    git pull
    pip install -e . -q
    echo "  ✓ 从本地源重装完成"
else
    echo "  ⚠️  未找到 RAG-Anything 源码"
    echo "  尝试从 PyPI 安装..."
    pip install raganything -q
fi

echo ""
echo "5. 验证安装..."
cd /home/honglianglu/ssd/casco/casco_rag_agent
python -c "
import openai
import httpx
from raganything import RAGAnything
from lightrag import LightRAG
print(f'  ✓ openai: {openai.__version__}')
print(f'  ✓ httpx: {httpx.__version__}')
print(f'  ✓ raganything: OK')
print(f'  ✓ lightrag: OK')
"

echo ""
echo "=========================================="
echo "✅ 修复完成！"
echo "=========================================="
echo ""
echo "现在运行:"
echo "  source env.sh"
echo "  python rag_qa_agent.py"
echo ""

