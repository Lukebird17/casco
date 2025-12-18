#!/usr/bin/env python3
"""
测试LibreOffice转换功能
"""
import sys
import os

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from document_loader import DocumentLoader
import tempfile
import shutil

def test_libreoffice_available():
    """测试LibreOffice是否可用"""
    print("\n" + "="*60)
    print("测试1: 检查LibreOffice可用性")
    print("="*60)
    
    loader = DocumentLoader()
    is_available = loader.check_libreoffice()
    
    if is_available:
        print("✅ LibreOffice 可用！")
        return True
    else:
        print("❌ LibreOffice 不可用")
        return False

def test_convert_pptx():
    """测试PPTX转换"""
    print("\n" + "="*60)
    print("测试2: PPTX转PDF转换")
    print("="*60)
    
    # 创建一个测试PPTX文件（如果存在的话）
    test_files = [
        "/home/honglianglu/hdd/rag-agent/data/default/2.3 中文分词与CRF.pptx",
        "/home/honglianglu/hdd/rag-agent/data/default/*.pptx"
    ]
    
    # 查找第一个存在的PPTX文件
    test_file = None
    for pattern in test_files:
        import glob
        files = glob.glob(pattern) if '*' in pattern else [pattern]
        for f in files:
            if os.path.exists(f) and f.endswith('.pptx'):
                test_file = f
                break
        if test_file:
            break
    
    if not test_file:
        print("⚠️  未找到测试PPTX文件，跳过测试")
        return False
    
    print(f"📄 测试文件: {test_file}")
    
    loader = DocumentLoader()
    
    # 复制到临时目录测试
    temp_dir = tempfile.mkdtemp()
    temp_pptx = os.path.join(temp_dir, "test.pptx")
    shutil.copy2(test_file, temp_pptx)
    
    try:
        print("🔄 开始转换...")
        pdf_path = loader.convert_to_pdf(temp_pptx)
        
        if pdf_path and os.path.exists(pdf_path):
            pdf_size = os.path.getsize(pdf_path) / 1024 / 1024
            print(f"✅ 转换成功！")
            print(f"   PDF路径: {pdf_path}")
            print(f"   PDF大小: {pdf_size:.2f} MB")
            return True
        else:
            print("❌ 转换失败")
            return False
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

def test_convert_docx():
    """测试DOCX转换"""
    print("\n" + "="*60)
    print("测试3: DOCX转PDF转换")
    print("="*60)
    
    # 查找测试DOCX文件
    import glob
    test_files = glob.glob("/home/honglianglu/hdd/rag-agent/data/default/*.docx")
    
    if not test_files:
        print("⚠️  未找到测试DOCX文件，跳过测试")
        return False
    
    test_file = test_files[0]
    print(f"📄 测试文件: {test_file}")
    
    loader = DocumentLoader()
    
    # 复制到临时目录测试
    temp_dir = tempfile.mkdtemp()
    temp_docx = os.path.join(temp_dir, "test.docx")
    shutil.copy2(test_file, temp_docx)
    
    try:
        print("🔄 开始转换...")
        pdf_path = loader.convert_to_pdf(temp_docx)
        
        if pdf_path and os.path.exists(pdf_path):
            pdf_size = os.path.getsize(pdf_path) / 1024 / 1024
            print(f"✅ 转换成功！")
            print(f"   PDF路径: {pdf_path}")
            print(f"   PDF大小: {pdf_size:.2f} MB")
            return True
        else:
            print("❌ 转换失败")
            return False
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

def test_load_pptx():
    """测试完整的PPTX加载流程"""
    print("\n" + "="*60)
    print("测试4: 完整PPTX加载流程（转换+MinerU）")
    print("="*60)
    
    import glob
    test_files = glob.glob("/home/honglianglu/hdd/rag-agent/data/default/*.pptx")
    
    if not test_files:
        print("⚠️  未找到测试PPTX文件，跳过测试")
        return False
    
    test_file = test_files[0]
    print(f"📄 测试文件: {test_file}")
    
    loader = DocumentLoader()
    
    try:
        print("🔄 加载PPTX（会自动转换为PDF并用MinerU处理）...")
        slides = loader.load_pptx(test_file)
        
        if slides:
            print(f"✅ 加载成功！")
            print(f"   幻灯片数量: {len(slides)}")
            print(f"   第一页预览: {slides[0]['text'][:100]}...")
            return True
        else:
            print("❌ 加载失败，未提取到内容")
            return False
    except Exception as e:
        print(f"❌ 加载失败: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """主测试函数"""
    print("\n" + "="*70)
    print("🧪 LibreOffice 转换功能测试")
    print("="*70)
    
    results = []
    
    # 测试1: LibreOffice可用性
    results.append(("LibreOffice可用性", test_libreoffice_available()))
    
    # 只有当LibreOffice可用时才继续测试
    if results[0][1]:
        # 测试2: PPTX转换
        results.append(("PPTX转PDF", test_convert_pptx()))
        
        # 测试3: DOCX转换
        results.append(("DOCX转PDF", test_convert_docx()))
        
        # 测试4: 完整流程
        results.append(("完整PPTX加载", test_load_pptx()))
    
    # 打印总结
    print("\n" + "="*70)
    print("📊 测试总结")
    print("="*70)
    
    for name, passed in results:
        status = "✅ 通过" if passed else "❌ 失败"
        print(f"  {name:20s} : {status}")
    
    total = len(results)
    passed = sum(1 for _, p in results if p)
    
    print(f"\n  总计: {passed}/{total} 测试通过")
    
    if passed == total:
        print("\n🎉 所有测试通过！LibreOffice转换功能正常工作。")
    else:
        print("\n⚠️  部分测试失败，请检查日志。")
    
    print("="*70 + "\n")

if __name__ == "__main__":
    main()



