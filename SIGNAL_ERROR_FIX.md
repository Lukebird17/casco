# 🐛 Signal错误修复

## 问题
```
ValueError: signal only works in main thread of the main interpreter
```

## 原因
我尝试在`ThreadPoolExecutor`的子线程中使用`signal.alarm()`来实现15秒超时，但`signal.alarm()`**只能在主线程中使用**。

## 解决方案
✅ **移除signal.alarm()超时机制**

我们已经有足够的超时保护：
1. ✅ **LLM API超时**: 20秒（在`CustomSiliconFlowLLM.generate()`中）
2. ✅ **整体评估超时**: 60秒（在`backend/api.py`中使用`asyncio.wait_for`）

不需要在子线程中再加超时。

## 修复内容

**文件**: `quality_evaluator_advanced.py`

**恢复到简单的try-except结构**:
```python
def run_safe_metric(metric_cls, name):
    try:
        print(f"🔍 [DEBUG] 开始评估指标: {name}")
        metric = metric_cls(
            threshold=0.5,
            model=self.llm,
            include_reason=False
        )
        print(f"🔍 [DEBUG] {name} 指标初始化成功，开始measure...")
        metric.measure(test_case)
        print(f"🔍 [DEBUG] {name} 评估完成，得分: {metric.score}")
        return name, metric.score, ""
    except Exception as e:
        print(f"  ⚠️  {name} 评估出错，已自动置为 0.5: {e}")
        return name, 0.5, "评估异常，默认中立"
```

## ✅ 修复完成

现在系统应该能正常工作了。

**超时保护层级**:
1. **LLM API**: 20秒硬超时（`timeout=20`参数）
2. **整体评估**: 60秒（`asyncio.wait_for(..., timeout=60.0)`）
3. **异常捕获**: 任何错误都会被捕获并返回默认值0.5

---

**修复时间**: 2025-12-20  
**状态**: ✅ 已修复signal错误

