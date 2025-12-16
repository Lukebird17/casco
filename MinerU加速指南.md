# MinerU 加速使用指南

## 一、快速配置（必做）

### 1. 配置HuggingFace镜像源

MinerU首次使用需要下载AI模型（约1-2GB），使用国内镜像可以大幅加速：

```bash
# 在终端执行
export HF_ENDPOINT=https://hf-mirror.com

# 永久生效（添加到配置文件）
echo 'export HF_ENDPOINT=https://hf-mirror.com' >> ~/.zshrc
source ~/.zshrc
```

### 2. 运行自动配置脚本

```bash
cd /Users/leon/Project/CS3602NLP/Proj2
chmod +x setup_mineru_acceleration.sh
./setup_mineru_acceleration.sh
```

这个脚本会自动：
- 配置HuggingFace镜像
- 创建MinerU配置文件
- 检测并启用GPU加速（如果可用）
- 初始化模型缓存

## 二、性能优化策略

### 1. 缓存机制（已自动启用）

框架已内置缓存功能：
- ✅ 首次处理文件时，结果会自动缓存
- ✅ 相同文件再次处理时，直接从缓存读取（速度提升10-100倍）
- ✅ 缓存目录：`.mineru_cache/`

### 2. GPU加速（如果有NVIDIA显卡）

检查是否支持GPU：
```bash
nvidia-smi
```

如果有GPU，编辑配置文件 `~/.magic-pdf.json`：
```json
{
    "device-mode": "cuda"
}
```

速度提升：CPU模式约30秒/页 → GPU模式约3秒/页

### 3. 批量处理优化

```python
from enhanced_ocr import EnhancedOCRProcessor

# 使用批量处理接口
processor = EnhancedOCRProcessor(use_cache=True)
results = processor.batch_process(file_list, output_base_dir)
```

### 4. 关闭不需要的功能

编辑 `~/.magic-pdf.json`：

```json
{
    "table-config": {
        "is_table_recog_enable": false,  // 不需要表格识别时关闭
        "max_time": 400
    },
    "formula-config": {
        "mfd_enable": false,  // 不需要公式检测时关闭
        "mfr_enable": false   // 不需要公式识别时关闭
    }
}
```

## 三、性能对比

| 场景 | 处理速度 | 说明 |
|------|---------|------|
| 首次处理（无缓存） | 30-60秒/页 | 取决于CPU/GPU |
| 缓存命中 | <0.1秒 | 直接读取缓存文件 |
| GPU加速 | 3-10秒/页 | 比CPU快5-10倍 |
| 关闭公式/表格识别 | 10-20秒/页 | 速度提升30-50% |

## 四、常见问题

### Q1: 首次运行很慢，一直在下载？
**A:** MinerU首次运行需要下载模型文件（1-2GB），配置HuggingFace镜像可以加速下载。

### Q2: 每次处理都很慢？
**A:** 检查缓存是否启用：
```python
processor = EnhancedOCRProcessor(use_cache=True)  # 确保use_cache=True
```

### Q3: 如何清理缓存？
**A:** 删除缓存目录：
```bash
rm -rf .mineru_cache/
```

### Q4: GPU加速没生效？
**A:** 检查：
1. 是否安装了CUDA版PyTorch
2. `~/.magic-pdf.json` 中 `device-mode` 是否为 `"cuda"`
3. 运行 `nvidia-smi` 确认GPU可用

## 五、实际使用示例

### 基础使用（自动缓存）
```python
from document_loader import DocumentLoader

loader = DocumentLoader()
documents = loader.load_document("data/test.pdf")  # 自动使用MinerU + 缓存
```

### 批量处理
```python
from enhanced_ocr import EnhancedOCRProcessor

processor = EnhancedOCRProcessor(use_cache=True)

# 批量处理多个文件
files = ["data/file1.pdf", "data/file2.pptx", "data/file3.docx"]
results = processor.batch_process(files)
```

### 查看处理统计
```python
# 查看缓存命中率
import os
cache_files = len(os.listdir('.mineru_cache'))
print(f"缓存文件数: {cache_files}")
```

## 六、性能监控

查看MinerU处理日志：
```bash
# MinerU会在终端输出详细日志
# 包括：处理进度、GPU内存使用、处理时间等
```

## 七、最佳实践

1. ✅ **首次使用前运行配置脚本**
2. ✅ **启用缓存（默认已启用）**
3. ✅ **有GPU优先使用GPU模式**
4. ✅ **批量处理时使用batch_process接口**
5. ✅ **定期清理不需要的缓存文件**

---

**注意事项：**
- 缓存基于文件内容hash，修改文件后会重新处理
- GPU模式需要显存≥6GB的NVIDIA显卡
- 首次处理较慢是正常现象，后续会很快

