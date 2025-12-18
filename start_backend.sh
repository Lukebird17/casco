#!/bin/bash
# 启动后端

echo "=========================================="
echo "🚀 启动 FastAPI 后端"
echo "=========================================="

# 激活 conda 环境
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate rag

# 启动后端
cd /home/honglianglu/hdd/rag-agent/backend

echo "📡 后端地址: http://localhost:8000"
echo "📖 API 文档: http://localhost:8000/docs"
echo ""

# 使用 uvicorn 启动，并允许从任何IP访问
uvicorn api:app --host 0.0.0.0 --port 8000 --reload

