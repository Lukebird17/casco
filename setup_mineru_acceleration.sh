#!/bin/bash
# MinerU加速配置脚本

echo "=== MinerU加速配置 ==="
echo ""

# 1. 配置HuggingFace镜像（解决下载慢的问题）
echo "📦 步骤1: 配置HuggingFace镜像源..."
export HF_ENDPOINT=https://hf-mirror.com
echo "export HF_ENDPOINT=https://hf-mirror.com" >> ~/.zshrc
echo "✅ HuggingFace镜像已配置（使用国内镜像）"
echo ""

# 2. 设置模型缓存目录
echo "📦 步骤2: 配置模型缓存目录..."
export HF_HOME=~/.cache/huggingface
mkdir -p $HF_HOME
echo "✅ 模型缓存目录: $HF_HOME"
echo ""

# 3. 创建MinerU配置文件
echo "📦 步骤3: 创建MinerU配置文件..."
cat > ~/.magic-pdf.json << 'EOF'
{
    "bucket-name-magic-pdf": "",
    "credentials-path": "",
    "temp-output-dir": "",
    "device-mode": "auto",
    "models-dir": "",
    "layoutreader-model-dir": "",
    "table-config": {
        "is_table_recog_enable": true,
        "max_time": 400
    },
    "formula-config": {
        "mfd_enable": true,
        "mfr_enable": true
    }
}
EOF
echo "✅ 配置文件已创建: ~/.magic-pdf.json"
echo ""

# 4. 检测GPU并配置
echo "📦 步骤4: 检测GPU..."
if command -v nvidia-smi &> /dev/null; then
    echo "✅ 检测到NVIDIA GPU，将启用CUDA加速"
    # 更新配置为cuda模式
    sed -i '' 's/"device-mode": "auto"/"device-mode": "cuda"/' ~/.magic-pdf.json
else
    echo "⚠️  未检测到NVIDIA GPU，使用CPU模式"
    echo "💡 CPU模式性能较低，建议使用GPU加速"
fi
echo ""

# 5. 显示当前配置
echo "📊 当前配置："
echo "   - HuggingFace镜像: https://hf-mirror.com"
echo "   - 模型缓存: $HF_HOME"
echo "   - 配置文件: ~/.magic-pdf.json"
echo ""

# 6. 首次初始化（下载必要的模型）
echo "📦 步骤5: 初始化MinerU（首次需要下载模型）..."
echo "⏳ 正在下载模型文件，请稍候..."
echo ""

# 使用镜像源初始化
HF_ENDPOINT=https://hf-mirror.com mineru --help > /dev/null 2>&1

echo ""
echo "✅ MinerU加速配置完成！"
echo ""
echo "使用建议："
echo "  1. 首次使用会下载模型（约1-2GB），请耐心等待"
echo "  2. 后续使用会直接从缓存加载，速度更快"
echo "  3. 如果网络仍然很慢，建议使用VPN或代理"
echo ""
echo "测试命令："
echo "  mineru -p <输入文件> -o <输出目录>"

