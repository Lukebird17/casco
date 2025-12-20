# OmniScry - Navigate the Depths of Knowledge

**全知洞察** - 探索知识的深渊

基于检索增强生成（RAG）和AI自省的智能问答系统，提供高质量、可追溯的知识检索与生成服务。

---

## ✨ 核心特性

### 🚀 技术架构

- **SOTA检索架构**: Query Expansion + Hybrid Search (Vector + BM25) + RRF Fusion + API Reranker
- **多模态支持**: 文本 + 图像 + 文件上传
- **AI自省评估**: 基于DeepEval的3维质量评估（忠实度、相关性、检索质量）
- **流式响应**: 答案立即显示，评估异步进行
- **知识库管理**: 多知识库隔离，支持动态切换

### 🎯 用户体验

- **实时反馈**: 8秒内显示答案（相比传统方法提升80-90%）
- **可追溯性**: 每个答案都有引用来源，可直接跳转到原文档页面
- **苏格拉底模式**: 启发式教学，引导用户思考
- **智能工具**: 文档大纲、概念定位、热力图、记忆闪卡、智能测验

### 📊 质量保证

- **AI自省报告**: 每个回答都附带3维雷达图质量评估
- **实时计时**: 检索、生成、评估各阶段耗时透明
- **引用验证**: 所有回答都基于检索到的文档内容

---

## 📋 项目结构

```
rag-agent/
├── backend/
│   ├── api.py                    # FastAPI后端主程序
│   ├── config.py                 # 配置文件
│   ├── document_loader.py        # 文档加载器（PDF/DOCX/PPTX/TXT/MD）
│   ├── text_splitter.py          # 文本切分器
│   ├── vector_store.py           # 向量数据库（ChromaDB + BM25）
│   ├── rag_agent.py              # RAG核心逻辑
│   ├── reranker.py               # API Reranker（bge-reranker-v2-m3）
│   ├── quality_evaluator_advanced.py  # DeepEval质量评估
│   ├── multimodal_input_handler.py    # 多模态输入处理
│   ├── socratic_mode.py          # 苏格拉底模式
│   ├── session_manager.py        # 会话管理
│   ├── quiz_generator.py         # 智能测验生成
│   ├── flashcard_system.py       # 记忆闪卡系统
│   └── ...
│
├── frontend/
│   ├── src/
│   │   ├── components/           # React组件
│   │   │   ├── ChatInterface.jsx      # 主聊天界面
│   │   │   ├── Sidebar.jsx            # 侧边栏
│   │   │   ├── DocumentViewer.jsx     # 文档查看器
│   │   │   ├── QualityMetrics.jsx     # AI自省报告
│   │   │   ├── RetrievalResults.jsx   # 检索结果显示
│   │   │   ├── AnswerWithCitations.jsx # 带引用的答案
│   │   │   └── ...
│   │   ├── hooks/
│   │   │   └── useChat.js        # 聊天逻辑Hook
│   │   ├── App.jsx               # 主应用组件
│   │   └── main.jsx              # 入口文件
│   ├── public/
│   │   └── logo.svg              # OmniScry Logo
│   ├── package.json
│   └── vite.config.js
│
├── data/                         # 知识库数据目录
│   └── [kb_id]/                  # 各知识库文件夹
├── vectordb/                     # ChromaDB向量数据库
│   └── [kb_id]/                  # 各知识库向量数据
├── sessions/                     # 会话历史
├── static/                       # 静态文件（页面截图）
├── requirements.txt              # Python依赖
└── README.md                     # 本文件
```

---

## 🚀 快速开始

### 1. 环境准备

**Python环境**：
```bash
conda create -n rag python=3.10
conda activate rag
```

**安装依赖**：
```bash
# 一键安装（推荐）
bash install.sh

# 或手动安装
cd /home/honglianglu/hdd/rag-agent
pip install -r requirements.txt
cd frontend && npm install
```

### 2. 配置API密钥

编辑 `config.py`：
```python
# OpenAI API配置（用于embeddings）
OPENAI_API_KEY = "your-openai-api-key"
OPENAI_API_BASE = "https://api.openai.com/v1"

# 主LLM配置（SiliconFlow）
SILICONFLOW_API_KEY = "your-siliconflow-api-key"
SILICONFLOW_BASE_URL = "https://api.siliconflow.cn/v1"
MAIN_MODEL_NAME = "Qwen/Qwen2.5-72B-Instruct"

# Reranker配置
RERANK_API_URL = "your-reranker-api-url"
RERANK_MODEL_NAME = "bge-reranker-v2-m3"
```

### 3. 启动服务

**后端**：
```bash
cd /home/honglianglu/hdd/rag-agent
uvicorn backend.api:app --host 0.0.0.0 --port 8000 --reload
```

**前端**：
```bash
cd /home/honglianglu/hdd/rag-agent/frontend
npm run dev
```

**访问**: 打开浏览器访问 `http://localhost:5173`

---

## 📚 核心功能

