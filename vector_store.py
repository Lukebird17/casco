import os
from typing import List, Dict

import chromadb
from chromadb.config import Settings
from openai import OpenAI
from tqdm import tqdm

from config import (
    VECTOR_DB_PATH,
    COLLECTION_NAME,
    OPENAI_API_KEY,
    OPENAI_API_BASE,
    OPENAI_EMBEDDING_MODEL,
    TOP_K,
)


class VectorStore:

    def __init__(
        self,
        db_path: str = VECTOR_DB_PATH,
        collection_name: str = COLLECTION_NAME,
        api_key: str = OPENAI_API_KEY,
        api_base: str = OPENAI_API_BASE,
    ):
        self.db_path = db_path
        self.collection_name = collection_name

        # 初始化OpenAI客户端
        self.client = OpenAI(api_key=api_key, base_url=api_base)

        # 初始化ChromaDB
        os.makedirs(db_path, exist_ok=True)
        self.chroma_client = chromadb.PersistentClient(
            path=db_path, settings=Settings(anonymized_telemetry=False)
        )

        # 获取或创建collection
        self.collection = self.chroma_client.get_or_create_collection(
            name=collection_name, metadata={"description": "课程材料向量数据库"}
        )

    def get_embedding(self, text: str) -> List[float]:
        """获取文本的向量表示

        使用OpenAI API获取文本的embedding向量
        """
        try:
            # 清理文本：移除多余的换行和空格
            text = text.replace("\n", " ").strip()
            
            # 调用OpenAI Embedding API
            response = self.client.embeddings.create(
                input=text,
                model=OPENAI_EMBEDDING_MODEL
            )
            
            # 返回向量
            return response.data[0].embedding
        
        except Exception as e:
            print(f"获取embedding失败: {e}")
            # 返回零向量作为fallback（实际应用中应该更好地处理）
            return [0.0] * 1536  # text-embedding-3-small的维度是1536

    def add_documents(self, chunks: List[Dict[str, str]]) -> None:
        """添加文档块到向量数据库
        要求：
        1. 遍历文档块
        2. 获取文档块内容
        3. 获取文档块元数据
        4. 打印添加进度
        """
        print(f"\n开始向量化并存储 {len(chunks)} 个文档块...")
        
        # 批量处理以提高效率
        batch_size = 10
        
        for i in tqdm(range(0, len(chunks), batch_size), desc="添加文档"):
            batch_chunks = chunks[i:i + batch_size]
            
            # 准备批次数据
            ids = []
            documents = []
            embeddings = []
            metadatas = []
            
            for idx, chunk in enumerate(batch_chunks):
                # 生成唯一ID
                doc_id = f"{chunk['filename']}_page{chunk['page_number']}_chunk{chunk['chunk_id']}_{i+idx}"
                ids.append(doc_id)
                
                # 文档内容
                documents.append(chunk['content'])
                
                # 获取embedding
                embedding = self.get_embedding(chunk['content'])
                embeddings.append(embedding)
                
                # 元数据
                metadata = {
                    'filename': chunk['filename'],
                    'filepath': chunk['filepath'],
                    'filetype': chunk['filetype'],
                    'page_number': chunk['page_number'],
                    'chunk_id': chunk['chunk_id']
                }
                metadatas.append(metadata)
            
            # 批量添加到ChromaDB
            try:
                self.collection.add(
                    ids=ids,
                    documents=documents,
                    embeddings=embeddings,
                    metadatas=metadatas
                )
            except Exception as e:
                print(f"添加批次失败: {e}")
        
        print(f"✅ 成功添加 {len(chunks)} 个文档块到向量数据库")

    def search(self, query: str, top_k: int = TOP_K) -> List[Dict]:
        """搜索相关文档

        要求：
        1. 首先获取查询文本的embedding向量（调用self.get_embedding）
        2. 使用self.collection进行向量搜索, 得到top_k个结果
        3. 格式化返回结果，每个结果包含：
           - content: 文档内容
           - metadata: 元数据（文件名、页码等）
        4. 返回格式化的结果列表
        """
        try:
            # 1. 获取查询的embedding
            query_embedding = self.get_embedding(query)
            
            # 2. 使用ChromaDB进行向量搜索
            results = self.collection.query(
                query_embeddings=[query_embedding],
                n_results=top_k,
                include=['documents', 'metadatas', 'distances']
            )
            
            # 3. 格式化返回结果
            formatted_results = []
            
            if results and results['documents'] and len(results['documents']) > 0:
                documents = results['documents'][0]  # 第一个查询的结果
                metadatas = results['metadatas'][0]
                distances = results['distances'][0]
                
                for doc, metadata, distance in zip(documents, metadatas, distances):
                    formatted_results.append({
                        'content': doc,
                        'metadata': metadata,
                        'distance': distance,  # 相似度分数（越小越相似）
                        'filename': metadata.get('filename', 'unknown'),
                        'page_number': metadata.get('page_number', 0),
                        'filetype': metadata.get('filetype', 'unknown')
                    })
            
            return formatted_results
        
        except Exception as e:
            print(f"搜索失败: {e}")
            return []

    def clear_collection(self) -> None:
        """清空collection"""
        self.chroma_client.delete_collection(name=self.collection_name)
        self.collection = self.chroma_client.create_collection(
            name=self.collection_name, metadata={"description": "课程向量数据库"}
        )
        print("向量数据库已清空")

    def get_collection_count(self) -> int:
        """获取collection中的文档数量"""
        return self.collection.count()
