#!/bin/bash

echo "======================================"
echo "📦 安装文档查看功能依赖"
echo "======================================"

# 激活conda环境
source ~/miniconda3/etc/profile.d/conda.sh
conda activate rag

echo ""
echo "1️⃣ 安装 mammoth (DOCX转HTML)"
pip install mammoth

echo ""
echo "2️⃣ 检查已安装的库"
python -c "
import sys
try:
    import mammoth
    print('✅ mammoth:', mammoth.__version__)
except:
    print('❌ mammoth 未安装')

try:
    import PyPDF2
    print('✅ PyPDF2:', PyPDF2.__version__)
except:
    print('❌ PyPDF2 未安装')

try:
    from pptx import Presentation
    print('✅ python-pptx: 已安装')
except:
    print('❌ python-pptx 未安装')

try:
    import docx
    print('✅ python-docx: 已安装')
except:
    print('❌ python-docx 未安装')
"

echo ""
echo "======================================"
echo "✅ 依赖安装完成"
echo "======================================"



