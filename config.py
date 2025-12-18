# API配置
OPENAI_API_KEY = "sk-aqrqxoeqrbfsfhvjhjpozbivejsqhhsqvagukbdlbzjfaawr"  # 请填写你的API密钥
OPENAI_API_BASE = "https://api.siliconflow.cn/v1/"  # 或其他API地址
TEXT_MODEL_NAME = "Qwen/Qwen2.5-72B-Instruct"  # 纯文本模型（用于纯文本问答）
MULTIMODAL_MODEL_NAME = "Qwen/Qwen3-VL-32B-Instruct"  # 多模态模型（用于图片/文件输入）
MODEL_NAME = "Qwen/Qwen3-VL-32B-Instruct"  # 默认对话模型（向后兼容）
OPENAI_EMBEDDING_MODEL = "Pro/BAAI/bge-m3"  # Embedding模型

# 数据目录配置
import os
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))  # 项目根目录
DATA_DIR = os.path.join(PROJECT_ROOT, "data")  # 课程文档目录

# 向量数据库配置
VECTOR_DB_PATH = os.path.join(PROJECT_ROOT, "vector_db")  # 使用绝对路径
COLLECTION_NAME = "course_documents"  # Collection名称

# 文本处理配置
CHUNK_SIZE = 500  # 每个文本块的最大字符数
CHUNK_OVERLAP = 100  # 相邻文本块的重叠字符数
MAX_TOKENS = 80000  # 上下文最大token数

# RAG配置
TOP_K = 5  # 检索返回的文档块数量 
