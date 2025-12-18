# React 前端完整使用指南 (Gemini 风格)

## 📋 目录

- [项目架构](#项目架构)
- [快速启动](#快速启动)
- [功能特性](#功能特性)
- [开发指南](#开发指南)
- [部署指南](#部署指南)
- [常见问题](#常见问题)

---

## 🏗️ 项目架构

### 技术栈

**前端：**
- ⚛️ React 18.3
- 🎨 Tailwind CSS 3.4
- 🚀 Vite 5.2
- 📡 Axios（HTTP 客户端）
- 🎭 Framer Motion（动画）
- 🔔 React Hot Toast（通知）
- 📝 React Markdown（Markdown 渲染）
- 💎 Lucide React（图标库）

**后端：**
- ⚡ FastAPI 0.110
- 🦄 Uvicorn（ASGI 服务器）
- 🤖 RAG Agent（智能问答引擎）

### 目录结构

```
rag-agent/
├── frontend/                  # React 前端
│   ├── src/
│   │   ├── api/              # API 客户端
│   │   │   └── client.js     # Axios 封装
│   │   ├── components/       # React 组件
│   │   │   ├── ChatInterface.jsx    # 聊天界面
│   │   │   ├── MessageBubble.jsx    # 消息气泡
│   │   │   ├── InputArea.jsx        # 输入区域
│   │   │   ├── ThinkingIndicator.jsx # 思考动画
│   │   │   ├── Sidebar.jsx          # 侧边栏
│   │   │   └── ToolPanel.jsx        # 工具面板
│   │   ├── hooks/            # 自定义 Hooks
│   │   │   ├── useChat.js    # 聊天状态管理
│   │   │   └── useSessions.js # 会话管理
│   │   ├── App.jsx           # 主应用
│   │   ├── App.css           # Gemini 风格样式
│   │   ├── index.css         # Tailwind CSS
│   │   └── main.jsx          # 入口文件
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   └── postcss.config.js
├── backend/                   # FastAPI 后端
│   ├── api.py                # API 路由
│   └── requirements.txt      # Python 依赖
├── start_dev.sh              # 开发环境启动脚本
├── stop_dev.sh               # 停止脚本
└── React前端使用指南.md      # 本文档
```

---

## 🚀 快速启动

### 前置要求

1. **Conda 环境：** 已激活 `rag` 环境
2. **Node.js：** 版本 >= 18.0
3. **npm：** 版本 >= 9.0

### 方式 1：一键启动（推荐）

```bash
# 激活 conda 环境
conda activate rag

# 一键启动前后端
./start_dev.sh
```

访问地址：
- 🌐 前端：http://localhost:5173
- 📡 后端：http://localhost:8000
- 📖 API 文档：http://localhost:8000/docs

### 方式 2：分别启动

**启动后端：**
```bash
conda activate rag
cd backend
python api.py
```

**启动前端：**
```bash
cd frontend

# 首次运行需要安装依赖
npm install

# 启动开发服务器
npm run dev
```

### 停止服务

```bash
# 方式 1：使用脚本
./stop_dev.sh

# 方式 2：手动停止
# 按 Ctrl+C 停止各个终端
```

---

## ✨ 功能特性

### 1. Gemini 风格界面

- ✅ **Google 配色方案：** 使用官方 Material Design 颜色
- ✅ **圆润设计：** 18px 圆角，柔和过渡
- ✅ **流畅动画：** Framer Motion 提供的丝滑交互
- ✅ **响应式布局：** 适配各种屏幕尺寸

### 2. 多模态交互

- ✅ **文本输入：** 支持多行输入，快捷键提交
- ✅ **图片上传：** 拖拽或点击上传，最大 10MB
- ✅ **文档上传：** 支持 PDF、DOCX、TXT 等格式
- ✅ **实时预览：** 上传后即时显示文件信息

### 3. 智能对话

- ✅ **多轮对话：** 自动保存对话历史
- ✅ **会话管理：** 创建、切换、删除会话
- ✅ **思考过程可视化：** 显示 AI 检索和思考过程
- ✅ **Markdown 渲染：** 支持代码高亮、表格、公式

### 4. 苏格拉底模式

- ✅ **引导式学习：** AI 通过反问引导思考
- ✅ **一键切换：** 顶部开关快速启用/禁用
- ✅ **视觉反馈：** 紫色图标标识当前模式

### 5. 引用与置信度

- ✅ **来源追踪：** 显示答案引用的文档和页码
- ✅ **置信度计算：** 实时评估答案可靠性
- ✅ **快速跳转：** 点击引用跳转到原文

### 6. 侧边栏工具

- ✅ **会话列表：** 查看和切换历史对话
- ✅ **工具面板：** 快速访问知识库、文档查看等
- ✅ **可折叠设计：** 节省屏幕空间

---

## 🛠️ 开发指南

### 前端开发

#### 1. 安装依赖

```bash
cd frontend
npm install
```

#### 2. 启动开发服务器

```bash
npm run dev
```

#### 3. 构建生产版本

```bash
npm run build
```

#### 4. 预览生产版本

```bash
npm run preview
```

### 添加新组件

1. 在 `src/components/` 创建组件文件
2. 使用 Tailwind CSS 类名进行样式设计
3. 遵循 Gemini 风格规范（圆角、配色、动画）

示例：

```jsx
import React from 'react';
import { motion } from 'framer-motion';

const MyComponent = () => {
  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      className="bg-white rounded-lg shadow-sm p-4"
    >
      <h2 className="text-google-gray-900 font-medium">
        我的组件
      </h2>
    </motion.div>
  );
};

export default MyComponent;
```

### 调用后端 API

使用 `src/api/client.js` 中封装的方法：

```javascript
import { sendMessage } from '../api/client';

const response = await sendMessage({
  message: '你好',
  session_id: 'session-123',
  enable_socratic: false,
});

console.log(response.response); // AI 回复
console.log(response.confidence); // 置信度
console.log(response.citations); // 引用列表
```

### 配色方案

Tailwind 配置中的 Google 颜色：

```javascript
// 蓝色（主色调）
bg-google-blue-500  // 按钮、强调
bg-google-blue-50   // 浅色背景

// 灰色（中性色）
bg-google-gray-50   // 页面背景
bg-google-gray-100  // 消息气泡
bg-google-gray-700  // 文字
bg-google-gray-900  // 标题
```

---

## 🚢 部署指南

### 前端部署

#### 1. 构建生产版本

```bash
cd frontend
npm run build
```

生成的静态文件在 `frontend/dist/` 目录。

#### 2. 部署到 Nginx

```nginx
server {
    listen 80;
    server_name your-domain.com;

    root /path/to/rag-agent/frontend/dist;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }

    location /api {
        proxy_pass http://localhost:8000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

### 后端部署

#### 1. 使用 Systemd 服务

创建 `/etc/systemd/system/rag-agent.service`：

```ini
[Unit]
Description=RAG Agent API
After=network.target

[Service]
Type=simple
User=your-user
WorkingDirectory=/path/to/rag-agent/backend
Environment="PATH=/path/to/conda/envs/rag/bin"
ExecStart=/path/to/conda/envs/rag/bin/python api.py
Restart=always

[Install]
WantedBy=multi-user.target
```

启动服务：

```bash
sudo systemctl daemon-reload
sudo systemctl start rag-agent
sudo systemctl enable rag-agent
```

#### 2. 使用 Docker

创建 `Dockerfile`：

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "backend/api.py"]
```

构建和运行：

```bash
docker build -t rag-agent .
docker run -d -p 8000:8000 rag-agent
```

---

## ❓ 常见问题

### Q1: 前端无法连接后端

**问题：** 控制台显示 CORS 错误或连接被拒绝。

**解决方案：**
1. 确认后端已启动：`curl http://localhost:8000/api/init`
2. 检查 `frontend/src/api/client.js` 中的 `API_BASE` 地址
3. 确认后端 CORS 配置正确

### Q2: npm install 失败

**问题：** 安装依赖时出错。

**解决方案：**
```bash
# 清除缓存
npm cache clean --force

# 删除 node_modules
rm -rf node_modules package-lock.json

# 重新安装
npm install
```

### Q3: 页面显示不正常

**问题：** 样式错乱或组件不显示。

**解决方案：**
1. 检查浏览器控制台错误
2. 确认 Tailwind CSS 配置正确
3. 尝试清除浏览器缓存：Ctrl+Shift+R

### Q4: 上传文件失败

**问题：** 文件上传后没有响应。

**解决方案：**
1. 检查文件大小限制（图片 10MB，文档 50MB）
2. 确认文件格式支持（图片：jpg/png/gif，文档：pdf/docx/txt）
3. 查看后端日志错误信息

### Q5: 热重载不工作

**问题：** 修改代码后页面不自动刷新。

**解决方案：**
```bash
# 重启 Vite 开发服务器
npm run dev
```

---

## 📚 相关文档

- [React 官方文档](https://react.dev/)
- [Tailwind CSS 文档](https://tailwindcss.com/docs)
- [Vite 文档](https://vitejs.dev/)
- [FastAPI 文档](https://fastapi.tiangolo.com/)
- [Framer Motion 文档](https://www.framer.com/motion/)

---

## 🎉 完成！

现在您已经掌握了 React + Tailwind CSS 前端的完整使用方法！

如果遇到问题，请查看：
- 📖 API 文档：http://localhost:8000/docs
- 🐛 Issue 追踪：查看项目 GitHub
- 💬 开发日志：查看终端输出

祝您使用愉快！🚀





