#!/usr/bin/env python3
"""
快速测试：验证页码准确性和查询功能
"""

from rag_agent import RAGAgent

def test_page_28_slab():
    """测试第28页slab图的检索"""
    
    print("=" * 60)
    print("测试：查询第28页的slab图")
    print("=" * 60)
    
    # 初始化 RAG Agent（启用多模态）
    agent = RAGAgent(
        model="qwen-vl-max",
        enable_tracking=True,
        enable_cot=False,
        use_multimodal=True  # 正确的参数名
    )
    
    # 测试查询
    query = "第28页的slab示意图中的Next_free下面一格里写着什么？"
    
    print(f"\n🔍 查询: {query}\n")
    
    try:
        answer = agent.answer_question(query)
        print(f"\n✅ 回答:\n{answer}\n")
        
    except Exception as e:
        print(f"\n❌ 错误: {e}\n")
        import traceback
        traceback.print_exc()
    
    print("=" * 60)

if __name__ == "__main__":
    test_page_28_slab()

