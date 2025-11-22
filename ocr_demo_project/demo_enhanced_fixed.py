#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
增强版 Demo 的修复版本
自动清除可能导致 HuggingFace 下载问题的环境变量
"""

import os
import sys

# ===== 在导入任何其他模块之前，先修复环境变量 =====
print("🔧 修复 HuggingFace 环境配置...")

# 1. 清除所有代理设置
proxy_vars = ['http_proxy', 'https_proxy', 'HTTP_PROXY', 'HTTPS_PROXY', 'all_proxy', 'ALL_PROXY']
for var in proxy_vars:
    if var in os.environ:
        print(f"   清除: {var}")
        del os.environ[var]

# 2. 清除或修正 HF_ENDPOINT
if 'HF_ENDPOINT' in os.environ:
    old_endpoint = os.environ['HF_ENDPOINT']
    if 'hf-mirror.com' in old_endpoint:
        print(f"   清除: HF_ENDPOINT={old_endpoint}")
        del os.environ['HF_ENDPOINT']
        print("   改用: HuggingFace 官方源")
    else:
        print(f"   保留: HF_ENDPOINT={old_endpoint}")
else:
    print("   HF_ENDPOINT 未设置，使用官方源")

# 3. 设置缓存目录
hf_home = os.path.expanduser("~/.cache/huggingface")
os.environ['HF_HOME'] = hf_home
os.environ['HF_HUB_DISABLE_SYMLINKS_WARNING'] = '1'
os.makedirs(hf_home, exist_ok=True)
print(f"   缓存目录: {hf_home}")

print("✅ 环境配置完成\n")

# ===== 现在导入并运行原始的 demo_enhanced =====
# 导入 demo_enhanced 中的 main 函数并执行
try:
    # 读取并执行 demo_enhanced.py
    demo_file = os.path.join(os.path.dirname(__file__), 'demo_enhanced.py')
    
    with open(demo_file, 'r', encoding='utf-8') as f:
        demo_code = f.read()
    
    # 在当前环境中执行
    exec(demo_code, {'__name__': '__main__'})
    
except FileNotFoundError:
    print(f"❌ 找不到 demo_enhanced.py 文件")
    print(f"   请确保该文件在同一目录下")
    sys.exit(1)
except Exception as e:
    print(f"\n❌ 发生错误: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

