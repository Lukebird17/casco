#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
混合检索器（Hybrid Retriever）
同时检索文本和图片，支持多模态查询
"""

from typing import List, Dict, Optional, Union
from pathlib import Path

from vector_store import VectorStore
from image_vector_store import ImageVectorStore
from config import TOP_K


class HybridRetriever:
    """
    混合检索器
    支持文本和图片的联合检索，返回多模态结果
    """
    
    def __init__(
        self,
        text_store: Optional[VectorStore] = None,
        image_store: Optional[ImageVectorStore] = None,
        text_weight: float = 0.6,
        image_weight: float = 0.4,
    ):
        """
        初始化混合检索器
        
        Args:
            text_store: 文本向量存储
            image_store: 图片向量存储
            text_weight: 文本检索权重（0-1）
            image_weight: 图片检索权重（0-1）
        """
        self.text_store = text_store or VectorStore()
        self.image_store = image_store or ImageVectorStore()
        self.text_weight = text_weight
        self.image_weight = image_weight
        
        # 验证权重
        if abs(text_weight + image_weight - 1.0) > 0.01:
            print(f"⚠️  权重之和不为1，已自动归一化")
            total = text_weight + image_weight
            self.text_weight = text_weight / total
            self.image_weight = image_weight / total
    
    def search(
        self, 
        query: Union[str, Dict],
        top_k: int = TOP_K,
        text_k: Optional[int] = None,
        image_k: Optional[int] = None,
        include_images: bool = True,
    ) -> Dict:
        """
        混合检索（文本 + 图片）
        
        Args:
            query: 查询内容
                - str: 纯文本查询
                - Dict: 多模态查询 {"text": "...", "image": "path/to/image"}
            top_k: 总共返回的结果数
            text_k: 文本检索数量（默认为 top_k * text_weight）
            image_k: 图片检索数量（默认为 top_k * image_weight）
            include_images: 是否包含图片结果
            
        Returns:
            {
                "text_results": [...],  # 文本检索结果
                "image_results": [...], # 图片检索结果
                "combined": [...]       # 混合排序后的结果
            }
        """
        # 解析查询
        text_query = None
        image_query = None
        
        if isinstance(query, str):
            text_query = query
        elif isinstance(query, dict):
            text_query = query.get("text")
            image_query = query.get("image")
        
        # 确定检索数量
        if text_k is None:
            text_k = max(1, int(top_k * self.text_weight))
        if image_k is None:
            image_k = max(1, int(top_k * self.image_weight))
        
        results = {
            "text_results": [],
            "image_results": [],
            "combined": []
        }
        
        # 1. 文本检索
        if text_query:
            try:
                print(f"  🔎 HybridRetriever: 开始文本检索, query='{text_query}', top_k={text_k}")
                text_results = self.text_store.search(text_query, top_k=text_k)
                print(f"  ✅ HybridRetriever: 文本检索返回 {len(text_results)} 个结果")
                results["text_results"] = text_results
            except Exception as e:
                print(f"⚠️  文本检索失败: {e}")
                import traceback
                traceback.print_exc()
        
        # 2. 图片检索
        if include_images:
            try:
                print(f"  🖼️  HybridRetriever: 开始图片检索, image_k={image_k}")
                if image_query:
                    # 以图搜图
                    image_results = self.image_store.search_by_text(image_query, top_k=image_k)
                elif text_query:
                    # 以文搜图
                    image_results = self.image_store.search_by_text(text_query, top_k=image_k)
                else:
                    image_results = []
                
                print(f"  ✅ HybridRetriever: 图片检索返回 {len(image_results)} 个结果")
                results["image_results"] = image_results
            except Exception as e:
                print(f"⚠️  图片检索失败: {e}")
                import traceback
                traceback.print_exc()
        
        # 3. 合并结果
        print(f"  🔀 HybridRetriever: 合并结果, 文本={len(results['text_results'])}, 图片={len(results['image_results'])}")
        results["combined"] = self._merge_results(
            results["text_results"],
            results["image_results"],
            top_k
        )
        print(f"  ✅ HybridRetriever: 合并后共 {len(results['combined'])} 个结果")
        
        return results
    
    def _merge_results(
        self,
        text_results: List[Dict],
        image_results: List[Dict],
        top_k: int
    ) -> List[Dict]:
        """
        合并文本和图片检索结果
        
        策略：交替插入，保持多样性
        例如：[文本1, 图片1, 文本2, 图片2, 文本3, ...]
        
        Args:
            text_results: 文本检索结果
            image_results: 图片检索结果
            top_k: 返回数量
            
        Returns:
            合并后的结果列表
        """
        combined = []
        text_idx = 0
        image_idx = 0
        
        # 交替插入
        while len(combined) < top_k and (text_idx < len(text_results) or image_idx < len(image_results)):
            # 插入文本
            if text_idx < len(text_results):
                combined.append({
                    **text_results[text_idx],
                    'type': 'text',
                    'rank': len(combined) + 1
                })
                text_idx += 1
            
            # 插入图片
            if len(combined) < top_k and image_idx < len(image_results):
                combined.append({
                    **image_results[image_idx],
                    'type': 'image',
                    'rank': len(combined) + 1
                })
                image_idx += 1
        
        return combined[:top_k]
    
    def format_context_for_llm(self, results: Dict, max_length: int = 4000) -> List[Dict]:
        """
        将检索结果格式化为适合 LLM 的多模态 context
        
        Args:
            results: search() 返回的结果
            max_length: 文本内容最大长度
            
        Returns:
            多模态 context 列表，格式：
            [
                {"type": "text", "content": "..."},
                {"type": "image", "path": "...", "description": "..."},
                ...
            ]
        """
        context = []
        current_text_length = 0
        
        for item in results["combined"]:
            if item['type'] == 'text':
                # 文本内容
                content = item.get('content', '')
                
                # 检查长度限制
                if current_text_length + len(content) > max_length:
                    # 截断
                    remaining = max_length - current_text_length
                    if remaining > 100:  # 至少保留100字符
                        content = content[:remaining] + "..."
                    else:
                        break  # 超出限制，停止添加
                
                context.append({
                    "type": "text",
                    "content": content,
                    "source": f"{item.get('filename', 'unknown')} (页{item.get('page_number', 0)})"
                })
                current_text_length += len(content)
                
            elif item['type'] == 'image':
                # 图片内容
                context.append({
                    "type": "image",
                    "path": item.get('image_path', ''),
                    "description": item.get('description', ''),
                    "source": f"{item.get('filename', 'unknown')} (页{item.get('page_number', 0)})"
                })
        
        return context
    
    def get_stats(self) -> Dict:
        """获取统计信息"""
        return {
            "text_documents": self.text_store.get_collection_count(),
            "images": self.image_store.get_collection_count(),
            "text_weight": self.text_weight,
            "image_weight": self.image_weight,
        }


if __name__ == "__main__":
    # 测试代码
    print("=== 测试混合检索器 ===\n")
    
    retriever = HybridRetriever()
    
    # 测试纯文本查询
    print("测试1: 纯文本查询")
    results = retriever.search("虚拟内存的页表结构", top_k=5)
    print(f"  文本结果: {len(results['text_results'])}")
    print(f"  图片结果: {len(results['image_results'])}")
    print(f"  合并结果: {len(results['combined'])}")
    
    # 格式化为 LLM context
    context = retriever.format_context_for_llm(results)
    print(f"\n  LLM Context 项数: {len(context)}")
    for idx, item in enumerate(context[:3], 1):
        print(f"    {idx}. {item['type']}: {item.get('source', 'N/A')}")

