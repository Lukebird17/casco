#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
简化版OCR系统 - 充分利用PaddleOCR 3.0原生能力
"""

import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

import cv2
import numpy as np
from typing import Dict, List
from PIL import Image
import io
import fitz
import json


class SimpleOCRSystem:
    """简化版OCR系统 - 支持本地引擎和Gradio在线API"""
    
    _instance = None
    _initialized = False
    
    # 在线API配置（Gradio应用）
    API_URL = os.getenv('PADDLEOCR_API_URL', '')
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, use_api: bool = True):
        """
        初始化OCR系统 - 仅支持Gradio API模式
        
        Args:
            use_api: 是否使用在线API（固定为True，保留参数仅为兼容性）
        """
        if SimpleOCRSystem._initialized:
            return
        
        print("🚀 初始化简化版OCR系统...")
        
        # 检查API配置
        if not self.API_URL:
            raise ValueError("❌ API_URL未配置！请设置环境变量 PADDLEOCR_API_URL")
        
        print(f"  🌐 使用Gradio在线API模式")
        print(f"  📍 API地址: {self.API_URL}")
        
        try:
            from gradio_client import Client
            self.gradio_client = Client(self.API_URL)
            print(f"  ✅ Gradio客户端初始化成功")
        except ImportError:
            raise ImportError("  ❌ gradio_client未安装！请运行: pip install gradio_client")
        except Exception as e:
            raise RuntimeError(f"  ❌ Gradio客户端初始化失败: {e}")
        
        self.use_api = True
        self.ocr = None  # API模式不需要本地引擎
        
        SimpleOCRSystem._initialized = True
        print("✅ OCR系统初始化完成")
    
    # 移除本地引擎初始化 - 仅使用API模式
    
    def process_document(self, pdf_path: str, 
                   use_structure_analysis: bool = True,
                   extract_toc: bool = True) -> Dict:
        """
        处理PDF文档 - 使用Gradio API
        
        Args:
            pdf_path: PDF文件路径
            use_structure_analysis: 是否使用结构分析（版面分析+表格识别）- API自动支持
            extract_toc: 是否提取目录
        
        Returns:
            处理结果字典
        
        """
        print(f"\n{'='*60}")
        print(f"处理文档: {os.path.basename(pdf_path)}")
        print(f"{'='*60}\n")
        
        # 仅使用API模式
        return self._process_with_api(pdf_path, extract_toc)
    
    def _process_with_api(self, pdf_path: str, extract_toc: bool) -> Dict:
        """使用Gradio在线API处理文档（并行处理多页）"""
        from gradio_client import handle_file
        import tempfile
        from concurrent.futures import ThreadPoolExecutor, as_completed
        
        print("🌐 使用Gradio API处理...")
        print(f"  📄 文件: {pdf_path}")
        
        # 创建输出目录
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
        
        # 创建临时目录存放转换的图片
        temp_dir = tempfile.mkdtemp(prefix="pdf2img_")
        
        try:
            # 第1步：将PDF转换为图片
            print(f"  🔄 将PDF转换为图片...")
            doc = fitz.open(pdf_path)
            total_pages = len(doc)
            print(f"  📄 共 {total_pages} 页")
            
            base_name = os.path.splitext(os.path.basename(pdf_path))[0]
            img_paths = []
            
            # 先转换所有页面为图片
            for page_num in range(total_pages):
                page = doc[page_num]
                pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # 2倍缩放提高质量
                img_path = os.path.join(temp_dir, f"page_{page_num + 1}.png")
                pix.save(img_path)
                img_paths.append((page_num + 1, img_path))
            
            doc.close()
            print(f"  ✅ 图片转换完成")
            
            # 第2步：并行调用API处理所有图片
            print(f"  🚀 并行处理 {total_pages} 页（最多同时 {min(total_pages, 5)} 个请求）...")
            
            def process_page(page_info):
                """处理单个页面的函数"""
                page_num, img_path = page_info
                try:
                    result = self.gradio_client.predict(
                        fp=handle_file(img_path),
                        use_chart=True,         # 启用图表解析
                        use_unwarping=True,     # 启用文档矫正
                        use_orientation=True,   # 启用方向分类
                        api_name="/parse_doc_router"
                    )
                    
                    # result是一个元组：(markdown_content, visualization_html, markdown_source)
                    markdown_content = result[0]
                    markdown_source = result[2]
                    text = markdown_content if markdown_content else markdown_source
                    
                    return {
                        'page_number': page_num,
                        'text': text,
                        'has_markdown': True,
                        'api_processed': True,
                        'success': True
                    }
                    
                except Exception as e:
                    return {
                        'page_number': page_num,
                        'text': '',
                        'has_markdown': False,
                        'api_processed': False,
                        'error': str(e),
                        'success': False
                    }
            
            # 使用线程池并行处理
            all_pages_text = [None] * total_pages  # 预分配列表
            max_workers = min(5, total_pages)  # 最多5个并发请求，避免过载
            
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                # 提交所有任务
                future_to_page = {executor.submit(process_page, page_info): page_info for page_info in img_paths}
                
                # 处理完成的任务
                completed = 0
                for future in as_completed(future_to_page):
                    result = future.result()
                    page_num = result['page_number']
                    all_pages_text[page_num - 1] = result  # 按页码顺序存储
                    
                    completed += 1
                    status = "✅" if result['success'] else "⚠️"
                    print(f"    {status} 第 {page_num}/{total_pages} 页完成 ({completed}/{total_pages})")
            
            print(f"  ✅ 所有页面处理完成")
            
            # 合并所有页面的文本
            combined_text = "\n\n---\n\n".join([p['text'] for p in all_pages_text if p['text']])
            
            # 保存合并的Markdown
            md_filename = os.path.join(output_dir, f"{base_name}.md")
            with open(md_filename, "w", encoding="utf-8") as f:
                f.write(combined_text)
            print(f"  💾 Markdown已保存: {md_filename}")
            
            # 提取目录（从本地PDF元数据）
            toc = []
            if extract_toc:
                try:
                    doc = fitz.open(pdf_path)
                    toc_raw = doc.get_toc()
                    if toc_raw:
                        toc = [{'level': item[0], 'title': item[1], 'page': item[2]} for item in toc_raw]
                        print(f"  📑 提取到 {len(toc)} 个目录项")
                    doc.close()
                except Exception as e:
                    print(f"  ⚠️  目录提取失败: {e}")
            
            print(f"\n✅ Gradio API处理完成！")
            print(f"  📊 共处理 {total_pages} 页")
            print(f"  📁 输出目录: {output_dir}")
            # print("process_api",all_pages_text)
            return {
                'file_name': os.path.basename(pdf_path),
                'total_pages': total_pages,
                'toc': toc,
                'pages': all_pages_text,
                'output_dir': output_dir,
                'api_processed': True,
                'combined_markdown': md_filename
            }
            
        except Exception as e:
            print(f"❌ Gradio API处理失败: {e}")
            print(f"  💡 提示：API可能只支持图片格式")
            raise
        finally:
            # 清理临时文件
            import shutil
            try:
                shutil.rmtree(temp_dir)
            except:
                pass
    
    def _process_with_local(self, pdf_path: str, use_structure_analysis: bool = True, extract_toc: bool = True) -> Dict:
        """本地处理方法已移除 - 仅支持API模式"""
        raise NotImplementedError("本地处理模式已移除，仅支持Gradio API模式。请配置PADDLEOCR_API_URL环境变量。")
    
    def _process_with_local_removed(self, pdf_path: str, use_structure_analysis: bool, extract_toc: bool) -> Dict:
        """使用本地引擎处理文档"""
        print("💻 使用本地引擎处理...")
        
        doc = fitz.open(pdf_path)
        results = {
            'file_name': os.path.basename(pdf_path),
            'total_pages': len(doc),
            'toc': [],
            'pages': []
        }
        
        # 1. 提取目录（来自PDF元数据）
        if extract_toc:
            toc = doc.get_toc()
            if toc:
                print(f"📑 提取到 {len(toc)} 个目录项")
                results['toc'] = [
                    {'level': item[0], 'title': item[1], 'page': item[2]}
                    for item in toc
                ]
        
        # 2. 逐页处理
        for page_num in range(len(doc)):
            print(f"\n处理第 {page_num + 1}/{len(doc)} 页...")
            page = doc[page_num]
            
            # 转为图像
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
            img_data = pix.tobytes("png")
            
            # 保存临时文件
            import tempfile
            with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
                tmp_path = tmp.name
                tmp.write(img_data)
            
            page_result = {
                'page_number': page_num + 1,
                'text': '',
                'tables': [],
                'layout': []
            }
            
            # 3. 使用PPStructureV3进行文档结构分析
            if use_structure_analysis and self.structure:
                try:
                    print("  📄 PPStructureV3分析文档结构...")
                    structure_result = self.structure.predict(input=tmp_path)
                    
                    text_parts = []
                    table_count = 0
                    
                    for res in structure_result:
                        # 保存markdown格式（包含表格和文本）
                        if hasattr(res, 'save_to_markdown'):
                            md_dir = f"output/page_{page_num + 1}"
                            os.makedirs(md_dir, exist_ok=True)
                            res.save_to_markdown(save_path=md_dir)
                        
                        # 提取文本
                        text = self._extract_text_from_result(res)
                        if text:
                            text_parts.append(text)
                        
                        # 统计表格
                        if hasattr(res, 'layout_parsing_result'):
                            layout = res.layout_parsing_result
                            if 'table' in str(layout).lower():
                                table_count += 1
                    
                    page_result['text'] = '\n'.join(text_parts)
                    
                    if table_count > 0:
                        print(f"  ✅ 检测到 {table_count} 个表格")
                        page_result['tables'].append({'count': table_count, 'markdown_dir': md_dir})
                    
                    print(f"  ✅ 提取文本内容")
                
                except Exception as e:
                    print(f"  ⚠️  结构分析失败: {e}")
                    import traceback
                    traceback.print_exc()
            
            # 删除临时文件
            try:
                os.unlink(tmp_path)
            except:
                pass
            
            results['pages'].append(page_result)
        
        doc.close()
        
        print(f"\n{'='*60}")
        print(f"处理完成！")
        print(f"{'='*60}\n")
        
        return results
    
    def _extract_text_from_result(self, result):
        """从PaddleOCR结果对象中提取文本"""
        try:
            # 方法1: 直接获取text属性
            if hasattr(result, 'text'):
                return result.text
            
            # 方法2: 从ocr_result属性获取
            if hasattr(result, 'ocr_result'):
                ocr_res = result.ocr_result
                if isinstance(ocr_res, list):
                    return '\n'.join([str(item) for item in ocr_res])
            
            # 方法3: 转字符串
            return str(result)
        except:
            return ""
    
    def export_results(self, results: Dict, output_path: str = None):
        """导出结果"""
        if output_path is None:
            output_path = f"output/{results['file_name']}_ocr.json"
        
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # 保存JSON
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"✅ JSON结果: {output_path}")
        
        # 保存文本版本
        txt_path = output_path.replace('.json', '.txt')
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(f"文档: {results['file_name']}\n")
            f.write(f"总页数: {results['total_pages']}\n")
            f.write("="*60 + "\n\n")
            
            # 目录
            if results['toc']:
                f.write("## 目录\n\n")
                for item in results['toc']:
                    indent = "  " * (item['level'] - 1)
                    f.write(f"{indent}- {item['title']} (第{item['page']}页)\n")
                f.write("\n" + "="*60 + "\n\n")
            
            # 页面内容
            for page in results['pages']:
                f.write(f"\n第 {page['page_number']} 页\n")
                f.write("-"*60 + "\n")
                
                if page['tables']:
                    f.write(f"[检测到 {len(page['tables'])} 个表格]\n\n")
                
                f.write(page['text'] + '\n\n')
        
        print(f"✅ 文本结果: {txt_path}")



if __name__ == "__main__":
    print("="*60)
    print("简化版OCR系统 - 基于PPStructureV3")
    print("="*60)
    print("\n✨ 核心技术：PPStructureV3")
    print("   - 文档结构分析（版面布局识别）")
    print("   - 表格识别（含合并单元格）")
    print("   - 文本OCR识别（多语言）")
    print("   - 自动方向检测和纠正")
    print("   - 自动文档畸变矫正")
    print("\n📋 功能特性:")
    print("  ✅ 多语言识别（中英文、繁体等）")
    print("  ✅ 版面分析（标题、段落、表格、图片）")
    print("  ✅ 表格结构识别（含合并单元格）")
    print("  ✅ 方向检测和纠正")
    print("  ✅ 文档畸变矫正")
    print("  ✅ 目录提取（PDF元数据）")
    print("  ✅ 输出Markdown格式")
    print("\n📝 使用示例:")
    print("""
from simple_ocr_system import SimpleOCRSystem

# 初始化（只需一次）
ocr = SimpleOCRSystem()

# 处理文档
results = ocr.process_document(
    'document.pdf',
    use_structure_analysis=True,  # 使用结构分析
    extract_toc=True              # 提取目录
)

# 导出结果
ocr.export_results(results)

# 结果包含：
# - 文本内容
# - 表格（Markdown格式）
# - 版面结构
# - 目录信息
""")

