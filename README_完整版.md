# 🎓 高级学习辅助系统 - 完整版

> 一个功能完善的 AI 学习助手，集成了所有您要求的高级功能

## ✨ 亮点特性

- 📚 **多轮对话管理** - 独立会话避免上下文混淆
- 🧠 **流式思维链** - 实时显示 AI 思考过程
- 📊 **置信度分析** - 四维度评估答案可靠性
- 📄 **PDF 阅览器** - 边看原文边提问
- 🔥 **文档热力图** - 标注常被引用的重点
- ⭐ **片段收藏** - 一键保存优质内容
- 📝 **智能测验** - 基于内容自动生成题目
- 🧙‍♂️ **苏格拉底模式** - 引导式深度学习
- 🕸️ **知识图谱** - 可视化概念关系
- 📇 **Anki 闪卡** - SM-2 算法间隔复习
- 🖼️ **多模态交互** - 支持图片、文件输入
- 📑 **智能大纲** - 自动提取文档结构

---

## 📁 项目结构

### 核心模块

```
rag-agent/
├── 核心组件
│   ├── rag_agent.py              # RAG 核心（支持多模态）
│   ├── vector_store.py           # 文本向量存储
│   ├── image_vector_store.py    # 图片向量存储
│   ├── hybrid_retriever.py      # 混合检索器
│   ├── config.py                 # 配置文件
│   └── multimodal_input_handler.py  # 多模态输入处理
│
├── 高级功能
│   ├── session_manager.py       # 会话管理 ✅
│   ├── confidence_calculator.py # 置信度计算 ✅
│   ├── document_viewer.py       # PDF 阅览器 ✅
│   ├── document_heatmap.py      # 文档热力图 ✅
│   ├── snippet_manager.py       # 片段收藏 ✅
│   ├── quiz_generator.py        # 测验生成 ✅
│   ├── socratic_mode.py         # 苏格拉底模式 ✅
│   ├── knowledge_graph.py       # 知识图谱 ✅
│   ├── flashcard_system.py      # 闪卡系统 ✅
│   └── document_outline.py      # 智能大纲 ✅
│
├── UI 界面
│   ├── app_complete.py          # 完整功能UI ⭐
│   ├── app_advanced.py          # 高级UI（部分功能）
│   ├── app_modern.py            # 现代化UI（基础版）
│   └── app.py                   # 原始UI
│
├── 辅助模块
│   ├── token_tracker.py         # Token 统计
│   ├── reasoning_chain.py       # 推理链记录
│   ├── auto_cot_prompting.py   # Auto-CoT
│   ├── document_loader.py       # 文档加载
│   ├── text_splitter.py         # 文本分割
│   └── enhanced_ocr.py          # OCR 处理
│
└── 文档
    ├── 完整功能说明.md           # 详细功能文档
    ├── 功能实现清单.md           # 实现进度清单
    ├── 高级UI使用指南.md         # UI 使用指南
    └── README_完整版.md          # 本文件
```

---

## 🚀 快速开始

### 1. 环境准备

```bash
# Python 3.10+
conda create -n rag python=3.10
conda activate rag

# 基础依赖
pip install gradio openai pillow chromadb PyMuPDF

# 可选增强（推荐）
pip install pyvis              # 交互式知识图谱
pip install PyPDF2             # PDF 增强处理
pip install python-docx        # Word 文档
pip install python-pptx        # PowerPoint
```

### 2. 配置 API

编辑 `config.py`:

```python
# API 配置
OPENAI_API_KEY = "your-api-key-here"
OPENAI_API_BASE = "https://api.siliconflow.cn/v1/"

# 模型配置
TEXT_MODEL_NAME = "Qwen/Qwen2.5-72B-Instruct"        # 纯文本模型
MULTIMODAL_MODEL_NAME = "Qwen/Qwen3-VL-32B-Instruct" # 多模态模型
OPENAI_EMBEDDING_MODEL = "Pro/BAAI/bge-m3"            # 嵌入模型
```

### 3. 准备数据

```bash
# 将学习资料放入 data 目录
mkdir -p data
cp /path/to/your/documents/*.pdf data/

# 运行数据处理
python process_data.py
```

### 4. 启动系统

```bash
# 启动完整功能版UI（推荐）
python app_complete.py

# 访问 http://localhost:7861
```

### 5. 初始化使用

