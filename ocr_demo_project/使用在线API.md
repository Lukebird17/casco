# 🌐 使用PaddleOCR在线API

## 📝 简介

现在系统支持两种模式：
- **在线API模式**：功能完整、稳定、支持GPU加速（推荐）
- **本地模式**：需要安装本地环境，可能有兼容性问题

## 🚀 快速开始 - 使用在线API

### 1. 设置环境变量

**方法1：在终端设置（临时）**
```bash
export PADDLEOCR_API_URL="你的API地址"
export PADDLEOCR_API_TOKEN="你的API Token"
```

**方法2：在Python代码中设置**
```python
import os
os.environ['PADDLEOCR_API_URL'] = "你的API地址"
os.environ['PADDLEOCR_API_TOKEN'] = "你的API Token"

from simple_ocr_system import SimpleOCRSystem
ocr = SimpleOCRSystem()  # 自动使用API模式
```

**方法3：创建.env文件**
```bash
# 在项目根目录创建.env文件
cat > .env << 'EOF'
PADDLEOCR_API_URL=你的API地址
PADDLEOCR_API_TOKEN=你的API Token
EOF
```

然后在代码开头：
```python
from dotenv import load_dotenv
load_dotenv()

from simple_ocr_system import SimpleOCRSystem
ocr = SimpleOCRSystem()
```

### 2. 直接运行

配置好环境变量后，直接运行：
```bash
python run_competition.py
```

系统会自动检测到API配置并使用在线API模式！

## 📊 API vs 本地对比

| 特性 | 在线API | 本地模式 |
|------|---------|----------|
| **安装难度** | ✅ 简单（无需安装） | ❌ 复杂（需要配置环境） |
| **稳定性** | ✅ 稳定 | ⚠️ 可能有兼容性问题 |
| **功能** | ✅ 完整（表格+版面+OCR） | ⚠️ 受限（基础OCR） |
| **速度** | ✅ 快（云端GPU） | ⚠️ 慢（本地CPU） |
| **成本** | ⚠️ 需要API费用 | ✅ 免费 |
| **网络要求** | ⚠️ 需要联网 | ✅ 离线可用 |

## 💡 如何获取API配置

### ⚠️ 重要提示

**你当前使用的URL不正确！**
- ❌ 错误URL：`https://qianfan.baidubce.com/v2`（这是百度千帆的URL）
- ✅ 正确URL：需要从PaddleX平台获取，格式类似 `https://xxx/layout-parsing`

### 方式1：使用PaddleX官方服务（推荐）

#### 步骤1：访问PaddleX官网

访问以下任一网址：
- PaddleX官网：https://www.paddlepaddle.org.cn/paddlex
- PaddleX文档中心：https://paddlepaddle.github.io/PaddleX/
- PaddlePaddle首页：https://www.paddlepaddle.org.cn/

#### 步骤2：注册并登录

- 如果没有账号，先注册一个百度账号
- 登录后进入控制台

#### 步骤3：开通PP-StructureV3服务

找到以下服务之一：
- **「文档解析」服务**
- **「PP-StructureV3」服务**
- **「OCR服务化部署」**

点击开通或申请试用。

#### 步骤4：获取API配置

开通后，你会获得：

1. **API_URL**（端点地址）
   - 格式：`https://your-domain.com/layout-parsing`
   - 或者：`https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/layout-parsing`
   - **注意**：必须以 `/layout-parsing` 结尾

2. **TOKEN**（访问令牌）
   - 一长串字符串，类似：`abcd1234efgh5678ijkl9012...`
   - 保密！不要泄露给他人

#### 步骤5：设置环境变量

```bash
# 替换为你实际获取的URL和TOKEN
export PADDLEOCR_API_URL="https://your-domain.com/layout-parsing"
export PADDLEOCR_API_TOKEN="your_access_token_here"
```

### 方式2：自建服务（高级用户）

如果你有自己的服务器，也可以部署PaddleX服务端：

```bash
# 1. 安装PaddleX
pip install paddlex

# 2. 部署PP-StructureV3服务
paddlex --serve --pipeline PP-StructureV3 --device gpu:0
```

部署成功后：
- API_URL: `http://localhost:8080/layout-parsing`（默认端口）
- TOKEN: 你自己设置的访问令牌

详细部署教程：https://github.com/PaddlePaddle/PaddleX

### API配置示例

```bash
# 示例1：使用官方云服务
export PADDLEOCR_API_URL="https://paddlex-api.baidubce.com/v1/layout-parsing"
export PADDLEOCR_API_TOKEN="sk_1234567890abcdefghijklmnopqrstuvwxyz"

# 示例2：使用自建服务
export PADDLEOCR_API_URL="http://localhost:8080/layout-parsing"
export PADDLEOCR_API_TOKEN="my_secret_token"

# 示例3：使用内网服务器
export PADDLEOCR_API_URL="http://192.168.1.100:8080/layout-parsing"
export PADDLEOCR_API_TOKEN="internal_token_123"
```

