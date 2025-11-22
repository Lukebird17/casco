#!/bin/bash
# 环境变量配置 - DeepSeek 版本
# 使用方法：source env.sh

# ============= LLM 配置 (DeepSeek) =============
export CLOUD_MODEL="DeepSeek-V3-0324"
export CLOUD_API_KEY="sk-wxZp2QgCmvkdng8o9dHhyvBAU8MJOUjjsSx5fJDO7l31KJhA"  # 👈 在 https://platform.deepseek.com 获取
export CLOUD_BASE_URL="https://ai.api.coregpu.cn/v1/"

# ============= Vision Model 配置 =============
# DeepSeek 暂不支持 vision，使用 OpenAI 或其他
export VISION_MODEL="Qwen2.5-VL-72B-Instruct"  # 或其他支持vision的模型
export VISION_API_KEY="sk-wxZp2QgCmvkdng8o9dHhyvBAU8MJOUjjsSx5fJDO7l31KJhA"  # OpenAI API Key
export VISION_BASE_URL="https://ai.api.coregpu.cn/v1/"

# ============= Embedding 配置 (保持原样) =============
export OPENAI_API_KEY="sk-aqrqxoeqrbfsfhvjhjpozbivejsqhhsqvagukbdlbzjfaawr"
export OPENAI_BASE_URL="https://api.siliconflow.cn/v1/"
export OPENAI_API_MODEL="BAAI/bge-m3"

# ============= 可选配置 =============
export WORKING_DIR="./rag_storage"
export PARSER="mineru"
export PARSE_METHOD="auto"

echo "✅ 环境变量已加载"
echo "使用的 LLM 模型: $CLOUD_MODEL"
echo "使用的 Embedding 模型: $OPENAI_API_MODEL"
