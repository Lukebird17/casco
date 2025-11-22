#!/bin/bash
# 修复维度不匹配错误的脚本

set -e

AGENT_DIR="/home/honglianglu/ssd/casco/casco_rag_agent"
cd "$AGENT_DIR"

echo "=========================================="
echo "修复 Embedding 维度不匹配错误"
echo "=========================================="
echo ""

# 检查当前配置
echo "1. 检查当前配置..."
source env.sh

echo "   Embedding Model: $OPENAI_API_MODEL"
echo "   Expected Dimension:"
case "$OPENAI_API_MODEL" in
    *"3-large"*)
        echo "     - text-embedding-3-large: 3072维"
        ;;
    *"3-small"*)
        echo "     - text-embedding-3-small: 1536维"
        ;;
    *"ada-002"*)
        echo "     - text-embedding-ada-002: 1536维"
        ;;
    *"bge-m3"*)
        echo "     - bge-m3: 1024维"
        ;;
    *)
        echo "     - 未知模型，可能是 1024 或 1536 维"
        ;;
esac
echo ""

# 询问是否继续
echo "2. 解决方案："
echo "   需要删除旧的向量数据库并重新创建"
echo ""
read -p "是否继续？这将删除 rag_storage 目录 (y/n): " confirm

if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
    echo "已取消"
    exit 0
fi

# 备份旧数据
if [ -d "rag_storage" ]; then
    backup_name="rag_storage_backup_$(date +%Y%m%d_%H%M%S)"
    echo ""
    echo "3. 备份旧数据..."
    mv rag_storage "$backup_name"
    echo "   ✓ 备份到: $backup_name"
fi

# 创建新目录
echo ""
echo "4. 创建新的存储目录..."
mkdir -p rag_storage
echo "   ✓ 已创建: rag_storage/"

# 显示摘要
echo ""
echo "=========================================="
echo "✅ 修复完成！"
echo "=========================================="
echo ""
echo "现在可以重新运行:"
echo "  python rag_qa_agent.py"
echo ""
echo "或测试 API 配置:"
echo "  python test_api.py"
echo ""

