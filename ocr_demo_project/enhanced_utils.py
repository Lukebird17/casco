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
import html
from bs4 import BeautifulSoup

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
        # print(file_list)
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
                # print(content)
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
        print("read_pdf_enhanced",results)
        # 合并所有页面的文本
        full_text = []
        metadata['total_pages'] = len(results['pages'])
        
        for page in results['pages']:
            full_text.append(f"\n{'='*50}\n[第 {page['page_number']} 页]\n{'='*50}\n")
            
            # 添加表格（Markdown格式）
            # 注意：API处理的结果可能没有'tables'字段，需要检查
            if 'tables' in page and page['tables']:
                for table in page['tables']:
                    if table.get('markdown'):
                        full_text.append(f"\n[表格 {table['table_index']}]\n{table['markdown']}\n")
            
            # 添加文本
            if page.get('text'):
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
        """
        增强的Markdown读取，特别处理HTML表格
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # 处理HTML表格，使其更易检索
        content = cls.enhance_markdown_tables(content)
        return content
    
    @classmethod
    def enhance_markdown_tables(cls, content: str) -> str:
        """
        增强HTML表格的可读性和可检索性
        1. 提取表格前的标题/说明
        2. 将HTML表格转换为更易检索的格式
        3. 保留表格的语义完整性
        """
        # 查找所有HTML表格及其上下文
        # 匹配：<div>表X</div> + 可能的空行 + <table>...</table>
        table_pattern = r'(<div[^>]*>.*?表\s*\d+.*?</div>\s*\n*\s*)?(<table[^>]*>.*?</table>)'
        
        enhanced_content = content
        tables = re.finditer(table_pattern, content, re.DOTALL | re.IGNORECASE)
        
        for match in tables:
            title_html = match.group(1) if match.group(1) else ''
            table_html = match.group(2)
            full_match = match.group(0)
            
            # 解析表格标题
            table_title = ''
            if title_html:
                soup_title = BeautifulSoup(title_html, 'html.parser')
                table_title = soup_title.get_text().strip()
            
            # 解析HTML表格
            try:
                soup = BeautifulSoup(table_html, 'html.parser')
                table = soup.find('table')
                
                if table:
                    # 提取表格为结构化文本
                    table_text = cls.html_table_to_text(table, table_title)
                    
                    # 替换原始HTML表格
                    enhanced_content = enhanced_content.replace(full_match, table_text)
            except Exception as e:
                print(f"Warning: Failed to parse table: {e}")
                continue
        
        return enhanced_content
    
    @classmethod
    def html_table_to_text(cls, table_soup, table_title: str = '') -> str:
        """
        将HTML表格转换为易于检索的文本格式
        保留完整的表格结构和语义信息
        """
        lines = []
        
        # 添加表格标题
        if table_title:
            lines.append(f"\n{'='*60}")
            lines.append(f"【{table_title}】")
            lines.append(f"{'='*60}\n")
        
        # 提取表头
        headers = []
        thead = table_soup.find('thead')
        if thead:
            header_rows = thead.find_all('tr')
            for row in header_rows:
                cells = row.find_all(['th', 'td'])
                headers = [cell.get_text().strip() for cell in cells]
        else:
            # 如果没有thead，尝试从第一行提取
            first_row = table_soup.find('tr')
            if first_row:
                cells = first_row.find_all(['th', 'td'])
                if any(cell.name == 'th' for cell in cells):
                    headers = [cell.get_text().strip() for cell in cells]
        
        # 提取所有行
        rows = []
        tbody = table_soup.find('tbody') or table_soup
        for row in tbody.find_all('tr'):
            cells = row.find_all(['td', 'th'])
            row_data = []
            for cell in cells:
                # 处理colspan和rowspan
                colspan = int(cell.get('colspan', 1))
                text = cell.get_text().strip()
                row_data.append(text)
                # 为colspan添加占位
                for _ in range(colspan - 1):
                    row_data.append('')
            if row_data:
                rows.append(row_data)
        
        # 如果有表头，单独标记
        if headers:
            lines.append("【表头】")
            lines.append(" | ".join(headers))
            lines.append("-" * 80)
        
        # 添加数据行
        lines.append("【表格数据】")
        for i, row in enumerate(rows):
            # 跳过可能重复的表头行
            if headers and row == headers:
                continue
            
            # 格式化每一行
            if headers and len(row) == len(headers):
                # 键值对格式，更易理解
                row_text = " | ".join([f"{h}:{v}" if v else h for h, v in zip(headers, row)])
            else:
                # 简单格式
                row_text = " | ".join(row)
            
            lines.append(f"  {row_text}")
        
        lines.append("\n" + "="*60 + "\n")
        
        return "\n".join(lines)

    @classmethod
    def read_text(cls, file_path: str) -> str:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    @classmethod
    def get_chunk_with_metadata(cls, text: str, metadata: Dict, 
                                max_token_len: int = 600, 
                                cover_content: int = 150) -> List[str]:
        """
        分块并保留元数据信息，确保不超过token限制
        """
        chunks = cls.get_chunk(text, max_token_len, cover_content)
        
        # 为每个chunk添加元数据标记，并验证token长度
        chunks_with_metadata = []
        metadata_header = f"[来源: {metadata['filename']}]"
        metadata_header_tokens = len(enc.encode(metadata_header))
        
        # 实际可用的token长度（留100 token余量）
        safe_max_tokens = 7900  # 远低于8000的硬限制
        
        for i, chunk in enumerate(chunks):
            chunk_with_meta = f"{metadata_header}\n{chunk}"
            chunk_tokens = len(enc.encode(chunk_with_meta))
            
            # 如果超过安全限制，需要进一步分割
            if chunk_tokens > safe_max_tokens:
                print(f"⚠️  警告: Chunk #{i+1} 超过限制 ({chunk_tokens} tokens)，进行强制分割...")
                
                # 计算每个子chunk的目标token数（留足余量）
                sub_chunk_target_tokens = safe_max_tokens - metadata_header_tokens - 100
                
                # 使用二分法找到合适的字符数
                lines = chunk.split('\n')
                current_lines = []
                current_tokens = 0
                
                for line in lines:
                    line_tokens = len(enc.encode(line + '\n'))
                    
                    if current_tokens + line_tokens <= sub_chunk_target_tokens:
                        current_lines.append(line)
                        current_tokens += line_tokens
                    else:
                        # 保存当前子chunk
                        if current_lines:
                            sub_chunk = '\n'.join(current_lines)
                            sub_chunk_with_meta = f"{metadata_header}\n{sub_chunk}"
                            
                            # 最后验证
                            final_tokens = len(enc.encode(sub_chunk_with_meta))
                            if final_tokens > safe_max_tokens:
                                print(f"   ⚠️  子chunk仍超限({final_tokens} tokens)，继续细分...")
                                # 进一步分割当前行
                                half = len(current_lines) // 2
                                if half > 0:
                                    sub_chunk = '\n'.join(current_lines[:half])
                                    sub_chunk_with_meta = f"{metadata_header}\n{sub_chunk}"
                                    chunks_with_metadata.append(sub_chunk_with_meta)
                                    current_lines = current_lines[half:]
                                else:
                                    # 单行太长，强制截断
                                    chunks_with_metadata.append(sub_chunk_with_meta[:safe_max_tokens*4])
                                    current_lines = []
                            else:
                                chunks_with_metadata.append(sub_chunk_with_meta)
                        
                        # 开始新的子chunk
                        current_lines = [line]
                        current_tokens = line_tokens
                
                # 保存最后一个子chunk
                if current_lines:
                    sub_chunk = '\n'.join(current_lines)
                    sub_chunk_with_meta = f"{metadata_header}\n{sub_chunk}"
                    chunks_with_metadata.append(sub_chunk_with_meta)
            else:
                chunks_with_metadata.append(chunk_with_meta)
        
        return chunks_with_metadata

    @classmethod
    def get_chunk(cls, text: str, max_token_len: int = 600, cover_content: int = 150) -> List[str]:
        """
        智能分块，保留段落和表格完整性
        """
        chunk_text = []
        curr_len = 0
        curr_chunk = ''
        token_len = max_token_len - cover_content
        
        # 先识别表格块（以【表头】或【表格数据】标记的块）
        table_pattern = r'(={60,}\n【.*?表.*?】\n={60,}.*?(?=\n={60,}\n\n|\Z))'
        
        # 分割文本，保留表格块的完整性
        parts = re.split(table_pattern, text, flags=re.DOTALL)
        
        for part in parts:
            if not part or not part.strip():
                continue
            
            # 检查是否是表格块
            is_table = '【表头】' in part or '【表格数据】' in part or part.startswith('='*60)
            
            if is_table:
                # 表格块单独处理
                part_len = len(enc.encode(part))
                
                # 如果表格太大，需要智能分割
                if part_len > max_token_len:
                    # 保存当前chunk
                    if curr_chunk:
                        chunk_text.append(curr_chunk)
                        curr_chunk = ''
                        curr_len = 0
                    
                    # 智能分割大表格
                    table_chunks = cls.split_large_table(part, token_len)
                    chunk_text.extend(table_chunks)
                
                # 表格能完整放入当前chunk
                elif curr_len + part_len + 2 <= token_len:
                    if curr_chunk:
                        curr_chunk += '\n\n'
                        curr_len += 2
                    curr_chunk += part
                    curr_len += part_len
                
                # 表格无法放入当前chunk，需要新chunk
                else:
                    if curr_chunk:
                        chunk_text.append(curr_chunk)
                    curr_chunk = part
                    curr_len = part_len
            
            else:
                # 普通文本按段落分割
                paragraphs = re.split(r'\n\s*\n', part)
                
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
    def split_large_table(cls, table_text: str, token_len: int) -> List[str]:
        """
        智能分割大表格，保留表头和标题
        确保每个chunk不超过token限制
        """
        chunks = []
        
        # 提取表格标题
        title_match = re.search(r'={60,}\n(【.*?】)\n={60,}', table_text)
        title = title_match.group(0) if title_match else ''
        
        # 提取表头
        header_match = re.search(r'【表头】\n(.*?)\n-{60,}', table_text, re.DOTALL)
        header = ''
        if header_match:
            header = f"【表头】\n{header_match.group(1)}\n{'-'*80}"
        
        # 提取数据行
        data_match = re.search(r'【表格数据】\n(.*?)(?=\n={60,}|\Z)', table_text, re.DOTALL)
        if not data_match:
            # 如果无法解析，直接按行分割
            lines = table_text.split('\n')
            curr_chunk = ''
            curr_len = 0
            
            # 使用更保守的token限制
            safe_limit = min(token_len, 600)
            
            for line in lines:
                line_len = len(enc.encode(line + '\n'))
                if curr_len + line_len <= safe_limit:
                    curr_chunk += line + '\n'
                    curr_len += line_len
                else:
                    if curr_chunk:
                        chunks.append(curr_chunk)
                    curr_chunk = line + '\n'
                    curr_len = line_len
            
            if curr_chunk:
                chunks.append(curr_chunk)
            
            return chunks if chunks else [table_text[:token_len*3]]
        
        data_lines = data_match.group(1).strip().split('\n')
        
        # 计算表头和标题的token长度
        header_len = len(enc.encode(title + '\n' + header))
        
        # 更保守的可用长度计算，确保不超过整体限制
        available_len = min(token_len - header_len - 200, 400)  # 最多400 token的数据
        
        if available_len < 100:
            # 如果表头太长，只能简化或放弃表头
            available_len = min(token_len - 100, 500)
            title = ''
            header = ''
        
        # 分批处理数据行
        curr_chunk_lines = []
        curr_data_len = 0
        
        for line in data_lines:
            line = line.strip()
            if not line:
                continue
            
            line_len = len(enc.encode(line + '\n'))
            
            # 如果单行就超过可用长度，需要截断
            if line_len > available_len:
                # 先保存当前积累的行
                if curr_chunk_lines:
                    chunk = title + '\n' + header + '\n【表格数据】\n' + '\n'.join(curr_chunk_lines) + '\n' + '='*60
                    chunks.append(chunk)
                    curr_chunk_lines = []
                    curr_data_len = 0
                
                # 截断超长行
                truncated_line = line[:available_len * 3]  # 粗略估算
                curr_chunk_lines = [truncated_line]
                curr_data_len = len(enc.encode(truncated_line))
                continue
            
            if curr_data_len + line_len <= available_len:
                curr_chunk_lines.append(line)
                curr_data_len += line_len
            else:
                # 保存当前chunk
                if curr_chunk_lines:
                    chunk = title + '\n' + header + '\n【表格数据】\n' + '\n'.join(curr_chunk_lines) + '\n' + '='*60
                    chunks.append(chunk)
                
                # 开始新chunk
                curr_chunk_lines = [line]
                curr_data_len = line_len
        
        # 保存最后一个chunk
        if curr_chunk_lines:
            chunk = title + '\n' + header + '\n【表格数据】\n' + '\n'.join(curr_chunk_lines) + '\n' + '='*60
            chunks.append(chunk)
        
        return chunks if chunks else [table_text[:token_len*3]]

    @classmethod
    def split_long_paragraph(cls, para: str, token_len: int) -> List[str]:
        """
        分割超长段落，尽量在句子边界处分割
        特别处理HTML表格
        """
        # 检测是否为HTML表格
        if para.strip().startswith('<table'):
            # 按表格行分割
            rows = re.split(r'(<tr>|</tr>)', para)
            chunks = []
            curr_chunk = ''
            curr_len = 0
            
            for row in rows:
                if not row or row in ['<tr>', '</tr>']:
                    curr_chunk += row
                    continue
                
                row_len = len(enc.encode(row))
                
                # 如果单行就超过限制，强制截断
                if row_len > token_len:
                    if curr_chunk:
                        chunks.append(curr_chunk)
                        curr_chunk = ''
                        curr_len = 0
                    # 超长行按字符分割
                    for i in range(0, len(row), token_len * 3):  # 粗略估算
                        sub_row = row[i:i + token_len * 3]
                        if len(enc.encode(sub_row)) <= token_len:
                            chunks.append(sub_row)
                        else:
                            # 继续细分
                            chunks.append(sub_row[:token_len * 2])
                    continue
                
                if curr_len + row_len <= token_len:
                    curr_chunk += row
                    curr_len += row_len
                else:
                    if curr_chunk:
                        chunks.append(curr_chunk)
                    curr_chunk = row
                    curr_len = row_len
            
            if curr_chunk:
                chunks.append(curr_chunk)
            
            return chunks if chunks else [para[:token_len * 3]]
        
        # 普通文本按句子分割（中英文）
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
            
            # 如果单个句子就超过限制，按字符强制分割
            if sent_len > token_len:
                if curr_chunk:
                    chunks.append(curr_chunk)
                    curr_chunk = ''
                    curr_len = 0
                # 强制按token_len分割
                for i in range(0, len(sentence), token_len * 3):
                    chunks.append(sentence[i:i + token_len * 3])
                continue
            
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
        
        return chunks if chunks else [para[:token_len * 3]]


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

