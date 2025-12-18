#!/bin/bash

# RAG Agent 开发环境启动脚本

echo "=========================================="
echo "🚀 启动 RAG Agent 开发环境"
echo "=========================================="

# 检查并激活 conda 环境
if [ "$CONDA_DEFAULT_ENV" != "rag" ]; then
    echo "⚠️  当前环境不是 rag，正在切换..."
    source "$(conda info --base)/etc/profile.d/conda.sh"
    conda activate rag
fi

echo "✅ Conda 环境: $CONDA_DEFAULT_ENV"

# 启动后端
echo ""
echo "1️⃣  启动 FastAPI 后端..."
cd backend
python api.py &
BACKEND_PID=$!
echo "   后端 PID: $BACKEND_PID"
echo "   后端地址: http://localhost:8000"
cd ..

# 等待后端启动
echo ""
echo "⏳ 等待后端启动..."
sleep 3

# 启动前端
echo ""
echo "2️⃣  启动 React 前端..."
cd frontend

# 检查是否已安装依赖
if [ ! -d "node_modules" ]; then
    echo "   📦 首次运行，安装依赖..."
    npm install
fi

npm run dev &
FRONTEND_PID=$!
echo "   前端 PID: $FRONTEND_PID"
echo "   前端地址: http://localhost:5173"
cd ..

echo ""
echo "=========================================="
echo "✅ 开发环境启动成功！"
echo "=========================================="
echo ""
echo "📌 访问地址："
echo "   前端: http://localhost:5173"
echo "   后端: http://localhost:8000"
echo "   API 文档: http://localhost:8000/docs"
echo ""
echo "🛑 停止服务: Ctrl+C 或运行 ./stop_dev.sh"
echo ""

# 等待用户中断
wait