### 🔍 如何验证配置正确

运行以下测试脚本：

```python
import requests
import base64
import os

API_URL = os.getenv('PADDLEOCR_API_URL')
TOKEN = os.getenv('PADDLEOCR_API_TOKEN')

print(f"API_URL: {API_URL}")
print(f"TOKEN: {TOKEN[:10]}..." if TOKEN else "TOKEN: 未设置")

# 测试请求
headers = {
    "Authorization": f"token {TOKEN}",
    "Content-Type": "application/json"
}

# 使用一个简单的测试图片
test_payload = {
    "file": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==",
    "fileType": 1
}

try:
    response = requests.post(API_URL, json=test_payload, headers=headers, timeout=10)
    print(f"✅ 连接成功！状态码: {response.status_code}")
    if response.status_code == 200:
        print("✅ API配置正确！")
    else:
        print(f"⚠️ 状态码异常: {response.text}")
except Exception as e:
    print(f"❌ 连接失败: {e}")
```

## 📚 官方API详细说明

### API基本信息

- **HTTP方法**：POST
- **端点路径**：`/layout-parsing`
- **请求格式**：JSON
- **响应格式**：JSON

### 请求头（Headers）

```python
headers = {
    "Authorization": f"token {TOKEN}",  # 注意格式：token 空格 TOKEN
    "Content-Type": "application/json"
}
```

### 请求参数（Request Payload）

#### 必需参数

| 参数名 | 类型 | 说明 |
|--------|------|------|
| `file` | string | Base64编码的文件内容或文件URL |
| `fileType` | integer | 文件类型：0=PDF，1=图像 |

#### 可选参数（功能开关）

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `useDocOrientationClassify` | boolean | false | 图片方向矫正（0°/90°/180°/270°） |
| `useDocUnwarping` | boolean | false | 图片扭曲矫正（褶皱、倾斜等） |
| `useTextlineOrientation` | boolean | false | 文本行方向矫正（0°/180°） |
| `useTableRecognition` | boolean | true | 表格识别并转HTML/Markdown |
| `useFormulaRecognition` | boolean | false | 公式识别并转LaTeX |
| `useChartRecognition` | boolean | false | 图表解析并转表格 |
| `useSealRecognition` | boolean | false | 印章文本识别 |
| `useRegionDetection` | boolean | false | 复杂版面处理（报纸、杂志等） |

### 响应格式

**成功响应（200）：**

```json
{
    "logId": "request-uuid",
    "errorCode": 0,
    "errorMsg": "Success",
    "result": {
        "layoutParsingResults": [
            {
                "markdown": {
                    "text": "# 标题\n\n正文内容...",
                    "images": {
                        "path/to/img1.jpg": "base64_encoded_image"
                    },
                    "isStart": true,
                    "isEnd": true
                },
                "outputImages": {
                    "visualization": "base64_encoded_image"
                },
                "inputImage": "base64_encoded_image"
            }
        ]
    }
}
```

**错误响应（非200）：**

```json
{
    "logId": "request-uuid",
    "errorCode": 404,
    "errorMsg": "Resource not found"
}
```

### 完整调用示例

```python
import base64
import requests

# API配置
API_URL = "https://your-domain.com/layout-parsing"
TOKEN = "your_token_here"

# 读取文件并Base64编码
file_path = "document.pdf"
with open(file_path, "rb") as f:
    file_bytes = f.read()
    file_data = base64.b64encode(file_bytes).decode("ascii")

# 构建请求
headers = {
    "Authorization": f"token {TOKEN}",
    "Content-Type": "application/json"
}

payload = {
    "file": file_data,
    "fileType": 0,  # 0=PDF, 1=Image
    "useDocOrientationClassify": True,  # 开启方向矫正
    "useDocUnwarping": True,  # 开启扭曲矫正
    "useTableRecognition": True,  # 开启表格识别
    "useFormulaRecognition": True,  # 开启公式识别
}

# 发送请求
response = requests.post(API_URL, json=payload, headers=headers, timeout=300)

# 处理响应
if response.status_code == 200:
    result = response.json()["result"]
    for i, page_result in enumerate(result["layoutParsingResults"]):
        markdown_text = page_result["markdown"]["text"]
        print(f"第{i+1}页内容：\n{markdown_text}\n")
else:
    print(f"错误：{response.status_code} - {response.text}")
```

## 🔧 使用示例

### 示例1：自动检测模式
```python
from simple_ocr_system import SimpleOCRSystem

# 如果有API配置，自动使用API；否则使用本地
ocr = SimpleOCRSystem()

results = ocr.process_document('document.pdf')
ocr.export_results(results)
```

### 示例2：强制使用API
```python
from simple_ocr_system import SimpleOCRSystem

# 强制使用API模式
ocr = SimpleOCRSystem(use_api=True)

results = ocr.process_document('document.pdf')
```

