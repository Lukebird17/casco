# 🚨 当前问题及解决方案

## 📌 你遇到的错误

```
❌ API请求失败: 404 Client Error: Not Found for url: https://qianfan.baidubce.com/v2
```

## 🔍 问题原因

你使用的URL **不正确**：

| 项目 | 说明 |
|-----|------|
| ❌ **你当前使用的** | `https://qianfan.baidubce.com/v2` |
| 说明 | 这是**百度千帆大模型**的API地址 |
| ✅ **你需要的** | `https://xxx.com/layout-parsing` |
| 说明 | 这是**PaddleX PP-StructureV3**的OCR API地址 |

**结论**：你配置了错误的API地址，需要重新获取正确的PaddleX API。

---

## ✅ 解决方案

### 方案A：获取正确的PaddleX API（推荐）

#### 第1步：访问PaddleX官网

打开浏览器，访问：
- 🌐 https://www.paddlepaddle.org.cn/paddlex
- 🌐 https://paddlepaddle.github.io/PaddleX/

#### 第2步：注册并登录

- 使用百度账号登录
- 如果没有账号，先注册一个

#### 第3步：申请PP-StructureV3服务

在控制台中找到：
- **「文档解析」服务**，或
- **「PP-StructureV3」服务**，或
- **「OCR服务化部署」**

点击"开通"或"申请试用"。

#### 第4步：获取API配置

开通后，你会得到：

1. **API_URL** - 端点地址
   - 格式：`https://xxxx.com/layout-parsing`
   - **必须**以 `/layout-parsing` 结尾

2. **TOKEN** - 访问令牌
   - 一长串字符串
   - 需要保密

#### 第5步：配置环境变量

```bash
# 在终端中执行（替换为你实际获取的值）
export PADDLEOCR_API_URL="https://your-actual-api-url.com/layout-parsing"
export PADDLEOCR_API_TOKEN="your_actual_token_here"
```

#### 第6步：测试配置

```bash
# 运行测试脚本
python test_api_config.py
```

如果看到 `✅ 测试通过！`，说明配置正确。

#### 第7步：运行程序

```bash
python run_competition.py
```

---

### 方案B：使用本地模式（临时方案）

如果暂时无法获取API，可以先使用本地模式：

#### 第1步：清除错误的API配置

```bash
# 在终端中执行
unset PADDLEOCR_API_URL
unset PADDLEOCR_API_TOKEN
```

#### 第2步：直接运行程序

```bash
python run_competition.py
```

程序会自动检测到没有API配置，切换到本地模式。

#### ⚠️ 本地模式的限制

- ❌ 不支持复杂表格识别
- ❌ 不支持版面分析
- ❌ 功能受限
- ✅ 可以处理简单文本

---

## 📋 配置检查清单

使用这个清单确保你的配置正确：

- [ ] API_URL 已设置
- [ ] API_URL 包含 `/layout-parsing`
- [ ] API_URL **不是**千帆的URL（不包含 `qianfan.baidubce.com`）
- [ ] TOKEN 已设置
- [ ] TOKEN 不为空
- [ ] 已运行 `python test_api_config.py` 测试
- [ ] 测试通过

---

## 🔧 测试工具

我们提供了一个测试脚本来验证你的配置：

### 使用方法

```bash
# 1. 设置环境变量
export PADDLEOCR_API_URL="你的API地址"
export PADDLEOCR_API_TOKEN="你的TOKEN"

# 2. 运行测试
python test_api_config.py
```

### 测试内容

测试脚本会检查：
1. ✅ 环境变量是否已设置
2. ✅ URL格式是否正确
3. ✅ 是否使用了错误的千帆URL
4. ✅ API连接是否正常
5. ✅ 响应格式是否正确

---

## 💡 常见问题

### Q1: 我应该去哪里申请API？

A: 访问 https://www.paddlepaddle.org.cn/paddlex 申请PaddleX的PP-StructureV3服务。

### Q2: API费用如何？

A: 
- 通常有免费试用额度
- 具体费用请查看PaddleX官网定价
- 或者自己部署服务（免费但需要技术能力）

### Q3: 可以自己部署API吗？

A: 可以！如果你有服务器：

```bash
# 安装PaddleX
pip install paddlex

# 部署服务
paddlex --serve --pipeline PP-StructureV3 --device gpu:0
```

部署后：
- API_URL: `http://localhost:8080/layout-parsing`
- TOKEN: 你自己设置的令牌

详细教程：https://github.com/PaddlePaddle/PaddleX

### Q4: 本地模式和API模式有什么区别？

| 特性 | 本地模式 | API模式 |
|-----|---------|---------|
| 安装 | ⚠️ 需要本地环境 | ✅ 无需安装 |
| 稳定性 | ⚠️ 可能有兼容问题 | ✅ 稳定 |
| 功能 | ⚠️ 基础OCR | ✅ 完整功能 |
| 表格识别 | ❌ 不支持 | ✅ 支持 |
| 版面分析 | ❌ 不支持 | ✅ 支持 |
| 速度 | ⚠️ 较慢（CPU） | ✅ 快（云端GPU） |
| 费用 | ✅ 免费 | ⚠️ 可能收费 |
| 网络 | ✅ 离线可用 | ⚠️ 需要联网 |

### Q5: 如何查看当前使用的是哪个模式？

A: 运行程序时会显示：

```
🚀 初始化简化版OCR系统...
  🌐 使用在线API模式          # API模式
  📍 API地址: https://...
```

或

```
🚀 初始化简化版OCR系统...
  💻 使用本地PaddleOCR引擎    # 本地模式
  🔧 使用设备: CPU
```

---

## 📚 相关文档

- 📄 `使用在线API.md` - 完整的API使用指南
- 📄 `simple_ocr_system.py` - OCR系统实现
- 🧪 `test_api_config.py` - API配置测试工具

---

## 🎯 快速总结

### 现在该做什么？

**如果你想获得完整功能：**
1. 去 https://www.paddlepaddle.org.cn/paddlex 申请API
2. 获取正确的 API_URL 和 TOKEN
3. 运行 `python test_api_config.py` 测试
4. 运行 `python run_competition.py`

**如果你想快速开始（功能受限）：**
1. 运行 `unset PADDLEOCR_API_URL && unset PADDLEOCR_API_TOKEN`
2. 运行 `python run_competition.py`

---

## ✨ 总结

你的问题是使用了错误的API地址（千帆的URL），而不是PaddleX的URL。

**解决办法**：
- **方案A**：去PaddleX官网获取正确的API（功能完整，推荐）
- **方案B**：暂时使用本地模式（功能受限，可快速开始）

选择一个方案，然后执行对应的步骤即可！🚀




