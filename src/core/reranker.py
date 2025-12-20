"""
Rerank模块
使用API提供的Rerank模型对检索结果进行重排序
"""

from typing import List, Dict
import requests
from config import OPENAI_API_KEY, OPENAI_API_BASE, RERANK_MODEL_NAME


class Reranker:
    """使用API的Rerank模型进行结果重排序"""
    
    def __init__(self, api_key: str = OPENAI_API_KEY, api_base: str = OPENAI_API_BASE):
        self.api_key = api_key
        self.api_base = api_base.rstrip('/')
        self.model = RERANK_MODEL_NAME
        
    def rerank(
        self, 
        query: str, 
        documents: List[Dict], 
        top_k: int = None
    ) -> List[Dict]:
        """
        对检索结果进行重排序
        
        Args:
            query: 用户查询
            documents: 检索到的文档列表
            top_k: 返回前k个结果（None则返回全部）
            
        Returns:
            重排序后的文档列表（添加了rerank_score字段）
        """
        if not documents:
            return []
        
        try:
            # 准备文档文本
            doc_texts = []
            for doc in documents:
                # 提取文档文本内容
                if 'content' in doc:
                    text = doc['content']
                elif 'text' in doc:
                    text = doc['text']
                elif 'description' in doc:  # 图片描述
                    text = doc['description']
                else:
                    text = str(doc)
                
                doc_texts.append(text[:500])  # 限制长度以提高速度
            
            # 调用Rerank API
            print(f"  🔄 Rerank: 对 {len(doc_texts)} 个结果进行重排序...")
            
            # 使用标准的rerank API格式
            response = requests.post(
                f"{self.api_base}/rerank",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": self.model,
                    "query": query,
                    "documents": doc_texts,
                    "top_n": top_k if top_k else len(doc_texts),
                    "return_documents": False  # 只返回索引和分数
                },
                timeout=30
            )
            
            if response.status_code != 200:
                print(f"  ⚠️  Rerank API失败 (状态码{response.status_code})，使用原始排序")
                return documents[:top_k] if top_k else documents
            
            result = response.json()
            
            # 解析rerank结果
            if 'results' in result:
                reranked_results = result['results']
                
                # 按rerank分数重新排序
                reranked_docs = []
                for item in reranked_results:
                    idx = item.get('index', 0)
                    score = item.get('relevance_score', 0.0)
                    
                    if 0 <= idx < len(documents):
                        doc = documents[idx].copy()
                        doc['rerank_score'] = score
                        reranked_docs.append(doc)
                
                print(f"  ✅ Rerank完成: {len(reranked_docs)} 个结果")
                top3_scores = [f"{d.get('rerank_score', 0):.3f}" for d in reranked_docs[:3]]
                print(f"     Top3分数: {top3_scores}")
                
                return reranked_docs[:top_k] if top_k else reranked_docs
            
            # 如果API格式不符，返回原始结果
            print(f"  ⚠️  Rerank响应格式异常，使用原始排序")
            return documents[:top_k] if top_k else documents
            
        except requests.exceptions.Timeout:
            print(f"  ⚠️  Rerank超时，使用原始排序")
            return documents[:top_k] if top_k else documents
        except Exception as e:
            print(f"  ⚠️  Rerank失败: {e}，使用原始排序")
            import traceback
            traceback.print_exc()
            return documents[:top_k] if top_k else documents


if __name__ == "__main__":
    # 测试
    reranker = Reranker()
    
    test_query = "什么是虚拟内存"
    test_docs = [
        {"content": "虚拟内存是操作系统的重要概念", "id": 1},
        {"content": "页表用于地址转换", "id": 2},
        {"content": "进程管理是操作系统的核心", "id": 3},
    ]
    
    result = reranker.rerank(test_query, test_docs, top_k=2)
    for doc in result:
        print(f"ID: {doc['id']}, Score: {doc.get('rerank_score', 0):.3f}, Content: {doc['content']}")

