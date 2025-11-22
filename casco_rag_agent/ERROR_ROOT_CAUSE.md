# 🔍 错误根源分析

## 错误信息
```
AsyncClient.__init__() got an unexpected keyword argument 'proxies'
```

## 🎯 根本原因

### 问题链条

```
你的代码
    ↓ 调用
RAG-Anything
    ↓ 调用
LightRAG (openai_embed / openai_complete)
    ↓ 调用
openai.AsyncOpenAI()
    ↓ 内部创建
httpx.AsyncClient(proxies=...)  ← 💥 这里出错！
```

### 详细解释

#### 1. httpx 版本变化

**httpx 0.27.x（旧版）**：
```python
client = httpx.AsyncClient(proxies={...})  # ✅ 支持
```

**httpx 0.28.x（新版）**：
```python
client = httpx.AsyncClient(proxies={...})  # ❌ 不支持
# 改为：
client = httpx.AsyncClient(proxy="...", mounts={...})  # ✅ 新API
```

#### 2. openai 库的适配

**openai < 1.40.x（旧版）**：
```python
# 在 openai/_base_client.py 中
self._client = httpx.AsyncClient(
    proxies=self._proxies,  # ← 使用旧的 proxies 参数
    ...
)
```

**openai >= 1.40.x（新版）**：
```python
# 已适配 httpx 0.28.x
self._client = httpx.AsyncClient(
    proxy=self._proxy,  # ← 使用新的 proxy 参数
    ...
)
```

#### 3. 你当前的情况

```bash
# 你安装了：
openai==1.50.2  # 已适配 httpx 0.28
httpx==0.27.2   # 旧版 API

# 但是 openai 1.50.2 使用新 API：
httpx.AsyncClient(proxy=...)  # ← 0.27.2 不认识 proxy

# 或者反过来，某些缓存的模块仍在使用旧代码：
httpx.AsyncClient(proxies=...)  # ← 但实际运行时用的是 0.28.x
```

## 🔧 真正的解决方案

### 方案 1: 确保版本完全匹配（推荐）

```bash
conda activate casco

# 完全卸载
pip uninstall -y openai httpx httpcore

# 安装兼容组合
pip install "openai==1.50.2" "httpx==0.27.2" "httpcore==1.0.2"

# 验证（重要！）
python << 'PYEOF'
import httpx
import inspect

# 检查 AsyncClient 的参数
sig = inspect.signature(httpx.AsyncClient.__init__)
params = list(sig.parameters.keys())

print(f"httpx version: {httpx.__version__}")
print(f"AsyncClient accepts 'proxies': {'proxies' in params}")
print(f"AsyncClient accepts 'proxy': {'proxy' in params}")

if 'proxies' in params:
    print("✅ 使用旧版 API (0.27.x)")
else:
    print("❌ 使用新版 API (0.28.x) - 不兼容！")
PYEOF
```

### 方案 2: 从源码重新安装所有组件

```bash
conda activate casco

# 1. 完全清理
pip uninstall -y raganything lightrag openai httpx httpcore

# 2. 安装基础依赖（锁定版本）
pip install "httpx==0.27.2" "httpcore==1.0.2"

# 3. 安装 openai（会检查 httpx 兼容性）
pip install "openai==1.50.2"

# 4. 从源码安装 RAG-Anything（不安装依赖，避免版本冲突）
cd /home/honglianglu/ssd/casco/RAG-Anything
pip install -e . --no-deps

# 5. 手动安装 RAG-Anything 的其他依赖（跳过 openai/httpx）
pip install lightrag litellm numpy tqdm python-dotenv

# 6. 重启 Python 进程测试
cd /home/honglianglu/ssd/casco/casco_rag_agent
python -c "
import httpx
import openai
print(f'httpx: {httpx.__version__}')
print(f'openai: {openai.__version__}')
from raganything import RAGAnything
print('✅ 导入成功')
"
```

### 方案 3: 检查是否有残留

```bash
# 查找所有 httpx 安装位置
python -c "import httpx; print(httpx.__file__)"

# 检查 pip 显示的版本
pip show httpx

# 查找是否有多个 httpx
find $CONDA_PREFIX -name "httpx" -type d

# 如果发现多个，手动删除旧的
```

## 🧪 验证脚本

创建并运行这个测试：

```python
# test_httpx_compat.py
import sys
import httpx
import inspect

print("="*60)
print("httpx 兼容性测试")
print("="*60)

# 版本
print(f"\nhttpx 版本: {httpx.__version__}")
print(f"Python 版本: {sys.version}")

# 检查 AsyncClient 参数
sig = inspect.signature(httpx.AsyncClient.__init__)
params = list(sig.parameters.keys())

print(f"\nAsyncClient 支持的参数:")
for p in params[:20]:  # 只显示前20个
    print(f"  - {p}")

# 关键参数检查
print(f"\n关键检查:")
print(f"  支持 'proxies': {'proxies' in params}")
print(f"  支持 'proxy': {'proxy' in params}")
print(f"  支持 'mounts': {'mounts' in params}")

# 判断版本
if 'proxies' in params:
    print("\n✅ 结论: httpx 0.27.x (旧API) - 与 openai < 1.50 兼容")
    expected_openai = "< 1.50"
elif 'proxy' in params:
    print("\n✅ 结论: httpx 0.28.x (新API) - 与 openai >= 1.50 兼容")
    expected_openai = ">= 1.50"
else:
    print("\n❌ 结论: 未知版本")
    expected_openai = "未知"

# 检查 openai
try:
    import openai
    print(f"\nopenai 版本: {openai.__version__}")
    
    # 尝试创建客户端
    try:
        client = httpx.AsyncClient(timeout=10.0)
        print("✅ 可以创建 AsyncClient")
        client.aclose()
    except Exception as e:
        print(f"❌ 创建 AsyncClient 失败: {e}")
        
except ImportError:
    print("\n⚠️  openai 未安装")

print("\n" + "="*60)
```

运行：
```bash
conda activate casco
cd /home/honglianglu/ssd/casco/casco_rag_agent
python test_httpx_compat.py
```

## 📌 最终建议

**如果 test_httpx_compat.py 显示 httpx 0.28.x**：
```bash
# httpx 降级失败，需要强制重装
pip uninstall -y httpx httpcore
pip install "httpx==0.27.2" "httpcore==1.0.2" --force-reinstall --no-cache-dir
```

**如果仍然失败**：
```bash
# 可能是环境污染，重建 conda 环境
conda create -n casco_clean python=3.11 -y
conda activate casco_clean
pip install "httpx==0.27.2" "openai==1.50.2"
cd /home/honglianglu/ssd/casco/RAG-Anything
pip install -e .
```

运行 `test_httpx_compat.py` 看看真实情况！

