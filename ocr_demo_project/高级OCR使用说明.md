# 高级OCR文档处理系统使用说明

## ✨ 功能特性

系统已默认集成PaddleOCR高级文档处理功能，自动支持：

### 📋 核心功能
- ✅ **自动旋转纠正** - 自动检测并纠正倾斜的文档
- ✅ **水印去除** - 自动去除浅色水印，提高识别准确率
- ✅ **模糊图像增强** - 自动增强模糊扫描件
- ✅ **复杂表格识别** - 支持合并单元格的复杂表格
- ✅ **多语言支持** - 中文（简繁体）、英文、德文、西班牙语等
- ✅ **数学公式提取** - 可选的公式识别功能

---

## 🚀 快速开始

### 1. 安装依赖

```bash
# 安装核心依赖
pip install paddleocr paddlepaddle opencv-python

# 或安装完整依赖
pip install -r requirements_enhanced.txt
```

### 2. 使用方法

#### 方式1：自动处理（推荐）

系统会**自动使用高级OCR**处理所有PDF文档：

```python
from enhanced_utils import EnhancedReadFiles

# 创建读取器
reader = EnhancedReadFiles('../data')

# 自动处理所有文档（自动使用高级OCR）
docs = reader.get_content(max_token_len=400, cover_content=50)

# 自动功能：
# - 旋转纠正
# - 水印去除
# - 模糊增强
# - 表格提取
# - 多语言识别
```

#### 方式2：单独处理某个文档

```python
from advanced_ocr_system import ComprehensiveOCRSystem

# 创建OCR系统
ocr_system = ComprehensiveOCRSystem()

# 处理文档
results = ocr_system.process_document(
    'your_document.pdf',
    auto_rotate=True,        # 自动旋转
    remove_watermark=True,   # 去水印
    enhance_blur=True,       # 增强模糊
    extract_tables=True,     # 提取表格
    extract_formulas=False,  # 提取公式（可选）
    language='auto'          # 自动检测语言
)

# 导出结果
ocr_system.export_results(results)
```

---

## 📊 功能详解

### 1. 自动旋转纠正

自动检测文档倾斜角度并纠正：
- 使用边缘检测算法
- 自动计算旋转角度
- 保持图像质量

### 2. 水印去除

智能去除文档水印：
- 自动检测水印区域
- 使用CLAHE增强对比度
- 保留原始文字清晰度

### 3. 模糊图像增强

增强模糊扫描件：
- 锐化处理
- 去噪处理
- 对比度增强

**效果对比：**
```
模糊度分数: <100 → 自动增强
模糊度分数: ≥100 → 保持原样
```

### 4. 复杂表格识别

支持各种复杂表格：
- ✅ 合并单元格（colspan/rowspan）
- ✅ 多行表头
- ✅ 嵌套表格
- ✅ 不规则边框

**输出格式：**
```markdown
| 列1 | 列2 | 列3 |
|---|---|---|
| 数据1 | 数据2 | 数据3 |
```

### 5. 多语言支持

自动检测并识别：
- 🇨🇳 中文（简体）
- 🇭🇰 中文（繁体）
- 🇬🇧 英文
- 🇩🇪 德文
- 🇪🇸 西班牙语
- 🇫🇷 法文
- 其他80+语言

---

## ⚙️ 配置选项

### 语言设置

```python
# 自动检测（推荐）
language='auto'

# 指定语言
language='chinese'   # 中文（简繁体）
language='english'   # 英文
language='multilang' # 多语言（包含德西法等）
```

### 处理选项

```python
results = ocr_system.process_document(
    file_path,
    
    # 图像预处理
    auto_rotate=True,       # 是否自动旋转
    remove_watermark=True,  # 是否去除水印
    enhance_blur=True,      # 是否增强模糊图像
    
    # 内容提取
    extract_tables=True,    # 是否提取表格
    extract_formulas=False, # 是否提取数学公式
    
    # 语言设置
    language='auto'         # 语言选择
)
```

---

## 📈 性能优化

### GPU加速（可选）

如果有GPU，可以显著提升速度：

```bash
# 卸载CPU版本
pip uninstall paddlepaddle

# 安装GPU版本
pip install paddlepaddle-gpu
```

然后在代码中设置：
```python
from paddleocr import PaddleOCR

ocr = PaddleOCR(
    use_gpu=True,  # 启用GPU
    ...
)
```

### 批量处理优化

