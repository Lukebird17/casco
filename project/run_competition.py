#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   run_competition.py
@Time    :   2025/11/15
@Desc    :   竞赛运行脚本 - 处理所有题目并生成提交文件
'''

import json
import os
from typing import List, Dict
from VectorBase import VectorStore
from LLM import OpenAIChat
from Embeddings import OpenAIEmbedding
from agent import RAGAgent
from enhanced_utils import EnhancedReadFiles
from tqdm import tqdm


# 初赛一期题目
COMPETITION_QUESTIONS = {
    "基础题": [
        "2024 年，株洲中车时代电气股份有限公司中标金额是多少？",
        "根据欧洲铁路局 2025-2027 年单一规划文件，机构注册系统迁移到知识图谱（knowledge graph）方法的目标进度在 2025 年底应达到多少百分比？",
        "在 UIC 的报告里，根据国际能源署的分析，铁路的市场份额需要增长多少才能在本十年内实现《巴黎协定》的目标",
        "参照 IEEE 1474.1 的定义，附件 D (Typical safe braking model) 中对安全制动模型的描述，在"滑行时间 (Coast time, C)"期间，列车被假定处于什么状态？",
        "在 Manresa 车站的事件调查报告中，列车 78443 被授权越过 3023 进站信号机后，何时（日期和时间）发生了列车 95218 最终启动了行驶，并最终导致两列车存在碰撞风险？"
    ],
    "中级题": [
        "南京地铁 S7 号线的运营里程，在江苏省内已运营地铁长度中排第几？",
        "车辆外部移动实体的场景要素：根据 GB/T 43267—2023（预期功能安全），在场景要素结构中，可移动实体的第 2 层要素和第 3 层要素分别是什么？（需完整列出第 3 层中所有实体类型）。",
        "根据文档《2024_Communications-Based Train Control》，图 5.11 所示的网状控制回路结构，ATO 子系统是如何实现自身的控制回路的？请阐述其如何获取输入（Messglieder），如何形成车辆轨迹（Fahrzeugtrajektorie），以及如何将轨迹作为目标值传递给列车的控制设备（Steuergerät）。"
    ],
    "高级题": [
        "在 CBTC 互联互通规范体系中，关于列车启动、加速、巡航和制动的自动控制功能，其在《系统总体要求》中的分配归属于哪个子系统？并在《CBTC 部分测试及验证》中体现在哪个功能的测试中，测试需求编号是什么？",
        "ERTMS/ETCS 列车牵引系统数据定义演变： 比较 SUBSET-026 Baseline 3 (v3.4.0) 和 Baseline 4 (v4.0.0) 版本中 Validated Train Data (Packet 11) 的内容定义：1）请指出该数据包中用于表示牵引系统标识的变量名称？2）当该变量不为零时，需要包含哪些额外的牵引数据变量？"
    ]
}


class CompetitionRunner:
    """
    竞赛运行器
    """
    
    def __init__(self, data_path: str = '../data', storage_path: str = 'storage'):
        self.data_path = data_path
        self.storage_path = storage_path
        self.vector_store = None
        self.agent = None
        
    def build_or_load_vectorstore(self, rebuild: bool = False):
        """
        构建或加载向量数据库
        """
        print("=" * 60)
        if rebuild or not os.path.exists(f"{self.storage_path}/vectors.json"):
            print("📚 构建向量数据库...")
            # 使用增强的文档读取器
            reader = EnhancedReadFiles(self.data_path)
            docs = reader.get_content(max_token_len=400, cover_content=50)
            print(f"   总共分块数: {len(docs)}")
            
            # 创建向量存储
            self.vector_store = VectorStore(docs)
            embedding = OpenAIEmbedding()
            
            print("   生成向量嵌入...")
            self.vector_store.get_vector(EmbeddingModel=embedding)
            
            print("   保存向量数据库...")
            self.vector_store.persist(path=self.storage_path)
            print("✅ 向量数据库构建完成！")
        else:
            print("📂 加载已有向量数据库...")
            self.vector_store = VectorStore()
            self.vector_store.load_vector(self.storage_path)
            print(f"✅ 加载完成！文档数量: {len(self.vector_store.document)}")
        print("=" * 60 + "\n")
    
    def initialize_agent(self):
        """
        初始化智能体
        """
        embedding = OpenAIEmbedding()
        llm = OpenAIChat()
        self.agent = RAGAgent(self.vector_store, llm, embedding)
        print("🤖 智能体初始化完成！\n")
    
    def process_single_question(self, query: str, question_type: str = "") -> Dict:
        """
        处理单个问题
        """
        print(f"\n{'='*60}")
        print(f"问题类型: {question_type}")
        print(f"问题: {query}")
        print(f"{'='*60}")
        
        result = self.agent.query_with_retry(query)
        output = self.agent.format_output(result)
        
        print(f"\n答案: {output['answer']}")
        print(f"检索到的文档片段数: {len(output['result'])}")
        
        return output
    
    def process_all_questions(self, output_dir: str = 'outputs'):
        """
        处理所有题目并保存结果
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        all_results = []
        
        for question_type, questions in COMPETITION_QUESTIONS.items():
            print(f"\n\n{'#'*60}")
            print(f"# 开始处理: {question_type} (共 {len(questions)} 道)")
            print(f"{'#'*60}\n")
            
            for idx, question in enumerate(questions, 1):
                try:
                    result = self.process_single_question(question, f"{question_type}-{idx}")
                    
                    # 保存单个结果
                    output_file = os.path.join(output_dir, f"{question_type}_{idx}.json")
                    with open(output_file, 'w', encoding='utf-8') as f:
                        json.dump(result, f, ensure_ascii=False, indent=2)
                    
                    all_results.append({
                        'type': question_type,
                        'index': idx,
                        'result': result
                    })
                    
                    print(f"✅ 已保存到: {output_file}\n")
                    
                except Exception as e:
                    print(f"❌ 处理出错: {e}\n")
                    continue
        
        # 保存汇总结果
        summary_file = os.path.join(output_dir, 'all_results.json')
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(all_results, f, ensure_ascii=False, indent=2)
        
        print(f"\n{'='*60}")
        print(f"🎉 所有题目处理完成！")
        print(f"📁 结果保存在: {output_dir}")
        print(f"📊 汇总文件: {summary_file}")
        print(f"{'='*60}\n")
        
        return all_results
    
    def run_interactive_mode(self):
        """
        交互模式 - 可以输入自定义问题
        """
        print("\n" + "="*60)
        print("🎯 进入交互模式")
        print("输入问题进行查询，输入 'quit' 或 'exit' 退出")
        print("="*60 + "\n")
        
        while True:
            try:
                query = input("\n请输入问题: ").strip()
                
                if query.lower() in ['quit', 'exit', 'q']:
                    print("👋 退出交互模式")
                    break
                
                if not query:
                    continue
                
                result = self.process_single_question(query, "自定义")
                
                # 询问是否保存
                save = input("\n是否保存结果？(y/n): ").strip().lower()
                if save == 'y':
                    filename = input("请输入文件名 (不含扩展名): ").strip()
                    if filename:
                        output_file = f"outputs/{filename}.json"
                        os.makedirs('outputs', exist_ok=True)
                        with open(output_file, 'w', encoding='utf-8') as f:
                            json.dump(result, f, ensure_ascii=False, indent=2)
                        print(f"✅ 已保存到: {output_file}")
                
            except KeyboardInterrupt:
                print("\n\n👋 退出交互模式")
                break
            except Exception as e:
                print(f"❌ 处理出错: {e}")
                continue


def main():
    """
    主函数
    """
    import argparse
    
    parser = argparse.ArgumentParser(description='智能体竞赛运行脚本')
    parser.add_argument('--mode', type=str, default='all', 
                       choices=['all', 'interactive', 'single'],
                       help='运行模式: all(处理所有题目), interactive(交互模式), single(单个问题)')
    parser.add_argument('--rebuild', action='store_true',
                       help='重新构建向量数据库')
    parser.add_argument('--query', type=str, default='',
                       help='单个问题模式下的查询')
    parser.add_argument('--data-path', type=str, default='../data',
                       help='数据目录路径')
    parser.add_argument('--storage-path', type=str, default='storage',
                       help='向量数据库存储路径')
    parser.add_argument('--output-dir', type=str, default='outputs',
                       help='输出目录路径')
    
    args = parser.parse_args()
    
    # 创建运行器
    runner = CompetitionRunner(
        data_path=args.data_path,
        storage_path=args.storage_path
    )
    
    # 构建或加载向量数据库
    runner.build_or_load_vectorstore(rebuild=args.rebuild)
    
    # 初始化智能体
    runner.initialize_agent()
    
    # 根据模式运行
    if args.mode == 'all':
        runner.process_all_questions(output_dir=args.output_dir)
    elif args.mode == 'interactive':
        runner.run_interactive_mode()
    elif args.mode == 'single':
        if not args.query:
            print("❌ 单个问题模式需要提供 --query 参数")
            return
        result = runner.process_single_question(args.query, "单个问题")
        
        # 保存结果
        os.makedirs(args.output_dir, exist_ok=True)
        output_file = os.path.join(args.output_dir, 'single_query_result.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"\n✅ 结果已保存到: {output_file}")


if __name__ == "__main__":
    main()

