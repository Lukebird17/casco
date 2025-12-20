#!/usr/bin/env python3
"""
DeepEval调试测试脚本
用于快速定位DeepEval评估中的死循环或卡顿问题
"""

import sys
import asyncio
import signal
from typing import List, Dict

# 添加超时信号处理
def timeout_handler(signum, frame):
    print("\n❌ 测试超时！检测到死循环或卡顿")
    sys.exit(1)

signal.signal(signal.SIGALRM, timeout_handler)

async def test_evaluator():
    """测试质量评估器"""
    print("=" * 60)
    print("🧪 DeepEval 调试测试")
    print("=" * 60)
    
    # 导入评估器
    print("\n步骤1: 导入质量评估器...")
    try:
        from quality_evaluator_advanced import AdvancedQualityEvaluator
        print("✅ 导入成功")
    except Exception as e:
        print(f"❌ 导入失败: {e}")
        return
    
    # 初始化评估器
    print("\n步骤2: 初始化评估器...")
    try:
        evaluator = AdvancedQualityEvaluator()
        print("✅ 初始化成功")
        print(f"   - DeepEval模式: {evaluator.deepeval_mode}")
    except Exception as e:
        print(f"❌ 初始化失败: {e}")
        import traceback
        traceback.print_exc()
        return
    
    # 准备测试数据
    print("\n步骤3: 准备测试数据...")
    test_query = "什么是机器学习？"
    test_answer = "机器学习是一种人工智能技术，它使计算机能够从数据中学习并做出预测或决策，而无需显式编程。"
    test_context = [
        {
            "content": "机器学习是人工智能的一个分支，专注于构建能够从数据中学习的系统。",
            "metadata": {"source": "test.pdf", "page": 1}
        },
        {
            "content": "深度学习是机器学习的一个子集，使用多层神经网络。",
            "metadata": {"source": "test.pdf", "page": 2}
        }
    ]
    print(f"✅ 测试数据准备完成")
    print(f"   - 查询: {test_query}")
    print(f"   - 答案长度: {len(test_answer)} 字符")
    print(f"   - 上下文文档数: {len(test_context)}")
    
    # 设置整体超时（90秒）
    print("\n步骤4: 开始评估（60秒超时保护）...")
    signal.alarm(90)  # 90秒硬超时
    
    try:
        # 使用asyncio超时
        result = await asyncio.wait_for(
            evaluator.evaluate(
                query=test_query,
                answer=test_answer,
                retrieved_context=test_context,
                chat_history=[]
            ),
            timeout=60.0
        )
        
        signal.alarm(0)  # 取消超时
        print("\n✅ 评估完成！")
        print("=" * 60)
        print("📊 评估结果:")
        print("=" * 60)
        print(f"总分: {result.get('overall_score', 'N/A')}")
        print(f"详细分数: {result.get('detailed_scores', {})}")
        print(f"雷达图数据: {result.get('radar_data', [])}")
        
    except asyncio.TimeoutError:
        signal.alarm(0)
        print("\n❌ 评估超时（60秒）")
        print("可能原因:")
        print("1. LLM API响应慢")
        print("2. DeepEval内部有死循环")
        print("3. JSON解析陷入无限循环")
        
    except Exception as e:
        signal.alarm(0)
        print(f"\n❌ 评估失败: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("🚀 启动DeepEval调试测试...")
    print("提示: 如果90秒后仍无响应，将自动终止\n")
    
    try:
        asyncio.run(test_evaluator())
    except KeyboardInterrupt:
        print("\n\n⚠️  用户中断测试")
    except Exception as e:
        print(f"\n\n❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n" + "=" * 60)
    print("测试结束")
    print("=" * 60)

