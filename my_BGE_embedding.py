# BGEEmbedding.py
import os
# 需要先安装: pip install -U FlagEmbedding
from FlagEmbedding import BGEM3FlagModel
from typing import List
from huggingface_hub import snapshot_download

class BGEEmbedding:
    def __init__(self, model_path: str = "BAAI/bge-m3"):
        print(f"🔄 正在加载 BGE 模型: {model_path} ...")
        
        # 尝试预先下载模型，忽略 .DS_Store 文件，解决 hf-mirror 上的 403 问题
        if not os.path.exists(model_path):
            try:
                print("   正在尝试预下载模型以避开 .DS_Store 问题...")
                # 下载到默认缓存目录，并获取本地路径
                model_path = snapshot_download(
                    repo_id=model_path, 
                    ignore_patterns=["*.DS_Store", "imgs/*", "imgs/.DS_Store"]
                )
                print(f"   模型已下载至: {model_path}")
            except Exception as e:
                print(f"   预下载警告: {e}")
                # 如果失败，继续尝试使用原始路径
        
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