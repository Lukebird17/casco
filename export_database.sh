#!/bin/bash

# 🎯 OmniScry 数据库迁移打包脚本
# 自动打包数据库，方便分享给他人

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "   📦 OmniScry 数据库迁移打包工具"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# 检查是否在正确的目录
if [ ! -d "data" ] || [ ! -d "vector_db" ]; then
    echo "❌ 错误: 请在 rag-agent 根目录运行此脚本"
    exit 1
fi

# 设置输出文件名
OUTPUT_DIR="$HOME"
DATE=$(date +%Y%m%d_%H%M%S)
OUTPUT_FILE="$OUTPUT_DIR/omniscry_migration_$DATE.tar.gz"

echo "📊 正在扫描数据库..."
echo ""

# 统计各知识库的大小
echo "知识库统计："
for kb in data/*/; do
    kb_name=$(basename "$kb")
    if [ "$kb_name" != "*" ]; then
        doc_count=$(find "$kb" -type f \( -name "*.pdf" -o -name "*.docx" -o -name "*.pptx" \) 2>/dev/null | wc -l)
        doc_size=$(du -sh "$kb" 2>/dev/null | awk '{print $1}')
        vector_size=$(du -sh "vector_db/$kb_name" 2>/dev/null | awk '{print $1}')
        echo "  📚 $kb_name: $doc_count 个文档, 原文件 $doc_size, 向量库 $vector_size"
    fi
done
echo ""

# 询问用户要打包哪些知识库
echo "打包选项："
echo "  1) 全部知识库（推荐）"
echo "  2) 仅指定知识库"
echo "  3) 取消"
echo ""
read -p "请选择 [1-3]: " choice

case $choice in
    1)
        echo ""
        echo "📦 正在打包全部知识库..."
        
        # 检查要打包的目录是否存在
        ITEMS_TO_PACK=""
        
        if [ -d "data" ]; then
            ITEMS_TO_PACK="$ITEMS_TO_PACK data/"
        fi
        
        if [ -d "vector_db" ]; then
            ITEMS_TO_PACK="$ITEMS_TO_PACK vector_db/"
        fi
        
        if [ -d "backend/static/doc_images" ]; then
            ITEMS_TO_PACK="$ITEMS_TO_PACK backend/static/doc_images/"
        fi
        
        if [ -z "$ITEMS_TO_PACK" ]; then
            echo "❌ 错误: 没有找到任何数据库文件"
            exit 1
        fi
        
        # 创建压缩包
        tar -czf "$OUTPUT_FILE" \
            --exclude='*.log' \
            --exclude='.gitkeep' \
            --exclude='__pycache__' \
            $ITEMS_TO_PACK \
            README.md \
            requirements.txt \
            start.sh \
            stop.sh \
            2>/dev/null
        
        if [ $? -eq 0 ]; then
            echo "✅ 打包完成！"
        else
            echo "❌ 打包失败"
            exit 1
        fi
        ;;
        
    2)
        echo ""
        echo "可用的知识库："
        kb_list=()
        index=1
        for kb in data/*/; do
            kb_name=$(basename "$kb")
            if [ "$kb_name" != "*" ]; then
                echo "  $index) $kb_name"
                kb_list+=("$kb_name")
                ((index++))
            fi
        done
        echo ""
        read -p "请输入知识库编号（多个用空格分隔）: " kb_indices
        
        # 构建要打包的文件列表
        ITEMS_TO_PACK=""
        for idx in $kb_indices; do
            if [ $idx -ge 1 ] && [ $idx -le ${#kb_list[@]} ]; then
                kb_name="${kb_list[$((idx-1))]}"
                echo "  ✓ 选择了: $kb_name"
                
                if [ -d "data/$kb_name" ]; then
                    ITEMS_TO_PACK="$ITEMS_TO_PACK data/$kb_name"
                fi
                
                if [ -d "vector_db/$kb_name" ]; then
                    ITEMS_TO_PACK="$ITEMS_TO_PACK vector_db/$kb_name"
                fi
            fi
        done
        
        if [ -z "$ITEMS_TO_PACK" ]; then
            echo "❌ 错误: 没有选择有效的知识库"
            exit 1
        fi
        
        echo ""
        echo "📦 正在打包选定的知识库..."
        
        # 创建临时目录结构
        TEMP_DIR=$(mktemp -d)
        mkdir -p "$TEMP_DIR/data" "$TEMP_DIR/vector_db"
        
        for item in $ITEMS_TO_PACK; do
            if [[ $item == data/* ]]; then
                kb_name=$(basename "$item")
                cp -r "data/$kb_name" "$TEMP_DIR/data/"
            elif [[ $item == vector_db/* ]]; then
                kb_name=$(basename "$item")
                cp -r "vector_db/$kb_name" "$TEMP_DIR/vector_db/"
            fi
        done
        
        # 复制文档图片（如果有）
        if [ -d "backend/static/doc_images" ]; then
            mkdir -p "$TEMP_DIR/backend/static"
            cp -r "backend/static/doc_images" "$TEMP_DIR/backend/static/"
        fi
        
        # 复制必要文件
        cp README.md requirements.txt start.sh stop.sh "$TEMP_DIR/" 2>/dev/null
        
        # 打包
        tar -czf "$OUTPUT_FILE" -C "$TEMP_DIR" . 2>/dev/null
        
        # 清理临时目录
        rm -rf "$TEMP_DIR"
        
        if [ $? -eq 0 ]; then
            echo "✅ 打包完成！"
        else
            echo "❌ 打包失败"
            exit 1
        fi
        ;;
        
    3)
        echo "取消打包"
        exit 0
        ;;
        
    *)
        echo "❌ 无效选择"
        exit 1
        ;;
esac

# 显示结果
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✨ 打包成功！"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📦 文件位置: $OUTPUT_FILE"
echo "📊 文件大小: $(ls -lh "$OUTPUT_FILE" | awk '{print $5}')"
echo ""
echo "📝 使用说明："
echo "   1. 将此文件传输给对方（SCP/云盘/U盘）"
echo "   2. 对方解压到他们的 rag-agent 目录："
echo "      cd /path/to/their/rag-agent"
echo "      tar -xzf $OUTPUT_FILE"
echo "   3. 对方修改 config.py 中的 API 密钥"
echo "   4. 对方启动系统: ./start.sh"
echo ""
echo "📚 详细说明: 查看 DATABASE_MIGRATION_GUIDE.md"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"



