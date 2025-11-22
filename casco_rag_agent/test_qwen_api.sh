#!/bin/bash
# 测试 Qwen API 是否真的可用

echo "=========================================="
echo "测试 Qwen API"
echo "=========================================="
echo ""

# 从 env.sh 读取配置
source /home/honglianglu/ssd/casco/casco_rag_agent/env.sh

echo "配置信息:"
echo "  Model: $CLOUD_MODEL"
echo "  Base URL: $CLOUD_BASE_URL"
echo "  API Key: ${CLOUD_API_KEY:0:20}..."
echo ""

# 测试 1: 不带斜杠
echo "测试 1: 调用 API (移除末尾斜杠)"
BASE_URL_NO_SLASH="${CLOUD_BASE_URL%/}"  # 移除末尾斜杠
echo "  URL: ${BASE_URL_NO_SLASH}/chat/completions"

curl -s -X POST "${BASE_URL_NO_SLASH}/chat/completions" \
  -H "Authorization: Bearer $CLOUD_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{
    \"model\": \"$CLOUD_MODEL\",
    \"messages\": [{\"role\": \"user\", \"content\": \"你好\"}],
    \"max_tokens\": 10
  }" | python -m json.tool 2>/dev/null || echo "  请求失败或返回非JSON"

echo ""
echo "=========================================="
echo ""

# 测试 2: 尝试其他模型名称
echo "测试 2: 尝试不同的模型名称格式"

for model_name in \
  "Qwen2.5-VL-72B-Instruct" \
  "qwen2.5-vl-72b-instruct" \
  "Qwen/Qwen2.5-VL-72B-Instruct" \
  "Qwen2.5-72B-Instruct"
do
  echo "  尝试: $model_name"
  response=$(curl -s -X POST "${BASE_URL_NO_SLASH}/chat/completions" \
    -H "Authorization: Bearer $CLOUD_API_KEY" \
    -H "Content-Type: application/json" \
    -d "{
      \"model\": \"$model_name\",
      \"messages\": [{\"role\": \"user\", \"content\": \"测试\"}],
      \"max_tokens\": 5
    }" 2>&1)
  
  # 检查是否成功
  if echo "$response" | grep -q '"id"'; then
    echo "    ✅ 成功！使用这个模型名称"
    echo "    响应: $(echo $response | python -m json.tool 2>/dev/null | head -20)"
    break
  else
    error=$(echo "$response" | grep -o '"error"[^}]*}' | head -1)
    if [ -n "$error" ]; then
      echo "    ❌ 失败: $error"
    else
      echo "    ❌ 失败"
    fi
  fi
done

echo ""
echo "=========================================="
echo "建议："
echo "=========================================="
echo ""
echo "如果所有测试都失败，可能的原因："
echo "  1. API Key 无效"
echo "  2. API 端点不支持这个模型"
echo "  3. 需要联系 API 提供商确认模型名称"
echo ""
echo "替代方案 - 使用 DeepSeek（稳定且便宜）："
echo "  export CLOUD_MODEL='deepseek-chat'"
echo "  export CLOUD_API_KEY='sk-your-deepseek-key'"
echo "  export CLOUD_BASE_URL='https://api.deepseek.com/v1'"
echo ""

