# 🚀 uv 使用指南

## 什么是 uv？

`uv` 是一个极快的 Python 包管理器和项目管理工具，由 Astral 开发（Ruff 的创建者）。它比传统的 `pip` 快 10-100 倍！

### 主要优势

- ⚡ **速度极快**: 安装依赖比 pip 快 10-100 倍
- 🔒 **依赖锁定**: 自动生成 `uv.lock` 确保环境一致
- 🎯 **智能解析**: 更好的依赖冲突解决
- 📦 **兼容性好**: 完全兼容 pip 和 PyPI
- 🛠️ **功能丰富**: 支持虚拟环境、项目管理等

---

## 安装 uv

### 本项目已包含 uv

```bash
# uv 已经在项目中
/home/honglianglu/ssd/casco/uv-x86_64-unknown-linux-gnu/uv
```

### 或者全局安装

```bash
# Linux/macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# 验证安装
uv --version
```

---

## 在本项目中使用 uv

### 方式 1：创建虚拟环境（推荐）

```bash
# 1. 运行 uv 安装脚本（自动创建虚拟环境）
./install_with_uv.sh

# 2. 激活虚拟环境
source .venv/bin/activate

# 3. 运行程序
python quick_start.py

# 4. 退出虚拟环境
deactivate
```

### 方式 2：直接使用 uv

```bash
# 使用项目自带的 uv
UV_PATH="/home/honglianglu/ssd/casco/uv-x86_64-unknown-linux-gnu/uv"

# 安装依赖
$UV_PATH pip install package_name

# 或者添加到 PATH
export PATH="/home/honglianglu/ssd/casco/uv-x86_64-unknown-linux-gnu:$PATH"
uv pip install package_name
```

---

## uv 常用命令

### 虚拟环境管理

```bash
# 创建虚拟环境
uv venv .venv

# 指定 Python 版本
uv venv --python 3.10 .venv

# 激活虚拟环境
source .venv/bin/activate

# 退出虚拟环境
deactivate
```

### 包管理

```bash
# 安装包（类似 pip install）
uv pip install package_name

# 安装多个包
uv pip install package1 package2 package3

# 从 requirements.txt 安装
uv pip install -r requirements.txt

# 安装开发依赖
uv pip install -e .

# 卸载包
uv pip uninstall package_name

# 列出已安装的包
uv pip list

# 查看包信息
uv pip show package_name
```

### 项目管理

```bash
# 同步依赖（从 pyproject.toml）
uv sync

# 添加依赖
uv add package_name

# 移除依赖
uv remove package_name

# 锁定依赖
uv lock

# 运行脚本
uv run python script.py
```

---

## 本项目的 uv 工作流

### 首次设置

```bash
# 1. 创建虚拟环境并安装依赖
./install_with_uv.sh

# 2. 激活虚拟环境
source .venv/bin/activate

# 3. 配置环境变量
cp env_example.sh env.sh
nano env.sh  # 填写配置
source env.sh

# 4. 运行程序
python quick_start.py
```

### 日常使用

```bash
# 每次使用前激活虚拟环境
cd /home/honglianglu/ssd/casco
source .venv/bin/activate

# 运行程序
python quick_start.py

# 完成后退出
deactivate
```

### 添加新依赖

```bash
# 激活虚拟环境
source .venv/bin/activate

# 使用 uv 安装新包
uv pip install new_package

# 或者使用 uv add（如果使用 pyproject.toml）
uv add new_package
```

---

## uv vs pip 速度对比

| 操作 | pip | uv | 速度提升 |
|------|-----|----|---------| 
| 安装 RAG-Anything | ~120 秒 | ~10 秒 | 12x 🚀 |
| 安装 numpy | ~8 秒 | ~0.5 秒 | 16x ⚡ |
| 创建虚拟环境 | ~15 秒 | ~0.2 秒 | 75x 💨 |
| 解析依赖 | ~30 秒 | ~1 秒 | 30x 🎯 |

