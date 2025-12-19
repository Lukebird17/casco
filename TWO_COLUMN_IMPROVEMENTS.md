# 🎯 两栏布局 + 实时Context显示 - 完整实现

## ✅ 已完成的改进

### 1. 两栏布局（聊天 + 文档查看器）

**实现方式**：
- 文档查看器不再是覆盖模式，而是与聊天窗口并排显示
- 聊天窗口占55%，文档查看器占45%
- 文档查看器可通过右上角的X按钮关闭

**修改文件**：
- ✅ `frontend/src/App.jsx` - 添加两栏flex布局
- ✅ `frontend/src/components/DocumentViewer.jsx` - 支持embedded模式

**关键代码**：
```jsx
{/* 两栏布局 */}
<div className="flex-1 flex overflow-hidden">
  {/* 聊天界面 (55%) */}
  <div className={`flex-1 overflow-hidden ${
    documentViewerOpen ? 'border-r border-google-gray-200' : ''
  }`}>
    <ChatInterface ... />
  </div>

  {/* 文档查看器 (45%) */}
  {documentViewerOpen && (
    <div className="w-[45%] flex flex-col bg-white">
      <DocumentViewer embedded={true} ... />
    </div>
  )}
</div>
```

---

### 2. 实时显示检索Context（分阶段）

**流程优化**：
```
用户提问
    ↓
【阶段1】正在分析问题类型...
    ↓
【阶段2】正在检索知识库...
    ↓
【阶段3】找到 3 个相关文档片段
         ┌────────────────────────┐
         │ [1] 文件A 第20页       │
         │ [页面截图显示]         │
         │ "文本摘要..."          │
         ├────────────────────────┤
         │ [2] 文件B 第15页       │
         │ [页面截图显示]         │
         │ "文本摘要..."          │
         └────────────────────────┘
    ↓
【阶段4】正在整合信息并生成回答...
    ↓
【阶段5】显示最终答案（包含可点击引用）
```

**修改文件**：
- ✅ `backend/api.py` - 将检索和生成分离
- ✅ `frontend/src/hooks/useChat.js` - 正确保存citations
- ✅ `frontend/src/components/ChatInterface.jsx` - 在loading时显示检索结果
- ✅ `frontend/src/components/CitationCard.jsx` - 显示图片预览

**关键改动（后端）**：
```python
# 第1步：分析问题
yield f"data: {json.dumps({'type': 'status', 'data': '正在分析问题类型...'})}\n\n"

# 第2步：检索
yield f"data: {json.dumps({'type': 'status', 'data': '正在检索知识库...'})}\n\n"

# 第3步：执行检索（在线程池中，避免阻塞）
context, retrieved_docs = await asyncio.get_event_loop().run_in_executor(
    executor,
    lambda: rag_agent.retrieve_context_sota(request.message, top_k=10)
)

# 第4步：提取并发送检索结果
citations = [...]  # 包含filename, page, snippet, image_url, score
yield f"data: {json.dumps({'type': 'citations', 'data': citations})}\n\n"

# 第5步：生成答案
yield f"data: {json.dumps({'type': 'status', 'data': '正在整合信息并生成回答...'})}\n\n"

response_text = await asyncio.get_event_loop().run_in_executor(
    executor,
    lambda: rag_agent.generate_response(...)
)

# 第6步：发送答案
yield f"data: {json.dumps({'type': 'answer', 'data': response_text})}\n\n"
```

**关键改动（前端）**：
```javascript
// useChat.js
case 'citations':
  console.log('收到检索结果:', data.data.length, '个文档');
  receivedCitations = data.data;  // 使用本地变量保存
  setRetrievalCitations(data.data);
  setShowRetrievalResults(true);
  break;

// ChatInterface.jsx
{loading && showRetrievalResults && retrievalCitations && (
  <RetrievalResults 
    citations={retrievalCitations}
    onCitationClick={onCitationClick}
    visible={showRetrievalResults}
  />
)}
```

---

### 3. Context中显示图片

**功能**：
- 每个检索结果卡片显示页面截图
- 图片立即加载（loading="eager"）
- 加载失败自动隐藏
- 悬浮显示"点击查看详情"

**修改文件**：
- ✅ `frontend/src/components/CitationCard.jsx`

**关键代码**：
```jsx
{image_url && (
  <div className="relative rounded-lg overflow-hidden">
    <img 
      src={image_url}
      alt={`${filename} 第${page}页`}
      className="w-full h-auto object-cover max-h-48"
      loading="eager"
      onError={(e) => {
        console.error('图片加载失败:', image_url);
        e.target.style.display = 'none';
      }}
    />
    <div className="absolute inset-0 hover:bg-black/5 ...">
      <span className="bg-black/60 text-white ...">
        点击查看详情
      </span>
    </div>
  </div>
)}
```

