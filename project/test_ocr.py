#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   test_ocr.py
@Time    :   2025/11/16
@Desc    :   测试 PaddleOCR PDF 提取
'''

from pdf_extractor import PaddleOCRPDFExtractor
import os

def test_single_pdf():
    """测试单个PDF文件"""
    print("="*50)
    print("测试 PaddleOCR PDF 提取")
    print("="*50)
    
    # 初始化提取器
    print("\n1. 初始化 PaddleOCR...")
    extractor = PaddleOCRPDFExtractor(lang='ch')
    
    # 找一个PDF测试
    data_dir = "../data"
    pdf_files = []
    
    # 遍历data目录找PDF
    for root, dirs, files in os.walk(data_dir):
        for file in files:
            if file.endswith('.pdf'):
                pdf_files.append(os.path.join(root, file))
                if len(pdf_files) >= 1:  # 只测试第一个
                    break
        if pdf_files:
            break
    
    if not pdf_files:
        print(f"\n未找到PDF文件在 {data_dir}")
        return
    
    test_pdf = pdf_files[0]
    print(f"\n2. 测试文件: {test_pdf}")
    
    # 提取
    print("\n3. 开始提取...")
    result = extractor.extract_from_pdf(test_pdf)
    
    # 显示结果
    print(f"\n4. 提取结果:")
    print(f"   总页数: {result['metadata']['page_count']}")
    print(f"   文本长度: {len(result['text'])} 字符")
    
    print(f"\n5. 每页提取方法:")
    for page_info in result['pages']:
        print(f"   第{page_info['page_number']}页: {page_info['extraction_method']}")
    
    print(f"\n6. 文本预览 (前500字符):")
    print("-"*50)
    print(result['text'][:500])
    print("-"*50)
    
    # 保存结果
    output_file = "test_ocr_output.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result['text'])
    print(f"\n7. 完整文本已保存到: {output_file}")


def compare_methods():
    """对比PyMuPDF和OCR的效果"""
    print("\n" + "="*50)
    print("对比 PyMuPDF vs PaddleOCR")
    print("="*50)
    
    import fitz
    from pdf_extractor import PaddleOCRPDFExtractor
    
    # 找测试PDF
    data_dir = "../data"
    for root, dirs, files in os.walk(data_dir):
        for file in files:
            if file.endswith('.pdf'):
                test_pdf = os.path.join(root, file)
                
                print(f"\n测试文件: {test_pdf}")
                
                # PyMuPDF提取
                doc = fitz.open(test_pdf)
                pymupdf_text = ""
                for page in doc:
                    pymupdf_text += page.get_text()
                doc.close()
                
                # PaddleOCR提取
                extractor = PaddleOCRPDFExtractor(lang='ch')
                ocr_result = extractor.extract_from_pdf(test_pdf)
                
                print(f"\nPyMuPDF 提取:")
                print(f"  文本长度: {len(pymupdf_text)} 字符")
                print(f"  预览: {pymupdf_text[:200]}")
                
                print(f"\nPaddleOCR 提取:")
                print(f"  文本长度: {len(ocr_result['text'])} 字符")
                print(f"  预览: {ocr_result['text'][:200]}")
                
                return  # 只测试一个文件


if __name__ == "__main__":
    # 测试单个PDF
    test_single_pdf()
    
    # 对比两种方法（可选）
    # compare_methods()
