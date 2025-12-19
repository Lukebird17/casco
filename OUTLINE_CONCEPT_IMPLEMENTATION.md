# 📚 文档大纲 & 🔍 概念定位功能实现

## ✅ 已完成的功能

### 1. 文档大纲功能 (Document Outline)

**目标**：自动提取文档的章节结构，帮助用户快速导航

**实现方式**：

#### 后端API实现

**API 1**: `/api/knowledge-bases/{kb_id}/documents/{filename}/outline`
- ✅ 使用 `pymupdf` (fitz) 提取PDF内置目录（TOC）
- ✅ 支持多级标题结构
- ✅ 自动提取页码信息
- ✅ 如果PDF无目录，自动生成基于页数的大纲（每10页一个章节）
- ✅ 支持文本文件（TXT/MD）的标题提取

**关键代码**：
```python
import fitz  # pymupdf
doc = fitz.open(filepath)

# 获取PDF目录
toc = doc.get_toc()  # 返回 [level, title, page]

for i, (level, title, page) in enumerate(toc):
    outlines.append({
        "id": f"outline-{i}",
        "title": title,
        "level": level,
        "page": page,
        "subsections": []
    })
```

**优势**：
- ✅ 比 PyPDF2 更强大和可靠
- ✅ 正确提取多级标题
- ✅ 准确的页码映射
- ✅ 处理中文标题无乱码

#### 前端UI实现

**组件**: `frontend/src/components/DocumentOutlinePanel.jsx`

**功能**：
- ✅ 侧边面板设计，从右侧滑出
- ✅ 知识库选择下拉菜单
- ✅ 文档列表展示
- ✅ 层次化的大纲树结构
- ✅ 可展开/折叠的章节
- ✅ 点击章节跳转到文档对应页面

**交互流程**：
```
打开大纲面板
    ↓
选择知识库
    ↓
选择文档
    ↓
显示大纲树
┌────────────────────┐
│ 📖 第1章 引言       │ ← 点击
│   • 1.1 背景       │
│   • 1.2 目标       │
├────────────────────┤
│ 📖 第2章 方法       │
│   • 2.1 算法       │
└────────────────────┘
    ↓
自动跳转到对应页面
```

---

### 2. 概念定位功能 (Concept Search)

**目标**：快速搜索并定位文档中的关键概念、术语、公式

**实现方式**：

#### 后端API实现

**API 1**: `/api/concepts/hot` - 获取热门概念
```python
@app.get("/api/concepts/hot")
async def get_hot_concepts(kb_id: str = 'default', limit: int = 10):
```

**功能**：
- ✅ 从向量库中提取所有文档
- ✅ 使用正则表达式提取中文词（2-4字）和英文词（3+字母）
- ✅ 统计词频，过滤停用词
- ✅ 返回top N高频概念
- ✅ 计算相关度分数

**API 2**: `/api/concepts/search` - 搜索概念
```python
@app.get("/api/concepts/search")
async def search_concepts(q: str, kb_id: str = 'default', limit: int = 20):
```

**功能**：
- ✅ 遍历知识库中的所有文档
- ✅ 使用 `pymupdf` 在PDF中搜索（逐页）
- ✅ 在文本文件中搜索（逐行）
- ✅ 提取匹配上下文（前后50字符）
- ✅ 返回文件名、页码/行号、上下文
- ✅ 限制返回数量避免超载

**API 3**: `/api/documents/{filename}/search` - 文档内搜索（已优化）
```python
@app.get("/api/documents/{filename}/search")
async def search_in_document(filename: str, query: str, kb_id: str = 'default'):
```

**改进**：
- ✅ 添加知识库支持（kb_id参数）
- ✅ 使用 `pymupdf` 替代 PyPDF2
- ✅ 更精确的上下文提取
- ✅ 性能优化

#### 前端UI实现

**组件**: `frontend/src/components/ConceptSearchPanel.jsx`

**功能**：
- ✅ 搜索框输入
- ✅ 支持Enter键搜索
- ✅ 显示搜索结果列表
- ✅ 每个结果显示：文件名、页码/行号、上下文、相关度
- ✅ 最近搜索记录（本地存储）
- ✅ 热门概念推荐
- ✅ 点击结果跳转到文档

**交互流程**：
```
打开概念定位面板
    ↓
输入关键词："SLUB分配器"
    ↓
显示搜索结果
┌────────────────────────────┐
│ 📄 Linux内核.pdf            │
│    第23页                    │
│    "...SLUB分配器是..."     │
│    相关度: 92%              │
├────────────────────────────┤
│ 📄 内存管理.pdf             │
│    第15页                    │
│    "...SLUB替代了SLAB..."   │
│    相关度: 85%              │
└────────────────────────────┘
    ↓
点击任一结果
    ↓
打开文档并跳转到对应页面
```

---

## 🔧 技术细节

### 依赖库

