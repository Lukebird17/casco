# 🚀 RAG-Agent 完整安装指南

## 📋 系统要求

- Python 3.10+
- Node.js 16+ & npm
- Linux/macOS
- 至少 8GB RAM
- 足够的磁盘空间（用于存储向量数据库和文档）

---

## 📦 安装步骤

### 第一步：Python 后端依赖

#### 1.1 创建并激活虚拟环境（推荐）

```bash
cd /home/honglianglu/hdd/rag-agent

# 如果使用 conda
conda create -n rag python=3.10
conda activate rag

# 或使用 venv
python3 -m venv venv
source venv/bin/activate
```

#### 1.2 安装核心依赖

```bash
pip install -r requirements.txt
```

#### 1.3 手动安装（如果 requirements.txt 有问题）

**核心库**：
```bash
# FastAPI 和服务器
pip install fastapi==0.104.1
pip install uvicorn[standard]==0.24.0
pip install python-multipart==0.0.6

# OpenAI API
pip install openai==1.3.5

# 向量数据库
pip install chromadb==0.4.18
pip install sentence-transformers==2.2.2

# 文档处理
pip install pypdf2==3.0.1
pip install python-docx==1.1.0
pip install python-pptx==0.6.23
pip install markdown==3.5.1
pip install beautifulsoup4==4.12.2
pip install pillow==10.1.0

# 中文分词和BM25
pip install jieba==0.42.1
pip install rank-bm25==0.2.2

# PDF处理（用于文档大纲）
pip install pymupdf==1.23.8

# HTTP请求
pip install requests==2.31.0
```

**可选但推荐的库**：
```bash
# DeepEval质量评估（强烈推荐）
pip install deepeval==0.21.73

# LlamaIndex知识图谱
pip install llama-index==0.10.0
pip install llama-index-llms-openai==0.1.5
pip install llama-index-embeddings-openai==0.1.6
pip install llama-index-vector-stores-chroma==0.1.4

# 网络可视化（用于知识图谱）
pip install networkx==3.2.1

# 性能优化
pip install uvloop==0.19.0
```

**完全可选的库**（功能降级时仍可使用）：
```bash
# FlashRank重排（备选，我们用的是BGE API）
# pip install flashrank==0.2.0
```

---

### 第二步：前端依赖

```bash
cd /home/honglianglu/hdd/rag-agent/frontend

# 安装 Node.js 依赖
npm install
```

**核心前端包**（已在 package.json 中）：
- `react` - 前端框架
- `react-dom` - React DOM 渲染
- `react-markdown` - Markdown渲染
- `remark-math` / `rehype-katex` - LaTeX数学公式
- `framer-motion` - 动画
- `lucide-react` - 图标
- `recharts` - 雷达图可视化 ⭐
- `tailwindcss` - CSS框架

---

### 第三步：系统配置

#### 3.1 配置 LibreOffice（用于 Office 文档转换）

如果已安装 LibreOffice，在 `config.py` 中配置路径：

```python
# config.py
LIBREOFFICE_PATH = "/usr/bin/soffice"  # 或你的实际路径
```

查找 LibreOffice 路径：
```bash
which soffice
# 或
which libreoffice
```

#### 3.2 配置 API 密钥

编辑 `config.py`：

```python
# API配置
OPENAI_API_KEY = "your-api-key-here"  # 替换为你的API密钥
OPENAI_API_BASE = "https://api.siliconflow.cn/v1/"  # 或其他API地址

# 模型配置
TEXT_MODEL_NAME = "Qwen/Qwen2.5-72B-Instruct"
MULTIMODAL_MODEL_NAME = "Qwen/Qwen3-VL-32B-Instruct"
OPENAI_EMBEDDING_MODEL = "Pro/BAAI/bge-m3"
RERANK_MODEL_NAME = "Pro/BAAI/bge-reranker-v2-m3"  # BGE重排模型
```

---

## 🗂️ 目录结构

系统会自动创建以下目录：

```
/home/honglianglu/hdd/rag-agent/
├── data/                    # 原始文档存储
│   └── default/            # 默认知识库
├── vector_db/              # 向量数据库
│   └── default/            # 默认知识库向量
├── static/                 # 静态文件（缓存的图片等）
├── sessions/               # 会话数据
├── backend/               # 后端代码
├── frontend/              # 前端代码
├── rag_agent.py           # RAG核心逻辑
├── quality_evaluator_advanced.py  # DeepEval评估器
└── requirements.txt       # Python依赖列表
```

---

## 🎯 验证安装

### 验证 Python 依赖

```bash
cd /home/honglianglu/hdd/rag-agent

# 运行验证脚本
./verify_yzy_integration.sh
```

### 手动验证关键模块

```bash
# 验证核心模块
python3 << EOF
import fastapi
import openai
import chromadb
import jieba
from rank_bm25 import BM25Okapi
print("✅ 核心依赖正常")

try:
    import deepeval
    print("✅ DeepEval 可用")
except:
    print("⚠️  DeepEval 不可用（可选）")

try:
    from llama_index.core import VectorStoreIndex
    print("✅ LlamaIndex 可用")
except:
    print("⚠️  LlamaIndex 不可用（可选）")
EOF
```

