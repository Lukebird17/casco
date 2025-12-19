import os
from typing import List, Dict, Optional

import chromadb
from chromadb.config import Settings
from openai import OpenAI
from tqdm import tqdm
import jieba  # 中文分词
from rank_bm25 import BM25Okapi  # BM25算法

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
        
        # ==========================================
        # 新增: BM25 索引构建逻辑
        # ==========================================
        self.bm25_model = None
        self.bm25_corpus_map = []  # 用于通过BM25索引找回原始文档
        self._build_bm25_index()

    def _tokenize(self, text: str) -> List[str]:
        """中文分词工具（用于BM25）"""
        # 使用搜索引擎模式，切分得更细，提高召回率
        return list(jieba.cut_for_search(text))

    def _build_bm25_index(self):
        """从 ChromaDB 加载所有数据并构建 BM25 索引"""
        try:
            count = self.collection.count()
            if count == 0:
                print("⚠️  向量库为空，跳过 BM25 索引构建")
                return

            print(f"🔄 正在构建 BM25 索引 (共 {count} 条数据)...")
            
            # 一次性拉取所有文档（如果数据量达到百万级，这里需要改为分页拉取）
            result = self.collection.get(include=['documents', 'metadatas'])
            
            tokenized_corpus = []
            self.bm25_corpus_map = []
            
            # 遍历构建
            for i, doc_content in enumerate(result['documents']):
                if not doc_content:
                    continue
                
                # 分词
                tokens = self._tokenize(doc_content)
                tokenized_corpus.append(tokens)
                
                # 建立映射: BM25 index -> 原始数据
                self.bm25_corpus_map.append({
                    "content": doc_content,
                    "metadata": result['metadatas'][i]
                })
            
            # 初始化 BM25Okapi
            if tokenized_corpus:
                self.bm25_model = BM25Okapi(tokenized_corpus)
                print("✅ BM25 索引构建完成")
            
        except Exception as e:
            print(f"❌ BM25 构建失败: {e}")

    def get_embedding(self, text: str) -> List[float]:
        """获取文本的向量表示

        使用OpenAI API获取文本的embedding向量
        """
        try:
            # 清理文本：移除多余的换行和空格
            text = text.replace("\n", " ").strip()
            
            # 如果文本为空，返回 None
            if not text:
                return None
            
            # 调用OpenAI Embedding API
            response = self.client.embeddings.create(
                input=text,
                model=OPENAI_EMBEDDING_MODEL
            )
            
            # 返回向量
            return response.data[0].embedding
        
        except Exception as e:
            print(f"⚠️  获取embedding失败: {e}")
            # 返回 None 表示失败，调用者应该跳过这个文档
            return None

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
        
        skipped_count = 0
        
        for i in tqdm(range(0, len(chunks), batch_size), desc="添加文档"):
            batch_chunks = chunks[i:i + batch_size]
            
            # 准备批次数据
            ids = []
            documents = []
            embeddings = []
            metadatas = []
            
            for idx, chunk in enumerate(batch_chunks):
                # 获取embedding
                embedding = self.get_embedding(chunk['content'])
                
                # 如果 embedding 为 None，跳过这个文档
                if embedding is None:
                    skipped_count += 1
                    continue
                
                # 生成唯一ID
                doc_id = f"{chunk['filename']}_page{chunk['page_number']}_chunk{chunk['chunk_id']}_{i+idx}"
                ids.append(doc_id)
                
                # 文档内容
                documents.append(chunk['content'])
                embeddings.append(embedding)
                
                # 元数据（支持image_url）
                source_meta = chunk.get('metadata', {})
                image_url = source_meta.get('image_url', '')
                
                metadata = {
                    'filename': chunk['filename'],
                    'filepath': chunk['filepath'],
                    'filetype': chunk['filetype'],
                    'page_number': chunk['page_number'],
                    'chunk_id': chunk['chunk_id'],
                    'image_url': image_url  # 支持图片URL
                }
                metadatas.append(metadata)
            
            # 如果这个批次没有有效数据，跳过
            if not ids:
                continue
            
            # 批量添加到ChromaDB
            try:
                # 重新获取 collection 引用以确保有效
                self.collection = self.chroma_client.get_or_create_collection(
                    name=self.collection_name, 
                    metadata={"description": "课程材料向量数据库"}
                )
                
                self.collection.add(
                    ids=ids,
                    documents=documents,
                    embeddings=embeddings,
                    metadatas=metadatas
                )
            except Exception as e:
                print(f"❌ 添加批次失败: {e}")
                skipped_count += len(ids)
        
        success_count = len(chunks) - skipped_count
        print(f"✅ 成功添加 {success_count} 个文档块到向量数据库")
        if skipped_count > 0:
            print(f"⚠️  跳过 {skipped_count} 个文档块（embedding 失败或文本过长）")
        
        # 重建BM25索引
        self._build_bm25_index()

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
            
            # 如果 embedding 失败，返回空结果
            if query_embedding is None:
                print("❌ 查询 embedding 失败")
                return []
            
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
    
    def search_bm25(self, query: str, top_k: int = TOP_K) -> List[Dict]:
        """【新增】BM25 关键词检索
        
        Args:
            query: 查询文本
            top_k: 返回结果数量
            
        Returns:
            检索结果列表
        """
        if not self.bm25_model:
            return []
        
        try:
            # 1. 对查询分词
            tokenized_query = self._tokenize(query)
            
            # 2. 获取分数
            doc_scores = self.bm25_model.get_scores(tokenized_query)
            
            # 3. 获取 TopK 索引
            # argsort 并取反切片
            top_n_indexes = sorted(
                range(len(doc_scores)), 
                key=lambda i: doc_scores[i], 
                reverse=True
            )[:top_k]
            
            results = []
            for idx in top_n_indexes:
                score = doc_scores[idx]
                # 过滤掉得分为0的结果（完全不匹配）
                if score <= 0:
                    continue
                
                doc_info = self.bm25_corpus_map[idx]
                results.append({
                    'content': doc_info['content'],
                    'metadata': doc_info['metadata'],
                    'score': score,  # BM25 分数
                    'filename': doc_info['metadata'].get('filename', 'unknown'),
                    'page_number': doc_info['metadata'].get('page_number', 0),
                    'filetype': doc_info['metadata'].get('filetype', 'unknown'),
                    'type': 'bm25'
                })
            return results
        except Exception as e:
            print(f"❌ BM25 搜索失败: {e}")
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
