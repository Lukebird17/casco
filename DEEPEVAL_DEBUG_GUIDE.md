# 🐛 DeepEval 调试指南

## 问题描述
DeepEval质量评估功能在运行时出现卡死/死循环现象。

## 🔧 已实施的修复

### 1. 添加超时保护
**文件**: `backend/api.py` (第675-720行)

```python
# 使用asyncio.wait_for添加60秒超时
quality_metrics = await asyncio.wait_for(
    quality_evaluator.evaluate(...),
    timeout=60.0  # 60秒超时
)
```

**效果**: 
- ✅ 如果评估超过60秒，自动使用默认值（0.75分）
- ✅ 不会阻塞整个系统

### 2. 添加详细调试日志
**文件**: `quality_evaluator_advanced.py` (第315-405行)

现在每个评估步骤都会打印调试信息：
```
🔍 [DEBUG] 开始DeepEval评估流程...
🔍 [DEBUG] 步骤1: 准备上下文，检索到 X 个文档
🔍 [DEBUG] 步骤2: 创建LLMTestCase...
🔍 [DEBUG] 开始评估指标: faithfulness
...
```

**用途**: 
- ✅ 快速定位卡在哪个步骤
- ✅ 查看每个指标的评估时间

### 3. LLM超时熔断
**文件**: `quality_evaluator_advanced.py` (第92行)

```python
response = self.client.chat.completions.create(
    ...,
    timeout=20  # 20秒超时熔断
)
```

**效果**:
- ✅ 单次LLM调用最多20秒
- ✅ 防止LLM API卡住

## 🧪 调试测试脚本

### 运行独立测试
```bash
cd /home/honglianglu/hdd/rag-agent
python test_deepeval_debug.py
```

**这个脚本会**:
1. ✅ 独立测试DeepEval评估器
2. ✅ 90秒硬超时保护
3. ✅ 打印每个步骤的详细信息
4. ✅ 如果卡住，自动终止并报告

### 预期输出
```
🧪 DeepEval 调试测试
============================================
步骤1: 导入质量评估器...
✅ 导入成功

步骤2: 初始化评估器...
✅ 初始化成功
   - DeepEval模式: True

步骤3: 准备测试数据...
✅ 测试数据准备完成

步骤4: 开始评估（60秒超时保护）...
🔍 [DEBUG] 开始DeepEval评估流程...
🔍 [DEBUG] 步骤1: 准备上下文，检索到 2 个文档
...
✅ 评估完成！
总分: 0.85
```

## 🔍 定位死循环的方法

### 方法1: 查看后端日志
重启后端，提问后观察日志输出，看卡在哪个步骤：

```bash
cd /home/honglianglu/hdd/rag-agent/backend
python api.py
```

查找日志中的`[DEBUG]`标记，最后一个`[DEBUG]`消息就是卡住的位置。

### 方法2: 运行独立测试
```bash
python test_deepeval_debug.py
```

如果测试也卡住，说明问题在DeepEval内部。

### 方法3: 禁用特定指标
如果某个指标卡住，可以在`quality_evaluator_advanced.py`第350-354行注释掉：

```python
futures = [
    executor.submit(run_safe_metric, FaithfulnessMetric, "faithfulness"),
    # executor.submit(run_safe_metric, AnswerRelevancyMetric, "answer_relevancy"),  # 暂时禁用
    executor.submit(run_safe_metric, ContextualRelevancyMetric, "contextual_relevancy")
]
```

## 🚨 可能的原因

### 原因1: LLM API响应慢
**症状**: 日志卡在`开始评估指标: XXX`
**解决**: 
- 检查网络连接
- 检查OPENAI_API_BASE配置
- 降低`max_tokens`（第90行）

### 原因2: DeepEval内部bug
**症状**: 日志卡在`XXX 指标初始化成功，开始measure...`
**解决**: 
- 升级DeepEval: `pip install --upgrade deepeval`
- 或临时禁用DeepEval（见下方）

### 原因3: JSON解析死循环
**症状**: 日志卡在某个metric的measure之后
**解决**: 
- 检查`_normalize_json_structure`方法（第123-247行）
- 已添加超时保护，但如果仍有问题，可以简化JSON修复逻辑

## 🔄 临时禁用DeepEval

如果问题仍无法解决，可以临时禁用：

**方法1**: 在`backend/api.py`第676行添加条件
```python
if quality_evaluator and False:  # 临时禁用
```

**方法2**: 使用简化评估
在`quality_evaluator_advanced.py`第267行修改：
```python
self.deepeval_mode = False  # 强制使用简化评估
```

## 📊 当前配置

- ✅ **整体超时**: 60秒 (`backend/api.py`)
- ✅ **LLM超时**: 20秒 (`quality_evaluator_advanced.py`)
- ✅ **测试超时**: 90秒 (`test_deepeval_debug.py`)
- ✅ **并行评估**: 3个指标同时运行
- ✅ **上下文限制**: 只用前3个文档
- ✅ **内容截断**: 每个文档最多800字符
- ✅ **禁用原因生成**: `include_reason=False`

## 📝 下一步

1. **先运行测试脚本**: `python test_deepeval_debug.py`
2. **查看输出**: 确定卡在哪个步骤
3. **重启后端**: 测试实际系统
4. **监控日志**: 找到`[DEBUG]`最后一条消息
5. **报告结果**: 告诉我卡在哪里，我可以进一步优化

## 🎯 快速启动

```bash
# 1. 测试DeepEval
cd /home/honglianglu/hdd/rag-agent
python test_deepeval_debug.py

# 2. 如果测试通过，重启后端
cd backend
python api.py

# 3. 如果测试失败，查看错误信息
# 然后告诉我具体卡在哪个步骤
```

---

**最后更新**: 2025-12-20
**状态**: 已添加调试功能，等待用户测试反馈

