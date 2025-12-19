#!/bin/bash
# 安装LaTeX公式渲染依赖

echo "📦 安装LaTeX公式渲染依赖..."
echo ""

cd "$(dirname "$0")"

# 检查是否有npm
if command -v npm &> /dev/null; then
    echo "✅ 找到npm，开始安装..."
    npm install remark-math rehype-katex katex
    echo ""
    echo "✅ 安装完成！"
elif command -v yarn &> /dev/null; then
    echo "✅ 找到yarn，开始安装..."
    yarn add remark-math rehype-katex katex
    echo ""
    echo "✅ 安装完成！"
elif command -v pnpm &> /dev/null; then
    echo "✅ 找到pnpm，开始安装..."
    pnpm add remark-math rehype-katex katex
    echo ""
    echo "✅ 安装完成！"
else
    echo "❌ 错误：未找到npm、yarn或pnpm"
    echo ""
    echo "请手动安装依赖："
    echo "  cd frontend"
    echo "  npm install remark-math rehype-katex katex"
    echo ""
    echo "或者使用conda环境中的node："
    echo "  conda activate rag"
    echo "  cd frontend"
    echo "  npm install remark-math rehype-katex katex"
    exit 1
fi




