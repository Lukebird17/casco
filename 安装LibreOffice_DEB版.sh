#!/bin/bash

echo "================================================"
echo "🔧 在用户目录安装 LibreOffice (DEB版本，无需sudo)"
echo "================================================"
echo ""

# 设置安装目录
INSTALL_DIR="$HOME/.local/libreoffice"
TEMP_DIR="/tmp/libreoffice_install_$$"

echo "📍 安装目录: $INSTALL_DIR"
echo ""

# 检测系统架构
ARCH=$(uname -m)
if [ "$ARCH" = "x86_64" ]; then
    ARCH="x86-64"
elif [ "$ARCH" = "aarch64" ]; then
    ARCH="aarch64"
else
    echo "❌ 不支持的架构: $ARCH"
    exit 1
fi

echo "🖥️  系统架构: $ARCH"
echo ""

# LibreOffice版本
LO_VERSION="24.2.7"

# 下载URL (DEB包)
LO_URL="https://download.documentfoundation.org/libreoffice/stable/${LO_VERSION}/deb/x86_64/LibreOffice_${LO_VERSION}_Linux_x86-64_deb.tar.gz"

echo "1️⃣ 下载 LibreOffice ${LO_VERSION}..."
echo "   URL: $LO_URL"
echo "   这可能需要几分钟，请耐心等待..."
echo ""

# 创建临时目录
mkdir -p "$TEMP_DIR"
cd "$TEMP_DIR"

# 下载
wget -q --show-progress "$LO_URL" -O libreoffice.tar.gz

if [ $? -ne 0 ]; then
    echo "❌ 下载失败"
    echo "💡 请尝试手动安装或使用RPM版本"
    rm -rf "$TEMP_DIR"
    exit 1
fi

echo ""
echo "2️⃣ 解压文件..."
tar -xzf libreoffice.tar.gz

# 找到解压后的目录
LO_DIR=$(find . -maxdepth 1 -type d -name "LibreOffice*" | head -n 1)

if [ -z "$LO_DIR" ]; then
    echo "❌ 未找到LibreOffice目录"
    rm -rf "$TEMP_DIR"
    exit 1
fi

echo "   找到目录: $LO_DIR"
echo ""

echo "3️⃣ 提取DEB包..."
cd "$LO_DIR/DEBS"

# 创建安装目录
mkdir -p "$INSTALL_DIR"

# 提取所有DEB包
for deb in *.deb; do
    echo "   提取: $deb"
    ar x "$deb" 2>/dev/null
    if [ -f data.tar.xz ]; then
        tar -xJf data.tar.xz -C "$INSTALL_DIR" 2>/dev/null
        rm data.tar.xz
    elif [ -f data.tar.gz ]; then
        tar -xzf data.tar.gz -C "$INSTALL_DIR" 2>/dev/null
        rm data.tar.gz
    fi
    rm -f control.tar.* debian-binary 2>/dev/null
done

echo ""
echo "4️⃣ 设置符号链接..."

# 创建bin目录
mkdir -p "$HOME/.local/bin"

# 找到LibreOffice程序目录
LO_PROGRAM_DIR=$(find "$INSTALL_DIR" -type d -path "*/opt/libreoffice*/program" | head -n 1)

if [ -z "$LO_PROGRAM_DIR" ]; then
    echo "❌ 未找到LibreOffice程序目录"
    rm -rf "$TEMP_DIR"
    exit 1
fi

# 创建符号链接
ln -sf "$LO_PROGRAM_DIR/soffice" "$HOME/.local/bin/libreoffice"
ln -sf "$LO_PROGRAM_DIR/soffice" "$HOME/.local/bin/soffice"

echo "   符号链接: $HOME/.local/bin/libreoffice -> $LO_PROGRAM_DIR/soffice"
echo ""

echo "5️⃣ 配置环境变量..."

# 检查shell类型
SHELL_RC="$HOME/.bashrc"
if [ -n "$ZSH_VERSION" ]; then
    SHELL_RC="$HOME/.zshrc"
fi

# 添加到PATH
if ! grep -q "$HOME/.local/bin" "$SHELL_RC" 2>/dev/null; then
    echo "" >> "$SHELL_RC"
    echo "# LibreOffice (用户安装)" >> "$SHELL_RC"
    echo "export PATH=\"\$HOME/.local/bin:\$PATH\"" >> "$SHELL_RC"
    echo "   已添加到 $SHELL_RC"
else
    echo "   PATH 已配置"
fi

echo ""
echo "6️⃣ 清理临时文件..."
rm -rf "$TEMP_DIR"

echo ""
echo "7️⃣ 验证安装..."

# 临时添加到PATH
export PATH="$HOME/.local/bin:$PATH"

# 测试
if "$HOME/.local/bin/libreoffice" --version >/dev/null 2>&1; then
    VERSION=$("$HOME/.local/bin/libreoffice" --version 2>/dev/null | head -n 1)
    echo "   ✅ LibreOffice 安装成功！"
    echo "   版本: $VERSION"
else
    echo "   ⚠️  安装完成，但验证失败"
    echo "   请手动测试: $HOME/.local/bin/libreoffice --version"
fi

echo ""
echo "================================================"
echo "✅ 安装完成！"
echo "================================================"
echo ""
echo "📍 安装位置:"
echo "   程序: $LO_PROGRAM_DIR"
echo "   链接: $HOME/.local/bin/libreoffice"
echo ""
echo "🔄 使环境变量生效 (选择一种方式):"
echo ""
echo "   方式1: 重新加载配置"
echo "   source $SHELL_RC"
echo ""
echo "   方式2: 当前终端临时使用"
echo "   export PATH=\"\$HOME/.local/bin:\$PATH\""
echo ""
echo "   方式3: 重新打开终端"
echo ""
echo "🧪 测试安装:"
echo "   libreoffice --version"
echo ""
echo "💡 现在可以重启后端，LibreOffice功能将自动生效！"
echo ""