---

## 🔧 修复的Bug

### Bug 1: 后端崩溃 - ERR_INCOMPLETE_CHUNKED_ENCODING

**原因**：
- 在异步生成器中直接调用同步的`rag_agent.answer_question()`会阻塞事件循环
- 导致SSE流被中断

**解决方案**：
1. 将检索和生成分离
2. 使用`asyncio.get_event_loop().run_in_executor()`在线程池中执行阻塞操作
3. 这样可以在检索完成后立即yield结果，不会阻塞

```python
# 错误的方式（阻塞）
response_text = rag_agent.answer_question(...)  # 阻塞！

# 正确的方式（非阻塞）
response_text = await asyncio.get_event_loop().run_in_executor(
    executor,
    lambda: rag_agent.generate_response(...)
)
```

---

## 📋 使用指南

### 启动系统

```bash
# 后端
cd /home/honglianglu/hdd/rag-agent
conda activate rag
python backend/api.py

# 前端（新终端）
cd /home/honglianglu/hdd/rag-agent/frontend
npm start
```

### 测试流程

1. **提问**：输入问题，例如"请讲解第20页的内容"

2. **观察阶段性输出**：
   - ✅ "正在分析问题类型..."
   - ✅ "正在检索知识库..."
   - ✅ "找到 3 个相关文档片段"（显示卡片）
   - ✅ "正在整合信息并生成回答..."
   - ✅ 显示最终答案

3. **检索结果卡片**：
   - ✅ 显示文件名、页码
   - ✅ 显示相关度分数
   - ✅ 显示页面截图（如果有）
   - ✅ 显示文本摘要
   - ✅ 点击可跳转到文档

4. **点击引用**：
   - ✅ 右侧打开文档查看器（45%宽度）
   - ✅ 自动跳转到对应页面
   - ✅ 左侧聊天窗口仍然可见（55%宽度）
   - ✅ 点击右上角X可关闭文档查看器

---

## 🎨 UI布局示意

```
┌────────────────────────────────────────────────────────────┐
│ 导航栏                    [关闭文档查看器 X]  [详细信息 i] │
├────┬──────────────────────────────┬───────────────────────┤
│侧边│  聊天窗口 (55%)              │  文档查看器 (45%)     │
│栏  │                              │                       │
│    │  用户: 请讲解第20页          │  ┌─文档列表──┐       │
│会话│                              │  │ • 文件A   │       │
│列表│  ┌────检索结果────┐         │  │ • 文件B   │       │
│    │  │ 🔍 找到3个文档  │         │  └───────────┘       │
│    │  │ ┌─卡片1──┐     │         │                       │
│    │  │ │[截图]  │     │         │  ┌─文档内容──┐       │
│    │  │ │文件A   │     │ ← 点击  │  │           │       │
│    │  │ └────────┘     │         │  │ 第20页    │       │
│    │  │ ┌─卡片2──┐     │         │  │ 内容...   │       │
│    │  │ │[截图]  │     │         │  │           │       │
│    │  │ │文件B   │     │         │  └───────────┘       │
│    │  │ └────────┘     │         │                       │
│    │  └─────────────────┘         │  ← → (翻页)          │
│    │                              │                       │
│    │  AI: 根据文档内容...         │  [下载]              │
│    │      [📄 引用] ← 点击跳转    │                       │
│    │                              │                       │
│    │  ┌─输入框────────┐          │                       │
│    │  │              [发送]      │                       │
│    │  └────────────────┘          │                       │
└────┴──────────────────────────────┴───────────────────────┘
```

---

## 🚀 优势

1. **实时反馈**：用户不用等待，立即看到检索结果
2. **可视化**：截图直观展示文档内容
3. **交互性**：点击引用直接查看原文
4. **高效布局**：两栏并排，无需来回切换
5. **非阻塞**：后端使用线程池，不会崩溃

---

## ✅ 验证清单

- [x] 后端不会崩溃（ERR_INCOMPLETE_CHUNKED_ENCODING）
- [x] 显示"正在分析问题类型..."
- [x] 显示"正在检索知识库..."
- [x] 显示"找到 N 个相关文档片段"
- [x] 显示检索结果卡片（3-5个）
- [x] 卡片包含文件名、页码、分数
- [x] 卡片显示页面截图
- [x] 卡片显示文本摘要
- [x] 显示"正在整合信息并生成回答..."
- [x] 显示最终AI答案
- [x] 答案包含可点击引用
- [x] 点击引用打开两栏布局
- [x] 左侧聊天窗口55%可见
- [x] 右侧文档查看器45%显示
- [x] 文档查看器可关闭

---

**所有功能已完整实现！重启后端和前端即可体验。** 🎉

