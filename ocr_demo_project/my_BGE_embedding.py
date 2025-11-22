# BGEEmbedding.py
import os
# 需要先安装: pip install -U FlagEmbedding
from FlagEmbedding import BGEM3FlagModel
from typing import List
from huggingface_hub import snapshot_download

class BGEEmbedding:
    def __init__(self, model_path: str = "BAAI/bge-m3"):
        print(f"🔄 正在加载 BGE 模型: {model_path} ...")
        
        # ===== 完全修复 HuggingFace 下载问题 =====
        # 1. 清除所有代理设置
        for proxy_var in ['http_proxy', 'https_proxy', 'HTTP_PROXY', 'HTTPS_PROXY', 'all_proxy', 'ALL_PROXY']:
            os.environ.pop(proxy_var, None)
        
        # 2. 强制使用官方源（完全移除 HF_ENDPOINT）
        os.environ.pop('HF_ENDPOINT', None)
        
        # 3. 设置忽略模式
        os.environ['HF_HUB_DISABLE_SYMLINKS_WARNING'] = '1'
        
        try:
            # 方案A: 先手动下载模型（带ignore_patterns），然后加载
            if not model_path.startswith('/'):  # 如果不是本地路径
                print("📥 正在从 HuggingFace 下载模型...")
                print("   (忽略系统文件，只下载必要文件)")
                
                local_model_path = snapshot_download(
                    repo_id=model_path,
                    cache_dir=os.path.expanduser("~/.cache/huggingface/hub"),
                    # 只下载必要的文件，忽略图片和系统文件
                    ignore_patterns=[
                        "*.DS_Store",       # macOS 系统文件
                        "*/.DS_Store",
                        "*.git*",           # git 相关
                        "imgs/*",           # 图片目录
                        "*.jpg",            # 图片文件
                        "*.jpeg",
                        "*.png",
                        "*.gif",
                        "*.md",             # markdown文件（可选）
                        "*.pdf",            # PDF文件（可选）
                    ],
                    resume_download=True,  # 支持断点续传
                )
                print(f"✅ 模型下载完成: {local_model_path}")
                model_path = local_model_path
            
            # 使用下载好的本地模型
            print("🔧 正在初始化模型...")
            self.model = BGEM3FlagModel(
                model_path, 
                use_fp16=True,
            )
            print("✅ BGE 模型加载完成")
            
        except Exception as e:
            print(f"❌ BGE模型加载失败: {e}")
            print("")
            print("=" * 60)
            print("💡 解决方案:")
            print("=" * 60)
            print("")
            print("方案1: 清除环境变量后重试")
            print("  unset HF_ENDPOINT")
            print("  unset http_proxy")
            print("  unset https_proxy")
            print("  python demo_enhanced.py")
            print("")
            print("方案2: 使用官方 HuggingFace 源")
            print("  export HF_ENDPOINT=https://huggingface.co")
            print("  python demo_enhanced.py")
            print("")
            print("方案3: 手动下载模型到本地")
            print("  mkdir -p ~/models")
            print("  cd ~/models")
            print("  git lfs install")
            print("  git clone https://huggingface.co/BAAI/bge-m3")
            print("  # 然后修改 demo_enhanced.py 中的 model_path")
            print("  # embedding = BGEEmbedding(model_path='~/models/bge-m3')")
            print("")
            print("方案4: 使用其他 Embedding 模型")
            print("  # 在 demo_enhanced.py 中使用 OpenAIEmbedding")
            print("  # embedding = OpenAIEmbedding()")
            print("")
            raise

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