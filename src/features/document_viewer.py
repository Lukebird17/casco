#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文档查看器
支持 PDF、DOCX 预览和引用跳转
"""

import os
import base64
from pathlib import Path
from typing import Optional, Dict, List
import fitz  # PyMuPDF


class DocumentViewer:
    """文档查看器"""
    
    def __init__(self, data_dir: str = "./data"):
        self.data_dir = Path(data_dir)
        self.current_doc: Optional[str] = None
        self.current_page: int = 1
        
    def render_pdf_page(self, pdf_path: str, page_num: int = 1, 
                       highlight_text: Optional[str] = None) -> str:
        """
        渲染 PDF 页面为 HTML
        
        Args:
            pdf_path: PDF 文件路径
            page_num: 页码（从1开始）
            highlight_text: 要高亮的文本
            
        Returns:
            HTML 字符串
        """
        try:
            # 打开 PDF
            doc = fitz.open(pdf_path)
            total_pages = len(doc)
            
            if page_num < 1 or page_num > total_pages:
                page_num = 1
            
            # 获取页面（PyMuPDF 从0开始）
            page = doc[page_num - 1]
            
            # 转换为图片
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # 2x 缩放提高清晰度
            img_data = pix.tobytes("png")
            img_base64 = base64.b64encode(img_data).decode()
            
            # 如果需要高亮，在页面上标记
            highlight_html = ""
            if highlight_text:
                text_instances = page.search_for(highlight_text)
                if text_instances:
                    highlight_html = f'''
                    <div style="background: #fef3c7; padding: 10px; border-radius: 6px; margin: 10px 0;">
                        🔍 找到 {len(text_instances)} 处匹配: "{highlight_text[:50]}..."
                    </div>
                    '''
            
            # 构建 HTML
            html = f'''
            <div style="font-family: 'Inter', sans-serif; background: #f9fafb; padding: 20px; border-radius: 12px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                    <div style="font-weight: bold; font-size: 16px; color: #374151;">
                        📄 {os.path.basename(pdf_path)}
                    </div>
                    <div style="background: #6366f1; color: white; padding: 6px 12px; border-radius: 20px; font-size: 14px;">
                        第 {page_num} / {total_pages} 页
                    </div>
                </div>
                
                {highlight_html}
                
                <div style="background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                    <img src="data:image/png;base64,{img_base64}" 
                         style="max-width: 100%; height: auto; display: block; margin: 0 auto;">
                </div>
                
                <div style="display: flex; justify-content: center; gap: 10px; margin-top: 15px;">
                    <button onclick="alert('prev')" 
                            style="padding: 8px 20px; background: #6366f1; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 500;">
                        ← 上一页
                    </button>
                    <button onclick="alert('next')" 
                            style="padding: 8px 20px; background: #6366f1; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 500;">
                        下一页 →
                    </button>
                </div>
            </div>
            '''
            
            doc.close()
            return html
            
        except Exception as e:
            return f'''
            <div style="padding: 40px; text-align: center; color: #ef4444;">
                ❌ 无法加载文档: {str(e)}
            </div>
            '''
    
    def jump_to_citation(self, filename: str, page: int, 
                         text_snippet: Optional[str] = None) -> str:
        """
        跳转到引用位置
        
        Args:
            filename: 文件名
            page: 页码
            text_snippet: 文本片段（用于高亮）
            
        Returns:
            渲染的 HTML
        """
        # 在数据目录中查找文件
        pdf_path = self._find_document(filename)
        
        if not pdf_path:
            return f'''
            <div style="padding: 40px; text-align: center; color: #f59e0b;">
                ⚠️ 找不到文档: {filename}
            </div>
            '''
        
        self.current_doc = str(pdf_path)
        self.current_page = page
        
        return self.render_pdf_page(str(pdf_path), page, text_snippet)
    
    def _find_document(self, filename: str) -> Optional[Path]:
        """在数据目录中查找文档"""
        # 直接匹配
        direct_path = self.data_dir / filename
        if direct_path.exists():
            return direct_path
        
        # 递归搜索
        for path in self.data_dir.rglob(filename):
            if path.is_file():
                return path
        
        return None
    
    def get_document_list(self) -> List[Dict]:
        """获取所有文档列表"""
        docs = []
        
        for ext in ['*.pdf', '*.docx', '*.pptx']:
            for path in self.data_dir.rglob(ext):
                if path.is_file():
                    docs.append({
                        "filename": path.name,
                        "path": str(path),
                        "size": path.stat().st_size,
                        "type": path.suffix[1:].upper()
                    })
        
        return sorted(docs, key=lambda x: x['filename'])
    
    def render_document_list(self) -> str:
        """渲染文档列表"""
        docs = self.get_document_list()
        
        if not docs:
            return '''
            <div style="padding: 40px; text-align: center; color: #9ca3af;">
                📭 暂无文档
            </div>
            '''
        
        html = '<div style="padding: 15px; background: #f9fafb; border-radius: 12px;">'
        html += f'<h3 style="color: #6366f1; margin-bottom: 15px;">📚 文档库 ({len(docs)})</h3>'
        
        for doc in docs:
            size_mb = doc['size'] / (1024 * 1024)
            
            html += f'''
            <div style="padding: 12px; margin: 8px 0; background: white; border-left: 4px solid #6366f1; 
                        border-radius: 6px; cursor: pointer; transition: all 0.2s;"
                 onmouseover="this.style.background='#f3f4f6'" 
                 onmouseout="this.style.background='white'">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <div style="font-weight: 600; color: #1f2937; margin-bottom: 4px;">
                            📄 {doc['filename']}
                        </div>
                        <div style="font-size: 12px; color: #6b7280;">
                            {doc['type']} · {size_mb:.2f} MB
                        </div>
                    </div>
                    <button style="padding: 6px 12px; background: #6366f1; color: white; 
                                   border: none; border-radius: 4px; cursor: pointer; font-size: 12px;">
                        打开
                    </button>
                </div>
            </div>
            '''
        
        html += '</div>'
        return html
    
    def extract_text_from_page(self, pdf_path: str, page_num: int) -> str:
        """从页面提取文本"""
        try:
            doc = fitz.open(pdf_path)
            if page_num < 1 or page_num > len(doc):
                return ""
            
            page = doc[page_num - 1]
            text = page.get_text()
            doc.close()
            
            return text
        except:
            return ""





