#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   demo_enhanced.py
@Time    :   2025/11/16
@Desc    :   增强版智能体使用示例
'''

from VectorBase import VectorStore
from LLM import OpenAIChat
from my_BGE_embedding import BGEEmbedding  # 导入你刚写好的BGE类
from enhanced_agent import EnhancedRAGAgent
import json
import os
import numpy as np

RESULTS_FILE = "enhanced_demo_results.json"

def convert(o):
    if isinstance(o, np.float32) or isinstance(o, np.float64):
        return float(o)
    if isinstance(o, np.int32) or isinstance(o, np.int64):
        return int(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    raise TypeError(f"Object of type {type(o).__name__} is not JSON serializable")

def main():
    """主函数：演示增强版智能体的使用"""
    
    print("╔══════════════════════════════════════════════════════╗")
    print("║         增强版智能体 Demo                            ║")
    print("╚══════════════════════════════════════════════════════╝\n")
    
    # 1. 加载向量数据库
    print("📂 加载向量数据库...")
    vector_store = VectorStore()
    vector_store.load_vector('./storage_bge_hierarchical')
    print(f"✅ 加载完成，文档数量: {len(vector_store.document)}\n")
    
    # 2. 初始化模型
    print("🤖 初始化模型...")
    embedding = BGEEmbedding()
    llm = OpenAIChat()
    print("✅ 模型初始化完成\n")
    
    # 3. 创建增强版智能体
    print("🚀 创建增强版智能体...")
    agent = EnhancedRAGAgent(
        vector_store=vector_store,
        llm=llm,
        embedding=embedding,
        enable_tracking=True  # 启用Token追踪
    )
    print("✅ 智能体创建完成\n")
    
    # 4. 测试问题
    test_questions = [
        "根据 GB/T 43267—2023（预期功能安全），在场景要素结构中，可移动实体的第 2 层要素和第 3 层要素分别是什么？（需完整列出第 3 层中所有实体类型）"
        ]
    
    results = []
    if test_questions:
        question = test_questions[0]
        print(f"\n============================================================")
        print(f"问题: {question}")
        print(f"============================================================\n")
        
        try:
            # 调用智能体，获取结果
            full_result_text = agent.query_with_full_features(question)
            
            # 存储当前问题的结果
            results.append({
                "question_id": 1,  # 固定ID为1
                "question": question,
                "answer": full_result_text,
                "status": "Success"
            })
            print(f"✅ 问题处理成功。")
            
        except Exception as e:
            # 捕获错误，记录下来
            print(f"❌ 问题发生错误，无法获取答案: {e}")
            results.append({
                "question_id": 1,  # 固定ID为1
                "question": question,
                "answer": None,
                "status": f"Error: {str(e)}"
            })
            
        finally:
            # 新增/修改：处理完毕后保存结果
            with open(RESULTS_FILE, 'w', encoding='utf-8') as f:
                json.dump(results, f, ensure_ascii=False, indent=4, default=convert)
            print(f"✅ 结果已保存到 {RESULTS_FILE}")

    print("\n所有问题处理完毕。")
    print("\n\n所有问题处理完毕。")
    
    
    print("\n" + "="*60)
    print("性能报告")
    print("="*60)
    print(agent.get_performance_report())
    
    # 12. 保存详细报告
    print("\n💾 保存详细报告...")
    agent.save_reports(output_dir='enhanced_reports')
    
    print("\n✅ Demo完成！")


def demo_advanced_features():
    """演示高级功能"""
    print("\n\n╔══════════════════════════════════════════════════════╗")
    print("║         高级功能演示                                  ║")
    print("╚══════════════════════════════════════════════════════╝\n")
    
    # 演示1：Token优化
    print("【功能1：Token优化】")
    from token_tracker import TokenTracker
    
    tracker = TokenTracker()
    long_text = "这是一段很长的文本。\n" * 500
    print(f"原始文本: {len(long_text)} 字符, {tracker.count_tokens(long_text)} tokens")
    
    optimized = tracker.optimize_context(long_text, max_tokens=30000)
    # optimized = tracker.optimize_context(long_text, max_tokens=200)
    print(f"优化后: {len(optimized)} 字符, {tracker.count_tokens(optimized)} tokens")
    print(f"节省: {len(long_text) - len(optimized)} 字符\n")
    
    # 演示2：推理链
    print("【功能2：推理链记录】")
    from reasoning_chain import ReasoningChain
    
    chain = ReasoningChain("测试问题")
    chain.add_analysis_step("分析问题类型")
    chain.add_retrieval_step("检索相关文档")
    chain.add_inference_step("进行逻辑推理", confidence=0.9)
    chain.add_conclusion_step("得出结论")
    
    print(chain.format_compact())
    print()
    
    # 演示3：表格提取
    print("【功能3：表格提取】")
    from advanced_document_processor import AdvancedTableExtractor
    
    extractor = AdvancedTableExtractor()
    print("表格提取器已初始化")
    print("支持pdfplumber和PyMuPDF两种方法\n")
    
    # 演示4：版本对比
    print("【功能4：版本对比】")
    from advanced_document_processor import VersionComparator
    
    comparator = VersionComparator()
    doc1 = "版本1的内容\n包含功能A\n包含功能B"
    doc2 = "版本2的内容\n包含功能A\n包含功能B\n新增功能C"
    
    comparison = comparator.compare_documents(doc1, doc2)
    print(f"相似度: {comparison['similarity_ratio']:.1%}")
    print(f"新增: {comparison['added_lines']}行")
    print(f"删除: {comparison['removed_lines']}行\n")


if __name__ == "__main__":
    try:
        # 运行主Demo
        main()
        
        # 运行高级功能演示
        demo_advanced_features()
        
    except Exception as e:
        print(f"\n❌ 发生错误: {e}")
        print("\n提示：请确保:")
        print("1. .env文件配置正确")
        print("2. 向量数据库已构建 (./storage_demo)")
        print("3. 所有依赖已安装")
        import traceback
        traceback.print_exc()

