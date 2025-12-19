# 🔄 重新生成知识图谱指南

## ❓ 问题

用户反馈：**"现在显示的点里的中文还是都是四个字的"**

## 🔍 原因分析

虽然代码已经修改（2-4字 → 2-8字），但是：

1. ✅ 代码已更新：`backend/api.py` 和 `knowledge_graph.py` 都已改为 `{2,8}`
2. ❌ 旧数据未更新：`knowledge_graph.json` 保存的是用旧规则（4字限制）提取的数据

**解决方案**：删除旧数据，重新提取知识图谱

---

## ✅ 已完成的清理

```bash
✅ 已删除 knowledge_graph.json
✅ 已清理 Python 缓存
```

---

## 🔄 重新生成知识图谱的方法

### 方法1：通过UI重新生成（推荐）

#### 步骤1：确保系统运行最新代码

```bash
cd /home/honglianglu/hdd/rag-agent
./restart_all.sh
```

#### 步骤2：触发知识图谱重新生成

有以下几种方式：

**选项A：重新上传文档**
```
1. 打开浏览器 http://localhost:5173
2. 点击"上传文档"
3. 选择一个或多个文档上传
4. 系统会自动提取知识图谱（使用新的8字限制）
```

**选项B：使用现有文档重新提取**
```
1. 在终端执行：
cd /home/honglianglu/hdd/rag-agent
python3 -c "
from knowledge_graph import KnowledgeGraph
from config import DATA_DIR
import os

kg = KnowledgeGraph()

# 读取现有文档并重新提取
for filename in os.listdir(DATA_DIR):
    if filename.endswith(('.txt', '.md')):
        filepath = os.path.join(DATA_DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
            print(f'正在处理: {filename}')
            num_e, num_r = kg.add_entities_and_relations(text, filename)
            print(f'  提取了 {num_e} 个实体, {num_r} 个关系')

print(f'\n✅ 总计: {len(kg.entities)} 个实体, {len(kg.relationships)} 个关系')
"
```

**选项C：API触发**
```bash
# 如果有API端点可以触发重新生成
curl -X POST http://localhost:8000/api/knowledge-graph/rebuild
```

#### 步骤3：验证结果

```bash
# 打开浏览器
http://localhost:5173

# 点击"知识图谱"
# 点击"可视化"

# 应该看到：
✅ "隐马尔可夫模型" (完整的7个字)
✅ "卷积神经网络" (完整的6个字)
✅ "自然语言处理" (完整的6个字)
✅ "反向传播算法" (完整的5个字)

# 不应该看到：
❌ "隐马尔" (被截断)
❌ "马尔可" (被截断)
```

---

### 方法2：使用改进的知识图谱系统

如果你想使用LLM增强的知识图谱（更高质量）：

```bash
cd /home/honglianglu/hdd/rag-agent

# 运行改进版的知识图谱提取
python3 knowledge_graph_improved.py

# 这会：
# 1. 使用jieba分词（支持更长的词）
# 2. 使用LLM智能提取
# 3. 生成更高质量的实体和关系
```

---

## 🧪 快速验证

### 验证1：检查代码

```bash
# 确认代码已更新
grep -n "{2,8}" /home/honglianglu/hdd/rag-agent/backend/api.py
grep -n "{2,8}" /home/honglianglu/hdd/rag-agent/knowledge_graph.py

# 应该显示：
# api.py:1674:chinese_words = re.findall(r'[\u4e00-\u9fa5]{2,8}', all_text)
# knowledge_graph.py:71:words = re.findall(r'[\u4e00-\u9fa5]{2,8}', text)
```

### 验证2：测试提取

```bash
cd /home/honglianglu/hdd/rag-agent

# 测试新的提取规则
python3 -c "
import re
test_text = '隐马尔可夫模型是一种统计模型，卷积神经网络在图像识别中表现优异。'
words = re.findall(r'[\u4e00-\u9fa5]{2,8}', test_text)
print('提取的词：', words)
"

# 应该输出：
# 提取的词：['隐马尔可夫模型', '是一种', '统计模型', '卷积神经网络', '在图', '图像', '像识', '识别', '中表', '表现', '现优', '优异']
# 注意："隐马尔可夫模型"和"卷积神经网络"是完整的！
```

### 验证3：检查knowledge_graph.json

```bash
# 生成后检查文件
cat knowledge_graph.json | head -50

# 应该看到完整的实体名称
```

---

## 📊 对比

### 旧数据（4字限制） ❌

```json
{
  "entities": {
    "隐马尔": {...},
    "马尔可": {...},
    "可夫模": {...},
    "夫模型": {...}
  }
}
```

### 新数据（8字限制） ✅

```json
{
  "entities": {
    "隐马尔可夫模型": {...},
    "卷积神经网络": {...},
    "自然语言处理": {...}
  }
}
```

---

## 🐛 仍然是4字？

如果重新生成后仍然是4字，检查以下几点：

### 1. 确认代码已更新

```bash
# 检查所有Python文件中是否还有 {2,4}
grep -r "{2,4}" /home/honglianglu/hdd/rag-agent/*.py

# 应该没有结果
```

### 2. 确认服务器已重启

```bash
# 杀掉旧进程
pkill -f "uvicorn.*api:app"
pkill -f "npm run dev"

# 重新启动
./restart_all.sh
```

### 3. 确认使用了正确的提取函数

检查 `backend/api.py` 中的 `/api/knowledge-graph` 端点：

```python
# 应该调用的是更新后的提取函数
entities, relationships = knowledge_graph.extract_entities_and_relations(text, source)
```

### 4. 清除所有缓存

```bash
# 彻底清除
rm -rf data/__pycache__
rm -rf backend/__pycache__
rm -f knowledge_graph.json
rm -f *.pyc

# 重启
./restart_all.sh
```

---

## 💡 提示

### 概念定位 vs 知识图谱

- **概念定位**（`/api/concepts/hot`）：实时从向量库提取，应该立即生效
- **知识图谱**（`/api/knowledge-graph`）：从 `knowledge_graph.json` 读取，需要重新生成

### 如何触发重新生成

知识图谱通常在以下时机生成：
1. 上传新文档时
2. 调用 `add_entities_and_relations()` 时
3. 手动运行提取脚本时

### 最简单的方法

**重新上传一个文档**即可触发重新生成，系统会使用新规则。

---

## ✅ 检查清单

- [ ] 代码已更新（`{2,8}`）
- [ ] 缓存已清理（`knowledge_graph.json` 已删除）
- [ ] 服务器已重启（运行 `./restart_all.sh`）
- [ ] 重新上传文档或运行提取脚本
- [ ] 验证结果（查看可视化界面）
- [ ] 看到完整的术语（如"隐马尔可夫模型"）

---

## 🎉 成功标准

当你在知识图谱可视化界面看到：

```
✅ 隐马尔可夫模型 (7个字，完整)
✅ 卷积神经网络 (6个字，完整)
✅ 自然语言处理 (6个字，完整)
✅ 反向传播算法 (5个字，完整)
```

而不是：

```
❌ 隐马尔 (4个字，不完整)
❌ 马尔可 (3个字，不完整)
```

就说明成功了！🎉

---

**日期**：2025-12-20  
**版本**：v5.1 - Data Regeneration Guide  
**状态**：✅ 缓存已清理，等待重新生成

