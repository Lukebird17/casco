#!/bin/bash

# 🚀 OmniScry 一键启动脚本
# Navigate the Depths of Knowledge

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "       ✨ OmniScry - 系统启动 ✨"
echo "    Navigate the Depths of Knowledge"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# 检查是否在正确的目录
if [ ! -d "backend" ] || [ ! -d "frontend" ]; then
    echo "❌ 错误: 请在 rag-agent 根目录运行此脚本"
    exit 1
fi

# 停止旧进程
echo "🛑 停止旧进程..."
pkill -f "uvicorn backend.api:app" 2>/dev/null
pkill -f "npm run dev" 2>/dev/null
sleep 2
echo "✅ 旧进程已停止"
echo ""

# 清理缓存
echo "🧹 清理缓存..."
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
find . -type f -name "*.pyc" -delete 2>/dev/null
cd frontend && rm -rf .vite 2>/dev/null && cd ..
echo "✅ 缓存已清理"
echo ""

# 检查环境
echo "🔍 检查环境..."
if ! command -v python &> /dev/null; then
    echo "❌ 错误: 未找到Python"
    exit 1
fi
if ! command -v npm &> /dev/null; then
    echo "❌ 错误: 未找到npm"
    exit 1
fi
echo "✅ Python: $(python --version 2>&1 | awk '{print $2}')"
echo "✅ Node: $(node --version 2>&1)"
echo "✅ npm: v$(npm --version 2>&1)"
echo ""

# 启动后端
echo "🚀 启动后端服务..."
cd "$(dirname "$0")"
nohup uvicorn backend.api:app --host 0.0.0.0 --port 8000 --reload > backend.log 2>&1 &
BACKEND_PID=$!
echo "✅ 后端PID: $BACKEND_PID"
echo "📝 后端日志: backend.log"
sleep 3

# 检查后端
echo "🔍 检查后端状态..."
for i in {1..10}; do
    if curl -s http://localhost:8000/api/health > /dev/null 2>&1; then
        echo "✅ 后端服务正常运行"
        break
    fi
    if [ $i -eq 10 ]; then
        echo "❌ 后端启动失败，请查看 backend.log"
        exit 1
    fi
    sleep 1
done
echo ""

# 启动前端
echo "🎨 启动前端服务..."
cd frontend
nohup npm run dev > ../frontend.log 2>&1 &
FRONTEND_PID=$!
cd ..
echo "✅ 前端PID: $FRONTEND_PID"
echo "📝 前端日志: frontend.log"
sleep 5
echo ""

# 显示访问信息
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "       ✨ OmniScry 启动完成 ✨"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🌐 访问地址:"
echo "   前端: http://localhost:5173"
echo "   后端: http://localhost:8000"
echo "   API文档: http://localhost:8000/docs"
echo ""
echo "📊 进程信息:"
echo "   后端PID: $BACKEND_PID"
echo "   前端PID: $FRONTEND_PID"
echo ""
echo "📝 日志文件:"
echo "   后端: tail -f backend.log"
echo "   前端: tail -f frontend.log"
echo ""
echo "🛑 停止服务:"
echo "   ./stop.sh"
echo "   或: pkill -f uvicorn && pkill -f 'npm run dev'"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Navigate the Depths of Knowledge 🌌"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

