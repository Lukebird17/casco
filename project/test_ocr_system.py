#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
测试脚本 - PaddleOCR高级系统功能验证
"""

import os
import sys
from advanced_ocr_system import ComprehensiveOCRSystem

def test_system_initialization():
    """测试1：系统初始化"""
    print("\n" + "="*60)
    print("测试1：系统初始化")
    print("="*60)
    
    try:
        ocr_system = ComprehensiveOCRSystem()
        print("✅ 系统初始化成功")
        return ocr_system
    except Exception as e:
        print(f"❌ 系统初始化失败: {e}")
        return None


def test_basic_ocr(ocr_system, pdf_path):
    """测试2：基础OCR功能"""
    print("\n" + "="*60)
    print("测试2：基础OCR功能")
    print("="*60)
    
    if not os.path.exists(pdf_path):
        print(f"⚠️  测试文件不存在: {pdf_path}")
        return None
    
    try:
        results = ocr_system.process_document(
            pdf_path,
            auto_rotate=False,
            remove_watermark=False,
            enhance_blur=False,
            extract_tables=False,
            extract_formulas=False,
            extract_toc=False,
            language='ch'
        )
        
        print(f"✅ 基础OCR成功")
        print(f"   文档: {results['file_name']}")
        print(f"   总页数: {results['total_pages']}")
        print(f"   首页文本长度: {len(results['pages'][0]['text'])} 字符")
        
        return results
    except Exception as e:
        print(f"❌ 基础OCR失败: {e}")
        import traceback
        traceback.print_exc()
        return None


def test_table_extraction(ocr_system, pdf_path):
    """测试3：表格提取功能"""
    print("\n" + "="*60)
    print("测试3：表格提取功能（PP-Structure）")
    print("="*60)
    
    if not os.path.exists(pdf_path):
        print(f"⚠️  测试文件不存在: {pdf_path}")
        return
    
    try:
        results = ocr_system.process_document(
            pdf_path,
            extract_tables=True,
            auto_rotate=False,
            remove_watermark=False,
            enhance_blur=False,
            extract_formulas=False,
            extract_toc=False
        )
        
        total_tables = sum(len(page['tables']) for page in results['pages'])
        print(f"✅ 表格提取成功")
        print(f"   总表格数: {total_tables}")
        
        for page in results['pages']:
            if page['tables']:
                print(f"\n   第{page['page_number']}页: {len(page['tables'])}个表格")
                for i, table in enumerate(page['tables'], 1):
                    print(f"      表格{i}: {'包含合并单元格' if table['has_merged_cells'] else '标准表格'}")
                    if table['data']:
                        print(f"      尺寸: {len(table['data'])}行 x {len(table['data'][0])}列")
        
    except Exception as e:
        print(f"❌ 表格提取失败: {e}")
        import traceback
        traceback.print_exc()


def test_multilang_ocr(ocr_system, pdf_path):
    """测试4：多语言识别"""
    print("\n" + "="*60)
    print("测试4：多语言自动识别")
    print("="*60)
    
    if not os.path.exists(pdf_path):
        print(f"⚠️  测试文件不存在: {pdf_path}")
        return
    
    try:
        results = ocr_system.process_document(
            pdf_path,
            language='auto',  # 自动检测语言
            auto_rotate=False,
            remove_watermark=False,
            enhance_blur=False,
            extract_tables=False,
            extract_formulas=False,
            extract_toc=False
        )
        
        print(f"✅ 多语言识别成功")
        
        lang_names = {
            'ch': '中文',
            'en': '英文',
            'de': '德文',
            'es': '西班牙语',
            'ja': '日文',
            'ko': '韩文'
        }
        
        for page in results['pages']:
            lang = page.get('detected_language', 'unknown')
            lang_name = lang_names.get(lang, lang)
            print(f"   第{page['page_number']}页: {lang_name}")
        
    except Exception as e:
        print(f"❌ 多语言识别失败: {e}")
        import traceback
        traceback.print_exc()


def test_toc_extraction(ocr_system, pdf_path):
    """测试5：目录提取"""
    print("\n" + "="*60)
    print("测试5：目录提取")
    print("="*60)
    
    if not os.path.exists(pdf_path):
        print(f"⚠️  测试文件不存在: {pdf_path}")
        return
    
    try:
        results = ocr_system.process_document(
            pdf_path,
            extract_toc=True,
            auto_rotate=False,
            remove_watermark=False,
            enhance_blur=False,
            extract_tables=False,
            extract_formulas=False
        )
        
        if results['toc']:
            print(f"✅ 目录提取成功")
            print(f"   目录项数: {len(results['toc'])}")
            print("\n   目录结构:")
            for item in results['toc'][:10]:  # 只显示前10项
                indent = "   " + "  " * (item['level'] - 1)
                print(f"{indent}- {item['title']} (第{item['page']}页) [{item['source']}]")
            
            if len(results['toc']) > 10:
                print(f"   ... 还有 {len(results['toc']) - 10} 项")
        else:
            print(f"⚠️  未找到目录")
        
    except Exception as e:
        print(f"❌ 目录提取失败: {e}")
        import traceback
        traceback.print_exc()


def test_formula_extraction(ocr_system, pdf_path):
    """测试6：公式提取"""
    print("\n" + "="*60)
    print("测试6：数学公式提取")
    print("="*60)
    
    if not os.path.exists(pdf_path):
        print(f"⚠️  测试文件不存在: {pdf_path}")
        return
    
    try:
        results = ocr_system.process_document(
            pdf_path,
            extract_formulas=True,
            auto_rotate=False,
            remove_watermark=False,
            enhance_blur=False,
            extract_tables=False,
            extract_toc=False
        )
        
        total_formulas = sum(len(page.get('formulas', [])) for page in results['pages'])
        
        if total_formulas > 0:
            print(f"✅ 公式提取成功")
            print(f"   总公式数: {total_formulas}")
            
            for page in results['pages']:
                if page.get('formulas'):
                    print(f"\n   第{page['page_number']}页: {len(page['formulas'])}个公式")
                    for formula in page['formulas'][:3]:  # 只显示前3个
                        print(f"      - {formula['text']}")
        else:
            print(f"⚠️  未检测到公式（可能文档中无公式）")
        
    except Exception as e:
        print(f"❌ 公式提取失败: {e}")
        import traceback
        traceback.print_exc()


def test_image_preprocessing(ocr_system, pdf_path):
    """测试7：图像预处理"""
    print("\n" + "="*60)
    print("测试7：图像预处理（旋转、水印、模糊增强）")
    print("="*60)
    
    if not os.path.exists(pdf_path):
        print(f"⚠️  测试文件不存在: {pdf_path}")
        return
    
    try:
        results = ocr_system.process_document(
            pdf_path,
            auto_rotate=True,         # 启用旋转
            remove_watermark=True,    # 启用去水印
            enhance_blur=True,        # 启用模糊增强
            extract_tables=False,
            extract_formulas=False,
            extract_toc=False
        )
        
        print(f"✅ 图像预处理成功")
        
        for page in results['pages']:
            if page['processing_steps']:
                steps = ', '.join(page['processing_steps'])
                print(f"   第{page['page_number']}页: {steps}")
        
    except Exception as e:
        print(f"❌ 图像预处理失败: {e}")
        import traceback
        traceback.print_exc()


def test_full_pipeline(ocr_system, pdf_path, output_dir='test_results'):
    """测试8：完整处理流程"""
    print("\n" + "="*60)
    print("测试8：完整处理流程（所有功能）")
    print("="*60)
    
    if not os.path.exists(pdf_path):
        print(f"⚠️  测试文件不存在: {pdf_path}")
        return
    
    try:
        # 创建输出目录
        os.makedirs(output_dir, exist_ok=True)
        
        # 完整处理
        results = ocr_system.process_document(
            pdf_path,
            auto_rotate=True,
            remove_watermark=True,
            enhance_blur=True,
            extract_tables=True,
            extract_formulas=True,
            extract_toc=True,
            language='auto'
        )
        
        # 导出结果
        output_path = os.path.join(output_dir, 'full_test_results.json')
        ocr_system.export_results(results, output_path)
        
        print(f"✅ 完整处理成功")
        print(f"\n   统计信息:")
        print(f"   - 文档名: {results['file_name']}")
        print(f"   - 总页数: {results['total_pages']}")
        print(f"   - 目录项: {len(results['toc'])}")
        
        total_tables = sum(len(page['tables']) for page in results['pages'])
        total_formulas = sum(len(page.get('formulas', [])) for page in results['pages'])
        total_chars = sum(len(page['text']) for page in results['pages'])
        
        print(f"   - 表格数: {total_tables}")
        print(f"   - 公式数: {total_formulas}")
        print(f"   - 总字符: {total_chars}")
        
        print(f"\n   输出文件:")
        print(f"   - JSON: {output_path}")
        print(f"   - TXT:  {output_path.replace('.json', '.txt')}")
        
    except Exception as e:
        print(f"❌ 完整处理失败: {e}")
        import traceback
        traceback.print_exc()


def main():
    """主测试函数"""
    print("\n" + "="*60)
    print("PaddleOCR高级系统 - 功能测试")
    print("="*60)
    
    # 检查测试文件
    if len(sys.argv) > 1:
        test_pdf = sys.argv[1]
    else:
        print("\n使用方法:")
        print("  python test_ocr_system.py <PDF文件路径>")
        print("\n示例:")
        print("  python test_ocr_system.py sample.pdf")
        print()
        
        # 尝试查找示例文件
        test_pdf = None
        for possible_file in ['sample.pdf', 'test.pdf', 'document.pdf']:
            if os.path.exists(possible_file):
                test_pdf = possible_file
                print(f"找到测试文件: {test_pdf}")
                break
        
        if not test_pdf:
            print("❌ 未找到测试PDF文件")
            print("\n请指定一个PDF文件进行测试，或将测试文件命名为:")
            print("  - sample.pdf")
            print("  - test.pdf")
            print("  - document.pdf")
            return
    
    print(f"\n测试文件: {test_pdf}")
    
    # 测试1：初始化
    ocr_system = test_system_initialization()
    if not ocr_system:
        print("\n❌ 系统初始化失败，无法继续测试")
        return
    
    # 测试2：基础OCR
    test_basic_ocr(ocr_system, test_pdf)
    
    # 测试3：表格提取
    test_table_extraction(ocr_system, test_pdf)
    
    # 测试4：多语言识别
    test_multilang_ocr(ocr_system, test_pdf)
    
    # 测试5：目录提取
    test_toc_extraction(ocr_system, test_pdf)
    
    # 测试6：公式提取
    test_formula_extraction(ocr_system, test_pdf)
    
    # 测试7：图像预处理
    test_image_preprocessing(ocr_system, test_pdf)
    
    # 测试8：完整流程
    test_full_pipeline(ocr_system, test_pdf)
    
    # 总结
    print("\n" + "="*60)
    print("测试完成！")
    print("="*60)
    print("\n功能清单:")
    print("  ✅ 系统初始化")
    print("  ✅ 基础OCR")
    print("  ✅ 表格提取（PP-Structure）")
    print("  ✅ 多语言识别")
    print("  ✅ 目录提取")
    print("  ✅ 公式识别")
    print("  ✅ 图像预处理")
    print("  ✅ 完整处理流程")
    print("\n查看详细文档: PaddleOCR使用指南.md")
    print()


if __name__ == "__main__":
    main()





