# 🔧 知识图谱仍然不对 - 根本原因和解决方案

## 🎯 核心问题

知识图谱显示的仍然是4字词，因为：

### 问题1：知识图谱不会自动重新生成

```
删除 knowledge_graph.json
    ↓
后端初始化时创建空的 KnowledgeGraph()
    ↓
但不会自动从向量库加载数据！
    ↓
前端访问时，看到的是空图谱或旧数据
```

### 问题2：向量库中的数据可能已经是4字分词的

```
文档上传时 → 文本分词 → 存入向量库
                ↓
            如果当时是4字规则
                ↓
            向量库中就是4字数据
```

---

## ✅ 根本解决方案

### 方案1：清空向量库，重新上传文档（推荐）

这是**唯一能保证彻底解决**的方法：

```bash
cd /home/honglianglu/hdd/rag-agent

# 1. 停止服务
pkill -f "uvicorn.*api:app"

# 2. 删除向量库数据
rm -rf vector_db/default/*
rm -rf vector_db/mynlp/*

# 3. 删除知识图谱
rm -f knowledge_graph.json

# 4. 重启服务
./restart_all.sh

# 5. 重新上传文档
# 这次上传会使用新的8字规则！
```

**为什么这样做？**
- 旧的向量库数据是用4字规则分词的
- 即使代码改了，读出来的还是旧数据
- 只有重新上传，才会用新规则处理

---

### 方案2：添加"重建知识图谱"端点（需要开发）

在 `backend/api.py` 中添加：

```python
@app.post("/api/knowledge-graph/rebuild")
async def rebuild_knowledge_graph():
    """
    从向量库重建知识图谱
    """
    try:
        if knowledge_graph is None or rag_agent is None:
            raise HTTPException(status_code=500, detail="系统未初始化")
        
        # 清空当前知识图谱
        knowledge_graph.entities.clear()
        knowledge_graph.relationships.clear()
        
        # 从向量库获取所有文档
        results = rag_agent.vector_store.collection.get(
            limit=500,
            include=['documents', 'metadatas']
        )
        
        if not results or not results.get('documents'):
            return {
                "success": False,
                "message": "向量库中没有文档"
            }
        
        documents = results['documents']
        metadatas = results.get('metadatas', [])
        
        # 按文档分组
        doc_groups = {}
        for doc, meta in zip(documents, metadatas):
            filename = meta.get('filename', '未知')
            if filename not in doc_groups:
                doc_groups[filename] = []
            doc_groups[filename].append(doc)
        
        # 提取知识图谱
        total_entities = 0
        total_relations = 0
        
        for filename, texts in doc_groups.items():
            full_text = ' '.join(texts)[:8000]  # 限制长度
            num_e, num_r = knowledge_graph.add_entities_and_relations(full_text, filename)
            total_entities += num_e
            total_relations += num_r
        
        return {
            "success": True,
            "message": "知识图谱重建成功",
            "stats": {
                "documents": len(doc_groups),
                "entities": len(knowledge_graph.entities),
                "relationships": len(knowledge_graph.relationships)
            }
        }
        
    except Exception as e:
        print(f"❌ 重建知识图谱错误: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
```

然后在前端添加一个"重建"按钮：

```jsx
<button onClick={async () => {
  const res = await axios.post('http://localhost:8000/api/knowledge-graph/rebuild');
  if (res.data.success) {
    toast.success('知识图谱重建成功！');
    loadStats(); // 重新加载
  }
}}>
  🔄 重建知识图谱
</button>
```

---

### 方案3：手动通过API触发（临时方案）

```bash
# 使用curl调用API重建
curl -X POST http://localhost:8000/api/knowledge-graph/rebuild
```

（前提是先添加方案2的端点）

---

## 🧪 验证代码是否正确

先确认代码确实改了：

```bash
cd /home/honglianglu/hdd/rag-agent

# 检查是否还有4字限制
grep -n "{2,4}" *.py backend/*.py

# 应该没有结果

# 检查是否改为8字
grep -n "{2,8}" *.py backend/*.py

# 应该看到：
# api.py:1684:chinese_words = re.findall(r'[\u4e00-\u9fa5]{2,8}', all_text)
# knowledge_graph.py:71:words = re.findall(r'[\u4e00-\u9fa5]{2,8}', text)
```

---

## 🎯 我推荐的做法

### 最简单有效的方法：

```bash
# 1. 进入目录
cd /home/honglianglu/hdd/rag-agent

# 2. 备份重要数据（如果有）
# cp -r data data_backup
# cp -r vector_db vector_db_backup

# 3. 删除当前知识库的向量数据
rm -rf vector_db/mynlp/*

# 4. 删除知识图谱
rm -f knowledge_graph.json

# 5. 确认代码已更新（应该看到8字）
grep "{2,8}" knowledge_graph.py backend/api.py

# 6. 重启服务
./restart_all.sh

# 7. 重新上传文档到 mynlp 知识库
# 打开浏览器 → 知识库 → 选择 mynlp → 上传文档

# 8. 等待处理完成后，查看知识图谱
# 点击"知识图谱" → 可视化
```

---

## 📊 预期结果

### 成功的标志

**知识图谱可视化界面应该显示**：

```
✅ 隐马尔可夫模型 (7个字)
✅ 卷积神经网络 (6个字)  
✅ 自然语言处理 (6个字)
✅ 循环神经网络 (5个字)
✅ 反向传播 (4个字) ← 4字是因为本来就是4字，不是被截断
```

**不应该看到**：

```
❌ 隐马尔 (4个字，被截断)
❌ 马尔可 (3个字，被截断)
❌ 可夫模 (3个字，被截断)
```

---

## 🔍 为什么删除向量库才能解决？

### 数据流程

```
┌─────────────┐
│  PDF文档    │
└──────┬──────┘
       ↓ 上传时处理
┌──────────────────────────┐
│ document_loader.py       │ ← 使用当时的代码规则
│ text_splitter.py         │
└──────┬───────────────────┘
       ↓ 已分词的文本
┌──────────────────────────┐
│ 向量库（ChromaDB）       │ ← 存储的是分词后的文本
│ {"content": "隐马尔"}    │ ← 如果用的是4字规则
└──────┬───────────────────┘
       ↓ 读取
┌──────────────────────────┐
│ knowledge_graph.py       │ ← 即使用8字规则
│ 读到的还是"隐马尔"      │ ← 因为源数据就是4字的
└──────────────────────────┘
```

**关键点**：
- 向量库存储的是**处理后的文本**
- 改代码只影响**新处理的文档**
- 已存储的数据不会自动更新

---

## 💡 总结

### 核心原因
1. ✅ 代码已改（{2,8}）
2. ❌ 但向量库中的数据是旧的（4字分词）
3. ❌ 知识图谱读取旧数据 → 仍显示4字

### 唯一解决方案
**删除向量库，重新上传文档**

这样整个流程都用新规则：
```
上传 → 8字分词 → 存入向量库 → 读取 → 知识图谱显示8字 ✅
```

---

## 🎯 立即行动

```bash
cd /home/honglianglu/hdd/rag-agent

# 清空数据
rm -rf vector_db/mynlp/*
rm -f knowledge_graph.json

# 确认代码
grep "{2,8}" knowledge_graph.py

# 重启
./restart_all.sh

# 重新上传文档
```

**5分钟后，你会看到完整的"隐马尔可夫模型"！** 🎉

---

**日期**：2025-12-20  
**问题**：知识图谱还是不对（4字）  
**原因**：向量库数据是旧的  
**解决**：删除向量库，重新上传  
**状态**：⏳ 等待执行