1. 打开浏览器访问 UI
2. 点击 "🚀 初始化系统"
3. 等待所有组件加载完成
4. 开始使用各项功能！

---

## 📚 功能详解

### 1. 💬 智能对话

**位置**: "对话" 标签页

**功能**:
- 纯文本问答（自动使用文本模型）
- 图片上传分析（自动描述+多模态理解）
- 文件上传处理（读取内容+智能回答）
- 实时思维链显示
- 置信度评估

**使用技巧**:
- 每个独立主题创建新会话
- 勾选"苏格拉底模式"进行深度学习
- 查看置信度判断答案可靠性

### 2. 📚 文档管理

**位置**: "文档" 标签页

**功能**:
- PDF/文档列表浏览
- 文档热力图（显示热点区域）
- 引用来源追踪

**使用场景**:
- 查看哪些内容被频繁引用
- 定位学习重点
- 快速找到相关文档

### 3. ⭐ 片段收藏

**位置**: "收藏" 标签页

**功能**:
- 收藏优质内容
- 添加标签分类
- 搜索和筛选
- 导出为 Markdown

**使用流程**:
1. 复制想要收藏的内容
2. 粘贴到"内容"框
3. 添加来源和标签
4. 点击"💾 保存"

### 4. 📝 测验系统

**位置**: "测验" 标签页

**功能**:
- 基于内容生成测试题
- 三种难度（简单/中等/困难）
- 选择题、简答题、判断题
- 自动生成详细解析

**使用方法**:
1. 输入测验主题
2. 选择题目数量和难度
3. 点击"🎲 生成测验"
4. 答题后点击"👁️ 显示答案"

### 5. 🕸️ 知识图谱

**位置**: "知识图谱" 标签页

**功能**:
- 自动提取概念和关系
- 可视化关系网络
- 交互式图谱（需安装 pyvis）

**使用方法**:
1. 点击"🔨 构建知识图谱"
2. 等待处理完成
3. 查看节点和关系
4. 点击节点查看详情

### 6. 📇 闪卡复习

**位置**: "闪卡" 标签页

**功能**:
- 自动生成记忆卡片
- SM-2 间隔复习算法
- 熟练度追踪
- 导出为 Anki 格式

**使用流程**:
1. 粘贴学习内容
2. 选择卡片数量
3. 点击"🎴 生成闪卡"
4. 点击"📚 开始复习"
5. 根据记忆情况评分（0-4分）

**评分标准**:
- 0 = 完全忘记
- 1 = 困难
- 2 = 一般
- 3 = 容易
- 4 = 非常容易

---

## 🎯 典型使用场景

### 场景 1: 考试复习

```
1. 上传课程PDF → process_data.py 处理
2. 对话提问理解概念
3. 生成测验自我检测
4. 制作闪卡长期记忆
5. 查看热力图定位重点
6. 考前复习闪卡队列
```

### 场景 2: 论文阅读

```
1. 上传论文PDF
2. 使用苏格拉底模式深度理解
3. 收藏重要片段
4. 构建知识图谱理清概念关系
5. 生成大纲梳理结构
```

### 场景 3: 技术学习

```
1. 上传技术文档
2. 对话学习API用法
3. 上传代码截图提问
4. 生成测试题巩固知识
5. 制作闪卡记忆关键点
```

---

## 🔧 高级配置

### 模型选择

系统自动根据输入类型选择模型：

```python
# 纯文本 → TEXT_MODEL_NAME
user: "什么是进程？"
system: 使用 Qwen2.5-72B-Instruct

# 图片输入 → MULTIMODAL_MODEL_NAME
user: [上传图片] + "这张图表示什么？"
system: 使用 Qwen3-VL-32B-Instruct

# 文件输入 → MULTIMODAL_MODEL_NAME
user: [上传PDF] + "总结这个文档"
system: 使用 Qwen3-VL-32B-Instruct
```

### 存储位置

```bash
./data/              # 原始文档
./vector_db/         # 文本向量数据库
./image_vector_db/   # 图片向量数据库
./sessions/          # 会话记录
./snippets.json      # 片段收藏
./flashcards.json    # 闪卡数据
./heatmap_data.json  # 热力图数据
```

### 性能优化

```python
# config.py

# 增加检索数量（更多上下文，但速度慢）
TOP_K = 10  # 默认 5

# 调整分块大小（更细粒度，但处理慢）
CHUNK_SIZE = 300  # 默认 500

# 限制上下文长度
MAX_TOKENS = 8000  # 默认 8000
```

