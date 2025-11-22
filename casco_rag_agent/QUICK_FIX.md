# 快速修复：404 Embedding 错误

## 问题

```
ERROR: <html><head><title>404 Not Found</title></head>...
openai.NotFoundError
```

这说明 **Embedding API 配置错误**。

## 快速测试

```bash
conda activate casco_rag
source env.sh
python test_api.py
```

这个脚本会自动测试你的 API 配置。

## 常见原因

### 原因 1: DeepSeek 不支持 Embedding

**问题**: DeepSeek API 只提供 LLM，不提供 Embedding 服务

**解决**: Embedding 必须使用 OpenAI API

```bash
# 编辑 env.sh
nano env.sh

# 修改为：
# LLM 用 DeepSeek
export CLOUD_MODEL="deepseek-chat"
export CLOUD_API_KEY="sk-your-deepseek-key"
export CLOUD_BASE_URL="https://api.deepseek.com/v1"

# Embedding 用 OpenAI
export OPENAI_API_KEY="sk-your-openai-key"
export OPENAI_BASE_URL="https://api.openai.com/v1"
export OPENAI_API_MODEL="text-embedding-3-large"

# 重新加载
source env.sh

# 测试
python test_api.py
```

### 原因 2: URL 末尾多了斜杠

**问题**: `https://api.openai.com/v1/` (多了 `/`)

**解决**: 应该是 `https://api.openai.com/v1` (没有最后的 `/`)

```bash
# 正确
export OPENAI_BASE_URL="https://api.openai.com/v1"

# 错误
export OPENAI_BASE_URL="https://api.openai.com/v1/"
```

### 原因 3: 模型名称错误

**问题**: 模型名称在你的 API 端点不存在

**解决**: 使用正确的模型名称

```bash
# OpenAI 官方
export OPENAI_API_MODEL="text-embedding-3-large"

# 或者
export OPENAI_API_MODEL="text-embedding-3-small"
export OPENAI_API_MODEL="text-embedding-ada-002"
```

### 原因 4: API Key 错误

**问题**: API Key 无效或过期

**解决**: 检查 API Key 是否正确

```bash
# 测试 API Key
curl -H "Authorization: Bearer $OPENAI_API_KEY" \
  https://api.openai.com/v1/models

# 应该返回模型列表，而不是 404
```

## 推荐配置

### 配置 1: DeepSeek + OpenAI（推荐）

```bash
# env.sh
# LLM 用 DeepSeek（便宜）
export CLOUD_MODEL="deepseek-chat"
export CLOUD_API_KEY="sk-xxxxxxxxxxxxx"  # 你的 DeepSeek Key
export CLOUD_BASE_URL="https://api.deepseek.com/v1"

# Embedding 用 OpenAI（必需）
export OPENAI_API_KEY="sk-xxxxxxxxxxxxx"  # 你的 OpenAI Key
export OPENAI_BASE_URL="https://api.openai.com/v1"
export OPENAI_API_MODEL="text-embedding-3-large"
```

### 配置 2: 全部使用 OpenAI

```bash
# env.sh
# LLM 用 OpenAI
export CLOUD_MODEL="gpt-4o-mini"
export CLOUD_API_KEY="sk-xxxxxxxxxxxxx"
export CLOUD_BASE_URL="https://api.openai.com/v1"

# Embedding 用 OpenAI
export OPENAI_API_KEY="sk-xxxxxxxxxxxxx"  # 可以是同一个 Key
export OPENAI_BASE_URL="https://api.openai.com/v1"
export OPENAI_API_MODEL="text-embedding-3-large"
```

## 修复步骤

```bash
# 1. 编辑配置
cd /home/honglianglu/ssd/casco/casco_rag_agent
nano env.sh

# 2. 根据上面的推荐配置修改

# 3. 重新加载
source env.sh

# 4. 测试 API
python test_api.py

# 5. 如果测试通过，重新运行
python rag_qa_agent.py
```

## 验证配置

```bash
# 检查环境变量是否设置
echo "CLOUD_BASE_URL: $CLOUD_BASE_URL"
echo "OPENAI_BASE_URL: $OPENAI_BASE_URL"
echo "OPENAI_API_MODEL: $OPENAI_API_MODEL"

# API Key 前10个字符（确认不是空的）
echo "CLOUD_API_KEY: ${CLOUD_API_KEY:0:10}..."
echo "OPENAI_API_KEY: ${OPENAI_API_KEY:0:10}..."
```

## 如果还是不行

### 方案 A: 使用国内兼容 API

如果有国内的 OpenAI 兼容 API：

```bash
export OPENAI_BASE_URL="https://your-api-proxy.com/v1"
export OPENAI_API_KEY="your-key"
export OPENAI_API_MODEL="text-embedding-3-large"
```

### 方案 B: 检查网络

```bash
# 测试能否访问 OpenAI
curl -I https://api.openai.com

# 如果不行，可能需要代理
export HTTP_PROXY=http://your-proxy:port
export HTTPS_PROXY=http://your-proxy:port
```

### 方案 C: 临时跳过（仅测试）

如果实在解决不了，可以临时修改代码使用本地 embedding（不推荐生产使用）：

```python
# 这只是为了测试，效果会很差
# 不要用于实际项目
```

## 获取 API Key

### OpenAI API Key

1. 访问: https://platform.openai.com/api-keys
2. 登录/注册
3. 创建新的 API Key
4. 复制并保存（只显示一次）

### DeepSeek API Key

1. 访问: https://platform.deepseek.com/
2. 登录/注册
3. 获取 API Key

## 成功标志

当你看到：

```
✅ 所有 API 测试通过！
   你可以运行: python rag_qa_agent.py
```

就可以正常使用了！

