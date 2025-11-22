# RAG 问答智能体使用说明

## 概述

基于 RAG-Anything 框架实现的问答智能体，可以处理 PDF 文档并提供智能问答功能。

## 功能特点

- ✅ 支持批量处理 PDF 文档
- ✅ 支持多模态内容（图像、表格、公式）
- ✅ 支持多种查询模式（hybrid、local、global、naive）
- ✅ 输出格式符合示例模板规范
- ✅ 严格遵循 RAG-Anything 官方实现

## 环境配置

### 1. 安装依赖

```bash
# 安装 RAG-Anything
cd /home/honglianglu/ssd/casco/RAG-Anything
pip install -e .

# 安装其他依赖
pip install python-dotenv openai
```

### 2. 配置环境变量

在项目根目录创建 `.env` 文件（或者修改 `config_template.py`）：

```bash
# LLM 配置
CLOUD_MODEL=deepseek-chat
CLOUD_API_KEY=your_api_key_here
CLOUD_BASE_URL=https://api.deepseek.com/v1

# Embedding 配置
OPENAI_API_KEY=your_api_key_here
OPENAI_BASE_URL=https://api.openai.com/v1
OPENAI_API_MODEL=text-embedding-3-large
```

或者直接设置环境变量：

```bash
export CLOUD_API_KEY="your_api_key_here"
export CLOUD_BASE_URL="https://api.deepseek.com/v1"
export CLOUD_MODEL="deepseek-chat"
export OPENAI_API_KEY="your_api_key_here"
export OPENAI_BASE_URL="https://api.openai.com/v1"
export OPENAI_API_MODEL="text-embedding-3-large"
```

## 使用方法

### 方式 1：运行完整流程（推荐）

```bash
python rag_qa_agent.py
```

这将：
1. 批量处理 `data` 目录下的所有 PDF 文档
2. 使用示例问题进行查询
3. 保存结果到 `qa_results.json`

### 方式 2：运行示例

```bash
python simple_qa_example.py
```

选择运行模式：
- `1`: 简单示例（处理单个文档）
- `2`: 批量示例（处理多个文档）
- `3`: 自定义查询（交互式问答）

### 方式 3：编程使用

```python
import asyncio
from rag_qa_agent import RAGQAAgent

async def my_qa_task():
    # 初始化智能体
    agent = RAGQAAgent(
        working_dir="./rag_storage",
        parser="mineru",
        parse_method="auto"
    )
    
    # 处理文档
    await agent.process_document(
        file_path="path/to/your/document.pdf",
        output_dir="./output"
    )
    
    # 查询
    result = await agent.query(
        "你的问题？",
        mode="hybrid"
    )
    
    print(result['answer'])

asyncio.run(my_qa_task())
```

## 查询模式说明

- **hybrid**: 混合模式（推荐），结合本地和全局检索
- **local**: 本地检索模式，基于局部上下文
- **global**: 全局检索模式，基于整体知识图谱
- **naive**: 简单检索模式，基于向量相似度

## 输出格式

结果按照示例模板格式输出：

```json
{
  "items": [
    {
      "question": "这里填写提问内容",
      "retrieved_contexts": [
        "召回的上下文1",
        "召回的上下文2"
      ],
      "answer": "基于召回内容生成的回答"
    }
  ]
}
```

## 文件结构

```
/home/honglianglu/ssd/casco/
├── data/                          # PDF 文档目录
│   ├── 事故报告/
│   ├── 技术报告/
│   ├── 标准规范/
│   └── 行业报告/
├── rag_storage/                   # RAG 存储目录
├── output/                        # 解析输出目录
├── rag_qa_agent.py               # 主程序
├── simple_qa_example.py          # 使用示例
├── config_template.py            # 配置模板
├── qa_results.json               # 查询结果
└── README_RAG_QA.md             # 本文档
```

## 核心代码说明

### 1. 初始化 RAG 系统

```python
agent = RAGQAAgent(
    working_dir="./rag_storage",    # RAG 存储目录
    parser="mineru",                 # 解析器：mineru 或 docling
    parse_method="auto"              # 解析方法：auto, ocr, txt
)
```

### 2. 处理文档

```python
# 处理单个文档
await agent.process_document(
    file_path="path/to/document.pdf",
    output_dir="./output"
)

# 批量处理
await agent.process_folder(
    folder_path="path/to/folder",
    output_dir="./output",
    file_extensions=[".pdf"],
    recursive=True,
    max_workers=4
)
```

### 3. 查询

```python
# 单个查询
result = await agent.query(
    "你的问题？",
    mode="hybrid"
)

# 批量查询
results = await agent.query_batch(
    questions=["问题1", "问题2", "问题3"],
    mode="hybrid"
)
```

### 4. 保存结果

```python
agent.save_results(
    results,
    output_file="qa_results.json"
)
```

## 严格遵循官方实现

本实现严格按照 RAG-Anything 官方示例编写，包括：

1. **LLM 函数定义**：完全按照官方 `llm_model_func` 格式
2. **Vision 函数定义**：完全按照官方 `vision_model_func` 格式
3. **Embedding 函数**：使用 `EmbeddingFunc` 和 `openai_embed`
4. **文档处理**：使用 `process_document_complete` 和 `process_folder_complete`
5. **查询方法**：使用 `aquery` 和相关查询模式

## 注意事项

1. **API Key**: 确保正确配置 API Key
2. **文档大小**: 大型文档处理需要较长时间
3. **并行处理**: `max_workers` 根据系统资源调整
4. **存储空间**: 确保有足够的磁盘空间存储解析结果

## 故障排查

### 问题 1: 找不到 API Key

```
ValueError: 未找到 API Key
```

**解决方案**: 设置环境变量 `CLOUD_API_KEY` 或 `OPENAI_API_KEY`

### 问题 2: 文档处理失败

```
Error processing document
```

**解决方案**: 
- 检查文档路径是否正确
- 确保安装了 MinerU 依赖
- 尝试使用不同的 `parse_method`

### 问题 3: 查询无结果

**解决方案**:
- 确保文档已经处理完成
- 检查 `rag_storage` 目录是否有数据
- 尝试使用不同的查询模式

## 联系方式

如有问题，请参考：
- RAG-Anything 官方文档: `/home/honglianglu/ssd/casco/RAG-Anything/README_zh.md`
- LightRAG 文档: https://github.com/HKUDS/LightRAG

