# 当前 RAG Agent 功能清单

## 📋 核心类和初始化

### `RAGAgent` 类
**位置**: `/home/honglianglu/hdd/rag-agent/rag_agent.py`

**初始化参数**:
```python
def __init__(
    self,
    model: str = MODEL_NAME,
    text_model: str = TEXT_MODEL_NAME,          # 纯文本模型
    multimodal_model: str = MULTIMODAL_MODEL_NAME,  # 多模态模型
    enable_tracking: bool = True,               # Token追踪
    enable_cot: bool = True,                    # Auto-CoT
    use_multimodal: bool = True,                # 多模态检索
)
```

**核心组件**:
- ✅ OpenAI Client
- ✅ VectorStore (文本向量库)
- ✅ HybridRetriever (混合检索器：文本+图片)
- ✅ TokenTracker (Token追踪器)
- ✅ AutoCotPromptBuilder (CoT构建器)
- ✅ ReasoningChain (推理链记录)

---

## 🔍 查询分析和增强

### 1. `analyze_query_type(query)` - 问题分类
**功能**: 分析问题复杂度
**返回**: 'basic' | 'intermediate' | 'advanced'

**分类标准**:
- **Basic**: 简单事实查询
  - 特征词：是什么、定义、名词解释
  - 无复杂推理
  
- **Intermediate**: 中等难度
  - 特征词：如何、为什么、比较、关系
  - 需要综合分析
  
- **Advanced**: 高级问题
  - 特征词：深入、全面、评价、设计
  - 需要深度推理

### 2. `enhance_query(query)` - 查询增强
**功能**: 生成多个查询变体
**返回**: List[str] - 3个查询版本

**策略**:
1. 原始查询
2. 简化版（提取关键词）
3. 扩展版（添加相关术语）

### 3. `extract_technical_terms(query)` - 提取术语
**功能**: 提取专业术语和关键词
**返回**: List[str]

---

## 🔎 检索策略（分层）

### 1. `basic_retrieve(query)` - 基础检索
**策略**:
- 初始检索：15个候选
- Rerank后返回：5个

**适用**: 简单事实查询

### 2. `intermediate_retrieve(query)` - 中级检索
**策略**:
- 初始检索：24个候选
- Rerank后返回：8个

**适用**: 需要综合多个文档

### 3. `advanced_retrieve(query)` - 高级检索
**策略**:
- 初始检索：30个候选
- Rerank后返回：10个
- 构建结构化上下文

**适用**: 复杂推理问题

### 4. `multi_query_retrieve(query, k)` - 多查询检索
**功能**: 
- 生成多个查询变体
- 对每个查询检索k个结果
- 去重合并

**核心代码**:
```python
# 1. 生成多个查询
queries = self.enhance_query(query)

# 2. 对每个查询检索
for q in queries:
    if self.use_multimodal and self.hybrid_retriever:
        results = self.hybrid_retriever.search(q, top_k=k)
    else:
        results = self.vector_store.search(q, top_k=k)

# 3. 去重合并
return all_results
```

### 5. `retrieve_context(query, top_k)` - 智能检索
**功能**: 根据问题类型自动选择检索策略
**流程**:
```
分析问题类型 → 选择策略 → 检索 → 记录推理链
```

---

## 🎯 结果处理

### 1. `rerank_results(query, results)` - 重排序
**功能**: 对检索结果重新排序
**策略**:
- 向量距离 (60% 权重)
- 关键词匹配率 (40% 权重)

**核心代码**:
```python
for result in results:
    match_ratio = sum(term in content for term in terms) / len(terms)
    result['rerank_score'] = original_distance * 0.6 - match_ratio * 0.4
```

### 2. `_format_context(results)` - 格式化上下文
**功能**: 将检索结果格式化为上下文字符串
**支持**: 文本 + 图片（多模态）

### 3. `_build_structured_context(results, query)` - 结构化上下文
**功能**: 为高级问题构建结构化上下文
**包含**: 相关性分析、关键要点、跨文档关联

