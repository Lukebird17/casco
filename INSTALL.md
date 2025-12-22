# 📦 RAG智能学习助手 - 安装指南

完整的安装和配置指南，适合初学者和高级用户。

---

## 📋 目录

1. [环境要求](#环境要求)
2. [快速安装](#快速安装)
3. [详细安装步骤](#详细安装步骤)
4. [配置说明](#配置说明)
5. [验证安装](#验证安装)
6. [故障排除](#故障排除)

---

## 环境要求

### 必需软件

| 软件 | 最低版本 | 推荐版本 | 说明 |
|------|---------|---------|------|
| Python | 3.10 | 3.10+ | 后端运行环境 |
| Node.js | 18.0 | 20.0+ | 前端构建工具 |
| npm | 9.0 | 10.0+ | 包管理器 |
| Git | 2.0 | 最新版 | 版本控制 |

### 系统要求

- **操作系统**: Linux / macOS / Windows 10+
- **内存**: 最低 4GB，推荐 8GB+
- **磁盘空间**: 至少 10GB 可用空间
- **网络**: 需要访问外网（用于API调用和下载依赖）

---

## 快速安装

适合有经验的用户：

```bash
# 1. 克隆项目
git clone <repository-url>
cd rag-agent

# 2. 配置环境
cp config.example.py config.py
# 编辑 config.py，填入API密钥

# 3. 后端安装
pip install -r requirements.txt

# 4. 前端安装
cd frontend && npm install && cd ..

# 5. 启动服务
bash start.sh
```

访问: http://localhost:5173

---

## 详细安装步骤

### 步骤 1: 安装 Python

#### Linux (Ubuntu/Debian)

```bash
# 更新包列表
sudo apt update

# 安装 Python 3.10+
sudo apt install python3.10 python3.10-venv python3-pip

# 验证安装
python3 --version  # 应显示 3.10.x 或更高
```

#### macOS

```bash
# 使用 Homebrew 安装
brew install python@3.10

# 验证安装
python3 --version
```

#### Windows

1. 访问 [Python官网](https://www.python.org/downloads/)
2. 下载 Python 3.10+ 安装包
3. 运行安装程序，**勾选 "Add Python to PATH"**
4. 打开命令提示符验证：`python --version`

### 步骤 2: 安装 Node.js

#### Linux (Ubuntu/Debian)

```bash
# 使用 NodeSource 仓库
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs

# 验证安装
node --version  # 应显示 v20.x.x 或更高
npm --version
```

#### macOS

```bash
# 使用 Homebrew 安装
brew install node

# 验证安装
node --version
npm --version
```

#### Windows

1. 访问 [Node.js官网](https://nodejs.org/)
2. 下载 LTS 版本安装包
3. 运行安装程序
4. 打开命令提示符验证：`node --version`

### 步骤 3: 获取项目代码

```bash
# 克隆项目（如果有Git仓库）
git clone <repository-url>
cd rag-agent

# 或者解压下载的ZIP文件
unzip rag-agent.zip
cd rag-agent
```

### 步骤 4: 配置环境变量

#### 创建配置文件

```bash
# 如果有示例配置文件
cp config.example.py config.py

# 或者创建新文件
nano config.py  # Linux/macOS
notepad config.py  # Windows
```

#### 配置内容示例

```python
# ========================================
# OpenAI API 配置
# ========================================

# API密钥（必需）
OPENAI_API_KEY = "sk-your-api-key-here"

# API地址（可选，默认使用OpenAI官方）
OPENAI_API_BASE = "https://api.siliconflow.cn/v1"
# 其他可选：
# - OpenAI官方: https://api.openai.com/v1
# - Azure OpenAI: https://your-resource.openai.azure.com
# - 本地部署: http://localhost:11434/v1

# ========================================
# 模型配置
# ========================================

# 文本模型（用于纯文本问答）
TEXT_MODEL_NAME = "deepseek-ai/DeepSeek-V3"
# 其他选项: "gpt-4", "gpt-3.5-turbo", "qwen-plus"

# 多模态模型（用于图片理解）
MULTIMODAL_MODEL_NAME = "Pro/Qwen/Qwen2-VL-72B-Instruct"
# 其他选项: "gpt-4-vision-preview"

# 默认模型（向后兼容）
MODEL_NAME = TEXT_MODEL_NAME

# ========================================
# 向量数据库配置
# ========================================

# 数据库存储路径
CHROMA_PERSIST_DIR = "./vector_db"

# 默认集合名称
COLLECTION_NAME = "default"

# ========================================
# 数据目录配置
# ========================================

# 原始文档存储路径
DATA_DIR = "./data"

# ========================================
# 检索配置
# ========================================

# 检索文档数量（推荐3-10）
TOP_K = 5

# 文本分块大小（推荐300-800）
CHUNK_SIZE = 500

# 分块重叠大小（推荐CHUNK_SIZE的10%）
CHUNK_OVERLAP = 50

# ========================================
# 模型参数
# ========================================

# 默认温度（0.0-1.0，越高越随机）
DEFAULT_TEMPERATURE = 0.7

# 最大输出Token数
MAX_TOKENS = 2000
```

### 步骤 5: 安装后端依赖

#### 创建虚拟环境（推荐）

```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

#### 安装依赖包

```bash
# 升级 pip
pip install --upgrade pip

# 安装所有依赖
pip install -r requirements.txt

# 如果遇到网络问题，使用国内镜像
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

#### 常见依赖说明

- `fastapi`: Web框架
- `uvicorn`: ASGI服务器
- `chromadb`: 向量数据库
- `sentence-transformers`: 文本嵌入模型
- `openai`: OpenAI API客户端
- `jieba`: 中文分词
- `rank-bm25`: BM25检索算法

### 步骤 6: 安装前端依赖

```bash
cd frontend

# 安装依赖
npm install

# 如果遇到网络问题，使用国内镜像
npm install --registry=https://registry.npmmirror.com

# 返回项目根目录
cd ..
```

### 步骤 7: 准备数据

#### 创建数据目录

```bash
mkdir -p data/NLP
```

#### 上传文档

将你的课程文档（PDF、Word、PPT等）放入 `data/NLP/` 目录：

```bash
# 示例
cp /path/to/your/documents/*.pdf data/NLP/
```

### 步骤 8: 启动服务

#### 方式一：使用启动脚本（推荐）

```bash
# 一键启动后端和前端
bash start.sh
```

#### 方式二：手动启动

**终端1 - 启动后端：**

```bash
cd backend
python api.py

# 或使用 uvicorn（带自动重载）
uvicorn api:app --reload --host 0.0.0.0 --port 8000
```

**终端2 - 启动前端：**

```bash
cd frontend
npm run dev
```

### 步骤 9: 验证安装

1. **检查后端**：访问 http://localhost:8000/docs
   - 应该看到 FastAPI 的 API 文档页面

2. **检查前端**：访问 http://localhost:5173
   - 应该看到应用的主界面

3. **测试功能**：
   - 尝试输入一个问题
   - 检查是否能正常返回答案
   - 上传一个文档测试

---

## 配置说明

### API密钥获取

#### OpenAI

1. 访问 https://platform.openai.com/
2. 注册/登录账号
3. 导航到 API Keys 页面
4. 创建新的 API Key
5. 复制并粘贴到 `config.py`

#### SiliconFlow（国内推荐）

1. 访问 https://siliconflow.cn/
2. 注册账号
3. 充值（新用户有免费额度）
4. 创建 API Key
5. 配置到 `config.py`

```python
OPENAI_API_BASE = "https://api.siliconflow.cn/v1"
OPENAI_API_KEY = "sk-your-siliconflow-key"
```

### 知识库配置

系统支持多知识库，每个知识库对应一个主题：

```python
# 在 config.py 中配置
KNOWLEDGE_BASES = {
    "default": {
        "name": "默认知识库",
        "data_dir": "./data/default",
        "vector_db": "./vector_db/default"
    },
    "NLP": {
        "name": "自然语言处理",
        "data_dir": "./data/NLP",
        "vector_db": "./vector_db/NLP"
    }
}
```

### 性能调优

#### 内存不足

如果遇到内存问题，可以调整以下参数：

```python
# 减少批处理大小
BATCH_SIZE = 10  # 默认32

# 减少检索数量
TOP_K = 3  # 默认5

# 减少文本块大小
CHUNK_SIZE = 300  # 默认500
```

#### 响应速度优化

```python
# 禁用质量评估（可提升30%速度）
ENABLE_QUALITY_EVAL = False

# 减少重排序数量
RERANK_TOP_K = 3  # 默认5
```

---

## 验证安装

### 自动验证脚本

运行快速测试：

```bash
python tests/quick_test.py
```

应该看到：

```
✅ 配置文件加载成功
✅ 向量数据库连接成功
✅ API服务正常
✅ 所有检查通过！
```

### 手动验证

#### 1. 检查Python依赖

```bash
python -c "import fastapi, chromadb, openai; print('✅ 核心依赖已安装')"
```

#### 2. 检查向量数据库

```bash
python -c "from src.core.vector_store import VectorStore; vs = VectorStore(); print(f'✅ 向量库初始化成功，共{vs.collection.count()}条数据')"
```

#### 3. 检查前端

```bash
cd frontend
npm run build
echo "✅ 前端构建成功"
```

---

## 故障排除

### 问题 1: Python版本不兼容

**错误信息**：
```
ERROR: Package requires Python 3.10 or later
```

**解决方案**：
```bash
# 检查Python版本
python --version

# 如果版本过低，安装新版本
# Linux
sudo apt install python3.10

# macOS
brew install python@3.10

# Windows: 从官网下载安装
```

### 问题 2: pip install失败

**错误信息**：
```
ERROR: Could not find a version that satisfies the requirement
```

**解决方案**：
```bash
# 升级pip
pip install --upgrade pip

# 使用国内镜像
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 单独安装问题包
pip install <package-name> --no-cache-dir
```

### 问题 3: ChromaDB初始化失败

**错误信息**：
```
chromadb.errors.InvalidDimensionException
```

**解决方案**：
```bash
# 删除旧的向量数据库
rm -rf vector_db/

# 重新启动，系统会自动创建
python backend/api.py
```

### 问题 4: npm install失败

**错误信息**：
```
npm ERR! code ECONNRESET
```

**解决方案**：
```bash
# 清除npm缓存
npm cache clean --force

# 使用国内镜像
npm install --registry=https://registry.npmmirror.com

# 或配置淘宝镜像
npm config set registry https://registry.npmmirror.com
```

### 问题 5: 端口被占用

**错误信息**：
```
Error: Port 8000 is already in use
```

**解决方案**：
```bash
# Linux/macOS - 查找占用端口的进程
lsof -i :8000
kill -9 <PID>

# Windows - 查找并结束进程
netstat -ano | findstr :8000
taskkill /F /PID <PID>

# 或者修改端口
uvicorn api:app --port 8001
```

### 问题 6: API调用失败

**错误信息**：
```
openai.error.AuthenticationError: Invalid API key
```

**解决方案**：
1. 检查 `config.py` 中的 API 密钥是否正确
2. 确认API密钥有足够的额度
3. 检查API地址是否正确
4. 尝试使用curl测试：

```bash
curl https://api.siliconflow.cn/v1/models \
  -H "Authorization: Bearer your-api-key"
```

### 问题 7: 前端页面空白

**解决方案**：
1. 检查浏览器控制台的错误信息
2. 确认后端正在运行
3. 清除浏览器缓存（Ctrl+Shift+R）
4. 检查前端配置：

```javascript
// frontend/src/api/client.js
const API_BASE_URL = 'http://localhost:8000';  // 确认地址正确
```

---

## 高级配置

### Docker部署（可选）

```bash
# 构建镜像
docker build -t rag-agent .

# 运行容器
docker run -d -p 8000:8000 -p 5173:5173 \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/vector_db:/app/vector_db \
  rag-agent
```

### 使用本地模型（Ollama）

```python
# config.py
OPENAI_API_BASE = "http://localhost:11434/v1"
OPENAI_API_KEY = "ollama"  # 任意字符串
TEXT_MODEL_NAME = "qwen2:7b"
```

```bash
# 安装并启动Ollama
ollama serve

# 下载模型
ollama pull qwen2:7b
```

### 生产环境部署

#### 使用Gunicorn

```bash
pip install gunicorn

# 启动后端
cd backend
gunicorn api:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

#### 使用Nginx反向代理

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:5173;
    }

    location /api {
        proxy_pass http://localhost:8000;
    }
}
```

---

## 下一步

安装完成后，你可以：

1. 📚 阅读 [README.md](README.md) 了解更多功能
2. 🎓 查看使用示例
3. 💬 加入社区讨论
4. 🐛 报告问题或建议

---

## 获取帮助

- **文档**: 查看项目README和Wiki
- **Issue**: 提交GitHub Issue
- **讨论**: 参与GitHub Discussions

---

<div align="center">

**祝你使用愉快！🎉**

[⬆ 回到顶部](#-rag智能学习助手---安装指南)

</div>



