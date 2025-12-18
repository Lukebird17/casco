# LibreOffice 集成完成说明

## ✅ 已完成的工作

### 1. LibreOffice 配置
- **路径**: `/home/honglianglu/hdd/my_libreoffice/extracted_libreoffice/opt/libreoffice25.8/program/soffice`
- **版本**: LibreOffice 25.8.3.2
- **状态**: ✅ 已验证可用

### 2. 代码集成

#### `config.py`
```python
LIBREOFFICE_PATH = "/home/honglianglu/hdd/my_libreoffice/extracted_libreoffice/opt/libreoffice25.8/program/soffice"
```

#### `document_loader.py`
- ✅ `check_libreoffice()` - 优先使用配置的LibreOffice路径
- ✅ `convert_to_pdf()` - 使用配置的路径进行转换
- ✅ `load_pptx()` - 转换为PDF后用MinerU处理
- ✅ `load_docx()` - 转换为PDF后用MinerU处理

#### `backend/api.py`
- ✅ `upload_to_knowledge_base()` - 自动检测PPTX/DOCX并转换为PDF
- ✅ 转换后的PDF保存到 `data/{kb_id}/`
- ✅ 向量化使用转换后的PDF

### 3. 测试结果

#### 测试1: PPTX 转换
```
输入: 2.3 中文分词与CRF.pptx (7.72 MB)
输出: 2.3 中文分词与CRF.pdf (4.58 MB)
状态: ✅ 成功
```

#### 测试2: DOCX 转换
```
输入: 自然语言处理Q.docx (0.54 MB)
输出: 自然语言处理Q.pdf (0.39 MB)
状态: ✅ 成功
```

#### 测试3: 完整 Pipeline
```
流程: PPTX → PDF → MinerU → 向量化
结果:
  - 文本块: 206
  - 图片: 14
  - 保存位置: data/test_upload/2.3 中文分词与CRF.pdf
状态: ✅ 成功
```

---

## 🔄 工作流程

### 用户上传 PPTX/DOCX 时

```
1. 用户在UI上传 presentation.pptx
   ↓
2. 后端接收文件
   ↓
3. 检测文件类型 (.pptx)
   ↓
4. 使用 LibreOffice 转换为 PDF
   /home/honglianglu/hdd/my_libreoffice/.../soffice --headless --convert-to pdf
   ↓
5. 转换成功 → presentation.pdf (4.6 MB)
   ↓
6. 保存 PDF 到 data/{kb_id}/presentation.pdf
   ↓
7. 使用 MinerU 处理 PDF
   - 提取文字和布局
   - 提取图片
   - 生成 Markdown
   ↓
8. 向量化处理
   - 文本块 → 文本向量库
   - 图片 → CLIP 向量库
   ↓
9. 完成！✅
```

### 用户查询时

```
1. 用户提问
   ↓
2. 检索向量库
   ↓
3. 找到相关内容
   - 来自 presentation.pdf 的文本块
   - 来自 presentation.pdf 的图片
   ↓
4. 生成答案（包含引用）
   ↓
5. 文档查看器显示原始 PDF（无需转换）
```

---

## 📊 性能数据

### PPTX 处理（2.3 中文分词与CRF.pptx）

| 步骤 | 时间 | 输出 |
|------|------|------|
| 1. 上传 | <1秒 | 7.72 MB |
| 2. 转换为PDF | ~5秒 | 4.58 MB |
| 3. MinerU处理 | ~2分钟 | 206文本块, 14图片 |
| 4. 向量化 | ~15秒 | 完成 |
| **总计** | **~2.5分钟** | **✅** |

### 对比：直接上传 PDF

| 步骤 | 时间 | 输出 |
|------|------|------|
| 1. 上传 | <1秒 | 4.58 MB |
| 2. MinerU处理 | ~2分钟 | 206文本块, 14图片 |
| 3. 向量化 | ~15秒 | 完成 |
| **总计** | **~2.25分钟** | **✅** |

**结论**: PPTX转换仅增加~5秒，完全可接受！

---

## 🎯 优势

### 1. 统一格式
- **之前**: data/ 里有 .pptx, .docx, .pdf 多种格式
- **现在**: data/ 里统一都是 .pdf 格式
- **好处**: 管理简单，处理统一

### 2. 完整 OCR
- **之前**: python-pptx 只能提取文本
- **现在**: LibreOffice转PDF + MinerU = 完整OCR + 图片提取
- **好处**: 更准确的内容提取

### 3. 一次转换
- **之前**: 每次查询/查看都可能需要转换
- **现在**: 上传时转换一次，永久使用
- **好处**: 查询和查看都很快

### 4. 用户体验
- **用户**: 上传PPTX/DOCX，和上传PDF一样简单
- **系统**: 自动转换，用户无感知
- **结果**: 获得最佳的OCR效果

---

