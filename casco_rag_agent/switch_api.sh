#!/bin/bash
# API 切换助手

echo "=========================================="
echo "  API 切换助手"
echo "=========================================="
echo ""

cd /home/honglianglu/ssd/casco/casco_rag_agent

# 检查当前配置
source env.sh 2>/dev/null

echo "当前配置:"
echo "  Model: $CLOUD_MODEL"
echo "  Base URL: $CLOUD_BASE_URL"
echo ""

echo "检测到的问题:"
echo "  ❌ TEXT_AUDIT_QUESTION_NOT_PASS (内容审核)"
echo "  ❌ 轨道交通技术文档被误判"
echo ""

echo "=========================================="
echo "  推荐方案：切换到 DeepSeek"
echo "=========================================="
echo ""
echo "优势："
echo "  ✅ 无内容审核"
echo "  ✅ 价格便宜（¥1/1M tokens）"
echo "  ✅ 完全兼容"
echo "  ✅ 质量好"
echo ""

read -p "是否切换到 DeepSeek？(y/n): " confirm

if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
    echo ""
    echo "已取消。"
    echo ""
    echo "替代方案："
    echo "  1. 联系 coregpu 客服要求关闭审核"
    echo "  2. 修改 rag_qa_agent.py 禁用多模态"
    echo ""
    exit 0
fi

echo ""
echo "=========================================="
echo "  步骤 1: 获取 DeepSeek API Key"
echo "=========================================="
echo ""
echo "请访问: https://platform.deepseek.com"
echo "  1. 注册账号（微信/手机号）"
echo "  2. 点击「API Keys」"
echo "  3. 创建新的 API Key"
echo "  4. 复制 API Key（sk-开头）"
echo ""

read -p "已获取 API Key？按回车继续..." dummy

echo ""
read -p "请输入你的 DeepSeek API Key: " new_api_key

if [ -z "$new_api_key" ]; then
    echo "❌ API Key 不能为空"
    exit 1
fi

echo ""
echo "=========================================="
echo "  步骤 2: 更新配置"
echo "=========================================="
echo ""

# 备份旧配置
cp env.sh env.sh.backup_$(date +%Y%m%d_%H%M%S)
echo "✅ 已备份旧配置"

# 创建新配置
cat > env.sh << EOF
#!/bin/bash
# 环境变量配置 - DeepSeek API
# 使用方法：source env.sh

# ============= LLM 配置 (DeepSeek) =============
export CLOUD_MODEL="deepseek-chat"
export CLOUD_API_KEY="$new_api_key"
export CLOUD_BASE_URL="https://api.deepseek.com/v1"

# ============= Vision Model 配置 =============
# 选项1: 暂时禁用（大部分信息在文本中）
# 在 rag_qa_agent.py 中设置 enable_image=False

# 选项2: 使用 OpenAI（如果你有 OpenAI API Key）
# export VISION_MODEL="gpt-4o-mini"
# export VISION_API_KEY="sk-your-openai-key"
# export VISION_BASE_URL="https://api.openai.com/v1"

# 选项3: 使用原 Qwen API（仅用于 vision）
export VISION_MODEL="Qwen2.5-VL-72B-Instruct"
export VISION_API_KEY="sk-wxZp2QgCmvkdng8o9dHhyvBAU8MJOUjjsSx5fJDO7l31KJhA"
export VISION_BASE_URL="https://ai.api.coregpu.cn/v1"

# ============= Embedding 配置 (保持不变) =============
export OPENAI_API_KEY="sk-aqrqxoeqrbfsfhvjhjpozbivejsqhhsqvagukbdlbzjfaawr"
export OPENAI_BASE_URL="https://api.siliconflow.cn/v1/"
export OPENAI_API_MODEL="BAAI/bge-m3"

# ============= 可选配置 =============
export WORKING_DIR="./rag_storage"
export PARSER="mineru"
export PARSE_METHOD="auto"

echo "✅ 环境变量已加载 (DeepSeek)"
echo "使用的 LLM 模型: \$CLOUD_MODEL"
echo "使用的 Embedding 模型: \$OPENAI_API_MODEL"
EOF

echo "✅ 已更新 env.sh"

echo ""
echo "=========================================="
echo "  步骤 3: 测试 API"
echo "=========================================="
echo ""

source env.sh

echo "测试 DeepSeek API..."
response=$(curl -s -X POST "https://api.deepseek.com/v1/chat/completions" \
  -H "Authorization: Bearer $new_api_key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": "你好"}],
    "max_tokens": 10
  }')

if echo "$response" | grep -q '"id"'; then
    echo "✅ API 测试成功！"
    echo ""
    echo "响应："
    echo "$response" | python -m json.tool 2>/dev/null | head -20
else
    echo "❌ API 测试失败"
    echo "响应: $response"
    echo ""
    echo "请检查："
    echo "  1. API Key 是否正确"
    echo "  2. 网络连接是否正常"
    exit 1
fi

echo ""
echo "=========================================="
echo "  ✅ 切换完成！"
echo "=========================================="
echo ""
echo "现在可以运行:"
echo "  source env.sh"
echo "  python rag_qa_agent.py"
echo ""
echo "备注:"
echo "  - 旧配置已备份"
echo "  - Vision 使用原 Qwen API（图像处理量少，不易触发审核）"
echo "  - 如果仍有问题，可以禁用多模态处理"
echo ""

