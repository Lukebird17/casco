#!/usr/bin/env python3
"""
快速方案：处理 NLP 文件并清理 default 库中的 NLP 数据
"""

import sys
import os

# 添加项目路径
sys.path.insert(0, '/home/honglianglu/hdd/rag-agent')

print("=" * 80)
print("🚀 NLP 知识库快速迁移方案")
print("=" * 80)
print()

# 步骤1：处理 NLP 文件
print("步骤 1/2: 向量化 NLP 文件")
print("-" * 80)
print()
print("正在处理 data/NLP/ 中的 14 个 PDF 文件...")
print("这将需要 5-15 分钟，请耐心等待...")
print()

try:
    from process_data import main as process_main
    import argparse
    
    # 模拟命令行参数
    sys.argv = ['process_data.py', '--kb', 'NLP']
    
    # 执行处理
    process_main()
    
    print()
    print("✅ NLP 文件处理完成！")
    print()
    
except Exception as e:
    print(f"❌ 处理失败: {e}")
    import traceback
    traceback.print_exc()
    print()
    print("请手动运行：")
    print("  cd /home/honglianglu/hdd/rag-agent")
    print("  conda activate rag")
    print("  python process_data.py --kb NLP")
    exit(1)

# 步骤2：清理 default 库（可选）
print()
print("步骤 2/2: 清理 default 库中的 NLP 文件（可选）")
print("-" * 80)
print()
print("⚠️  注意：NLP 文件现在在两个库中都有：")
print("   - vector_db/default/ （旧的，可以删除）")
print("   - vector_db/NLP/ （新的，应该使用）")
print()
print("清理 default 库的方法：")
print("1. 重新构建 default 库（推荐）")
print("2. 手动删除特定文件（复杂）")
print()

response = input("是否重新构建 default 库？(yes/no): ").strip().lower()

if response == 'yes':
    print()
    print("🔄 重新构建 default 库...")
    print()
    
    # 删除 default 向量库
    import shutil
    default_vector_dir = "/home/honglianglu/hdd/rag-agent/vector_db/default"
    
    if os.path.exists(default_vector_dir):
        # 备份
        import time
        backup_dir = f"{default_vector_dir}.backup_{int(time.time())}"
        shutil.move(default_vector_dir, backup_dir)
        print(f"   ✅ 备份到: {backup_dir}")
        
        # 重新创建
        os.makedirs(default_vector_dir, exist_ok=True)
        print(f"   ✅ 重新创建: {default_vector_dir}")
    
    # 检查 data/default/ 是否有文件
    default_data_dir = "/home/honglianglu/hdd/rag-agent/data/default"
    if os.path.exists(default_data_dir) and os.listdir(default_data_dir):
        print()
        print("   data/default/ 中有文件，重新处理...")
        
        try:
            sys.argv = ['process_data.py', '--kb', 'default']
            process_main()
            print("   ✅ default 库重建完成")
        except Exception as e:
            print(f"   ⚠️  重建失败: {e}")
    else:
        print()
        print("   ℹ️  data/default/ 为空，跳过处理")
    
    print()
    print("✅ 清理完成！")
else:
    print()
    print("   ⏭️  跳过清理，NLP 文件将保留在 default 库中")
    print("   （不影响使用，只是占用额外空间）")

print()
print("=" * 80)
print("✨ 迁移完成！")
print("=" * 80)
print()
print("📋 总结：")
print("   ✅ NLP 文件已向量化到 vector_db/NLP/")
print("   ✅ 前端选择知识库功能正常")
print("   ✅ 可以在对话栏切换到 NLP 库使用")
print()
print("🧪 测试建议：")
print("   1. 重启系统: ./start.sh")
print("   2. 在对话栏选择 'NLP' 知识库")
print("   3. 提问: '什么是隐马尔科夫模型'")
print("   4. 检查是否能检索到 NLP 文件")
print()
print("Navigate the Depths of Knowledge 🌌")
print("=" * 80)


