# 🎓 RAG智能学习助手

> 基于检索增强生成(RAG)技术的智能课程助教系统，提供文档问答、知识图谱、质量评估等功能

![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-green.svg)
![React](https://img.shields.io/badge/react-18.3-61dafb.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)

---

## ✨ 核心特性

### 🚀 智能检索
- **混合检索**: 结合BM25关键词匹配和向量语义搜索，提升检索精度
- **智能重排序**: 使用BGE-Reranker-v2-m3模型进行结果重排序
- **多模态支持**: 支持PDF、Word、PPT、图片等多种文档格式

### 📊 质量评估
- **AI自省报告**: 5维度自动评估答案质量
  - 忠实度 (Faithfulness): 答案是否基于检索内容
  - 相关性 (Relevancy): 答案是否直接回应问题
  - 完整性 (Completeness): 答案是否全面
  - 准确性 (Accuracy): 答案是否准确无误
  - 检索质量 (Retrieval Quality): 检索文档的相关性
- **置信度计算**: 基于检索相似度的置信度评分
- **可视化展示**: 雷达图直观展示评估结果

### 🎯 高级功能
- **知识图谱**: 自动构建课程知识网络，支持概念关系可视化
- **概念检索**: 智能识别并高亮文档中的关键概念
- **文档大纲**: 自动提取PDF文档目录结构
- **记忆卡片**: 自动生成学习记忆卡片
- **苏格拉底模式**: 引导式教学，培养独立思考能力

### 🎨 现代化界面
- **Gemini风格**: 仿照Google Gemini的简洁美观设计
- **实时流式输出**: 使用SSE技术实现逐字输出效果
- **LaTeX渲染**: 完美支持数学公式显示（KaTeX）
- **引用跳转**: 点击引用直接定位到原文档对应位置
- **深色模式**: 支持深色/浅色主题切换

---

## 📁 项目结构

```
rag-agent/
├── src/                          # 源代码（模块化设计）
│   ├── core/                     # 核心RAG功能
│   │   ├── rag_agent.py         # 主RAG引擎
│   │   ├── vector_store.py      # ChromaDB向量存储
│   │   ├── hybrid_retriever.py  # 混合检索器（BM25+向量）
│   │   ├── reranker.py          # BGE重排序器
│   │   └── image_vector_store.py # 图片向量存储
│   │
│   ├── processors/               # 文档处理
│   │   ├── document_loader.py   # 多格式文档加载器
│   │   ├── text_splitter.py     # 智能文本分割
│   │   ├── enhanced_ocr.py      # OCR文字识别
│   │   └── image_describer.py   # 图片描述生成
│   │
│   ├── evaluators/               # 质量评估
│   │   ├── quality_evaluator.py # 5维度质量评估
│   │   └── confidence_calculator.py # 置信度计算
│   │
│   ├── features/                 # 高级功能
│   │   ├── knowledge_graph.py   # 知识图谱生成
│   │   ├── flashcard_system.py  # 记忆卡片系统
│   │   ├── socratic_mode.py     # 苏格拉底模式
│   │   ├── reasoning_chain.py   # 推理链
│   │   ├── quiz_generator.py    # 测验生成
│   │   ├── document_heatmap.py  # 文档热力图
│   │   ├── document_outline.py  # 文档大纲
│   │   └── enhanced_features.py # 增强功能
│   │
│   └── utils/                    # 工具类
│       ├── session_manager.py   # 会话管理
│       ├── token_tracker.py     # Token统计
│       ├── dynamic_db_manager.py # 动态数据库管理
│       └── snippet_manager.py   # 代码片段管理
│
├── backend/                      # FastAPI后端
│   ├── api.py                   # RESTful API
│   └── sessions/                # 会话存储
│
├── frontend/                     # React前端
│   ├── src/
│   │   ├── components/          # UI组件
│   │   ├── hooks/               # 自定义Hooks
│   │   └── api/                 # API客户端
│   └── package.json
│
├── data/                         # 原始文档目录
│   └── NLP/                     # 示例：NLP课程文档
│
├── vector_db/                    # 向量数据库存储
│   ├── default/                 # 默认知识库
│   └── NLP/                     # NLP知识库
│
├── scripts/                      # 工具脚本
│   ├── process_data.py          # 数据处理
│   ├── rebuild_kg.py            # 重建知识图谱
│   └── update_imports.py        # 更新导入路径
│
├── tests/                        # 测试文件
│   ├── quick_test.py
│   └── test_latex_fix.py
│
├── config.py                     # 配置文件
├── requirements.txt              # Python依赖
├── start.sh                      # 一键启动脚本
├── stop.sh                       # 停止服务脚本
├── README.md                     # 本文档
└── INSTALL.md                    # 安装指南
```

---

## 🚀 快速开始

### 环境要求

- **Python**: 3.10 或更高版本
- **Node.js**: 18.0 或更高版本
- **操作系统**: Linux / macOS / Windows
- **内存**: 建议 8GB 以上
- **磁盘**: 建议 10GB 以上可用空间

### 快速安装

```bash
# 1. 克隆项目
git clone <repository-url>
cd rag-agent

# 2. 配置环境变量（复制并编辑config.py）
cp config.example.py config.py
# 编辑config.py，填入你的API密钥

# 3. 安装后端依赖
pip install -r requirements.txt

# 4. 安装前端依赖
cd frontend && npm install && cd ..

# 5. 启动服务
bash start.sh
```

### 访问应用

打开浏览器访问：**http://localhost:5173**

> 📖 详细安装步骤请参考 [INSTALL.md](INSTALL.md)

---

## 📚 使用指南

### 1. 上传文档

**方式一：批量上传**
- 将课程文档（PDF、Word、PPT等）放入 `data/` 目录
- 系统会自动检测并构建向量索引

**方式二：界面上传**
- 点击界面的"上传文档"按钮
- 选择文件并上传
- 系统实时处理并索引

### 2. 开始对话

- 直接在输入框输入问题
- 系统会从文档中检索相关内容并回答
- 支持上传图片进行多模态问答
- 支持上传临时文档进行即时分析

### 3. 查看引用

- 答案中的蓝色标签是引用链接
- 点击引用可跳转到原文档对应位置
- 右侧"检索结果"面板显示所有相关片段

### 4. 质量评估

- 点击答案下方的"详细信息"按钮
- 查看AI自省报告（雷达图）
- 了解答案的可靠性和改进方向

### 5. 知识图谱

- 点击左侧"知识图谱"按钮
- 查看课程概念网络可视化
- 点击节点查看详细说明
- 支持搜索和过滤功能

### 6. 多知识库管理

- 在输入框上方切换知识库
- 每个知识库对应一个课程或主题
- 支持动态创建和管理知识库

---

## ⚙️ 配置说明

### 基础配置 (config.py)

```python
# OpenAI API配置
OPENAI_API_KEY = "your-api-key-here"
OPENAI_API_BASE = "https://api.siliconflow.cn/v1"  # 或其他兼容服务

# 模型配置
TEXT_MODEL_NAME = "deepseek-ai/DeepSeek-V3"
MULTIMODAL_MODEL_NAME = "Pro/Qwen/Qwen2-VL-72B-Instruct"

# 向量数据库配置
CHROMA_PERSIST_DIR = "./vector_db"
COLLECTION_NAME = "default"

# 数据目录
DATA_DIR = "./data"
```

### 检索参数调整

```python
# 在 config.py 中调整
TOP_K = 5                    # 检索文档数量（推荐3-10）
CHUNK_SIZE = 500             # 文本分块大小（推荐300-800）
CHUNK_OVERLAP = 50           # 分块重叠大小（推荐CHUNK_SIZE的10%）
```

### 质量评估配置

```python
# 启用/禁用质量评估
enable_quality_evaluation = True

# 评估超时设置
evaluation_timeout = 60  # 秒
```

---

## 🛠️ 技术栈

### 后端技术
- **FastAPI**: 现代化高性能Web框架
- **ChromaDB**: 向量数据库，支持高效相似度搜索
- **Sentence-Transformers**: 文本嵌入模型
- **BGE-Reranker**: 智能检索重排序
- **Jieba**: 中文分词
- **Rank-BM25**: 关键词检索算法

### 前端技术
- **React 18**: 现代化前端框架
- **Vite**: 下一代前端构建工具
- **TailwindCSS**: 实用优先的CSS框架
- **Framer Motion**: 流畅的动画库
- **KaTeX**: 高质量数学公式渲染
- **Recharts**: React图表库
- **React Hot Toast**: 优雅的提示组件

### AI技术
- **RAG**: 检索增强生成
- **Hybrid Retrieval**: BM25 + 向量检索
- **Reranking**: BGE-Reranker-v2-m3
- **Streaming**: SSE流式输出
- **DeepEval**: 质量评估框架

---

## 📊 性能优化

### 1. 检索优化
- 使用混合检索提升召回率（BM25 + 向量检索）
- 使用重排序模型提升精确度（BGE-Reranker）
- 智能分块策略，保持语义完整性

### 2. 响应速度
- SSE流式输出，提升用户体验
- 异步处理，后台评估不阻塞主流程
- 数据库连接池管理

### 3. 内存管理
- 按需加载文档
- 定期清理过期会话
- 向量数据库分片存储

---

## 🐛 常见问题

### Q: 如何解决API限流问题？

**A:** 有以下几种方案：
1. 在 `config.py` 中配置多个API密钥进行轮询
2. 使用本地模型（如Ollama）
3. 降低并发请求数量

### Q: 文档上传失败怎么办？

**A:** 请检查：
1. 文档格式是否支持（PDF、Word、PPT、TXT、Markdown）
2. 文件大小不超过50MB
3. 文件名不包含特殊字符
4. 磁盘空间是否充足

### Q: 答案不准确怎么办？

**A:** 可以尝试：
1. 调整检索参数（增加TOP_K）
2. 检查文档质量，确保内容清晰
3. 查看质量评估报告，了解问题所在
4. 尝试重新表述问题

### Q: 前端无法连接后端？

**A:** 请检查：
1. 后端是否正常运行（访问 http://localhost:8000/docs）
2. 防火墙是否阻止了8000端口
3. CORS配置是否正确
4. 查看浏览器控制台的错误信息

### Q: LaTeX公式无法正确显示？

**A:** 请确保：
1. 公式使用 `$...$` (行内) 或 `$$...$$` (独立) 格式
2. 浏览器已加载KaTeX样式
3. 清除浏览器缓存后重试

### Q: 如何备份数据？

**A:** 需要备份以下目录：
```bash
# 备份向量数据库
tar -czf vector_db_backup.tar.gz vector_db/

# 备份会话数据
tar -czf sessions_backup.tar.gz backend/sessions/

# 备份原始文档
tar -czf data_backup.tar.gz data/
```

---

## 🔧 开发指南

### 项目设置

```bash
# 克隆仓库
git clone <repository-url>
cd rag-agent

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装开发依赖
pip install -r requirements.txt
cd frontend && npm install && cd ..
```

### 运行开发服务器

```bash
# 终端1：启动后端（自动重载）
cd backend
uvicorn api:app --reload --port 8000

# 终端2：启动前端（自动重载）
cd frontend
npm run dev
```

### 代码规范

- **Python**: 遵循PEP 8规范
- **JavaScript**: 使用ESLint配置
- **提交信息**: 使用语义化提交（feat, fix, docs等）

### 测试

```bash
# 运行Python测试
python -m pytest tests/

# 快速功能测试
python tests/quick_test.py
```

---

## 🤝 贡献指南

欢迎提交Issue和Pull Request！

### 贡献流程

1. Fork本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 提交Pull Request

### 提交规范

```
feat: 新功能
fix: 修复bug
docs: 文档更新
style: 代码格式调整
refactor: 重构代码
test: 测试相关
chore: 构建/工具链相关
```

---

## 📝 更新日志

### v2.0.0 (2024-12-21)

**🎉 重大更新**
- ✨ 完全重构项目结构，采用模块化设计
- ✨ 新增AI质量自省报告（5维度评估）
- ✨ 优化LaTeX公式渲染系统
- ✨ 新增知识图谱可视化功能
- ✨ 采用Gemini风格的现代化UI
- 🐛 修复多个已知问题
- 📝 完善文档和安装指南

**架构改进**
- 📦 源代码重组为 `src/{core,processors,evaluators,features,utils}`
- 🔧 统一import路径管理
- 🧹 清理冗余文件，提升项目可维护性

### v1.0.0 (2024-11)

- 🎉 初始版本发布
- ✨ 基础RAG功能
- ✨ 文档上传和检索
- ✨ 基础问答功能

---

## 📄 许可证

本项目采用 [MIT License](LICENSE) 开源协议

---

## 👥 联系方式

- **问题反馈**: 请提交 [GitHub Issue](issues)
- **功能建议**: 请提交 [GitHub Discussion](discussions)

---

## 🙏 致谢

感谢以下开源项目的支持：

- [FastAPI](https://fastapi.tiangolo.com/) - 现代化Python Web框架
- [React](https://react.dev/) - 构建用户界面的JavaScript库
- [ChromaDB](https://www.trychroma.com/) - AI原生向量数据库
- [Sentence-Transformers](https://www.sbert.net/) - 文本嵌入模型
- [BGE](https://github.com/FlagOpen/FlagEmbedding) - 中英文语义表示模型
- [DeepEval](https://github.com/confident-ai/deepeval) - LLM评估框架
- [TailwindCSS](https://tailwindcss.com/) - CSS框架
- [Vite](https://vitejs.dev/) - 前端构建工具

---

<div align="center">

**⭐ 如果这个项目对你有帮助，请给个Star！⭐**

Made with ❤️ by RAG Team

[⬆ 回到顶部](#-rag智能学习助手)

</div>
