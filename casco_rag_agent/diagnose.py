#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
完整的配置诊断工具
"""

import os
import sys
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

def print_section(title):
    """打印分节标题"""
    print(f"\n{'='*70}")
    print(f"  {title}")
    print(f"{'='*70}")

def check_var(name, value, required=True):
    """检查单个环境变量"""
    if value:
        # 隐藏敏感信息
        if 'KEY' in name or 'PASSWORD' in name:
            display = value[:10] + '...' if len(value) > 10 else '***'
        else:
            display = value
        status = "✅"
        print(f"{status} {name:25s} = {display}")
        return True
    else:
        status = "❌" if required else "⚠️ "
        print(f"{status} {name:25s} = 未设置")
        return not required

def main():
    print("\n" + "="*70)
    print("  RAG 系统配置诊断工具")
    print("="*70)
    
    all_ok = True
    
    # 1. LLM 配置
    print_section("LLM 配置（用于文本生成和实体提取）")
    llm_model = os.getenv('CLOUD_MODEL')
    llm_key = os.getenv('CLOUD_API_KEY')
    llm_url = os.getenv('CLOUD_BASE_URL')
    
    all_ok &= check_var('CLOUD_MODEL', llm_model)
    all_ok &= check_var('CLOUD_API_KEY', llm_key)
    all_ok &= check_var('CLOUD_BASE_URL', llm_url)
    
    if llm_model:
        print(f"\n💡 当前 LLM 模型: {llm_model}")
        if 'qwen' in llm_model.lower():
            print("   ℹ️  检测到 Qwen 模型")
            print("   ⚠️  确保你的 API 端点支持此模型")
        elif 'deepseek' in llm_model.lower():
            print("   ℹ️  检测到 DeepSeek 模型")
        elif 'gpt' in llm_model.lower():
            print("   ℹ️  检测到 OpenAI GPT 模型")
        
        if 'vl' in llm_model.lower() or 'vision' in llm_model.lower():
            print("   ℹ️  这是一个 Vision 模型，支持图像处理")
    
    # 2. Vision Model 配置
    print_section("Vision Model 配置（用于图像、表格处理）")
    vision_model = os.getenv('VISION_MODEL')
    vision_key = os.getenv('VISION_API_KEY')
    vision_url = os.getenv('VISION_BASE_URL')
    
    if vision_model:
        check_var('VISION_MODEL', vision_model, required=False)
        check_var('VISION_API_KEY', vision_key, required=False)
        check_var('VISION_BASE_URL', vision_url, required=False)
        print(f"\n💡 使用独立的 Vision 模型: {vision_model}")
    else:
        print("⚠️  VISION_MODEL 未设置")
        print(f"💡 将使用 LLM 模型处理图像: {llm_model}")
        if llm_model and 'vl' not in llm_model.lower() and 'vision' not in llm_model.lower():
            print("   ⚠️  警告: 该 LLM 模型可能不支持图像处理")
            print("   建议设置支持 vision 的模型，例如:")
            print("      export VISION_MODEL='gpt-4o'")
    
    # 3. Embedding 配置
    print_section("Embedding 配置（用于向量化文档）")
    emb_model = os.getenv('OPENAI_API_MODEL')
    emb_key = os.getenv('OPENAI_API_KEY')
    emb_url = os.getenv('OPENAI_BASE_URL')
    
    all_ok &= check_var('OPENAI_API_MODEL', emb_model)
    all_ok &= check_var('OPENAI_API_KEY', emb_key)
    all_ok &= check_var('OPENAI_BASE_URL', emb_url)
    
    if emb_model:
        print(f"\n💡 Embedding 模型: {emb_model}")
        dim_map = {
            'text-embedding-3-large': 3072,
            'text-embedding-3-small': 1536,
            'text-embedding-ada-002': 1536,
            'bge-m3': 1024,
        }
        for key, dim in dim_map.items():
            if key in emb_model:
                print(f"   向量维度: {dim}")
                break
    
    # 4. HuggingFace 配置
    print_section("HuggingFace 配置（用于下载模型）")
    hf_endpoint = os.getenv('HF_ENDPOINT')
    check_var('HF_ENDPOINT', hf_endpoint, required=False)
    if not hf_endpoint:
        print("   建议设置: export HF_ENDPOINT=https://hf-mirror.com")
    
    # 5. 配置一致性检查
    print_section("配置一致性检查")
    
    issues = []
    
    # 检查 API URL 是否匹配
    if llm_url and emb_url and llm_url == emb_url:
        print("✅ LLM 和 Embedding 使用相同的 API 端点")
        if llm_key != emb_key:
            issues.append("⚠️  LLM 和 Embedding 使用相同端点但不同的 API Key")
    else:
        print("ℹ️  LLM 和 Embedding 使用不同的 API 端点（这是正常的）")
    
    # 检查模型名称
    if llm_model:
        if 'qwen' in llm_model.lower():
            if 'siliconflow' not in str(llm_url).lower() and 'dashscope' not in str(llm_url).lower():
                issues.append(f"⚠️  Qwen 模型通常需要特定的 API 端点")
                issues.append(f"   当前 URL: {llm_url}")
                issues.append(f"   确认此端点支持: {llm_model}")
    
    if issues:
        print("\n发现潜在问题:")
        for issue in issues:
            print(f"  {issue}")
    else:
        print("✅ 未发现明显的配置冲突")
    
    # 6. 推荐配置
    print_section("推荐配置示例")
    
    print("\n方案 1: DeepSeek + OpenAI (推荐)")
    print("-" * 70)
    print("# LLM 用 DeepSeek（便宜）")
    print("export CLOUD_MODEL='deepseek-chat'")
    print("export CLOUD_API_KEY='sk-your-deepseek-key'")
    print("export CLOUD_BASE_URL='https://api.deepseek.com/v1'")
    print()
    print("# Vision 用 OpenAI gpt-4o-mini（支持图像）")
    print("export VISION_MODEL='gpt-4o-mini'")
    print("export VISION_API_KEY='sk-your-openai-key'")
    print("export VISION_BASE_URL='https://api.openai.com/v1'")
    print()
    print("# Embedding 用 OpenAI")
    print("export OPENAI_API_KEY='sk-your-openai-key'")
    print("export OPENAI_BASE_URL='https://api.openai.com/v1'")
    print("export OPENAI_API_MODEL='text-embedding-3-large'")
    
    print("\n方案 2: 全部 OpenAI")
    print("-" * 70)
    print("export CLOUD_MODEL='gpt-4o-mini'")
    print("export CLOUD_API_KEY='sk-your-openai-key'")
    print("export CLOUD_BASE_URL='https://api.openai.com/v1'")
    print("export OPENAI_API_KEY='sk-your-openai-key'")
    print("export OPENAI_BASE_URL='https://api.openai.com/v1'")
    print("export OPENAI_API_MODEL='text-embedding-3-large'")
    
    if llm_model and 'qwen' in llm_model.lower():
        print("\n方案 3: 当前 Qwen 配置（确保 API 正确）")
        print("-" * 70)
        print(f"export CLOUD_MODEL='{llm_model}'")
        print(f"export CLOUD_API_KEY='your-api-key'")
        print(f"export CLOUD_BASE_URL='{llm_url}'  # 确保此 API 支持 {llm_model}")
        print()
        print("# 如果 Qwen 不支持 vision，需要单独配置")
        print("export VISION_MODEL='gpt-4o-mini'  # 或其他支持 vision 的模型")
        print("export VISION_API_KEY='sk-openai-key'")
        print("export VISION_BASE_URL='https://api.openai.com/v1'")
    
    # 总结
    print_section("诊断总结")
    
    if all_ok:
        print("✅ 所有必需的环境变量已配置")
        print("\n下一步:")
        print("  1. 测试 API: python test_api.py")
        print("  2. 运行系统: python rag_qa_agent.py")
    else:
        print("❌ 发现配置问题")
        print("\n请执行:")
        print("  1. 编辑 env.sh: nano env.sh")
        print("  2. 重新加载: source env.sh")
        print("  3. 重新诊断: python diagnose.py")
    
    print("\n" + "="*70)
    
    return 0 if all_ok else 1

if __name__ == "__main__":
    sys.exit(main())

