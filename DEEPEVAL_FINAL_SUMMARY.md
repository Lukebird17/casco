# 🎯 DeepEval完整实现总结

## 📊 指标配置

### YZY版本（参考标准）
**使用3个指标**:
1. **FaithfulnessMetric** (忠实度) - 答案是否基于检索到的上下文
2. **AnswerRelevancyMetric** (切题度) - 答案是否回答了用户问题
3. **ContextualRelevancyMetric** (检索质量) - 检索到的上下文是否与问题相关

### 我们的版本
**✅ 与YZY一致，使用3个指标**

## 🔧 关键实现细节

### 1. 线程池并行执行（YZY版本）
```python
def run_safe_metric(metric_cls, name):
    try:
        # 强制 include_reason=False 提速
        metric = metric_cls(threshold=0.5, model=judge_model, include_reason=False)
        metric.measure(test_case)
        return name, metric.score, ""
    except Exception as e:
        print(f"  ⚠️ {name} 评估出错，已自动置为 0.5: {e}")
        return name, 0.5, "评估异常，默认中立"

results = {}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    futures = [
        executor.submit(run_safe_metric, FaithfulnessMetric, "faithfulness"),
        executor.submit(run_safe_metric, AnswerRelevancyMetric, "answer_relevancy"),
        executor.submit(run_safe_metric, ContextualRelevancyMetric, "context_relevancy")
    ]
    
    for future in concurrent.futures.as_completed(futures):
        name, score, reason = future.result()
        results[name] = {"score": score, "reason": reason}
```

**关键点**:
- ✅ **不使用signal** - 在子线程中signal不可用
- ✅ **简单的try-except** - 捕获所有异常，返回默认值0.5
- ✅ **include_reason=False** - 大幅提速，避免LLM生成冗长的解释
- ✅ **ThreadPoolExecutor** - 3个指标并行执行

### 2. 雷达图数据结构
```python
radar_data = [
    {"subject": "忠实度", "A": round(f_score * 100, 0), "fullMark": 100},
    {"subject": "切题度", "A": round(a_score * 100, 0), "fullMark": 100},
    {"subject": "检索质量", "A": round(c_score * 100, 0), "fullMark": 100},
]
```

### 3. 返回数据结构
```python
{
    "passed": is_passed,     # 是否通过阈值
    "score": avg_score,      # 平均分
    "scores": {
        "faithfulness": f_score,
        "answer_relevancy": a_score,
        "context_relevancy": c_score
    },
    "reasons": {
        "faithfulness": "",
        "answer_relevancy": "",
        "context_relevancy": ""
    },
    "radar_data": radar_data
}
```

## ⚠️ 常见问题

### Q1: 为什么不用5个指标？
**A**: DeepEval确实提供更多指标，但：
- 3个核心指标已足够评估RAG质量
- 更多指标 = 更多LLM调用 = 更慢、更贵
- YZY经过实践验证，3个指标效果良好

### Q2: 为什么会有signal错误？
**A**: 如果在`ThreadPoolExecutor`的子线程中使用`signal.alarm()`，会报错：
```
ValueError: signal only works in main thread of the main interpreter
```

**解决**: 不要在子线程中使用signal，用简单的try-except即可。

### Q3: 为什么评估会卡死？
**可能原因**:
1. **LLM API无响应** - 在LLM调用时添加timeout参数
2. **DeepEval内部bug** - 使用最新版本，或添加整体超时
3. **JSON解析死循环** - 简化JSON修复逻辑

**YZY的解决方案**: 简单粗暴，任何错误都返回0.5，不阻塞流程。

## ✅ 我们的最终实现

### 文件: `quality_evaluator_advanced.py`

**关键修复**:
1. ✅ **移除signal** - 不在子线程使用signal
2. ✅ **真正的异步** - `a_generate`使用`loop.run_in_executor`
3. ✅ **详细日志** - 每个步骤都有DEBUG输出
4. ✅ **多层超时**:
   - LLM API: 20秒
   - 整体评估: 60秒（asyncio.wait_for）
5. ✅ **与YZY一致** - 3个指标，相同的数据结构

### 超时保护层级

| 层级 | 超时时间 | 位置 | 说明 |
|------|---------|------|------|
| LLM API | 20秒 | `CustomSiliconFlowLLM.generate()` | 单次LLM调用 |
| 整体评估 | 60秒 | `backend/api.py` | asyncio.wait_for |
| 异常捕获 | - | `run_safe_metric()` | 任何错误返回0.5 |

### 当前状态检查

运行这个命令检查是否还有signal调用：
```bash
grep -r "import signal\|signal\." /home/honglianglu/hdd/rag-agent/quality_evaluator_advanced.py
```

**预期输出**: 应该是空的（没有signal调用）

## 🚀 下一步

1. **确认重启后端** - 确保使用的是新代码
2. **测试评估** - 提问并观察DEBUG日志
3. **检查结果** - 应该看到3个指标的评分

### 预期日志输出
```
📊 开始质量评估...
🔍 [DEBUG] 开始DeepEval评估流程...
🔍 [DEBUG] 步骤1: 准备上下文，检索到 X 个文档
🔍 [DEBUG] 步骤2: 创建LLMTestCase...
🔍 [DEBUG] 步骤4: 开始并行执行3个指标评估...
🔍 [DEBUG] 开始评估指标: faithfulness
🔍 [LLM] generate 被调用...
🔍 [LLM] API响应成功
🔍 [DEBUG] faithfulness 评估完成，得分: 0.85
🔍 [DEBUG] 任务 1/3 完成
... (重复3次)
🔍 [DEBUG] 步骤5: 组装最终评估结果...
✅ 质量评估完成: 总分 0.85
```

---

**总结**: 
- ✅ 3个指标（与YZY一致）
- ✅ 无signal调用
- ✅ 简单的异常处理
- ✅ 多层超时保护
- ✅ 详细的DEBUG日志

**如果还有问题，请重启后端并查看DEBUG日志的最后一条消息！**

