#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
配置文件 - 统一管理所有路径和配置
"""

import os
from pathlib import Path

# ============= 项目路径配置 =============

# 获取当前文件所在目录（agent 目录）
AGENT_DIR = Path(__file__).parent.absolute()

# 项目根目录（casco 目录）
PROJECT_ROOT = AGENT_DIR.parent

# 数据目录
DATA_DIR = PROJECT_ROOT / "data"

# RAG-Anything 目录
RAG_ANYTHING_DIR = PROJECT_ROOT / "RAG-Anything"

# OCR 示例模板文件
TEMPLATE_FILE = PROJECT_ROOT / "ocr_demo_project" / "示例模板.json"

# uv 可执行文件路径
UV_EXECUTABLE = PROJECT_ROOT / "uv-x86_64-unknown-linux-gnu" / "uv"

# ============= RAG 配置 =============

# RAG 工作目录
WORKING_DIR = AGENT_DIR / "rag_storage"

# 文档解析输出目录
OUTPUT_DIR = AGENT_DIR / "output"

# 查询结果输出文件
RESULTS_FILE = AGENT_DIR / "qa_results.json"

# 解析器配置
PARSER = os.getenv("PARSER", "mineru")
PARSE_METHOD = os.getenv("PARSE_METHOD", "auto")

# ============= API 配置 =============

# LLM 配置
CLOUD_MODEL = os.getenv("CLOUD_MODEL", "DeepSeek-V3-0324")
CLOUD_API_KEY = os.getenv("CLOUD_API_KEY","sk-wxZp2QgCmvkdng8o9dHhyvBAU8MJOUjjsSx5fJDO7l31KJhA")
CLOUD_BASE_URL = os.getenv("CLOUD_BASE_URL", "https://ai.api.coregpu.cn/v1/")

# Embedding 配置
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY","sk-aqrqxoeqrbfsfhvjhjpozbivejsqhhsqvagukbdlbzjfaawr")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.siliconflow.cn/v1/")
OPENAI_API_MODEL = os.getenv("OPENAI_API_MODEL", "BAAI/bge-m3")

VISION_MODEL = os.getenv("VISION_MODEL", "Qwen2.5-VL-72B-Instruct")
VISION_API_KEY = os.getenv("VISIOND_API_KEY","sk-wxZp2QgCmvkdng8o9dHhyvBAU8MJOUjjsSx5fJDO7l31KJhA")
VISION_BASE_URL = os.getenv("VISION_BASE_URL", "https://ai.api.coregpu.cn/v1/")
# ============= 多模态处理配置 =============

ENABLE_IMAGE_PROCESSING = True
ENABLE_TABLE_PROCESSING = True
ENABLE_EQUATION_PROCESSING = True

# ============= 批量处理配置 =============

MAX_WORKERS = 5  # 并行处理文档数量
SUPPORTED_EXTENSIONS = [".pdf", ".docx", ".pptx"]
RECURSIVE_PROCESSING = True

# ============= 辅助函数 =============

def get_data_dir(subdir: str = None) -> Path:
    """获取数据目录路径"""
    if subdir:
        return DATA_DIR / subdir
    return DATA_DIR


def get_output_dir() -> Path:
    """获取输出目录，不存在则创建"""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    return OUTPUT_DIR


def get_working_dir() -> Path:
    """获取工作目录，不存在则创建"""
    WORKING_DIR.mkdir(parents=True, exist_ok=True)
    return WORKING_DIR


def validate_config():
    """验证配置是否完整"""
    errors = []
    
    if not CLOUD_API_KEY:
        errors.append("未设置 CLOUD_API_KEY")
    
    if not OPENAI_API_KEY:
        errors.append("未设置 OPENAI_API_KEY")
    
    if not DATA_DIR.exists():
        errors.append(f"数据目录不存在: {DATA_DIR}")
    
    if not RAG_ANYTHING_DIR.exists():
        errors.append(f"RAG-Anything 目录不存在: {RAG_ANYTHING_DIR}")
    
    return errors


if __name__ == "__main__":
    # 测试配置
    print("=" * 60)
    print("配置信息")
    print("=" * 60)
    print(f"Agent 目录: {AGENT_DIR}")
    print(f"项目根目录: {PROJECT_ROOT}")
    print(f"数据目录: {DATA_DIR}")
    print(f"RAG-Anything 目录: {RAG_ANYTHING_DIR}")
    print(f"模板文件: {TEMPLATE_FILE}")
    print(f"工作目录: {WORKING_DIR}")
    print(f"输出目录: {OUTPUT_DIR}")
    print()
    print("API 配置:")
    print(f"  LLM 模型: {CLOUD_MODEL}")
    print(f"  LLM API Key: {'已设置' if CLOUD_API_KEY else '未设置'}")
    print(f"  Embedding API Key: {'已设置' if OPENAI_API_KEY else '未设置'}")
    print()
    print("验证配置:")
    errors = validate_config()
    if errors:
        print("❌ 发现以下问题:")
        for error in errors:
            print(f"  - {error}")
    else:
        print("✅ 配置验证通过")

