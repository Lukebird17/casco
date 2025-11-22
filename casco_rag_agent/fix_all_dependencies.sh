#!/bin/bash
# 一次性修复所有依赖版本问题

set -e

echo "=========================================="
echo "修复所有依赖版本兼容性"
echo "=========================================="
echo ""

cd /home/honglianglu/ssd/casco/casco_rag_agent

# 检查 conda 环境
if [ -n "$CONDA_DEFAULT_ENV" ]; then
    echo "✓ Conda 环境: $CONDA_DEFAULT_ENV"
else
    echo "❌ 未在 conda 环境中"
    echo "   请先激活: conda activate casco_rag"
    exit 1
fi

echo ""
echo "当前版本:"
python -c "import openai; print(f'  openai: {openai.__version__}')" 2>/dev/null || echo "  openai: 未安装"
python -c "import httpx; print(f'  httpx: {httpx.__version__}')" 2>/dev/null || echo "  httpx: 未安装"
python -c "import lightrag; print(f'  lightrag: {lightrag.__version__}')" 2>/dev/null || echo "  lightrag: 未知版本"

echo ""
echo "问题："
echo "  1. openai 1.109.1 太新 → APIStatusError 参数错误"
echo "  2. httpx 版本不匹配 → AsyncClient 不接受 'proxies' 参数"
echo ""
echo "解决方案："
echo "  使用兼容的版本组合"
echo ""

read -p "是否继续修复？(y/n): " confirm

if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
    echo "已取消"
    exit 0
fi

echo ""
echo "正在安装兼容版本..."
echo ""

# 方案：使用 openai 1.40.0 + 匹配的 httpx
pip install "openai>=1.40.0,<1.50.0" "httpx>=0.27.0,<0.28.0" --force-reinstall

echo ""
echo "验证安装..."
new_openai=$(python -c "import openai; print(openai.__version__)")
new_httpx=$(python -c "import httpx; print(httpx.__version__)")

echo "  ✓ openai: $new_openai"
echo "  ✓ httpx: $new_httpx"

echo ""
echo "=========================================="
echo "✅ 修复完成！"
echo "=========================================="
echo ""
echo "现在可以重新运行:"
echo "  python rag_qa_agent.py"
echo ""

