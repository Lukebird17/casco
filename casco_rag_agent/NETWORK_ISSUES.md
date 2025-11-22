# 网络问题解决方案

## 问题描述

MinerU 在首次运行时需要从 HuggingFace 下载模型文件，如果网络不稳定会导致连接失败：

```
Connection reset by peer
Retrying in 8s [Retry 4/5]
```

## 解决方案

### 方案 1: 设置 HuggingFace 镜像（推荐）

在运行前设置环境变量使用国内镜像：

```bash
# 添加到 env.sh
export HF_ENDPOINT=https://hf-mirror.com
export HF_HUB_ENABLE_HF_TRANSFER=1

# 或临时设置
export HF_ENDPOINT=https://hf-mirror.com
python rag_qa_agent.py
```

### 方案 2: 使用代理

```bash
# HTTP 代理
export HTTP_PROXY=http://your-proxy:port
export HTTPS_PROXY=http://your-proxy:port

# SOCKS5 代理
export ALL_PROXY=socks5://your-proxy:port
```

### 方案 3: 预下载模型（最稳定）

手动下载 MinerU 需要的模型：

```bash
conda activate casco_rag

# 使用 huggingface-cli 下载
pip install huggingface-hub

# 下载模型（会自动重试）
huggingface-cli download opendatalab/PDF-Extract-Kit-1.0 \
    --local-dir ~/.cache/huggingface/hub/PDF-Extract-Kit-1.0 \
    --resume-download

# 或者使用 Python 脚本下载
python -c "
from huggingface_hub import snapshot_download
snapshot_download('opendatalab/PDF-Extract-Kit-1.0', resume_download=True)
"
```

### 方案 4: 降低并发处理数

减少同时处理的文档数量，避免触发太多下载请求：

```python
# 在 rag_qa_agent.py 的 main() 函数中
await agent.process_folder(
    folder_path=data_dir,
    max_workers=1,  # 改为 1，一次只处理一个文件
    recursive=False  # 先不递归，只处理当前目录
)
```

### 方案 5: 使用 txt 模式（临时方案）

如果模型下载一直失败，可以先用纯文本模式测试：

```python
agent = RAGQAAgent(
    parse_method="txt"  # 使用纯文本模式，不需要模型
)
```

## 推荐步骤

1. **首先尝试方案 1**（设置镜像）：

```bash
cd /home/honglianglu/ssd/casco/casco_rag_agent

# 编辑 env.sh，添加：
echo 'export HF_ENDPOINT=https://hf-mirror.com' >> env.sh

# 重新加载
source env.sh

# 运行
python rag_qa_agent.py
```

2. **如果还是失败，使用方案 3**（预下载）：

```bash
conda activate casco_rag

# 安装下载工具
pip install -U huggingface-hub

# 手动下载（支持断点续传）
python << 'EOF'
from huggingface_hub import snapshot_download
import os

os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

print("开始下载 MinerU 模型...")
snapshot_download(
    'opendatalab/PDF-Extract-Kit-1.0',
    resume_download=True,
    max_workers=4
)
print("下载完成！")
EOF
```

3. **验证模型已下载**：

```bash
# 检查模型缓存
ls -lh ~/.cache/huggingface/hub/
```

4. **重新运行**：

```bash
python rag_qa_agent.py
```

## 修改后的配置

已更新 `env_example.sh`，包含 HuggingFace 镜像配置：

```bash
# HuggingFace 配置（解决网络问题）
export HF_ENDPOINT=https://hf-mirror.com
export HF_HUB_ENABLE_HF_TRANSFER=1
```

## 进度监控

现在程序已添加详细的进度显示：
- ✅ 文件扫描进度
- ✅ 文档处理进度
- ✅ 查询进度
- ✅ 详细的日志输出

## 常见错误

### 1. Connection reset by peer
**原因**: 网络不稳定  
**解决**: 使用镜像或代理

### 2. Read timed out
**原因**: 下载超时  
**解决**: 使用 `resume_download=True` 断点续传

### 3. 403 Forbidden
**原因**: HuggingFace 访问限制  
**解决**: 使用镜像或注册 HF token

## 获取帮助

如果问题持续：
1. 检查网络连接: `ping hf-mirror.com`
2. 查看日志: 程序会显示详细错误信息
3. 使用 txt 模式临时绕过模型下载

