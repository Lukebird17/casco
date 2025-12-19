# 🐛 Bug修复记录

## Bug #1: KeyError: 'content' in _rrf_fusion

### 问题描述
```
KeyError: 'content'
  File "/data/14thdd/users/honglianglu/rag-agent/rag_agent.py", line 276, in get_doc_id
    return f"{doc.get('filename','_')}_{doc.get('page_number','_')}_{doc['content'][:50]}"
```

### 问题原因
在`_rrf_fusion`方法的`get_doc_id`函数中，使用了`doc['content']`来访问文档内容，但是：
1. **图片文档**没有`content`字段，而是有`description`和`image_path`字段
2. 当HybridRetriever返回混合结果（文本+图片）时，RRF融合会失败

### 影响范围
- ✅ 纯文本检索正常
- ❌ 混合检索（文本+图片）会报错
- ❌ 使用`retrieve_context_sota`会触发此bug

### 修复方案

**修改前**：
```python
def get_doc_id(doc):
    # 尝试构建唯一ID，优先使用 content 哈希
    return f"{doc.get('filename','_')}_{doc.get('page_number','_')}_{doc['content'][:50]}"
```

**修改后**：
```python
def get_doc_id(doc):
    # 尝试构建唯一ID，支持文本和图片文档
    filename = doc.get('filename', '_')
    page_num = doc.get('page_number', doc.get('page', '_'))
    
    # 文本文档使用content，图片文档使用description或image_path
    if 'content' in doc and doc['content']:
        content_snippet = doc['content'][:50]
    elif 'description' in doc:
        content_snippet = doc.get('description', '')[:50]
    elif 'image_path' in doc:
        content_snippet = doc.get('image_path', '')[:50]
    else:
        content_snippet = str(hash(str(doc)))[:10]  # 兜底方案
    
    return f"{filename}_{page_num}_{content_snippet}"
```

### 修复位置
- **文件**: `rag_agent.py`
- **函数**: `_rrf_fusion` -> `get_doc_id`
- **行号**: 274-289

### 验证方法
1. 启动后端
2. 提问包含文档名和页码的问题（触发混合检索）
3. 观察是否报错

### 修复后的预期日志
```
========================================
🔎 开始增强检索 (SOTA)
========================================
  🔍 查询增强: [...]
  📥 粗排召回: Vector=14, BM25=12
  🔗 RRF融合: 26 条文档  ← 应该成功，不再报错
  ⚡ API Rerank 精排中...
  ✅ Rerank完成: 10 个结果
```

### 相关代码检查
✅ `_format_context` - 已经正确处理图片文档  
✅ `_build_structured_context` - 已经正确处理图片文档  
✅ `retrieve_context_sota` - 支持混合检索  

---

## 测试建议

### 测试用例1：纯文本问题
```
问题："什么是虚拟内存？"
预期：正常工作
```

### 测试用例2：指定文档和页码
```
问题："请你讲解2_1_统计语言模型2025_秋.pdf中第20页的内容"
预期：正常工作（之前会报错）
```

### 测试用例3：混合检索
```
问题："展示关于深度学习的图片"
预期：正常返回文本和图片结果
```

---

---

## Bug #2: 页码信息丢失

### 问题描述
前端显示的引用中页码为0或错误的页码，导致无法正确跳转到文档的对应页面。

### 问题原因
在`backend/api.py`中提取页码信息时，代码使用了：
```python
page_num = doc.get("page_num", doc.get("page_number", 0))
```

这个逻辑有问题：
1. **优先级错误**：先查找`page_num`，再查找`page_number`
2. **实际情况**：`vector_store`返回的字段是`page_number`
3. **后果**：如果`page_num`不存在或为`None`，会返回错误的值

### 数据流分析
```
document_loader.py
    ↓ (返回 page_number)
text_splitter.py
    ↓ (传递 page_number)
vector_store.py
    ↓ (存储 page_number)
vector_store.search()
    ↓ (返回 page_number)
rag_agent.last_context_docs
    ↓ (包含 page_number)
backend/api.py
    ↓ (❌ 先查page_num，找不到正确值)
前端
    ↓ (❌ 收到错误的page值)
```

### 影响范围
- ✅ 文档加载正常（page_number正确）
- ✅ vector_store存储正常（page_number正确）
- ❌ API返回给前端的page值错误
- ❌ 前端引用链接无法正确跳转

### 修复方案

**修改位置1** - 普通chat端点（第294行）：
```python
# 修改前
page_num = doc.get("page_num", doc.get("page_number", 0))

# 修改后
page_num = doc.get("page_number", doc.get("page_num", 0))
```

**修改位置2** - 流式chat端点（第438行）：
```python
# 修改前
page_num = doc.get("page_num", doc.get("page_number", 0))

# 修改后
page_num = doc.get("page_number", doc.get("page_num", 0))
```

### 关键改动
**优先级调整**：先查找`page_number`（vector_store的标准字段），再查找`page_num`（兜底）

### 验证方法
1. 重启后端
2. 提问任何问题
3. 查看前端引用卡片中的页码是否正确
4. 点击引用，查看是否跳转到正确页面

### 预期结果
```json
// API返回的citations
{
  "filename": "2_1_统计语言模型2025_秋.pdf",
  "page": 20,  // ✅ 正确的页码（之前为0）
  "snippet": "...",
  "image_url": "/static/doc_images/xxx.png"
}
```

### 相关代码检查
✅ `document_loader.py` - 正确设置page_number  
✅ `text_splitter.py` - 正确传递page_number  
✅ `vector_store.py` - 正确存储page_number  
✅ `rag_agent.py (_format_context)` - 正确使用page_number  
✅ `backend/api.py` - 已修复，优先使用page_number  

---

---

