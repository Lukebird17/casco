#!/bin/bash
# 环境变量配置示例
# 使用方法：
# 1. 复制此文件为 env.sh: cp env_example.sh env.sh
# 2. 修改 env.sh 填入您的实际配置
# 3. 运行: source env.sh

# ============= LLM 配置 =============
# 使用 DeepSeek API
export CLOUD_MODEL="deepseek-chat"
export CLOUD_API_KEY="your_deepseek_api_key_here"
export CLOUD_BASE_URL="https://api.deepseek.com/v1"

# 或者使用 OpenAI API
# export CLOUD_MODEL="gpt-4o-mini"
# export CLOUD_API_KEY="your_openai_api_key_here"
# export CLOUD_BASE_URL="https://api.openai.com/v1"

# ============= Vision Model 配置（用于图像、表格处理）=============
# 如果不设置，默认使用 LLM 的配置
# 如果你的 LLM 不支持 vision，需要单独配置支持 vision 的模型
# export VISION_MODEL="gpt-4o"
# export VISION_API_KEY="your_openai_api_key"
# export VISION_BASE_URL="https://api.openai.com/v1"

# ============= Embedding 配置 =============
export OPENAI_API_KEY="your_openai_api_key_here"
export OPENAI_BASE_URL="https://api.openai.com/v1"
export OPENAI_API_MODEL="text-embedding-3-large"

# ============= HuggingFace 配置（解决网络问题）=============
# 使用国内镜像加速模型下载
export HF_ENDPOINT=https://hf-mirror.com
export HF_HUB_ENABLE_HF_TRANSFER=1

# 如果使用代理（可选）
# export HTTP_PROXY=http://your-proxy:port
# export HTTPS_PROXY=http://your-proxy:port

# ============= 可选配置 =============
# RAG 工作目录
export WORKING_DIR="./rag_storage"

# 解析器配置
export PARSER="mineru"
export PARSE_METHOD="auto"

echo "✅ 环境变量已加载"
echo "使用的 LLM 模型: $CLOUD_MODEL"
echo "使用的 Embedding 模型: $OPENAI_API_MODEL"
echo "HuggingFace 镜像: $HF_ENDPOINT"

