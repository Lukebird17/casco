# 智能课程助教系统 - RAG实现

基于检索增强生成（RAG）的智能课程助教系统，可以回答关于课程内容的问题。

## 📋 项目结构

```
Proj2/
├── config.py              # 配置文件（API密钥、参数设置）
├── document_loader.py     # 文档加载器（支持PDF/PPTX/DOCX/TXT）
├── text_splitter.py       # 文本切分器
├── vector_store.py        # 向量数据库（基于ChromaDB）
├── rag_agent.py          # RAG智能体核心逻辑
├── process_data.py       # 数据处理脚本
├── main.py               # 主程序入口
├── enhanced_features.py  # 可选的增强功能
├── requirements.txt      # 依赖包
└── data/                 # 课程文档目录
    ├── NLP-Slides/       # NLP课程PPT
    └── OS-Slides/        # OS课程PPT
```

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置API密钥

编辑 `config.py`，填写你的API配置：

```python
OPENAI_API_KEY = "your-api-key-here"
OPENAI_API_BASE = "https://api.deepseek.com"
MODEL_NAME = "deepseek-chat"
OPENAI_EMBEDDING_MODEL = "text-embedding-3-small"
```

### 3. 准备课程文档

将课程文档放入 `data/` 目录：
- 支持格式：PDF, PPTX, DOCX, TXT
- 建议选择内容丰富、结构清晰的课程课件

### 4. 处理数据并建库

```bash
python process_data.py
```

这会：
- 加载所有文档
- 进行文本切分
- 生成向量并存入ChromaDB

### 5. 启动对话系统

```bash
python main.py
```

## 💬 使用示例

```
学生: 词的连续向量表示为什么又称作"分布式表达"？

助教: 根据课程文档《3.1 词向量 2025.pptx》第 6 页的内容...

连续向量表示被称为"分布式表达"是因为：

1. **表示方式的本质**：在连续向量空间中，一个词由整个向量的所有维度共同表示，
   而不是只由某一个维度表示。

2. **与局部表达的对比**：传统的one-hot编码是"局部语义表达"或"非分布式表达"，
   每个词仅由一个维度（值为1）来表示，其他维度都是0。

3. **分布式的含义**：在词向量中，语义信息分布在向量的多个维度上，每个维度都
   捕获了词的某些语义特征，这些特征组合起来完整地表示了词的含义。

这种表示方法的优势在于能够捕获词之间的语义关系和相似度。
```

## ✨ 核心功能实现

### 1. 文档加载（document_loader.py）

支持多种文档格式的文本提取：

```python
# PDF提取
def load_pdf(file_path) -> List[Dict]:
    # 使用PyPDF2逐页提取文本
    
# PPT提取  
def load_pptx(file_path) -> List[Dict]:
    # 使用python-pptx提取幻灯片内容
    
# Word提取
def load_docx(file_path) -> str:
    # 使用docx2txt提取文本
    
# 纯文本
def load_txt(file_path) -> str:
    # 直接读取
```

### 2. 文本切分（text_splitter.py）

智能文本切分，保持上下文连续性：

```python
class TextSplitter:
    def split_text(self, text: str) -> List[str]:
        # 1. 按chunk_size切分
        # 2. 在句子边界处切分
        # 3. 保持chunk_overlap的重叠
        # 4. 返回文本块列表
```

**特点：**
- 尽量在句子边界处切分
- 相邻块之间有重叠，保持上下文
- PDF/PPT按页面处理，DOCX/TXT进行切分

### 3. 向量存储（vector_store.py）

基于ChromaDB的向量检索：

```python
class VectorStore:
    def get_embedding(self, text: str) -> List[float]:
        # 调用OpenAI Embedding API
        
    def add_documents(self, chunks: List[Dict]) -> None:
        # 批量向量化并存储
        
    def search(self, query: str, top_k: int) -> List[Dict]:
        # 向量相似度检索
```

**特点：**
- 持久化存储（自动保存到磁盘）
- 批量处理提高效率
- 返回相似度分数和元数据

### 4. RAG智能体（rag_agent.py）

核心RAG逻辑：

```python
class RAGAgent:
    def retrieve_context(self, query: str) -> Tuple[str, List[Dict]]:
        # 1. 向量检索相关文档
        # 2. 格式化为上下文字符串
        # 3. 包含来源信息
        
    def generate_response(self, query: str, context: str) -> str:
        # 1. 构建消息（System + Context + Query）
        # 2. 调用LLM生成回答
```

