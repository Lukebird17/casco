#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
API 配置测试脚本
快速检查 LLM 和 Embedding API 是否配置正确
"""

import os
import asyncio
from dotenv import load_dotenv
from openai import OpenAI, AsyncOpenAI

# 加载环境变量
load_dotenv()

def test_env_vars():
    """测试环境变量是否设置"""
    print("=" * 60)
    print("检查环境变量")
    print("=" * 60)
    
    required_vars = {
        'CLOUD_MODEL': os.getenv('CLOUD_MODEL'),
        'CLOUD_API_KEY': os.getenv('CLOUD_API_KEY'),
        'CLOUD_BASE_URL': os.getenv('CLOUD_BASE_URL'),
        'OPENAI_API_KEY': os.getenv('OPENAI_API_KEY'),
        'OPENAI_BASE_URL': os.getenv('OPENAI_BASE_URL'),
        'OPENAI_API_MODEL': os.getenv('OPENAI_API_MODEL'),
    }
    
    all_ok = True
    for key, value in required_vars.items():
        if value:
            # 隐藏敏感信息
            if 'KEY' in key:
                display = value[:10] + '...' if len(value) > 10 else '***'
            else:
                display = value
            print(f"✓ {key}: {display}")
        else:
            print(f"✗ {key}: 未设置")
            all_ok = False
    
    print()
    return all_ok


def test_llm_api():
    """测试 LLM API"""
    print("=" * 60)
    print("测试 LLM API")
    print("=" * 60)
    
    try:
        client = OpenAI(
            api_key=os.getenv('CLOUD_API_KEY'),
            base_url=os.getenv('CLOUD_BASE_URL')
        )
        
        print(f"API Base URL: {os.getenv('CLOUD_BASE_URL')}")
        print(f"模型: {os.getenv('CLOUD_MODEL')}")
        print("发送测试请求...")
        
        response = client.chat.completions.create(
            model=os.getenv('CLOUD_MODEL', 'gpt-3.5-turbo'),
            messages=[
                {"role": "user", "content": "你好，请用一句话回复"}
            ],
            max_tokens=50
        )
        
        print(f"✓ LLM API 测试成功!")
        print(f"回复: {response.choices[0].message.content}")
        print()
        return True
        
    except Exception as e:
        print(f"✗ LLM API 测试失败!")
        print(f"错误: {e}")
        print()
        return False


def test_embedding_api():
    """测试 Embedding API"""
    print("=" * 60)
    print("测试 Embedding API")
    print("=" * 60)
    
    try:
        client = OpenAI(
            api_key=os.getenv('OPENAI_API_KEY'),
            base_url=os.getenv('OPENAI_BASE_URL')
        )
        
        print(f"API Base URL: {os.getenv('OPENAI_BASE_URL')}")
        print(f"模型: {os.getenv('OPENAI_API_MODEL')}")
        print("发送测试请求...")
        
        response = client.embeddings.create(
            model=os.getenv('OPENAI_API_MODEL', 'text-embedding-3-large'),
            input="测试文本"
        )
        
        embedding = response.data[0].embedding
        print(f"✓ Embedding API 测试成功!")
        print(f"向量维度: {len(embedding)}")
        print(f"向量示例: [{embedding[0]:.6f}, {embedding[1]:.6f}, ...]")
        print()
        return True
        
    except Exception as e:
        print(f"✗ Embedding API 测试失败!")
        print(f"错误: {e}")
        print()
        print("常见问题:")
        print("1. 检查 OPENAI_BASE_URL 是否正确")
        print("   - OpenAI: https://api.openai.com/v1")
        print("   - 如果用同一个 DeepSeek API，应该设置为:")
        print("     export OPENAI_BASE_URL=$CLOUD_BASE_URL")
        print("     export OPENAI_API_KEY=$CLOUD_API_KEY")
        print()
        print("2. 检查模型名称是否正确")
        print("   - OpenAI: text-embedding-3-large")
        print("   - DeepSeek: 可能不支持 embedding，需要用 OpenAI")
        print()
        return False


async def test_async_embedding():
    """测试异步 Embedding API"""
    print("=" * 60)
    print("测试异步 Embedding API")
    print("=" * 60)
    
    try:
        client = AsyncOpenAI(
            api_key=os.getenv('OPENAI_API_KEY'),
            base_url=os.getenv('OPENAI_BASE_URL')
        )
        
        print("发送异步测试请求...")
        
        response = await client.embeddings.create(
            model=os.getenv('OPENAI_API_MODEL', 'text-embedding-3-large'),
            input=["测试文本1", "测试文本2"]
        )
        
        print(f"✓ 异步 Embedding API 测试成功!")
        print(f"批量处理: {len(response.data)} 个文本")
        print()
        return True
        
    except Exception as e:
        print(f"✗ 异步 Embedding API 测试失败!")
        print(f"错误: {e}")
        print()
        return False


def print_config_guide():
    """打印配置指南"""
    print("\n" + "=" * 60)
    print("配置指南")
    print("=" * 60)
    print()
    print("如果你使用 DeepSeek:")
    print("---")
    print("# LLM 使用 DeepSeek")
    print("export CLOUD_MODEL='deepseek-chat'")
    print("export CLOUD_API_KEY='your_deepseek_key'")
    print("export CLOUD_BASE_URL='https://api.deepseek.com/v1'")
    print()
    print("# Embedding 必须使用 OpenAI（DeepSeek 不支持）")
    print("export OPENAI_API_KEY='your_openai_key'")
    print("export OPENAI_BASE_URL='https://api.openai.com/v1'")
    print("export OPENAI_API_MODEL='text-embedding-3-large'")
    print()
    print("如果你都使用 OpenAI:")
    print("---")
    print("# LLM")
    print("export CLOUD_MODEL='gpt-4o-mini'")
    print("export CLOUD_API_KEY='your_openai_key'")
    print("export CLOUD_BASE_URL='https://api.openai.com/v1'")
    print()
    print("# Embedding")
    print("export OPENAI_API_KEY='your_openai_key'")
    print("export OPENAI_BASE_URL='https://api.openai.com/v1'")
    print("export OPENAI_API_MODEL='text-embedding-3-large'")
    print()
    print("修改 env.sh 后，记得重新加载:")
    print("  source env.sh")
    print("=" * 60)


async def main():
    """主函数"""
    print("\n" + "=" * 60)
    print("API 配置测试工具")
    print("=" * 60)
    print()
    
    # 1. 检查环境变量
    env_ok = test_env_vars()
    
    if not env_ok:
        print("⚠️  请先设置所有必需的环境变量")
        print("   编辑 env.sh 并运行: source env.sh")
        print_config_guide()
        return
    
    # 2. 测试 LLM API
    llm_ok = test_llm_api()
    
    # 3. 测试 Embedding API
    embed_ok = test_embedding_api()
    
    # 4. 测试异步 Embedding
    if embed_ok:
        async_ok = await test_async_embedding()
    
    # 总结
    print("=" * 60)
    print("测试总结")
    print("=" * 60)
    
    if llm_ok and embed_ok:
        print("✅ 所有 API 测试通过！")
        print("   你可以运行: python rag_qa_agent.py")
    else:
        print("❌ 部分 API 测试失败")
        if not llm_ok:
            print("   - LLM API 有问题")
        if not embed_ok:
            print("   - Embedding API 有问题（这是你当前的问题）")
        print()
        print("请检查配置并重新测试:")
        print("  nano env.sh")
        print("  source env.sh")
        print("  python test_api.py")
        
        print_config_guide()
    
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())

