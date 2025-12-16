#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
测试MinerU在Proj2框架中的集成
"""

import os
from pathlib import Path
from document_loader import DocumentLoader


def test_mineru_integration():
    """测试MinerU集成"""
    print("\n" + "="*60)
    print("测试 MinerU 在 Proj2 框架中的集成")
    print("="*60 + "\n")
    
    # 初始化DocumentLoader
    loader = DocumentLoader()
    
    # 查找测试文件
    data_dir = "data"
    test_files = []
    
    print("🔍 搜索测试文件...\n")
    
    for ext in ['.pdf', '.pptx', '.docx']:
        files = list(Path(data_dir).rglob(f'*{ext}'))
        if files:
            test_files.append(files[0])  # 取第一个文件
            print(f"   找到 {ext}: {files[0]}")
    
    if not test_files:
        print("❌ 没有找到测试文件")
        return
    
    print(f"\n📋 将测试 {len(test_files)} 个文件\n")
    
    # 测试每个文件
    for i, file_path in enumerate(test_files, 1):
        print(f"\n{'='*60}")
        print(f"测试 {i}/{len(test_files)}: {file_path.name}")
        print('='*60)
        
        try:
            # 使用DocumentLoader加载文件
            documents = loader.load_document(str(file_path))
            
            if documents:
                print(f"✅ 成功加载 {len(documents)} 个文档块")
                
                # 显示第一个文档块的预览
                if documents[0]['content']:
                    preview = documents[0]['content'][:300]
                    print(f"\n📄 内容预览:")
                    print(f"{preview}...")
                    print(f"\n📊 文档信息:")
                    print(f"   - 文件名: {documents[0]['filename']}")
                    print(f"   - 文件类型: {documents[0]['filetype']}")
                    print(f"   - 内容长度: {len(documents[0]['content'])} 字符")
            else:
                print(f"⚠️  加载失败，未返回文档")
                
        except Exception as e:
            print(f"❌ 处理失败: {e}")
            import traceback
            traceback.print_exc()
    
    print(f"\n{'='*60}")
    print("✅ 测试完成！")
    print('='*60 + "\n")


if __name__ == "__main__":
    test_mineru_integration()

