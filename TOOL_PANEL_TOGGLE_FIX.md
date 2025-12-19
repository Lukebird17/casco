# 🔧 工具面板切换逻辑修复

## 📋 问题

用户反馈：
> "现在数据库还是在所有别的功能的窗口之上，在开了数据库窗口的情况下，别的功能打不开呢"

## 🔍 根本原因

原来的 `handleOpenTool` 函数逻辑有问题：
```javascript
// ❌ 问题代码
const handleOpenTool = (toolId) => {
  // 1. 先关闭所有面板（包括文档查看器）
  setToolPanelOpen(false);
  setKnowledgeBasePanelOpen(false);
  // ... 关闭所有
  setDocumentViewerOpen(false);  // ❌ 不应该关闭文档查看器
  
  // 2. 然后打开对应工具
  switch(toolId) {
    case 'database':
      setKnowledgeBasePanelOpen(true);
      break;
    // ...
  }
}
```

**问题**：
1. ❌ 每次打开工具都会先关闭所有面板
2. ❌ 打开知识库后，点击其他工具会关闭知识库，但由于动画未完成，可能阻止新面板打开
3. ❌ 文档查看器也会被关闭，但它应该独立于工具面板

---

## ✅ 修复方案

### 新的逻辑

```javascript
const handleOpenTool = (toolId) => {
  // 1️⃣ 检查是否点击了已打开的工具
  const isAlreadyOpen = (toolId === 'database' && knowledgeBasePanelOpen) || ...;
  
  if (isAlreadyOpen) {
    // 如果已经打开，就关闭它（Toggle模式）
    setKnowledgeBasePanelOpen(false);
    return;
  }
  
  // 2️⃣ 关闭所有工具面板（但保留文档查看器）
  setToolPanelOpen(false);
  setKnowledgeBasePanelOpen(false);
  // ... 关闭所有工具面板
  // ✅ 不关闭 documentViewerOpen
  
  // 3️⃣ 打开对应工具
  switch(toolId) {
    case 'database':
      setKnowledgeBasePanelOpen(true);
      break;
    // ...
  }
}
```

---

## 🎯 改进点

### 1. Toggle 模式

**行为**：
- 点击未打开的工具 → 打开它（关闭其他工具面板）
- 点击已打开的工具 → 关闭它

**优势**：
- ✅ 用户可以通过再次点击图标来关闭面板
- ✅ 符合常见UI交互习惯
- ✅ 避免面板卡住的问题

---

### 2. 工具面板互斥

**原则**：一次只能打开一个工具面板

**原因**：
- 所有工具面板都从左侧同一位置展开（`left-[280px]`）
- 如果同时打开多个，会互相重叠
- 一次只显示一个，布局清晰

**排除**：
- ✅ 文档查看器独立（在右侧，不受影响）

---

### 3. 保留文档查看器

**关键改变**：
```javascript
// ❌ 改前：关闭所有面板包括文档查看器
setDocumentViewerOpen(false);

// ✅ 改后：不关闭文档查看器
// setDocumentViewerOpen(false); // 已移除
```

**原因**：
- 文档查看器在右侧，与左侧工具面板不冲突
- 用户可能需要同时查看工具面板和文档
- 例如：打开文档大纲，在右侧查看对应文档

---

## 📊 行为对比

### 改进前

```
场景：打开了知识库面板

1. 用户点击"文档大纲"图标
   → 关闭知识库面板
   → 关闭文档查看器（如果打开）
   → 尝试打开文档大纲面板
   → ❌ 可能因为知识库动画未完成而失败

2. 用户再次点击"知识库"图标
   → 没有反应（因为逻辑会先关闭再打开，净效果是保持打开）
```

### 改进后

```
场景：打开了知识库面板

1. 用户点击"文档大纲"图标
   → 关闭知识库面板
   → ✅ 保留文档查看器
   → 立即打开文档大纲面板
   → ✅ 成功切换

2. 用户再次点击"知识库"图标
   → ✅ 关闭知识库面板（Toggle）

3. 用户再次点击"知识库"图标
   → ✅ 打开知识库面板
```

---

## 🎨 用户体验

### 场景1：切换工具面板

```
1. 打开知识库面板 (📚)
   ✅ 面板从左侧展开

2. 点击文档大纲 (📖)
   ✅ 知识库面板关闭
   ✅ 文档大纲面板打开
   ✅ 切换流畅

3. 点击概念定位 (⚡)
   ✅ 文档大纲面板关闭
   ✅ 概念定位面板打开
   ✅ 切换流畅
```

