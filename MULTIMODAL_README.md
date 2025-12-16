# 多模态 RAG 系统使用指南

## 🎯 系统架构

```
┌──────────────────┐        ┌──────────────────┐
│  文本向量数据库   │        │  图片向量数据库   │
│   (BGE-M3)      │        │  (CLIP)         │
│  - 文本块        │        │  - 图片文件      │
│  - 1024维向量    │        │  - 512维向量     │
└──────────────────┘        └──────────────────┘
         ↓                           ↓
         └───────────┬───────────────┘
                     ↓
           ┌──────────────────┐
           │  混合检索器       │
           │ HybridRetriever │
           └──────────────────┘
                     ↓
         ┌───────────────────────┐
         │ 多模态 Context        │
         │ [文本1, 图片1, ...]   │
         └───────────────────────┘
                     ↓
           ┌──────────────────┐
           │   Qwen-VL 大模型  │
           └──────────────────┘
```

## 📦 安装依赖

### 1. 基础依赖（已安装）
```bash
# 文本处理
chromadb
openai
tqdm
```

### 2. 新增依赖（图片处理）
```bash
# 运行安装脚本
chmod +x install_clip_dependencies.sh
./install_clip_dependencies.sh
```

或手动安装：
```bash
conda activate rag

# 安装 PyTorch（如果未安装）
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# 安装 Transformers
pip install transformers

# 安装 Pillow
pip install Pillow
```

## 🚀 使用流程

### 步骤1: 数据处理（建立索引）

```bash
# 设置 HuggingFace 镜像
export HF_ENDPOINT=https://hf-mirror.com

# 运行数据处理脚本
python process_data.py
```

**处理流程：**
1. ✅ 使用 MinerU 提取 PDF 文本和图片
2. ✅ 文本切分为 500 字符的块
3. ✅ 文本块用 BGE-M3 编码 → 文本向量数据库
4. ✅ 图片用 Chinese-CLIP 编码 → 图片向量数据库

**输出示例：**
```
📚 加载文档...
正在加载: ./data/OS-08 pm-manage.pdf
📄 处理文件: OS-08 pm-manage.pdf
   📝 找到Markdown: OS-08 pm-manage.md
   📊 提取统计:
      - 文本块: 311
      - 图片: 44

✅ 加载完成:
   - 文档: 1 个
   - 图片: 44 张

📝 处理文本数据...
✅ 成功添加 47 个文档块到向量数据库

🖼️  处理图片数据...
✅ 成功添加 44 张图片到向量数据库

📊 数据处理完成！
✅ 文本文档块: 47
✅ 图片数量: 44
```

### 步骤2: 使用混合检索器

```python
from hybrid_retriever import HybridRetriever

# 初始化检索器
retriever = HybridRetriever(
    text_weight=0.6,    # 文本权重 60%
    image_weight=0.4    # 图片权重 40%
)

# 1. 纯文本查询
results = retriever.search(
    query="什么是虚拟内存的页表结构？",
    top_k=5
)

# 2. 多模态查询（文本 + 图片）
results = retriever.search(
    query={
        "text": "解释一下这个架构",
        "image": "user_uploaded_image.jpg"  # 用户上传的图片
    },
    top_k=5
)

# 3. 查看结果
print(f"文本结果: {len(results['text_results'])} 个")
print(f"图片结果: {len(results['image_results'])} 张")
print(f"合并结果: {len(results['combined'])} 个")

# 4. 格式化为 LLM Context
context = retriever.format_context_for_llm(results)
# context 格式:
# [
#     {"type": "text", "content": "...", "source": "..."},
#     {"type": "image", "path": "...", "description": "...", "source": "..."},
#     ...
# ]
```

### 步骤3: 传给多模态大模型（Qwen-VL）

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-api-key",
    base_url="https://api.siliconflow.cn/v1/"
)

# 构建多模态消息
messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "什么是虚拟内存的页表结构？"},
            {"type": "text", "text": f"参考资料：\n{format_context(context)}"},
        ]
    }
]

# 添加图片（如果有）
for item in context:
    if item['type'] == 'image':
        messages[0]["content"].append({
            "type": "image_url",
            "image_url": {"url": f"file://{item['path']}"}
        })

