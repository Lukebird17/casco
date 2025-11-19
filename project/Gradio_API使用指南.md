# 🎯 Gradio API 使用指南

## 📌 API信息

- **API地址**：`https://app-u613z0mda075e806.aistudio-app.com/`
- **API类型**：Gradio应用API
- **认证方式**：无需Token（公开API）
- **功能**：文档解析、OCR、表格识别、图表解析

---

## 🚀 快速开始

### 第1步：安装Gradio客户端

```bash
pip install gradio_client
```

### 第2步：设置环境变量

```bash
export PADDLEOCR_API_URL="https://app-u613z0mda075e806.aistudio-app.com/"
```

**注意**：不需要设置`PADDLEOCR_API_TOKEN`，Gradio API不需要Token！

### 第3步：运行程序

```bash
python run_competition.py
```

程序会自动检测到API配置并使用Gradio API模式！

---

## 📋 API端点说明

### 1. `/parse_doc_router` - 文档解析（**推荐使用**）

**功能**：全功能文档解析，支持PDF和图片

**参数**：
- `fp`: 文件路径（必需）
- `use_chart`: 是否启用图表解析（默认：False）
- `use_unwarping`: 是否启用文档矫正（默认：False）
- `use_orientation`: 是否启用方向分类（默认：False）

**返回值**：元组 `(markdown_content, visualization_html, markdown_source)`
- `[0] markdown_content`: 格式化的Markdown内容
- `[1] visualization_html`: 可视化HTML（带标注的原文档）
- `[2] markdown_source`: 原始Markdown源代码

**使用示例**：

```python
from gradio_client import Client, handle_file

client = Client("https://app-u613z0mda075e806.aistudio-app.com/")

result = client.predict(
    fp=handle_file('document.pdf'),
    use_chart=True,
    use_unwarping=True,
    use_orientation=True,
    api_name="/parse_doc_router"
)

markdown_content = result[0]
visualization_html = result[1]
markdown_source = result[2]

print(markdown_content)
```

### 2. `/parse_vl_router` - 视觉语言模型解析

**功能**：使用视觉大模型解析文档

**参数**：
- `fp`: 文件路径（必需）

**返回值**：元组 `(markdown_content, raw_output)`

**使用场景**：复杂文档、手写体、特殊排版

### 3. 其他端点

- `/parse_vl_router_1`、`/parse_vl_router_2`、`/parse_vl_router_3`：不同的VL模型变体
- `/on_file_doc_change`：文件上传回调
- `/on_gallery_select_for_doc`：画廊选择回调

---

## 💡 使用示例

### 示例1：基础使用

```python
from gradio_client import Client, handle_file

# 初始化客户端
client = Client("https://app-u613z0mda075e806.aistudio-app.com/")

# 解析PDF
result = client.predict(
    fp=handle_file('document.pdf'),
    use_chart=True,
    use_unwarping=True,
    use_orientation=True,
    api_name="/parse_doc_router"
)

# 获取Markdown内容
print(result[0])
```

### 示例2：批量处理

```python
import os
from gradio_client import Client, handle_file

client = Client("https://app-u613z0mda075e806.aistudio-app.com/")

# 遍历所有PDF文件
for pdf_file in os.listdir('pdfs/'):
    if pdf_file.endswith('.pdf'):
        pdf_path = os.path.join('pdfs', pdf_file)
        
        # 解析文档
        result = client.predict(
            fp=handle_file(pdf_path),
            use_chart=True,
            use_unwarping=True,
            use_orientation=True,
            api_name="/parse_doc_router"
        )
        
        # 保存结果
        output_file = f"output/{pdf_file.replace('.pdf', '.md')}"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result[0])
        
        print(f"✅ {pdf_file} 处理完成")
```

### 示例3：集成到项目中

```python
from simple_ocr_system import SimpleOCRSystem

# 自动使用Gradio API（如果配置了环境变量）
ocr = SimpleOCRSystem()

# 处理文档
results = ocr.process_document('document.pdf', extract_toc=True)

# 查看结果
print(f"文件：{results['file_name']}")
print(f"页数：{results['total_pages']}")
print(f"文本：{results['pages'][0]['text'][:500]}...")
```

---

## 🔧 配置方式

### 方式1：环境变量（推荐）

```bash
# 在终端设置
export PADDLEOCR_API_URL="https://app-u613z0mda075e806.aistudio-app.com/"

# 运行程序
python run_competition.py
```

### 方式2：Python代码

```python
import os
os.environ['PADDLEOCR_API_URL'] = "https://app-u613z0mda075e806.aistudio-app.com/"

from simple_ocr_system import SimpleOCRSystem
ocr = SimpleOCRSystem()  # 自动使用API模式
```

### 方式3：.env文件

创建`.env`文件：
```
PADDLEOCR_API_URL=https://app-u613z0mda075e806.aistudio-app.com/
```