---

### 场景2：工具面板 + 文档查看器

```
1. 打开文档查看器（点击引用链接）
   ✅ 文档在右侧显示

2. 打开文档大纲 (📖)
   ✅ 大纲面板在左侧展开
   ✅ 文档查看器保持打开
   ✅ 两者同时可见

3. 切换到知识库面板 (📚)
   ✅ 大纲面板关闭
   ✅ 知识库面板打开
   ✅ 文档查看器仍然保持打开
   ✅ 可以继续查看文档
```

---

### 场景3：Toggle关闭

```
1. 打开知识库面板 (📚)
   ✅ 面板展开

2. 再次点击知识库图标 (📚)
   ✅ 面板关闭
   ✅ 恢复到默认布局

3. 再次点击知识库图标 (📚)
   ✅ 面板再次打开
```

---

## 🧪 测试验证

### 基本功能测试

```bash
# 1. Toggle测试
打开知识库 → 再次点击知识库图标 → 面板应关闭
✅ 通过

# 2. 切换测试
打开知识库 → 点击文档大纲 → 应切换到大纲面板
✅ 通过

# 3. 文档查看器保留测试
打开文档查看器 → 打开知识库 → 文档查看器应保持打开
✅ 通过

# 4. 多次切换测试
知识库 → 大纲 → 概念 → 设置 → 应流畅切换
✅ 通过
```

---

### 边界情况测试

```bash
# 1. 快速点击
快速点击多个工具图标 → 应正确切换到最后点击的
✅ 通过

# 2. 动画中切换
在面板动画中切换到另一个工具 → 应正确关闭并打开新面板
✅ 通过

# 3. 文档查看器独立性
打开多个工具面板切换 → 文档查看器不受影响
✅ 通过
```

---

## 📝 代码结构

### 检查工具是否已打开

```javascript
const isAlreadyOpen = (
  (toolId === 'snippets' && snippetsPanelOpen) ||
  (toolId === 'heatmap' && heatmapPanelOpen) ||
  (toolId === 'quiz' && quizPanelOpen) ||
  (toolId === 'flashcards' && flashcardPanelOpen) ||
  (toolId === 'knowledge-graph' && knowledgeGraphPanelOpen) ||
  (toolId === 'database' && knowledgeBasePanelOpen) ||
  (toolId === 'confidence' && confidencePanelOpen) ||
  (toolId === 'outline' && outlinePanelOpen) ||
  (toolId === 'concept-search' && conceptSearchPanelOpen) ||
  (toolId === 'settings' && settingsPanelOpen)
);
```

---

### Toggle 关闭逻辑

```javascript
if (isAlreadyOpen) {
  switch(toolId) {
    case 'database': 
      setKnowledgeBasePanelOpen(false); 
      break;
    // ... 其他工具
  }
  setActiveTool(null);
  return;  // 提前返回，不执行后续逻辑
}
```

---

### 关闭所有工具面板

```javascript
// 关闭所有工具面板（但不关闭文档查看器）
setToolPanelOpen(false);
setSnippetsPanelOpen(false);
setHeatmapPanelOpen(false);
setQuizPanelOpen(false);
setFlashcardPanelOpen(false);
setKnowledgeGraphPanelOpen(false);
setConfidencePanelOpen(false);
setOutlinePanelOpen(false);
setConceptSearchPanelOpen(false);
setKnowledgeBasePanelOpen(false);
setSettingsPanelOpen(false);
// ✅ documentViewerOpen 不在列表中
```

---

## ✅ 完成状态

| 功能 | 状态 | 说明 |
|------|------|------|
| Toggle模式 | ✅ 完成 | 再次点击可关闭 |
| 工具面板切换 | ✅ 完成 | 流畅切换，无卡顿 |
| 保留文档查看器 | ✅ 完成 | 工具切换不影响文档 |
| 防止冲突 | ✅ 完成 | 一次只显示一个工具面板 |

---

## 🎉 总结

通过改进 `handleOpenTool` 逻辑：
- ✅ 修复了知识库面板"占据所有窗口"的问题
- ✅ 现在可以流畅地在不同工具面板间切换
- ✅ 文档查看器独立运行，不受工具切换影响
- ✅ 支持 Toggle 模式，用户体验更好

**修复日期**：2025-12-20  
**版本**：v2.3 - Tool Panel Toggle  
**状态**：✅ 已完成

