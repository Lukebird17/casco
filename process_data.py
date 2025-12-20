"""
批量处理脚本 - 与 UI 上传逻辑一致
支持多知识库、文件转换、知识图谱提取
"""

import os
import sys
import argparse
from pathlib import Path

# 添加当前目录到路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from document_loader import DocumentLoader
from text_splitter import TextSplitter
from vector_store import VectorStore
from image_vector_store import ImageVectorStore
from knowledge_graph import KnowledgeGraph
from config import get_kb_data_dir, get_kb_vector_dir, ensure_kb_dirs, CHUNK_SIZE, CHUNK_OVERLAP


def process_knowledge_base(kb_id: str, clear_existing: bool = False, extract_kg: bool = True):
    """
    处理指定知识库的所有文档
    
    Args:
        kb_id: 知识库ID
        clear_existing: 是否清空现有数据（默认False，增量添加）
        extract_kg: 是否提取知识图谱（默认True）
    """
    print("=" * 60)
    print(f"📚 处理知识库: {kb_id}")
    print("=" * 60)
    
    # 确保知识库目录存在
    kb_data_dir, kb_vector_dir = ensure_kb_dirs(kb_id)
    print(f"📂 数据目录: {kb_data_dir}")
    print(f"📂 向量库目录: {kb_vector_dir}")
    print("")
    
    # 检查数据目录
    if not os.path.exists(kb_data_dir):
        print(f"❌ 数据目录不存在: {kb_data_dir}")
        print("💡 请先将文档放入该目录，支持: PDF、DOCX、PPTX、TXT、MD")
        return
    
    # 检查是否有文件
    files = list(Path(kb_data_dir).glob("*"))
    supported_exts = {'.pdf', '.docx', '.pptx', '.txt', '.md', '.jpg', '.jpeg', '.png', '.gif'}
    valid_files = [f for f in files if f.suffix.lower() in supported_exts]
    
    if not valid_files:
        print(f"❌ 数据目录中没有支持的文件")
        print(f"💡 支持的格式: {', '.join(supported_exts)}")
        return
    
    print(f"✅ 找到 {len(valid_files)} 个文件:")
    for f in valid_files:
        print(f"   - {f.name}")
    print("")
    
    # 初始化组件
    print("🔧 初始化组件...")
    loader = DocumentLoader(data_dir=kb_data_dir)
    splitter = TextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    text_vector_store = VectorStore(db_path=kb_vector_dir)
    image_vector_store = ImageVectorStore(db_path=kb_vector_dir)
    
    if extract_kg:
        knowledge_graph = KnowledgeGraph()
        print("✅ 知识图谱提取器已初始化")
    
    # 清空数据库（如果需要）
    if clear_existing:
        print("\n⚠️  清空现有数据...")
        text_vector_store.clear_collection()
        image_vector_store.clear_collection()
        print("✅ 已清空")
    else:
        print("\n📊 增量添加模式（不清空现有数据）")
    print("")
    
    # 处理 PPTX/DOCX 转换
    print("=" * 60)
    print("🔄 检查文件转换...")
    print("=" * 60)
    
    converted_count = 0
    for file_path in valid_files:
        if file_path.suffix.lower() in ['.pptx', '.docx']:
            print(f"\n📄 处理: {file_path.name}")
            print(f"   检测到 {file_path.suffix.upper()} 文件，转换为 PDF...")
            
            try:
                pdf_path = loader.convert_to_pdf(str(file_path))
                
                if pdf_path and os.path.exists(pdf_path):
                    print(f"   ✅ 转换成功: {os.path.basename(pdf_path)}")
                    converted_count += 1
                else:
                    print(f"   ⚠️  转换失败，将使用原始文件")
            except Exception as e:
                print(f"   ❌ 转换错误: {e}")
                print(f"   ⚠️  将尝试直接处理原始文件")
    
    if converted_count > 0:
        print(f"\n✅ 共转换 {converted_count} 个文件")
    print("")
    
    # 加载文档和图片
    print("=" * 60)
    print("📚 加载文档和图片...")
    print("=" * 60)
    
    try:
        documents, images = loader.load_all_documents()
    except Exception as e:
        print(f"❌ 加载文档失败: {e}")
        import traceback
        traceback.print_exc()
        return
    
    if not documents and not images:
        print("❌ 未能加载任何文档或图片")
        return
    
    print(f"\n✅ 加载完成:")
    print(f"   - 文档: {len(documents)} 个")
    print(f"   - 图片: {len(images)} 张")
    print("")
    
    # 处理文本
    if documents:
        print("=" * 60)
        print("📝 处理文本数据...")
        print("=" * 60)
        
        try:
            chunks = splitter.split_documents(documents)
            print(f"✅ 分割为 {len(chunks)} 个文本块")
            
            text_vector_store.add_documents(chunks)
            print(f"✅ 已添加到向量数据库")
            
            # 统计信息
            total_chunks = text_vector_store.get_collection_count()
            print(f"📊 当前向量库共有 {total_chunks} 个文本块")
        except Exception as e:
            print(f"❌ 处理文本失败: {e}")
            import traceback
            traceback.print_exc()
        print("")
    
    # 处理图片
    if images:
        print("=" * 60)
        print("🖼️  处理图片数据...")
        print("=" * 60)
        
        try:
            image_vector_store.add_images(images)
            print(f"✅ 已添加 {len(images)} 张图片到向量数据库")
            
            # 统计信息
            total_images = image_vector_store.get_collection_count()
            print(f"📊 当前向量库共有 {total_images} 张图片")
        except Exception as e:
            print(f"❌ 处理图片失败: {e}")
            import traceback
            traceback.print_exc()
        print("")
    
    # 提取知识图谱
    if extract_kg and documents:
        print("=" * 60)
        print("🧠 提取知识图谱...")
        print("=" * 60)
        
        entities_count = 0
        relations_count = 0
        
        # 只处理前5个文档以节省时间
        docs_to_process = documents[:5]
        print(f"处理前 {len(docs_to_process)} 个文档...")
        
        for i, doc in enumerate(docs_to_process, 1):
            try:
                text = doc.get('content', '')[:2000]  # 限制文本长度
                if len(text) > 100:
                    print(f"\n   [{i}/{len(docs_to_process)}] {doc.get('filename', 'unknown')}")
                    
                    entities, relations = knowledge_graph.extract_entities_and_relations(
                        text,
                        source=doc.get('filename', 'unknown'),
                        use_simple=True  # 使用简单快速的关键词提取
                    )
                    
                    # 添加到知识图谱
                    if entities or relations:
                        knowledge_graph.add_to_graph(entities, relations)
                        print(f"      ✅ 提取 {len(entities)} 个实体，{len(relations)} 个关系")
                        entities_count += len(entities)
                        relations_count += len(relations)
                    else:
                        print(f"      ⚠️  未提取到实体和关系")
            except Exception as e:
                print(f"      ❌ 提取失败: {e}")
        
        print(f"\n✅ 知识图谱提取完成:")
        print(f"   - 实体: {entities_count} 个")
        print(f"   - 关系: {relations_count} 个")
        print("")
    
    # 最终统计
    print("=" * 60)
    print("📊 处理完成！")
    print("=" * 60)
    print(f"✅ 知识库: {kb_id}")
    print(f"✅ 文本块: {text_vector_store.get_collection_count()}")
    print(f"✅ 图片: {image_vector_store.get_collection_count()}")
    if extract_kg:
        print(f"✅ 实体: {entities_count}")
        print(f"✅ 关系: {relations_count}")
    print("")


