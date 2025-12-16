#!/bin/bash

echo "=== 安装缺失的依赖 ==="

# MinerU（核心OCR引擎）
echo "📦 安装 MinerU..."
pip install mineru

# 其他必要的库
echo "📦 安装其他依赖..."
pip install python-docx
pip install python-pptx
pip install docx2txt
pip install pillow

echo ""
echo "✅ 安装完成！"
echo ""
echo "验证安装："
python -c "import mineru; print('✅ MinerU')" 2>/dev/null || echo "❌ MinerU"
python -c "import docx; print('✅ python-docx')" 2>/dev/null || echo "❌ python-docx"
python -c "import pptx; print('✅ python-pptx')" 2>/dev/null || echo "❌ python-pptx"
python -c "import PIL; print('✅ Pillow')" 2>/dev/null || echo "❌ Pillow"

echo ""
echo "检查命令行工具："
command -v mineru >/dev/null 2>&1 && echo "✅ mineru 命令可用" || echo "⚠️  mineru 命令不在PATH中"
