#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
httpx 兼容性诊断脚本
"""

import sys
import inspect

print("="*70)
print("  httpx 兼容性诊断")
print("="*70)

# 1. 检查 httpx
try:
    import httpx
    print(f"\n✅ httpx 已安装")
    print(f"   版本: {httpx.__version__}")
    print(f"   位置: {httpx.__file__}")
    
    # 检查 AsyncClient 参数
    sig = inspect.signature(httpx.AsyncClient.__init__)
    params = list(sig.parameters.keys())
    
    print(f"\n   AsyncClient 参数 (前20个):")
    for p in params[:20]:
        print(f"     - {p}")
    
    # 关键参数
    has_proxies = 'proxies' in params
    has_proxy = 'proxy' in params
    
    print(f"\n   关键参数检查:")
    print(f"     支持 'proxies': {has_proxies} {'✅' if has_proxies else '❌'}")
    print(f"     支持 'proxy': {has_proxy} {'✅' if has_proxy else '❌'}")
    
    # 判断版本类型
    if has_proxies and not has_proxy:
        print(f"\n   ✅ 检测到: httpx 0.27.x (旧API)")
        print(f"      兼容: openai < 1.50")
    elif has_proxy and not has_proxies:
        print(f"\n   ⚠️  检测到: httpx 0.28.x (新API)")
        print(f"      兼容: openai >= 1.50")
        print(f"      问题: 如果看到 'proxies' 错误，说明 openai 版本不匹配")
    elif has_proxies and has_proxy:
        print(f"\n   ℹ️  检测到: httpx 过渡版本（同时支持新旧API）")
    else:
        print(f"\n   ❌ 未知版本")
    
except ImportError as e:
    print(f"\n❌ httpx 未安装: {e}")
    sys.exit(1)

# 2. 检查 openai
print("\n" + "="*70)
try:
    import openai
    print(f"✅ openai 已安装")
    print(f"   版本: {openai.__version__}")
    print(f"   位置: {openai.__file__}")
    
    # 检查版本号
    version_parts = openai.__version__.split('.')
    major = int(version_parts[0])
    minor = int(version_parts[1]) if len(version_parts) > 1 else 0
    
    if major == 1 and minor < 50:
        print(f"\n   ℹ️  openai < 1.50，使用旧 API (proxies)")
        print(f"      需要: httpx 0.27.x")
    elif major == 1 and minor >= 50:
        print(f"\n   ℹ️  openai >= 1.50，使用新 API (proxy)")
        print(f"      需要: httpx 0.27.x (如果兼容旧版) 或 0.28.x")
    else:
        print(f"\n   ⚠️  openai 版本较旧或较新")
    
except ImportError as e:
    print(f"❌ openai 未安装: {e}")

# 3. 兼容性总结
print("\n" + "="*70)
print("  兼容性总结")
print("="*70)

try:
    import httpx
    import openai
    
    httpx_version = httpx.__version__
    openai_version = openai.__version__
    
    # 提取版本号
    httpx_minor = int(httpx_version.split('.')[1])
    openai_minor = int(openai_version.split('.')[1])
    
    print(f"\n当前组合:")
    print(f"  httpx: {httpx_version}")
    print(f"  openai: {openai_version}")
    
    # 推荐组合
    print(f"\n推荐组合:")
    print(f"  ✅ openai 1.40-1.60 + httpx 0.27.x")
    print(f"  ✅ openai 1.70+ + httpx 0.28.x")
    
    # 判断当前是否兼容
    if httpx_minor == 27 and 40 <= openai_minor <= 60:
        print(f"\n✅ 当前组合应该兼容")
    elif httpx_minor == 28 and openai_minor >= 70:
        print(f"\n✅ 当前组合应该兼容")
    else:
        print(f"\n⚠️  当前组合可能不兼容")
        
        if httpx_minor == 28 and openai_minor < 70:
            print(f"   建议: 降级 httpx 到 0.27.2")
            print(f"   命令: pip install 'httpx==0.27.2' --force-reinstall")
        elif httpx_minor == 27 and openai_minor > 60:
            print(f"   建议: 升级 httpx 到 0.28.x 或降级 openai")
            
except Exception as e:
    print(f"❌ 检查失败: {e}")

# 4. 测试实际创建
print("\n" + "="*70)
print("  实际测试")
print("="*70)

try:
    import httpx
    
    print(f"\n测试 1: 创建 AsyncClient (无参数)")
    try:
        client = httpx.AsyncClient(timeout=10.0)
        print(f"  ✅ 成功")
    except Exception as e:
        print(f"  ❌ 失败: {e}")
    
    print(f"\n测试 2: 创建 AsyncClient (带 proxies - 旧API)")
    try:
        client = httpx.AsyncClient(proxies={"http://": None}, timeout=10.0)
        print(f"  ✅ 成功 - httpx 支持旧 API")
    except TypeError as e:
        if 'proxies' in str(e):
            print(f"  ❌ 失败 - httpx 不支持旧 API: {e}")
            print(f"     这就是你遇到的错误！")
    except Exception as e:
        print(f"  ⚠️  其他错误: {e}")
    
    print(f"\n测试 3: 创建 AsyncClient (带 proxy - 新API)")
    try:
        client = httpx.AsyncClient(proxy=None, timeout=10.0)
        print(f"  ✅ 成功 - httpx 支持新 API")
    except TypeError as e:
        if 'proxy' in str(e):
            print(f"  ❌ 失败 - httpx 不支持新 API: {e}")
    except Exception as e:
        print(f"  ⚠️  其他错误: {e}")
        
except Exception as e:
    print(f"❌ 测试失败: {e}")

# 5. 解决方案
print("\n" + "="*70)
print("  解决方案")
print("="*70)

print(f"""
如果看到 'proxies' 错误，执行:

conda activate casco
pip uninstall -y httpx httpcore
pip install "httpx==0.27.2" "httpcore==1.0.2" --force-reinstall --no-cache-dir

然后重新运行此脚本验证。
""")

print("="*70)

