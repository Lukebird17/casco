# 安装指南

## 推荐方式：使用 Conda 环境

### 为什么用 Conda？

- ✅ **简单易用**：一键创建隔离环境
- ✅ **依赖管理**：自动处理 Python 和系统依赖
- ✅ **广泛使用**：科学计算领域标准工具
- ✅ **兼容 uv**：可在 conda 环境中使用 uv 加速安装

### 快速安装（3步）

```bash
# 1. 运行安装脚本
./install_conda.sh

# 2. 激活环境
conda activate casco_rag

# 3. 配置 API
cp env_example.sh env.sh
nano env.sh  # 填入 API Key
source env.sh
```

### 详细步骤

#### 1. 确保安装了 Conda

如果没有安装，下载 Miniconda：

```bash
# Linux
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh

# 或使用已有的 Anaconda/Miniconda
```

验证安装：

```bash
conda --version
# 输出: conda 23.x.x
```

#### 2. 运行安装脚本

```bash
cd /home/honglianglu/ssd/casco/casco_rag_agent
chmod +x install_conda.sh
./install_conda.sh
```

安装脚本会：
1. 创建名为 `casco_rag` 的 conda 环境（Python 3.10）
2. 在环境中安装 uv 包管理器
3. 使用 uv 安装 RAG-Anything（官方推荐方式）
4. 安装其他依赖（langchain、openai 等）
5. 验证所有包安装成功

#### 3. 激活环境

```bash
conda activate casco_rag
```

你会看到命令行提示符变为：
```
(casco_rag) user@hostname:~$
```

#### 4. 配置环境变量

```bash
cp env_example.sh env.sh
nano env.sh  # 或使用 vim/code 编辑
```

填入你的 API Key：

```bash
# LLM API
export CLOUD_MODEL="deepseek-chat"
export CLOUD_API_KEY="sk-your-actual-api-key"
export CLOUD_BASE_URL="https://api.deepseek.com/v1"

# Embedding API
export OPENAI_API_KEY="sk-your-actual-api-key"
export OPENAI_BASE_URL="https://api.openai.com/v1"
export OPENAI_API_MODEL="text-embedding-3-large"
```

加载环境变量：

```bash
source env.sh
```

#### 5. 运行程序

```bash
# 方式 1: 交互式启动
python quick_start.py

# 方式 2: 一键启动脚本
./run.sh

# 方式 3: 直接运行主程序
python rag_qa_agent.py
```

---

## 日常使用

### 每次使用前

```bash
cd /home/honglianglu/ssd/casco/casco_rag_agent
conda activate casco_rag
source env.sh  # 如果需要
python quick_start.py
```

### 使用完毕后

```bash
conda deactivate
```

---

## 环境管理

### 查看环境

```bash
# 查看所有 conda 环境
conda env list

# 查看当前环境安装的包
conda list
pip list
```

### 更新依赖

```bash
conda activate casco_rag

# 更新单个包
pip install --upgrade package_name

# 使用 uv 更新（更快）
uv pip install --upgrade package_name
```

### 重新安装

```bash
# 删除环境
conda env remove -n casco_rag

# 重新运行安装脚本
./install_conda.sh
```

### 导出环境

```bash
# 导出环境配置
conda env export > environment_backup.yml

# 从备份恢复
conda env create -f environment_backup.yml
```

---

## 故障排查

### 问题 1: conda 命令找不到

```bash
# 初始化 conda
conda init bash
source ~/.bashrc

# 或手动激活
source ~/miniconda3/etc/profile.d/conda.sh
```

### 问题 2: 激活环境失败

```bash
# 确保环境已创建
conda env list

# 如果不存在，重新运行安装脚本
./install_conda.sh
```

### 问题 3: RAG-Anything 安装失败

```bash
conda activate casco_rag

# 手动安装
cd /home/honglianglu/ssd/casco/RAG-Anything

# 方式 1: 使用 uv（推荐）
uv pip install -r requirements.txt
uv pip install -e .

# 方式 2: 使用 pip
pip install -r requirements.txt
pip install -e .
```

### 问题 4: 缺少系统依赖

某些包可能需要系统级依赖：

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install build-essential python3-dev

# 对于 LibreOffice 支持（处理 Office 文档）
sudo apt-get install libreoffice
```

### 问题 5: 验证失败

```bash
conda activate casco_rag

# 逐个测试
python -c "import raganything; print('✓ raganything')"
python -c "import lightrag; print('✓ lightrag')"
python -c "import openai; print('✓ openai')"
python -c "import langchain; print('✓ langchain')"

# 如果某个失败，单独安装
pip install package_name
```

---

## 其他安装方式

### 方式 2: 使用 uv 虚拟环境（不用 conda）

```bash
./install_with_uv.sh
source .venv/bin/activate
```

优点：
- 更快的安装速度
- 更小的环境体积
- uv 原生管理

缺点：
- 需要单独安装 uv
- 不如 conda 通用

### 方式 3: 直接安装到系统（不推荐）

```bash
./install_dependencies.sh
```

缺点：
- 可能污染系统 Python 环境
- 依赖冲突风险高
- 难以清理

---

## Conda vs uv vs pip

| 特性 | Conda | uv | pip |
|------|-------|----|----|
| 速度 | 中等 | 最快 | 慢 |
| 环境隔离 | ✅ | ✅ | ❌ |
| 系统依赖 | ✅ | ❌ | ❌ |
| 易用性 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| 兼容性 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

**推荐组合**：Conda + uv
- 用 Conda 创建环境（隔离 + 系统依赖）
- 在环境中用 uv 安装包（速度快）

---

## 完整工作流示例

```bash
# === 首次安装 ===
cd /home/honglianglu/ssd/casco/casco_rag_agent
./install_conda.sh
conda activate casco_rag
cp env_example.sh env.sh
nano env.sh  # 填入 API Key
source env.sh

# === 测试运行 ===
python check_environment.py  # 检查环境
python quick_start.py        # 交互式使用

# === 处理文档 ===
# 在 quick_start.py 中选择：
# 1 - 处理单个文档
# 2 - 批量处理事故报告
# 3 - 批量处理所有文档

# === 查询 ===
# 在 quick_start.py 中选择：
# 4 - 仅查询
# 5 - 交互式问答

# === 使用完毕 ===
conda deactivate
```

---

## 环境配置检查清单

- [ ] Conda 已安装 (`conda --version`)
- [ ] 环境已创建 (`conda env list` 看到 `casco_rag`)
- [ ] 环境已激活 (命令行显示 `(casco_rag)`)
- [ ] uv 已安装 (`uv --version`)
- [ ] RAG-Anything 已安装 (`python -c "import raganything"`)
- [ ] API Key 已配置 (`echo $CLOUD_API_KEY`)
- [ ] 数据目录存在 (`ls /home/honglianglu/ssd/casco/data`)

全部✅后即可正常使用！

---

## 获取帮助

- 📖 [README.md](README.md) - 项目概览
- 🚀 [QUICKSTART.md](QUICKSTART.md) - 快速指南
- 📚 [使用说明.md](使用说明.md) - 完整文档
- ⚡ [UV_GUIDE.md](UV_GUIDE.md) - uv 使用指南

---

**推荐：使用 Conda 环境，简单可靠！** 🎉

