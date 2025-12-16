import re
import numpy as np
from typing import List
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from LLM import OpenAIChat

def enhance_query(llm, query: str) -> List[str]:
    """
    查询增强：生成多个检索查询，同时使用LLM生成更复杂的子问题，并加入原问题以防止退行
    Args:
        llm: 已初始化的 LLM 实例（例如 OpenAIChat）
        query: 原始查询
    Returns:
        增强后的查询列表
    """
    queries = [query]
    
    # 1. 提取括号、引号、《》中的内容，并限制关键词数量
    keywords = extract_keywords(query)
    queries.extend(keywords)
    
    # 2. 使用 LLM 扩展查询
    try:
        # 调用 LLM 来生成复杂查询
        prompt = f"""
        你是一个专业的检索增强生成(RAG)查询改写专家。
        请基于用户问题，生成 3-5 个**尽可能详细、包含完整上下文的搜索长句**。请生成包括不同城市的相关查询，如“南京地铁S7号线”，并对比其他城市（例如：苏州市、泰州市等）的地铁情况。

        【核心原则】
        1. **拒绝短词**：不要把问题切碎成单词，要保留词组搭配。
        2. **集合展开**：如果涉及集合中排名（如"江苏省内地铁"），请具体展开主要成员(无锡,徐州,常州,苏州,南通,连云港,淮安,盐城,扬州,镇江,泰州,宿迁)。
        3. **版本对比**: 如果涉及两个及以上文档对比，分别检索两个文档对应定义，再融合。

        【示例】
                Input: "比较 SUBSET-026 Baseline 3 和 4 中 Packet 11 的定义"
                Output:
                SUBSET-026 Baseline 3 Packet 11 definition details
                SUBSET-026 Baseline 4 Packet 11 structure and content
                Difference of Packet 11 between Baseline 3 and Baseline 4

        用户问题："{query}"
        输出（每行一个）：  
        """
        
        # 调用 LLM 完成查询扩展
        response = llm.chat(prompt, [], "")
        sub_queries = [line.strip() for line in response.split('\n') if line.strip()]
        
        # 去重：计算相似度并删除相似度高的重复查询
        sub_queries = remove_similar_queries(sub_queries, threshold=0.8)
        
        # 将生成的子查询按顺序添加到queries列表，最后一个查询包含原始问题
        for i, q in enumerate(sub_queries):
            if i == len(sub_queries) - 1:  # 只有最后一条子查询加入原始查询
                queries.append(f"{q} {query}")
            else:
                queries.append(q)
    except Exception as e:
        print(f"[enhance_query Warning] LLM generation failed: {e}")
    
    # 3. 去重，避免相同查询
    return list(set(queries))  # 去重返回

# 1. 提取关键词

# def enhance_query(llm, query: str) -> List[str]:
#     queries = [query]
#     keywords = extract_keywords(query)
#     queries.extend(keywords)
    
#     # 2. 简单拆分：按逗号和问号拆分子句
#     # 很多时候长句中的逗号分隔了独立的子问题或限定条件
#     simple_splits = re.split(r'[，,？?]', query)
#     # 过滤过短的片段（例如少于4个字），保留有意义的短语
#     simple_splits = [s.strip() for s in simple_splits if len(s.strip()) > 4]
#     queries.extend(simple_splits)
    
#     # 3. 使用 LLM 扩展查询
#     try:
#         prompt = f"""
#         你是一个专业的检索增强生成(RAG)查询改写专家。
#           请基于用户问题，生成 3-5 个**尽可能详细、包含完整上下文的搜索长句**。请生成包括不同城市的相关查询，如“南京地铁S7号线”，并对比其他城市（例如：苏州市、泰州市等）的地铁情况。

#           【核心原则】
#           1. **拒绝短词**：不要把问题切碎成单词，要保留词组搭配。
#           2. **集合展开**：如果涉及集合中排名（如"江苏省内地铁"），请具体展开主要成员(无锡,徐州,常州,苏州,南通,连云港,淮安,盐城,扬州,镇江,泰州,宿迁)。
#           3. **版本对比**: 如果涉及两个及以上文档对比，分别检索两个文档对应定义，再融合。

#           【示例】
#                   Input: "比较 SUBSET-026 Baseline 3 和 4 中 Packet 11 的定义"
#                   Output:
#                   SUBSET-026 Baseline 3 Packet 11 definition details
#                   SUBSET-026 Baseline 4 Packet 11 structure and content
#                   Difference of Packet 11 between Baseline 3 and Baseline 4

#           用户问题："{query}"
#           输出（每行一个）：  
#           """
        
#         response = llm.chat(prompt, [], "")
#         sub_queries = [line.strip() for line in response.split('\n') if line.strip()]
        
#         # 将生成的子查询添加到列表
#         queries.extend(sub_queries)
        
#     except Exception as e:
#         print(f"[enhance_query Warning] LLM generation failed: {e}")
    
#     # 4. 最终去重
#     # 使用简单的字符串去重，为了保留多样性，这里不做过于激进的相似度去除，
#     # 依赖后续检索阶段的重排序(Rerank)来筛选最佳结果。
#     unique_queries = list(set(queries))
    
#     return unique_queries

def remove_similar_queries(queries: List[str], threshold: float = 0.8) -> List[str]:
        """
        去除相似度高的查询，避免重复的查询。
        Args:
            queries: 待处理的查询列表
            threshold: 相似度阈值
        Returns:
            去重后的查询列表
        """
        # 使用TF-IDF向量化查询
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(queries)
        
        # 计算余弦相似度
        cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
        
        # 去除相似度高于阈值的查询
        to_remove = set()
        for i in range(len(cosine_sim)):
            for j in range(i+1, len(cosine_sim)):
                if cosine_sim[i][j] > threshold:
                    to_remove.add(j)  # 标记为重复的查询
        
        # 保留未被标记为重复的查询
        return [queries[i] for i in range(len(queries)) if i not in to_remove]


def extract_keywords(query: str) -> List[str]:
    """
    提取关键词：括号、引号、《》中的内容，以及英文、德文、西班牙文的整体词组。
    Args:
        query: 查询文本
    Returns:
        提取的关键词列表（限制为最多4个关键词）
    """
    keywords = []
    
    # 提取括号、引号、《》中的内容
    patterns = [r'\[(.*?)\]', r'\'(.*?)\'', r'\"(.*?)\"', r'《(.*?)》']
    for pattern in patterns:
        matches = re.findall(pattern, query)
        keywords.extend(matches)
    
    # 提取英文、德文、西班牙文的词组（确保只提取整体词组）
    foreign_patterns = [r'\b[A-Za-z]+(?:[-][A-Za-z]+)*\b']
    for pattern in foreign_patterns:
        matches = re.findall(pattern, query)
        keywords.extend(matches)
    keywords = list(set(keywords))
    print("keywords:", keywords)
    # 只返回最多4个关键词
    return keywords[:4]

# 示例如何调用 LLM 实例来生成查询
if __name__ == "__main__":
    # 你应该在这里初始化你的 LLM 实例，例如 OpenAIChat
    # 例如：llm = OpenAIChat(api_key="your-api-key")
    llm = OpenAIChat()  # 假设这是一个已经初始化好的实例
    
    query = "南京地铁 S7 号线的运营里程，在江苏省内已运营地铁长度中排第几？"
    enhanced_queries = enhance_query(llm, query)
    
    print("Enhanced Queries:")
    for q in enhanced_queries:
        print(q)
