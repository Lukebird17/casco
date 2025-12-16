#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
演示MinerU加速效果
展示缓存机制如何大幅提升处理速度
"""

import time
from pathlib import Path
from enhanced_ocr import EnhancedOCRProcessor


def demo_cache_acceleration():
    """演示缓存加速效果"""
    
    print("\n" + "="*70)
    print("MinerU 加速演示：缓存机制")
    print("="*70 + "\n")
    
    # 查找一个测试文件
    data_dir = Path("data")
    test_file = None
    
    for ext in ['.pdf', '.pptx', '.docx']:
        files = list(data_dir.rglob(f'*{ext}'))
        if files:
            test_file = str(files[0])
            break
    
    if not test_file:
        print("❌ 未找到测试文件")
        return
    
    print(f"📄 测试文件: {Path(test_file).name}\n")
    
    # 初始化处理器（启用缓存）
    processor = EnhancedOCRProcessor(use_cache=True)
    
    # 第一次处理（无缓存）
    print("🔄 第一次处理（需要运行MinerU）...")
    print("-" * 70)
    start_time = time.time()
    
    result1 = processor.process_file(test_file)
    
    time1 = time.time() - start_time
    print(f"\n⏱️  耗时: {time1:.2f} 秒")
    
    if not result1:
        print("❌ 处理失败")
        return
    
    # 第二次处理（有缓存）
    print("\n" + "="*70)
    print("🔄 第二次处理（从缓存读取）...")
    print("-" * 70)
    start_time = time.time()
    
    result2 = processor.process_file(test_file)
    
    time2 = time.time() - start_time
    print(f"\n⏱️  耗时: {time2:.2f} 秒")
    
    # 对比结果
    print("\n" + "="*70)
    print("📊 加速效果对比")
    print("="*70)
    print(f"第一次处理（无缓存）: {time1:.2f} 秒")
    print(f"第二次处理（有缓存）: {time2:.2f} 秒")
    
    if time1 > 0 and time2 > 0:
        speedup = time1 / time2
        print(f"\n🚀 加速倍数: {speedup:.1f}x")
        print(f"⚡ 速度提升: {((time1 - time2) / time1 * 100):.1f}%")
    
    print("\n💡 提示:")
    print("  - 首次处理需要运行MinerU（较慢）")
    print("  - 后续处理直接读取缓存（极快）")
    print("  - 缓存目录: .mineru_cache/")
    print("\n" + "="*70 + "\n")


def show_cache_stats():
    """显示缓存统计"""
    import os
    
    cache_dir = ".mineru_cache"
    
    if not os.path.exists(cache_dir):
        print("📦 缓存目录不存在")
        return
    
    cache_files = [f for f in os.listdir(cache_dir) if f.endswith('.json')]
    
    print("\n📊 缓存统计:")
    print(f"  - 缓存文件数: {len(cache_files)}")
    
    if cache_files:
        total_size = sum(
            os.path.getsize(os.path.join(cache_dir, f)) 
            for f in cache_files
        )
        print(f"  - 缓存大小: {total_size / 1024:.2f} KB")
        print(f"  - 缓存目录: {cache_dir}/")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--stats":
        show_cache_stats()
    else:
        demo_cache_acceleration()
        show_cache_stats()