**System Prompt特点：**
- 明确助教角色定位
- 强调准确性和来源标注
- 处理特殊情况（无相关材料等）

## 🎯 扩展功能建议

项目包含了 `enhanced_features.py`，提供可选的增强功能：

### 1. 多查询检索（Multi-Query）

```python
from enhanced_features import QueryEnhancer

enhancer = QueryEnhancer()
queries = enhancer.enhance_query("什么是NLP？")
# 生成多个检索查询，提高召回率
```

### 2. 结果重排序（Rerank）

```python
from enhanced_features import ResultReranker

reranker = ResultReranker()
reranked_results = reranker.rerank_by_keyword_match(query, results)
# 基于关键词匹配度重新排序
```

### 3. Token追踪

```python
from enhanced_features import TokenCounter

tracker = TokenCounter()
tracker.track_query(prompt, response)
tracker.print_summary()
# 追踪Token消耗情况
```

### 如何集成增强功能

在 `rag_agent.py` 中添加：

```python
from enhanced_features import QueryEnhancer, ResultReranker

class EnhancedRAGAgent(RAGAgent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.enhancer = QueryEnhancer()
        self.reranker = ResultReranker()
    
    def retrieve_context(self, query: str, top_k: int = TOP_K):
        # 1. 生成多个查询
        queries = self.enhancer.enhance_query(query)
        
        # 2. 对每个查询检索
        all_results = []
        for q in queries:
            results = self.vector_store.search(q, top_k)
            all_results.extend(results)
        
        # 3. 去重和重排序
        unique_results = self._deduplicate(all_results)
        reranked = self.reranker.rerank_by_keyword_match(query, unique_results)
        
        # 4. 格式化返回
        return self._format_context(reranked[:top_k])
```

## 🔧 参数调优建议

在 `config.py` 中可以调整：

```python
# 文本切分
CHUNK_SIZE = 500        # 增大→每块包含更多上下文，但可能包含无关信息
CHUNK_OVERLAP = 100     # 增大→更好的上下文连续性，但冗余增加

# 检索
TOP_K = 5              # 增大→检索更多文档，但噪声可能增加

# Token限制
MAX_TOKENS = 8000      # 根据模型上下文窗口调整
```

**调优策略：**
1. 如果答案不够完整：增大 `TOP_K` 和 `CHUNK_SIZE`
2. 如果答案包含无关信息：减小 `TOP_K`，提高检索精度
3. 如果上下文断裂：增大 `CHUNK_OVERLAP`

## 📊 性能监控

系统会显示：
- 文档加载进度
- 向量化进度
- 检索到的文档数量

可以添加更详细的监控：

```python
import time

start = time.time()
results = agent.answer_question(query)
elapsed = time.time() - start

print(f"响应时间: {elapsed:.2f}秒")
```

## 🐛 常见问题

### 1. API调用失败

**错误：** `获取embedding失败`

**解决：**
- 检查API密钥是否正确
- 检查网络连接
- 确认API额度

### 2. 找不到相关内容

**问题：** 系统回答"未检索到相关材料"

**解决：**
- 确认文档已正确加载（查看process_data.py输出）
- 尝试增大 `TOP_K`
- 检查问题措辞是否与文档内容匹配

### 3. 回答不准确

**解决：**
- 优化System Prompt
- 使用重排序功能
- 增加检索文档数量
- 考虑使用更强的LLM模型

## 📚 技术栈

- **向量数据库：** ChromaDB
- **文档处理：** PyPDF2, python-pptx, python-docx
- **Embedding：** OpenAI text-embedding-3-small
- **LLM：** DeepSeek / OpenAI GPT系列
- **其他：** tqdm（进度条）

## 🎓 学习资源

如果想深入理解RAG技术，可以参考：

1. **基础概念：**
   - 向量检索原理
   - Embedding的作用
   - 上下文窗口管理

2. **进阶技术：**
   - 混合检索（BM25 + 向量）
   - 查询改写和扩展
   - 多轮对话支持

3. **本项目参考：**
   - `casco/` 目录：完整的生产级RAG系统
   - 包含更多高级特性：推理链、多语言、版本对比等

## 📝 作业提交

确保包含：
1. ✅ 所有TODO已实现
2. ✅ 代码可以正常运行
3. ✅ 对话示例截图
4. ✅ （可选）扩展功能说明

运行测试：
```bash
# 1. 处理数据
python process_data.py

# 2. 启动对话
python main.py

# 3. 测试几个问题，截图保存
```

祝你完成一个优秀的RAG系统！🎉

