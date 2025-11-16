#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   pdf_extractor.py
@Time    :   2025/11/16
@Desc    :   使用 PaddleOCR 提取 PDF 内容（支持扫描PDF）
'''

import os
from pathlib import Path
from typing import List, Dict, Optional
import fitz  # pymupdf
from paddleocr import PaddleOCR
from PIL import Image
import io


class PaddleOCRPDFExtractor:
    """
    使用 PaddleOCR 提取 PDF 内容
    特别适合处理扫描PDF和图片型PDF
    """
    
    def __init__(self, use_angle_cls=True, lang='ch'):
        """
        初始化 PaddleOCR
        
        Args:
            use_angle_cls: 是否使用角度分类（处理旋转文字）
            lang: 语言，'ch' 中文, 'en' 英文, 或 'ch,en' 中英文混合
        """
        # 初始化PaddleOCR
        # use_angle_cls=True 可以识别旋转的文字
        # lang='ch' 支持中文，可以改为 'en' 或 'ch,en'
        self.ocr = PaddleOCR(
            use_angle_cls=use_angle_cls,
            lang=lang,
            show_log=False,  # 不显示日志
            use_gpu=True if self._check_gpu() else False
        )
        print(f"PaddleOCR 初始化完成 (语言: {lang}, GPU: {self.ocr.use_gpu})")
    
    def _check_gpu(self):
        """检查是否有可用的GPU"""
        import paddle
        return paddle.device.is_compiled_with_cuda()
    
    def extract_from_pdf(self, pdf_path: str, use_ocr_threshold: float = 0.5) -> Dict:
        """
        从PDF提取文本
        
        Args:
            pdf_path: PDF文件路径
            use_ocr_threshold: 决定是否使用OCR的阈值
                             如果pymupdf提取的文字少于总面积的这个比例，则使用OCR
        
        Returns:
            {
                'text': 完整文本,
                'pages': [每页的详细信息],
                'metadata': 元数据
            }
        """
        result = {
            'text': '',
            'pages': [],
            'metadata': {},
            'source': pdf_path
        }
        
        doc = fitz.open(pdf_path)
        result['metadata'] = {
            'page_count': len(doc),
            'title': doc.metadata.get('title', ''),
            'author': doc.metadata.get('author', ''),
        }
        
        for page_num in range(len(doc)):
            page = doc[page_num]
            
            # 先尝试直接提取文字
            text_from_pymupdf = page.get_text()
            
            # 判断是否需要OCR
            # 如果提取的文字很少，可能是扫描PDF，使用OCR
            needs_ocr = len(text_from_pymupdf.strip()) < 50
            
            if needs_ocr:
                # 使用OCR提取
                text = self._ocr_page(page, page_num)
                method = 'OCR'
            else:
                # 使用pymupdf提取的文字
                text = text_from_pymupdf
                method = 'PyMuPDF'
            
            page_info = {
                'page_number': page_num + 1,
                'text': text,
                'extraction_method': method
            }
            
            result['pages'].append(page_info)
            result['text'] += f"\n\n=== 第 {page_num + 1} 页 ===\n{text}"
        
        doc.close()
        
        return result
    
    def _ocr_page(self, page, page_num: int) -> str:
        """
        对单个PDF页面进行OCR
        
        Args:
            page: PyMuPDF page对象
            page_num: 页码
        
        Returns:
            提取的文本
        """
        # 将PDF页面转为图片
        # zoom=2 提高分辨率，提升OCR准确度
        zoom = 2
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)
        
        # 转换为PIL Image
        img_data = pix.tobytes("png")
        img = Image.open(io.BytesIO(img_data))
        
        # 使用PaddleOCR识别
        result = self.ocr.ocr(img_data, cls=True)
        
        # 提取文字
        if result and result[0]:
            texts = [line[1][0] for line in result[0] if line[1][0]]
            return '\n'.join(texts)
        else:
            return ""
    
    def extract_from_image(self, image_path: str) -> str:
        """
        从图片提取文字
        
        Args:
            image_path: 图片路径
        
        Returns:
            提取的文本
        """
        result = self.ocr.ocr(image_path, cls=True)
        
        if result and result[0]:
            texts = [line[1][0] for line in result[0] if line[1][0]]
            return '\n'.join(texts)
        else:
            return ""
    
    def batch_extract(self, pdf_files: List[str], output_dir: Optional[str] = None) -> List[Dict]:
        """
        批量提取PDF
        
        Args:
            pdf_files: PDF文件路径列表
            output_dir: 输出目录（可选），如果提供则保存为txt
        
        Returns:
            提取结果列表
        """
        results = []
        
        for pdf_file in pdf_files:
            print(f"处理: {pdf_file}")
            result = self.extract_from_pdf(pdf_file)
            results.append(result)
            
            # 保存到文件
            if output_dir:
                os.makedirs(output_dir, exist_ok=True)
                output_file = Path(output_dir) / f"{Path(pdf_file).stem}.txt"
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(result['text'])
                print(f"保存到: {output_file}")
        
        return results


def test_extractor():
    """测试函数"""
    # 初始化提取器
    extractor = PaddleOCRPDFExtractor(lang='ch')
    
    # 测试单个PDF
    pdf_path = "../data/test.pdf"  # 替换为你的PDF路径
    if os.path.exists(pdf_path):
        result = extractor.extract_from_pdf(pdf_path)
        
        print(f"\n文档信息:")
        print(f"  页数: {result['metadata']['page_count']}")
        print(f"  标题: {result['metadata']['title']}")
        
        print(f"\n提取的文本预览:")
        print(result['text'][:500])  # 显示前500字符
        
        # 显示每页的提取方法
        print(f"\n提取方法统计:")
        for page_info in result['pages']:
            print(f"  第{page_info['page_number']}页: {page_info['extraction_method']}")
    else:
        print(f"文件不存在: {pdf_path}")


if __name__ == "__main__":
    test_extractor()
