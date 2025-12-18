#!/bin/bash

# RAG Agent 停止开发环境脚本

echo "=========================================="
echo "🛑 停止 RAG Agent 开发环境"
echo "=========================================="

# 停止后端
echo ""
echo "1️⃣  停止 FastAPI 后端..."
pkill -f "python.*api.py"

# 停止前端
echo "2️⃣  停止 React 前端..."
pkill -f "vite"

echo ""
echo "✅ 开发环境已停止"
echo "=========================================="


