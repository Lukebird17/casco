#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   VectorBase.py
@Time    :   2025/11/10
@Ref   :   不要葱姜蒜
'''

import os
from typing import Dict, List, Optional, Tuple, Union
import json
from Embeddings import BaseEmbeddings, OpenAIEmbedding
import numpy as np
from tqdm import tqdm


class VectorStore:
    def __init__(self, document: List[str] = [''], sources: Optional[List[str]] = None) -> None:
        """
        初始化向量存储
        
        Args:
            document: 文档列表
            sources: 文档来源列表（文件名），与document一一对应
        """
        self.document = document
        # 如果没有提供sources，默认为None
        self.sources = sources if sources is not None else [None] * len(document)

    def get_vector(self, EmbeddingModel: BaseEmbeddings) -> List[List[float]]:
        
        self.vectors = []
        for doc in tqdm(self.document, desc="Calculating embeddings"):
            self.vectors.append(EmbeddingModel.get_embedding(doc))
        return self.vectors

    def persist(self, path: str = 'storage'):
        if not os.path.exists(path):
            os.makedirs(path)
        with open(f"{path}/doecment.json", 'w', encoding='utf-8') as f:
            json.dump(self.document, f, ensure_ascii=False)
        if self.vectors:
            with open(f"{path}/vectors.json", 'w', encoding='utf-8') as f:
                json.dump(self.vectors, f)
        # 保存来源信息
        if self.sources:
            with open(f"{path}/sources.json", 'w', encoding='utf-8') as f:
                json.dump(self.sources, f, ensure_ascii=False)

    def load_vector(self, path: str = 'storage'):
        with open(f"{path}/vectors.json", 'r', encoding='utf-8') as f:
            self.vectors = json.load(f)
        with open(f"{path}/doecment.json", 'r', encoding='utf-8') as f:
            self.document = json.load(f)
        # 加载来源信息（如果存在）
        sources_path = f"{path}/sources.json"
        if os.path.exists(sources_path):
            with open(sources_path, 'r', encoding='utf-8') as f:
                self.sources = json.load(f)
        else:
            self.sources = [None] * len(self.document)

    def get_similarity(self, vector1: List[float], vector2: List[float]) -> float:
        return BaseEmbeddings.cosine_similarity(vector1, vector2)

    def query(self, query: str, EmbeddingModel: BaseEmbeddings, k: int = 1) -> List[str]:
        """
        查询文档（兼容旧版本，只返回文档内容）
        
        Args:
            query: 查询文本
            EmbeddingModel: 向量模型
            k: 返回的文档数量
            
        Returns:
            文档内容列表
        """
        query_vector = EmbeddingModel.get_embedding(query)
        result = np.array([self.get_similarity(query_vector, vector)
                          for vector in self.vectors])
        return np.array(self.document)[result.argsort()[-k:][::-1]].tolist()
    
    def query_with_source(self, query: str, EmbeddingModel: BaseEmbeddings, k: int = 1) -> List[Dict]:
        """
        查询文档（返回文档内容和来源）
        
        Args:
            query: 查询文本
            EmbeddingModel: 向量模型
            k: 返回的文档数量
            
        Returns:
            包含content和source的字典列表
        """
        query_vector = EmbeddingModel.get_embedding(query)
        similarities = np.array([self.get_similarity(query_vector, vector)
                                for vector in self.vectors])
        
        # 获取top-k的索引
        top_k_indices = similarities.argsort()[-k:][::-1]
        
        results = []
        for idx in top_k_indices:
            results.append({
                'content': self.document[idx],
                'source': self.sources[idx] if self.sources and idx < len(self.sources) else None,
                'similarity': float(similarities[idx])
            })
        
        return results
