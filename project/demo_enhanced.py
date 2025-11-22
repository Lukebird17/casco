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

RESULTS_FILE = "enhanced_demo_results.json"

def main():
    """主函数：演示增强版智能体的使用"""
    
    print("╔══════════════════════════════════════════════════════╗")
    print("║         增强版智能体 Demo                            ║")
    print("╚══════════════════════════════════════════════════════╝\n")
    
    # 1. 加载向量数据库
    print("📂 加载向量数据库...")
    vector_store = VectorStore()
    vector_store.load_vector('./trial_bge')
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
        "2024 年，株洲中车时代电气股份有限公司中标金额是多少？",
        "根据欧洲铁路局 2025-2027 年单一规划文件，机构注册系统迁移到知识图谱（knowledge graph）方法的目标进度在 2025 年底应达到多少百分比？",
        "在 UIC 的报告里，根据国际能源署的分析，铁路的市场份额需要增长多少才能在本十年内实现《巴黎协定》的目标?",
        "参照 IEEE 1474.1 的定义，附件 D (Typical safe braking model) 中对安全制动模型的描述，在'滑行时间 (Coast time, C)'期间，列车被假定处于什么状态？",
        "在 Manresa 车站的事件调查报告中，列车 78443 被授权越过 3023 进站信号机后，何时（日期和时间）发生了列车 95218 最终启动了行驶，并最终导致两列车存在碰撞风险？",
        
        "南京地铁 S7 号线的运营里程，在江苏省内已运营地铁长度中排第几？",
        "车辆外部移动实体的场景要素：根据 GB/T 43267—2023（预期功能安全），在场景要素结构中，可移动实体的第 2 层要素和第 3 层要素分别是什么？（需完整列出第 3 层中所有实体类型）。",
        "根据文档《2024_Communications-Based Train Control》，图 5.11 所示的网状控制回路结构，ATO 子系统是如何实现自身的控制回路的？请阐述其如何获取输入（Messglieder），如何形成车辆轨迹（Fahrzeugtrajektorie），以及如何将轨迹作为目标值传递给列车的控制设备（Steuergerät）。",

        "在 CBTC 互联互通规范体系中，关于列车启动、加速、巡航和制动的自动控制功能，其在《系统总体要求》中的分配归属于哪个子系统？并在《CBTC 部分测试及验证》中体现在哪个功能的测试中，测试需求编号是什么？",
        "ERTMS/ETCS 列车牵引系统数据定义演变： 比较 SUBSET-026 Baseline 3 (v3.4.0) 和 Baseline 4 (v4.0.0) 版本中 Validated Train Data (Packet 11) 的内容定义：1）请指出该数据包中用于表示牵引系统标识的变量名称？2）当该变量不为零时，需要包含哪些额外的牵引数据变量？",
        ]
    
    results = []
    start_index = 0

    # 尝试加载已有的结果，以便从断点恢复
    if os.path.exists(RESULTS_FILE):
        try:
            with open(RESULTS_FILE, 'r', encoding='utf-8') as f:
                results = json.load(f)
            print(f"✅ 已加载 {len(results)} 个历史结果，将从下一题继续。")
        except json.JSONDecodeError:
            print("⚠️ 历史结果文件损坏，将重新开始。")
            results = []
    
    # 从上次结束的位置开始处理新问题
    start_index = len(results)

    for i in range(start_index, len(test_questions)):
        question = test_questions[i]
        print(f"\n============================================================")
        print(f"问题 {i+1}: {question}")
        print(f"============================================================\n")
        full_result_text = None
        try:
            # 调用智能体，获取结果
            full_result_text = agent.query_with_full_features(question)
            
            # 存储当前问题的结果
            results.append({
                "question_id": i + 1,
                "question": question,
                "answer": full_result_text,
                "status": "Success"
            })
            
        except Exception as e:
            # 捕获错误，记录下来，并继续下一个问题
            print(f"❌ 问题 {i+1} 发生错误，无法获取答案: {e}")
            results.append({
                "question_id": i + 1,
                "question": question,
                "answer": None,
                "status": f"Error: {str(e)}"
            })
            
        finally:
            # ⚠️ 每次循环结束都保存结果（增量保存）
            with open(RESULTS_FILE, 'w', encoding='utf-8') as f:
                json.dump(results, f, ensure_ascii=False, indent=4)
            print(f"✅ 问题 {i+1} 的结果已保存到 {RESULTS_FILE}")

    print("\n\n所有问题处理完毕。")
    
    
    # for i, question in enumerate(test_questions, 1):
    #     print(f"\n{'='*60}")
    #     print(f"问题 {i}: {question}")
    #     print(f"{'='*60}\n")
        
    #     # 5. 执行查询（使用完整增强功能）
    #     result = agent.query_with_full_features(question)
        
    #     # 6. 显示答案
    #     print(f"\n✅ 答案:")
    #     print(f"{result['answer']}\n")
        
    #     # 7. 显示推理链（可选）
    #     if result.get('reasoning_chain'):
    #         print("\n" + "="*60)
    #         print("推理过程:")
    #         print("="*60)
    #         print(result['reasoning_chain'].format_chain(detailed=False))
        
    #     # 8. 显示Token使用情况
    #     if result.get('token_usage'):
    #         print(f"\n📊 本次查询Token消耗:")
    #         print(f"  • 总计: {result['token_usage']['total_tokens']:,} tokens")
        
    #     # 9. 格式化输出（符合竞赛要求）
    #     formatted_output = agent.format_output(result, include_reasoning=False)
    #     results.append(formatted_output)
        
    #     print("\n" + "="*60)
    
    # # 10. 保存结果
    # print("\n💾 保存结果...")
    # final_output = {"items": results}
    # with open('enhanced_demo_results.json', 'w', encoding='utf-8') as f:
    #     json.dump(final_output, f, ensure_ascii=False, indent=2) # 写入 final_output
    # print("✅ 结果已保存到: enhanced_demo_results.json\n")
    # ...
    # 11. 显示性能报告
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
    
    optimized = tracker.optimize_context(long_text, max_tokens=200)
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

