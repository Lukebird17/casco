#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
环境检查脚本
检查所有必要的依赖和配置是否就绪
"""

import sys
import os


def check_python_version():
    """检查 Python 版本"""
    version = sys.version_info
    print(f"✓ Python 版本: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("  ⚠️  警告: 推荐使用 Python 3.8 或更高版本")
        return False
    return True


def check_package(package_name, import_name=None):
    """检查 Python 包是否已安装"""
    if import_name is None:
        import_name = package_name
    
    try:
        __import__(import_name)
        print(f"✓ {package_name} 已安装")
        return True
    except ImportError:
        print(f"✗ {package_name} 未安装")
        return False


def check_env_var(var_name, description):
    """检查环境变量是否设置"""
    value = os.getenv(var_name)
    if value:
        # 隐藏敏感信息
        if "KEY" in var_name or "PASSWORD" in var_name:
            display_value = value[:8] + "..." if len(value) > 8 else "***"
        else:
            display_value = value
        print(f"✓ {var_name}: {display_value}")
        return True
    else:
        print(f"✗ {var_name} 未设置 ({description})")
        return False


def check_directory(dir_path, description):
    """检查目录是否存在"""
    if os.path.exists(dir_path):
        print(f"✓ {description}: {dir_path}")
        return True
    else:
        print(f"✗ {description} 不存在: {dir_path}")
        return False


def main():
    """主检查函数"""
    print("="*60)
    print("RAG 问答系统环境检查")
    print("="*60)
    
    all_ok = True
    
    # 1. 检查 Python 版本
    print("\n1. Python 版本检查")
    print("-"*60)
    if not check_python_version():
        all_ok = False
    
    # 2. 检查核心依赖
    print("\n2. 核心依赖检查")
    print("-"*60)
    packages = [
        ("python-dotenv", "dotenv"),
        ("openai", "openai"),
        ("raganything", "raganything"),
        ("lightrag", "lightrag"),
        ("langchain", "langchain"),
        ("langchain-openai", "langchain_openai"),
        ("tiktoken", "tiktoken"),
        ("numpy", "numpy"),
    ]
    
    for pkg_name, import_name in packages:
        if not check_package(pkg_name, import_name):
            all_ok = False
    
    # 3. 检查可选依赖
    print("\n3. 可选依赖检查")
    print("-"*60)
    optional_packages = [
        ("pillow", "PIL"),
        ("reportlab", "reportlab"),
    ]
    
    for pkg_name, import_name in optional_packages:
        check_package(pkg_name, import_name)  # 可选，不影响 all_ok
    
    # 4. 检查环境变量
    print("\n4. 环境变量检查")
    print("-"*60)
    env_vars = [
        ("CLOUD_API_KEY", "LLM API Key"),
        ("CLOUD_BASE_URL", "LLM Base URL"),
        ("CLOUD_MODEL", "LLM 模型名称"),
        ("OPENAI_API_KEY", "Embedding API Key"),
        ("OPENAI_BASE_URL", "Embedding Base URL"),
        ("OPENAI_API_MODEL", "Embedding 模型名称"),
    ]
    
    env_ok = True
    for var_name, description in env_vars:
        if not check_env_var(var_name, description):
            env_ok = False
    
    if not env_ok:
        print("\n  💡 提示: 请运行以下命令设置环境变量:")
        print("     source env.sh")
        all_ok = False
    
    # 5. 检查目录结构
    print("\n5. 目录结构检查")
    print("-"*60)
    dirs = [
        ("/home/honglianglu/ssd/casco/data", "数据目录"),
        ("/home/honglianglu/ssd/casco/RAG-Anything", "RAG-Anything 框架"),
        ("/home/honglianglu/ssd/casco/ocr_demo_project/示例模板.json", "示例模板文件"),
    ]
    
    for dir_path, description in dirs:
        if not check_directory(dir_path, description):
            # 目录不存在不是致命错误，只是警告
            pass
    
    # 6. 检查 RAG-Anything 安装
    print("\n6. RAG-Anything 安装检查")
    print("-"*60)
    try:
        from raganything import RAGAnything, RAGAnythingConfig
        print("✓ RAG-Anything 核心模块可用")
        print("✓ RAGAnything 类可导入")
        print("✓ RAGAnythingConfig 类可导入")
    except ImportError as e:
        print(f"✗ RAG-Anything 导入失败: {e}")
        print("  💡 请运行: cd RAG-Anything && pip install -e .")
        all_ok = False
    
    # 总结
    print("\n" + "="*60)
    if all_ok:
        print("✅ 环境检查通过！所有必要的依赖和配置都已就绪。")
        print("\n下一步：")
        print("  python quick_start.py  # 开始使用")
    else:
        print("⚠️  环境检查发现问题，请按照上述提示进行修复。")
        print("\n修复步骤：")
        print("  1. 安装缺失的依赖:")
        print("     ./install_dependencies.sh")
        print("  2. 配置环境变量:")
        print("     cp env_example.sh env.sh")
        print("     编辑 env.sh 填入您的配置")
        print("     source env.sh")
        print("  3. 重新运行检查:")
        print("     python check_environment.py")
    print("="*60)
    
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())

