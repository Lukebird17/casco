#!/bin/bash
# 重启前端服务脚本

echo "🔄 重启前端服务..."

# 停止旧的前端进程
pkill -f "vite" 2>/dev/null
pkill -f "npm run dev" 2>/dev/null
sleep 2

# 激活conda环境并启动前端
cd /home/honglianglu/hdd/rag-agent/frontend

# 使用conda环境
source ~/.bashrc
conda activate rag

echo "✅ 启动前端服务（监听 0.0.0.0:5173）..."
npm run dev

echo "✅ 前端服务已启动"
echo "📱 访问地址: http://<服务器IP>:5173"