### 4. `_print_retrieved_context(retrieved_docs)` - 打印Context
**功能**: 在检索完成后立即打印详细信息
**输出**:
```
================================================================================
📚 检索到的Context详情: (10 个文档)
================================================================================

  [1] 文件: 操作系统.pdf
      页码: 第 42 页
      相似度: 0.234
      内容: 虚拟内存使用页表...
```

---

## 🤖 回答生成

### 1. `generate_response(...)` - 生成回答
**参数**:
```python
def generate_response(
    query: str,
    context: str,
    chat_history: Optional[List[Dict]] = None,
    query_type: str = 'basic',
    image: Optional[str] = None,           # 图片输入
    file_content: Optional[str] = None,     # 文件内容
    use_multimodal_model: bool = False,
    enable_socratic: bool = False,          # 苏格拉底模式
    thinking_mode: str = 'fast',            # 思考模式
    temperature: float = 0.7,
    max_tokens: int = 2000,
)
```

**核心功能**:
1. **智能模型选择**
   ```python
   if has_image_input or has_image_in_context:
       selected_model = multimodal_model  # 多模态
   else:
       selected_model = text_model        # 纯文本
   ```

2. **苏格拉底模式**
   - 不直接给答案
   - 通过提问引导思考

3. **思考模式**
   - `fast`: 快速回答
   - `thinking`: 使用CoT深度思考

4. **Auto-CoT集成**
   ```python
   if thinking_mode == 'thinking' and self.cot_builder:
       prompt = self.cot_builder.build_cot_prompt(query, context)
   ```

5. **推理链记录**
   ```python
   if self.current_reasoning_chain:
       self.current_reasoning_chain.add_generation_step(
           "生成回答",
           f"模型: {model_type}, 温度: {temperature}"
       )
   ```

### 2. `_check_image_in_context(retrieved_docs)` - 检查图片
**功能**: 检查context中是否包含图片
**逻辑**:
- 检查 `type == 'image'`
- 检查 `【图片描述】` 标记
- 检查 `image_path` 字段

**用途**: 决定使用文本模型还是多模态模型

---

## 🎓 完整问答流程

### `answer_question(...)` - 主入口
**参数**:
```python
def answer_question(
    query: str,
    chat_history: Optional[List[Dict]] = None,
    top_k: int = TOP_K,
    max_retries: int = 2,
    image: Optional[str] = None,
    file_content: Optional[str] = None,
    enable_socratic: bool = False,
    thinking_mode: str = 'fast',
    stream_thinking: bool = False,
    temperature: float = 0.7,
    max_tokens: int = 2000,
)
```

**完整流程**:
```
1. 创建推理链
   ↓
2. 根据输入类型确定策略
   - 有图片: 描述图片 → 增强query → 检索 → 多模态生成
   - 有文件: 原始query → 检索 → 多模态生成
   - 纯文本: 分析类型 → 检索 → 选择模型 → 生成
   ↓
3. 立即打印检索结果（context详情）
   ↓
4. 生成回答
   ↓
5. 质量检查 (check_answer_quality)
   ↓
6. 记录Token使用
   ↓
7. 返回答案
```

---

## 🔧 质量控制

### `check_answer_quality(answer, query)` - 答案质量检查
**检查项**:
1. ❌ 长度过短 (<10字符)
2. ❌ 通用回复（"我不知道"等）
3. ❌ 明显错误标记
4. ✅ 包含关键术语
5. ✅ 与问题相关

**返回**: bool

---

## 📊 追踪和报告

### 1. `get_reasoning_chain()` - 获取推理链
**返回**: ReasoningChain对象

**包含**:
- 问题分析步骤
- 检索步骤
- 生成步骤
- 结论

### 2. `get_token_report()` - Token报告
**返回**: JSON字符串

**统计**:
- 总Token数
- 查询Token
- 上下文Token
- 回答Token
- 成本估算

### 3. `get_performance_summary()` - 性能摘要
**返回**: Dict

**包含**:
- 查询总数
- 总Token数
- 平均每次查询Token
- 估算成本

---

## 🎨 特色功能

### 1. 多模态支持
- ✅ 文本检索
- ✅ 图片检索（CLIP）
- ✅ 混合检索
- ✅ 图片描述生成并嵌入文本
- ✅ 智能模型选择

