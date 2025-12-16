import os
from typing import List, Dict, Optional, Tuple
from pathlib import Path

from config import DATA_DIR
from enhanced_ocr import EnhancedOCRProcessor, MINERU_AVAILABLE


class DocumentLoader:
    def __init__(
        self,
        data_dir: str = DATA_DIR,
    ):
        self.data_dir = data_dir
        self.supported_formats = [".pdf", ".pptx", ".docx", ".txt"]
        
        # 初始化MinerU处理器
        if MINERU_AVAILABLE:
            self.ocr_processor = EnhancedOCRProcessor()
            print("✅ MinerU已启用，将用于处理PDF/PPTX/DOCX")
        else:
            self.ocr_processor = None
            print("⚠️  MinerU不可用，将使用基础解析器")

    def load_pdf(self, file_path: str) -> Tuple[List[Dict], List[Dict]]:
        """加载PDF文件，返回文本内容和图片信息（优先使用MinerU）

        要求：
        1. 优先使用MinerU处理PDF文件
        2. 提取文本内容并格式化
        3. 提取图片信息
        
        Returns:
            (pages, images): 页面文本列表和图片信息列表
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
                    formatted_text = f"--- PDF文档（MinerU处理） ---\n{markdown_content}\n"
                    pages.append({"text": formatted_text})
                    
                    # 提取图片信息
                    if 'images' in full_result and full_result['images']:
                        images = full_result['images']
                        print(f"   📸 提取到 {len(images)} 张图片")
                    
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
                    formatted_text = f"--- 第 {page_num} 页 ---\n{text}\n"
                    pages.append({"text": formatted_text})
        except Exception as e:
            print(f"❌ 加载PDF文件失败 {file_path}: {e}")
        
        return pages, images

    def load_pptx(self, file_path: str) -> List[Dict]:
        """加载PPT文件，按幻灯片返回内容（优先使用MinerU）

        要求：
        1. 优先使用MinerU处理PPT文件
        2. 提取文本内容并格式化
        3. 格式化为"--- 幻灯片 X ---\n文本内容\n"
        4. 返回幻灯片内容列表，每个元素包含 {"text": "..."}
        """
        slides = []
        
        # 优先使用MinerU
        if self.ocr_processor:
            try:
                result = self.ocr_processor.process_pptx(file_path)
                if result:
                    # MinerU返回的是完整的markdown文本
                    formatted_text = f"--- PPTX文档（MinerU处理） ---\n{result}\n"
                    slides.append({"text": formatted_text})
                    return slides
            except Exception as e:
                print(f"⚠️  MinerU处理失败，尝试基础解析器: {e}")
        
        # 如果MinerU不可用或失败，使用基础解析器
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
            print(f"❌ 加载PPT文件失败 {file_path}: {e}")
        
        return slides

    def load_docx(self, file_path: str) -> str:
        """加载DOCX文件（优先使用MinerU）
        要求：
        1. 优先使用MinerU处理DOCX文件
        2. 返回文本内容
        """
        # 优先使用MinerU
        if self.ocr_processor:
            try:
                result = self.ocr_processor.process_docx(file_path)
                if result:
                    return result
            except Exception as e:
                print(f"⚠️  MinerU处理失败，尝试基础解析器: {e}")
        
        # 如果MinerU不可用或失败，使用基础解析器
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
                        "page_number": page_idx,
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
                        "page_number": slide_idx,
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
                        "page_number": 0,
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
                        "page_number": 0,
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
