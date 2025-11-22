#!/bin/bash
# 切换到 DeepSeek API（无内容审核，完全兼容）

echo "=========================================="
echo "切换到 DeepSeek API"
echo "=========================================="
echo ""

cd /home/honglianglu/ssd/casco/casco_rag_agent

echo "当前问题："
echo "  ❌ Qwen API 内容审核过严格"
echo "  ❌ TEXT_AUDIT_QUESTION_NOT_PASS"
echo ""
echo "解决方案："
echo "  ✅ 使用 DeepSeek（无审核，便宜，快速）"
echo ""

cat > env.sh << 'EOF'
#!/bin/bash
# 环境变量配置 - DeepSeek 版本
# 使用方法：source env.sh

# ============= LLM 配置 (DeepSeek) =============
export CLOUD_MODEL="deepseek-chat"
export CLOUD_API_KEY="sk-your-deepseek-api-key-here"  # 👈 在 https://platform.deepseek.com 获取
export CLOUD_BASE_URL="https://api.deepseek.com/v1"

# ============= Vision Model 配置 =============
# DeepSeek 暂不支持 vision，使用 OpenAI 或其他
export VISION_MODEL="gpt-4o-mini"  # 或其他支持vision的模型
export VISION_API_KEY="sk-your-openai-api-key"  # OpenAI API Key
export VISION_BASE_URL="https://api.openai.com/v1"

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
EOF

echo "✅ 已创建新的 env.sh（DeepSeek 配置）"
echo ""
echo "=========================================="
echo "下一步操作："
echo "=========================================="
echo ""
echo "1. 获取 DeepSeek API Key:"
echo "   访问 https://platform.deepseek.com"
echo "   注册并创建 API Key"
echo ""
echo "2. 编辑 env.sh，填入你的 API Key:"
echo "   nano env.sh"
echo "   找到这一行："
echo "     export CLOUD_API_KEY=\"sk-your-deepseek-api-key-here\""
echo "   替换为你的实际 API Key"
echo ""
echo "3. 可选：配置 Vision Model"
echo "   如果需要处理图像/表格，需要配置 VISION_MODEL"
echo "   可以用 OpenAI gpt-4o-mini 或其他支持 vision 的模型"
echo ""
echo "4. 运行测试:"
echo "   source env.sh"
echo "   python rag_qa_agent.py"
echo ""
echo "=========================================="
echo "DeepSeek 优势："
echo "=========================================="
echo "  ✅ 无内容审核"
echo "  ✅ 价格便宜（1M tokens = ¥1）"
echo "  ✅ 速度快"
echo "  ✅ 完全兼容 OpenAI 格式"
echo "  ✅ 质量好"
echo ""