## 🚀 使用方法

### 重启后端

```bash
cd /home/honglianglu/hdd/rag-agent
./start_backend.sh
```

### 测试上传

1. 打开浏览器：`http://localhost:5173`

2. 点击左侧 **数据库图标**

3. 选择一个知识库（如 "default"）

4. 点击 **上传文件**

5. 选择一个 PPTX 或 DOCX 文件

6. 观察后端日志：

```
📤 上传文件到知识库: default
   文件数量: 1

   📄 处理文件: presentation.pptx
      检测到 PPTX 文件，转换为PDF...
      ✅ 使用配置的LibreOffice: /home/honglianglu/hdd/my_libreoffice/.../soffice
      🔄 使用LibreOffice转换为PDF: presentation.pptx
      ✅ 转换成功: presentation.pdf
      ✅ 已转换并保存为: presentation.pdf
         永久路径: /home/honglianglu/hdd/rag-agent/data/default/presentation.pdf

   🔄 开始向量化处理...
   ✅ 添加了 206 个文本块
   ✅ 添加了 14 张图片
```

7. 检查 `data/default/` 目录：

```bash
ls -lh data/default/
# 应该看到 presentation.pdf（而不是 presentation.pptx）
```

8. 在 **文档查看器** 中打开，应该立即显示PDF！

---

## 🐛 故障排除

### 问题1: 转换失败

**症状**:
```
⚠️ LibreOffice转换失败，使用基础解析器
```

**检查**:
```bash
# 1. 验证LibreOffice可用
/home/honglianglu/hdd/my_libreoffice/extracted_libreoffice/opt/libreoffice25.8/program/soffice --version

# 2. 手动测试转换
cd /tmp
/home/honglianglu/hdd/my_libreoffice/extracted_libreoffice/opt/libreoffice25.8/program/soffice --headless --convert-to pdf test.pptx
```

### 问题2: 找不到转换后的文件

**检查**:
```bash
# 查看data目录
ls -la data/default/

# 应该看到 .pdf 文件，而不是 .pptx
```

### 问题3: MinerU 处理失败

**检查后端日志**:
```
# 应该看到 MinerU 的处理过程
2025-12-18 20:53:40.953 | INFO | Batch 1/1: 123 pages/123 pages
```

---

## 📁 文件位置总结

### LibreOffice
```
/home/honglianglu/hdd/my_libreoffice/
├── LibreOffice_25.8.3.2_Linux_x86-64_deb/    (原始安装包)
└── extracted_libreoffice/                     (提取后的程序)
    └── opt/
        └── libreoffice25.8/
            └── program/
                └── soffice                    ← 可执行文件
```

### 数据目录（新结构）
```
/home/honglianglu/hdd/rag-agent/
├── data/
│   ├── default/
│   │   ├── file1.pdf          ← 原始PDF
│   │   ├── slides.pdf         ← 从slides.pptx转换
│   │   └── document.pdf       ← 从document.docx转换
│   └── test_upload/
│       └── 2.3 中文分词与CRF.pdf  ← 测试文件
│
├── vector_db/
│   ├── default/
│   │   └── chroma.sqlite3
│   └── test_upload/
│       └── chroma.sqlite3
│
└── config.py                   ← LibreOffice路径配置
```

---

## ✅ 功能检查清单

测试完成后，确认以下都正常：

- [x] LibreOffice 可用（版本 25.8.3.2）
- [x] PPTX 可以转换为 PDF
- [x] DOCX 可以转换为 PDF
- [x] 转换后的 PDF 保存到正确位置
- [x] MinerU 可以处理转换后的 PDF
- [x] 文本和图片都能正确提取
- [x] 向量化正常工作
- [x] 完整 pipeline 测试通过

---

## 🎉 总结

### 核心改进
1. ✅ 集成了 LibreOffice 25.8 (便携版)
2. ✅ 实现了 PPTX/DOCX → PDF 自动转换
3. ✅ 统一了数据格式（全部 PDF）
4. ✅ 完整的 OCR 和图片提取
5. ✅ 一次转换，永久使用

### 用户体验
- **上传**: 和以前一样简单，系统自动转换
- **查询**: 更快，无需等待转换
- **查看**: 立即显示，无需下载
- **质量**: 完整的 OCR + 图片支持

### 性能
- **转换时间**: ~5秒（PPTX/DOCX → PDF）
- **处理时间**: ~2分钟（MinerU OCR）
- **总时间**: ~2.5分钟（可接受）

---

## 🚀 现在可以使用了！

```bash
# 重启后端
./start_backend.sh

# 在浏览器中
# 1. 打开 http://localhost:5173
# 2. 上传 PPTX/DOCX 文件
# 3. 系统自动转换为 PDF
# 4. 完整的 OCR 处理
# 5. 开始提问！
```

**享受完整的 PPTX/DOCX 支持！** 🎉



