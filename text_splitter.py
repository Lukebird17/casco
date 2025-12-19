from typing import List, Dict
from tqdm import tqdm


class TextSplitter:
    def __init__(self, chunk_size: int, chunk_overlap: int):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split_text(self, text: str) -> List[str]:
        """将文本切分为块

        要求：
        1. 将文本按照chunk_size切分为多个块
        2. 相邻块之间要有chunk_overlap的重叠（用于保持上下文连续性）
        3. 尽量在句子边界处切分（查找句子结束符：。！？.!?\n\n）
        4. 返回切分后的文本块列表
        """
        if not text:
            return []

        chunks = []
        
        # 定义句子分隔符
        sentence_endings = ['。', '！', '？', '.', '!', '?', '\n\n']
        
        # 当前块的起始位置
        start = 0
        
        while start < len(text):
            # 确定当前块的结束位置
            end = start + self.chunk_size
            
            # 如果已经到达文本末尾
            if end >= len(text):
                chunks.append(text[start:].strip())
                break
            
            # 尝试在句子边界处切分
            # 在end位置附近查找句子结束符
            best_split = end
            search_range = 50  # 在end前后50个字符内查找句子边界
            
            # 向前查找最近的句子结束符
            for i in range(max(0, end - search_range), end + 1):
                if i < len(text) and text[i] in sentence_endings:
                    best_split = i + 1
            
            # 提取当前块
            chunk = text[start:best_split].strip()
            if chunk:
                chunks.append(chunk)
            
            # 移动到下一个块的起始位置（考虑重叠）
            start = best_split - self.chunk_overlap
            
            # 确保不会倒退
            if start <= chunks[-1].__len__() // 2 if chunks else False:
                start = best_split

        return chunks

    def split_documents(self, documents: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """切分多个文档，并【至关重要】地保留元数据（包括image_url）
        
        所有文档都进行文本切分，以确保不超过 embedding 模型的 token 限制
        """
        chunks_with_metadata = []

        for doc in tqdm(documents, desc="处理文档", unit="文档"):
            content = doc.get("content", "")
            filetype = doc.get("filetype", "")
            
            # === [核心修复点 1] 获取原始 metadata (这里面才有 image_url!) ===
            # 如果这里没拿到，Loader 做的一切都白费了
            original_metadata = doc.get("metadata", {}) 
            
            # 所有类型的文档都进行切分
            chunks = self.split_text(content)
            
            for i, chunk in enumerate(chunks):
                # === [核心修复点 2] 必须为每个块复制一份 metadata ===
                chunk_metadata = original_metadata.copy()
                
                chunk_data = {
                    "content": chunk,
                    "filename": doc.get("filename", "unknown"),
                    "filepath": doc.get("filepath", ""),
                    "filetype": filetype,
                    "page_number": doc.get("page_number", 0),
                    "chunk_id": i,
                    "images": doc.get("images", []),
                    # === [核心修复点 3] 必须显式传递这个字段 ===
                    "metadata": chunk_metadata 
                }
                chunks_with_metadata.append(chunk_data)

        print(f"\n文档处理完成，共 {len(chunks_with_metadata)} 个块")
        return chunks_with_metadata
