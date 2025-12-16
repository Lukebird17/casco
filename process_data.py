import os
from document_loader import DocumentLoader
from text_splitter import TextSplitter
from vector_store import VectorStore
from image_vector_store import ImageVectorStore

from config import DATA_DIR, CHUNK_SIZE, CHUNK_OVERLAP, VECTOR_DB_PATH


def main():
    if not os.path.exists(DATA_DIR):
        print(f"数据目录不存在: {DATA_DIR}")
        print("请创建数据目录并放入PDF、PPTX、DOCX或TXT文件")
        return

    # 初始化组件
    loader = DocumentLoader(
        data_dir=DATA_DIR,
    )
    splitter = TextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    
    # 初始化文本和图片向量存储
    text_vector_store = VectorStore(db_path=VECTOR_DB_PATH)
    image_vector_store = ImageVectorStore(db_path=VECTOR_DB_PATH)
    
    # 清空数据库
    text_vector_store.clear_collection()
    image_vector_store.clear_collection()

    # 加载文档和图片
    print("=" * 60)
    print("📚 加载文档...")
    print("=" * 60)
    documents, images = loader.load_all_documents()
    
    if not documents and not images:
        print("未找到任何文档或图片")
        return
    
    print(f"\n✅ 加载完成:")
    print(f"   - 文档: {len(documents)} 个")
    print(f"   - 图片: {len(images)} 张")

    # 处理文本
    print("\n" + "=" * 60)
    print("📝 处理文本数据...")
    print("=" * 60)
    
    chunks = splitter.split_documents(documents)
    text_vector_store.add_documents(chunks)
    
    # 处理图片
    if images:
        print("\n" + "=" * 60)
        print("🖼️  处理图片数据...")
        print("=" * 60)
        image_vector_store.add_images(images)
    
    # 统计信息
    print("\n" + "=" * 60)
    print("📊 数据处理完成！")
    print("=" * 60)
    print(f"✅ 文本文档块: {text_vector_store.get_collection_count()}")
    print(f"✅ 图片数量: {image_vector_store.get_collection_count()}")
    print("\n🎉 可以运行 main.py 开始对话")


if __name__ == "__main__":
    main()
