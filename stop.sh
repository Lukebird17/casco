#!/bin/bash

# 🛑 OmniScry 停止脚本

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "       🛑 停止 OmniScry 服务"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

echo "🛑 停止后端服务..."
pkill -f "uvicorn backend.api:app"
echo "✅ 后端已停止"

echo "🛑 停止前端服务..."
pkill -f "npm run dev"
echo "✅ 前端已停止"

sleep 1

echo ""
echo "✅ OmniScry 所有服务已停止"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

