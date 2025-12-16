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
import time

RESULTS_FILE = "./output/answers_and_contexts.json"
PERFORMANCE_FILE = "./output/performance.json"

def convert(o):
    if isinstance(o, np.float32) or isinstance(o, np.float64):
        return float(o)
    if isinstance(o, np.int32) or isinstance(o, np.int64):
        return int(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    raise TypeError(f"Object of type {type(o).__name__} is not JSON serializable")

def _estimate_tokens(text):
    """
    估算文本的token数量
    使用tiktoken库（OpenAI官方token计数器）
    如果tiktoken不可用，则使用简单估算方法
    """
    try:
        import tiktoken
        # 使用gpt-3.5-turbo的编码器
        encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
        return len(encoding.encode(text))
    except:
        # 如果tiktoken不可用，使用简单估算：
        # 中文约1.5字符/token，英文约4字符/token
        # 这里采用混合估算
        chinese_chars = sum(1 for c in text if '\u4e00' <= c <= '\u9fff')
        other_chars = len(text) - chinese_chars
        estimated_tokens = int(chinese_chars / 1.5 + other_chars / 4)
        return estimated_tokens

def main():
    """主函数：演示增强版智能体的使用"""
    
    print("╔══════════════════════════════════════════════════════╗")
    print("║         增强版智能体 Demo                            ║")
    print("╚══════════════════════════════════════════════════════╝\n")
    
    # 1. 加载向量数据库
    print("📂 加载向量数据库...")
    vector_store = VectorStore()
    vector_store.load_vector('./storage')

    vector_text = VectorStore()
    vector_image = VectorStore()
    vector_table = VectorStore()

    vector_text.load_vector('./storage')
    vector_image.load_vector('./storage_graph')
    vector_table.load_vector('./storage_table_gxt')

    # vector_store = VectorStore()
    # vector_store.document = (
    #     vector_text.document +
    #     vector_image.document +
    #     vector_table.document
    # )

    print(f"✅ 加载完成，文档数量: {len(vector_store.document)}\n")
    
    # 2. 初始化模型
    print("🤖 初始化模型...")
    embedding = BGEEmbedding()
    llm = OpenAIChat()
    print("✅ 模型初始化完成\n")
    
    # 3. 创建增强版智能体
    print("🚀 创建增强版智能体...")
    agent = EnhancedRAGAgent(
        vector_store=[vector_text, vector_image, vector_table],
        llm=llm,
        embedding=embedding,
        enable_tracking=True  # 启用Token追踪
    )

    print("✅ 智能体创建完成\n")
    
    

    test_questions = [
        {
            "question": "2024 年，株洲中车时代电气股份有限公司中标金额是多少？",
            "type": "basic"
        },
        {
            "question": "根据欧洲铁路局 2025-2027 年单一规划文件，机构注册系统迁移到知识图谱（knowledge graph）方法的目标进度在 2025 年底应达到多少百分比？",
            "type": "basic"
        },
        {
            "question": "在 UIC 的报告里，根据国际能源署的分析，铁路的市场份额需要增长多少才能在本十年内实现《巴黎协定》的目标",
            "type": "basic"
        },
        {
            "question": "参照 IEEE 1474.1 的定义，附件 D (Typical safe braking model) 中对安全制动模型的描述，在“滑行时间 (Coast time, C)”期间，列车被假定处于什么状态？",
            "type": "basic"
        },
        {
            "question": "在 Manresa 车站的事件调查报告中，列车 78443 被授权越过 3023 进站信号机后，何时（日期和时间）发生了列车 95218 最终启动了行驶，并最终导致两列车存在碰撞风险？",
            "type": "basic"
        },
        {
    
            "question": "南京地铁 S7 号线的运营里程，在江苏省内已运营地铁长度中排第几？",
            "type": "advanced"
        },
        {
    
            "question": "车辆外部移动实体的场景要素：根据 GB/T 43267—2023（预期功能安全），在场景要素结构中，可移动实体的第 2 层要素和第 3 层要素分别是什么？（需完整列出第 3 层中所有实体类型）。",
            "type": "basic"
        },
        {
    
            "question": "根据文档《2024_Communications-Based Train Control》，图 5.11 所示的网状控制回路结构，ATO 子系统是如何实现自身的控制回路的？请阐述其如何获取输入（Messglieder），如何形成车辆轨迹（Fahrzeugtrajektorie），以及如何将轨迹作为目标值传递给列车的控制设备（Steuergerät）。",
            "type": "advanced"
        },
        {
    
            "question": "在 CBTC 互联互通规范体系中，关于列车启动、加速、巡航和制动的自动控制功能，其在《系统总体要求》中的分配归属于哪个子系统？并在《CBTC 部分测试及验证》中体现在哪个功能的测试中，测试需求编号是什么？",
            "type": "advanced"
        },
        {
            "question": "ERTMS/ETCS 列车牵引系统数据定义演变： 比较 SUBSET-026 Baseline 3 (v3.4.0) 和 Baseline 4 (v4.0.0) 版本中 Validated Train Data (Packet 11) 的内容定义：1）请指出该数据包中用于表示牵引系统标识的变量名称？2）当该变量不为零时，需要包含哪些额外的牵引数据变量？",    
            "type": "advanced"
        },
        {
    
            "question": "R2DATO项目D13.1可交付成果的安全分析部分（Part 3）采用了哪种专注于“不安全控制行为”（UCA）的新型分析方法？该方法的结果与D13.1的系统规格部分（Part 2）在哪个工作包（WP）中得到了持续跟进和更新？",
            "type": "advanced"
        },
        {
    
            "question": "根据《道路车辆 预期功能安全》中的 图11回答，当对已知危害场景的风险（步骤 10）和未知场景的残余风险（步骤 11）进行评估后，必须满足什么条件才能达到最终“预期功能安全发布”（步骤 12）的目标？",
            "type": "advanced"
        },
        {
    
            "question": "请比较在Subset-026的v3.4.0和v4.0.0中，对于安全紧急制动建立时间（Safe brake build up time）的定义有什么区别，请按照相同点、不同点的方式进行回答。",
            "type": "advanced"
        },
        {
    
            "question": "请比较《城市轨道交通全自动运行系统 通用技术条件》和《城市轨道交通全自动运行系统运营技术和管理规范（试行）》中，对于全自动列车列车过标或欠标时的处置原则有何异同。",
            "type": "advanced"
        },
        {
    
            "question": "北京地铁昌平线“7·25”脱轨事故调查报告指出，市地铁公司汲取“12·14”追尾事故教训不深刻。请结合两份事故报告，总结市地铁公司在行车调度员满岗要求和突发情况处置流程细化两个方面，具体哪些整改要求在“7·25”事故中被查明落实不到位或存在缺陷？",
            "type": "advanced"
        }
    ]


    
    # 创建output目录
    os.makedirs('./output', exist_ok=True)
    
    results = []
    performance_data = []
    
    for i, item in enumerate(test_questions, 1):
        question = item["question"]
        question_type = item.get("type", "auto")  # 默认为自动分析

        print(f"\n============================================================")
        print(f"问题{i}: {question} （类型: {question_type}）")
        print(f"============================================================\n")
    
        try:
            # 记录总开始时间
            total_start_time = time.time()
            
            # 调用智能体，获取结果
            result = agent.query_with_full_features(question, force_query_type=question_type)
            
            # 记录总结束时间
            total_end_time = time.time()
            total_time_ms = (total_end_time - total_start_time) * 1000
            
            # 使用format_output方法格式化输出，获取正确的context格式
            formatted_result = agent.format_output(result, include_reasoning=False)
            
            # 从格式化后的结果中提取答案和召回上下文
            full_result_text = formatted_result.get('answer', '')
            retrieved_contexts = formatted_result.get('retrieved_contexts', [])
            
            # 尝试从agent返回的结果中获取详细信息，否则使用估算
            if isinstance(result, dict):
                # 如果agent返回了详细的性能信息，优先使用
                retrieval_ms = result.get('retrieval_time_ms', int(total_time_ms * 0.3))
                generation_ms = result.get('generation_time_ms', int(total_time_ms * 0.7))
                
                # 尝试获取token使用情况
                token_usage = result.get('token_usage', {})
                prompt_tokens_est = token_usage.get('prompt_tokens', _estimate_tokens(question) * 11)
                answer_tokens_est = token_usage.get('completion_tokens', _estimate_tokens(full_result_text))
            else:
                # 使用估算方法
                # 假设召回占30%，生成占70%
                retrieval_ms = int(total_time_ms * 0.3)
                generation_ms = int(total_time_ms * 0.7)
                
                # 估算tokens
                prompt_tokens_est = _estimate_tokens(question) * 11  # 问题 + 上下文估算
                answer_tokens_est = _estimate_tokens(full_result_text)
            
            # 打印性能信息
            print(f"⏱️  召回时间: {retrieval_ms} ms")
            print(f"⏱️  生成时间: {generation_ms} ms")
            print(f"📊 输入tokens估算: {prompt_tokens_est}")
            print(f"📊 输出tokens估算: {answer_tokens_est}")
            print(f"📚 召回上下文数量: {len(retrieved_contexts)}")
            
            # 存储性能数据
            performance_data.append({
                "retrieval_ms": retrieval_ms,
                "generation_ms": generation_ms,
                "prompt_tokens_est": prompt_tokens_est,
                "answer_tokens_est": answer_tokens_est
            })
            
            # 存储当前问题的结果（按照要求的格式）
            results.append({
                "question": question,
                "retrieved_contexts": retrieved_contexts,
                "answer": full_result_text
            })
            print(f"✅ 问题处理成功。")
            
        except Exception as e:
            # 捕获错误，记录下来
            print(f"❌ 问题发生错误，无法获取答案: {e}")
            results.append({
                "question": question,
                "retrieved_contexts": [],
                "answer": f"错误: {str(e)}"
            })
            # 错误情况下也记录性能数据（全部为0）
            performance_data.append({
                "retrieval_ms": 0,
                "generation_ms": 0,
                "prompt_tokens_est": 0,
                "answer_tokens_est": 0
            })
            
        finally:
            # 新增/修改：处理完毕后保存结果（使用要求的格式）
            output_data = {"items": results}
            with open(RESULTS_FILE, 'w', encoding='utf-8') as f:
                json.dump(output_data, f, ensure_ascii=False, indent=2, default=convert)
            print(f"✅ 结果已保存到 {RESULTS_FILE}")
            
            # 保存性能数据
            with open(PERFORMANCE_FILE, 'w', encoding='utf-8') as f:
                json.dump(performance_data, f, ensure_ascii=False, indent=4)
            print(f"✅ 性能数据已保存到 {PERFORMANCE_FILE}")

    print("\n所有问题处理完毕。")
    
    # 打印性能统计摘要
    print("\n" + "="*60)
    print("📊 性能统计摘要")
    print("="*60)
    
    if performance_data:
        total_retrieval = sum(p['retrieval_ms'] for p in performance_data)
        total_generation = sum(p['generation_ms'] for p in performance_data)
        total_prompt_tokens = sum(p['prompt_tokens_est'] for p in performance_data)
        total_answer_tokens = sum(p['answer_tokens_est'] for p in performance_data)
        
        print(f"总召回时间: {total_retrieval:.0f} ms")
        print(f"总生成时间: {total_generation:.0f} ms")
        print(f"总处理时间: {total_retrieval + total_generation:.0f} ms")
        print(f"总输入tokens: {total_prompt_tokens:,}")
        print(f"总输出tokens: {total_answer_tokens:,}")
        print(f"总tokens: {total_prompt_tokens + total_answer_tokens:,}")
        print(f"\n平均每题召回时间: {total_retrieval/len(performance_data):.0f} ms")
        print(f"平均每题生成时间: {total_generation/len(performance_data):.0f} ms")
        print(f"平均每题输入tokens: {total_prompt_tokens/len(performance_data):.0f}")
        print(f"平均每题输出tokens: {total_answer_tokens/len(performance_data):.0f}")
    
    print("="*60 + "\n")
    
    
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
    
    optimized = tracker.optimize_context(long_text, max_tokens=50000)
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

