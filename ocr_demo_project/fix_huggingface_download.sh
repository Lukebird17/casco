#!/bin/bash
# 修复 HuggingFace 模型下载问题

echo "=========================================="
echo "  HuggingFace 模型下载问题修复脚本"
echo "=========================================="
echo ""

# 1. 清理代理设置
echo "1️⃣ 清理代理设置..."
unset http_proxy
unset https_proxy
unset HTTP_PROXY
unset HTTPS_PROXY
unset all_proxy
unset ALL_PROXY
echo "✅ 代理已清理"
echo ""

# 2. 切换到官方源
echo "2️⃣ 切换 HuggingFace 源..."
unset HF_ENDPOINT

# 可选：使用国内镜像（如果官方源速度慢）
# export HF_ENDPOINT=https://hf-mirror.com

echo "✅ 已切换到 HuggingFace 官方源"
echo ""

# 3. 设置 HuggingFace 缓存目录
echo "3️⃣ 设置缓存目录..."
export HF_HOME="${HOME}/.cache/huggingface"
export TRANSFORMERS_CACHE="${HOME}/.cache/huggingface/transformers"
mkdir -p "$HF_HOME"
mkdir -p "$TRANSFORMERS_CACHE"
echo "✅ 缓存目录: $HF_HOME"
echo ""

# 4. 忽略系统文件
export HF_HUB_DISABLE_SYMLINKS_WARNING=1
echo "✅ 已配置忽略系统文件警告"
echo ""

# 5. 显示当前环境
echo "=========================================="
echo "当前环境配置:"
echo "=========================================="
echo "HF_ENDPOINT: ${HF_ENDPOINT:-未设置(使用官方源)}"
echo "HF_HOME: ${HF_HOME}"
echo "代理: 已清除"
echo ""

# 6. 尝试下载模型（预检查）
echo "=========================================="
echo "6️⃣ 测试模型下载..."
echo "=========================================="
python3 -c "
import os
os.environ['HF_HUB_DISABLE_SYMLINKS_WARNING'] = '1'
from huggingface_hub import snapshot_download
try:
    print('正在检查模型缓存...')
    path = snapshot_download(
        'BAAI/bge-m3',
        cache_dir=os.path.expanduser('~/.cache/huggingface'),
        allow_patterns=['*.json', '*.txt', '*.model', '*.safetensors', '*.bin', 'config.json', 'tokenizer*'],
        ignore_patterns=['*.DS_Store', '*.git*', 'imgs/*'],
        resume_download=True
    )
    print(f'✅ 模型已就绪: {path}')
except Exception as e:
    print(f'⚠️ 模型下载/检查遇到问题: {e}')
    print('')
    print('建议手动下载模型:')
    print('git lfs install')
    print('git clone https://huggingface.co/BAAI/bge-m3')
    print('然后在代码中使用本地路径')
"

echo ""
echo "=========================================="
echo "✅ 修复完成！"
echo "=========================================="
echo ""
echo "现在可以运行你的程序了:"
echo "  python demo_enhanced.py"
echo ""
echo "如果仍有问题，请手动下载模型:"
echo "  1. 访问: https://huggingface.co/BAAI/bge-m3"
echo "  2. 下载到本地目录"
echo "  3. 修改代码使用本地路径: BGEEmbedding(model_path='/path/to/local/bge-m3')"