### 验证前端依赖

```bash
cd /home/honglianglu/hdd/rag-agent/frontend
npm list recharts
# 应该显示 recharts@2.10.0 或类似版本
```

---

## 🚀 启动系统

### 方法1：使用启动脚本（推荐）

**终端1 - 启动后端**：
```bash
cd /home/honglianglu/hdd/rag-agent
./start_backend.sh
```

**终端2 - 启动前端**：
```bash
cd /home/honglianglu/hdd/rag-agent
./start_frontend.sh
```

### 方法2：手动启动

**后端**：
```bash
cd /home/honglianglu/hdd/rag-agent/backend
uvicorn api:app --host 0.0.0.0 --port 8000 --reload
```

**前端**：
```bash
cd /home/honglianglu/hdd/rag-agent/frontend
npm run dev
```

### 访问系统

- **前端**: http://localhost:5173
- **后端API**: http://localhost:8000
- **API文档**: http://localhost:8000/docs

---

## 📚 完整依赖列表

### Python 依赖（requirements.txt）

```txt
# Web框架
fastapi==0.104.1
uvicorn[standard]==0.24.0
python-multipart==0.0.6

# AI/ML
openai==1.3.5
sentence-transformers==2.2.2

# 向量数据库
chromadb==0.4.18

# 文档处理
pypdf2==3.0.1
python-docx==1.1.0
python-pptx==0.6.23
markdown==3.5.1
beautifulsoup4==4.12.2
pillow==10.1.0
pymupdf==1.23.8

# 中文NLP
jieba==0.42.1
rank-bm25==0.2.2

# 质量评估
deepeval==0.21.73

# 知识图谱
llama-index==0.10.0
llama-index-llms-openai==0.1.5
llama-index-embeddings-openai==0.1.6
llama-index-vector-stores-chroma==0.1.4
networkx==3.2.1

# 工具库
requests==2.31.0
uvloop==0.19.0
```

### 前端依赖（package.json）

```json
{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-markdown": "^9.0.0",
    "remark-math": "^6.0.0",
    "rehype-katex": "^7.0.0",
    "framer-motion": "^10.16.0",
    "lucide-react": "^0.294.0",
    "recharts": "^2.10.0"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.2.0",
    "autoprefixer": "^10.4.16",
    "postcss": "^8.4.32",
    "tailwindcss": "^3.3.6",
    "vite": "^5.0.5"
  }
}
```

---

## 🔧 常见问题

### 1. 依赖冲突

如果出现依赖冲突（特别是 click, requests 等），可以忽略警告，不影响核心功能。

### 2. DeepEval 安装失败

DeepEval 是可选的，如果安装失败，系统会自动降级到简化评估模式：
```bash
pip install deepeval
# 如果失败，系统仍可正常运行
```

### 3. LibreOffice 找不到

Office 文档处理需要 LibreOffice，如果没有：
```bash
# Ubuntu/Debian
sudo apt-get install libreoffice

# macOS
brew install --cask libreoffice

# 或者手动下载安装
# https://www.libreoffice.org/download/
```

### 4. 前端启动失败

```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
npm run dev
```

### 5. 端口占用

如果端口8000或5173被占用：
```bash
# 查找占用进程
lsof -i :8000
lsof -i :5173

# 杀死进程
kill -9 <PID>
```

---

## ✅ 安装检查清单

- [ ] Python 3.10+ 已安装
- [ ] Node.js 16+ 已安装
- [ ] Python 虚拟环境已创建并激活
- [ ] 所有 Python 依赖已安装（`pip install -r requirements.txt`）
- [ ] 前端依赖已安装（`npm install`）
- [ ] API 密钥已配置在 `config.py`
- [ ] LibreOffice 已安装并配置路径（可选）
- [ ] 运行 `./verify_yzy_integration.sh` 全部通过
- [ ] 后端可以正常启动（无报错）
- [ ] 前端可以正常启动并访问

---

## 🎉 功能特性

安装完成后，你的系统将拥有：

### 核心功能
- ✅ SOTA检索架构（Query Expansion + Vector + BM25 + RRF + BGE Reranker）
- ✅ DeepEval质量评估（3个指标 + 雷达图）
- ✅ 实时检索结果显示
- ✅ 可点击引用跳转文档
- ✅ 文档查看器（支持PDF/Word/PPT等）
- ✅ 多知识库管理
- ✅ LlamaIndex知识图谱
- ✅ 苏格拉底模式
- ✅ 文档大纲提取
- ✅ 概念搜索
- ✅ 会话管理

### 支持的文档类型
- PDF
- Word (docx)
- PowerPoint (pptx)
- Markdown (md)
- 纯文本 (txt)
- 图片（多模态）

---

## 📞 技术支持

如遇问题，请参考：
1. `YZY_FINAL_SUMMARY.md` - 完整功能说明
2. `FIX_DEEPEVAL_IMPORT_ERROR.md` - 导入错误修复
3. `./verify_yzy_integration.sh` - 自动诊断脚本

---

**祝你使用愉快！** 🚀

*最后更新: 2025-12-20*

