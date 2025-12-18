# LibreOffice 安装指南

## 🎯 为什么需要LibreOffice？

LibreOffice用于将PPTX/DOCX自动转换为PDF，从而：
- ✅ 获得完整的OCR文字提取
- ✅ 提取图片和图表
- ✅ 保持文档格式和布局
- ✅ 统一存储为PDF格式

**新功能**：上传PPTX/DOCX时会自动转换为PDF并保存！

---

## 📋 三种安装方式

### 方式1：用户目录安装（推荐，无需sudo）

**适用于**：没有sudo权限的用户

**步骤**：
```bash
cd /home/honglianglu/hdd/rag-agent
./安装LibreOffice_用户版.sh
```

**安装位置**：
- 程序：`~/.local/libreoffice/`
- 链接：`~/.local/bin/libreoffice`

**使用**：
```bash
# 方式1：临时生效（当前终端）
export PATH="$HOME/.local/bin:$PATH"

# 方式2：永久生效（重新加载配置）
source ~/.bashrc

# 方式3：重新打开终端（自动生效）
```

**测试**：
```bash
libreoffice --version
```

**优点**：
- ✅ 无需sudo权限
- ✅ 不影响系统
- ✅ 可以随时删除

**缺点**：
- ⚠️ 需要下载约300MB
- ⚠️ 首次安装较慢（5-10分钟）

---

### 方式2：系统安装（需要sudo）

**适用于**：有sudo权限的用户

**步骤**：
```bash
cd /home/honglianglu/hdd/rag-agent
./安装LibreOffice.sh
```

**或手动安装**：
```bash
sudo apt-get update
sudo apt-get install -y libreoffice-writer libreoffice-impress
```

**优点**：
- ✅ 安装简单快速
- ✅ 系统级别，所有用户可用
- ✅ 包管理器自动更新

**缺点**：
- ❌ 需要sudo权限

---

### 方式3：不安装LibreOffice

**适用于**：
- 只处理PDF文件
- 或者可以手动转换PPTX/DOCX

**工作模式**：
```
上传PPTX/DOCX：
  → 检测到无LibreOffice
  → 保存原始文件
  → 使用基础解析器（仅文本）
  → 无法提取图片 ❌
```

**替代方案**：
1. 手动转换为PDF后上传
2. 使用在线转换工具
3. 在本地电脑转换

**优点**：
- ✅ 无需安装任何东西
- ✅ 系统资源占用少

**缺点**：
- ❌ PPTX/DOCX只能提取文本
- ❌ 无法处理图片和图表

---

## 🔍 功能对比

### 有LibreOffice
```
上传: presentation.pptx
  ↓
自动转换为PDF
  ↓
保存: presentation.pdf
  ↓
MinerU处理:
  - 提取文字 ✅
  - 提取图片 ✅
  - OCR识别 ✅
  - 保持布局 ✅
```

### 无LibreOffice
```
上传: presentation.pptx
  ↓
保存: presentation.pptx
  ↓
python-pptx处理:
  - 提取文字 ✅
  - 提取图片 ❌
  - OCR识别 ❌
  - 保持布局 ❌
```

---

## 🧪 验证安装

### 检查LibreOffice是否可用

```bash
# 方法1：直接调用
libreoffice --version

# 方法2：检查命令
which libreoffice

# 方法3：测试转换
cd /tmp
echo "测试" > test.txt
libreoffice --headless --convert-to pdf test.txt
ls -lh test.pdf  # 应该生成test.pdf
```

### 后端日志确认

启动后端时，应该看到：
```bash
./start_backend.sh

# 日志中应该有：
✅ MinerU 已安装并可用
✅ LibreOffice 可用
```

### 上传测试

```bash
# 上传一个PPTX文件
# 应该看到：
📄 处理文件: test.pptx
   检测到 PPTX 文件，转换为PDF...
   🔄 使用LibreOffice转换为PDF: test.pptx
   ✅ 转换成功: test.pdf
   ✅ 已转换并保存为: test.pdf
```

---

## 🐛 故障排除

### 问题1：找不到libreoffice命令

**症状**：
```bash
$ libreoffice --version
bash: libreoffice: command not found
```

**解决方案（用户安装）**：
```bash
# 临时添加到PATH
export PATH="$HOME/.local/bin:$PATH"

# 或使用完整路径
$HOME/.local/bin/libreoffice --version

# 或重新加载配置
source ~/.bashrc
```

**解决方案（系统安装）**：
```bash
# 检查是否安装
dpkg -l | grep libreoffice

# 如果没有，重新安装
sudo apt-get install libreoffice-writer libreoffice-impress
```

---

### 问题2：转换失败

