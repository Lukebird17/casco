# BGEEmbedding.py
import os
# 需要先安装: pip install -U FlagEmbedding
from FlagEmbedding import BGEM3FlagModel
from typing import List

class BGEEmbedding:
    def __init__(self, model_path: str = "BAAI/bge-m3"):
        print(f"🔄 正在加载 BGE 模型: {model_path} ...")
        # use_fp16=True 开启半精度，节省显存并加速
        self.model = BGEM3FlagModel(model_path, use_fp16=True)
        print("✅ BGE 模型加载完成")

    def get_embedding(self, text: str) -> List[float]:
        """
        适配 VectorStore 的调用接口
        """
        # BGE-M3 encode 返回字典，我们只需要稠密向量 (dense_vecs)
        # 这里的 max_length 可以根据显存调整，BGE-M3 支持 8192
        output = self.model.encode(text, 
                                 batch_size=1, 
                                 max_length=1024, 
                                 return_dense=True, 
                                 return_sparse=False, 
                                 return_colbert_vecs=False)
        return output['dense_vecs'].tolist()