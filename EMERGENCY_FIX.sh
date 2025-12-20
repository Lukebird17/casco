#!/bin/bash

# 紧急修复脚本 - 清理所有可能的缓存

echo "🔧 开始紧急修复..."

# 1. 停止所有相关进程
echo "1️⃣ 停止现有进程..."
pkill -f "python.*api.py" || true
pkill -f "npm.*start" || true
sleep 2

# 2. 清理session数据
echo "2️⃣ 清理session数据..."
rm -rf /home/honglianglu/hdd/rag-agent/sessions/*.json
rm -rf /home/honglianglu/hdd/rag-agent/sessions/*
echo "   ✅ Sessions清理完成"

# 3. 清理前端缓存
echo "3️⃣ 清理前端缓存..."
cd /home/honglianglu/hdd/rag-agent/frontend
rm -rf .vite
rm -rf node_modules/.vite
rm -rf dist
echo "   ✅ 前端缓存清理完成"

# 4. 清理浏览器localStorage（提示用户手动操作）
echo ""
echo "⚠️  重要：请手动清理浏览器缓存"
echo "   1. 打开浏览器 DevTools (F12)"
echo "   2. 打开 Application 标签"
echo "   3. 左侧找到 Local Storage"
echo "   4. 点击 http://localhost:3000"
echo "   5. 点击右侧的 Clear All 按钮"
echo "   6. 刷新页面 (Ctrl+Shift+R)"
echo ""

# 5. 确认代码修复
echo "4️⃣ 检查代码修复..."
grep -n "session.add_message" /home/honglianglu/hdd/rag-agent/backend/api.py | grep "第7步" -A1 | tail -2
echo ""

echo "✅ 紧急修复完成！"
echo ""
echo "📋 下一步操作："
echo "   1. 重启后端: python backend/api.py"
echo "   2. 重启前端: cd frontend && npm start"
echo "   3. 打开浏览器: http://localhost:3000"
echo "   4. 点击'新对话'按钮"
echo "   5. 测试提问"




