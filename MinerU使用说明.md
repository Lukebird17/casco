# MinerU 使用说明

## 📚 MinerU 简介

**MinerU** (magic-pdf) 是 OpenDataLab 开发的高质量PDF解析工具，专门用于科研和学术文档处理。

### ✨ 核心优势

1. **高质量文本提取** - 保留原始格式和结构
2. **完美图文分离** - 独立提取图片和文本
3. **表格识别** - 识别并保留表格结构
4. **公式支持** - 识别LaTeX公式
5. **Markdown输出** - 直接转换为Markdown格式
6. **多种PDF支持** - 文本PDF和图片PDF都可以

---

## 🚀 安装

### 方式1：使用安装脚本（推荐）

```bash
cd /Users/leon/Project/CS3602NLP/Proj2
chmod +x install_missing.sh
bash install_missing.sh
```

### 方式2：手动安装

```bash
# 完整安装（包含OCR）
pip install magic-pdf[full]

# 或仅基础功能
pip install magic-pdf
```

---

## 💡 使用方法

### 1. 基础使用

```python
from enhanced_ocr import EnhancedOCRProcessor

# 创建处理器
processor = EnhancedOCRProcessor(use_ocr=False)  # 文本PDF
# processor = EnhancedOCRProcessor(use_ocr=True)  # 图片PDF（需要OCR）

# 处理PDF
results = processor.process_pdf("document.pdf")

# 格式化输出
formatted_text = processor.format_results_with_page_num(results, "pdf")
print(formatted_text)
```

### 2. 在动态数据库管理中使用

```python
from dynamic_db_manager import DynamicDBManager

manager = DynamicDBManager()

# 添加文件（自动使用MinerU）
result = manager.add_file(
    "data/course.pdf",
    course_name="自然语言处理",
    use_ocr=False  # 如果是扫描版PDF，设为True
)
```

### 3. 在Web界面中使用

```bash
# 启动Web界面
python app_enhanced.py

# 在"数据库管理"标签：
# 1. 选择PDF文件
# 2. 输入课程名称
# 3. 勾选"使用OCR"（如果需要）
# 4. 点击"添加文件"
```

---

## 📊 处理模式

### 模式1：文本提取模式（默认）

适用于：正常的PDF文档（有文本层）

```python
processor = EnhancedOCRProcessor(use_ocr=False)
```

**特点：**
- ✅ 处理速度快
- ✅ 准确率高
- ✅ 保留格式
- ✅ 不需要GPU

### 模式2：OCR模式

适用于：扫描版PDF、图片PDF

```python
processor = EnhancedOCRProcessor(use_ocr=True)
```

**特点：**
- ✅ 识别图片中的文字
- ✅ 处理扫描版文档
- ⚠️  速度较慢
- ⚠️  需要更多资源

---

## 🔄 处理流程

```
PDF文件
    ↓
【MinerU解析】
    ├─→ 文本提取（保留格式）
    ├─→ 图片提取（独立保存）
    ├─→ 表格识别（结构化）
    ├─→ 公式识别（LaTeX）
    └─→ 转为Markdown
    ↓
【按页面组织】
    ├─→ 第1页: 文本 + 图片 + 表格
    ├─→ 第2页: 文本 + 图片 + 表格
    └─→ ...
    ↓
【格式化输出】
    ↓
存入向量数据库
```

---

## 📝 输出格式示例

```
============================================================
第 1 页
============================================================

【文本内容】
这是第一页的文本内容...
可能包含多个段落。

【表格 1】
列1 | 列2 | 列3
数据1 | 数据2 | 数据3

【包含 2 张图片】

============================================================
第 2 页
============================================================

【文本内容】
这是第二页的内容...
```

---

## 🆚 对比其他工具

| 特性 | MinerU | PyMuPDF | pdfplumber | PaddleOCR |
|-----|--------|---------|------------|-----------|
| 文本提取 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| 图文分离 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| 表格识别 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ |
| 公式识别 | ⭐⭐⭐⭐⭐ | ⭐ | ⭐ | ⭐⭐ |
| 格式保留 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐ |
| 处理速度 | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ |
| 安装难度 | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐ |

**总结：** MinerU在质量上最优，特别适合学术文档和课程资料。

---

## ⚙️ 高级配置

### 自定义输出目录

```python
processor = EnhancedOCRProcessor()
results = processor.process_pdf(
    "document.pdf",
    output_dir="custom_output/"  # 自定义输出目录
)
```

### 处理DOCX和PPTX

```python
# DOCX
results_docx = processor.process_docx("document.docx")
formatted = processor.format_results_with_page_num(results_docx, "docx")

# PPTX
results_pptx = processor.process_pptx("slides.pptx")
formatted = processor.format_results_with_page_num(results_pptx, "pptx")
```

---

## 🐛 常见问题

### Q1: 安装失败？

```bash
# 尝试单独安装依赖
pip install torch torchvision
pip install magic-pdf
```

### Q2: 处理速度慢？

**原因：**
- 使用了OCR模式
- PDF页数太多
- 图片分辨率过高

**解决：**
- 对文本PDF使用 `use_ocr=False`
- 分批处理大文件
- 降低图片质量

### Q3: MinerU不可用时会怎样？

系统会自动降级到PyMuPDF备选方案：

```
⚠️  MinerU 不可用
✅ 使用PyMuPDF备选方案
```

仍然可以处理PDF，只是功能会稍微弱一些。

---

## 📚 参考资源

- **GitHub:** https://github.com/opendatalab/MinerU
- **文档:** https://github.com/opendatalab/MinerU/blob/master/README_zh-CN.md
- **论文:** MinerU: An End-to-End Solution for PDF Parsing

---

## ✅ 总结

**MinerU的优势：**
1. ✅ 最高质量的PDF解析
2. ✅ 完美的图文分离
3. ✅ 支持复杂格式（表格、公式）
4. ✅ 直接输出Markdown
5. ✅ 特别适合学术文档

**最佳实践：**
- 📄 普通PDF → `use_ocr=False`（快速、准确）
- 🖼️ 扫描PDF → `use_ocr=True`（完整识别）
- 📚 大批量处理 → 分批处理
- 💾 保留原始输出 → 指定`output_dir`

**开始使用：**
```bash
bash install_missing.sh
python app_enhanced.py
```

🚀 **享受高质量的PDF解析体验！**

