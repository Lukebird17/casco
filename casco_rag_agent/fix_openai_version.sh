#!/bin/bash
# 修复 openai 库版本兼容性问题

set -e

echo "=========================================="
echo "修复 openai 库版本兼容性"
echo "=========================================="
echo ""

cd /home/honglianglu/ssd/casco/casco_rag_agent

# 检查当前版本
echo "1. 检查当前 openai 版本..."
current_version=$(python -c "import openai; print(openai.__version__)" 2>/dev/null || echo "未安装")
echo "   当前版本: $current_version"

# 检查 conda 环境
if [ -n "$CONDA_DEFAULT_ENV" ]; then
    echo "   Conda 环境: $CONDA_DEFAULT_ENV"
else
    echo "   ⚠️  未在 conda 环境中"
    echo "   请先激活: conda activate casco_rag"
    exit 1
fi

echo ""
echo "2. 修复方案："
echo "   错误: APIStatusError.__init__() missing 2 required keyword-only arguments"
echo "   原因: openai 库版本不兼容"
echo ""

read -p "是否降级 openai 到兼容版本 1.12.0？(y/n): " confirm

if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
    echo "已取消"
    exit 0
fi

echo ""
echo "3. 降级 openai 库..."
pip install "openai==1.12.0" --force-reinstall

echo ""
echo "4. 验证安装..."
new_version=$(python -c "import openai; print(openai.__version__)")
echo "   新版本: $new_version"

echo ""
echo "=========================================="
echo "✅ 修复完成！"
echo "=========================================="
echo ""
echo "现在可以重新运行:"
echo "  python rag_qa_agent.py"
echo ""