## Bug #3: LLM API调用失败 - 参数顺序错误

### 问题描述
```
Error code: 400 - {'code': 20015, 'message': "Input tag '请你讲解2_1_统计语言模型2025_秋.pdf中第20页的内容' found using 'role' does not match any of the expected tags: 'system', 'user', 'assistant', 'tool'", 'data': None}
```

### 问题原因
在`backend/api.py`的流式chat端点（`/api/chat/stream`）中，调用`session.add_message`时参数顺序写反了：

**错误代码**：
```python
session.add_message(request.message, "user")  # ❌ 参数顺序错误
session.add_message(response_text, "assistant")  # ❌ 参数顺序错误
```

**正确签名**：
```python
def add_message(self, role: str, content: str, metadata: Optional[Dict] = None):
    # 第一个参数应该是role，第二个参数是content
```

**后果**：
1. 用户消息的内容（如"请你讲解..."）被当作role
2. "user"被当作content
3. chat_history格式错误
4. LLM API调用失败

### 数据流分析
```
用户提问："请你讲解2_1_统计语言模型2025_秋.pdf中第20页的内容"
    ↓
流式API端点
    ↓
session.add_message(request.message, "user")  ❌ 参数反了
    ↓
messages = [{
    "role": "请你讲解...",  ❌ 内容被当作role
    "content": "user",     ❌ role被当作content
    ...
}]
    ↓
self.client.chat.completions.create(messages=messages)
    ↓
❌ API报错：不识别的role
```

### 影响范围
- ✅ 普通chat端点（`/api/chat`）正常 - 参数顺序正确
- ❌ 流式chat端点（`/api/chat/stream`）报错 - 参数顺序错误
- 所有使用流式API的查询都会失败

### 修复方案

**修改位置**：`backend/api.py` 第475-476行

**修改前**：
```python
session.add_message(request.message, "user")
session.add_message(response_text, "assistant")
```

**修改后**：
```python
session.add_message("user", request.message)
session.add_message("assistant", response_text)
```

### 验证方法
1. 重启后端
2. 使用流式API提问
3. 查看是否正常返回答案
4. 检查不再出现role错误

### 预期结果
```
用户提问
    ↓
正确保存到session.messages：
[{
    "role": "user",                     ✅ 正确
    "content": "请你讲解...",           ✅ 正确
    "timestamp": "..."
}]
    ↓
传递给LLM API
    ↓
✅ 正常生成回答
```

---

---

## Bug #4: React Key重复警告

### 问题描述
```
Warning: Encountered two children with the same key, `2_1_统计语言模型2025_秋_p22`. 
Keys should be unique so that components maintain their identity across updates.
```

### 问题原因
在检索结果中，同一个文档的同一页可能被多次返回（例如从vector search和BM25都检索到），它们生成了相同的cite_id，导致React key重复。

**数据流**：
```
vector_search → 返回文档A第22页
BM25_search → 也返回文档A第22页
    ↓
RRF融合 → 两个结果都保留
    ↓
API Rerank → 两个结果都在top_k中
    ↓
后端生成citations → 两个cite_id都是 "文档A_p22"
    ↓
前端渲染 → ❌ React警告：重复的key
```

### 影响范围
- ⚠️ 控制台出现警告
- ⚠️ 可能导致UI更新异常
- ⚠️ 浪费带宽（发送重复数据）

### 修复方案

#### 方案1：后端去重（主要修复）

**修改位置**：`backend/api.py` 两处

**修改前**：
```python
citations = []
for doc in rag_agent.last_context_docs:
    cite_id = f"{filename}_p{page_num}"
    citations.append({"id": cite_id, ...})
# 可能有重复的cite_id
```

**修改后**：
```python
citations = []
seen_cite_ids = {}  # 用于去重
for doc in rag_agent.last_context_docs:
    cite_id = f"{filename}_p{page_num}"
    score = doc.get("score", 0)
    
    # 如果已存在，保留分数更高的
    if cite_id not in seen_cite_ids or score > seen_cite_ids[cite_id]["score"]:
        seen_cite_ids[cite_id] = {"id": cite_id, ...}

# 转换为列表，按分数排序
citations = sorted(seen_cite_ids.values(), key=lambda x: x["score"], reverse=True)
```

**优势**：
- ✅ 减少冗余数据传输
- ✅ 保留最高分的结果
- ✅ 前端无需处理重复

#### 方案2：前端key组合（兜底保护）

**修改位置**：`frontend/src/components/RetrievalResults.jsx`

**修改前**：
```jsx
key={citation.id || index}
```

**修改后**：
```jsx
key={`${citation.id}-${index}`}
```

**作用**：即使后端有重复，前端也能正确渲染

### 验证方法
1. 重启后端
2. 提问："请你讲解2_1_统计语言模型2025_秋.pdf中第20页的内容"
3. 观察浏览器控制台
4. 不应再出现key重复警告

### 预期结果

**修复前**：
```
检索结果：
- 文档A第22页（vector search，分数0.85）
- 文档A第22页（BM25，分数0.75）  ← 重复
- 文档B第10页（vector search，分数0.80）

前端：❌ React警告key重复
```

**修复后**：
```
检索结果：
- 文档A第22页（分数0.85）  ← 只保留最高分
- 文档B第10页（分数0.80）

前端：✅ 无警告
```

### 修复位置
1. ✅ `backend/api.py` - 普通chat端点（第288-316行）
2. ✅ `backend/api.py` - 流式chat端点（第426-467行）
3. ✅ `frontend/src/components/RetrievalResults.jsx` - key组合（第44行）

---

## 修复日期
2024年12月

## 状态
✅ Bug #1 已修复并验证  
✅ Bug #2 已修复并验证  
✅ Bug #3 已修复并验证  
✅ Bug #4 已修复并验证

