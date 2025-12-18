#!/usr/bin/env python3
"""
测试完整的上传Pipeline（PPTX/DOCX → PDF → 向量化）
"""
import sys
import os
import asyncio
import tempfile
import shutil

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

async def test_upload_pptx():
    """模拟PPTX上传流程"""
    print("\n" + "="*70)
    print("🧪 测试完整上传Pipeline: PPTX → PDF → 向量化")
    print("="*70)
    
    # 导入必要的模块
    from document_loader import DocumentLoader
    from text_splitter import TextSplitter
    from vector_store import VectorStore
    from config import get_kb_data_dir, get_kb_vector_dir, ensure_kb_dirs
    
    # 测试文件
    test_pptx = "/home/honglianglu/hdd/rag-agent/data/nlp2/2.3 中文分词与CRF.pptx"
    
    if not os.path.exists(test_pptx):
        print("❌ 测试文件不存在")
        return False
    
    print(f"\n📄 测试文件: {os.path.basename(test_pptx)}")
    print(f"   大小: {os.path.getsize(test_pptx)/1024/1024:.2f} MB")
    
    # 使用test知识库
    kb_id = "test_upload"
    kb_data_dir, kb_vector_dir = ensure_kb_dirs(kb_id)
    
    print(f"\n📦 知识库: {kb_id}")
    print(f"   数据目录: {kb_data_dir}")
    print(f"   向量库目录: {kb_vector_dir}")
    
    # 创建临时目录模拟上传
    temp_dir = tempfile.mkdtemp()
    saved_files = []
    permanent_files = []
    
    try:
        print("\n🔄 步骤1: 模拟文件上传...")
        
        # 复制文件到临时目录
        filename = os.path.basename(test_pptx)
        temp_path = os.path.join(temp_dir, filename)
        shutil.copy2(test_pptx, temp_path)
        print(f"   ✅ 文件已保存到临时目录: {temp_path}")
        
        # 初始化DocumentLoader
        loader = DocumentLoader(data_dir=temp_dir)
        
        # 检查文件类型
        file_ext = os.path.splitext(filename)[1].lower()
        base_name = os.path.splitext(filename)[0]
        
        print(f"\n🔄 步骤2: 转换 {file_ext.upper()} → PDF...")
        
        if file_ext in ['.pptx', '.docx']:
            # 转换为PDF
            pdf_path = loader.convert_to_pdf(temp_path)
            
            if pdf_path and os.path.exists(pdf_path):
                # 转换成功
                final_filename = f"{base_name}.pdf"
                permanent_path = os.path.join(kb_data_dir, final_filename)
                
                # 保存PDF到data目录
                shutil.copy2(pdf_path, permanent_path)
                
                # 也保存到临时目录用于向量化
                temp_pdf = os.path.join(temp_dir, final_filename)
                shutil.copy2(pdf_path, temp_pdf)
                saved_files.append(temp_pdf)
                permanent_files.append(permanent_path)
                
                print(f"   ✅ 转换成功！")
                print(f"   ✅ 已保存为: {final_filename}")
                print(f"      永久路径: {permanent_path}")
                print(f"      PDF大小: {os.path.getsize(permanent_path)/1024/1024:.2f} MB")
            else:
                print("   ❌ 转换失败")
                return False
        
        print(f"\n🔄 步骤3: 向量化处理（MinerU + 向量存储）...")
        
        # 处理文件（从临时目录加载转换后的PDF）
        splitter = TextSplitter(chunk_size=500, chunk_overlap=100)
        text_vector_store = VectorStore(db_path=kb_vector_dir)
        
        documents, images = loader.load_all_documents()
        
        print(f"   📝 提取到 {len(documents)} 个文档块")
        print(f"   📸 提取到 {len(images)} 张图片")
        
        if documents:
            chunks = splitter.split_documents(documents)
            text_vector_store.add_documents(chunks)
            print(f"   ✅ 已添加 {len(chunks)} 个文本块到向量库")
        
        if images:
            from image_vector_store import ImageVectorStore
            image_vector_store = ImageVectorStore(db_path=kb_vector_dir)
            image_vector_store.add_images(images)
            print(f"   ✅ 已添加 {len(images)} 张图片到向量库")
        
        print(f"\n✅ Pipeline完成！")
        print(f"\n📊 总结:")
        print(f"   - 原始文件: {filename}")
        print(f"   - 转换后: {final_filename}")
        print(f"   - 保存位置: {permanent_path}")
        print(f"   - 文本块数: {len(chunks)}")
        print(f"   - 图片数: {len(images)}")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Pipeline失败: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        # 清理临时目录
        shutil.rmtree(temp_dir, ignore_errors=True)
        print(f"\n🧹 已清理临时文件")

async def main():
    """主函数"""
    print("\n" + "="*70)
    print("🚀 完整上传Pipeline测试")
    print("   PPTX/DOCX → PDF → MinerU → 向量化")
    print("="*70)
    
    success = await test_upload_pptx()
    
    print("\n" + "="*70)
    if success:
        print("🎉 测试成功！Pipeline正常工作！")
        print("\n💡 现在可以：")
        print("   1. 重启后端: ./start_backend.sh")
        print("   2. 在UI中上传PPTX/DOCX文件")
        print("   3. 系统会自动转换为PDF并保存")
    else:
        print("❌ 测试失败，请检查错误信息")
    print("="*70 + "\n")

if __name__ == "__main__":
    asyncio.run(main())