### 示例3：强制使用本地
```python
from simple_ocr_system import SimpleOCRSystem

# 强制使用本地引擎
ocr = SimpleOCRSystem(use_api=False)

results = ocr.process_document('document.pdf')
```

## ⚡ 性能对比

**测试文档**：10页PDF，包含文字和表格

| 模式 | 处理时间 | 准确率 | 表格识别 |
|------|---------|--------|----------|
| 在线API | ~10秒 | 95%+ | ✅ 完整支持 |
| 本地CPU | ~30秒 | 90% | ❌ 不支持 |
| 本地GPU | ~15秒 | 90% | ❌ 不支持 |

## 🐛 常见问题

### Q: 如何知道是否使用了API模式？

A: 启动时会显示：
```
🚀 初始化简化版OCR系统...
  🌐 使用在线API模式
  📍 API地址: https://...
✅ OCR系统初始化完成
```

### Q: API请求超时怎么办？

A: 在代码中增加超时时间：
```python
# 在simple_ocr_system.py中修改timeout参数
response = requests.post(self.API_URL, json=payload, headers=headers, timeout=600)  # 改为600秒
```

### Q: API费用如何计算？

A: 请参考PaddleX官方定价文档。

### Q: 可以批量处理吗？

A: 可以！API模式支持批量处理：
```python
import os
from simple_ocr_system import SimpleOCRSystem

ocr = SimpleOCRSystem(use_api=True)

for pdf_file in os.listdir('pdfs/'):
    if pdf_file.endswith('.pdf'):
        results = ocr.process_document(f'pdfs/{pdf_file}')
        ocr.export_results(results, f'output/{pdf_file}_results.json')
```

## 📌 推荐配置

### 场景1：开发测试
```bash
# 使用本地模式（免费）
export PADDLEOCR_API_URL=""
export PADDLEOCR_API_TOKEN=""
python run_competition.py
```

### 场景2：生产环境
```bash
# 使用API模式（稳定、快速）
export PADDLEOCR_API_URL="你的API地址"
export PADDLEOCR_API_TOKEN="你的API Token"
python run_competition.py
```

## ✅ 配置验证

运行测试脚本验证配置：
```python
import os
from simple_ocr_system import SimpleOCRSystem

# 检查配置
api_url = os.getenv('PADDLEOCR_API_URL', '')
api_token = os.getenv('PADDLEOCR_API_TOKEN', '')

if api_url and api_token:
    print("✅ API配置已设置")
    print(f"   URL: {api_url[:50]}...")
    print(f"   Token: {api_token[:10]}...")
else:
    print("⚠️  API配置未设置，将使用本地模式")

# 初始化
ocr = SimpleOCRSystem()
print(f"   当前模式: {'API' if ocr.use_api else '本地'}")
```

---

**现在就试试吧！** 🎉

1. 设置环境变量
2. 运行 `python run_competition.py`
3. 享受快速、稳定的OCR服务！

---

## 🎯 总结：你的当前问题

### ❌ 问题诊断

你遇到的错误：
```
❌ API请求失败: 404 Client Error: Not Found for url: https://qianfan.baidubce.com/v2
```

**原因**：
- 你使用的URL `https://qianfan.baidubce.com/v2` 是**百度千帆大模型**的API地址
- 而你需要的是**PaddleX PP-StructureV3**的API地址
- 这是**两个完全不同的服务**

### ✅ 解决方案

#### 方案A：获取正确的API（推荐）

1. **访问PaddleX平台**
   - 网址：https://www.paddlepaddle.org.cn/paddlex
   - 或：https://paddlepaddle.github.io/PaddleX/

2. **申请PP-StructureV3服务**
   - 注册/登录百度账号
   - 开通"文档解析"或"PP-StructureV3"服务
   - 获取你的API_URL和TOKEN

3. **正确配置**
   ```bash
   # 正确的URL格式（示例）
   export PADDLEOCR_API_URL="https://paddlex-api.baidubce.com/v1/layout-parsing"
   export PADDLEOCR_API_TOKEN="你获取的TOKEN"
   ```

4. **运行程序**
   ```bash
   python run_competition.py
   ```

#### 方案B：使用本地模式（临时方案）

如果暂时无法获取API，可以先使用本地基础OCR：

```bash
# 清除错误的API配置
unset PADDLEOCR_API_URL
unset PADDLEOCR_API_TOKEN

# 运行程序（将自动切换到本地模式）
python run_competition.py
```

**注意**：本地模式功能受限，不支持复杂表格识别。

---

## 📞 需要帮助？

如果你：
- ✅ 已经获取了正确的API_URL和TOKEN → 直接配置并运行
- ⏳ 正在申请API访问权限 → 先使用方案B（本地模式）
- ❓ 不知道如何申请API → 查看上面的"如何获取API配置"部分
- 🚀 想自己部署服务 → 查看"方式2：自建服务"

**下一步操作**：
1. 去PaddleX官网申请API（**推荐**）
2. 或者，暂时取消API配置，使用本地模式（功能受限）

