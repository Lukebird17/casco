# RAGAgent 参数说明

## 📋 初始化参数

### 正确用法

```python
from rag_agent import RAGAgent
from config import MODEL_NAME

agent = RAGAgent(
    model=MODEL_NAME,                # 模型名称
    enable_tracking=True,            # 启用追踪
    enable_cot=True,                 # 启用Chain-of-Thought
    use_multimodal=True              # ⭐ 启用多模态（正确参数名）
)
```

---

## ⚠️ 常见错误

### ❌ 错误用法

```python
agent = RAGAgent(
    enable_multimodal=True  # ❌ 错误：参数名不存在
)
```

**错误信息**：
```
TypeError: RAGAgent.__init__() got an unexpected keyword argument 'enable_multimodal'
```

### ✅ 正确用法

```python
agent = RAGAgent(
    use_multimodal=True  # ✅ 正确：应该是 use_multimodal
)
```

---

## 📖 参数详解

### 1. `model` (str)
- **默认值**: `MODEL_NAME` (来自config.py)
- **说明**: 使用的AI模型名称
- **示例**: `"Qwen/Qwen3-VL-32B-Instruct"`

### 2. `enable_tracking` (bool)
- **默认值**: `True`
- **说明**: 是否启用性能追踪和统计
- **功能**:
  - 记录API调用次数
  - 统计Token消耗
  - 监控响应时间

### 3. `enable_cot` (bool)
- **默认值**: `True`
- **说明**: 是否启用Chain-of-Thought推理
- **功能**:
  - 显示推理步骤
  - 提高回答质量
  - 增强可解释性

### 4. `use_multimodal` (bool) ⭐
- **默认值**: `True`
- **说明**: 是否启用多模态检索
- **功能**:
  - 同时检索文本和图片
  - 使用HybridRetriever混合检索器
  - 支持图片问答
- **注意**: 
  - ⚠️ 参数名是 `use_multimodal` 不是 `enable_multimodal`
  - 需要先运行 `process_data.py` 构建图片向量库

---

## 🔧 完整示例

### 基础用法（不使用多模态）

```python
from rag_agent import RAGAgent

# 最小化配置
agent = RAGAgent(
    use_multimodal=False  # 仅使用文本检索
)

# 提问
answer = agent.answer_question("什么是slab分配器？")
print(answer)
```

### 高级用法（启用所有功能）

```python
from rag_agent import RAGAgent
from config import MODEL_NAME

# 完整配置
agent = RAGAgent(
    model=MODEL_NAME,         # 使用指定模型
    enable_tracking=True,     # 追踪性能
    enable_cot=True,          # 启用CoT推理
    use_multimodal=True       # 启用多模态
)

# 提问
answer = agent.answer_question(
    "第28页的slab示意图中的Next_free是什么？",
    chat_history=[]
)

# 查看推理链
if agent.get_reasoning_chain():
    print(agent.get_reasoning_chain().format_chain())

# 查看Token统计
print(agent.get_token_report())
```

---

## 🎯 不同场景的推荐配置

### 场景1：快速问答（追求速度）

```python
agent = RAGAgent(
    enable_tracking=False,   # 关闭追踪减少开销
    enable_cot=False,        # 关闭CoT加快速度
    use_multimodal=False     # 仅文本检索
)
```

### 场景2：深度分析（追求质量）

```python
agent = RAGAgent(
    enable_tracking=True,    # 监控性能
    enable_cot=True,         # 详细推理
    use_multimodal=True      # 全面检索
)
```

### 场景3：调试模式

```python
agent = RAGAgent(
    enable_tracking=True,    # 追踪所有操作
    enable_cot=True,         # 显示推理过程
    use_multimodal=True      # 启用多模态
)

# 设置详细日志
import logging
logging.basicConfig(level=logging.DEBUG)
```

---

## 🐛 故障排除

### 问题1：`unexpected keyword argument 'enable_multimodal'`

**原因**：参数名错误

**解决**：
```python
# ❌ 错误
agent = RAGAgent(enable_multimodal=True)

# ✅ 正确
agent = RAGAgent(use_multimodal=True)
```

---

### 问题2：多模态初始化失败

**错误信息**：
```
⚠️ 多模态检索初始化失败: ...
```

**原因**：
1. 图片向量库未创建
2. CLIP模型未加载
3. 依赖包未安装

**解决**：
```bash
# 1. 安装依赖
pip install transformers torch pillow

# 2. 构建图片向量库
python process_data.py

# 3. 重新初始化
python app_modern.py
```

---

### 问题3：模型找不到

**错误信息**：
```
Model not found: ...
```

**解决**：
```python
# 检查 config.py 中的模型配置
from config import MODEL_NAME
print(f"当前模型: {MODEL_NAME}")

# 或手动指定模型
agent = RAGAgent(model="qwen-vl-max")
```

---

## 📚 相关文档

- [现代化UI使用指南](现代化UI使用指南.md)
- [多模态RAG说明](MULTIMODAL_README.md)
- [完整README](README_现代化UI.md)

---

## ✅ 总结

**核心要点**：
1. ⭐ 参数名是 **`use_multimodal`** 不是 `enable_multimodal`
2. 默认所有功能都启用（推荐配置）
3. 多模态需要先构建图片向量库
4. 根据场景选择合适的配置

**记住这个！**
```python
agent = RAGAgent(use_multimodal=True)  # ✅ 正确！
```

---

*最后更新: 2025-12-17*

