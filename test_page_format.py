#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
测试新的页码标注格式
"""

from enhanced_ocr import EnhancedOCRProcessor
from document_loader import DocumentLoader
from pathlib import Path

def test_page_format():
    """测试页码标注在文本中的格式"""
    
    print("=" * 80)
    print("测试新的页码标注格式")
    print("=" * 80)
    
    # 找一个已处理的PDF文件
    test_file = None
    for pdf_file in Path("data").rglob("*.pdf"):
        test_file = str(pdf_file)
        break
    
    if not test_file:
        print("❌ 没有找到测试PDF文件")
        return
    
    print(f"\n📄 测试文件: {test_file}")
    
    # 初始化loader
    loader = DocumentLoader()
    
    # 加载文档
    print(f"\n🔄 加载文档...")
    pages, images = loader.load_pdf(test_file)
    
    if not pages:
        print("❌ 没有加载到内容")
        return
    
    print(f"\n✅ 加载成功！")
    print(f"   - 页数: {len(pages)}")
    print(f"   - 图片数: {len(images)}")
    
    # 展示前3页的格式
    print(f"\n" + "=" * 80)
    print("📋 内容格式示例（前3页）")
    print("=" * 80)
    
    for i, page in enumerate(pages[:3], 1):
        text = page.get('text', '')
        page_num = page.get('page_number', 0)
        
        # 显示前200字符
        preview = text[:200].replace('\n', '\n   ')
        
        print(f"\n【页面 {i}】(page_number={page_num})")
        print(f"   {preview}...")
        print(f"   ...")
    
    # 检查页码标注
    print(f"\n" + "=" * 80)
    print("🔍 页码标注检查")
    print("=" * 80)
    
    has_page_marker = False
    for page in pages[:5]:
        text = page.get('text', '')
        if '【第' in text and '页】' in text:
            has_page_marker = True
            # 提取页码标记
            import re
            markers = re.findall(r'【第(\d+)页】', text)
            if markers:
                print(f"   ✅ 找到页码标记: 【第{markers[0]}页】")
                break
    
    if has_page_marker:
        print(f"\n✅ 页码标注格式正确！")
        print(f"   格式: 【第X页】...内容...【/第X页】")
    else:
        print(f"\n⚠️  未找到页码标注")
    
    # 检查图片描述中的页码
    if images:
        print(f"\n" + "=" * 80)
        print("🖼️  图片描述中的页码")
        print("=" * 80)
        
        for img in images[:3]:
            page_num = img.get('page_number', 0)
            desc = img.get('description', '')[:50]
            print(f"   图片在第{page_num}页: {desc}...")
    
    print(f"\n" + "=" * 80)
    print("✅ 测试完成！")
    print("=" * 80)

if __name__ == "__main__":
    test_page_format()


