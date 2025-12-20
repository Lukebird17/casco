#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试任务取消功能
模拟用户快速连续提问，验证旧的评估任务是否被取消
"""

import asyncio
import aiohttp
import json
import time

BASE_URL = "http://localhost:8000"
SESSION_ID = "test_cancel_123"

async def send_question(session, question, question_num):
    """发送问题并接收流式响应"""
    print(f"\n{'='*60}")
    print(f"📝 发送问题 {question_num}: {question}")
    print(f"{'='*60}")
    
    start_time = time.time()
    
    try:
        async with session.post(
            f"{BASE_URL}/api/chat/stream",
            json={
                "message": question,
                "session_id": SESSION_ID,
                "thinking_mode": "standard",
                "retrieval_k": 5
            },
            timeout=aiohttp.ClientTimeout(total=120)
        ) as resp:
            if resp.status != 200:
                print(f"❌ HTTP错误: {resp.status}")
                return
            
            answer_received = False
            evaluation_received = False
            
            async for line in resp.content:
                line = line.decode('utf-8').strip()
                if not line or not line.startswith('data:'):
                    continue
                
                try:
                    data_str = line[5:].strip()  # 去掉 "data: "
                    data = json.loads(data_str)
                    
                    msg_type = data.get('type')
                    
                    if msg_type == 'status':
                        print(f"  ⏳ 状态: {data.get('data')}")
                    elif msg_type == 'citations':
                        citations = data.get('data', [])
                        print(f"  📚 找到 {len(citations)} 个相关文档")
                    elif msg_type == 'answer':
                        answer = data.get('data', '')
                        gen_time = data.get('generation_time', 0)
                        print(f"  ✅ 答案: {answer[:100]}...")
                        print(f"  ⏱️  生成时间: {gen_time}秒")
                        answer_received = True
                    elif msg_type == 'quality_metrics':
                        metrics = data.get('data', {})
                        if metrics.get('status') == 'evaluating':
                            print(f"  📊 评估中...")
                        else:
                            score = metrics.get('overall_score', 0)
                            eval_time = metrics.get('eval_time', 0)
                            print(f"  📊 质量评分: {score}/5.0 (耗时 {eval_time}秒)")
                            evaluation_received = True
                    elif msg_type == 'done':
                        elapsed = time.time() - start_time
                        print(f"  ✅ 问题 {question_num} 处理完成 (总耗时 {elapsed:.2f}秒)")
                        if not evaluation_received:
                            print(f"  ⚠️  注意: 评估可能在后台运行或被取消")
                
                except json.JSONDecodeError:
                    continue
    
    except asyncio.TimeoutError:
        print(f"❌ 超时")
    except Exception as e:
        print(f"❌ 错误: {e}")

async def test_normal_flow():
    """测试1: 正常流程（等待评估完成）"""
    print("\n" + "="*80)
    print("🧪 测试1: 正常流程 - 单个问题，等待评估完成")
    print("="*80)
    
    async with aiohttp.ClientSession() as session:
        await send_question(session, "什么是深度学习？请简要回答。", 1)
        print("\n⏳ 等待5秒，让评估完成...")
        await asyncio.sleep(5)

async def test_rapid_questions():
    """测试2: 快速连续提问（应该取消旧评估）"""
    print("\n" + "="*80)
    print("🧪 测试2: 快速连续提问 - 验证任务取消")
    print("="*80)
    
    async with aiohttp.ClientSession() as session:
        # 问题1
        await send_question(session, "什么是神经网络？请简要回答。", 1)
        
        # 等待2秒（评估还在进行中）
        print("\n⏳ 等待2秒后发送下一个问题...")
        await asyncio.sleep(2)
        
        # 问题2（应该取消问题1的评估）
        await send_question(session, "什么是卷积神经网络？请简要回答。", 2)
        
        # 等待2秒（评估还在进行中）
        print("\n⏳ 等待2秒后发送下一个问题...")
        await asyncio.sleep(2)
        
        # 问题3（应该取消问题2的评估）
        await send_question(session, "什么是循环神经网络？请简要回答。", 3)

async def test_parallel_sessions():
    """测试3: 不同会话的并行请求（不应该互相影响）"""
    print("\n" + "="*80)
    print("🧪 测试3: 并行会话 - 不同会话不应互相影响")
    print("="*80)
    
    async def session_a():
        async with aiohttp.ClientSession() as session:
            await send_question(session, "深度学习的历史是什么？", "A1")
            await asyncio.sleep(2)
            await send_question(session, "深度学习的应用有哪些？", "A2")
    
    async def session_b():
        await asyncio.sleep(1)  # 稍微延迟启动
        async with aiohttp.ClientSession() as session:
            await send_question(session, "机器学习和深度学习的区别是什么？", "B1")
            await asyncio.sleep(2)
            await send_question(session, "机器学习有哪些算法？", "B2")
    
    # 并行运行两个会话
    await asyncio.gather(session_a(), session_b())

async def main():
    """主测试函数"""
    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   🧪 任务取消功能测试套件                                    ║
║                                                              ║
║   这个测试脚本会验证:                                         ║
║   1. 正常情况下评估能正常完成                                 ║
║   2. 快速连续提问时，旧评估会被取消                           ║
║   3. 不同会话之间互不影响                                     ║
║                                                              ║
║   请观察后端日志中的:                                         ║
║   - 🛑 检测到新问题，取消会话 xxx 的旧评估任务                ║
║   - ✅ 旧评估任务已取消                                       ║
║   - 🛑 后台评估已被取消（新问题到来）                         ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
""")
    
    # 测试1: 正常流程
    await test_normal_flow()
    await asyncio.sleep(3)
    
    # 测试2: 快速连续提问
    await test_rapid_questions()
    await asyncio.sleep(3)
    
    # 测试3: 并行会话（注释掉，因为可能比较慢）
    # await test_parallel_sessions()
    
    print("\n" + "="*80)
    print("✅ 所有测试完成！")
    print("="*80)
    print("\n请检查后端日志，确认任务取消功能正常工作。")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n⚠️  测试被用户中断")
    except Exception as e:
        print(f"\n\n❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()

