# API配置
OPENAI_API_KEY = "sk-aqrqxoeqrbfsfhvjhjpozbivejsqhhsqvagukbdlbzjfaawr"  # 请填写你的API密钥
OPENAI_API_BASE = "https://api.siliconflow.cn/v1/"  # 或其他API地址
TEXT_MODEL_NAME = "Qwen/Qwen2.5-72B-Instruct"  # 纯文本模型（用于纯文本问答）
MULTIMODAL_MODEL_NAME = "Qwen/Qwen3-VL-32B-Instruct"  # 多模态模型（用于图片/文件输入）
MODEL_NAME = "Qwen/Qwen3-VL-32B-Instruct"  # 默认对话模型（向后兼容）
OPENAI_EMBEDDING_MODEL = "Pro/BAAI/bge-m3"  # Embedding模型
RERANK_MODEL_NAME = "Pro/BAAI/bge-reranker-v2-m3"  # Rerank模型（用于重排序检索结果）

# 数据目录配置
import os
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))  # 项目根目录
DATA_DIR = os.path.join(PROJECT_ROOT, "data")  # 原文件根目录
VECTOR_DB_DIR = os.path.join(PROJECT_ROOT, "vector_db")  # 向量库根目录

# 默认知识库配置
DEFAULT_KB = "default"
VECTOR_DB_PATH = os.path.join(VECTOR_DB_DIR, DEFAULT_KB)  # 默认向量库路径（向后兼容）
COLLECTION_NAME = "course_documents"  # Collection名称

# LibreOffice 路径配置
LIBREOFFICE_PATH = "/home/honglianglu/hdd/my_libreoffice/extracted_libreoffice/opt/libreoffice25.8/program/soffice"

# 知识库路径辅助函数
def get_kb_data_dir(kb_id="default"):
    """获取指定知识库的原文件目录"""
    return os.path.join(DATA_DIR, kb_id)

def get_kb_vector_dir(kb_id="default"):
    """获取指定知识库的向量库目录"""
    return os.path.join(VECTOR_DB_DIR, kb_id)

def ensure_kb_dirs(kb_id="default"):
    """确保知识库目录存在"""
    data_dir = get_kb_data_dir(kb_id)
    vector_dir = get_kb_vector_dir(kb_id)
    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(vector_dir, exist_ok=True)
    return data_dir, vector_dir

# 文本处理配置
CHUNK_SIZE = 500  # 每个文本块的最大字符数
CHUNK_OVERLAP = 100  # 相邻文本块的重叠字符数
MAX_TOKENS = 80000  # 上下文最大token数

# RAG配置
TOP_K = 5  # 检索返回的文档块数量 
