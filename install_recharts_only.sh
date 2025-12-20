#!/bin/bash

echo "📦 安装 recharts 依赖"
echo "============================================================"
echo ""

# 进入前端目录
cd /home/honglianglu/hdd/rag-agent/frontend

echo "1️⃣  检查 npm..."
if ! command -v npm &> /dev/null; then
    echo "   ⚠️  npm 未找到，尝试使用 nvm..."
    
    # 尝试加载 nvm
    export NVM_DIR="$HOME/.nvm"
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
    
    if command -v npm &> /dev/null; then
        echo "   ✅ 成功加载 nvm 中的 npm"
    else
        echo "   ❌ 错误：npm 不可用"
        echo ""
        echo "请手动执行："
        echo "  cd /home/honglianglu/hdd/rag-agent/frontend"
        echo "  npm install recharts"
        exit 1
    fi
fi

NPM_PATH=$(which npm)
echo "   ✅ npm 路径: $NPM_PATH"
echo ""

echo "2️⃣  安装 recharts..."
npm install recharts

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ recharts 安装成功！"
    echo ""
    echo "3️⃣  验证安装..."
    npm list recharts
    echo ""
    echo "============================================================"
    echo "🎉 安装完成！"
    echo "============================================================"
    echo ""
    echo "📝 下一步："
    echo "1. 重启前端服务（./start_frontend.sh 或在终端按 Ctrl+C 然后重新运行）"
    echo "2. 刷新浏览器页面"
    echo "3. 测试雷达图功能"
    echo ""
else
    echo ""
    echo "❌ 安装失败"
    echo ""
    echo "请尝试："
    echo "  cd /home/honglianglu/hdd/rag-agent/frontend"
    echo "  npm install"
    echo ""
fi

