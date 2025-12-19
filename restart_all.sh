#!/bin/bash

echo "🔄 重启RAG系统..."
echo ""

# 获取脚本所在目录
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# 找到并杀死旧的后端进程
echo "1️⃣  停止旧的后端进程..."
pkill -f "python.*backend/api.py" || echo "   没有发现运行中的后端进程"
sleep 2

# 找到并杀死旧的前端进程
echo "2️⃣  停止旧的前端进程..."
pkill -f "vite.*5173" || echo "   没有发现运行中的前端进程"
cd frontend && pkill -f "npm.*start" || true
cd ..
sleep 2

echo ""
echo "✅ 旧进程已停止"
echo ""
echo "3️⃣  启动后端..."
echo "   后端将在 http://localhost:8000 运行"
echo ""

# 在后台启动后端
nohup python backend/api.py > backend.log 2>&1 &
BACKEND_PID=$!
echo "   后端PID: $BACKEND_PID"
echo "   日志: $SCRIPT_DIR/backend.log"

sleep 3

# 检查后端是否启动成功
if ps -p $BACKEND_PID > /dev/null; then
    echo "   ✅ 后端启动成功"
else
    echo "   ❌ 后端启动失败，请查看 backend.log"
    exit 1
fi

echo ""
echo "4️⃣  启动前端..."
echo "   前端将在 http://localhost:5173 运行"
echo ""

cd frontend
nohup npm start > ../frontend.log 2>&1 &
FRONTEND_PID=$!
echo "   前端PID: $FRONTEND_PID"
echo "   日志: $SCRIPT_DIR/frontend.log"

cd ..

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🎉 RAG系统启动完成！"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📊 访问地址:"
echo "   🌐 前端: http://localhost:5173"
echo "   🔧 后端: http://localhost:8000"
echo ""
echo "📝 日志文件:"
echo "   后端: tail -f $SCRIPT_DIR/backend.log"
echo "   前端: tail -f $SCRIPT_DIR/frontend.log"
echo ""
echo "🛑 停止服务:"
echo "   kill $BACKEND_PID $FRONTEND_PID"
echo ""
echo "💡 提示: 等待10-15秒让前端完全启动"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

