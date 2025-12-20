#!/bin/bash
# 预下载CLIP模型到本地缓存

echo "📥 预下载 CLIP 模型到本地..."
echo "============================================================"
echo ""

# 设置HuggingFace镜像（可选）
export HF_ENDPOINT=https://hf-mirror.com

# 使用Python预下载模型
python3 << 'EOF'
from transformers import CLIPModel, CLIPProcessor
import os

print("🔧 开始下载 CLIP 模型...")
print("   模型: openai/clip-vit-base-patch32")
print("")

try:
    # 下载模型和处理器
    model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
    processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
    
    print("✅ CLIP 模型下载完成！")
    print(f"   缓存位置: {os.path.expanduser('~/.cache/huggingface')}")
    print("")
    print("📝 下次启动将直接从本地加载，无需联网")
    
except Exception as e:
    print(f"❌ 下载失败: {e}")
    print("")
    print("💡 解决建议:")
    print("   1. 检查网络连接")
    print("   2. 使用方案2（更换镜像源）")
    print("   3. 使用方案3（禁用CLIP）")

EOF

echo ""
echo "============================================================"
echo "✨ 完成！"

