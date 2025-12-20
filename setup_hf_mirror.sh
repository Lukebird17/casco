#!/bin/bash
# 配置HuggingFace镜像源

echo "🔧 配置 HuggingFace 镜像源"
echo "============================================================"
echo ""

# 检查当前配置
if [ -f ~/.bashrc ]; then
    if grep -q "HF_ENDPOINT" ~/.bashrc; then
        echo "✅ 镜像源已配置"
        grep "HF_ENDPOINT" ~/.bashrc
    else
        echo "📝 正在配置镜像源..."
        echo "" >> ~/.bashrc
        echo "# HuggingFace 镜像源配置" >> ~/.bashrc
        echo "export HF_ENDPOINT=https://hf-mirror.com" >> ~/.bashrc
        echo "✅ 已添加到 ~/.bashrc"
    fi
fi

echo ""
echo "🌐 可用的镜像源："
echo "   1. https://hf-mirror.com (默认，国内镜像)"
echo "   2. https://huggingface.co (官方，需要良好的国际网络)"
echo "   3. https://hub.tensorflow.google.cn (Google镜像)"
echo ""
echo "💡 立即生效（当前终端）："
echo "   export HF_ENDPOINT=https://hf-mirror.com"
echo ""
echo "🔄 或重新加载配置："
echo "   source ~/.bashrc"
echo ""
echo "============================================================"

