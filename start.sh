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
pkill -f "vite" 2>/dev/null
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

# 检查 npm 并尝试多个查找方法
NPM_PATH=""
if command -v npm &> /dev/null; then
    NPM_PATH=$(command -v npm)
elif [ -f "$HOME/.nvm/nvm.sh" ]; then
    # 尝试加载 nvm
    source "$HOME/.nvm/nvm.sh"
    if command -v npm &> /dev/null; then
        NPM_PATH=$(command -v npm)
    fi
elif [ -d "$HOME/.nvm/versions/node" ]; then
    # 尝试查找 nvm 安装的最新版本
    LATEST_NODE=$(ls -1 "$HOME/.nvm/versions/node" | sort -V | tail -1)
    if [ -n "$LATEST_NODE" ] && [ -f "$HOME/.nvm/versions/node/$LATEST_NODE/bin/npm" ]; then
        NPM_PATH="$HOME/.nvm/versions/node/$LATEST_NODE/bin/npm"
        export PATH="$HOME/.nvm/versions/node/$LATEST_NODE/bin:$PATH"
    fi
fi

if [ -z "$NPM_PATH" ]; then
    echo "❌ 错误: 未找到npm"
    echo "💡 提示:"
    echo "   1. 请确保已安装 Node.js"
    echo "   2. 如果使用 nvm，请先运行: source ~/.nvm/nvm.sh"
    echo "   3. 或手动指定 npm 路径: export PATH=\$PATH:/path/to/node/bin"
    exit 1
fi

echo "✅ Python: $(python --version 2>&1 | awk '{print $2}')"
echo "✅ Node: $(node --version 2>&1)"
echo "✅ npm: v$(npm --version 2>&1)"
echo "✅ npm路径: $NPM_PATH"
echo ""

# 启动后端
echo "🚀 启动后端服务..."
cd "$(dirname "$0")"
nohup uvicorn backend.api:app --host 0.0.0.0 --port 8000 --reload > backend.log 2>&1 &
BACKEND_PID=$!
echo "✅ 后端PID: $BACKEND_PID"
echo "📝 后端日志: backend.log"

# 检查后端
echo "🔍 检查后端状态（等待启动，最多30秒）..."
for i in {1..30}; do
    sleep 1
    if curl -s http://localhost:8000/docs > /dev/null 2>&1; then
        echo "✅ 后端服务正常运行（用时 ${i} 秒）"
        break
    fi
    # 每5秒显示一次进度
    if [ $((i % 5)) -eq 0 ]; then
        echo "   ⏳ 等待中... (${i}/30秒)"
    fi
    if [ $i -eq 30 ]; then
        echo "❌ 后端启动超时，但进程可能仍在启动中"
        echo "💡 请检查:"
        echo "   1. 查看日志: tail -f backend.log"
        echo "   2. 访问 API 文档: http://localhost:8000/docs"
        echo "   3. 如果能访问，说明启动成功，只是时间较长"
        exit 1
    fi
done
echo ""

# 启动前端
echo "🎨 启动前端服务..."

FRONTEND_STARTED=false

# 方案1: 使用 screen（最佳）
if command -v screen &> /dev/null; then
    echo "💡 使用 screen 启动前端..."
    cd frontend
    screen -dmS omniscry-frontend bash -c "source ~/.bashrc 2>/dev/null; npm run dev"
    cd ..
    sleep 2
    
    # 检查是否启动成功
    if screen -list | grep -q omniscry-frontend; then
        echo "✅ 前端已在 screen 会话中启动"
        echo "   查看: screen -r omniscry-frontend"
        echo "   分离: Ctrl+A 然后按 D"
        FRONTEND_STARTED=true
    else
        echo "⚠️  screen 启动失败，尝试其他方法..."
    fi
fi

# 方案2: 使用完整路径的 npm 和 nohup
if [ "$FRONTEND_STARTED" = false ]; then
    echo "💡 使用 nohup 启动前端..."
    cd frontend
    
    # 使用绝对路径和环境变量
    if [ -n "$NPM_PATH" ]; then
        nohup bash -c "export PATH='$(dirname $NPM_PATH):\$PATH'; npm run dev" > ../frontend.log 2>&1 &
        FRONTEND_PID=$!
        cd ..
        sleep 3
        
        # 检查进程是否存在
        if ps -p $FRONTEND_PID > /dev/null 2>&1; then
            echo "✅ 前端PID: $FRONTEND_PID"
            echo "📝 前端日志: frontend.log"
            FRONTEND_STARTED=true
        else
            echo "⚠️  nohup 启动失败"
            cat frontend.log
        fi
    fi
fi

# 方案3: 提示手动启动
if [ "$FRONTEND_STARTED" = false ]; then
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "⚠️  自动启动前端失败"
    echo ""
    echo "📝 请在新终端窗口手动启动前端:"
    echo ""
    echo "   cd $(pwd)/frontend"
    echo "   npm run dev"
    echo ""
    echo "或者使用提供的启动脚本:"
    echo "   cd $(pwd)/frontend"
    echo "   bash ../start_frontend.sh"
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
fi

sleep 2
echo ""

# 显示访问信息
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
if [ "$FRONTEND_STARTED" = true ]; then
    echo "       ✨ OmniScry 启动完成 ✨"
else
    echo "       ✨ OmniScry 后端启动完成 ✨"
fi
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🌐 访问地址:"
if [ "$FRONTEND_STARTED" = true ]; then
    echo "   前端: http://localhost:5173  ✅"
else
    echo "   前端: http://localhost:5173  (需手动启动)"
fi
echo "   后端: http://localhost:8000  ✅"
echo "   API文档: http://localhost:8000/docs  ✅"
echo ""
echo "📊 进程信息:"
echo "   后端PID: $BACKEND_PID"
if [ "$FRONTEND_STARTED" = true ] && [ -n "$FRONTEND_PID" ]; then
    echo "   前端PID: $FRONTEND_PID"
fi
echo ""
echo "📝 日志文件:"
echo "   后端: tail -f backend.log"
if [ "$FRONTEND_STARTED" = true ]; then
    if command -v screen &> /dev/null && screen -list | grep -q omniscry-frontend; then
        echo "   前端: screen -r omniscry-frontend"
    else
        echo "   前端: tail -f frontend.log"
    fi
fi
echo ""
echo "🛑 停止服务:"
echo "   ./stop.sh"
echo "   或后端: pkill -f uvicorn"
if [ "$FRONTEND_STARTED" = true ]; then
    if command -v screen &> /dev/null; then
        echo "   或前端: screen -X -S omniscry-frontend quit"
    else
        echo "   或前端: pkill -f 'npm run dev'"
    fi
fi
echo ""
if [ "$FRONTEND_STARTED" = false ]; then
    echo "💡 提示:"
    echo "   前端需要在新终端窗口手动启动"
    echo "   建议安装 screen 以支持后台启动: sudo apt install screen"
    echo ""
fi
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Navigate the Depths of Knowledge 🌌"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
