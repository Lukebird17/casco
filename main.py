import os
from rag_agent import RAGAgent
from config import VECTOR_DB_PATH, MODEL_NAME


def main():
    print("=" * 60)
    print("🎓 智能课程助教系统 - 命令行版")
    print("=" * 60)
    print()

    # 检查向量数据库
    if not os.path.exists(VECTOR_DB_PATH):
        print("❌ 向量数据库不存在！")
        print()
        print("请先运行以下命令初始化知识库：")
        print("  python process_data.py")
        print()
        print("或者参考 README_完整版.md 了解如何使用动态数据库管理。")
        return

    print("📚 正在初始化RAG Agent...")
    
    # 初始化RAG Agent
    agent = RAGAgent(
        model=MODEL_NAME,
        enable_tracking=True,
        enable_cot=True
    )

    # 检查知识库
    count = agent.vector_store.get_collection_count()
    if count == 0:
        print("❌ 知识库为空！")
        print()
        print("请先添加文档到知识库：")
        print("  python process_data.py")
        print()
        return

    print(f"✅ 知识库已加载，包含 {count} 个文档片段")
    print()
    print("💡 功能特色：")
    print("  • 智能问题分类")
    print("  • 多查询增强检索")
    print("  • 答案质量检查")
    print("  • Token追踪和优化")
    if agent.enable_cot:
        print("  • Auto-CoT推理增强")
    print()
    print("特殊命令：")
    print("  /reasoning - 查看推理链")
    print("  /tokens    - 查看Token统计")
    print("  quit       - 退出系统")
    print()

    # 启动交互式对话
    agent.chat()


if __name__ == "__main__":
    main()
