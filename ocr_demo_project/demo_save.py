from VectorBase import VectorStore
from utils import ReadFiles
from LLM import OpenAIChat
from Embeddings import OpenAIEmbedding
import json

# 加载数据库
vector = VectorStore([])
embedding = OpenAIEmbedding()
vector.load_vector('./storage_demo')

# 问题
question = '南京地铁S7号线的运营里程，在南京的已运营地铁线路中长度排第几?'

# 检索（返回前3条）
results = vector.query(question, EmbeddingModel=embedding, k=3)

# 构造输出格式
output = {}

# 1. Query
output['query'] = question

# 2. Result
output['result'] = []
for i, doc in enumerate(results, 1):
    output['result'].append({
        "position": i,
        "content": doc  # 可能需要添加来源信息
    })

# 3. Answer
chat = OpenAIChat(model='DeepSeek')
# 将所有检索结果合并
context = "\n\n".join([f"文档{i+1}:\n{doc}" for i, doc in enumerate(results)])
answer = chat.chat(question, [], context)
output['answer'] = answer

# 输出为 JSON
print(json.dumps(output, ensure_ascii=False, indent=2))

