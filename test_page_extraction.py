#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
测试页码提取功能
"""

from enhanced_ocr import EnhancedOCRProcessor
from pathlib import Path

def test_page_extraction():
    """测试从MinerU输出中提取准确的页码"""
    
    # 找一个已经处理过的文件
    mineru_output_dir = Path(".mineru_output")
    
    if not mineru_output_dir.exists():
        print("❌ .mineru_output 目录不存在")
        return
    
    # 找第一个输出目录
    output_dirs = list(mineru_output_dir.glob("*/"))
    if not output_dirs:
        print("❌ 没有找到MinerU输出")
        return
    
    test_dir = output_dirs[0]
    print(f"📁 测试目录: {test_dir}")
    
    # 直接调用解析方法（不需要完整初始化）
    from enhanced_ocr import EnhancedOCRProcessor
    processor = object.__new__(EnhancedOCRProcessor)
    
    # 解析输出
    result = processor._parse_mineru_output(str(test_dir), "test.pdf")
    
    print(f"\n📊 解析结果:")
    print(f"   - 文本块数: {result.get('text_blocks', 0)}")
    print(f"   - 图片数: {result.get('image_count', 0)}")
    print(f"   - 页面数: {len(result.get('pages', []))}")
    
    if result.get('pages'):
        print(f"\n📄 页面信息:")
        for i, page in enumerate(result['pages'][:5]):  # 只显示前5页
            page_num = page.get('page_number', 0)
            content_preview = page.get('content', '')[:100].replace('\n', ' ')
            print(f"   第{page_num}页: {content_preview}...")
    
    if result.get('images'):
        print(f"\n🖼️  图片信息:")
        for i, img in enumerate(result['images'][:3]):  # 只显示前3张
            page_num = img.get('page_number', 0)
            img_path = img.get('image_path', '')
            print(f"   图片{i+1}: 第{page_num}页, {Path(img_path).name}")
    
    print(f"\n✅ 测试完成！")

if __name__ == "__main__":
    test_page_extraction()

