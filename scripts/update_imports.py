#!/usr/bin/env python3
"""
自动更新import路径的脚本
"""
import os
import re

# 定义需要更新的文件和对应的import映射
IMPORT_MAPPINGS = {
    # 核心模块
    'from vector_store import': 'from src.core.vector_store import',
    'from hybrid_retriever import': 'from src.core.hybrid_retriever import',
    'from reranker import': 'from src.core.reranker import',
    'from image_vector_store import': 'from src.core.image_vector_store import',
    'from rag_agent import': 'from src.core.rag_agent import',
    
    # 处理器
    'from document_loader import': 'from src.processors.document_loader import',
    'from text_splitter import': 'from src.processors.text_splitter import',
    'from enhanced_ocr import': 'from src.processors.enhanced_ocr import',
    'from image_describer import': 'from src.processors.image_describer import',
    
    # 评估器
    'from quality_evaluator import': 'from src.evaluators.quality_evaluator import',
    'from quality_evaluator_advanced import': 'from src.evaluators.quality_evaluator_advanced import',
    'from confidence_calculator import': 'from src.evaluators.confidence_calculator import',
    
    # 功能模块
    'from knowledge_graph import': 'from src.features.knowledge_graph import',
    'from knowledge_graph_llamaindex import': 'from src.features.knowledge_graph_llamaindex import',
    'from flashcard_system import': 'from src.features.flashcard_system import',
    'from socratic_mode import': 'from src.features.socratic_mode import',
    'from reasoning_chain import': 'from src.features.reasoning_chain import',
    'from auto_cot_prompting import': 'from src.features.auto_cot_prompting import',
    'from quiz_generator import': 'from src.features.quiz_generator import',
    
    # 工具
    'from session_manager import': 'from src.utils.session_manager import',
    'from token_tracker import': 'from src.utils.token_tracker import',
    'from dynamic_db_manager import': 'from src.utils.dynamic_db_manager import',
    'from multimodal_input_handler import': 'from src.utils.multimodal_input_handler import',
    'from snippet_manager import': 'from src.utils.snippet_manager import',
}

def update_imports_in_file(filepath):
    """更新单个文件的import"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 应用所有import映射
        for old_import, new_import in IMPORT_MAPPINGS.items():
            content = content.replace(old_import, new_import)
        
        # 如果有变化，写回文件
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"  ❌ 更新失败 {filepath}: {e}")
        return False

def main():
    """主函数"""
    print("🔄 开始更新import路径...")
    
    # 需要更新的目录
    directories_to_update = [
        'src/core',
        'src/processors',
        'src/evaluators',
        'src/features',
        'src/utils',
    ]
    
    updated_files = []
    
    for directory in directories_to_update:
        if not os.path.exists(directory):
            continue
            
        for filename in os.listdir(directory):
            if filename.endswith('.py') and filename != '__init__.py':
                filepath = os.path.join(directory, filename)
                if update_imports_in_file(filepath):
                    updated_files.append(filepath)
                    print(f"  ✅ 更新 {filepath}")
    
    print(f"\n✅ 完成！共更新 {len(updated_files)} 个文件")
    
    if updated_files:
        print("\n更新的文件列表：")
        for filepath in updated_files:
            print(f"  - {filepath}")

if __name__ == '__main__':
    main()

