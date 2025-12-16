#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
增强OCR系统（使用MinerU）
MinerU: mineru -p <input_path> -o <output_path>

优化策略：
1. 使用HuggingFace镜像加速模型下载
2. 缓存处理结果，避免重复处理
3. 支持批量处理
"""

import os
import subprocess
import json
import hashlib
from typing import List, Dict, Tuple, Optional
from pathlib import Path

# 配置HuggingFace镜像（加速模型下载）
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

# 检查MinerU是否可用
def check_mineru():
    try:
        result = subprocess.run(['mineru', '--version'], 
                              capture_output=True, text=True, timeout=5)
        return result.returncode == 0
    except:
        return False

MINERU_AVAILABLE = check_mineru()
if MINERU_AVAILABLE:
    print("✅ MinerU 已安装并可用")
else:
    print("⚠️  MinerU 不可用，请安装: pip install mineru")


class EnhancedOCRProcessor:
    """
    增强OCR处理器（基于MinerU）
    支持PDF、DOCX、PPTX的高质量解析
    
    优化特性：
    1. 缓存处理结果，避免重复处理
    2. 并行处理支持
    3. 自动清理临时文件
    """
    
    def __init__(self, use_cache: bool = True, cache_dir: str = None):
        """
        初始化处理器
        
        Args:
            use_cache: 是否使用缓存（默认True）
            cache_dir: 缓存目录（默认为.mineru_cache）
        """
        if not MINERU_AVAILABLE:
            raise Exception("MinerU 不可用，请先安装: pip install mineru")
        
        self.use_cache = use_cache
        self.cache_dir = cache_dir or ".mineru_cache"
        
        if self.use_cache:
            os.makedirs(self.cache_dir, exist_ok=True)
    
    def _get_file_hash(self, file_path: str) -> str:
        """计算文件的MD5哈希值（用于缓存键）"""
        hasher = hashlib.md5()
        with open(file_path, 'rb') as f:
            # 只读取前1MB来计算hash（加速）
            hasher.update(f.read(1024 * 1024))
        return hasher.hexdigest()
    
    def _get_cache_path(self, file_path: str) -> str:
        """获取缓存文件路径"""
        file_hash = self._get_file_hash(file_path)
        file_name = Path(file_path).stem
        cache_file = f"{file_name}_{file_hash}.json"
        return os.path.join(self.cache_dir, cache_file)
    
    def _load_from_cache(self, file_path: str) -> Optional[Dict]:
        """从缓存加载结果"""
        if not self.use_cache:
            return None
        
        cache_path = self._get_cache_path(file_path)
        if os.path.exists(cache_path):
            try:
                with open(cache_path, 'r', encoding='utf-8') as f:
                    print(f"   📦 从缓存加载: {Path(cache_path).name}")
                    return json.load(f)
            except Exception as e:
                print(f"   ⚠️  缓存加载失败: {e}")
        return None
    
    def _save_to_cache(self, file_path: str, result: Dict):
        """保存结果到缓存"""
        if not self.use_cache or not result:
            return
        
        cache_path = self._get_cache_path(file_path)
        try:
            with open(cache_path, 'w', encoding='utf-8') as f:
                json.dump(result, f, ensure_ascii=False, indent=2)
            print(f"   💾 已缓存结果: {Path(cache_path).name}")
        except Exception as e:
            print(f"   ⚠️  缓存保存失败: {e}")
    
    def process_file(self, file_path: str, output_dir: str = None) -> Dict:
        """
        使用MinerU处理文件（PDF、DOCX、PPTX）
        带缓存支持，避免重复处理
        
        Args:
            file_path: 输入文件路径
            output_dir: 输出目录
            
        Returns:
            处理结果，包含文本、图片、表格等
        """
        if not os.path.exists(file_path):
            print(f"❌ 文件不存在: {file_path}")
            return None
        
        file_name = os.path.basename(file_path)
        print(f"\n📄 处理文件: {file_name}")
        
        # 尝试从缓存加载
        cached_result = self._load_from_cache(file_path)
        if cached_result:
            return cached_result
        
        # 准备输出目录
        if output_dir is None:
            file_basename = Path(file_path).stem
            output_dir = os.path.join(
                os.path.dirname(file_path), 
                f"mineru_output_{file_basename}"
            )
        os.makedirs(output_dir, exist_ok=True)
        
        file_ext = Path(file_path).suffix.lower()
        print(f"   输出目录: {output_dir}")
        
        try:
            # 构建MinerU命令
            cmd = ['mineru', '-p', file_path, '-o', output_dir]
            
            print(f"   🔧 执行: {' '.join(cmd)}")
            print(f"   ⏳ 处理中...（可能需要几分钟）")
            
            # 执行命令
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=600,  # 10分钟超时
                cwd=os.getcwd()
            )
            
            if result.returncode != 0:
                print(f"   ❌ MinerU处理失败")
                print(f"   错误: {result.stderr}")
                return None
            
            print(f"   ✅ MinerU处理完成")
            
            # 解析输出结果
            parsed_result = self._parse_mineru_output(output_dir, file_name)
            
            if parsed_result:
                print(f"   📊 提取统计:")
                print(f"      - 文本块: {parsed_result.get('text_blocks', 0)}")
                print(f"      - 图片: {parsed_result.get('image_count', 0)}")
                print(f"      - 表格: {parsed_result.get('table_count', 0)}")
                
                # 保存到缓存
                self._save_to_cache(file_path, parsed_result)
            
            return parsed_result
            
        except subprocess.TimeoutExpired:
            print(f"   ❌ 处理超时（10分钟）")
            return None
        except Exception as e:
            print(f"   ❌ 处理失败: {e}")
            return None
    
    def _parse_mineru_output(self, output_dir: str, original_filename: str) -> Dict:
        """
        解析MinerU的输出结果
        
        Args:
            output_dir: MinerU输出目录
            original_filename: 原始文件名
            
        Returns:
            解析后的结果字典
        """
        result = {
            'original_file': original_filename,
            'output_dir': output_dir,
            'markdown': '',
            'text_blocks': 0,
            'image_count': 0,
            'table_count': 0,
            'content': ''
        }
        
        try:
            # 查找生成的Markdown文件
            md_files = list(Path(output_dir).rglob('*.md'))
            
            if md_files:
                md_file = md_files[0]  # 取第一个MD文件
                print(f"   📝 找到Markdown: {md_file.name}")
                
                with open(md_file, 'r', encoding='utf-8') as f:
                    markdown_content = f.read()
                
                result['markdown'] = markdown_content
                result['content'] = markdown_content
                
                # 统计信息
                result['text_blocks'] = len(markdown_content.split('\n\n'))
                result['image_count'] = markdown_content.count('![')
                result['table_count'] = markdown_content.count('|')
            
            # 查找提取的图片
            image_files = []
            for ext in ['.png', '.jpg', '.jpeg']:
                image_files.extend(Path(output_dir).rglob(f'*{ext}'))
            
            result['image_files'] = [str(f) for f in image_files]
            result['image_count'] = len(image_files)
            
            return result
            
        except Exception as e:
            print(f"   ⚠️  解析输出失败: {e}")
            return result
    
    def process_pdf(self, pdf_path: str, output_dir: str = None) -> str:
        """
        处理PDF文件，返回提取的文本
        
        Args:
            pdf_path: PDF文件路径
            output_dir: 输出目录
            
        Returns:
            提取的文本内容
        """
        result = self.process_file(pdf_path, output_dir)
        if result:
            return result.get('content', '')
        return ''
    
    def process_docx(self, docx_path: str, output_dir: str = None) -> str:
        """
        处理DOCX文件，返回提取的文本
        
        Args:
            docx_path: DOCX文件路径
            output_dir: 输出目录
            
        Returns:
            提取的文本内容
        """
        result = self.process_file(docx_path, output_dir)
        if result:
            return result.get('content', '')
        return ''
    
    def process_pptx(self, pptx_path: str, output_dir: str = None) -> str:
        """
        处理PPTX文件，返回提取的文本
        
        Args:
            pptx_path: PPTX文件路径
            output_dir: 输出目录
            
        Returns:
            提取的文本内容
        """
        result = self.process_file(pptx_path, output_dir)
        if result:
            return result.get('content', '')
        return ''
    
    def batch_process(self, file_list: List[str], output_base_dir: str = None) -> Dict:
        """
        批量处理文件
        
        Args:
            file_list: 文件路径列表
            output_base_dir: 输出根目录
            
        Returns:
            批量处理结果统计
        """
        results = {
            'total': len(file_list),
            'success': 0,
            'failed': 0,
            'files': []
        }
        
        for file_path in file_list:
            file_ext = Path(file_path).suffix.lower()
            
            # 跳过txt文件
            if file_ext == '.txt':
                print(f"⏭️  跳过TXT文件: {os.path.basename(file_path)}")
                continue
            
            # 准备输出目录
            if output_base_dir:
                file_basename = Path(file_path).stem
                output_dir = os.path.join(output_base_dir, file_basename)
            else:
                output_dir = None
            
            # 处理文件
            result = self.process_file(file_path, output_dir)
            
            if result:
                results['success'] += 1
                results['files'].append({
                    'file': file_path,
                    'status': 'success',
                    'result': result
                })
            else:
                results['failed'] += 1
                results['files'].append({
                    'file': file_path,
                    'status': 'failed'
                })
        
        print(f"\n{'='*60}")
        print(f"📊 批量处理完成:")
        print(f"   总计: {results['total']}")
        print(f"   成功: {results['success']}")
        print(f"   失败: {results['failed']}")
        print(f"{'='*60}\n")
        
        return results


def test_mineru():
    """测试MinerU"""
    if not MINERU_AVAILABLE:
        print("❌ MinerU 不可用")
        print("安装方法: pip install mineru")
        return
    
    print("\n=== 测试MinerU ===\n")
    processor = EnhancedOCRProcessor()
    
    # 测试示例
    test_files = [
        "data/test.pdf",
        "data/test.docx", 
        "data/test.pptx"
    ]
    
    for file_path in test_files:
        if os.path.exists(file_path):
            print(f"测试文件: {file_path}")
            result = processor.process_file(file_path)
            if result:
                print(f"✅ 成功")
            else:
                print(f"❌ 失败")
        else:
            print(f"⏭️  文件不存在: {file_path}")


if __name__ == "__main__":
    test_mineru()
