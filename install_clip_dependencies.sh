#!/bin/bash
# 安装 CLIP 模型相关依赖

echo "=== 安装双索引系统依赖 ==="
echo ""

# 检查 conda 环境
if [ -z "$CONDA_DEFAULT_ENV" ]; then
    echo "⚠️  请先激活 conda 环境: conda activate rag"
    exit 1
fi

echo "当前环境: $CONDA_DEFAULT_ENV"
echo ""

# 1. 安装 transformers 和 torch（如果未安装）
echo "📦 步骤1: 检查 PyTorch 和 Transformers..."
python -c "import torch; print(f'✅ PyTorch {torch.__version__} 已安装')" 2>/dev/null || {
    echo "安装 PyTorch..."
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
}

python -c "import transformers; print(f'✅ Transformers 已安装')" 2>/dev/null || {
    echo "安装 Transformers..."
    pip install transformers
}

# 2. 安装 PIL/Pillow
echo ""
echo "📦 步骤2: 检查 Pillow..."
python -c "from PIL import Image; print('✅ Pillow 已安装')" 2>/dev/null || {
    echo "安装 Pillow..."
    pip install Pillow
}

# 3. 下载 CLIP 模型（使用 HuggingFace 镜像加速）
echo ""
echo "📦 步骤3: 下载 CLIP 模型..."
echo ""
echo "模型选择说明："
echo "  1. openai/clip-vit-base-patch32 (推荐) - 中英文混合，通用性好"
echo "  2. openai/clip-vit-large-patch14 - 更强但更大，需要更多内存"
echo "  3. OFA-Sys/chinese-clip-vit-base-patch16 - 中文优化，英文效果一般"
echo ""
echo "默认下载: openai/clip-vit-base-patch32 (适合中英文混合场景)"
echo ""

export HF_ENDPOINT=https://hf-mirror.com

python -c "
from transformers import CLIPModel, CLIPProcessor
import sys

# 默认使用原版 CLIP（对中英文都有良好支持）
model_name = 'openai/clip-vit-base-patch32'

print(f'正在下载 {model_name}...')
print('此模型对中英文图片都有良好的识别能力')
print()

try:
    model = CLIPModel.from_pretrained(model_name)
    processor = CLIPProcessor.from_pretrained(model_name)
    print('✅ 模型下载完成')
    print(f'   模型维度: {model.config.projection_dim}')
except Exception as e:
    print(f'⚠️  下载失败: {e}')
    print('💡 请检查网络连接或使用 VPN')
    sys.exit(1)
"

echo ""
echo "=== 安装完成 ==="
echo ""
echo "测试命令："
echo "  python -c 'from image_vector_store import ImageVectorStore; print(\"✅ 图片向量存储可用\")'"
echo ""

