#!/bin/bash

echo "🎨 质量评估雷达图 - 快速安装脚本"
echo "============================================================"
echo ""

# 步骤1：安装前端依赖
echo "📦 步骤1：安装前端依赖 (recharts)"
cd /home/honglianglu/hdd/rag-agent/frontend

if [ ! -d "node_modules" ]; then
    echo "   ⚠️  node_modules 不存在，需要先运行 npm install"
    echo "   正在安装所有依赖..."
    npm install
fi

echo "   正在安装 recharts..."
npm install recharts

if [ $? -eq 0 ]; then
    echo "   ✅ recharts 安装成功"
else
    echo "   ❌ recharts 安装失败"
    exit 1
fi

echo ""
echo "✅ 前端依赖安装完成"
echo ""

# 步骤2：检查后端文件
echo "📝 步骤2：检查后端文件"
cd /home/honglianglu/hdd/rag-agent

if [ -f "quality_evaluator.py" ]; then
    echo "   ✅ quality_evaluator.py 存在"
else
    echo "   ❌ quality_evaluator.py 不存在"
    exit 1
fi

echo ""

# 步骤3：检查前端文件
echo "📝 步骤3：检查前端文件"
cd /home/honglianglu/hdd/rag-agent/frontend/src/components

if [ -f "QualityMetrics.jsx" ]; then
    echo "   ✅ QualityMetrics.jsx 存在"
else
    echo "   ❌ QualityMetrics.jsx 不存在"
    exit 1
fi

echo ""

# 步骤4：重启服务
echo "🔄 步骤4：重启服务"
cd /home/honglianglu/hdd/rag-agent

if [ -f "restart_all.sh" ]; then
    echo "   正在重启服务..."
    ./restart_all.sh
    echo "   ✅ 服务重启完成"
else
    echo "   ⚠️  restart_all.sh 不存在，请手动重启服务"
fi

echo ""
echo "============================================================"
echo "🎉 安装完成！"
echo "============================================================"
echo ""
echo "📝 测试步骤："
echo "1. 打开浏览器 http://localhost:5173"
echo "2. 上传文档并提问"
echo "3. 等待回答完成"
echo "4. 点击右侧「详细信息」按钮"
echo "5. 应该看到雷达图和质量评估"
echo ""
echo "📊 预期效果："
echo "   ⭐⭐⭐⭐⭐ 置信度: 85%"
echo "   [显示雷达图，包含5个维度]"
echo "   准确性、相关性、完整性、忠实度、清晰度"
echo ""
echo "⚠️  注意事项："
echo "   - 质量评估需要约2秒额外时间"
echo "   - 只有在使用知识库问答时才会显示"
echo "   - 如果评估失败，会显示默认值"
echo ""
echo "📚 详细文档: QUALITY_METRICS_IMPLEMENTATION.md"
echo ""

