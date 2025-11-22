#!/bin/bash
# 最终修复方案

set -e

echo "=========================================="
echo "最终修复"
echo "=========================================="

# 1. 激活环境
export PATH="/data/4tssd/anaconda3/bin:$PATH"
eval "$(conda shell.bash hook)"
conda activate casco

cd /home/honglianglu/ssd/casco/casco_rag_agent

echo ""
echo "1. 降级 openai 到更容错的版本..."
# openai 1.10.0 对非标准响应更宽容
pip install "openai==1.10.0" -q --force-reinstall

echo ""
echo "2. 确保 httpx 兼容..."
pip install "httpx==0.26.0" -q --force-reinstall

echo ""
echo "3. 验证版本..."
python -c "
import openai
import httpx
print(f'✅ openai: {openai.__version__}')
print(f'✅ httpx: {httpx.__version__}')
"

echo ""
echo "4. 清空旧数据（避免维度错误）..."
if [ -d "rag_storage" ]; then
    backup="rag_storage_backup_$(date +%Y%m%d_%H%M%S)"
    mv rag_storage "$backup"
    echo "   备份到: $backup"
fi
mkdir -p rag_storage

echo ""
echo "=========================================="
echo "✅ 修复完成！"
echo "=========================================="
echo ""
echo "现在运行:"
echo "  source env.sh"
echo "  python rag_qa_agent.py"
echo ""

