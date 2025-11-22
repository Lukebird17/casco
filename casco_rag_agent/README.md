# CASCO RAG 问答智能体

> 基于 RAG-Anything 官方框架的智能文档问答系统

## 🚀 快速开始（三步）

```bash
# 1. 使用 uv 创建虚拟环境并安装依赖（推荐）
./install_with_uv.sh

# 2. 激活虚拟环境
source .venv/bin/activate

# 3. 配置环境变量
cp env_example.sh env.sh
nano env.sh  # 填入您的 API Key
source env.sh

# 4. 运行程序
python quick_start.py
```

## ✨ 主要特性

- ✅ 严格遵循 RAG-Anything 官方实现
- ✅ 支持多模态内容（图像、表格、公式）
- ✅ 批量处理 PDF 文档
- ✅ 4 种查询模式（hybrid/local/global/naive）
- ✅ 符合示例模板输出格式
- ✅ 使用 uv 包管理器（比 pip 快 10-100 倍）
- ✅ 独立打包，路径自动适配

## 📁 文件结构

```
casco_rag_agent/
├── config.py                  # ⚙️ 统一配置文件（路径、API等）
├── rag_qa_agent.py           # ⭐ 主程序
├── quick_start.py            # 🚀 快速启动脚本
├── simple_qa_example.py      # 📝 使用示例
├── check_environment.py      # 🔍 环境检查
│
├── env_example.sh            # 🔑 环境变量模板
├── install_with_uv.sh        # ⚡ uv 安装脚本（推荐）
├── install_dependencies.sh   # 📦 传统安装脚本
├── run.sh                    # 🎮 一键启动
├── requirements_rag.txt      # 📋 依赖列表
│
├── README.md                 # 📄 本文档
├── QUICKSTART.md             # 🚀 快速指南
├── 使用说明.md                # 📖 完整指南（推荐）
├── README_RAG_QA.md         # 📚 API 文档
├── PROJECT_SUMMARY.md       # 📊 项目总结
└── UV_GUIDE.md              # ⚡ uv 使用指南
```

## 💡 使用方式

### 方式 1: 交互式使用（推荐）

```bash
# 激活环境
source .venv/bin/activate

# 运行交互式菜单
python quick_start.py
# 或
./run.sh
```

### 方式 2: 直接运行主程序

```bash
source .venv/bin/activate
python rag_qa_agent.py
```

### 方式 3: 编程使用

```python
import asyncio
import sys
from pathlib import Path

# 添加 agent 目录到路径
sys.path.insert(0, str(Path(__file__).parent))

from rag_qa_agent import RAGQAAgent
from config import DATA_DIR

async def main():
    # 初始化
    agent = RAGQAAgent()
    
    # 处理文档
    await agent.process_document(str(DATA_DIR / "事故报告/某文件.pdf"))
    
    # 查询
    result = await agent.query("问题?", mode="hybrid")
    print(result['answer'])

asyncio.run(main())
```

## 🔧 配置说明

### 1. 环境变量配置（必需）

编辑 `env.sh` 文件：

```bash
# LLM 配置
export CLOUD_MODEL="deepseek-chat"
export CLOUD_API_KEY="your_api_key"
export CLOUD_BASE_URL="https://api.deepseek.com/v1"

# Embedding 配置
export OPENAI_API_KEY="your_api_key"
export OPENAI_BASE_URL="https://api.openai.com/v1"
export OPENAI_API_MODEL="text-embedding-3-large"
```

### 2. 路径配置（自动）

所有路径在 `config.py` 中统一管理，自动适配项目结构：

- **数据目录**: `../data/`
- **RAG-Anything**: `../RAG-Anything/`
- **模板文件**: `../ocr_demo_project/示例模板.json`
- **工作目录**: `./rag_storage/`（agent 内部）
- **输出目录**: `./output/`（agent 内部）

## 📊 输出格式

查询结果符合示例模板格式，保存在 `qa_results.json`：

```json
{
  "items": [
    {
      "question": "提问内容",
      "retrieved_contexts": ["上下文1", "上下文2"],
      "answer": "生成的回答"
    }
  ]
}
```

## 🎯 核心功能

| 功能 | 说明 |
|------|------|
| **文档处理** | 支持 PDF、Office、图像等多种格式 |
| **多模态** | 自动识别和处理图像、表格、公式 |
| **批量处理** | 递归处理整个目录树 |
| **查询模式** | hybrid/local/global/naive 可选 |
| **输出格式** | 符合示例模板规范 |
| **路径自适应** | 自动适配项目结构 |

## 📚 详细文档

- **快速开始**: [QUICKSTART.md](QUICKSTART.md) ⭐ 5分钟上手
- **完整指南**: [使用说明.md](使用说明.md) ⭐⭐⭐⭐⭐ 推荐阅读
- **API 文档**: [README_RAG_QA.md](README_RAG_QA.md)
- **uv 指南**: [UV_GUIDE.md](UV_GUIDE.md) ⚡ uv 使用说明
- **项目总结**: [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)

## 🔍 查询模式

| 模式 | 速度 | 准确性 | 适用场景 |
|------|------|--------|---------|
| `hybrid` | 中等 | 最高 | 一般用途（推荐） |
| `local` | 快 | 较高 | 局部细节 |
| `global` | 慢 | 高 | 全局概览 |
| `naive` | 最快 | 中等 | 快速查找 |

## ⚡ 为什么使用 uv？

- **速度快**: 比 pip 快 10-100 倍
- **官方推荐**: RAG-Anything 官方使用
- **依赖管理**: 更好的依赖解析和锁定
- **虚拟环境**: 轻松创建和管理

详见：[UV_GUIDE.md](UV_GUIDE.md)

## 🛠️ 技术栈

- **RAG-Anything**: 多模态文档处理
- **LightRAG**: 知识图谱 RAG
- **MinerU**: 文档解析
- **uv**: 包管理器
- **OpenAI API**: LLM 和 Embedding

## ❓ 常见问题

### Q: 如何修改数据目录？

A: 编辑 `config.py` 中的 `DATA_DIR`

### Q: 如何使用不同的 LLM？

A: 修改 `env.sh` 中的 `CLOUD_MODEL` 和 `CLOUD_BASE_URL`

### Q: 虚拟环境在哪里？

A: `.venv/` 目录（使用 `install_with_uv.sh` 自动创建）

### Q: 如何添加新依赖？

```bash
source .venv/bin/activate
uv pip install new_package
```

详见：[使用说明.md](使用说明.md)

## 📦 项目结构

```
/home/honglianglu/ssd/casco/
├── casco_rag_agent/          # 👈 本 Agent 系统
│   ├── config.py             # 统一配置
│   ├── rag_qa_agent.py       # 主程序
│   ├── .venv/                # 虚拟环境
│   ├── rag_storage/          # RAG 知识库
│   ├── output/               # 解析输出
│   └── qa_results.json       # 查询结果
│
├── data/                     # 输入数据
│   ├── 事故报告/
│   ├── 技术报告/
│   ├── 标准规范/
│   └── 行业报告/
│
├── RAG-Anything/             # RAG 框架
└── ocr_demo_project/         # OCR 项目
    └── 示例模板.json
```

## 🎉 开始使用

```bash
cd /home/honglianglu/ssd/casco/casco_rag_agent
./install_with_uv.sh && source .venv/bin/activate && ./run.sh
```

**就是这么简单！** 🚀

---

_查看 [使用说明.md](使用说明.md) 获取完整文档_