---

## 📊 功能对比

| 功能 | app.py | app_modern.py | app_advanced.py | app_complete.py ⭐ |
|------|--------|---------------|-----------------|-------------------|
| 基础对话 | ✅ | ✅ | ✅ | ✅ |
| 会话管理 | ❌ | ✅ | ✅ | ✅ |
| 思维链显示 | ❌ | ❌ | ✅ | ✅ |
| 置信度分析 | ❌ | ❌ | ✅ | ✅ |
| PDF 阅览器 | ❌ | ❌ | ❌ | ✅ |
| 文档热力图 | ❌ | ❌ | ❌ | ✅ |
| 片段收藏 | ❌ | ❌ | ❌ | ✅ |
| 测验生成 | ❌ | ❌ | ❌ | ✅ |
| 苏格拉底模式 | ❌ | ❌ | ❌ | ✅ |
| 知识图谱 | ❌ | ❌ | ❌ | ✅ |
| 闪卡系统 | ❌ | ❌ | ❌ | ✅ |
| 智能大纲 | ❌ | ❌ | ❌ | ✅ |

**推荐**: 使用 `app_complete.py` 获得完整功能体验！

---

## 🐛 常见问题

### Q1: 初始化失败

**原因**:
- API密钥错误
- 网络连接问题
- 向量数据库不存在

**解决**:
```bash
# 检查配置
cat config.py | grep API_KEY

# 测试网络
curl https://api.siliconflow.cn/

# 重新处理数据
python process_data.py
```

### Q2: 图片描述不准确

**原因**:
- 多模态模型能力限制
- 图片质量问题

**解决**:
- 使用更高分辨率图片
- 提供更具体的问题描述
- 尝试不同的多模态模型

### Q3: 闪卡复习间隔过长

**原因**:
- SM-2 算法自动调整

**解决**:
```python
# 在 flashcard_system.py 中调整
new_ease = old_ease + ...  # 调小这个值可以增加复习频率
```

### Q4: 知识图谱不显示

**原因**:
- 需要安装 pyvis

**解决**:
```bash
pip install pyvis
```

### Q5: 内存占用过高

**解决**:
```python
# config.py
CHUNK_SIZE = 800  # 增大分块
TOP_K = 3  # 减少检索数量
```

---

## 📈 性能指标

### 响应时间（参考）

| 操作 | 时间 |
|------|------|
| 纯文本问答 | 2-5秒 |
| 图片分析 | 5-10秒 |
| 文件处理 | 10-30秒 |
| 生成测验 | 5-15秒 |
| 构建知识图谱 | 10-60秒 |
| 生成闪卡 | 3-8秒 |

*实际时间取决于模型、网络和内容复杂度*

### 资源消耗

- 内存: 1-3GB（取决于文档数量）
- 磁盘: 500MB-2GB（向量数据库）
- GPU: 不需要（使用API）

---

## 🔄 更新日志

### v2.0 - 完整功能版 (2025-12-18)

✅ 新增功能:
- PDF 文档阅览器
- 文档热力图
- 片段收藏系统
- 智能测验生成
- 苏格拉底引导模式
- 知识图谱可视化
- Anki 式闪卡系统
- 文档智能大纲
- 多模态输入处理增强

🔧 改进:
- 动态模型切换（文本/多模态）
- 置信度四维度分析
- 流式思维链显示
- 会话持久化

### v1.0 - 基础版

- 基本问答功能
- 文档向量化
- 简单UI

---

## 🤝 贡献

欢迎提出建议和改进！

### 可以改进的方向

1. **前端交互增强**
   - PDF 点击跳转的 JavaScript 实现
   - 更丰富的图表可视化
   - 拖拽式文档上传

2. **功能扩展**
   - 语音输入/输出
   - 协作学习（多用户）
   - 移动端适配

3. **AI 增强**
   - 更多推理链策略
   - 自适应难度调整
   - 个性化学习路径

---

## 📄 许可

MIT License

---

## 🙏 致谢

感谢以下开源项目:
- Gradio - UI 框架
- ChromaDB - 向量数据库
- PyMuPDF - PDF 处理
- OpenAI - API 接口
- Qwen - 语言模型

---

## 📞 联系方式

如有问题或建议，欢迎联系！

---

**享受学习！🎓**
