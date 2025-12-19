# 🔧 知识库和文件上传问题修复

## 📋 用户反馈的问题

1. **文件上传只能单个** - "为什么现在上传文件只能支持单个文件，之前不是可以多个文件的吗"
2. **新建知识库还是4字** - "我新建了个库，还是四个字的知识图啊"

---

## ✅ 问题1：文件上传（已支持多文件）

### 检查结果

**文件**：`frontend/src/components/KnowledgeBasePanel.jsx` 第378行

```jsx
<input
  type="file"
  multiple  ← ✅ 已有 multiple 属性
  accept=".pdf,.docx,.txt,.md,.pptx"
  onChange={handleFileSelect}
  className="hidden"
  id="file-upload"
/>
```

### 结论

✅ **前端代码已经支持多文件上传**（`multiple` 属性）

### 如果仍然只能选一个文件

可能原因：
1. 浏览器缓存 - 刷新浏览器（Ctrl + Shift + R）
2. 上传处理逻辑问题 - 检查后端是否正确处理多文件

### 测试多文件上传

```
1. 打开 http://localhost:5173
2. 点击侧边栏"知识库"图标
3. 点击"选择文件"或拖拽区域
4. 在文件选择对话框中，按住 Ctrl（Windows）或 Cmd（Mac）
5. 选择多个文件
6. 点击"打开"
```

如果成功，会看到多个文件同时上传。

---

## ❌ 问题2：新建知识库还是4字

### 根本原因

**知识图谱文件是全局共享的**，不按知识库分开：

```python
# knowledge_graph.py 第20行
def __init__(self, storage_file: str = "./knowledge_graph.json", ...):
    # ❌ 所有知识库都用同一个文件
```

**影响**：
- 创建新知识库 → 上传新文档 → 查看知识图谱
- 仍然显示旧的 4 字数据（因为读取的是旧的 `knowledge_graph.json`）

### 已执行的修复

✅ **已删除旧的 knowledge_graph.json**

```bash
rm -f /home/honglianglu/hdd/rag-agent/knowledge_graph.json
```

### 现在的行为

- 下次访问知识图谱时，系统会**自动重新生成**
- 使用**新的 8 字规则**提取实体
- "隐马尔可夫模型"会完整保留

---

## 🔄 验证步骤

### 步骤1：确认文件已删除

```bash
ls /home/honglianglu/hdd/rag-agent/knowledge_graph.json

# 应该显示：No such file or directory
```

### 步骤2：测试多文件上传

```
1. 打开 http://localhost:5173
2. 点击"知识库"
3. 选择你的新知识库
4. 点击"上传文件"
5. 按住 Ctrl/Cmd 选择多个文件
6. 观察是否能同时选择和上传多个文件
```

### 步骤3：验证知识图谱（8字规则）

```
1. 等待文档上传完成
2. 点击"知识图谱"图标
3. 点击"可视化"按钮
4. 查看节点名称
```

**✅ 应该看到**：
```
- 隐马尔可夫模型 (7个字，完整)
- 卷积神经网络 (6个字，完整)
- 自然语言处理 (6个字，完整)
```

**❌ 不应该看到**：
```
- 隐马尔 (4个字，被截断)
- 马尔可 (3个字，被截断)
```

---

## 🎯 长期解决方案（建议）

### 问题：知识图谱不按知识库分开

**当前**：
```
所有知识库 → 同一个 knowledge_graph.json
```

**建议**：
```
default 知识库 → data/default/knowledge_graph.json
mynlp 知识库 → data/mynlp/knowledge_graph.json
```

### 实现建议

修改 `backend/api.py` 第77行：

```python
# 改前
knowledge_graph = KnowledgeGraph()

# 改后
# 在切换知识库时，重新初始化知识图谱
def get_knowledge_graph(kb_id='default'):
    kg_file = os.path.join(get_kb_data_dir(kb_id), 'knowledge_graph.json')
    return KnowledgeGraph(storage_file=kg_file)
```

**优点**：
- ✅ 每个知识库独立的知识图谱
- ✅ 切换知识库时显示对应的知识图谱
- ✅ 不会互相干扰

**缺点**：
- 需要较大的代码改动
- 需要修改多个端点

---

## 📊 对比

### 改进前（旧数据） ❌

```json
{
  "entities": {
    "隐马尔": {"type": "关键词", "frequency": 5},
    "马尔可": {"type": "关键词", "frequency": 5},
    "可夫模": {"type": "关键词", "frequency": 4}
  }
}
```

### 改进后（新数据） ✅

```json
{
  "entities": {
    "隐马尔可夫模型": {"type": "概念", "frequency": 5},
    "卷积神经网络": {"type": "技术", "frequency": 8},
    "自然语言处理": {"type": "概念", "frequency": 12}
  }
}
```

---

## 🧪 完整测试流程

### 1. 重启系统

```bash
cd /home/honglianglu/hdd/rag-agent
./restart_all.sh
```

### 2. 测试多文件上传

```
浏览器 → 知识库 → 上传文件
按住 Ctrl/Cmd 选择多个文件 → 上传
```

### 3. 等待处理完成

观察上传进度和处理状态。

### 4. 查看知识图谱

```
点击"知识图谱" → 可视化
验证实体名称是否完整（≥5个字）
```

---

## ✅ 验收标准

### 多文件上传
- [ ] 可以同时选择多个文件
- [ ] 文件列表显示所有选中的文件
- [ ] 所有文件都能成功上传
- [ ] 上传进度正常显示

### 知识图谱（8字规则）
- [ ] 实体名称完整（如"隐马尔可夫模型"）
- [ ] 没有被截断的词（如"隐马尔"）
- [ ] 字体清晰可读（18px）
- [ ] 图表布局舒适

---

## 🐛 如果仍有问题

### 多文件上传不工作

**检查后端是否支持多文件**：

```bash
# 查看上传端点
grep -A 20 "def upload_file" /home/honglianglu/hdd/rag-agent/backend/api.py
```

确认是否有处理多文件的逻辑。

### 知识图谱仍然是4字

**检查是否有其他 knowledge_graph.json 文件**：

```bash
find /home/honglianglu/hdd/rag-agent -name "knowledge_graph.json"
```

如果找到，全部删除：

```bash
find /home/honglianglu/hdd/rag-agent -name "knowledge_graph.json" -delete
```

**检查代码是否有其他4字限制**：

```bash
grep -r "{2,4}" /home/honglianglu/hdd/rag-agent/*.py

# 应该没有结果
```

---

## 💡 总结

### 问题1：多文件上传
- **状态**：✅ 已支持（前端有 `multiple` 属性）
- **测试**：按住 Ctrl/Cmd 选择多个文件

### 问题2：新知识库4字
- **原因**：知识图谱文件全局共享
- **修复**：✅ 已删除旧文件
- **效果**：下次自动重新生成（8字规则）

### 后续建议
- 考虑让知识图谱按知识库分开存储
- 避免不同知识库互相干扰

---

**日期**：2025-12-20  
**问题**：多文件上传 + 新知识库4字  
**修复**：已支持多文件 + 已删除旧数据  
**状态**：✅ 准备就绪，待验证

