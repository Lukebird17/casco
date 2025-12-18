# 统一PDF存储方案说明

## 🎯 核心策略

**所有PPTX/DOCX在上传时自动转换为PDF后保存**

---

## ✨ 方案优势

### 1. 统一存储格式
```
data/default/
├── lecture1.pdf          ← 原始PDF
├── slides.pdf            ← 从 slides.pptx 转换
├── document.pdf          ← 从 document.docx 转换
├── notes.txt             ← 保持原样
└── readme.md             ← 保持原样
```

### 2. 处理流程优化

#### 上传时（一次性转换）
```
用户上传 slides.pptx
    ↓
检测文件类型 (.pptx)
    ↓
LibreOffice转换为PDF
    ↓
保存 slides.pdf 到 data/default/
    ↓
向量化处理（MinerU）
```

#### 查询时（直接使用）
```
检索相关文档
    ↓
找到 slides.pdf
    ↓
直接显示（无需转换）
```

### 3. 性能提升
- ✅ 只转换一次（上传时）
- ✅ 查询时无需重复转换
- ✅ 文档查看器直接显示PDF
- ✅ 减少临时文件生成

### 4. 完整的OCR支持
- ✅ 所有文档统一用MinerU处理
- ✅ 提取图片和文字
- ✅ 高质量的向量化

---

## 📋 文件处理规则

| 上传类型 | 保存格式 | 处理方式 |
|---------|---------|---------|
| PDF     | PDF     | 直接保存 → MinerU |
| PPTX    | **PDF** | 转换 → 保存 → MinerU |
| DOCX    | **PDF** | 转换 → 保存 → MinerU |
| TXT     | TXT     | 直接保存 → 文本提取 |
| MD      | MD      | 直接保存 → 文本提取 |
| 图片    | 原格式  | 直接保存 → CLIP向量化 |

---

## 🔄 详细流程

### 上传PPTX文件

```python
# 1. 用户上传 presentation.pptx
files = [presentation.pptx]

# 2. 后端处理
for file in files:
    # 2.1 保存到临时目录
    temp_path = "/tmp/xxx/presentation.pptx"
    
    # 2.2 检测文件类型
    if file.endswith('.pptx'):
        # 2.3 转换为PDF
        print("检测到 PPTX 文件，转换为PDF...")
        pdf_path = convert_to_pdf(temp_path)
        
        # 2.4 保存PDF到data目录
        permanent_path = "data/default/presentation.pdf"  # 注意扩展名改为.pdf
        shutil.copy(pdf_path, permanent_path)
        
        print("✅ 已转换并保存为: presentation.pdf")
    
    # 3. 向量化处理（使用转换后的PDF）
    documents, images = loader.load_pdf("data/default/presentation.pdf")
    vector_store.add_documents(documents)
    image_store.add_images(images)
```

### 查看文档

```javascript
// 前端请求
GET /api/knowledge-bases/default/documents/presentation.pdf/raw

// 后端响应
// 直接返回PDF文件（无需转换）
return FileResponse("data/default/presentation.pdf")

// 浏览器
// 内嵌显示PDF
```

---

## 🎨 用户体验

### 上传时的反馈

```
📤 上传文件到知识库: default
   文件数量: 1

   📄 处理文件: my_slides.pptx
      检测到 PPTX 文件，转换为PDF...
      🔄 使用LibreOffice转换为PDF: my_slides.pptx
      ✅ 转换成功: my_slides.pdf
      ✅ 已转换并保存为: my_slides.pdf
         永久路径: /home/user/rag-agent/data/default/my_slides.pdf

   🔄 开始向量化处理...
   ✅ 添加了 45 个文本块
   ✅ 添加了 12 张图片
```

### 文件列表显示

前端会看到：
```
知识库文件 (3)
├── 📄 my_slides.pdf        (4.5 MB)  PDF
├── 📄 lecture.pdf          (2.1 MB)  PDF
└── 📄 notes.txt            (0.1 MB)  TXT
```

**注意**：用户看到的是 `my_slides.pdf`，而不是原始的 `my_slides.pptx`

---

## ⚠️ 注意事项

### 1. 文件名变化
```
上传: presentation.pptx
保存: presentation.pdf     ← 扩展名改变

上传: document.docx
保存: document.pdf          ← 扩展名改变
```

### 2. 文件冲突处理
```
# 如果已存在 slides.pdf
上传: slides.pptx
保存: slides_1734518400.pdf    ← 添加时间戳
```

### 3. 转换失败回退
```
上传: corrupted.pptx
    ↓
尝试转换为PDF
    ↓
转换失败 ❌
    ↓
保存原始PPTX
    ↓
使用基础解析器（仅文本）
```

### 4. 无LibreOffice的情况
```
上传: slides.pptx
    ↓
检查LibreOffice可用性
    ↓
不可用 ❌
    ↓
保存原始PPTX
    ↓
使用python-pptx提取文本
```

---

## 🧪 测试场景

### 场景1：上传PPTX（有LibreOffice）
```bash
1. 上传 test.pptx
2. 应该看到：
   ✅ 检测到 PPTX 文件，转换为PDF...
   ✅ 转换成功: test.pdf
   ✅ 已转换并保存为: test.pdf
3. 检查data/目录：
   ls data/default/
   # 应该看到 test.pdf（而不是test.pptx）
4. 打开文档查看器：
   # 应该列出 test.pdf
   # 点击后直接显示（无需转换）
```

