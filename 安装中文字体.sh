#!/bin/bash

echo "================================================"
echo "🔤 安装中文字体（无需sudo）"
echo "================================================"
echo ""

# 用户字体目录
FONT_DIR="$HOME/.local/share/fonts"
LO_FONT_DIR="/home/honglianglu/hdd/my_libreoffice/extracted_libreoffice/opt/libreoffice25.8/share/fonts/truetype"

echo "📁 字体安装目录:"
echo "   用户字体: $FONT_DIR"
echo "   LibreOffice字体: $LO_FONT_DIR"
echo ""

# 创建字体目录
mkdir -p "$FONT_DIR"
mkdir -p "$LO_FONT_DIR"

echo "1️⃣ 检查系统中文字体..."
echo ""

# 查找系统中的中文字体
SYSTEM_FONTS=$(find /usr/share/fonts -name "*SimSun*" -o -name "*SimHei*" -o -name "*WenQuanYi*" -o -name "*Noto*CJK*" 2>/dev/null | head -10)

if [ -z "$SYSTEM_FONTS" ]; then
    echo "⚠️  未找到系统中文字体"
    echo ""
    echo "💡 解决方案："
    echo ""
    echo "方案1: 从网上下载中文字体（推荐）"
    echo "  wget https://github.com/adobe-fonts/source-han-sans/releases/download/2.004R/SourceHanSansCN.zip"
    echo "  unzip SourceHanSansCN.zip -d $FONT_DIR"
    echo ""
    echo "方案2: 从Windows复制字体"
    echo "  cp /path/to/SimSun.ttf $FONT_DIR/"
    echo "  cp /path/to/SimHei.ttf $FONT_DIR/"
    echo ""
    echo "方案3: 使用在线字体"
    echo "  (需要网络连接)"
    exit 1
fi

echo "✅ 找到系统中文字体:"
echo "$SYSTEM_FONTS" | while read font; do
    if [ -f "$font" ]; then
        fontname=$(basename "$font")
        echo "   - $fontname"
    fi
done

echo ""
echo "2️⃣ 复制字体到用户目录..."
echo ""

copied=0
echo "$SYSTEM_FONTS" | while read font; do
    if [ -f "$font" ]; then
        fontname=$(basename "$font")
        
        # 复制到用户字体目录
        if [ ! -f "$FONT_DIR/$fontname" ]; then
            cp "$font" "$FONT_DIR/"
            echo "   ✅ $fontname → $FONT_DIR/"
            ((copied++))
        fi
        
        # 复制到LibreOffice字体目录
        if [ ! -f "$LO_FONT_DIR/$fontname" ]; then
            cp "$font" "$LO_FONT_DIR/"
            echo "   ✅ $fontname → $LO_FONT_DIR/"
        fi
    fi
done

echo ""
echo "3️⃣ 更新字体缓存..."
fc-cache -f "$FONT_DIR" 2>/dev/null || echo "   ⚠️  无法更新字体缓存（需要fontconfig）"

echo ""
echo "4️⃣ 验证安装..."
echo ""

# 列出已安装的中文字体
if [ -d "$FONT_DIR" ]; then
    font_count=$(ls "$FONT_DIR"/*.ttf "$FONT_DIR"/*.TTF "$FONT_DIR"/*.otf "$FONT_DIR"/*.OTF 2>/dev/null | wc -l)
    echo "   用户字体目录: $font_count 个字体"
    ls "$FONT_DIR"/*.{ttf,TTF,otf,OTF} 2>/dev/null | while read f; do
        echo "     - $(basename "$f")"
    done
fi

echo ""
if [ -d "$LO_FONT_DIR" ]; then
    lo_font_count=$(ls "$LO_FONT_DIR"/*.ttf "$LO_FONT_DIR"/*.TTF "$LO_FONT_DIR"/*.otf "$LO_FONT_DIR"/*.OTF 2>/dev/null | wc -l)
    echo "   LibreOffice字体: $lo_font_count 个字体"
fi

echo ""
echo "================================================"
echo "✅ 字体安装完成！"
echo "================================================"
echo ""
echo "💡 现在测试转换:"
echo "   cd /tmp"
echo "   /home/honglianglu/hdd/my_libreoffice/.../soffice --headless --convert-to pdf test.docx"
echo ""
echo "   然后检查PDF中的中文是否正常显示"
echo ""