```python
# 处理多个文档
from enhanced_utils import EnhancedReadFiles

reader = EnhancedReadFiles('../data')

# 自动并行处理所有文档
docs = reader.get_content(
    max_token_len=400,
    cover_content=50
)

# 文档会自动：
# 1. 检测文档类型（正常/扫描）
# 2. 选择最优处理方案
# 3. 提取文字和表格
# 4. 保留来源信息
```

---

## 🔍 处理流程

```
PDF文档
   ↓
检测文档类型
   ↓
┌─────────────┬─────────────┐
│  正常PDF    │  扫描PDF    │
└─────────────┴─────────────┘
       ↓             ↓
   直接提取      PaddleOCR
                     ↓
              图像预处理
              - 旋转纠正
              - 去水印
              - 增强模糊
                     ↓
              表格识别
              - 检测表格
              - 提取结构
              - 转Markdown
                     ↓
              文字识别
              - 多语言OCR
              - 置信度筛选
                     ↓
              结果合并
                     ↓
            结构化输出
```

---

## ⚠️ 故障排查

### 问题1：PaddleOCR初始化失败

**错误：** `ImportError: No module named 'paddleocr'`

**解决：**
```bash
pip install paddleocr paddlepaddle
```

### 问题2：OpenCV报错

**错误：** `cv2.error: ...`

**解决：**
```bash
pip install opencv-python opencv-contrib-python
```

### 问题3：内存不足

**解决：** 减小图片分辨率或分批处理
```python
# 在advanced_ocr_system.py中调整
pix = page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5))  # 从2降到1.5
```

### 问题4：识别速度慢

**解决方案：**
1. 使用GPU版本（提速5-10倍）
2. 减小处理分辨率
3. 关闭不需要的功能：
```python
results = ocr_system.process_document(
    file_path,
    auto_rotate=False,      # 如果文档已经正的
    remove_watermark=False, # 如果没有水印
    enhance_blur=False      # 如果清晰度好
)
```

---

## 📦 输出格式

### JSON格式

```json
{
  "file_name": "document.pdf",
  "total_pages": 10,
  "pages": [
    {
      "page_number": 1,
      "text": "识别的文字...",
      "tables": [
        {
          "table_index": 1,
          "markdown": "| 列1 | 列2 |\n|---|---|\n| 数据1 | 数据2 |",
          "has_merged_cells": true
        }
      ],
      "processing_steps": ["模糊增强", "方向检测与旋转"]
    }
  ]
}
```

### 文本格式

```
文档: document.pdf
总页数: 10
==================================================

第 1 页
--------------------------------------------------
处理步骤: 模糊增强, 方向检测与旋转

[检测到 1 个表格]

| 公司名称 | 中标金额 |
|---|---|
| 公司A | 15.8亿元 |

识别的文字内容...
```

---

## 💡 最佳实践

### 1. 处理大量文档

```python
from enhanced_utils import EnhancedReadFiles

# 直接处理整个目录
reader = EnhancedReadFiles('../data')
docs = reader.get_content()

# 系统会自动：
# - 识别所有PDF
# - 智能选择处理方案
# - 批量处理
# - 保存结果
```

### 2. 处理特定类型文档

```python
# 处理扫描件（强制使用高级OCR）
# 系统已默认使用，无需额外配置

# 处理纯文本PDF（会自动检测并快速处理）
# 系统自动降级到标准方法，速度更快
```

### 3. 获取详细处理信息

```python
results = ocr_system.process_document(file_path)

for page in results['pages']:
    print(f"第{page['page_number']}页:")
    print(f"  处理步骤: {page['processing_steps']}")
    print(f"  表格数: {len(page['tables'])}")
    print(f"  文字长度: {len(page['text'])}")
```

---

## 🎯 总结

### 默认功能（无需配置）
- ✅ 自动使用PaddleOCR
- ✅ 自动旋转纠正
- ✅ 自动去水印
- ✅ 自动增强模糊图像
- ✅ 自动提取复杂表格
- ✅ 自动多语言识别
- ✅ 失败自动降级

### 使用建议
1. **正常使用**：直接用`EnhancedReadFiles`，系统会自动处理
2. **特殊需求**：使用`ComprehensiveOCRSystem`进行精细控制
3. **速度优化**：安装GPU版本或关闭不需要的功能
4. **质量优先**：保持所有功能开启（默认）

### 快速命令

```bash
# 安装
pip install paddleocr paddlepaddle opencv-python

# 使用
python demo_enhanced.py

# 或
from enhanced_utils import EnhancedReadFiles
reader = EnhancedReadFiles('../data')
docs = reader.get_content()
```

就这么简单！系统会自动处理所有复杂情况。

