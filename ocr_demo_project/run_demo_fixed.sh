#!/bin/bash
# 修复 HuggingFace 下载问题并运行 demo

echo "=========================================="
echo "  启动增强版 Demo（已修复下载问题）"
echo "=========================================="
echo ""

# 1. 清除所有可能干扰的环境变量
unset HF_ENDPOINT
unset http_proxy
unset https_proxy
unset HTTP_PROXY
unset HTTPS_PROXY
unset all_proxy
unset ALL_PROXY

# 2. 设置 HuggingFace 缓存
export HF_HOME="${HOME}/.cache/huggingface"
export HF_HUB_DISABLE_SYMLINKS_WARNING=1
mkdir -p "$HF_HOME"

# 3. 显示当前配置
echo "✅ 环境已配置:"
echo "   - 已清除所有代理设置"
echo "   - 已清除 HF_ENDPOINT（使用官方源）"
echo "   - 缓存目录: $HF_HOME"
echo ""

# 4. 运行程序
echo "🚀 启动程序..."
echo "=========================================="
echo ""

python demo_enhanced.py

echo ""
echo "=========================================="
echo "程序已结束"
echo "=========================================="

