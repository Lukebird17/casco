# 🚀 快速启动指南

## 三步开始使用

### 第一步：安装依赖

**推荐方式：使用 uv 创建虚拟环境（更快更好）**

```bash
# 使用 uv 创建虚拟环境并安装依赖（推荐）
./install_with_uv.sh

# 激活虚拟环境
source .venv/bin/activate
```

**或者：直接安装到系统环境**

```bash
# 使用 uv 直接安装（不创建虚拟环境）
./install_dependencies.sh
```

> 💡 **uv 是什么？** uv 是一个极快的 Python 包管理器，比 pip 快 10-100 倍！RAG-Anything 官方使用 uv。

### 第二步：配置环境

```bash
# 1. 复制配置文件
cp env_example.sh env.sh

# 2. 编辑配置文件，填入您的 API Key
nano env.sh  # 或使用任何编辑器

# 3. 加载环境变量
source env.sh
```

**需要填写的配置：**
- `CLOUD_API_KEY`: 您的 LLM API Key
- `OPENAI_API_KEY`: 您的 Embedding API Key

### 第三步：运行程序

```bash
# 方式 1: 一键启动（最简单）
./run.sh

# 方式 2: 快速启动脚本
python quick_start.py

# 方式 3: 直接运行主程序
python rag_qa_agent.py
```

---

## 📦 创建的文件说明

### 🎯 核心程序（必看）

| 文件 | 用途 | 何时使用 |
|------|------|---------|
| `run.sh` | 🚀 一键启动脚本 | **首次使用推荐** |
| `quick_start.py` | 交互式菜单程序 | 日常使用 |
| `rag_qa_agent.py` | 主程序（完整流程） | 批量处理+查询 |
| `simple_qa_example.py` | 使用示例 | 学习如何编程使用 |

### ⚙️ 配置文件

| 文件 | 用途 | 必需？ |
|------|------|-------|
| `env_example.sh` | 环境变量模板 | ✅ 需要复制并填写 |
| `config_template.py` | Python 配置模板 | ❌ 可选 |
| `requirements_rag.txt` | 依赖列表 | ℹ️ 自动使用 |

### 🛠️ 工具脚本

| 文件 | 用途 |
|------|------|
| `install_dependencies.sh` | 一键安装所有依赖 |
| `check_environment.py` | 检查环境配置是否正确 |

### 📖 文档文件

| 文件 | 内容 | 推荐阅读 |
|------|------|---------|
| `README.md` | 项目入口文档 | ⭐⭐⭐ |
| `使用说明.md` | **完整使用指南** | ⭐⭐⭐⭐⭐ |
| `README_RAG_QA.md` | 详细 API 文档 | ⭐⭐⭐⭐ |
| `PROJECT_SUMMARY.md` | 项目总结 | ⭐⭐⭐ |
| `QUICKSTART.md` | 本文档 | ⭐⭐⭐⭐⭐ |

---

## 🎮 使用场景

### 场景 1：首次使用（推荐使用 uv）

```bash
# 1. 使用 uv 创建虚拟环境并安装依赖
./install_with_uv.sh

# 2. 激活虚拟环境
source .venv/bin/activate

# 3. 配置环境变量
cp env_example.sh env.sh
nano env.sh  # 填写 API Key
source env.sh

# 4. 一键启动
./run.sh
```

**或者不使用虚拟环境：**

```bash
# 1. 检查环境
python check_environment.py

# 2. 直接安装依赖
./install_dependencies.sh

# 3. 配置环境变量
cp env_example.sh env.sh
nano env.sh  # 填写 API Key
source env.sh

# 4. 一键启动
./run.sh
```

### 场景 2：处理单个文档

```bash
python quick_start.py
# 选择: 1 (处理单个文档)
```

### 场景 3：批量处理所有事故报告

```bash
python quick_start.py
# 选择: 2 (批量处理事故报告)
```

### 场景 4：交互式问答

```bash
python quick_start.py
# 选择: 5 (交互式问答)
# 然后输入您的问题
```

### 场景 5：编程使用

```python
# 创建 my_script.py
import asyncio
from rag_qa_agent import RAGQAAgent

async def main():
    agent = RAGQAAgent()
    
    # 处理文档
    await agent.process_document("path/to/file.pdf")
    
    # 查询
    result = await agent.query("问题?", mode="hybrid")
    print(result['answer'])

asyncio.run(main())
```

