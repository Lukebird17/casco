# 智能体竞赛使用指南

## 📋 目录
1. [系统概述](#系统概述)
2. [快速开始](#快速开始)
3. [核心功能](#核心功能)
4. [优化策略](#优化策略)
5. [使用示例](#使用示例)
6. [提交文件准备](#提交文件准备)
7. [常见问题](#常见问题)

---

## 系统概述

这是一个针对智能体竞赛设计的深度研究任务系统，能够处理：
- ✅ 扫描PDF文档
- ✅ 多版本文档对比
- ✅ 中英文规范解析
- ✅ 结构化表格数据
- ✅ 跨源对比分析
- ✅ 演变追溯与逻辑推理

### 系统架构

```
智能体系统
├── 文档处理层 (enhanced_utils.py)
│   ├── PDF增强读取（表格检测）
│   ├── 智能分块（保留上下文）
│   └── 元数据保留（来源追踪）
│
├── 检索层 (VectorBase.py + agent.py)
│   ├── 多查询增强
│   ├── 向量检索
│   ├── 重排序机制
│   └── 多轮检索（高级题）
│
├── 推理层 (agent.py + LLM.py)
│   ├── 问题类型识别
│   ├── 分层提示词策略
│   ├── 多文档推理
│   └── 答案质量检查
│
└── 输出层 (run_competition.py)
    ├── 格式化输出
    ├── 批量处理
    └── 结果汇总
```

---

## 快速开始

### 1. 环境准备

```bash
# 安装依赖
cd demo
pip install -r requirements.txt

# 或使用conda
conda create -n casco python=3.9
conda activate casco
pip install -r requirements.txt
```

### 2. 配置API密钥

创建 `.env` 文件：

```bash
# OpenAI兼容的API配置（用于Embedding）
OPENAI_API_KEY=your_embedding_api_key
OPENAI_BASE_URL=https://api.your-service.com/v1
OPENAI_API_MODEL=BAAI/bge-large-zh-v1.5

# LLM API配置（用于生成答案）
CLOUD_MODEL=deepseek-chat
CLOUD_API_KEY=your_llm_api_key
CLOUD_BASE_URL=https://api.deepseek.com/v1
```

### 3. 构建向量数据库

```bash
# 首次运行，构建向量数据库
python run_competition.py --mode all --rebuild

# 后续运行，直接加载
python run_competition.py --mode all
```

---

## 核心功能

### 1. 智能问题分类

系统自动识别三种问题类型：

#### 基础题 - "大海捞针"
- 特征：单文档、精确查找
- 策略：高精度检索 + 精确匹配
- 检索数：k=3

#### 中级题 - 多位置综合
- 特征：同文档多段落、需要汇总
- 策略：增加召回 + 信息融合
- 检索数：k=8

#### 高级题 - 跨文档推理
- 特征：多文档、版本对比、演变分析
- 策略：多轮检索 + 推理链
- 检索数：k=10，支持二次检索

### 2. 多查询增强

系统会自动将一个查询扩展为多个：

```python
原始查询: "2024年，株洲中车时代电气股份有限公司中标金额是多少？"

扩展查询:
- "2024年，株洲中车时代电气股份有限公司中标金额是多少？"
- "2024"
- "株洲中车时代电气"
- "中标金额"
```

### 3. 重排序机制

基于关键词匹配度对检索结果重新排序，提高相关性。

### 4. 分层提示词

针对不同题型使用不同的提示词模板，优化答案质量：
- 基础题：强调精确性
- 中级题：强调综合性
- 高级题：强调推理性

---

## 优化策略

### 针对评测维度的优化

竞赛评测关注三个维度：
1. **答案质量** - 主要权重
2. **Token消耗** - 成本优化
3. **模型参数量** - 模型选择

#### 答案质量优化

```python
# config.py 中调整
LLM_CONFIG = {
    'temperature': 0.1,  # 基础题用0，高级题用0.2
    'max_tokens': 1000,  # 控制答案长度
}

# 启用重试机制
OPTIMIZATION_CONFIG = {
    'max_retries': 2,
    'retry_on_low_quality': True,
}
```

#### Token消耗优化

```python
# 减小chunk大小
CHUNK_CONFIG = {
    'max_token_len': 400,  # 从600降到400
    'cover_content': 50,   # 控制重叠
}

# 控制检索数量
RETRIEVAL_CONFIG = {
    'basic': {'k': 3},      # 基础题只需要3个
    'intermediate': {'k': 5},  # 降低到5
    'advanced': {'k': 8},   # 降低到8
}
```

#### 模型参数量优化

推荐使用的开源模型：

| 模型 | 参数量 | 适用场景 | Token效率 |
|------|--------|----------|-----------|
| Qwen2.5-7B | 7B | 基础-中级题 | ⭐⭐⭐⭐⭐ |
| DeepSeek-V2 | 16B | 全部题型 | ⭐⭐⭐⭐ |
| Llama3-8B | 8B | 基础-中级题 | ⭐⭐⭐⭐ |
| GLM-4-9B | 9B | 全部题型 | ⭐⭐⭐⭐ |

---

## 使用示例

### 模式1：处理所有竞赛题目

```bash
# 一次性处理所有题目
python run_competition.py --mode all --output-dir outputs

# 输出结构：
# outputs/
# ├── 基础题_1.json
# ├── 基础题_2.json
# ├── ...
# ├── 高级题_2.json
# └── all_results.json
```

### 模式2：交互式查询

```bash
# 进入交互模式
python run_competition.py --mode interactive

# 然后输入问题：
请输入问题: 2024年，株洲中车时代电气股份有限公司中标金额是多少？
```

### 模式3：单个问题查询

```bash
python run_competition.py --mode single \
  --query "2024年，株洲中车时代电气股份有限公司中标金额是多少？"
```

### 在代码中使用

```python
from run_competition import CompetitionRunner

# 创建运行器
runner = CompetitionRunner(
    data_path='../data',
    storage_path='storage'
)

# 构建向量库
runner.build_or_load_vectorstore(rebuild=False)

# 初始化智能体
runner.initialize_agent()

# 处理单个问题
result = runner.process_single_question(
    "你的问题",
    question_type="测试"
)

print(result['answer'])
```

---

## 提交文件准备

### 需要提交的文件

1. **storage文件夹**
   ```
   storage/
   ├── vectors.json      # 向量数据
   └── doecment.json     # 文档内容
   ```

2. **示例模板.json** - 按照要求格式的答案文件
   ```json
   {
     "query": "问题内容",
     "result": [
       {
         "position": 1,
         "content": "第1条召回结果"
       },
       {
         "position": 2,
         "content": "第2条召回结果"
       }
     ],
     "answer": "基于召回内容生成的回答"
   }
   ```

### 生成提交文件的步骤

```bash
# 1. 运行竞赛脚本
python run_competition.py --mode all --output-dir submission

# 2. storage文件夹已自动生成在demo/storage/

# 3. 将outputs中的结果按要求命名
# 每道题一个JSON文件，格式参考示例模板.json
```

### 检查清单

- [ ] storage/vectors.json 文件存在且大小合理
- [ ] storage/doecment.json 文件存在
- [ ] 每道题的JSON文件格式正确
- [ ] answer字段包含完整答案
- [ ] result数组包含检索到的文档片段
- [ ] 文件编码为UTF-8

---

## 常见问题

### Q1: 如何提高答案准确性？

**A:** 
1. 调整检索参数：增加`k`值
2. 启用多查询增强
3. 降低temperature到0
4. 使用更大的chunk_size保留完整上下文

```python
# 在config.py中修改
RETRIEVAL_CONFIG['basic']['k'] = 5  # 增加到5
LLM_CONFIG['temperature'] = 0.0     # 降到0
```

### Q2: 如何减少Token消耗？

**A:**
1. 减小chunk大小
2. 减少检索数量k
3. 关闭多查询增强
4. 使用更小参数的模型

```python
CHUNK_CONFIG['max_token_len'] = 300  # 从400降到300
RETRIEVAL_CONFIG['basic']['k'] = 2   # 从3降到2
```

### Q3: 处理表格数据效果不好？

**A:**
系统已内置表格检测，但可以进一步优化：

```python
# 在enhanced_utils.py中
# 调整detect_tables_in_page()函数的阈值
if re.search(r'\s{2,}|\t', line) and len(line.split()) >= 2:
    # 这里可以调整检测逻辑
```

### Q4: 多版本对比题怎么处理？

**A:**
系统会自动识别为高级题，使用多轮检索：

```python
# 在agent.py的advanced_retrieve中
# 第一轮检索两个版本的文档
# 第二轮细化检索具体差异点
```

### Q5: 如何调试某道题？

**A:**
```bash
# 使用single模式，添加调试信息
python run_competition.py --mode single \
  --query "你的问题" \
  2>&1 | tee debug.log

# 查看检索到的文档片段
cat outputs/single_query_result.json | jq '.result'
```

---

## 进阶优化技巧

### 1. 针对特定文档类型优化

```python
# 在enhanced_utils.py中
def read_file_content_with_metadata(cls, file_path: str):
    # 针对事故报告类文档
    if '事故报告' in file_path:
        # 使用更大的chunk保持完整性
        metadata['chunk_size'] = 600
    
    # 针对标准规范类文档
    elif '标准规范' in file_path:
        # 保留标题层级结构
        metadata['preserve_structure'] = True
```

### 2. 自定义重排序策略

```python
# 在agent.py中增强rerank_results
def rerank_results(self, query: str, results: List[Dict]):
    # 添加语义相似度评分
    # 添加关键实体匹配评分
    # 添加文档类型权重
    pass
```

### 3. 答案后处理

```python
def post_process_answer(self, answer: str, query: str):
    # 移除冗余信息
    # 格式化数字和日期
    # 确保答案直接性
    pass
```

---

## 性能监控

### Token使用统计

```python
# 运行后查看token统计
import json
with open('outputs/all_results.json', 'r') as f:
    results = json.load(f)

# 统计每道题的token使用
# (需要在LLM.py中添加token计数)
```

### 答案质量评估

```python
# 人工检查答案质量
for result in results:
    print(f"问题: {result['query']}")
    print(f"答案: {result['answer']}")
    print(f"检索文档数: {len(result['result'])}")
    print("-" * 60)
```

---

## 联系与支持

如果遇到问题，检查：
1. API密钥配置是否正确
2. 数据文件路径是否正确
3. 依赖包是否完整安装
4. Python版本是否 >= 3.8

---

## 更新日志

- **v1.0** (2025-11-15): 初始版本
  - 基础RAG功能
  - 三级问题分类
  - 多查询增强
  - 重排序机制
  - 批量处理支持

