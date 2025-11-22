#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   VectorBase.py
@Time    :   2025/11/10
@Ref   :   不要葱姜蒜
'''

import os
from typing import Any, Dict, List, Optional, Tuple, Union
import json
from Embeddings import BaseEmbeddings, OpenAIEmbedding
import numpy as np
from tqdm import tqdm


class VectorStore:
    # ❗ 1. 修改 __init__ 接受新的文档结构
    def __init__(self, document: List[Dict[str, Any]] = [{'content': '', 'lang': 'zh'}]) -> None:
        self.document = document
        self.vectors: List[List[float]] = [] # 预设 vectors 属性

    # ❗ 2. get_vector 已在您的 snippet 中修改正确，无需再次修改
    def get_vector(self, EmbeddingModel: BaseEmbeddings) -> List[List[float]]:
        self.vectors = []
        # 迭代 document 中的字典，取出 'content'
        for doc_dict in tqdm(self.document, desc="Calculating embeddings"):
            self.vectors.append(EmbeddingModel.get_embedding(doc_dict['content']))
        return self.vectors

    # ❗ 3. 修改 persist 方法，确保 document 是 List[Dict] 能够被正确存储
    def persist(self, path: str = 'storage'):
        if not os.path.exists(path):
            os.makedirs(path)
        # document 现在是 List[Dict]，可以直接存储
        with open(f"{path}/doecment.json", 'w', encoding='utf-8') as f:
            json.dump(self.document, f, ensure_ascii=False)
        if self.vectors:
            with open(f"{path}/vectors.json", 'w', encoding='utf-8') as f:
                json.dump(self.vectors, f)

    # ❗ 4. 修改 load_vector 方法，确保 document 加载后是 List[Dict]
    def load_vector(self, path: str = 'storage'):
        # ... (与 persist 对应，加载 vectors 和 document)
        with open(f"{path}/vectors.json", 'r', encoding='utf-8') as f:
            self.vectors = json.load(f)
        with open(f"{path}/doecment.json", 'r', encoding='utf-8') as f:
            self.document = json.load(f)

    def get_similarity(self, vector1: List[float], vector2: List[float]) -> float:
        return BaseEmbeddings.cosine_similarity(vector1, vector2)

    # ❗ 5. 修改 query 方法，增加 LLM 相关的参数
    def query(self, query: str, EmbeddingModel: BaseEmbeddings, 
              llm_translator_class, llm_instance, # 接收 LLM 类和实例
              k: int = 4) -> List[Dict[str, Union[str, float]]]:
        """
        查询向量存储，支持多语言动态查询翻译。
        """
        if not self.vectors:
            return []

        best_similarity_scores = []
        query_vector_cache = {} # 缓存翻译后的查询向量
        
        # 遍历所有文档块
        for i, doc_dict in enumerate(self.document):
            # 获取文档语言，默认 'zh'
            doc_lang = doc_dict.get('lang', 'zh') 
            doc_vector = self.vectors[i]

            # 1. 动态翻译查询并获取嵌入向量
            if doc_lang not in query_vector_cache:
                # 调用 LLM.py 中实现的翻译方法（使用传入的 LLM 类）
                translated_query = llm_translator_class.translate_query(
                    llm_instance, query, doc_lang
                )
                
                # BGE 嵌入翻译后的查询
                query_vector = EmbeddingModel.get_embedding(translated_query)
                query_vector_cache[doc_lang] = query_vector
            else:
                query_vector = query_vector_cache[doc_lang] # 从缓存中获取

            # 2. 计算相似度 (用翻译后的查询向量对原始文档向量)
            score = self.get_similarity(query_vector, doc_vector)
            
            # (得分, 原始索引, 文档语言)
            best_similarity_scores.append((score, i, doc_lang))

        # 3. 排序并返回Top K
        best_similarity_scores.sort(key=lambda x: x[0], reverse=True)

        results = []
        for score, original_index, doc_lang in best_similarity_scores[:k]:
            results.append({
                'content': self.document[original_index]['content'], # 取出原始文档内容
                'similarity': score,
                'lang': doc_lang # 附加语言标签
            })
            
        return results