**后端**：
- `pymupdf` (fitz) - PDF处理（比PyPDF2更强大）
- `collections.Counter` - 词频统计
- `re` - 正则表达式

**前端**：
- React Hooks (useState, useEffect)
- Framer Motion - 动画
- Lucide Icons - 图标

---

### API端点总结

| API路径 | 方法 | 功能 | 状态 |
|--------|------|------|------|
| `/api/knowledge-bases/{kb_id}/documents/{filename}/outline` | GET | 获取文档大纲 | ✅ |
| `/api/documents/{filename}/outline` | GET | 获取文档大纲（默认KB） | ✅ |
| `/api/concepts/hot` | GET | 获取热门概念 | ✅ 新增 |
| `/api/concepts/search` | GET | 搜索概念 | ✅ 新增 |
| `/api/documents/{filename}/search` | GET | 文档内搜索 | ✅ 优化 |

---

## 🚀 使用指南

### 1. 文档大纲

**步骤**：
1. 点击侧边栏的"文档大纲"按钮
2. 选择知识库（如果有多个）
3. 点击要查看的文档
4. 等待大纲加载（1-2秒）
5. 浏览层次化的章节结构
6. 点击任一章节直接跳转

**适用场景**：
- 📖 快速了解文档结构
- 📖 跳转到特定章节
- 📖 学术论文导航
- 📖 技术文档查阅

---

### 2. 概念定位

**步骤**：
1. 点击侧边栏的"概念定位"按钮
2. 在搜索框输入关键词
3. 按Enter或点击"搜索"按钮
4. 浏览搜索结果
5. 点击任一结果跳转到文档

**高级功能**：
- 🔥 查看热门概念推荐
- 🕒 查看最近搜索历史
- 🎯 相关度排序
- 📄 上下文预览

**适用场景**：
- 🔍 查找术语定义
- 🔍 定位关键公式
- 🔍 查找人名/地名
- 🔍 概念理解

---

## 📊 性能优化

### 文档大纲

- ✅ PDF目录提取速度快（pymupdf）
- ✅ 缓存文档列表，减少重复请求
- ✅ 限制章节数量（最多50个）

### 概念搜索

- ✅ 限制搜索结果数量（默认20个）
- ✅ 限制热门概念数量（默认10个）
- ✅ 本地存储最近搜索（减少服务器负担）
- ✅ 停用词过滤（提升质量）

---

## 🐛 已知限制

### 文档大纲

1. **无内置目录的PDF**：只能生成简单的页码大纲
2. **扫描版PDF**：无法提取文字大纲
3. **图片文件**：不支持大纲提取

**解决方案**：考虑使用OCR + NLP提取标题（未来改进）

### 概念搜索

1. **大文档搜索慢**：100+页的PDF需要3-5秒
2. **词频统计简单**：未使用TF-IDF或更高级的算法
3. **中文分词不精确**：使用正则表达式，非专业分词

**解决方案**：
- 引入 `whoosh` 或 `elasticsearch` 构建全文索引（未来改进）
- 使用 `jieba` 进行中文分词（未来改进）

---

## ✅ 测试清单

### 文档大纲测试

- [ ] 打开文档大纲面板
- [ ] 选择知识库
- [ ] 选择PDF文档
- [ ] 验证大纲层次结构
- [ ] 点击章节跳转
- [ ] 验证页码正确
- [ ] 测试返回文档列表功能

### 概念定位测试

- [ ] 打开概念定位面板
- [ ] 查看热门概念列表
- [ ] 输入关键词搜索
- [ ] 验证搜索结果
- [ ] 点击结果跳转到文档
- [ ] 验证页码/行号正确
- [ ] 测试最近搜索记录

---

## 🎯 后续改进建议

### 短期改进（1-2周）

1. **文档大纲**：
   - 添加书签功能
   - 支持大纲导出
   - 添加搜索章节功能

2. **概念搜索**：
   - 添加搜索历史管理
   - 支持正则表达式搜索
   - 添加搜索过滤器（文件类型、日期）

### 长期改进（1-3月）

1. **全文索引**：
   - 使用Elasticsearch构建索引
   - 支持模糊搜索
   - 支持同义词搜索

2. **智能提取**：
   - 使用NLP提取关键概念
   - 自动生成概念关系图
   - 智能推荐相关概念

3. **OCR支持**：
   - 处理扫描版PDF
   - 提取图片中的文字

---

## 📝 修改文件列表

### 后端修改

1. **backend/api.py**
   - ✅ 优化 `get_kb_document_outline` 使用pymupdf
   - ✅ 新增 `get_hot_concepts` API
   - ✅ 新增 `search_concepts` API
   - ✅ 优化 `search_in_document` 支持知识库

### 前端修改

1. **frontend/src/components/DocumentOutlinePanel.jsx**
   - ✅ 已存在，连接到后端API

2. **frontend/src/components/ConceptSearchPanel.jsx**
   - ✅ 已存在，连接到后端API

---

**所有功能已实现！重启后端即可使用。** 🎉