### 2. 动态TopK
| 问题复杂度 | 文本初始 | 图片初始 | 最终返回 |
|-----------|---------|---------|---------|
| Simple    | 20      | 5       | 5       |
| Medium    | 50      | 10      | 8       |
| Complex   | 100     | 20      | 10      |

### 3. Rerank重排序
- ✅ 使用 `Pro/BAAI/bge-reranker-v2-m3`
- ✅ API调用，专业模型
- ✅ Top3分数显示

### 4. 页码准确性
- ✅ 从JSON提取100%准确页码
- ✅ 页码嵌入文本：`【第X页】...【/第X页】`
- ✅ 图片页码：`【第X页·图片】...【/图片】`

### 5. 推理模式
- ✅ Fast模式：快速回答
- ✅ Thinking模式：CoT深度思考
- ✅ Socratic模式：启发式引导

---

## 🔗 依赖模块

### 核心依赖
1. **vector_store.py** - 文本向量存储
2. **hybrid_retriever.py** - 混合检索器
3. **token_tracker.py** - Token追踪
4. **reasoning_chain.py** - 推理链记录
5. **auto_cot_prompting.py** - Auto-CoT构建
6. **reranker.py** - Rerank模型 (新增)
7. **image_describer.py** - 图片描述生成 (新增)

### 新增功能模块
- ✅ **reranker.py**: 专业Rerank模型
- ✅ **image_describer.py**: 多模态图片描述
- ✅ **enhanced_ocr.py**: MinerU集成+准确页码
- ✅ **document_loader.py**: 统一文档加载+页码标注

---

## 🚀 最新改进 (v3.0)

### 1. 向量库重构
- MinerU输出统一管理
- 图片描述生成并嵌入文本
- 动态TopK平衡
- Rerank模型集成

### 2. 页码系统
- 从JSON提取100%准确页码
- 页码标注嵌入文本内容
- LLM可见页码信息

### 3. 智能模型选择
- 检查context中是否有图片
- 自动选择文本/多模态模型
- 如有图片引用，自动附加原图

---

## 📝 使用示例

### 基础使用
```python
agent = RAGAgent()
answer = agent.answer_question("什么是虚拟内存？")
```

### 多模态使用
```python
agent = RAGAgent(use_multimodal=True)
answer = agent.answer_question(
    "解释这张图",
    image="path/to/image.png"
)
```

### 高级使用
```python
agent = RAGAgent(
    text_model="Qwen/Qwen2.5-72B-Instruct",
    multimodal_model="Qwen/Qwen3-VL-32B-Instruct",
    enable_tracking=True,
    enable_cot=True,
    use_multimodal=True
)

answer = agent.answer_question(
    "深入分析页表的工作原理",
    thinking_mode='thinking',  # CoT模式
    enable_socratic=False,
    temperature=0.7,
    max_tokens=2000,
    top_k=10
)

# 获取详细报告
print(agent.get_token_report())
print(agent.get_performance_summary())
```

---

## ⚠️ 已知限制

1. **依赖MinerU**: 准确页码需要MinerU处理
2. **API成本**: 图片描述和Rerank会增加API调用
3. **处理速度**: 大量候选文档的Rerank较慢
4. **内存占用**: 混合检索需要同时加载文本和图片向量库

---

## 🎯 与参考代码对比清单

请对照参考代码 `/Users/leon/Project/CS3602NLP/yzy/rag_agent.py` 检查：

### 功能检查表
- [ ] 是否有我们缺少的查询分析方法？
- [ ] 是否有更好的检索策略？
- [ ] 是否有不同的重排序算法？
- [ ] 是否有额外的质量控制机制？
- [ ] 是否有不同的模型选择逻辑？
- [ ] 是否有特殊的上下文构建方法？
- [ ] 是否有我们没有的评估指标？
- [ ] 是否有不同的错误处理？
- [ ] 是否有额外的优化技巧？
- [ ] 是否有不同的提示词工程？

### 建议下一步
1. **提供参考文件内容**或上传文件
2. **列出参考代码的关键功能**
3. **指出你想要的具体功能**

---

生成时间: 2025-12-19
当前版本: v3.0
文件: `/home/honglianglu/hdd/rag-agent/rag_agent.py`


