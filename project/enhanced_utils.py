#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   enhanced_utils.py
@Time    :   2025/11/15
@Desc    :   增强的文档处理工具，支持表格提取和结构化信息保留
'''

import os
import re
from typing import Dict, List, Tuple
import json
from tqdm import tqdm
import tiktoken
import fitz  # PyMuPDF
from PIL import Image
import io

enc = tiktoken.get_encoding("cl100k_base")


class EnhancedReadFiles:
    """
    增强的文件读取类，支持表格提取和元数据保留
    """
    
    # 类级别的OCR系统实例（全局共享，只初始化一次）
    _ocr_system = None

    def __init__(self, path: str) -> None:
        self._path = path
        self.file_list = self.get_files()
        
        # 如果OCR系统还没初始化，则初始化一次
        if EnhancedReadFiles._ocr_system is None:
            print("🚀 初始化OCR系统（全局单例）...")
            from simple_ocr_system import SimpleOCRSystem
            EnhancedReadFiles._ocr_system = SimpleOCRSystem()
            print("✅ OCR系统初始化完成！")

    def get_files(self):
        file_list = []
        for filepath, dirnames, filenames in os.walk(self._path):
            for filename in filenames:
                if filename.endswith((".md", ".txt", ".pdf")):
                    file_list.append(os.path.join(filepath, filename))
        return file_list

    def get_content(self, max_token_len: int = 600, cover_content: int = 150):
        """
        获取所有文档内容，保留元数据
        """
        docs = []
        for file in tqdm(self.file_list, desc="Processing files"):
            try:
                # 读取文件内容和元数据
                content, metadata = self.read_file_content_with_metadata(file)
                
                # 分块并附加元数据
                chunk_content = self.get_chunk_with_metadata(
                    content, metadata, 
                    max_token_len=max_token_len, 
                    cover_content=cover_content
                )
                docs.extend(chunk_content)
            except Exception as e:
                print(f"Error processing {file}: {e}")
                continue
        
        return docs

    @classmethod
    def read_file_content_with_metadata(cls, file_path: str) -> Tuple[str, Dict]:
        """
        读取文件内容并提取元数据
        """
        metadata = {
            'source': file_path,
            'filename': os.path.basename(file_path),
            'file_type': os.path.splitext(file_path)[1]
        }
        
        if file_path.endswith('.pdf'):
            content = cls.read_pdf_enhanced(file_path, metadata)
        elif file_path.endswith('.md'):
            content = cls.read_markdown(file_path)
        elif file_path.endswith('.txt'):
            content = cls.read_text(file_path)
        else:
            raise ValueError("Unsupported file type")
        
        return content, metadata

    @classmethod
    def read_pdf_enhanced(cls, file_path: str, metadata: Dict) -> str:
        """
        增强的PDF读取，使用PaddleOCR支持表格、多语言、旋转纠正等
        Args:
            file_path: PDF文件路径
            metadata: 元数据字典
        Returns:
            提取的文本
        """
        # 使用类级别的OCR系统实例（已经初始化好了）
        ocr_system = cls._ocr_system
        
        # 使用PPStructureV3进行文档结构分析
        results = ocr_system.process_document(
            file_path,
            use_structure_analysis=True,  # 使用结构分析（版面+表格+OCR）
            extract_toc=True              # 提取目录
        )
        
        # 合并所有页面的文本
        full_text = []
        metadata['total_pages'] = len(results['pages'])
        
        for page in results['pages']:
            full_text.append(f"\n{'='*50}\n[第 {page['page_number']} 页]\n{'='*50}\n")
            
            # 添加表格（Markdown格式）
            if page['tables']:
                for table in page['tables']:
                    if table.get('markdown'):
                        full_text.append(f"\n[表格 {table['table_index']}]\n{table['markdown']}\n")
            
            # 添加文本
            if page['text']:
                full_text.append(page['text'])
        
        return "\n".join(full_text)

    @classmethod
    def detect_tables_in_page(cls, page) -> List[str]:
        """
        检测页面中的表格并提取
        使用简单的启发式方法检测表格结构
        """
        tables = []
        text = page.get_text("text")
        lines = text.split('\n')
        
        # 简单的表格检测：连续多行包含多个空格分隔的内容
        potential_table = []
        in_table = False
        
        for line in lines:
            # 检测是否可能是表格行（包含多个连续空格或制表符）
            if re.search(r'\s{2,}|\t', line) and len(line.split()) >= 2:
                potential_table.append(line)
                in_table = True
            elif in_table:
                # 如果表格中断，保存当前表格
                if len(potential_table) >= 3:  # 至少3行才算表格
                    tables.append('\n'.join(potential_table))
                potential_table = []
                in_table = False
        
        # 保存最后一个表格
        if len(potential_table) >= 3:
            tables.append('\n'.join(potential_table))
        
        return tables

    @classmethod
    def read_markdown(cls, file_path: str) -> str:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    @classmethod
    def read_text(cls, file_path: str) -> str:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    @classmethod
    def get_chunk_with_metadata(cls, text: str, metadata: Dict, 
                                max_token_len: int = 600, 
                                cover_content: int = 150) -> List[str]:
        """
        分块并保留元数据信息
        """
        chunks = cls.get_chunk(text, max_token_len, cover_content)
        
        # 为每个chunk添加元数据标记
        chunks_with_metadata = []
        for i, chunk in enumerate(chunks):
            # 在chunk开头添加来源信息
            metadata_header = f"[来源: {metadata['filename']}]"
            chunk_with_meta = f"{metadata_header}\n{chunk}"
            chunks_with_metadata.append(chunk_with_meta)
        
        return chunks_with_metadata

    @classmethod
    def get_chunk(cls, text: str, max_token_len: int = 600, cover_content: int = 150) -> List[str]:
        """
        智能分块，保留段落完整性
        """
        chunk_text = []
        curr_len = 0
        curr_chunk = ''
        token_len = max_token_len - cover_content
        
        # 按段落分割（保留页面标记）
        paragraphs = re.split(r'\n\s*\n', text)
        
        for para in paragraphs:
            para = para.strip()
            if not para:
                continue
                
            para_len = len(enc.encode(para))
            
            # 如果单个段落超长，需要进一步分割
            if para_len > max_token_len:
                if curr_chunk:
                    chunk_text.append(curr_chunk)
                    curr_chunk = ''
                    curr_len = 0
                
                # 分割长段落
                sub_chunks = cls.split_long_paragraph(para, token_len)
                chunk_text.extend(sub_chunks)
                
            elif curr_len + para_len + 2 <= token_len:
                if curr_chunk:
                    curr_chunk += '\n\n'
                    curr_len += 2
                curr_chunk += para
                curr_len += para_len
            else:
                if curr_chunk:
                    chunk_text.append(curr_chunk)
                
                # 添加覆盖内容
                if chunk_text and cover_content > 0:
                    prev_chunk = chunk_text[-1]
                    cover_part = prev_chunk[-cover_content:] if len(prev_chunk) > cover_content else prev_chunk
                    curr_chunk = cover_part + '\n\n' + para
                    curr_len = len(enc.encode(cover_part)) + 2 + para_len
                else:
                    curr_chunk = para
                    curr_len = para_len
        
        if curr_chunk:
            chunk_text.append(curr_chunk)
        
        return chunk_text

    @classmethod
    def split_long_paragraph(cls, para: str, token_len: int) -> List[str]:
        """
        分割超长段落，尽量在句子边界处分割
        """
        # 按句子分割（中英文）
        sentences = re.split(r'([。！？\.!?])', para)
        
        chunks = []
        curr_chunk = ''
        curr_len = 0
        
        for i in range(0, len(sentences), 2):
            if i + 1 < len(sentences):
                sentence = sentences[i] + sentences[i + 1]
            else:
                sentence = sentences[i]
            
            sentence = sentence.strip()
            if not sentence:
                continue
            
            sent_len = len(enc.encode(sentence))
            
            if curr_len + sent_len <= token_len:
                curr_chunk += sentence
                curr_len += sent_len
            else:
                if curr_chunk:
                    chunks.append(curr_chunk)
                curr_chunk = sentence
                curr_len = sent_len
        
        if curr_chunk:
            chunks.append(curr_chunk)
        
        return chunks


class QueryParser:
    """
    查询解析器，提取查询中的关键信息
    """
    
    @staticmethod
    def extract_entities(query: str) -> Dict[str, List[str]]:
        """
        从查询中提取实体
        """
        entities = {
            'years': [],
            'standards': [],
            'companies': [],
            'numbers': [],
            'locations': []
        }
        
        # 提取年份
        years = re.findall(r'\b(19|20)\d{2}\b', query)
        entities['years'] = years
        
        # 提取标准号（如GB/T 12345-2023, IEEE 1474.1等）
        standards = re.findall(r'\b[A-Z]{2,}[\/\s]*[A-Z]*\s*\d+[\.\-]\d+[\-\d]*\b', query)
        entities['standards'] = standards
        
        # 提取数字
        numbers = re.findall(r'\d+', query)
        entities['numbers'] = numbers
        
        # 提取地点（简单的中文地名检测）
        locations = re.findall(r'(北京|上海|广州|深圳|南京|杭州|武汉|成都|重庆|天津|[\u4e00-\u9fa5]{2,}市|[\u4e00-\u9fa5]{2,}省)', query)
        entities['locations'] = locations
        
        return entities
    
    @staticmethod
    def is_comparison_query(query: str) -> bool:
        """
        判断是否为对比类查询
        """
        comparison_keywords = ['对比', '比较', '不同', '差异', '区别', '演变', '变化', 'vs', 'versus']
        return any(keyword in query.lower() for keyword in comparison_keywords)
    
    @staticmethod
    def is_ranking_query(query: str) -> bool:
        """
        判断是否为排名类查询
        """
        ranking_keywords = ['排名', '排第几', '排行', '第几', '名次']
        return any(keyword in query for keyword in ranking_keywords)
    
    @staticmethod
    def is_listing_query(query: str) -> bool:
        """
        判断是否为列举类查询
        """
        listing_keywords = ['列出', '所有', '全部', '完整', '哪些', '分别']
        return any(keyword in query for keyword in listing_keywords)


if __name__ == "__main__":
    # 测试代码
    reader = EnhancedReadFiles('../data')
    docs = reader.get_content(max_token_len=400, cover_content=50)
    print(f"Total chunks: {len(docs)}")
    print(f"First chunk preview: {docs[0][:200]}...")

