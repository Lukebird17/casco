from VectorBase import VectorStore
from utils import ReadFiles
from LLM import OpenAIChat
from Embeddings import OpenAIEmbedding

# 没有保存数据库
# BAAI/bge-large-zh-v1.5 限制最大 512 tokens，必须设置更小的值
docs = ReadFiles('../data').get_content(max_token_len=400, cover_content=50) # 获得data目录下的所有文件内容并分割
vector = VectorStore(docs)
embedding = OpenAIEmbedding() # 创建EmbeddingModel
# vector.get_vector(EmbeddingModel=embedding)
# vector.persist(path='storage') # 将向量和文档内容保存到storage目录下，下次再用就可以直接加载本地的数据库

vector.load_vector('./storage_demo') # 加载本地的数据库

question = '南京地铁S7号线的运营里程，在南京的已运营地铁线路中长度排第几?'

content = vector.query(question, EmbeddingModel=embedding, k=1)[0]
print(content)
chat = OpenAIChat(model='DeepSeek')
print(chat.chat(question, [], content))