def list_knowledge_bases():
    """列出所有知识库"""
    from config import DATA_DIR
    
    print("=" * 60)
    print("📚 可用的知识库:")
    print("=" * 60)
    
    if not os.path.exists(DATA_DIR):
        print("❌ data/ 目录不存在")
        return
    
    kb_dirs = [d for d in os.listdir(DATA_DIR) if os.path.isdir(os.path.join(DATA_DIR, d))]
    
    if not kb_dirs:
        print("❌ 没有找到知识库")
        print("💡 创建知识库: mkdir -p data/{kb_id}")
        return
    
    for kb_id in sorted(kb_dirs):
        kb_path = os.path.join(DATA_DIR, kb_id)
        files = list(Path(kb_path).glob("*.*"))
        print(f"\n📂 {kb_id}")
        print(f"   文件数: {len(files)}")
        
        # 显示文件列表
        if files:
            for f in files[:5]:  # 最多显示5个
                print(f"      - {f.name}")
            if len(files) > 5:
                print(f"      ... 还有 {len(files) - 5} 个文件")
    print("")


def main():
    parser = argparse.ArgumentParser(
        description="OmniScry - 批量处理知识库文档",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 列出所有知识库
  python process_data.py --list
  
  # 处理指定知识库（增量添加）
  python process_data.py --kb-id my_knowledge_base
  
  # 清空并重新处理
  python process_data.py --kb-id my_knowledge_base --clear
  
  # 不提取知识图谱（更快）
  python process_data.py --kb-id my_knowledge_base --no-kg
  
使用步骤:
  1. 创建知识库目录: mkdir -p data/{kb_id}
  2. 将文档放入该目录
  3. 运行此脚本处理文档
  4. 启动系统开始使用
        """
    )
    
    parser.add_argument(
        '--kb-id',
        type=str,
        help='知识库ID（对应 data/ 下的子目录名）'
    )
    
    parser.add_argument(
        '--clear',
        action='store_true',
        help='清空现有数据后重新处理（默认为增量添加）'
    )
    
    parser.add_argument(
        '--no-kg',
        action='store_true',
        help='不提取知识图谱（处理更快）'
    )
    
    parser.add_argument(
        '--list',
        action='store_true',
        help='列出所有知识库'
    )
    
    args = parser.parse_args()
    
    print("\n" + "=" * 60)
    print("🌌 OmniScry - 知识库批量处理工具")
    print("   Navigate the Depths of Knowledge")
    print("=" * 60 + "\n")
    
    # 列出知识库
    if args.list:
        list_knowledge_bases()
        return
    
    # 检查是否指定了知识库
    if not args.kb_id:
        print("❌ 错误: 请指定知识库ID")
        print("💡 使用 --list 查看所有知识库")
        print("💡 使用 --kb-id {kb_id} 处理指定知识库")
        print("💡 使用 --help 查看完整帮助")
        print("")
        list_knowledge_bases()
        return
    
    # 处理知识库
    try:
        process_knowledge_base(
            kb_id=args.kb_id,
            clear_existing=args.clear,
            extract_kg=not args.no_kg
        )
        
        print("🎉 处理成功！")
        print("💡 现在可以启动系统并在该知识库中进行问答")
        print("")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  用户中断")
        print("")
    except Exception as e:
        print(f"\n❌ 处理失败: {e}")
        import traceback
        traceback.print_exc()
        print("")


if __name__ == "__main__":
    main()