**症状**：
```
⚠️ LibreOffice转换失败，使用基础解析器
```

**可能原因**：
1. LibreOffice未正确安装
2. 文件损坏
3. 不支持的文件格式
4. 权限问题

**调试**：
```bash
# 手动测试转换
libreoffice --headless --convert-to pdf your_file.pptx

# 查看错误信息
echo $?  # 应该返回0（成功）
```

---

### 问题3：用户安装后PATH未生效

**症状**：
```bash
$ libreoffice --version
bash: libreoffice: command not found

$ $HOME/.local/bin/libreoffice --version
LibreOffice 24.2.7.2  # 这个可以
```

**解决方案**：
```bash
# 1. 检查.bashrc是否有配置
cat ~/.bashrc | grep "\.local/bin"

# 2. 如果没有，手动添加
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc

# 3. 重新加载
source ~/.bashrc

# 4. 或者重新登录终端
```

---

### 问题4：下载速度慢

**症状**：
```
1️⃣ 下载 LibreOffice 24.2.7...
   这可能需要几分钟，请耐心等待...
   [卡住很久]
```

**解决方案**：

**方案A：使用镜像**（需要修改脚本）
```bash
# 编辑安装脚本
nano 安装LibreOffice_用户版.sh

# 替换下载URL为国内镜像
# 清华镜像：https://mirrors.tuna.tsinghua.edu.cn/libreoffice/...
# 中科大镜像：https://mirrors.ustc.edu.cn/libreoffice/...
```

**方案B：手动下载**
```bash
# 1. 手动下载到本地
wget https://download.documentfoundation.org/libreoffice/stable/24.2.7/rpm/x86_64/LibreOffice_24.2.7_Linux_x86-64_rpm.tar.gz

# 2. 修改脚本跳过下载步骤
# 3. 直接解压和安装
```

**方案C：使用代理**
```bash
# 如果有代理
export http_proxy=http://proxy:port
export https_proxy=http://proxy:port

# 然后运行安装脚本
./安装LibreOffice_用户版.sh
```

---

## 📊 推荐配置

### 最佳体验（推荐）
```
✅ 安装LibreOffice（用户版或系统版）
✅ 直接上传PPTX/DOCX
✅ 自动转换为PDF
✅ 完整的OCR和图片提取
```

### 最小配置
```
❌ 不安装LibreOffice
✅ 手动转换PPTX/DOCX为PDF
✅ 上传PDF文件
✅ 完整的OCR和图片提取
```

### 折中方案
```
❌ 不安装LibreOffice
⚠️ 直接上传PPTX/DOCX
⚠️ 仅提取文本（无图片）
```

---

## ✅ 安装成功检查清单

完成安装后，确认以下都正常：

- [ ] `libreoffice --version` 能显示版本信息
- [ ] 后端启动时显示 "LibreOffice 可用"
- [ ] 上传PPTX文件能看到 "转换为PDF" 的日志
- [ ] `data/default/` 目录里保存的是PDF文件
- [ ] 文档查看器能正常显示转换后的PDF
- [ ] 查询时能检索到PPTX中的内容和图片

---

## 🚀 快速开始

### 推荐流程（用户安装）

```bash
# 1. 安装LibreOffice到用户目录
./安装LibreOffice_用户版.sh

# 2. 使配置生效
source ~/.bashrc

# 3. 验证安装
libreoffice --version

# 4. 启动后端
./start_backend.sh

# 5. 启动前端
./start_frontend.sh

# 6. 上传PPTX/DOCX测试
# 应该自动转换为PDF！
```

---

## 💡 其他说明

### 卸载

**用户安装的LibreOffice**：
```bash
# 删除程序
rm -rf ~/.local/libreoffice

# 删除链接
rm ~/.local/bin/libreoffice
rm ~/.local/bin/soffice

# 从.bashrc删除PATH配置
nano ~/.bashrc
# 删除包含 "LibreOffice (用户安装)" 的行
```

**系统安装的LibreOffice**：
```bash
sudo apt-get remove libreoffice-*
```

### 更新

**用户安装**：
- 删除旧版本
- 重新运行安装脚本

**系统安装**：
```bash
sudo apt-get update
sudo apt-get upgrade libreoffice-*
```

---

## 📖 相关文档

- **统一PDF存储方案说明.md** - 了解自动转换机制
- **快速启动指南.md** - 系统启动步骤
- **无sudo权限使用指南.md** - 不安装LibreOffice的替代方案

---

现在就开始安装吧！推荐使用用户目录安装（无需sudo）：

```bash
./安装LibreOffice_用户版.sh
```

安装完成后，就可以享受PPTX/DOCX自动转PDF的便利了！🎉



