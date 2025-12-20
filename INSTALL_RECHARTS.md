# ⚠️  recharts 依赖安装说明

## 问题

前端报错：`Failed to resolve import "recharts"`

## 原因

质量评估雷达图功能需要 `recharts` 库，但尚未安装。

## 解决方案

### 方法1：使用 npm（推荐）

```bash
cd /home/honglianglu/hdd/rag-agent/frontend
npm install
```

这会安装所有依赖，包括新添加的 recharts。

### 方法2：只安装 recharts

```bash
cd /home/honglianglu/hdd/rag-agent/frontend
npm install recharts
```

### 方法3：使用 yarn（如果你用yarn）

```bash
cd /home/honglianglu/hdd/rag-agent/frontend
yarn install
# 或
yarn add recharts
```

### 方法4：使用 pnpm（如果你用pnpm）

```bash
cd /home/honglianglu/hdd/rag-agent/frontend
pnpm install
# 或
pnpm add recharts
```

---

## 已完成的工作

✅ 已在 `package.json` 中添加了 recharts 依赖：

```json
"dependencies": {
  ...
  "recharts": "^2.10.0",
  ...
}
```

---

## 执行步骤

### 1. 打开终端

### 2. 进入前端目录
```bash
cd /home/honglianglu/hdd/rag-agent/frontend
```

### 3. 安装依赖
```bash
npm install
```

### 4. 等待安装完成
```
added 1 package, and audited X packages in Xs
```

### 5. 刷新浏览器

按 `Ctrl+R` 或 `F5` 刷新页面，错误应该消失。

---

## 验证安装

```bash
# 检查是否安装成功
cd /home/honglianglu/hdd/rag-agent/frontend
npm list recharts

# 应该看到：
# recharts@2.10.0
```

---

## 如果还有问题

### 清理并重新安装

```bash
cd /home/honglianglu/hdd/rag-agent/frontend

# 删除 node_modules
rm -rf node_modules

# 删除 package-lock.json
rm -f package-lock.json

# 重新安装
npm install
```

### 检查 npm 路径

```bash
which npm
# 如果没有输出，说明 npm 不在 PATH 中

# 查找 npm
find ~ -name "npm" 2>/dev/null | grep bin
```

### 使用 nvm 的 npm

```bash
# 如果使用 nvm
source ~/.nvm/nvm.sh

# 激活 node 版本
nvm use node

# 然后再安装
npm install
```

---

## 完成后

一旦安装完成，质量评估雷达图功能就可以正常使用了！

测试步骤：
1. 刷新浏览器
2. 上传文档并提问
3. 点击「详细信息」
4. 看到雷达图

---

**创建时间**：2025-12-20  
**状态**：⏳ 等待用户安装依赖

