# 🎯 最终解决方案

## 问题根源

你的 `https://ai.api.coregpu.cn` API 有以下问题：

1. **内容审核过严** - LightRAG 的提示词被拦截
   ```
   TEXT_AUDIT_QUESTION_NOT_PASS (code: 600003)
   "很抱歉，关于这个问题我无法提供相应的信息"
   ```

2. **返回格式非标准** - 多了 `code` 字段
   ```json
   {"code": 0, "id": "...", ...}  // 标准是没有 code 的
   ```

3. **openai 库不兼容** - 版本问题

## ✅ 解决方案（3选1）

### 方案 1: 换 API（最推荐）⭐⭐⭐⭐⭐

**使用 DeepSeek（无审核、便宜、稳定）**

```bash
# 1. 获取 API Key
# 访问: https://platform.deepseek.com
# 注册并创建 API Key（有免费额度）

# 2. 编辑配置
cd /home/honglianglu/ssd/casco/casco_rag_agent
nano env.sh

# 修改为：
export CLOUD_MODEL="deepseek-chat"
export CLOUD_API_KEY="sk-your-deepseek-api-key"
export CLOUD_BASE_URL="https://api.deepseek.com/v1"

# 3. 运行
source env.sh
python rag_qa_agent.py
```

**优势**：
- ✅ 无内容审核
- ✅ 完全兼容 OpenAI 格式
- ✅ 价格：¥1/1M tokens
- ✅ 速度快
- ✅ 质量好

---

### 方案 2: 联系 API 提供商 ⭐⭐⭐

联系 `coregpu.cn` 的客服：

1. **询问是否有无审核的 API 端点**
2. **询问是否有专门的技术类 API**（轨道交通是技术文档，不应该被审核）
3. **要求白名单** - 让他们把 LightRAG 的提示词加入白名单

---

### 方案 3: 降级到纯文本模式（临时方案）⭐⭐

禁用多模态处理，只处理文本：

```bash
cd /home/honglianglu/ssd/casco/casco_rag_agent
```

修改 `rag_qa_agent.py`，在 `config` 中设置：
```python
self.config = RAGAnythingConfig(
    working_dir=working_dir,
    parser=parser,
    parse_method=parse_method,
    enable_image=False,      # 禁用图像
    enable_table=False,      # 禁用表格
    enable_equation=False,   # 禁用公式
)
```

这样可以减少被审核的提示词数量，但会损失多模态内容。

---

## 🚀 快速对比

| 方案 | 难度 | 时间 | 效果 | 推荐度 |
|------|------|------|------|--------|
| 换 DeepSeek | 简单 | 5分钟 | 完美 | ⭐⭐⭐⭐⭐ |
| 联系客服 | 中等 | 1-3天 | 可能 | ⭐⭐⭐ |
| 纯文本模式 | 简单 | 2分钟 | 妥协 | ⭐⭐ |

---

## 📝 DeepSeek 快速上手

### 1. 注册（2分钟）
```
1. 访问: https://platform.deepseek.com
2. 点击"开始使用"
3. 微信/手机号注册
4. 创建 API Key
```

### 2. 配置（1分钟）
```bash
cd /home/honglianglu/ssd/casco/casco_rag_agent
nano env.sh
```

找到：
```bash
export CLOUD_MODEL="Qwen2.5-VL-72B-Instruct"
export CLOUD_API_KEY="sk-wxZp..."
export CLOUD_BASE_URL="https://ai.api.coregpu.cn/v1"
```

改为：
```bash
export CLOUD_MODEL="deepseek-chat"
export CLOUD_API_KEY="sk-your-new-deepseek-key"
export CLOUD_BASE_URL="https://api.deepseek.com/v1"
```

### 3. 运行（1分钟）
```bash
source env.sh
python rag_qa_agent.py
```

---

## ❓ 常见问题

### Q: DeepSeek 支持图像/表格吗？
A: DeepSeek 本身不支持 vision，但你可以：
- 用 OpenAI gpt-4o-mini 做 Vision Model
- 或者暂时禁用多模态（大部分信息在文本中）

配置示例：
```bash
# LLM 用 DeepSeek
export CLOUD_MODEL="deepseek-chat"
export CLOUD_BASE_URL="https://api.deepseek.com/v1"
export CLOUD_API_KEY="sk-deepseek-key"

# Vision 用 OpenAI
export VISION_MODEL="gpt-4o-mini"
export VISION_BASE_URL="https://api.openai.com/v1"
export VISION_API_KEY="sk-openai-key"

# Embedding 保持不变
export OPENAI_API_MODEL="BAAI/bge-m3"
export OPENAI_BASE_URL="https://api.siliconflow.cn/v1/"
export OPENAI_API_KEY="sk-aqrq..."
```

### Q: DeepSeek 贵吗？
A: 非常便宜！
- **deepseek-chat**: ¥1 / 1M tokens
- 你的 107 个文档，预计 ¥5-10 即可完成

### Q: 数据安全吗？
A: 
- DeepSeek 是国内大厂（深度求索）
- 有企业级数据保护
- 不训练用户数据

---

## 💡 我的建议

**立即切换到 DeepSeek**，理由：
1. ✅ 5分钟搞定，不用等客服回复
2. ✅ 无内容审核，技术文档完全没问题
3. ✅ 价格便宜，几块钱就能跑完
4. ✅ 质量好，专门为中文优化

---

## 🔗 相关链接

- DeepSeek 官网: https://platform.deepseek.com
- DeepSeek 文档: https://platform.deepseek.com/docs
- DeepSeek 定价: https://platform.deepseek.com/pricing

