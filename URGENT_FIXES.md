# 🔧 紧急修复清单

## 问题1: 去掉知识图谱功能

### 操作步骤
编辑 `frontend/src/components/Sidebar.jsx`，找到知识图谱按钮并删除或注释：

```jsx
// 删除或注释这个按钮
// { id: 'knowledge-graph', icon: Network, label: '知识图谱' },
```

## 问题2: 雷达图替代置信度分析

### 当前状态
- ✅ 雷达图已在 `QualityMetrics.jsx` 中实现
- ✅ 已在 `ToolPanel.jsx` 中显示
- ⚠️ 需要确认UI位置是否正确

### 确认
雷达图目前显示在右侧面板，包含3个维度：
- 忠实度 (Faithfulness)
- 相关性 (Answer Relevancy)  
- 检索质量 (Contextual Relevancy)

这应该已经替代了原来的置信度条。

## 问题3: Context显示时机 ⚠️重要

### 当前问题
Context只在LLM输出完成后才显示。

### 需求
1. ✅ LLM开始生成前 - 显示检索到的context
2. ✅ LLM生成过程中 - context保持显示
3. ✅ LLM生成完成后 - context依然显示

### 当前实现检查
查看 `ChatInterface.jsx` 第65-97行：

```jsx
{/* 检索结果展示（答案出现后也保持显示，不消失） */}
{showRetrievalResults && retrievalCitations && retrievalCitations.length > 0 && (
  <RetrievalResults 
    citations={retrievalCitations}
    onCitationClick={onCitationClick}
    visible={true} // Always visible once shown
  />
)}
```

**问题**: `showRetrievalResults` 的控制逻辑可能有问题。

### 修复方案
检查 `useChat.js` 中 `showRetrievalResults` 的设置：

```javascript
// 确保在收到citations后立即显示，且永不隐藏
case 'citations':
  const citations = JSON.parse(event.data);
  setRetrievalCitations(citations);
  setShowRetrievalResults(true);  // ✅ 设置为true
  break;

// ❌ 删除任何设置为false的代码
// setShowRetrievalResults(false);  // 不要有这行
```

## 问题4: DeepEval相关性为0 🐛

### 原因分析

从日志看：
```
⚠️  LLM 生成异常: Request timed out.
```

**不是相关性指标bug，而是API超时！**

### 根本原因
1. DeepEval的每个指标调用LLM 2-3次
2. 你的API响应慢（>60秒）
3. 导致超时，返回fallback值0.5

### 解决方案A: 进一步加速（推荐）

修改 `quality_evaluator_advanced.py`:

```python
# 第361行 - 只用1个文档
eval_context_docs = retrieved_context[:1]  # 改为1

# 第363行 - 每个只取300字符
doc.get('content', '')[:300]  # 改为300

# 第90行 - 减少max_tokens
max_tokens=256  # 改为256
```

### 解决方案B: 使用简化评估（快速）

修改 `quality_evaluator_advanced.py` 第295行：

```python
self.deepeval_mode = False  # 禁用DeepEval
```

简化评估会基于规则快速给出分数，不调用LLM。

### 解决方案C: 异步评估（最佳但复杂）

让评估在后台运行，先返回答案，评估完成后再更新雷达图。

**推荐先用方案A或B**

## 🎯 快速修复顺序

### 1. 修复Context显示（最重要）

检查 `frontend/src/hooks/useChat.js`:

```javascript
// 搜索 setShowRetrievalResults(false)
// 如果找到，删除它！

// 应该只有这一处设置为true:
case 'citations':
  setRetrievalCitations(JSON.parse(event.data));
  setShowRetrievalResults(true);
  break;
```

### 2. 去掉知识图谱按钮

编辑 `frontend/src/components/Sidebar.jsx`:
- 找到 `knowledge-graph` 相关的按钮定义
- 删除或注释掉

### 3. 加速或禁用DeepEval

选择以下之一：

**选项A - 进一步加速**:
```python
# quality_evaluator_advanced.py
eval_context_docs = retrieved_context[:1]  # 第361行
[:300]  # 第363行
max_tokens=256  # 第90行
```

**选项B - 暂时禁用**:
```python
# quality_evaluator_advanced.py 第295行
self.deepeval_mode = False
```

## 📋 验证清单

- [ ] Context在LLM回答前就显示
- [ ] Context在回答后不消失
- [ ] 知识图谱按钮已移除
- [ ] 雷达图正常显示（3个维度）
- [ ] 没有API超时错误
- [ ] 评估分数不是全0

---

**优先级**: 
1. 🔴 Context显示时机（用户体验）
2. 🟡 DeepEval加速/禁用（性能）
3. 🟢 去掉知识图谱（清理）

