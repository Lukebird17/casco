import os
import subprocess
import tempfile
import shutil
from typing import List, Dict, Optional, Tuple
from pathlib import Path

from config import DATA_DIR, LIBREOFFICE_PATH
from enhanced_ocr import EnhancedOCRProcessor, MINERU_AVAILABLE


class DocumentLoader:
    def __init__(
        self,
        data_dir: str = DATA_DIR,
    ):
        self.data_dir = data_dir
        self.supported_formats = [".pdf", ".pptx", ".docx", ".txt", ".md"]
        
        # 初始化MinerU处理器
        if MINERU_AVAILABLE:
            self.ocr_processor = EnhancedOCRProcessor()
            print("✅ MinerU已启用，将用于处理PDF")
        else:
            self.ocr_processor = None
            print("⚠️  MinerU不可用，将使用基础解析器")
    
    def check_libreoffice(self) -> bool:
        """检查LibreOffice是否可用"""
        try:
            # 优先使用配置的路径
            if os.path.exists(LIBREOFFICE_PATH):
                result = subprocess.run(
                    [LIBREOFFICE_PATH, '--version'],
                    capture_output=True,
                    timeout=5
                )
                if result.returncode == 0:
                    print(f"   ✅ 使用配置的LibreOffice: {LIBREOFFICE_PATH}")
                    return True
            
            # 回退到系统PATH中的libreoffice
            result = subprocess.run(
                ['libreoffice', '--version'],
                capture_output=True,
                timeout=5
            )
            if result.returncode == 0:
                print(f"   ✅ 使用系统LibreOffice")
                return True
            return False
        except:
            return False
    
    def convert_to_pdf(self, file_path: str) -> Optional[str]:
        """
        使用LibreOffice将PPTX/DOCX转换为PDF（如果可用）
        
        Returns:
            转换后的PDF文件路径，如果失败或LibreOffice不可用则返回None
        """
        # 检查LibreOffice是否可用
        if not self.check_libreoffice():
            print(f"   ℹ️  LibreOffice不可用，将使用基础解析器")
            return None
        
        try:
            # 创建临时目录
            temp_dir = tempfile.mkdtemp()
            
            # 确定使用哪个LibreOffice
            libreoffice_cmd = LIBREOFFICE_PATH if os.path.exists(LIBREOFFICE_PATH) else 'libreoffice'
            
            # 使用LibreOffice转换
            cmd = [
                libreoffice_cmd,
                '--headless',
                '--convert-to', 'pdf',
                '--outdir', temp_dir,
                file_path
            ]
            
            print(f"   🔄 使用LibreOffice转换为PDF: {os.path.basename(file_path)}")
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=60  # 60秒超时
            )
            
            if result.returncode == 0:
                # 查找生成的PDF文件
                pdf_filename = os.path.splitext(os.path.basename(file_path))[0] + '.pdf'
                pdf_path = os.path.join(temp_dir, pdf_filename)
                
                if os.path.exists(pdf_path):
                    print(f"   ✅ 转换成功: {pdf_filename}")
                    return pdf_path
                else:
                    print(f"   ⚠️  未找到转换后的PDF文件")
                    return None
            else:
                print(f"   ⚠️  LibreOffice转换失败，使用基础解析器")
                return None
                
        except subprocess.TimeoutExpired:
            print(f"   ⚠️  转换超时，使用基础解析器")
            return None
        except Exception as e:
            print(f"   ⚠️  转换错误: {e}，使用基础解析器")
            return None

    def load_pdf(self, file_path: str) -> Tuple[List[Dict], List[Dict]]:
        """加载PDF文件，返回文本内容和图片信息（优先使用MinerU）

        要求：
        1. 优先使用MinerU处理PDF文件
        2. 提取文本内容并格式化，保留页码信息
        3. 提取图片信息
        
        Returns:
            (pages, images): 页面文本列表和图片信息列表
            pages格式: [{"text": str, "page_number": int, "section": str}, ...]
        """
        pages = []
        images = []
        
        # 优先使用MinerU
        if self.ocr_processor:
            try:
                # 直接调用 process_file 获取完整结果（包括文本和图片）
                full_result = self.ocr_processor.process_file(file_path)
                
                if full_result and full_result.get('content'):
                    # 提取文本内容
                    markdown_content = full_result['content']
                    
                    # 尝试按页分割内容（MinerU可能在markdown中包含页码标记）
                    # 如果没有明确的页码标记，我们按段落分割并估计页码
                    lines = markdown_content.split('\n')
                    current_page = 1
                    current_section = ""
                    current_text = []
                    
                    for line in lines:
                        # 检测是否是新的章节/标题（通常是新页的开始）
                        if line.strip().startswith('#'):
                            # 如果有累积的文本，保存为一个段落
                            if current_text:
                                pages.append({
                                    "text": '\n'.join(current_text),
                                    "page_number": current_page,
                                    "section": current_section
                                })
                                current_text = []
                                current_page += 1
                            
                            # 更新当前章节
                            current_section = line.strip().replace('#', '').strip()
                            current_text.append(line)
                        else:
                            current_text.append(line)
                            
                            # 每500字符估算为一页（可调整）
                            if len('\n'.join(current_text)) > 500 and line.strip() == '':
                                pages.append({
                                    "text": '\n'.join(current_text),
                                    "page_number": current_page,
                                    "section": current_section
                                })
                                current_text = []
                                current_page += 1
                    
                    # 保存最后剩余的文本
                    if current_text:
                        pages.append({
                            "text": '\n'.join(current_text),
                            "page_number": current_page,
                            "section": current_section
                        })
                    
                    # 如果分割失败，至少保存整个文档
                    if not pages:
                        pages.append({
                            "text": markdown_content,
                            "page_number": 1,
                            "section": "全文"
                        })
                    
                    # 提取图片信息
                    if 'images' in full_result and full_result['images']:
                        images = full_result['images']
                        print(f"   📸 提取到 {len(images)} 张图片")
                    
                    print(f"   📄 分割为 {len(pages)} 个段落")
                    return pages, images
            except Exception as e:
                print(f"⚠️  MinerU处理失败，尝试基础解析器: {e}")
        
        # 如果MinerU不可用或失败，使用基础解析器（需要手动安装PyPDF2）
        try:
            from PyPDF2 import PdfReader
            reader = PdfReader(file_path)
            for page_num, page in enumerate(reader.pages, 1):
                text = page.extract_text()
                if text.strip():
                    pages.append({
                        "text": f"--- 第 {page_num} 页 ---\n{text}\n",
                        "page_number": page_num,
                        "section": f"第 {page_num} 页"
                    })
        except Exception as e:
            print(f"❌ 加载PDF文件失败 {file_path}: {e}")
        
        return pages, images

    def load_pptx(self, file_path: str) -> List[Dict]:
        """加载PPTX文件

        策略（优先级从高到低）：
        1. 如果LibreOffice可用：转换为PDF → 用MinerU处理（OCR + 图片）
        2. 如果LibreOffice不可用或转换失败：使用python-pptx提取文本（仅文本）
        
        注意：python-pptx只能提取文本，无法处理图片和复杂布局
        """
        slides = []
        pdf_path = None
        
        # 策略1: 转换为PDF并用MinerU处理
        if self.ocr_processor:
            try:
                pdf_path = self.convert_to_pdf(file_path)
                if pdf_path:
                    # 用MinerU处理转换后的PDF
                    pages, images = self.load_pdf(pdf_path)
                    # 清理临时PDF
                    if os.path.exists(pdf_path):
                        temp_dir = os.path.dirname(pdf_path)
                        shutil.rmtree(temp_dir, ignore_errors=True)
                    
                    if pages:
                        return pages
            except Exception as e:
                print(f"⚠️  PDF转换+MinerU处理失败: {e}")
                # 清理临时文件
                if pdf_path and os.path.exists(pdf_path):
                    temp_dir = os.path.dirname(pdf_path)
                    shutil.rmtree(temp_dir, ignore_errors=True)
        
        # 策略2: 使用python-pptx基础解析器
        try:
            from pptx import Presentation
            prs = Presentation(file_path)
            for slide_num, slide in enumerate(prs.slides, 1):
                text_parts = []
                
                # 提取幻灯片中所有文本框的内容
                for shape in slide.shapes:
                    if hasattr(shape, "text"):
                        text_parts.append(shape.text)
                
                # 合并所有文本
                slide_text = "\n".join(text_parts)
                
                if slide_text.strip():
                    formatted_text = f"--- 幻灯片 {slide_num} ---\n{slide_text}\n"
                    slides.append({"text": formatted_text})
        except Exception as e:
            print(f"❌ 加载PPTX文件失败 {file_path}: {e}")
        
        return slides

    def load_docx(self, file_path: str) -> str:
        """加载DOCX文件
        
        策略（优先级从高到低）：
        1. 如果LibreOffice可用：转换为PDF → 用MinerU处理（OCR + 图片）
        2. 如果LibreOffice不可用或转换失败：使用docx2txt提取文本（仅文本）
        
        注意：docx2txt只能提取文本，无法处理图片和复杂布局
        """
        pdf_path = None
        
        # 策略1: 转换为PDF并用MinerU处理
        if self.ocr_processor:
            try:
                pdf_path = self.convert_to_pdf(file_path)
                if pdf_path:
                    # 用MinerU处理转换后的PDF
                    pages, images = self.load_pdf(pdf_path)
                    # 清理临时PDF
                    if os.path.exists(pdf_path):
                        temp_dir = os.path.dirname(pdf_path)
                        shutil.rmtree(temp_dir, ignore_errors=True)
                    
                    if pages:
                        # 合并所有页面的文本
                        return "\n".join([p["text"] for p in pages])
            except Exception as e:
                print(f"⚠️  PDF转换+MinerU处理失败: {e}")
                # 清理临时文件
                if pdf_path and os.path.exists(pdf_path):
                    temp_dir = os.path.dirname(pdf_path)
                    shutil.rmtree(temp_dir, ignore_errors=True)
        
        # 策略2: 使用docx2txt基础解析器
        try:
            import docx2txt
            text = docx2txt.process(file_path)
            return text if text else ""
        except Exception as e:
            print(f"❌ 加载DOCX文件失败 {file_path}: {e}")
            return ""

    def load_txt(self, file_path: str) -> str:
        """加载TXT文件
        要求：
        1. 使用open读取TXT文件（注意使用encoding="utf-8"）
        2. 返回文本内容
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"加载TXT文件失败 {file_path}: {e}")
            return ""
    
    def load_md(self, file_path: str) -> str:
        """加载Markdown文件
        要求：
        1. 使用open读取MD文件（注意使用encoding="utf-8"）
        2. 返回文本内容
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"加载Markdown文件失败 {file_path}: {e}")
            return ""

    def load_document(self, file_path: str) -> Tuple[List[Dict[str, str]], List[Dict]]:
        """加载单个文档，PDF和PPT按页/幻灯片分割，返回文档块列表和图片列表
        
        Returns:
            (documents, images): 文档块列表和图片信息列表
        """
        ext = os.path.splitext(file_path)[1].lower()
        filename = os.path.basename(file_path)
        documents = []
        images = []

        if ext == ".pdf":
            pages, images = self.load_pdf(file_path)
            for page_idx, page_data in enumerate(pages, 1):
                documents.append(
                    {
                        "content": page_data["text"],
                        "filename": filename,
                        "filepath": file_path,
                        "filetype": ext,
                        "page_number": page_data.get("page_number", page_idx),
                        "section": page_data.get("section", ""),
                    }
                )
        elif ext == ".pptx":
            slides = self.load_pptx(file_path)
            for slide_idx, slide_data in enumerate(slides, 1):
                documents.append(
                    {
                        "content": slide_data["text"],
                        "filename": filename,
                        "filepath": file_path,
                        "filetype": ext,
                        "page_number": slide_data.get("page_number", slide_idx),
                        "section": slide_data.get("section", f"幻灯片 {slide_idx}"),
                    }
                )
        elif ext == ".docx":
            content = self.load_docx(file_path)
            if content:
                documents.append(
                    {
                        "content": content,
                        "filename": filename,
                        "filepath": file_path,
                        "filetype": ext,
                        "page_number": 1,
                        "section": "文档内容",
                    }
                )
        elif ext == ".txt":
            content = self.load_txt(file_path)
            if content:
                documents.append(
                    {
                        "content": content,
                        "filename": filename,
                        "filepath": file_path,
                        "filetype": ext,
                        "page_number": 1,
                        "section": "文本内容",
                    }
                )
        elif ext == ".md":
            content = self.load_md(file_path)
            if content:
                documents.append(
                    {
                        "content": content,
                        "filename": filename,
                        "filepath": file_path,
                        "filetype": ext,
                        "page_number": 1,
                        "section": "Markdown内容",
                    }
                )
        else:
            print(f"不支持的文件格式: {ext}")

        return documents, images

    def load_all_documents(self) -> Tuple[List[Dict[str, str]], List[Dict]]:
        """加载数据目录下的所有文档
        
        Returns:
            (documents, images): 所有文档块列表和所有图片信息列表
        """
        if not os.path.exists(self.data_dir):
            print(f"数据目录不存在: {self.data_dir}")
            return [], []

        documents = []
        all_images = []

        for root, dirs, files in os.walk(self.data_dir):
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext in self.supported_formats:
                    file_path = os.path.join(root, file)
                    print(f"正在加载: {file_path}")
                    doc_chunks, images = self.load_document(file_path)
                    if doc_chunks:
                        documents.extend(doc_chunks)
                    if images:
                        all_images.extend(images)

        return documents, all_images
