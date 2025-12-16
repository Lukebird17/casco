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
                    cached_data = json.load(f)
                    print(f"   📦 从缓存加载: {Path(cache_path).name}")
                    
                    # 检查缓存是否包含新字段（images）
                    if 'images' not in cached_data or cached_data['images'] is None:
                        print(f"   🔄 缓存版本旧，重新解析图片信息...")
                        # 重新解析输出目录（不需要重新运行 MinerU）
                        if 'output_dir' in cached_data and os.path.exists(cached_data['output_dir']):
                            file_name = os.path.basename(file_path)
                            updated_result = self._parse_mineru_output(
                                cached_data['output_dir'], 
                                file_name
                            )
                            # 更新缓存
                            self._save_to_cache(file_path, updated_result)
                            return updated_result
                    
                    return cached_data
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
            # 输出到项目根目录的 .mineru_output，避免递归处理
            output_dir = os.path.join(
                ".mineru_output", 
                file_basename
            )
        os.makedirs(output_dir, exist_ok=True)
        
        file_ext = Path(file_path).suffix.lower()
        print(f"   输出目录: {output_dir}")
        
        try:
            # 构建MinerU命令
            cmd = ['mineru', '-p', file_path, '-o', output_dir]
            
            print(f"   🔧 执行: {' '.join(cmd)}")
            print(f"   ⏳ 处理中...（可能需要几分钟）")
            print(f"\n{'='*60}")
            print("MinerU 输出:")
            print('='*60)
            
            # 执行命令（实时显示输出）
            result = subprocess.run(
                cmd,
                text=True,
                timeout=600,  # 10分钟超时
                cwd=os.getcwd()
            )
            
            print('='*60)
            
            if result.returncode != 0:
                print(f"   ❌ MinerU处理失败 (退出码: {result.returncode})")
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
            解析后的结果字典，包含详细的图片信息
        """
        result = {
            'original_file': original_filename,
            'output_dir': output_dir,
            'markdown': '',
            'text_blocks': 0,
            'image_count': 0,
            'table_count': 0,
            'content': '',
            'images': []  # 新增：详细的图片信息列表
        }
        
        try:
            # 查找生成的Markdown文件
            md_files = list(Path(output_dir).rglob('*.md'))
            markdown_content = ''
            
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
            
            # 查找提取的图片文件
            image_files = []
            for ext in ['.png', '.jpg', '.jpeg']:
                image_files.extend(Path(output_dir).rglob(f'*{ext}'))
            
            # 解析图片详细信息（包括上下文）
            result['images'] = self._extract_image_info(
                markdown_content, 
                image_files, 
                original_filename,
                output_dir
            )
            result['image_count'] = len(result['images'])
            
            return result
            
        except Exception as e:
            print(f"   ⚠️  解析输出失败: {e}")
            return result
    
    def _build_image_page_mapping(self, output_dir: str) -> Dict[str, int]:
        """
        从 MinerU 的 middle.json 构建图片hash到页码的映射
        
        Args:
            output_dir: MinerU 输出目录
            
        Returns:
            字典：{image_hash: page_number}
        """
        import json
        from pathlib import Path
        
        mapping = {}
        
        try:
            # 查找 middle.json 文件
            middle_json_path = None
            for json_file in Path(output_dir).rglob('*_middle.json'):
                middle_json_path = json_file
                break
            
            if not middle_json_path or not middle_json_path.exists():
                return mapping
            
            # 解析 middle.json
            with open(middle_json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            pdf_info = data.get('pdf_info', [])
            
            # 遍历每一页
            for page_idx, page_data in enumerate(pdf_info):
                page_number = page_idx + 1  # 页码从1开始
                
                # 遍历页面中的所有块
                for block in page_data.get('preproc_blocks', []):
                    # 查找图片块
                    if block.get('type') in ['image', 'image_body']:
                        # 递归查找 image_path
                        self._extract_image_paths_from_block(block, page_number, mapping)
            
            return mapping
            
        except Exception as e:
            print(f"   ⚠️  构建图片页码映射失败: {e}")
            return mapping
    
    def _extract_image_paths_from_block(self, block: Dict, page_number: int, mapping: Dict):
        """
        递归从块中提取图片路径
        
        Args:
            block: 块数据
            page_number: 页码
            mapping: 映射字典（会被修改）
        """
        # 检查当前块
        if isinstance(block, dict):
            # 如果有 image_path 字段
            if 'image_path' in block:
                img_path = block['image_path']
                # 提取hash（不含扩展名）
                img_hash = Path(img_path).stem
                mapping[img_hash] = page_number
            
            # 递归检查子块
            for key in ['blocks', 'lines', 'spans']:
                if key in block and isinstance(block[key], list):
                    for sub_block in block[key]:
                        self._extract_image_paths_from_block(sub_block, page_number, mapping)
        elif isinstance(block, list):
            for item in block:
                self._extract_image_paths_from_block(item, page_number, mapping)
    
    def _extract_image_info(self, markdown_content: str, image_files: List, 
                           original_filename: str, output_dir: str) -> List[Dict]:
        """
        从 markdown 中提取图片信息及其上下文
        
        Args:
            markdown_content: Markdown 内容
            image_files: 图片文件路径列表
            original_filename: 原始文件名
            output_dir: 输出目录
            
        Returns:
            图片信息列表，每个元素包含：
            - image_path: 图片绝对路径
            - image_name: 图片文件名
            - filename: 源文件名
            - page_number: 准确的页码（从MinerU的middle.json中提取）
            - context_before: 图片前的文本（100字符）
            - context_after: 图片后的文本（100字符）
            - section: 所在章节标题
        """
        import re
        import json
        
        images_info = []
        
        # 1. 从 middle.json 构建图片hash到页码的映射
        image_hash_to_page = self._build_image_page_mapping(output_dir)
        
        # 构建图片文件名到路径的映射
        image_name_to_path = {}
        for img_path in image_files:
            img_name = Path(img_path).name
            image_name_to_path[img_name] = str(img_path)
        
        # 使用正则表达式找到所有图片引用: ![...](images/xxx.jpg)
        image_pattern = r'!\[(.*?)\]\((.*?)\)'
        matches = list(re.finditer(image_pattern, markdown_content))
        
        # 按章节分割 markdown
        lines = markdown_content.split('\n')
        current_section = "未分类"
        
        for match in matches:
            alt_text = match.group(1)
            img_ref = match.group(2)  # 如: images/xxx.jpg
            
            # 提取图片文件名
            img_name = Path(img_ref).name
            
            # 查找实际图片路径
            img_full_path = image_name_to_path.get(img_name)
            if not img_full_path:
                # 尝试在输出目录中查找
                possible_path = Path(output_dir) / img_ref
                if possible_path.exists():
                    img_full_path = str(possible_path)
                else:
                    continue  # 图片不存在，跳过
            
            # 获取图片在 markdown 中的位置
            img_position = match.start()
            
            # 提取上下文（前后各100个字符）
            context_before = markdown_content[max(0, img_position-100):img_position].strip()
            context_after = markdown_content[img_position+len(match.group(0)):img_position+len(match.group(0))+100].strip()
            
            # 尝试找到所在章节（向前查找最近的标题）
            text_before_img = markdown_content[:img_position]
            section_matches = list(re.finditer(r'^#{1,6}\s+(.+)$', text_before_img, re.MULTILINE))
            if section_matches:
                current_section = section_matches[-1].group(1).strip()
            
            # 从映射中获取准确的页码（如果有的话）
            # 提取图片的hash部分（不含扩展名）
            img_hash = Path(img_name).stem
            accurate_page = image_hash_to_page.get(img_hash, None)
            
            # 如果没有找到准确页码，使用估算（向前查找，每10个双换行算一页）
            if accurate_page is None:
                accurate_page = len(text_before_img.split('\n\n')) // 10 + 1
            
            images_info.append({
                'image_path': img_full_path,
                'image_name': img_name,
                'filename': original_filename,
                'page_number': accurate_page,
                'context_before': context_before[-100:],  # 限制长度
                'context_after': context_after[:100],
                'context': context_before[-50:] + ' [图片] ' + context_after[:50],
                'section': current_section,
                'alt_text': alt_text,
            })
        
        return images_info
    
    def process_pdf(self, pdf_path: str, output_dir: str = None) -> str:
        """
        处理PDF文件，返回提取的文本
        
        Note: 这个方法只返回文本内容，如需图片信息请使用 process_file()
        
        Args:
            pdf_path: PDF文件路径
            output_dir: 输出目录
            
        Returns:
            提取的文本内容（markdown格式）
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