# 调用大模型
response = client.chat.completions.create(
    model="Qwen/Qwen3-VL-32B-Instruct",
    messages=messages
)
```

## 📊 检索结果格式

### 文本结果
```python
{
    "type": "text",
    "content": "虚拟内存使用页表进行地址转换...",
    "metadata": {
        "filename": "OS-08 pm-manage.pdf",
        "page_number": 5,
        "chunk_id": 2
    },
    "distance": 0.234,  # 越小越相似
    "rank": 1
}
```

### 图片结果
```python
{
    "type": "image",
    "image_path": "/path/to/.mineru_output/OS-08 pm-manage/images/xxx.jpg",
    "description": "图片来源: OS-08 pm-manage.pdf, 第5页\n上下文: ...页表结构...",
    "metadata": {
        "filename": "OS-08 pm-manage.pdf",
        "page_number": 5,
        "section": "物理内存管理",
        "context": "...前后文本..."
    },
    "distance": 0.156,
    "rank": 2
}
```

## 🔧 参数调整

### 1. 文本/图片权重
```python
# 更重视文本
retriever = HybridRetriever(text_weight=0.8, image_weight=0.2)

# 更重视图片
retriever = HybridRetriever(text_weight=0.4, image_weight=0.6)

# 仅文本检索
results = retriever.search(query, include_images=False)
```

### 2. 检索数量
```python
# 总共返回 10 个结果
results = retriever.search(query, top_k=10)

# 精确控制文本和图片数量
results = retriever.search(
    query, 
    top_k=10,
    text_k=6,   # 6个文本结果
    image_k=4   # 4个图片结果
)
```

### 3. Context 长度限制
```python
# 限制文本总长度为 2000 字符
context = retriever.format_context_for_llm(results, max_length=2000)
```

## 🎨 系统特性

### ✅ 已实现
1. **双索引系统**
   - 文本索引（BGE-M3，1024维）
   - 图片索引（Chinese-CLIP，512维）

2. **多模态查询**
   - 纯文本查询
   - 文本+图片查询
   - 以图搜图

3. **智能合并**
   - 交替插入文本和图片
   - 保持结果多样性

4. **上下文提取**
   - 图片前后文本
   - 所在章节标题
   - 页码信息

5. **缓存机制**
   - MinerU 结果缓存
   - 避免重复处理

### 🔄 下一步（TODO）
- [ ] 修改 main.py 支持多模态输入输出
- [ ] 图片描述生成（可选，使用 Qwen-VL）
- [ ] 支持用户上传图片查询
- [ ] Web UI 展示图片结果

## 📁 文件结构

```
rag-agent/
├── image_vector_store.py       # 图片向量存储（新）
├── hybrid_retriever.py         # 混合检索器（新）
├── enhanced_ocr.py            # MinerU 处理（已修改）
├── document_loader.py         # 文档加载（已修改）
├── process_data.py            # 数据处理（已修改）
├── vector_store.py            # 文本向量存储
├── text_splitter.py           # 文本切分
├── main.py                    # 主程序（待修改）
├── config.py                  # 配置文件
│
├── data/                      # 原始数据
│   └── OS-08 pm-manage.pdf
│
├── .mineru_output/            # MinerU 输出（新位置）
│   └── OS-08 pm-manage/
│       └── images/            # 提取的图片
│
└── vector_db/                 # 向量数据库
    ├── chroma.sqlite3
    └── ...
```

## ⚠️  注意事项

1. **首次运行会下载模型**
   - Chinese-CLIP (~500MB)
   - 需要网络连接
   - 已配置 HuggingFace 镜像加速

2. **GPU 内存需求**
   - CLIP 模型: ~1GB
   - 如无 GPU，自动使用 CPU（较慢）

3. **图片路径**
   - 图片存储在 `.mineru_output/` 目录
   - 路径为绝对路径，可直接访问

4. **向量数据库**
   - 文本和图片在同一个数据库的不同 collection
   - collection 名称：
     - `course_documents` (文本)
     - `image_documents` (图片)

## 🧪 测试

```bash
# 测试图片向量存储
python -c "from image_vector_store import ImageVectorStore; print('✅ 可用')"

# 测试混合检索器
python -c "from hybrid_retriever import HybridRetriever; print('✅ 可用')"

# 完整测试
python hybrid_retriever.py
```

## 🐛 故障排除

### 问题1: 模型下载失败
```bash
# 解决方案：使用镜像
export HF_ENDPOINT=https://hf-mirror.com
python install_clip_dependencies.sh
```

### 问题2: CUDA out of memory
```bash
# 解决方案：使用 CPU
# 编辑 image_vector_store.py:
# self.device = "cpu"  # 强制使用 CPU
```

### 问题3: 图片索引为空
```bash
# 检查 MinerU 是否提取了图片
ls -la .mineru_output/*/images/

# 重新处理数据
python process_data.py
```

## 📞 支持

有问题请查看：
1. 日志输出
2. 检查 `.mineru_output/` 目录
3. 验证向量数据库状态：
   ```python
   from hybrid_retriever import HybridRetriever
   retriever = HybridRetriever()
   print(retriever.get_stats())
   ```

