#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   advanced_document_processor.py
@Time    :   2025/11/16
@Desc    :   高级文档处理：OCR、表格提取、版本对比
'''

import os
import re
from typing import Dict, List, Tuple, Optional
import fitz  # PyMuPDF
from PIL import Image
import io


class AdvancedTableExtractor:
    """高级表格提取器"""
    
    def __init__(self):
        self.extracted_tables = []
    
    def extract_from_pdf(self, file_path: str) -> List[Dict]:
        """
        从PDF中提取表格
        Args:
            file_path: PDF文件路径
        Returns:
            提取的表格列表
        """
        tables = []
        
        try:
            # 优先尝试pdfplumber
            tables = self._extract_with_pdfplumber(file_path)
        except ImportError:
            print("  ⚠️  pdfplumber未安装，使用基础表格检测")
            tables = self._extract_with_pymupdf(file_path)
        except Exception as e:
            print(f"  ⚠️  pdfplumber提取失败: {e}，使用基础方法")
            tables = self._extract_with_pymupdf(file_path)
        
        self.extracted_tables = tables
        return tables
    
    def _extract_with_pdfplumber(self, file_path: str) -> List[Dict]:
        """使用pdfplumber提取表格（推荐）"""
        import pdfplumber
        
        tables = []
        with pdfplumber.open(file_path) as pdf:
            for page_num, page in enumerate(pdf.pages):
                page_tables = page.extract_tables()
                
                for table_idx, table in enumerate(page_tables):
                    if table and len(table) > 0:
                        # 转换为Markdown格式
                        markdown_table = self._convert_to_markdown(table)
                        
                        tables.append({
                            'page': page_num + 1,
                            'table_index': table_idx + 1,
                            'raw_data': table,
                            'markdown': markdown_table,
                            'row_count': len(table),
                            'col_count': len(table[0]) if table else 0
                        })
        
        return tables
    
    def _extract_with_pymupdf(self, file_path: str) -> List[Dict]:
        """使用PyMuPDF基础表格检测（备选方案）"""
        tables = []
        doc = fitz.open(file_path)
        
        for page_num, page in enumerate(doc):
            # 提取文本
            text = page.get_text("text")
            
            # 检测表格
            page_tables = self._detect_tables_in_text(text)
            
            for table_idx, table in enumerate(page_tables):
                tables.append({
                    'page': page_num + 1,
                    'table_index': table_idx + 1,
                    'raw_data': table,
                    'markdown': table,  # 已经是markdown格式
                    'row_count': len(table.split('\n')),
                    'col_count': 0
                })
        
        doc.close()
        return tables
    
    def _detect_tables_in_text(self, text: str) -> List[str]:
        """在文本中检测表格"""
        lines = text.split('\n')
        tables = []
        current_table = []
        in_table = False
        
        for line in lines:
            # 检测表格行特征：多个连续空格或制表符
            if re.search(r'\s{2,}|\t', line) and len(line.split()) >= 2:
                current_table.append(line)
                in_table = True
            elif in_table:
                # 表格结束
                if len(current_table) >= 3:  # 至少3行
                    table_text = self._format_table_text(current_table)
                    tables.append(table_text)
                current_table = []
                in_table = False
        
        # 处理最后一个表格
        if len(current_table) >= 3:
            table_text = self._format_table_text(current_table)
            tables.append(table_text)
        
        return tables
    
    def _format_table_text(self, table_lines: List[str]) -> str:
        """格式化表格文本为Markdown"""
        if not table_lines:
            return ""
        
        # 简单格式化
        formatted = ["[表格数据]"]
        for line in table_lines:
            formatted.append(line.strip())
        
        return '\n'.join(formatted)
    
    def _convert_to_markdown(self, table_data: List[List]) -> str:
        """
        将表格数据转换为Markdown格式
        Args:
            table_data: 二维列表
        Returns:
            Markdown格式的表格
        """
        if not table_data or len(table_data) == 0:
            return ""
        
        markdown_lines = []
        
        # 处理表头
        header = table_data[0]
        header_line = "| " + " | ".join(str(cell) if cell else "" for cell in header) + " |"
        markdown_lines.append(header_line)
        
        # 分隔线
        separator = "|" + "|".join(["---" for _ in header]) + "|"
        markdown_lines.append(separator)
        
        # 表格内容
        for row in table_data[1:]:
            # 确保行长度与表头一致
            padded_row = row + [''] * (len(header) - len(row))
            row_line = "| " + " | ".join(str(cell) if cell else "" for cell in padded_row[:len(header)]) + " |"
            markdown_lines.append(row_line)
        
        return '\n'.join(markdown_lines)
    
    def get_tables_summary(self) -> str:
        """获取提取的表格摘要"""
        if not self.extracted_tables:
            return "未检测到表格"
        
        summary = f"共检测到 {len(self.extracted_tables)} 个表格：\n"
        for table in self.extracted_tables:
            summary += f"  - 第{table['page']}页，表格{table['table_index']}：{table['row_count']}行\n"
        
        return summary


class OCRProcessor:
    """OCR处理器（处理扫描PDF）"""
    
    def __init__(self, use_paddleocr: bool = True):
        """
        初始化OCR处理器
        Args:
            use_paddleocr: 是否优先使用PaddleOCR（推荐，中文识别效果更好）
        """
        self.use_paddleocr = use_paddleocr
        self.ocr_engine = None
        self.ocr_available = self._check_ocr_availability()
    
    def _check_ocr_availability(self) -> bool:
        """检查OCR工具是否可用"""
        if self.use_paddleocr:
            try:
                from paddleocr import PaddleOCR
                # 初始化PaddleOCR（中英文混合识别）
                self.ocr_engine = PaddleOCR(
                    use_angle_cls=True,  # 使用角度分类器
                    lang='ch',           # 中文模型（同时支持英文）
                    use_gpu=False,       # 使用CPU（如果有GPU可设为True）
                    show_log=False       # 不显示日志
                )
                print("✅ PaddleOCR初始化成功")
                return True
            except ImportError:
                print("⚠️  PaddleOCR未安装，尝试使用Tesseract...")
                return self._check_tesseract()
            except Exception as e:
                print(f"⚠️  PaddleOCR初始化失败: {e}")
                return self._check_tesseract()
        else:
            return self._check_tesseract()
    
    def _check_tesseract(self) -> bool:
        """检查Tesseract是否可用（备选方案）"""
        try:
            import pytesseract
            from pdf2image import convert_from_path
            pytesseract.get_tesseract_version()
            self.ocr_engine = "tesseract"
            print("✅ Tesseract可用")
            return True
        except:
            print("❌ OCR工具不可用（PaddleOCR和Tesseract都未安装）")
            return False
    
    def is_scanned_pdf(self, file_path: str, sample_pages: int = 3) -> bool:
        """
        判断PDF是否为扫描版
        Args:
            file_path: PDF文件路径
            sample_pages: 抽样检查的页数
        Returns:
            是否为扫描PDF
        """
        try:
            doc = fitz.open(file_path)
            total_pages = len(doc)
            
            # 抽样检查前几页
            check_pages = min(sample_pages, total_pages)
            text_length = 0
            
            for page_num in range(check_pages):
                text = doc[page_num].get_text("text")
                text_length += len(text.strip())
            
            doc.close()
            
            # 如果平均每页文本少于100字符，很可能是扫描版
            avg_text_per_page = text_length / check_pages
            return avg_text_per_page < 100
            
        except Exception as e:
            print(f"  ⚠️  检测PDF类型失败: {e}")
            return False
    
    def ocr_pdf(self, file_path: str, lang: str = 'ch') -> str:
        """
        OCR处理PDF
        Args:
            file_path: PDF文件路径
            lang: OCR语言（PaddleOCR: 'ch'中文, 'en'英文；Tesseract: 'chi_sim+eng'）
        Returns:
            提取的文本
        """
        if not self.ocr_available:
            return self._fallback_ocr_message(file_path)
        
        # 优先使用PaddleOCR
        if isinstance(self.ocr_engine, object) and hasattr(self.ocr_engine, 'ocr'):
            return self._ocr_with_paddleocr(file_path)
        else:
            return self._ocr_with_tesseract(file_path, lang)
    
    def _ocr_with_paddleocr(self, file_path: str) -> str:
        """使用PaddleOCR处理PDF"""
        try:
            import fitz  # PyMuPDF
            from PIL import Image
            import io
            
            print(f"  🔍 使用PaddleOCR处理: {os.path.basename(file_path)}")
            
            doc = fitz.open(file_path)
            full_text = []
            
            for page_num in range(len(doc)):
                print(f"    处理第 {page_num+1}/{len(doc)} 页...")
                
                page = doc[page_num]
                
                # 将PDF页面转换为图片
                pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # 提高分辨率
                img_data = pix.tobytes("png")
                image = Image.open(io.BytesIO(img_data))
                
                # 转换为numpy数组（PaddleOCR需要）
                import numpy as np
                img_array = np.array(image)
                
                # OCR识别
                result = self.ocr_engine.ocr(img_array, cls=True)
                
                # 提取文本
                page_text = []
                page_text.append(f"\n{'='*50}\n[第 {page_num+1} 页 - PaddleOCR提取]\n{'='*50}\n")
                
                if result and result[0]:
                    for line in result[0]:
                        if line and len(line) >= 2:
                            text = line[1][0]  # 提取识别的文本
                            confidence = line[1][1]  # 置信度
                            if confidence > 0.5:  # 只保留置信度>0.5的结果
                                page_text.append(text)
                
                full_text.extend(page_text)
            
            doc.close()
            print(f"  ✅ PaddleOCR完成，共处理 {len(doc)} 页")
            return '\n'.join(full_text)
            
        except Exception as e:
            print(f"  ❌ PaddleOCR处理失败: {e}")
            import traceback
            traceback.print_exc()
            return self._fallback_ocr_message(file_path)
    
    def _ocr_with_tesseract(self, file_path: str, lang: str = 'chi_sim+eng') -> str:
        """使用Tesseract处理PDF（备选方案）"""
        try:
            import pytesseract
            from pdf2image import convert_from_path
            
            print(f"  🔍 使用Tesseract处理: {os.path.basename(file_path)}")
            
            # 转换PDF为图片
            images = convert_from_path(file_path, dpi=300)
            
            full_text = []
            for i, image in enumerate(images):
                print(f"    处理第 {i+1}/{len(images)} 页...")
                
                # OCR识别
                text = pytesseract.image_to_string(image, lang=lang)
                
                full_text.append(f"\n{'='*50}\n[第 {i+1} 页 - Tesseract提取]\n{'='*50}\n")
                full_text.append(text)
            
            print(f"  ✅ Tesseract完成，共处理 {len(images)} 页")
            return '\n'.join(full_text)
            
        except Exception as e:
            print(f"  ❌ Tesseract处理失败: {e}")
            return self._fallback_ocr_message(file_path)
    
    def _fallback_ocr_message(self, file_path: str) -> str:
        """OCR不可用时的后备消息"""
        return f"""
[OCR处理失败或不可用]

文件: {os.path.basename(file_path)}

提示：此PDF可能是扫描版，需要OCR处理。

推荐方案（PaddleOCR - 中文识别效果好）：
  pip install paddleocr paddlepaddle

备选方案（Tesseract）：
  pip install pytesseract pdf2image
  sudo apt-get install tesseract-ocr tesseract-ocr-chi-sim

或手动处理此文档。
"""
    
    def smart_extract(self, file_path: str) -> Tuple[str, bool]:
        """
        智能提取：自动判断是否需要OCR
        Args:
            file_path: PDF文件路径
        Returns:
            (提取的文本, 是否使用了OCR)
        """
        # 先尝试正常提取
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text("text")
        doc.close()
        
        # 判断是否需要OCR
        if len(text.strip()) < 100:
            print(f"  ⚠️  检测到扫描PDF，尝试OCR...")
            if self.ocr_available:
                ocr_text = self.ocr_pdf(file_path)
                return ocr_text, True
            else:
                return self._fallback_ocr_message(file_path), False
        
        return text, False


class VersionComparator:
    """版本对比器"""
    
    def __init__(self):
        self.comparison_result = None
    
    def compare_documents(self, doc1_text: str, doc2_text: str,
                         doc1_name: str = "版本1", 
                         doc2_name: str = "版本2") -> Dict:
        """
        对比两个文档版本
        Args:
            doc1_text: 文档1文本
            doc2_text: 文档2文本
            doc1_name: 文档1名称
            doc2_name: 文档2名称
        Returns:
            对比结果字典
        """
        import difflib
        
        # 按行分割
        lines1 = doc1_text.splitlines()
        lines2 = doc2_text.splitlines()
        
        # 使用difflib进行对比
        differ = difflib.Differ()
        diff = list(differ.compare(lines1, lines2))
        
        # 分类差异
        added = []
        removed = []
        modified = []
        
        for line in diff:
            if line.startswith('+ '):
                added.append(line[2:])
            elif line.startswith('- '):
                removed.append(line[2:])
            elif line.startswith('? '):
                # 修改标记
                continue
        
        # 统计信息
        self.comparison_result = {
            'doc1_name': doc1_name,
            'doc2_name': doc2_name,
            'doc1_lines': len(lines1),
            'doc2_lines': len(lines2),
            'added_lines': len(added),
            'removed_lines': len(removed),
            'added_content': added[:20],  # 只保留前20条
            'removed_content': removed[:20],
            'similarity_ratio': self._calculate_similarity(lines1, lines2)
        }
        
        return self.comparison_result
    
    def _calculate_similarity(self, lines1: List[str], lines2: List[str]) -> float:
        """计算相似度"""
        import difflib
        matcher = difflib.SequenceMatcher(None, lines1, lines2)
        return matcher.ratio()
    
    def extract_version_info(self, text: str) -> Dict:
        """
        从文本中提取版本信息
        Args:
            text: 文档文本
        Returns:
            版本信息字典
        """
        version_info = {
            'version_number': None,
            'baseline': None,
            'date': None,
            'identifiers': []
        }
        
        # 提取版本号模式
        version_patterns = [
            r'[Vv]ersion\s*[\.:：]?\s*([0-9\.]+)',
            r'[Vv](\d+\.\d+\.\d+)',
            r'Baseline\s*(\d+)',
            r'v(\d+\.\d+)',
        ]
        
        for pattern in version_patterns:
            match = re.search(pattern, text[:2000])  # 只在前2000字符中查找
            if match:
                version_info['version_number'] = match.group(1)
                break
        
        # 提取Baseline信息（特定于ERTMS等标准）
        baseline_match = re.search(r'Baseline\s*(\d+)', text[:2000])
        if baseline_match:
            version_info['baseline'] = baseline_match.group(1)
        
        # 提取日期
        date_patterns = [
            r'(\d{4}-\d{2}-\d{2})',
            r'(\d{4}/\d{2}/\d{2})',
            r'(\d{2}/\d{2}/\d{4})',
        ]
        
        for pattern in date_patterns:
            match = re.search(pattern, text[:2000])
            if match:
                version_info['date'] = match.group(1)
                break
        
        return version_info
    
    def format_comparison(self, comparison: Dict = None) -> str:
        """
        格式化对比结果为可读文本
        Args:
            comparison: 对比结果（如果为None，使用最后一次对比结果）
        Returns:
            格式化的对比文本
        """
        if comparison is None:
            comparison = self.comparison_result
        
        if not comparison:
            return "无对比结果"
        
        formatted = f"""
╔══════════════════════════════════════════════════════╗
║                   版本对比结果                        ║
╚══════════════════════════════════════════════════════╝

【版本信息】
  {comparison['doc1_name']}: {comparison['doc1_lines']} 行
  {comparison['doc2_name']}: {comparison['doc2_lines']} 行
  相似度: {comparison['similarity_ratio']:.1%}

【变更统计】
  ✅ 新增: {comparison['added_lines']} 行
  ❌ 删除: {comparison['removed_lines']} 行
  📝 总变更: {comparison['added_lines'] + comparison['removed_lines']} 行

【新增内容】（前10条）
"""
        for i, line in enumerate(comparison['added_content'][:10], 1):
            formatted += f"  {i}. {line[:100]}...\n" if len(line) > 100 else f"  {i}. {line}\n"
        
        formatted += "\n【删除内容】（前10条）\n"
        for i, line in enumerate(comparison['removed_content'][:10], 1):
            formatted += f"  {i}. {line[:100]}...\n" if len(line) > 100 else f"  {i}. {line}\n"
        
        formatted += "\n╚══════════════════════════════════════════════════════╝"
        
        return formatted
    
    def generate_evolution_summary(self, comparison: Dict, query: str = "") -> str:
        """
        生成演变分析摘要
        Args:
            comparison: 对比结果
            query: 用户问题（可选）
        Returns:
            演变分析文本
        """
        summary = f"""
=== 演变分析摘要 ===

【版本对比】
从 {comparison['doc1_name']} 到 {comparison['doc2_name']}

【主要变化】
- 内容增长: {comparison['doc2_lines'] - comparison['doc1_lines']} 行
- 新增内容: {comparison['added_lines']} 处
- 删除内容: {comparison['removed_lines']} 处
- 整体变化率: {(1 - comparison['similarity_ratio']) * 100:.1f}%

【关键演变点】
"""
        # 分析关键变化
        if comparison['added_lines'] > comparison['removed_lines']:
            summary += f"- 主要为内容扩充，新增了 {comparison['added_lines'] - comparison['removed_lines']} 处净增内容\n"
        elif comparison['removed_lines'] > comparison['added_lines']:
            summary += f"- 主要为内容精简，删除了 {comparison['removed_lines'] - comparison['added_lines']} 处冗余内容\n"
        else:
            summary += "- 主要为内容替换和更新\n"
        
        if query:
            summary += f"\n【针对问题】{query}\n"
        
        return summary


if __name__ == "__main__":
    # 测试表格提取
    print("=== 测试表格提取 ===")
    table_extractor = AdvancedTableExtractor()
    
    # 测试OCR
    print("\n=== 测试OCR处理器 ===")
    ocr_processor = OCRProcessor()
    print(f"OCR可用性: {ocr_processor.ocr_available}")
    
    # 测试版本对比
    print("\n=== 测试版本对比 ===")
    comparator = VersionComparator()
    doc1 = "第一版内容\n包含一些数据\n定义了概念A"
    doc2 = "第二版内容\n包含更多数据\n定义了概念A和概念B\n新增功能"
    result = comparator.compare_documents(doc1, doc2)
    print(comparator.format_comparison(result))