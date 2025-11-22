# BGE模型下载问题修复指南

## 问题描述

运行 `demo_enhanced.py` 时遇到以下错误：
```
403 Forbidden: Cannot access content at: https://hf-mirror.com/.../imgs%2F.DS_Store
```

这是因为：
1. 系统配置了 `HF_ENDPOINT=https://hf-mirror.com`
2. BGE模型仓库中包含 `.DS_Store` 文件（macOS系统文件）
3. hf-mirror 镜像站禁止访问某些系统文件

## 解决方案

### 方案1: 使用修复版启动脚本（推荐）

直接运行修复版的Python脚本：

```bash
python demo_enhanced_fixed.py
```

这个脚本会自动：
- 清除所有代理设置
- 清除或修正 HF_ENDPOINT
- 忽略 .DS_Store 等系统文件
- 然后运行原始的 demo_enhanced.py

### 方案2: 使用Shell脚本启动

```bash
./run_demo_fixed.sh
```

或者

```bash
bash run_demo_fixed.sh
```

### 方案3: 手动设置环境变量

在运行前执行以下命令：

```bash
# 清除环境变量
unset HF_ENDPOINT
unset http_proxy
unset https_proxy

# 运行程序
python demo_enhanced.py
```

### 方案4: 修改 ~/.bashrc 或 ~/.zshrc

如果需要永久修改，编辑你的shell配置文件：

```bash
nano ~/.bashrc  # 或 ~/.zshrc

# 注释掉或删除以下行
# export HF_ENDPOINT=https://hf-mirror.com

# 保存后重新加载
source ~/.bashrc
```

### 方案5: 手动下载模型到本地

如果网络问题持续，可以手动下载模型：

```bash
# 1. 创建模型目录
mkdir -p ~/models
cd ~/models

# 2. 安装 git-lfs
# Ubuntu/Debian:
sudo apt-get install git-lfs

# CentOS/RHEL:
sudo yum install git-lfs

# 3. 初始化 git-lfs
git lfs install

# 4. 克隆模型（只下载必要文件）
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/BAAI/bge-m3
cd bge-m3

# 5. 只拉取必要的文件
git lfs pull --include="*.safetensors,*.json,*.txt,*.model"

# 6. 修改代码使用本地模型
# 在 demo_enhanced.py 中：
# embedding = BGEEmbedding(model_path='/home/你的用户名/models/bge-m3')
```

### 方案6: 使用其他 Embedding 模型

如果BGE模型下载困难，可以使用在线API：

修改 `demo_enhanced.py` 的第 43 行：

```python
# 原来：
# embedding = BGEEmbedding()

# 改为（使用OpenAI Embedding）：
from Embeddings import OpenAIEmbedding
embedding = OpenAIEmbedding()
```

注意：需要在 `.env` 文件中配置 OpenAI API Key。

## 代码修改说明

`my_BGE_embedding.py` 已经更新，新增功能：

1. **自动清除代理设置**
2. **自动清除 HF_ENDPOINT**
3. **使用 ignore_patterns 跳过系统文件**
4. **支持断点续传**

关键代码：
```python
local_model_path = snapshot_download(
    repo_id=model_path,
    ignore_patterns=[
        "*.DS_Store",  # 忽略macOS系统文件
        "imgs/*",      # 忽略图片
        ...
    ],
    resume_download=True,
)
```

## 验证环境

检查当前环境配置：

```bash
echo "HF_ENDPOINT: $HF_ENDPOINT"
echo "http_proxy: $http_proxy"
echo "https_proxy: $https_proxy"
```

如果有输出，说明环境变量还在，需要清除。

## 常见问题

### Q1: 为什么清除 HF_ENDPOINT 后还是报错？

A: Python进程在启动时就读取了环境变量，需要在新的shell中运行或使用 `demo_enhanced_fixed.py`。

### Q2: 下载速度很慢怎么办？

A: 
1. 检查网络连接
2. 使用国内服务器
3. 使用本地已下载的模型
4. 改用在线API

### Q3: 如何查看模型缓存位置？

A: 默认在 `~/.cache/huggingface/hub/`

```bash
ls -lh ~/.cache/huggingface/hub/
```

### Q4: 如何清除缓存重新下载？

A: 
```bash
rm -rf ~/.cache/huggingface/hub/models--BAAI--bge-m3
```

## 联系支持

如果问题仍然存在，请提供：
1. 完整的错误日志
2. 环境变量输出（`env | grep -E 'HF|proxy'`）
3. Python版本（`python --version`）
4. 网络环境信息

