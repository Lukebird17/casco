# 🐛 DeepEval卡死问题 - 深度调试

## 📊 问题分析

### 现象
```
✨ You're running DeepEval's latest Answer Relevancy Metric!
(using Qwen/Qwen3-VL-32B-Instruct, strict=False…
```
然后系统卡死，无响应。

### 可能原因

#### 1. **异步同步混用问题** ⭐（最可能）
**位置**: `quality_evaluator_advanced.py` 第124-132行

**原问题**:
```python
async def a_generate(self, prompt: str) -> str:
    return self.generate(prompt)  # ❌ 直接调用同步方法
```

DeepEval内部可能在异步上下文中调用`a_generate`，而`generate`是同步的，可能导致事件循环阻塞。

**修复**:
```python
async def a_generate(self, prompt: str) -> str:
    import asyncio
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, self.generate, prompt)
    return result
```

#### 2. **JSON解析循环**
`_normalize_json_structure`有复杂的嵌套逻辑，可能在某些边缘情况下陷入无限循环。

**修复**: 添加了详细的DEBUG日志，可以定位到具体哪一步卡住。

#### 3. **LLM API无响应**
如果API端点有问题，可能无限等待。

**修复**: 已有20秒超时 + 15秒指标级超时 + 60秒总体超时。

## 🔧 已实施的修复

### 1. 真正的异步支持
**文件**: `quality_evaluator_advanced.py` 第124-132行

```python
async def a_generate(self, prompt: str) -> str:
    print(f"🔍 [LLM] a_generate 被调用（异步）")
    import asyncio
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, self.generate, prompt)
    print(f"🔍 [LLM] a_generate 完成")
    return result
```

### 2. 详细的调试日志

#### LLM调用日志
```
🔍 [LLM] generate 被调用，prompt长度: XXX
🔍 [LLM] 准备调用LLM API...
🔍 [LLM] 开始请求 Qwen/XXX...
🔍 [LLM] API响应成功
🔍 [LLM] 响应内容长度: XXX
🔍 [LLM] 开始JSON结构规范化...
```

#### JSON解析日志
```
🔍 [JSON] 开始规范化，输入长度: XXX
🔍 [JSON] A. 基础清洗...
🔍 [JSON] B. 替换换行符...
🔍 [JSON] C. 尝试JSON解析...
🔍 [JSON] JSON解析成功，类型: dict
🔍 [JSON] D. 键名规范化...
🔍 [JSON] E. 构建super_json...
🔍 [JSON] 数据合并，keys: [...]
🔍 [JSON] F. 字段互通...
🔍 [JSON] G. Verdicts清洗...
🔍 [JSON] ✅ JSON规范化完成，返回结果
```

#### 评估指标日志
```
🔍 [DEBUG] 开始评估指标: faithfulness
🔍 [DEBUG] faithfulness 指标初始化成功，开始measure...
🔍 [DEBUG] faithfulness 评估完成，得分: 0.85
```

### 3. 多层超时保护

| 层级 | 超时时间 | 位置 |
|------|---------|------|
| LLM API调用 | 20秒 | `CustomSiliconFlowLLM.generate()` |
| 单个指标评估 | 15秒 | `run_safe_metric()` 使用signal.alarm |
| 整体评估 | 60秒 | `backend/api.py` 使用asyncio.wait_for |

### 4. UI布局修复
**文件**: `frontend/src/components/ChatInterface.jsx`

**修改**: RetrievalResults现在显示在最后一条助手消息**之前**，而不是之后。

```jsx
{isLastMessage && isAssistantMessage && showRetrievalResults && (
  <RetrievalResults ... />
)}
<MessageBubble ... />
```

## 🧪 如何测试

### 步骤1: 查看详细日志
重启后端并提问，观察终端输出：

```bash
cd /home/honglianglu/hdd/rag-agent/backend
python api.py
```

### 步骤2: 定位卡住位置
查找最后一条`🔍`日志，例如：

**卡在LLM调用**:
```
🔍 [LLM] 开始请求 Qwen/XXX...
（卡住，没有后续）
```
→ 说明LLM API有问题

**卡在JSON解析**:
```
🔍 [JSON] C. 尝试JSON解析...
（卡住，没有后续）
```
→ 说明JSON解析有问题

**卡在指标measure**:
```
🔍 [DEBUG] faithfulness 指标初始化成功，开始measure...
（卡住，没有后续）
```
→ 说明DeepEval内部有问题

### 步骤3: 根据位置调试

#### 情况A: 卡在LLM API
**可能原因**: 
- 网络问题
- API端点错误
- 模型名称错误

**检查**:
```bash
# 查看配置
grep -E "OPENAI_API_BASE|MODEL_NAME" /home/honglianglu/hdd/rag-agent/config.py

# 测试API连接
curl -X POST YOUR_API_BASE/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{"model": "YOUR_MODEL", "messages": [{"role": "user", "content": "test"}]}'
```

#### 情况B: 卡在JSON解析
**解决**: 检查LLM返回的JSON格式，可能需要调整`_normalize_json_structure`。

#### 情况C: 卡在DeepEval measure
**解决**: 这是DeepEval内部问题，15秒后会自动超时并使用默认值0.5。

## 📋 预期行为

### 正常流程
```
📊 开始质量评估...
🔍 [DEBUG] 开始DeepEval评估流程...
🔍 [DEBUG] 步骤1: 准备上下文，检索到 3 个文档
🔍 [DEBUG] 步骤2: 创建LLMTestCase...
🔍 [DEBUG] LLMTestCase创建成功
🔍 [DEBUG] 步骤4: 开始并行执行3个指标评估...
🔍 [DEBUG] 提交3个评估任务到线程池...
🔍 [DEBUG] 等待评估任务完成...

🔍 [DEBUG] 开始评估指标: faithfulness
🔍 [LLM] generate 被调用，prompt长度: 1234
🔍 [LLM] 准备调用LLM API...
🔍 [LLM] 开始请求 Qwen/XXX...
🔍 [LLM] API响应成功
🔍 [JSON] 开始规范化...
🔍 [JSON] ✅ JSON规范化完成
🔍 [DEBUG] faithfulness 评估完成，得分: 0.85

🔍 [DEBUG] 任务 1/3 完成
... (重复2次)
🔍 [DEBUG] 任务 3/3 完成
🔍 [DEBUG] 步骤5: 组装最终评估结果...
🔍 [DEBUG] ✅ 评估流程完成，返回结果
✅ 质量评估完成: 总分 0.85
```

### 超时情况
```
🔍 [DEBUG] faithfulness 指标初始化成功，开始measure...
（15秒后）
⚠️  faithfulness 评估超时（15秒），已自动置为 0.5
🔍 [DEBUG] 任务 1/3 完成
```

## 🎯 下一步

1. **重启后端**: `cd backend && python api.py`
2. **提问测试**: 在前端提一个问题
3. **查看日志**: 观察终端中的`🔍`日志
4. **报告结果**: 告诉我最后一条`🔍`日志是什么

如果仍然卡住，日志会准确告诉我们卡在哪里，然后我可以针对性地修复。

---

**修复时间**: 2025-12-20  
**状态**: ✅ 已添加详细调试日志 + 真正的异步支持 + UI布局修复

