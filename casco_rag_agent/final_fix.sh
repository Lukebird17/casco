#!/bin/bash
# 最终完整修复方案

set -e

echo "=========================================="
echo "  完整诊断和修复"
echo "=========================================="
echo ""

# 激活环境
export PATH="/data/4tssd/anaconda3/bin:$PATH"
eval "$(conda shell.bash hook)" 2>/dev/null || true
conda activate casco 2>/dev/null || true

cd /home/honglianglu/ssd/casco/casco_rag_agent

echo "1. 当前版本检查"
echo "----------------------------------------"
python << 'PYEOF'
import openai
import httpx
print(f"openai: {openai.__version__}")
print(f"httpx: {httpx.__version__}")

# 检查版本兼容性
openai_ver = tuple(map(int, openai.__version__.split('.')[:2]))
httpx_ver = tuple(map(int, httpx.__version__.split('.')[:2]))

print(f"\n兼容性检查:")
if openai_ver[0] == 1 and 30 <= openai_ver[1] <= 60 and httpx_ver == (0, 27):
    print("✅ 版本组合兼容")
elif openai_ver[0] == 1 and openai_ver[1] >= 70 and httpx_ver == (0, 28):
    print("✅ 版本组合兼容")
else:
    print("⚠️  版本组合可能不兼容")
    print(f"   建议: openai 1.40.x + httpx 0.27.x")
PYEOF

echo ""
echo "2. 问题诊断"
echo "----------------------------------------"

# 测试 API
echo "测试 Qwen API..."
source env.sh

response=$(curl -s -X POST "${CLOUD_BASE_URL%/}/chat/completions" \
  -H "Authorization: Bearer $CLOUD_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "'"$CLOUD_MODEL"'",
    "messages": [
      {"role": "system", "content": "你是一个专业的技术文档分析助手。"},
      {"role": "user", "content": "请从以下文本中提取实体和关系：轨道交通系统包括信号系统、车辆系统和通信系统。"}
    ],
    "max_tokens": 100
  }')

if echo "$response" | grep -q "TEXT_AUDIT_QUESTION_NOT_PASS"; then
    echo "❌ API 有内容审核"
    echo "   检测到: TEXT_AUDIT_QUESTION_NOT_PASS"
    echo "   LightRAG 的提示词被拦截"
    echo ""
    echo "解决方案:"
    echo "  1. 换 API (推荐): 使用 DeepSeek"
    echo "  2. 联系 API 提供商关闭审核"
    echo "  3. 禁用多模态处理"
    HAS_AUDIT=true
elif echo "$response" | grep -q '"id"'; then
    echo "✅ API 可用"
    echo "   响应: $(echo $response | python -m json.tool 2>/dev/null | head -10)"
    HAS_AUDIT=false
else
    echo "⚠️  API 返回异常"
    echo "   响应: $response"
    HAS_AUDIT=unknown
fi

echo ""
echo "3. 解决方案"
echo "----------------------------------------"

if [ "$HAS_AUDIT" = "true" ]; then
    echo ""
    echo "检测到内容审核问题！"
    echo ""
    echo "方案 A: 切换到 DeepSeek API (强烈推荐)"
    echo "  - 无内容审核"
    echo "  - 完全兼容"
    echo "  - 价格便宜"
    echo ""
    read -p "是否切换到 DeepSeek? (y/n): " switch_api
    
    if [ "$switch_api" = "y" ] || [ "$switch_api" = "Y" ]; then
        echo ""
        echo "运行切换脚本..."
        ./switch_api.sh
        exit 0
    fi
    
    echo ""
    echo "方案 B: 禁用多模态处理"
    echo "  - 只处理文本"
    echo "  - 减少审核触发"
    echo ""
    read -p "是否禁用多模态? (y/n): " disable_vlm
    
    if [ "$disable_vlm" = "y" ] || [ "$disable_vlm" = "Y" ]; then
        echo "已经在代码中配置，重新运行即可"
        echo ""
        echo "如果仍有问题，说明文本提示词也被审核，必须换 API"
    fi
else
    echo "✅ API 正常，修复 openai 库版本"
    echo ""
    echo "安装兼容版本..."
    pip install "openai==1.40.0" "httpx==0.27.2" -q --force-reinstall
    
    echo ""
    echo "验证..."
    python -c "import openai; print(f'✅ openai {openai.__version__} 安装完成')"
fi

echo ""
echo "=========================================="
echo "  修复完成"
echo "=========================================="
echo ""
echo "运行:"
echo "  source env.sh"
echo "  python rag_qa_agent.py"
echo ""

