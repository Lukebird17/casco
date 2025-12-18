#!/bin/bash

echo "================================================"
echo "🔧 安装 LibreOffice（用于PPTX/DOCX转PDF）"
echo "================================================"
echo ""

echo "1️⃣ 更新软件包列表..."
sudo apt-get update

echo ""
echo "2️⃣ 安装 LibreOffice..."
sudo apt-get install -y libreoffice-writer libreoffice-impress libreoffice-common

echo ""
echo "3️⃣ 验证安装..."
if command -v libreoffice &> /dev/null; then
    version=$(libreoffice --version)
    echo "   ✅ LibreOffice 安装成功！"
    echo "   版本: $version"
else
    echo "   ❌ LibreOffice 安装失败"
    exit 1
fi

echo ""
echo "================================================"
echo "✅ 安装完成！"
echo "================================================"
echo ""
echo "💡 LibreOffice 用于："
echo "   - 将 PPTX 转换为 PDF（然后用 MinerU 处理）"
echo "   - 将 DOCX 转换为 PDF（然后用 MinerU 处理）"
echo ""
echo "🚀 现在可以上传 PPTX/DOCX 文件了！"
echo ""



