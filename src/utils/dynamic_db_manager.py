#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
动态数据库管理器
支持按课程标签动态添加文件到向量数据库
"""

import os
import hashlib
from typing import List, Dict, Optional
from datetime import datetime

from src.processors.document_loader import DocumentLoader
from src.processors.text_splitter import TextSplitter
from src.core.vector_store import VectorStore
from src.processors.enhanced_ocr import EnhancedOCRProcessor
from config import CHUNK_SIZE, CHUNK_OVERLAP


class DynamicDBManager:
    """
    动态数据库管理器
    
    功能：
    1. 按课程标签组织文档
    2. 动态添加文件到数据库
    3. 删除课程相关文档
    4. 查询课程文档列表
    5. 增量更新（避免重复处理）
    """
    
    def __init__(self, vector_store: VectorStore = None):
        """
        初始化管理器
        
        Args:
            vector_store: 向量存储实例
        """
        self.vector_store = vector_store or VectorStore()
        self.document_loader = DocumentLoader()
        self.text_splitter = TextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP
        )
        self.ocr_processor = EnhancedOCRProcessor(use_cache=True)
        
        # 文档元数据缓存
        self.metadata_file = "vector_db_metadata.json"
        self.metadata = self._load_metadata()
    
    def _load_metadata(self) -> Dict:
        """加载元数据"""
        import json
        
        if os.path.exists(self.metadata_file):
            with open(self.metadata_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {
            'courses': {},  # course_name -> {files: [], doc_count: int}
            'files': {}     # file_hash -> {path, course, chunks, add_time}
        }
    
    def _save_metadata(self):
        """保存元数据"""
        import json
        
        with open(self.metadata_file, 'w', encoding='utf-8') as f:
            json.dump(self.metadata, f, ensure_ascii=False, indent=2)
    
    def _calculate_file_hash(self, file_path: str) -> str:
        """计算文件哈希值"""
        hasher = hashlib.md5()
        
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        
        return hasher.hexdigest()
    
    def add_file(self, 
                 file_path: str, 
                 course_name: str,
                 use_ocr: bool = False) -> Dict[str, any]:
        """
        添加文件到数据库
        
        Args:
            file_path: 文件路径
            course_name: 课程名称（作为标签）
            use_ocr: 是否使用OCR
            
        Returns:
            处理结果统计
        """
        if not os.path.exists(file_path):
            return {'success': False, 'error': '文件不存在'}
        
        # 检查文件是否已添加
        file_hash = self._calculate_file_hash(file_path)
        if file_hash in self.metadata['files']:
            existing = self.metadata['files'][file_hash]
            return {
                'success': False,
                'error': '文件已存在',
                'existing_course': existing['course'],
                'add_time': existing['add_time']
            }
        
        print(f"\n📄 处理文件: {file_path}")
        print(f"📚 课程标签: {course_name}")
        
        try:
            # 1. 加载文档
            filename = os.path.basename(file_path)
            file_ext = os.path.splitext(filename)[1].lower()
            
            if use_ocr and file_ext in ['.pdf', '.docx', '.pptx']:
                # 使用OCR处理
                content = self._load_with_ocr(file_path, file_ext)
            else:
                # 常规加载
                content = self.document_loader.load_file(file_path)
            
            if not content:
                return {'success': False, 'error': '文档内容为空'}
            
            # 2. 文本切分
            text_chunks = self.text_splitter.split_text(content)
            print(f"  ✂️  切分为 {len(text_chunks)} 个文本块")
            
            # 3. 构建文档块（包含内容和元数据）
            chunks = [
                {
                    'content': text,
                    'filename': filename,
                    'filepath': file_path,
                    'filetype': file_ext[1:],  # 去掉点号
                    'page_number': 0,  # 整个文档，无法确定具体页码
                    'chunk_id': i,
                    'course': course_name,
                    'file_hash': file_hash,
                    'add_time': datetime.now().isoformat()
                }
                for i, text in enumerate(text_chunks)
            ]
            
            # 4. 添加到向量库
            self.vector_store.add_documents(chunks)
            print(f"  ✅ 已添加到向量库（课程: {course_name}）")
            
            # 4. 更新元数据
            if course_name not in self.metadata['courses']:
                self.metadata['courses'][course_name] = {
                    'files': [],
                    'doc_count': 0
                }
            
            self.metadata['courses'][course_name]['files'].append(filename)
            self.metadata['courses'][course_name]['doc_count'] += len(chunks)
            
            self.metadata['files'][file_hash] = {
                'path': file_path,
                'filename': filename,
                'course': course_name,
                'chunks': len(chunks),
                'add_time': datetime.now().isoformat()
            }
            
            self._save_metadata()
            
            return {
                'success': True,
                'filename': filename,
                'course': course_name,
                'chunks': len(chunks),
                'file_hash': file_hash
            }
        
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def _load_with_ocr(self, file_path: str, file_ext: str) -> str:
        """使用OCR加载文档（基于MinerU）"""
        if file_ext in ['.pdf', '.docx', '.pptx']:
            # 使用 MinerU 处理
            result = self.ocr_processor.process_file(file_path)
            if result and result.get('content'):
                return result['content']
            else:
                raise Exception(f"MinerU 处理失败: {file_path}")
        else:
            # 其他文件类型使用默认加载器
            return self.document_loader.load_file(file_path)
    
    def add_directory(self, 
                     directory: str, 
                     course_name: str,
                     use_ocr: bool = False,
                     file_extensions: List[str] = None) -> Dict:
        """
        批量添加目录中的文件
        
        Args:
            directory: 目录路径
            course_name: 课程名称
            use_ocr: 是否使用OCR
            file_extensions: 文件扩展名过滤（如['.pdf', '.docx']）
            
        Returns:
            批量处理结果
        """
        if not os.path.exists(directory):
            return {'success': False, 'error': '目录不存在'}
        
        if file_extensions is None:
            file_extensions = ['.pdf', '.docx', '.pptx', '.txt']
        
        results = {
            'total': 0,
            'success': 0,
            'failed': 0,
            'skipped': 0,
            'details': []
        }
        
        print(f"\n📁 批量处理目录: {directory}")
        print(f"📚 课程标签: {course_name}")
        
        for root, dirs, files in os.walk(directory):
            for filename in files:
                ext = os.path.splitext(filename)[1].lower()
                
                if ext in file_extensions:
                    file_path = os.path.join(root, filename)
                    results['total'] += 1
                    
                    result = self.add_file(file_path, course_name, use_ocr)
                    
                    if result['success']:
                        results['success'] += 1
                        print(f"  ✅ {filename}")
                    elif 'existing_course' in result:
                        results['skipped'] += 1
                        print(f"  ⏭️  {filename} (已存在)")
                    else:
                        results['failed'] += 1
                        print(f"  ❌ {filename}: {result.get('error', '未知错误')}")
                    
                    results['details'].append({
                        'file': filename,
                        'result': result
                    })
        
        print(f"\n📊 处理完成:")
        print(f"  总计: {results['total']} | 成功: {results['success']} | 失败: {results['failed']} | 跳过: {results['skipped']}")
        
        return results
    
    def remove_course(self, course_name: str) -> Dict:
        """
        删除课程的所有文档
        
        Args:
            course_name: 课程名称
            
        Returns:
            删除结果
        """
        if course_name not in self.metadata['courses']:
            return {'success': False, 'error': '课程不存在'}
        
        # 获取课程的所有文件哈希
        file_hashes_to_remove = []
        for file_hash, file_info in self.metadata['files'].items():
            if file_info['course'] == course_name:
                file_hashes_to_remove.append(file_hash)
        
        # 从向量库删除（这里需要ChromaDB支持按metadata删除）
        # 由于ChromaDB的限制，这里只能删除元数据记录
        # 实际向量需要重建数据库
        
        for file_hash in file_hashes_to_remove:
            del self.metadata['files'][file_hash]
        
        doc_count = self.metadata['courses'][course_name]['doc_count']
        del self.metadata['courses'][course_name]
        
        self._save_metadata()
        
        print(f"⚠️  已从元数据中删除课程 '{course_name}'")
        print(f"   删除了 {len(file_hashes_to_remove)} 个文件的记录")
        print(f"   注意：向量库需要重建以完全删除数据")
        
        return {
            'success': True,
            'course': course_name,
            'files_removed': len(file_hashes_to_remove),
            'docs_removed': doc_count,
            'note': '需要重建向量库以完全删除'
        }
    
    def list_courses(self) -> Dict[str, Dict]:
        """列出所有课程及其文档统计"""
        return self.metadata['courses']
    
    def search_by_course(self, 
                        query: str, 
                        course_name: str, 
                        top_k: int = 5) -> List[Dict]:
        """
        在指定课程中搜索
        
        Args:
            query: 查询文本
            course_name: 课程名称
            top_k: 返回结果数
            
        Returns:
            搜索结果
        """
        # 这里需要vector_store支持metadata过滤
        # 暂时返回所有结果后过滤
        all_results = self.vector_store.search(query, top_k=top_k * 3)
        
        # 过滤指定课程
        filtered = [
            r for r in all_results 
            if r.get('course') == course_name
        ]
        
        return filtered[:top_k]
    
    def get_statistics(self) -> Dict:
        """获取数据库统计信息"""
        total_courses = len(self.metadata['courses'])
        total_files = len(self.metadata['files'])
        total_chunks = sum(
            course_info['doc_count'] 
            for course_info in self.metadata['courses'].values()
        )
        
        return {
            'total_courses': total_courses,
            'total_files': total_files,
            'total_chunks': total_chunks,
            'courses': {
                name: {
                    'files': len(info['files']),
                    'chunks': info['doc_count']
                }
                for name, info in self.metadata['courses'].items()
            }
        }


def test_dynamic_db():
    """测试动态数据库管理"""
    manager = DynamicDBManager()
    
    # 测试添加文件
    result = manager.add_file(
        "data/test.pdf",
        course_name="NLP课程",
        use_ocr=False
    )
    print(f"\n添加结果: {result}")
    
    # 测试批量添加
    result = manager.add_directory(
        "data/NLP-Slides",
        course_name="自然语言处理",
        use_ocr=False
    )
    print(f"\n批量添加结果: {result}")
    
    # 查看统计
    stats = manager.get_statistics()
    print(f"\n数据库统计: {stats}")
    
    # 列出课程
    courses = manager.list_courses()
    print(f"\n课程列表: {courses}")


if __name__ == "__main__":
    test_dynamic_db()

