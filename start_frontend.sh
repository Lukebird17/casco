#!/bin/bash

# 🎨 OmniScry 前端启动脚本
# 单独启动前端服务

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "       🎨 OmniScry - 前端启动"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# 检查是否在 frontend 目录
if [ ! -f "package.json" ]; then
    echo "❌ 错误: 请在 frontend 目录运行此脚本"
    echo "💡 正确用法: cd frontend && bash ../start_frontend.sh"
    exit 1
fi

# 检查 npm
if ! command -v npm &> /dev/null; then
    echo "❌ 错误: 未找到 npm"
    echo "💡 请确保已安装 Node.js 并配置环境变量"
    exit 1
fi

echo "✅ Node: $(node --version)"
echo "✅ npm: v$(npm --version)"
echo ""

# 检查依赖
if [ ! -d "node_modules" ]; then
    echo "📦 检测到未安装依赖，正在安装..."
    npm install
    echo ""
fi

# 启动开发服务器
echo "🚀 启动 Vite 开发服务器..."
echo ""
npm run dev
