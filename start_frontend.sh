#!/bin/bash
# 启动前端

cd /home/honglianglu/hdd/rag-agent/frontend

echo "=========================================="
echo "🚀 启动 React 前端"
echo "=========================================="

# 检查是否已安装依赖
if [ ! -d "node_modules" ]; then
    echo "📦 首次运行，安装依赖..."
    npm install
fi

echo ""
echo "🌐 前端地址: http://localhost:5173"
echo ""

npm run dev


