#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
langchain兼容性补丁
用于解决PaddleX与新版本langchain的兼容性问题
"""

import sys
from types import ModuleType

# 创建虚拟的langchain.docstore模块
if 'langchain.docstore' not in sys.modules:
    docstore_module = ModuleType('langchain.docstore')
    document_module = ModuleType('langchain.docstore.document')
    
    # 从langchain_core导入Document类
    try:
        from langchain_core.documents import Document
        document_module.Document = Document
    except ImportError:
        # 如果langchain_core不可用，创建一个简单的占位符
        class Document:
            def __init__(self, page_content='', metadata=None):
                self.page_content = page_content
                self.metadata = metadata or {}
        document_module.Document = Document
    
    docstore_module.document = document_module
    sys.modules['langchain.docstore'] = docstore_module
    sys.modules['langchain.docstore.document'] = document_module

print("✅ langchain兼容性补丁已加载")





