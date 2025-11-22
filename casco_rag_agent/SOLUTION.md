# 🔧 依赖问题最终解决方案

## 问题诊断

你遇到了两个主要错误：

### 错误 1: API 400 错误
```
ERROR: OpenAI API Call Failed, Model: Qwen2.5-VL-72B-Instruct, Got: Error code: 400
APIStatusError.__init__() missing 2 required keyword-only arguments: 'response' and 'body'
```

**原因**: openai 库版本与 lightrag 不兼容

### 错误 2: httpx proxies 参数错误
```
ERROR: AsyncClient.__init__() got an unexpected keyword argument 'proxies'
```

**原因**: httpx 版本太新（0.28.x），与 openai/lightrag 不兼容

## 🎯 解决方案

### 方案 A: 完全重装（推荐）

```bash
# 1. 激活环境
conda activate casco

# 2. 卸载旧版本
pip uninstall -y raganything openai httpx

# 3. 安装兼容版本组合
pip install "openai==1.50.2" "httpx==0.27.2"

# 4. 从源码重装 RAG-Anything
cd /home/honglianglu/ssd/casco/RAG-Anything
pip install -e . --no-deps

# 5. 验证
python -c "import openai, httpx; print(f'openai: {openai.__version__}, httpx: {httpx.__version__}')"

# 6. 运行
cd /home/honglianglu/ssd/casco/casco_rag_agent
source env.sh
python rag_qa_agent.py
```

### 方案 B: 使用 uv（更快）

```bash
conda activate casco
cd /home/honglianglu/ssd/casco/RAG-Anything

# 使用 uv 重装（会自动处理依赖）
uv pip install -e . --force-reinstall

cd /home/honglianglu/ssd/casco/casco_rag_agent
source env.sh
python rag_qa_agent.py
```

### 方案 C: 修改 API 配置（如果 400 错误持续）

编辑 `env.sh`，测试其他模型：

```bash
# 选项1: 使用 DeepSeek（推荐，稳定且便宜）
export CLOUD_MODEL="deepseek-chat"
export CLOUD_API_KEY="sk-your-deepseek-key"
export CLOUD_BASE_URL="https://api.deepseek.com/v1"

# 选项2: 使用 OpenAI
export CLOUD_MODEL="gpt-4o-mini"
export CLOUD_API_KEY="sk-your-openai-key"
export CLOUD_BASE_URL="https://api.openai.com/v1"

# 选项3: 修改 Qwen URL（去掉末尾斜杠）
export CLOUD_BASE_URL="https://ai.api.coregpu.cn/v1"  # 无斜杠
```

## 🔍 验证步骤

### 1. 检查版本
```bash
conda activate casco
python -c "
import openai
import httpx
print(f'openai: {openai.__version__}')
print(f'httpx: {httpx.__version__}')
print('Expected: openai 1.50.2, httpx 0.27.2')
"
```

### 2. 测试 API
```bash
python test_api.py
```

### 3. 诊断配置
```bash
python diagnose.py
```

## 🎁 兼容版本组合

| openai | httpx | 状态 |
|--------|-------|------|
| 1.50.2 | 0.27.2 | ✅ 推荐 |
| 1.40.x | 0.27.x | ✅ 可用 |
| 1.109.x | 0.28.x | ❌ 不兼容 |
| 1.1.0 | 0.27.x | ❌ 太旧 |

## 📞 如果还有问题

### 清空并重新开始
```bash
cd /home/honglianglu/ssd/casco/casco_rag_agent

# 备份并清空存储
mv rag_storage rag_storage_backup_$(date +%Y%m%d_%H%M%S)
mkdir -p rag_storage

# 重新运行
source env.sh
python rag_qa_agent.py
```

### 检查 API 是否可用
```bash
# 测试 Qwen API
curl -X POST https://ai.api.coregpu.cn/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "Qwen2.5-VL-72B-Instruct",
    "messages": [{"role": "user", "content": "测试"}],
    "max_tokens": 100
  }'
```

如果返回 400，说明 API 端点不支持该模型，需要更换模型或 API。

