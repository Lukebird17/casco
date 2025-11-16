#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   config.py
@Time    :   2025/11/15
@Desc    :   配置文件 - 调整参数以优化性能和token消耗
'''

# ========== 文档处理配置 ==========
# 文档分块配置
CHUNK_CONFIG = {
    # 基础配置
    'max_token_len': 400,      # 每个chunk的最大token数（降低可减少token消耗）
    'cover_content': 50,       # chunk之间的重叠token数（确保上下文连续性）
    
    # 针对不同文件类型的配置
    'pdf': {
        'max_token_len': 500,  # PDF通常结构更复杂，需要更大的chunk
        'cover_content': 80,
    },
    'markdown': {
        'max_token_len': 400,
        'cover_content': 50,
    }
}

# ========== 检索配置 ==========
RETRIEVAL_CONFIG = {
    # 基础题检索配置
    'basic': {
        'k': 3,                # 初始检索数量
        'rerank_top_k': 3,     # 重排序后保留的数量
        'multi_query': True,   # 是否使用多查询增强
    },
    
    # 中级题检索配置
    'intermediate': {
        'k': 8,
        'rerank_top_k': 5,
        'multi_query': True,
    },
    
    # 高级题检索配置
    'advanced': {
        'k': 10,
        'rerank_top_k': 8,
        'multi_query': True,
        'multi_round': True,   # 是否使用多轮检索
    }
}

# ========== LLM配置 ==========
LLM_CONFIG = {
    # 模型选择（根据评测规则选择合适的模型）
    'model_name': 'deepseek',  # 或其他开源模型
    
    # 生成参数
    'temperature': 0.1,        # 降低temperature以获得更确定性的答案
    'max_tokens': 1000,        # 答案的最大token数
    
    # 对不同题型的温度设置
    'temperature_by_type': {
        'basic': 0.0,          # 基础题需要精确答案
        'intermediate': 0.1,   # 中级题需要一定推理
        'advanced': 0.2,       # 高级题需要更多创造性
    }
}

# ========== Embedding配置 ==========
EMBEDDING_CONFIG = {
    'model': 'BAAI/bge-large-zh-v1.5',  # 或其他开源embedding模型
    'batch_size': 32,                    # 批处理大小
}

# ========== 输出配置 ==========
OUTPUT_CONFIG = {
    'max_retrieval_results': 10,  # 最多返回的检索结果数量
    'include_metadata': True,      # 是否包含元数据
    'format_version': '1.0',
}

# ========== 优化策略配置 ==========
OPTIMIZATION_CONFIG = {
    # Token优化策略
    'enable_token_optimization': True,  # 启用token优化
    'remove_redundant_content': True,   # 移除重复内容
    'compress_context': False,          # 是否压缩上下文（可能影响准确性）
    
    # 缓存策略
    'enable_cache': True,               # 启用结果缓存
    'cache_embeddings': True,           # 缓存embeddings
    
    # 重试策略
    'max_retries': 2,                   # 最大重试次数
    'retry_on_low_quality': True,       # 低质量答案时重试
}

# ========== 评测相关配置 ==========
EVALUATION_CONFIG = {
    # 用于平衡准确性和token消耗的权重
    'accuracy_weight': 0.7,    # 答案质量权重
    'efficiency_weight': 0.3,  # Token效率权重
    
    # 监控配置
    'track_token_usage': True, # 追踪token使用量
    'log_retrieval_results': True,  # 记录检索结果
}


# ========== 提示词模板 ==========
PROMPT_TEMPLATES = {
    'basic': """请基于以下文档内容，精确回答问题。

问题：{query}

文档内容：
{context}

要求：
1. 直接从文档中提取准确答案
2. 如果是数字、日期、名称等，必须完全准确
3. 不要添加任何文档中没有的信息
4. 如果找不到答案，明确说明

答案：""",

    'intermediate': """请综合分析以下文档片段，完整回答问题。

问题：{query}

文档内容：
{context}

要求：
1. 综合多个片段的信息
2. 如需排序或对比，仔细分析所有数据
3. 完整列出所有相关内容
4. 保持答案结构化和条理清晰

答案：""",

    'advanced': """请深入分析以下文档，进行跨文档推理和对比。

问题：{query}

文档内容：
{context}

要求：
1. 识别不同文档/版本间的关键差异
2. 进行逻辑推理和演变分析
3. 明确指出信息来源
4. 结构化呈现对比结果
5. 提供清晰的推理过程

答案："""
}


def get_config(config_type: str = 'all'):
    """
    获取配置
    """
    if config_type == 'chunk':
        return CHUNK_CONFIG
    elif config_type == 'retrieval':
        return RETRIEVAL_CONFIG
    elif config_type == 'llm':
        return LLM_CONFIG
    elif config_type == 'embedding':
        return EMBEDDING_CONFIG
    elif config_type == 'output':
        return OUTPUT_CONFIG
    elif config_type == 'optimization':
        return OPTIMIZATION_CONFIG
    elif config_type == 'evaluation':
        return EVALUATION_CONFIG
    elif config_type == 'prompts':
        return PROMPT_TEMPLATES
    else:
        return {
            'chunk': CHUNK_CONFIG,
            'retrieval': RETRIEVAL_CONFIG,
            'llm': LLM_CONFIG,
            'embedding': EMBEDDING_CONFIG,
            'output': OUTPUT_CONFIG,
            'optimization': OPTIMIZATION_CONFIG,
            'evaluation': EVALUATION_CONFIG,
            'prompts': PROMPT_TEMPLATES,
        }


if __name__ == "__main__":
    import json
    config = get_config('all')
    print(json.dumps(config, indent=2, ensure_ascii=False))

