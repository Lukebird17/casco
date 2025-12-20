# 🚀 快速安装指南

## 一键安装（推荐）

```bash
cd /home/honglianglu/hdd/rag-agent
./install.sh
```

脚本会自动安装所有依赖并验证。

---

## 手动安装

### 1. Python后端（必需）

```bash
cd /home/honglianglu/hdd/rag-agent

# 安装核心依赖
pip install fastapi uvicorn[standard] openai chromadb \
            pypdf2 pymupdf python-docx python-pptx \
            jieba rank-bm25 requests sentence-transformers

# 安装可选依赖（推荐）
pip install deepeval llama-index networkx
```

### 2. 前端（必需）

```bash
cd /home/honglianglu/hdd/rag-agent/frontend
npm install
```

---

## 核心依赖清单

### Python（15个核心包）

| 包名 | 用途 | 必需 |
|------|------|------|
| `fastapi` | Web框架 | ✅ |
| `uvicorn` | ASGI服务器 | ✅ |
| `openai` | LLM API | ✅ |
| `chromadb` | 向量数据库 | ✅ |
| `sentence-transformers` | 嵌入模型 | ✅ |
| `pypdf2` | PDF处理 | ✅ |
| `pymupdf` | PDF高级处理 | ✅ |
| `python-docx` | Word处理 | ✅ |
| `python-pptx` | PPT处理 | ✅ |
| `jieba` | 中文分词 | ✅ |
| `rank-bm25` | BM25检索 | ✅ |
| `requests` | HTTP请求 | ✅ |
| `deepeval` | 质量评估 | ⭐ 推荐 |
| `llama-index` | 知识图谱 | ⭐ 推荐 |
| `networkx` | 图可视化 | ⭐ 推荐 |

### 前端（8个核心包）

| 包名 | 用途 | 必需 |
|------|------|------|
| `react` | 前端框架 | ✅ |
| `react-dom` | DOM渲染 | ✅ |
| `react-markdown` | Markdown渲染 | ✅ |
| `remark-math` | 数学公式 | ✅ |
| `rehype-katex` | LaTeX渲染 | ✅ |
| `framer-motion` | 动画 | ✅ |
| `lucide-react` | 图标 | ✅ |
| `recharts` | 雷达图 | ✅ |

---

## 验证安装

```bash
# 验证Python
python3 -c "import fastapi, openai, chromadb, jieba; print('✅ Python依赖正常')"

# 验证前端
cd frontend && npm list recharts && echo "✅ 前端依赖正常"

# 完整验证
cd .. && ./verify_yzy_integration.sh
```

---

## 启动系统

```bash
# 终端1
./start_backend.sh

# 终端2  
./start_frontend.sh
```

访问: http://localhost:5173

---

## 完整文档

详细安装说明请查看: `INSTALLATION_GUIDE.md`

---

**安装时间**: 约5-10分钟  
**磁盘空间**: 约2-3GB（包含所有依赖）