---

## 💡 常用命令速查

### 环境相关

```bash
# 检查环境
python check_environment.py

# 加载环境变量
source env.sh

# 查看环境变量
echo $CLOUD_API_KEY
echo $OPENAI_API_KEY
```

### 运行程序

```bash
# 一键启动（推荐）
./run.sh

# 交互式菜单
python quick_start.py

# 直接运行
python rag_qa_agent.py

# 运行示例
python simple_qa_example.py
```

### 查看文档

```bash
# 查看入口文档
cat README.md

# 查看完整指南
less 使用说明.md  # 按 q 退出

# 在浏览器中查看（如果有图形界面）
xdg-open README.md
```

---

## 🎯 推荐工作流

### 新手推荐流程

1. **第一次运行**: `./run.sh` → 选择 `1` (环境检查)
2. **处理测试文档**: `./run.sh` → 选择 `2` → 选择 `1` (单个文档)
3. **测试查询**: `./run.sh` → 选择 `2` → 选择 `4` (仅查询)
4. **熟悉后**: 直接使用 `python quick_start.py`

### 高级用户流程

1. **批量处理**: 修改 `rag_qa_agent.py` 中的参数
2. **自定义查询**: 编写自己的 Python 脚本
3. **集成到项目**: 导入 `RAGQAAgent` 类使用

---

## ⚙️ 配置说明

### 最小配置（必需）

```bash
# env.sh 文件
export CLOUD_API_KEY="your_llm_api_key"
export OPENAI_API_KEY="your_embedding_api_key"
export CLOUD_BASE_URL="https://api.deepseek.com/v1"
export OPENAI_BASE_URL="https://api.openai.com/v1"
```

### 完整配置（可选）

```bash
# LLM 配置
export CLOUD_MODEL="deepseek-chat"
export CLOUD_API_KEY="your_api_key"
export CLOUD_BASE_URL="https://api.deepseek.com/v1"

# Embedding 配置
export OPENAI_API_KEY="your_api_key"
export OPENAI_BASE_URL="https://api.openai.com/v1"
export OPENAI_API_MODEL="text-embedding-3-large"

# RAG 配置（可选）
export WORKING_DIR="./rag_storage"
export PARSER="mineru"
export PARSE_METHOD="auto"
```

---

## 📊 输出文件

运行程序后会生成以下文件和目录：

```
/home/honglianglu/ssd/casco/
├── rag_storage/           # RAG 知识库（自动创建）
│   ├── kv_store_*.json
│   ├── vdb_entities_*.json
│   └── graph_*.json
│
├── output/                # 文档解析结果（自动创建）
│   └── *.md
│
└── qa_results.json        # 查询结果（自动生成）
```

---

## ❓ 遇到问题？

### 问题 1: 环境变量未设置

```bash
# 症状：ValueError: 未找到 API Key
# 解决：
source env.sh
```

### 问题 2: 依赖未安装

```bash
# 症状：ImportError: No module named 'raganything'
# 解决：
./install_dependencies.sh
```

### 问题 3: 查询无结果

```bash
# 症状：查询返回空或不相关
# 解决：
# 1. 确认文档已处理：ls -la rag_storage/
# 2. 尝试不同查询模式：mode="global"
```

### 更多问题

查看详细文档：`使用说明.md`

---

## 📚 进一步学习

### 阅读顺序推荐

1. ✅ `QUICKSTART.md` (本文档) - 快速开始
2. 📖 `README.md` - 项目概览
3. 📘 `使用说明.md` - 完整指南
4. 📕 `README_RAG_QA.md` - API 详解
5. 📗 `PROJECT_SUMMARY.md` - 项目总结

### 代码学习顺序

1. 阅读 `simple_qa_example.py` - 了解基本用法
2. 研究 `rag_qa_agent.py` - 理解核心实现
3. 参考 RAG-Anything 官方文档 - 深入学习

---

## 🎉 开始使用

```bash
# 立即开始！
./run.sh
```

**就是这么简单！** 🚀

---

## 📞 获取帮助

- 📖 完整文档：`使用说明.md`
- 🔧 API 文档：`README_RAG_QA.md`
- 📊 项目总结：`PROJECT_SUMMARY.md`
- 🌐 官方文档：`RAG-Anything/README_zh.md`

---

**祝您使用愉快！** ✨