### 场景2：上传DOCX（有LibreOffice）
```bash
1. 上传 report.docx
2. 应该看到：
   ✅ 检测到 DOCX 文件，转换为PDF...
   ✅ 转换成功: report.pdf
3. 检查data/目录：
   # 应该看到 report.pdf
```

### 场景3：上传PDF（无需转换）
```bash
1. 上传 paper.pdf
2. 应该看到：
   ✅ 保存: paper.pdf
3. 检查data/目录：
   # 应该看到 paper.pdf（保持原样）
```

### 场景4：文件名冲突
```bash
1. 上传 slides.pptx → 保存为 slides.pdf
2. 再次上传 slides.pptx
3. 应该看到：
   ⚠️  PDF已存在，重命名为: slides_1734518400.pdf
4. 检查data/目录：
   # 应该看到 slides.pdf 和 slides_1734518400.pdf
```

---

## 💡 最佳实践

### 1. 推荐的文件组织
```
data/default/
├── lectures/
│   ├── week1.pdf          ← 从week1.pptx转换
│   ├── week2.pdf          ← 从week2.pptx转换
│   └── notes.txt
├── papers/
│   ├── paper1.pdf         ← 原始PDF
│   └── paper2.pdf         ← 原始PDF
└── docs/
    ├── manual.pdf         ← 从manual.docx转换
    └── readme.md
```

### 2. 命名建议
- 使用有意义的文件名
- 避免特殊字符
- 中文文件名完全支持
- 相同内容不同格式可以用相同名字（反正会转成PDF）

### 3. 上传策略
```
优先级：
1. 直接上传PDF（最快）
2. 上传PPTX/DOCX（自动转换）
3. 本地转换后上传（如果担心服务器性能）
```

---

## 📊 性能对比

### 旧方案（每次转换）
```
用户查询 → 检索到slides.pptx → 转换为PDF → MinerU处理 → 返回结果
          |__________________ 5-30秒 ______________________|

文档查看 → 点击slides.pptx → 转换为PDF → 显示
          |_________ 5-30秒 __________|
```

### 新方案（一次转换）
```
上传时:
  上传slides.pptx → 转换为PDF → 保存slides.pdf
                    |__ 5-30秒 __|
                    (只执行一次)

查询时:
  用户查询 → 检索到slides.pdf → 直接使用向量 → 返回结果
            |____________ <1秒 ______________|

查看时:
  点击slides.pdf → 直接显示
  |_____ <1秒 _____|
```

**性能提升**：
- 查询速度：无需等待转换
- 查看速度：即时显示
- 系统负载：减少重复转换

---

## 🔧 技术实现

### 核心修改

**`backend/api.py` - `upload_to_knowledge_base()`**:
```python
# 上传时检测文件类型
file_ext = os.path.splitext(file.filename)[1].lower()

if file_ext in ['.pptx', '.docx']:
    # 转换为PDF
    pdf_path = loader.convert_to_pdf(temp_path)
    
    # 保存PDF（扩展名改为.pdf）
    final_filename = f"{base_name}.pdf"
    permanent_path = os.path.join(kb_data_dir, final_filename)
    shutil.copy2(pdf_path, permanent_path)
else:
    # 其他文件直接保存
    permanent_path = os.path.join(kb_data_dir, file.filename)
    shutil.copy(content, permanent_path)
```

**`document_loader.py` - `convert_to_pdf()`**:
```python
def convert_to_pdf(self, file_path: str) -> Optional[str]:
    """使用LibreOffice转换PPTX/DOCX为PDF"""
    # 检查LibreOffice可用性
    if not self.check_libreoffice():
        return None
    
    # 转换
    cmd = ['libreoffice', '--headless', '--convert-to', 'pdf', ...]
    result = subprocess.run(cmd, ...)
    
    # 返回PDF路径
    return pdf_path
```

---

## ✅ 总结

### 优点
1. ✅ 统一存储格式（全部PDF）
2. ✅ 上传时一次转换
3. ✅ 查询和查看无需等待
4. ✅ 完整的OCR和图片提取
5. ✅ 简化文档管理

### 缺点
1. ⚠️ 上传时需要等待转换（5-30秒）
2. ⚠️ 文件名扩展名会改变（.pptx → .pdf）
3. ⚠️ 需要LibreOffice支持（但有回退机制）

### 结论
**这是最优方案**：
- 用户体验好（查询和查看快）
- 系统负载低（只转换一次）
- 管理简单（统一格式）
- 质量高（完整OCR）

---

## 🚀 立即使用

```bash
# 1. 安装LibreOffice（如果还没有）
./安装LibreOffice_用户版.sh

# 2. 重启后端
./start_backend.sh

# 3. 上传文件
# - PPTX会自动转换为PDF并保存
# - DOCX会自动转换为PDF并保存
# - PDF直接保存
# - 所有文件都获得完整的OCR支持

# 4. 享受快速的查询和查看体验！
```

现在就试试上传一个PPTX文件吧！🎉



