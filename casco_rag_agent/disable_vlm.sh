#!/bin/bash
# 禁用多模态处理，只使用文本

echo "=========================================="
echo "  禁用 VLM（多模态），只处理文本"
echo "=========================================="
echo ""

cd /home/honglianglu/ssd/casco/casco_rag_agent

echo "优势："
echo "  ✅ 继续使用现有的 Qwen API"
echo "  ✅ 避免触发内容审核"
echo "  ✅ 处理速度更快"
echo "  ✅ 成本更低"
echo ""

echo "影响："
echo "  ⚠️  文档中的图像、表格、公式不会被处理"
echo "  ⚠️  只提取文本内容"
echo "  ℹ️  对于技术文档，大部分关键信息在文本中"
echo ""

echo "已修改 rag_qa_agent.py:"
echo "  enable_image_processing=False"
echo "  enable_table_processing=False"
echo "  enable_equation_processing=False"
echo ""

echo "=========================================="
echo "  测试运行"
echo "=========================================="
echo ""

# 激活环境
export PATH="/data/4tssd/anaconda3/bin:$PATH"
eval "$(conda shell.bash hook)" 2>/dev/null || true
conda activate casco 2>/dev/null || true

# 加载配置
source env.sh

echo "当前配置："
echo "  LLM: $CLOUD_MODEL"
echo "  Embedding: $OPENAI_API_MODEL"
echo "  多模态: 已禁用"
echo ""

read -p "是否立即测试运行？(y/n): " confirm

if [ "$confirm" = "y" ] || [ "$confirm" = "Y" ]; then
    echo ""
    echo "启动 RAG 系统..."
    python rag_qa_agent.py
else
    echo ""
    echo "手动运行:"
    echo "  source env.sh"
    echo "  python rag_qa_agent.py"
fi

