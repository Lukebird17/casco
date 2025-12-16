#!/usr/bin/env python3
"""
测试 MinerU 图片页码提取的准确性
"""

import sys
from enhanced_ocr import EnhancedOCRProcessor

def test_page_number_accuracy():
    """测试页码准确性"""
    
    print("=" * 60)
    print("测试图片页码提取")
    print("=" * 60)
    
    # 初始化处理器
    processor = EnhancedOCRProcessor(use_cache=True)
    
    # 测试文件
    test_file = "./data/OS-08 pm-manage.pdf"
    
    print(f"\n📄 处理文件: {test_file}")
    
    # 处理文件（会使用缓存）
    result = processor.process_file(test_file)
    
    if not result:
        print("❌ 文件处理失败")
        return
    
    images = result.get('images', [])
    print(f"\n✅ 找到 {len(images)} 张图片")
    
    # 显示所有图片的页码信息
    print("\n图片页码信息：")
    print("-" * 60)
    
    for i, img_info in enumerate(images, 1):
        img_name = img_info.get('image_name', 'N/A')
        page_num = img_info.get('page_number', 0)
        section = img_info.get('section', 'N/A')
        
        print(f"{i:2d}. {img_name[:20]}... -> 第 {page_num:2d} 页")
        print(f"    章节: {section[:40]}")
    
    # 重点检查第28页的slab图
    print("\n" + "=" * 60)
    print("查找第28页的图片：")
    print("=" * 60)
    
    page_28_images = [img for img in images if img.get('page_number') == 28]
    
    if page_28_images:
        print(f"\n✅ 找到 {len(page_28_images)} 张第28页的图片：")
        for img in page_28_images:
            print(f"\n  图片: {img.get('image_name')}")
            print(f"  路径: {img.get('image_path')}")
            print(f"  章节: {img.get('section')}")
            print(f"  上下文: {img.get('context', '')[:100]}...")
    else:
        print("❌ 没有找到第28页的图片")
    
    print("\n" + "=" * 60)
    print("测试完成！")
    print("=" * 60)

if __name__ == "__main__":
    test_page_number_accuracy()