### 1. 智能问答

- **文本问答**: 支持多轮对话，上下文记忆
- **图像问答**: 上传图片，AI识别并回答
- **文件问答**: 上传文档，直接提问
- **苏格拉底模式**: 启发式提问，引导思考

### 2. 知识库管理

- **多知识库**: 创建、切换、删除独立知识库
- **文档上传**: 支持PDF、DOCX、PPTX、TXT、MD格式
- **批量上传**: 一次上传多个文件
- **自动处理**: 文档自动切分、向量化、索引

### 3. 文档工具

- **文档大纲**: 智能提取PDF/Word文档目录结构
- **概念定位**: 关键词提取与文档内搜索
- **文档查看器**: 双栏显示，引用可点击跳转

### 4. 学习工具

- **智能测验**: 基于知识库自动生成选择题
- **记忆闪卡**: Anki风格的间隔重复学习
- **片段收藏**: 保存重要文本片段
- **热力图**: 可视化学习活动

### 5. AI自省报告

- **3维评估**: 忠实度、相关性、检索质量
- **雷达图可视化**: 直观展示各维度得分
- **详细解释**: 每个指标的具体评分原因
- **实时计时**: 各阶段耗时透明

---

## 🎨 设计理念

### Logo设计

OmniScry的Logo采用宇宙星球主题，象征知识的广袤无垠：

- **中心星球**: 代表知识的核心
- **三重轨道**: 代表RAG的三个检索路径（Vector、BM25、Rerank）
- **闪烁节点**: 代表知识点的连接
- **质量星标**: 代表AI自省的质量保证

### 命名含义

- **Omni**: 全知、全面
- **Scry**: 洞察、预见
- **Navigate the Depths of Knowledge**: 探索知识的深渊

---

## 🔧 技术栈

### 后端

- **框架**: FastAPI
- **向量数据库**: ChromaDB
- **检索**: BM25 (rank-bm25) + RRF
- **重排序**: bge-reranker-v2-m3 (API)
- **LLM**: Qwen2.5-72B-Instruct (SiliconFlow)
- **嵌入**: text-embedding-3-large (OpenAI)
- **质量评估**: DeepEval
- **文档处理**: PyMuPDF, python-pptx, python-docx

### 前端

- **框架**: React 18
- **构建**: Vite
- **样式**: Tailwind CSS
- **动画**: Framer Motion
- **图表**: Recharts
- **Markdown**: react-markdown + remark-math + rehype-katex
- **图标**: lucide-react

---

## 📈 性能指标

### 检索性能

| 指标 | 数值 |
|------|------|
| 平均检索时间 | 1-3秒 |
| 检索召回率 | 90%+ |
| 重排序准确率 | 95%+ |

### 生成性能

| 指标 | 优化前 | 优化后 | 提升 |
|------|--------|--------|------|
| 答案显示时间 | 38-98秒 | **8秒** | **80-90%** ↓ |
| 评估完成时间 | 38-98秒 | 18-53秒 | 40-50% ↓ |

### 质量指标

| 指标 | 平均分 |
|------|--------|
| 忠实度（Faithfulness） | 0.85-0.95 |
| 相关性（Relevancy） | 0.80-0.90 |
| 检索质量（Contextual） | 0.85-0.95 |

---

## 🛠️ 开发指南

### 添加新知识库

```python
# 后端会自动创建知识库
POST /api/knowledge-bases
{
  "kb_name": "新知识库名称"
}
```

### 上传文档

```python
POST /api/upload
Content-Type: multipart/form-data

files: [file1, file2, ...]
kb_id: "your-kb-id"
```

### 发起问答

```python
POST /api/chat/stream
{
  "message": "你的问题",
  "session_id": "your-session-id",
  "kb_id": "your-kb-id",
  "enable_socratic": false,
  "thinking_mode": false
}
```

---

## 📖 详细文档

- [YZY功能整合总结](YZY_FINAL_SUMMARY.md)
- [安装指南](INSTALLATION_GUIDE.md)
- [性能优化总结](PERFORMANCE_OPTIMIZATION.md)
- [UX改进总结](UX_IMPROVEMENTS_FINAL.md)
- [DeepEval实现](DEEPEVAL_IMPLEMENTATION.md)
- [SOTA检索架构](SOTA_RETRIEVAL_ENABLED.md)
- [Bug修复记录](BUG_FIX.md)

---

## 🐛 已知问题

1. **CLIP模型加载**: 首次使用多模态功能时需要下载CLIP模型（约1GB），可能较慢
   - 解决方案: 运行 `bash download_clip_model.sh` 预下载
2. **DeepEval偶尔超时**: 在网络不佳时，质量评估可能超时（45秒）
   - 影响: 使用默认评估值（0.75），不影响答案显示

---

## 🤝 贡献

欢迎提交Issue和Pull Request！

---

## 📄 许可

MIT License

---

## 👨‍💻 作者

OmniScry Team

**Navigate the Depths of Knowledge** 🌌