在代码中：
```python
from dotenv import load_dotenv
load_dotenv()

from simple_ocr_system import SimpleOCRSystem
ocr = SimpleOCRSystem()
```

---

## ⚙️ 功能选项说明

### use_chart（图表解析）

- **True**: 启用图表识别，将图表转换为表格数据
- **False**: 保持图表为图片形式
- **适用场景**: 包含柱状图、饼图、折线图的文档

### use_unwarping（文档矫正）

- **True**: 矫正扭曲、褶皱、倾斜的文档
- **False**: 不进行矫正
- **适用场景**: 扫描件、拍照文档

### use_orientation（方向分类）

- **True**: 自动识别并矫正0°/90°/180°/270°的图片
- **False**: 假设图片方向正确
- **适用场景**: 混合方向的文档集合

---

## 📊 API vs 本地对比

| 特性 | Gradio API | 本地PaddleOCR |
|------|-----------|--------------|
| **安装** | ✅ 只需pip install gradio_client | ⚠️ 需要安装PaddlePaddle |
| **稳定性** | ✅ 云端稳定 | ⚠️ 可能有兼容性问题 |
| **功能** | ✅ 完整（表格+版面+OCR+图表） | ⚠️ 基础OCR |
| **速度** | ✅ 云端GPU加速 | ⚠️ 本地CPU较慢 |
| **成本** | ✅ 免费（公开API） | ✅ 免费 |
| **网络** | ⚠️ 需要联网 | ✅ 离线可用 |
| **认证** | ✅ 无需Token | N/A |

---

## 🐛 常见问题

### Q1: 如何确认是否使用了API模式？

启动时会显示：
```
🚀 初始化简化版OCR系统...
  🌐 使用Gradio在线API模式
  📍 API地址: https://app-u613z0mda075e806.aistudio-app.com/
  ✅ Gradio客户端初始化成功
✅ OCR系统初始化完成
```

### Q2: API请求慢怎么办？

可能原因：
1. 网络连接慢
2. 文档很大（多页PDF）
3. API服务繁忙

解决办法：
- 分批处理大文档
- 使用更快的网络
- 考虑使用本地模式

### Q3: gradio_client安装失败？

```bash
# 尝试升级pip
pip install --upgrade pip

# 安装gradio_client
pip install gradio_client

# 或者指定版本
pip install gradio_client==0.7.0
```

### Q4: 如何切换回本地模式？

```bash
# 清除API配置
unset PADDLEOCR_API_URL

# 运行程序
python run_competition.py
```

或者在代码中：
```python
from simple_ocr_system import SimpleOCRSystem
ocr = SimpleOCRSystem(use_api=False)  # 强制使用本地
```

### Q5: API返回的Markdown格式是什么样的？

典型格式：
```markdown
# 文档标题

## 章节1

正文内容...

| 列1 | 列2 |
|-----|-----|
| 数据1 | 数据2 |

![图片](image_path.jpg)

$$
数学公式
$$
```

### Q6: 可以处理哪些文件类型？

支持的文件类型：
- ✅ PDF文档（单页或多页）
- ✅ 图片（PNG, JPG, JPEG, BMP）
- ✅ 扫描件
- ✅ 拍照文档

### Q7: API有调用次数限制吗？

这是一个公开的Gradio应用，通常有一定的调用限制。如果遇到限制：
1. 降低请求频率
2. 考虑自己部署PaddleX服务
3. 使用本地模式

---

## 🔍 输出说明

### Markdown内容

API会将文档转换为结构化的Markdown格式，包括：
- 标题层级
- 段落文本
- 表格（HTML或Markdown格式）
- 图片链接
- 数学公式（LaTeX格式）

### 可视化HTML

可视化HTML包含：
- 原文档图片
- 版面检测框
- 文本识别结果
- 不同元素类型的颜色标注

### Markdown源代码

原始的、未经格式化的Markdown文本，可以直接用于：
- 文本编辑器打开
- 导入到笔记软件
- 进一步处理

---

## ✨ 总结

### 优点

- ✅ **简单**：只需要一个URL，无需Token
- ✅ **稳定**：云端部署，不受本地环境影响
- ✅ **功能强**：支持表格、图表、公式识别
- ✅ **免费**：公开API，无需付费
- ✅ **快速**：云端GPU加速

### 适用场景

- 📄 PDF文档批量处理
- 📊 包含表格和图表的文档
- 🔄 需要处理多种格式的文档
- 🌐 有网络连接的环境
- 🚀 快速原型开发

### 立即开始

```bash
# 1. 安装客户端
pip install gradio_client

# 2. 设置环境变量
export PADDLEOCR_API_URL="https://app-u613z0mda075e806.aistudio-app.com/"

# 3. 运行程序
python run_competition.py
```

就这么简单！🎉




