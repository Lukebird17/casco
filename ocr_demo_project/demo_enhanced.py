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
REASONING_LOG_FILE = "reasoning_log.txt"

def convert(o):
    if isinstance(o, np.float32) or isinstance(o, np.float64):
        return float(o)
    if isinstance(o, np.int32) or isinstance(o, np.int64):
        return int(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    raise TypeError(f"Object of type {type(o).__name__} is not JSON serializable")

def init_output_files():
    """初始化输出文件：强制覆盖旧文件，写入初始结构"""
    print("🧹 初始化输出文件...")
    
    # 1. 强制重置 JSON 文件为正确的字典结构
    initial_json = {"items": []}
    with open(RESULTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(initial_json, f, ensure_ascii=False, indent=4)
    
    # 2. 强制重置 日志文件
    with open(REASONING_LOG_FILE, 'w', encoding='utf-8') as f:
        f.write("=== 增强版智能体 推理链日志 ===\n")
        f.write("说明：此文件记录Agent的内部执行步骤。\n\n")

def save_result_incrementally(item: dict):
    """
    实时保存单个结果到JSON文件
    逻辑：读取 -> 校验 -> 追加 -> 回写
    """
    try:
        # 1. 读取现有内容
        if os.path.exists(RESULTS_FILE):
            with open(RESULTS_FILE, 'r', encoding='utf-8') as f:
                try:
                    current_data = json.load(f)
                except json.JSONDecodeError:
                    current_data = {"items": []} # 文件损坏则重置
        else:
            current_data = {"items": []}

        # 2. 关键修复：如果读出来是列表（旧格式），强制转为字典
        if isinstance(current_data, list):
            print("⚠️ 检测到旧格式数据，正在修正结构...")
            current_data = {"items": current_data}

        # 3. 追加新条目
        if "items" not in current_data:
            current_data["items"] = []
        current_data["items"].append(item)
        
        # 4. 回写整个文件
        with open(RESULTS_FILE, 'w', encoding='utf-8') as f:
            json.dump(current_data, f, ensure_ascii=False, indent=4, default=convert)
            
    except Exception as e:
        print(f"❌ 保存结果到JSON失败: {e}")

def save_reasoning_incrementally(query: str, reasoning_content: str):
    """实时追加推理日志"""
    try:
        with open(REASONING_LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(f"【时间】: {query}\n") # 这里用 query 标识段落
            f.write(f"{'-'*30}\n")
            f.write(reasoning_content)
            f.write(f"\n{'='*60}\n\n")
    except Exception as e:
        print(f"❌ 保存推理日志失败: {e}")

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
        "R2DATO项目D13.1可交付成果的安全分析部分（Part 3）采用了哪种专注于'不安全控制行为'（UCA）的新型分析方法？该方法的结果与D13.1的系统规格部分（Part 2）在哪个工作包（WP）中得到了持续跟进和更新？"
        ]
    
    if test_questions:
        for idx, question in enumerate(test_questions):
            print(f"\n============================================================")
            print(f"正在处理第{idx+1}/{len(test_questions)} 题: {question}")
            print(f"============================================================\n")
            # 构建符合模板的结果项
            item = {
                "question": question,
                "retrieved_contexts": [],
                "answer": ""
            }
            try:
                # 调用智能体，获取结果
                result_dict = agent.query_with_full_features(question)
                # 1. 提取上下文纯文本 (符合 items[].retrieved_contexts 格式)
                contexts = [res['content'] for res in result_dict.get('results', [])]
                
                # 2. 填充结果项
                item["retrieved_contexts"] = contexts
                item["answer"] = result_dict.get('answer', "未生成答案")
                
                # 3. 实时保存数据 (JSON)
                save_result_incrementally(item)
                
                # 4. 实时保存推理链 (TXT)
                reasoning_txt = result_dict.get('reasoning_chain', "无推理链记录")
                save_reasoning_incrementally(question, reasoning_txt)
                
                print(f"✅ 第 {idx+1} 题已完成并保存。")
                
            except Exception as e:
                print(f"❌ 第 {idx+1} 题处理出错: {e}")
                # 即使出错，也保存报错信息，防止序位错乱
                item["answer"] = f"Error during processing: {str(e)}"
                save_result_incrementally(item)
                

    print("\n" + "="*60)
    print(f"🎉 所有任务完成！")
    print(f"📂 结果文件: {RESULTS_FILE}")
    print(f"📂 推理日志: {REASONING_LOG_FILE}")
    print("="*60)
    
    
    # print("\n" + "="*60)
    # print("性能报告")
    # print("="*60)
    # === 新增功能：获取性能报告并保存到推理链文件末尾 ===
    try:
        report = agent.get_performance_report()
        
        # 1. 打印到终端
        print(report)
        
        # 2. 追加到日志文件
        with open(REASONING_LOG_FILE, 'a', encoding='utf-8') as f:
            f.write("\n\n")  # 增加一些空行
            f.write(report)
            f.write("\n")
            
        print(f"✅ 性能报告已追加保存到 {REASONING_LOG_FILE}")
        
    except Exception as e:
        print(f"❌ 保存性能报告时发生错误: {e}")
    
    # # 12. 保存详细报告
    # print("\n💾 保存详细报告...")
    # agent.save_reports(output_dir='enhanced_reports')
    
    # print("\n✅ Demo完成！")


# def demo_advanced_features():
#     """演示高级功能"""
#     print("\n\n╔══════════════════════════════════════════════════════╗")
#     print("║         高级功能演示                                  ║")
#     print("╚══════════════════════════════════════════════════════╝\n")
    
#     # 演示1：Token优化
#     print("【功能1：Token优化】")
#     from token_tracker import TokenTracker
    
#     tracker = TokenTracker()
#     long_text = "这是一段很长的文本。\n" * 500
#     print(f"原始文本: {len(long_text)} 字符, {tracker.count_tokens(long_text)} tokens")
    
#     optimized = tracker.optimize_context(long_text, max_tokens=30000)
#     # optimized = tracker.optimize_context(long_text, max_tokens=200)
#     print(f"优化后: {len(optimized)} 字符, {tracker.count_tokens(optimized)} tokens")
#     print(f"节省: {len(long_text) - len(optimized)} 字符\n")
    
#     # 演示2：推理链
#     print("【功能2：推理链记录】")
#     from reasoning_chain import ReasoningChain
    
#     chain = ReasoningChain("测试问题")
#     chain.add_analysis_step("分析问题类型")
#     chain.add_retrieval_step("检索相关文档")
#     chain.add_inference_step("进行逻辑推理", confidence=0.9)
#     chain.add_conclusion_step("得出结论")
    
#     print(chain.format_compact())
#     print()
    
#     # 演示3：表格提取
#     print("【功能3：表格提取】")
#     from advanced_document_processor import AdvancedTableExtractor
    
#     extractor = AdvancedTableExtractor()
#     print("表格提取器已初始化")
#     print("支持pdfplumber和PyMuPDF两种方法\n")
    
#     # 演示4：版本对比
#     print("【功能4：版本对比】")
#     from advanced_document_processor import VersionComparator
    
#     comparator = VersionComparator()
#     doc1 = "版本1的内容\n包含功能A\n包含功能B"
#     doc2 = "版本2的内容\n包含功能A\n包含功能B\n新增功能C"
    
#     comparison = comparator.compare_documents(doc1, doc2)
#     print(f"相似度: {comparison['similarity_ratio']:.1%}")
#     print(f"新增: {comparison['added_lines']}行")
#     print(f"删除: {comparison['removed_lines']}行\n")


if __name__ == "__main__":
    try:
        # 运行主Demo
        main()
        
        # 运行高级功能演示
        #demo_advanced_features()
        
    except Exception as e:
        print(f"\n❌ 发生错误: {e}")
        print("\n提示：请确保:")
        print("1. .env文件配置正确")
        print("2. 向量数据库已构建 (./storage_demo)")
        print("3. 所有依赖已安装")
        import traceback
        traceback.print_exc()