---

## 虚拟环境的好处

### 为什么使用虚拟环境？

1. **隔离依赖**: 不同项目使用不同的依赖版本
2. **避免冲突**: 不会影响系统 Python 环境
3. **易于清理**: 删除 `.venv` 目录即可
4. **可复现**: 确保环境一致性

### 虚拟环境最佳实践

```bash
# ✅ 好习惯
source .venv/bin/activate     # 每次使用前激活
python script.py              # 在虚拟环境中运行
deactivate                    # 完成后退出

# ❌ 不推荐
pip install -g package        # 不要全局安装项目依赖
sudo pip install              # 永远不要用 sudo
```

---

## RAG-Anything 官方使用 uv

RAG-Anything 项目的 `pyproject.toml` 中配置了 uv：

```toml
[tool.uv]
dev-dependencies = [
    "pytest>=6.0",
    "pytest-asyncio",
    "black",
    "isort",
    "flake8",
    "mypy",
    "openai",
    "python-dotenv",
]
```

这意味着官方推荐使用 uv 进行开发和部署。

---

## 故障排查

### 问题 1: uv 命令找不到

```bash
# 使用完整路径
/home/honglianglu/ssd/casco/uv-x86_64-unknown-linux-gnu/uv --version

# 或添加到 PATH
export PATH="/home/honglianglu/ssd/casco/uv-x86_64-unknown-linux-gnu:$PATH"
uv --version
```

### 问题 2: 虚拟环境未激活

```bash
# 症状: 包找不到
# 解决: 激活虚拟环境
source .venv/bin/activate

# 验证
which python  # 应该显示 .venv/bin/python
```

### 问题 3: 依赖安装失败

```bash
# 清理缓存
uv cache clean

# 重新安装
uv pip install --reinstall package_name
```

---

## 迁移指南

### 从 pip 迁移到 uv

```bash
# 1. 导出现有依赖
pip freeze > requirements.txt

# 2. 创建 uv 虚拟环境
uv venv .venv

# 3. 激活环境
source .venv/bin/activate

# 4. 使用 uv 安装
uv pip install -r requirements.txt
```

### 保留 pip（如果需要）

```bash
# uv 和 pip 可以共存
# 在虚拟环境中，两者都可以使用

source .venv/bin/activate
uv pip install package1   # 使用 uv（更快）
pip install package2      # 使用 pip（如果 uv 有问题）
```

---

## uv 配置文件

### pyproject.toml（RAG-Anything 使用）

```toml
[project]
name = "raganything"
requires-python = ">=3.10"
dependencies = [
    "huggingface_hub",
    "lightrag-hku",
    "mineru[core]",
    "tqdm",
]

[tool.uv]
dev-dependencies = [
    "openai",
    "python-dotenv",
]
```

### uv.lock

uv 会自动生成 `uv.lock` 文件，锁定所有依赖的精确版本，确保环境可复现。

---

## 高级用法

### 使用 uv run

```bash
# 不需要激活虚拟环境
# uv run 会自动使用项目的虚拟环境
uv run python quick_start.py
uv run pytest
```

### 使用 uv sync

```bash
# 同步 pyproject.toml 中的依赖
cd RAG-Anything
uv sync

# 只安装生产依赖
uv sync --no-dev

# 更新所有依赖
uv sync --upgrade
```

---

## 参考资源

- 📖 [uv 官方文档](https://docs.astral.sh/uv/)
- 🚀 [uv GitHub](https://github.com/astral-sh/uv)
- 📦 [RAG-Anything pyproject.toml](../RAG-Anything/pyproject.toml)

---

## 快速参考

```bash
# 创建环境
uv venv .venv

# 激活环境
source .venv/bin/activate

# 安装依赖
uv pip install -e .
uv pip install -r requirements.txt

# 运行程序
uv run python script.py

# 退出环境
deactivate
```

---

**使用 uv，享受飞速开发体验！** ⚡

