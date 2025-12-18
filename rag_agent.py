from typing import List, Dict, Optional, Tuple
import re
import base64
import io
from PIL import Image

from openai import OpenAI

from config import (
    OPENAI_API_KEY,
    OPENAI_API_BASE,
    MODEL_NAME,
    TEXT_MODEL_NAME,
    MULTIMODAL_MODEL_NAME,
    TOP_K,
)
from vector_store import VectorStore
from hybrid_retriever import HybridRetriever
from token_tracker import TokenTracker
from reasoning_chain import ReasoningChain
from auto_cot_prompting import AutoCotPromptBuilder


class RAGAgent:
    """
    完全增强版RAG智能体（集成Casco所有核心功能）
    
    核心功能：
    1. 问题分析和分类（basic/intermediate/advanced）
    2. 查询增强（多查询生成）
    3. 多查询检索
    4. 结果重排序
    5. 分层检索策略
    6. 动态温度控制
    7. Token追踪和优化 ✅ 新增
    8. 推理链记录 ✅ 新增
    9. Auto-CoT推理 ✅ 新增
    10. 答案质量检查和重试 ✅ 新增
    """
    
    def __init__(
        self,
        model: str = MODEL_NAME,
        text_model: str = TEXT_MODEL_NAME,  # 新增：纯文本模型
        multimodal_model: str = MULTIMODAL_MODEL_NAME,  # 新增：多模态模型
        enable_tracking: bool = True,
        enable_cot: bool = True,
        use_multimodal: bool = True,  # 新增：是否使用多模态检索
    ):
        self.model = model  # 默认模型（向后兼容）
        self.text_model = text_model  # 纯文本模型
        self.multimodal_model = multimodal_model  # 多模态模型
        self.use_multimodal = use_multimodal

        self.client = OpenAI(api_key=OPENAI_API_KEY, base_url=OPENAI_API_BASE)

        # 初始化检索器
        self.vector_store = VectorStore()
        
        if use_multimodal:
            try:
                self.hybrid_retriever = HybridRetriever()
                print("✅ 多模态检索已启用（文本+图片）")
            except Exception as e:
                print(f"⚠️  多模态检索初始化失败: {e}")
                print("   回退到纯文本检索")
                self.use_multimodal = False
                self.hybrid_retriever = None
        else:
            self.hybrid_retriever = None

        # 不同难度的温度设置
        self.temp_map = {
            'basic': 0.3,         # 事实提取，要求精确
            'intermediate': 0.5,  # 综合分析，允许轻微推理
            'advanced': 0.7,      # 深度推理，允许更高探索性
        }
        
        # ========== 新增功能模块 ==========
        
        # Token追踪器
        self.token_tracker = TokenTracker() if enable_tracking else None
        
        # Auto-CoT构建器
        self.enable_cot = enable_cot
        if enable_cot:
            try:
                self.cot_builder = AutoCotPromptBuilder()
            except Exception as e:
                print(f"⚠️  CoT加载失败: {e}，将使用基础提示词")
                self.enable_cot = False
                self.cot_builder = None
        else:
            self.cot_builder = None
        
        # 当前推理链
        self.current_reasoning_chain: Optional[ReasoningChain] = None
        
        # 统计信息
        self.query_count = 0

        """
        系统提示词：定义助教的角色和回答策略
        """
        self.system_prompt = """你是一位专业、耐心的课程助教，你的任务是帮助学生理解课程内容。

【你的职责】
1. 根据提供的课程材料准确回答学生的问题
2. 如果课程材料中有相关内容，优先引用这些内容
3. 提供清晰、结构化的解答
4. 在回答中明确标注信息来源（文件名和页码）

【回答规范】
1. 准确性：确保回答基于课程材料，不编造信息
2. 完整性：提供充分的解释和必要的背景知识
3. 清晰性：使用易懂的语言，适当使用例子说明
4. 来源标注：在回答中注明"根据《文件名》第X页..."

【特殊情况处理】
- 如果课程材料中没有相关信息，诚实告知学生
- 如果问题不够清楚，可以请学生补充说明
- 如果涉及复杂概念，可以分步骤讲解

请始终保持专业、友好的态度，帮助学生更好地掌握课程知识。"""
    
    # ==================== Casco核心功能：问题分析 ====================
    
    def analyze_query_type(self, query: str) -> str:
        """
        分析问题类型（移植自Casco）
        
        分类：
        - basic: 简单事实提取
        - intermediate: 需要综合多个片段
        - advanced: 需要跨文档推理、对比分析
        
        参数:
            query: 用户问题
            
        返回:
            问题类型
        """
        # 高级题特征
        advanced_keywords = ['对比', '演变', '如何', '计算', '区别', 
                            '哪', '版本', '分别', '不同', 'baseline', '变化', '差异',
                            '为什么', '原因', '解释']
        
        # 中级题特征
        intermediate_keywords = ['排第几', '排名', '列出', '完整', '所有', '分别是',
                               '有哪些', '包括', '包含']
        
        query_lower = query.lower()
        
        # 检查高级特征
        for keyword in advanced_keywords:
            if keyword in query:
                print(f"  🎯 识别为【高级题】- 关键词: '{keyword}'")
                return 'advanced'
        
        # 检查中级特征
        for keyword in intermediate_keywords:
            if keyword in query:
                print(f"  🎯 识别为【中级题】- 关键词: '{keyword}'")
                return 'intermediate'
        
        print(f"  🎯 识别为【基础题】")
        return 'basic'
    
    # ==================== Casco核心功能：查询增强 ====================
    
    def enhance_query(self, query: str) -> List[str]:
        """
        查询增强：生成多个检索查询（移植自Casco）
        
        策略：
        1. 原始查询
        2. 提取的年份
        3. 提取的专业术语
        4. 提取的标准号
        
        参数:
            query: 原始查询
            
        返回:
            增强后的查询列表
        """
        queries = [query]
        
        # 提取年份
        years = re.findall(r'\b(19|20)\d{2}\b', query)
        queries.extend(years)
        
        # 提取专业术语（大写缩写，如NLP, BERT, CRF等）
        abbreviations = re.findall(r'\b[A-Z]{2,}[\w\-\.]*\b', query)
        queries.extend(abbreviations)
        
        # 提取标准号模式（如GB/T 12345-2023）
        standard_patterns = re.findall(r'[A-Z]{2,}[\/\s]*[A-Z]*\s*\d+[\.\-]\d+[\-\d]*', query)
        queries.extend(standard_patterns)
        
        # 去重并保持顺序
        seen = set()
        unique_queries = []
        for q in queries:
            if q not in seen:
                seen.add(q)
                unique_queries.append(q)
        
        if len(unique_queries) > 1:
            print(f"  🔍 查询增强: {len(unique_queries)} 个查询 - {unique_queries[:3]}...")
        
        return unique_queries
    
    def extract_technical_terms(self, query: str) -> List[str]:
        """
        提取专业术语（移植自Casco）
        
        参数:
            query: 查询文本
            
        返回:
            专业术语列表
        """
        terms = []
        
        # 提取大写缩写
        abbreviations = re.findall(r'\b[A-Z]{2,}[\w\-\.]*\b', query)
        terms.extend(abbreviations)
        
        # 提取标准号模式
        standard_patterns = re.findall(r'[A-Z]{2,}[\/\s]*[A-Z]*\s*\d+[\.\-]\d+[\-\d]*', query)
        terms.extend(standard_patterns)
        
        return terms
    
    # ==================== Casco核心功能：重排序 ====================
    
    def rerank_results(self, query: str, results: List[Dict]) -> List[Dict]:
        """
        重排序检索结果（支持多模态：文本+图片）
        
        基于关键词匹配度重新排序
        
        参数:
            query: 原始查询
            results: 检索结果（可能包含文本和图片）
            
        返回:
            重排序后的结果
        """
        if not results:
            return results
        
        # 提取查询关键词
        query_keywords = set(query.lower().split())
        
        # 计算每个结果的匹配度
        for result in results:
            # 获取文本内容（支持多模态）
            if result.get('type') == 'image':
                # 图片类型：使用 description 字段
                content = result.get('description', '') + ' ' + result.get('metadata', {}).get('context', '')
            else:
                # 文本类型：使用 content 字段
                content = result.get('content', '')
            
            content_lower = content.lower()
            
            # 计算关键词匹配数
            match_count = sum(1 for keyword in query_keywords if keyword in content_lower)
            
            # 计算匹配率
            match_ratio = match_count / len(query_keywords) if query_keywords else 0
            
            # 原始距离分数（越小越好）
            original_distance = result.get('distance', 1.0)
            
            # 综合分数：距离 * 0.6 - 匹配率 * 0.4
            # （分数越小越好，所以匹配率用减法）
            result['rerank_score'] = original_distance * 0.6 - match_ratio * 0.4
            result['match_ratio'] = match_ratio
        
        # 按综合分数排序
        results.sort(key=lambda x: x.get('rerank_score', 1.0))
        
        top3_ratios = ', '.join([f"{r.get('match_ratio', 0):.1%}" for r in results[:3]])
        print(f"  📊 重排序完成: Top3匹配率 [{top3_ratios}]")
        
        return results

    # ==================== Casco核心功能：分层检索策略 ====================
    
    def multi_query_retrieve(self, query: str, k: int) -> List[Dict]:
        """
        多查询检索（支持多模态）
        
        参数:
            query: 查询问题
            k: 每个查询的检索数量
            
        返回:
            检索结果列表（已去重）
        """
        # 1. 生成多个查询
        queries = self.enhance_query(query)
        print(f"  🔍 生成了 {len(queries)} 个检索查询")
        
        # 2. 对每个查询检索
        all_results = []
        seen_contents = set()
        
        for i, q in enumerate(queries, 1):
            print(f"     查询 {i}/{len(queries)}: {q[:50]}{'...' if len(q) > 50 else ''}")
            
            # 使用混合检索（如果启用）
            if self.use_multimodal and self.hybrid_retriever:
                search_results = self.hybrid_retriever.search(
                    query=q,
                    top_k=k,
                    include_images=True
                )
                results = search_results['combined']  # 获取合并后的结果
            else:
                results = self.vector_store.search(q, top_k=k)
            
            print(f"     → 找到 {len(results)} 个相关文档")
            
            # 去重（基于content或image_path）
            for result in results:
                if result.get('type') == 'image':
                    content_key = f"img_{result.get('image_path', '')}"
                else:
                    content_key = result.get('content', '')[:100]
                    
                if content_key not in seen_contents:
                    seen_contents.add(content_key)
                    all_results.append(result)
        
        print(f"  ✓ 合并去重后共 {len(all_results)} 个文档")
        return all_results[:k*2]  # 限制总数
    
    def basic_retrieve(self, query: str) -> Tuple[str, List[Dict]]:
        """
        基础检索策略（移植自Casco）
        
        特点：
        - 检索数量：3个
        - 适用于简单事实提取
        
        参数:
            query: 查询问题
            
        返回:
            (上下文字符串, 检索结果列表)
        """
        print(f"  📚 使用【基础检索】策略 (k=3)")
        
        # 多查询检索
        results = self.multi_query_retrieve(query, k=3)
        
        # 重排序
        print(f"  🔄 正在重排序 {len(results)} 个结果...")
        results = self.rerank_results(query, results)
        
        # 格式化
        print(f"  📝 格式化上下文...")
        context = self._format_context(results[:3])
        
        return context, results[:3]
    
    def intermediate_retrieve(self, query: str) -> Tuple[str, List[Dict]]:
        """
        中级检索策略（移植自Casco）
        
        特点：
        - 检索数量：6个
        - 需要综合多个文档片段
        
        参数:
            query: 查询问题
            
        返回:
            (上下文字符串, 检索结果列表)
        """
        print(f"  📚 使用【中级检索】策略 (k=6)")
        
        # 多查询检索
        results = self.multi_query_retrieve(query, k=6)
        
        # 重排序
        print(f"  🔄 正在重排序 {len(results)} 个结果...")
        results = self.rerank_results(query, results)
        
        # 格式化
        print(f"  📝 格式化上下文...")
        context = self._format_context(results[:6])
        
        return context, results[:6]
    
    def advanced_retrieve(self, query: str) -> Tuple[str, List[Dict]]:
        """
        高级检索策略（移植自Casco）
        
        特点：
        - 检索数量：8个
        - 支持跨文档分析和对比
        
        参数:
            query: 查询问题
            
        返回:
            (上下文字符串, 检索结果列表)
        """
        print(f"  📚 使用【高级检索】策略 (k=8)")
        
        # 多查询检索（更多数量）
        results = self.multi_query_retrieve(query, k=8)
        
        # 重排序
        print(f"  🔄 正在重排序 {len(results)} 个结果...")
        results = self.rerank_results(query, results)
        
        # 构建结构化上下文
        print(f"  📝 构建结构化上下文...")
        context = self._build_structured_context(results[:8], query)
        
        return context, results[:8]
    
    def _format_context(self, results: List[Dict]) -> str:
        """
        格式化上下文（支持多模态：文本+图片）
        
        参数:
            results: 检索结果列表（可能包含文本和图片）
            
        返回:
            格式化的上下文字符串
        """
        if not results:
            return ""
        
        context_parts = []
        context_parts.append("【相关课程材料】\n")
        
        for idx, doc in enumerate(results, 1):
            # 获取文件信息（兼容多模态）
            if doc.get('type') == 'image':
                # 图片类型
                filename = doc.get('filename', 'unknown')
                page_num = doc.get('page_number', 0)
                content = f"[图片]\n路径: {doc.get('image_path', 'N/A')}\n描述: {doc.get('description', 'N/A')}"
            else:
                # 文本类型
                filename = doc.get('filename', 'unknown')
                page_num = doc.get('page_number', 0)
                content = doc.get('content', 'N/A')
            
            match_ratio = doc.get('match_ratio', 0)
            
            # 格式化每个文档片段
            context_parts.append(f"\n[材料 {idx}] (相关度: {match_ratio:.1%})")
            
            # 添加来源信息
            if page_num > 0:
                context_parts.append(f"来源：《{filename}》第 {page_num} 页")
            else:
                context_parts.append(f"来源：《{filename}》")
            
            # 添加内容
            context_parts.append(f"内容：\n{content}\n")
            context_parts.append("-" * 50)
        
        return "\n".join(context_parts)
    
    def _build_structured_context(self, results: List[Dict], query: str) -> str:
        """
        构建结构化上下文（支持多模态：文本+图片）
        
        参数:
            results: 检索结果（可能包含文本和图片）
            query: 原始查询
            
        返回:
            结构化的上下文字符串
        """
        if not results:
            return ""
        
        context_parts = []
        context_parts.append("=== 检索到的相关文档 ===\n")
        
        for idx, doc in enumerate(results, 1):
            # 获取文件信息（兼容多模态）
            if doc.get('type') == 'image':
                # 图片类型
                filename = doc.get('filename', 'unknown')
                page_num = doc.get('page_number', 0)
                content = f"[图片]\n路径: {doc.get('image_path', 'N/A')}\n描述: {doc.get('description', 'N/A')}"
                icon = "🖼️"
            else:
                # 文本类型
                filename = doc.get('filename', 'unknown')
                page_num = doc.get('page_number', 0)
                content = doc.get('content', 'N/A')
                icon = "📄"
            
            match_ratio = doc.get('match_ratio', 0)
            
            # 结构化格式
            context_parts.append(f"\n【文档片段 {idx}】(相关度: {match_ratio:.1%})")
            
            if page_num > 0:
                context_parts.append(f"{icon} 来源：《{filename}》第 {page_num} 页")
            else:
                context_parts.append(f"{icon} 来源：《{filename}》")
            
            context_parts.append(f"\n{content}\n")
            context_parts.append("")
        
        return "\n".join(context_parts)

    def retrieve_context(
        self, query: str, top_k: int = TOP_K
    ) -> Tuple[str, List[Dict]]:
        """
        智能检索上下文（集成推理链记录）
        
        根据问题类型自动选择检索策略：
        - basic: 3个文档，简单检索
        - intermediate: 6个文档，综合分析
        - advanced: 8个文档，深度分析
        
        参数:
            query: 用户问题
            top_k: 检索数量（如果指定，会覆盖自动策略）
            
        返回:
            (上下文字符串, 检索结果列表)
        """
        print(f"\n{'='*60}")
        print(f"🔎 开始检索")
        print(f"{'='*60}")
        
        # 【新增】记录推理步骤
        if self.current_reasoning_chain:
            self.current_reasoning_chain.add_analysis_step(
                "开始分析问题",
                f"问题: {query}"
            )
        
        # 1. 分析问题类型
        query_type = self.analyze_query_type(query)
        
        # 【新增】记录分析结果
        if self.current_reasoning_chain:
            technical_terms = self.extract_technical_terms(query)
            self.current_reasoning_chain.add_analysis_step(
                f"识别为{query_type}类型问题",
                f"关键特征: {', '.join(technical_terms) if technical_terms else '无明显专业术语'}"
            )
        
        # 2. 根据类型选择检索策略
        if query_type == 'basic':
            context, results = self.basic_retrieve(query)
        elif query_type == 'intermediate':
            context, results = self.intermediate_retrieve(query)
        else:  # advanced
            context, results = self.advanced_retrieve(query)
        
        # 【新增】记录检索结果
        if self.current_reasoning_chain:
            langs = set(r.get('lang', 'unknown') for r in results if 'lang' in r)
            self.current_reasoning_chain.add_retrieval_step(
                f"检索到{len(results)}个相关文档",
                f"策略: {query_type}, 文档来源: {len(set(r['filename'] for r in results))}个文件"
            )
        
        # 【新增】追踪检索上下文Token
        if self.token_tracker:
            self.token_tracker.track_retrieval(context)
        
        print(f"\n  ✅ 检索完成: 返回 {len(results)} 个文档片段")
        print(f"{'='*60}\n")
        
        return context, results

    def generate_response(
        self,
        query: str,
        context: str,
        chat_history: Optional[List[Dict]] = None,
        query_type: str = 'basic',
        image: Optional[str] = None,  # 新增：图片路径或base64
        file_content: Optional[str] = None,  # 新增：文件内容
        use_multimodal_model: bool = False,  # 新增：是否使用多模态模型
        enable_socratic: bool = False,  # 新增：苏格拉底模式
    ) -> str:
        """
        生成回答（集成Auto-CoT和Token追踪）
        
        参数:
            query: 用户问题
            context: 检索到的上下文
            chat_history: 对话历史
            query_type: 问题类型（用于选择温度和CoT）
            image: 图片路径或base64（可选）
            file_content: 文件内容（可选）
            use_multimodal_model: 是否使用多模态模型
        """
        # 【暂时注释】Token优化上下文 - 先确保基本功能正确
        # if self.token_tracker:
        #     original_len = len(context)
        #     context = self.token_tracker.optimize_context(context, max_tokens=8000)
        #     if len(context) < original_len and self.current_reasoning_chain:
        #         self.current_reasoning_chain.add_step(
        #             "优化",
        #             f"上下文过长，优化至{self.token_tracker.count_tokens(context)} tokens",
        #             f"原始: {original_len}字符 -> 优化后: {len(context)}字符"
        #         )
        
        messages = [{"role": "system", "content": self.system_prompt}]

        if chat_history:
            messages.extend(chat_history)

        # 【新增】根据问题类型和模式选择prompt
        if enable_socratic:
            # 苏格拉底模式：通过反问引导思考
            user_text = f"""你是一位苏格拉底式的导师，通过提问引导学生思考，而不是直接给出答案。

【背景知识】
{context}

【学生问题】
{query}

请按照苏格拉底式教学法回应：
1. 不要直接给出答案
2. 通过2-3个递进的引导性问题帮助学生自己思考
3. 问题应该从简单到复杂，引导学生逐步发现答案
4. 语气要鼓励和启发
5. 可以给出一些提示或线索，但不要直接透露答案

现在开始引导学生思考："""
            
            if self.current_reasoning_chain:
                self.current_reasoning_chain.add_step(
                    "苏格拉底模式",
                    "启用引导式提问",
                    "通过反问帮助学生思考"
                )
            print(f"  🤔 启用苏格拉底模式")
            
        elif self.enable_cot and self.cot_builder and query_type in ['intermediate', 'advanced']:
            # 使用Auto-CoT构建提示词
            user_text = self.cot_builder.build_prompt(query, context, max_examples=2)
            
            if self.current_reasoning_chain:
                self.current_reasoning_chain.add_step(
                    "CoT",
                    f"启用Auto-CoT推理（{query_type}题）",
                    f"注入了 {len(self.cot_builder.examples)} 个推理示例"
                )
            
            print(f"  💡 启用Auto-CoT推理")
        else:
            # 使用标准提示词
            user_text = f"""{context}

【学生问题】
{query}

请根据上述课程材料回答学生的问题。如果材料中有相关内容，请优先使用并标注来源；如果材料不足以完整回答，请诚实说明。"""

        # 【新增】构建多模态消息（如果有图片或文件）
        if image or file_content:
            # 多模态消息格式
            user_content = []
            
            # 添加文本内容
            user_content.append({
                "type": "text",
                "text": user_text
            })
            
            # 添加图片
            if image:
                # 支持本地路径和base64
                if image.startswith('data:image'):
                    # base64格式
                    user_content.append({
                        "type": "image_url",
                        "image_url": {"url": image}
                    })
                else:
                    # 本地文件路径
                    try:
                        img = Image.open(image)
                        buffered = io.BytesIO()
                        img.save(buffered, format="PNG")
                        img_base64 = base64.b64encode(buffered.getvalue()).decode()
                        user_content.append({
                            "type": "image_url",
                            "image_url": {"url": f"data:image/png;base64,{img_base64}"}
                        })
                    except Exception as e:
                        print(f"  ⚠️ 图片加载失败: {e}")
            
            # 添加文件内容（如果有）
            if file_content:
                user_content[0]["text"] += f"\n\n【文件内容】\n{file_content}"
            
            messages.append({"role": "user", "content": user_content})
        else:
            # 纯文本消息
            messages.append({"role": "user", "content": user_text})
        
        # 根据问题类型选择温度
        temperature = self.temp_map.get(query_type, 0.5)
        
        print(f"  🤖 生成回答 (temperature={temperature})")
        
        # 【新增】记录推理步骤
        if self.current_reasoning_chain:
            self.current_reasoning_chain.add_step(
                "生成",
                f"使用{query_type}题型的提示词生成答案",
                f"温度: {temperature}, CoT: {'是' if self.enable_cot and query_type in ['intermediate', 'advanced'] else '否'}"
            )

        try:
            # 【新增】根据输入类型选择模型
            if use_multimodal_model or image or file_content:
                selected_model = self.multimodal_model
                model_type = "多模态模型"
            else:
                selected_model = self.text_model
                model_type = "文本模型"
            
            # 显示上下文信息
            if self.token_tracker:
                context_tokens = self.token_tracker.count_tokens(user_text)
                print(f"  📝 上下文长度: {len(context)} 字符, {context_tokens} tokens")
            
            print(f"  🌐 正在调用LLM API ({selected_model} - {model_type})...")
            if image:
                print(f"     🖼️ 包含图片输入")
            if file_content:
                print(f"     📄 包含文件内容 ({len(file_content)} 字符)")
            print(f"     这可能需要几秒到几十秒，请耐心等待...")
            
            response = self.client.chat.completions.create(
                model=selected_model, 
                messages=messages, 
                temperature=temperature,
                max_tokens=1500
            )
            
            print(f"  ✅ 收到LLM响应")

            answer = response.choices[0].message.content
            
            # 【新增】追踪Token使用
            if self.token_tracker:
                token_usage = self.token_tracker.track_llm(user_text, answer)
                if self.current_reasoning_chain:
                    self.current_reasoning_chain.add_step(
                        "统计",
                        f"Token消耗: 输入{token_usage['input']}, 输出{token_usage['output']}",
                        f"总计: {token_usage['total']} tokens"
                    )
            
            return answer
            
        except Exception as e:
            return f"生成回答时出错: {str(e)}"

    # ==================== 答案质量检查（从Casco移植） ====================
    
    def check_answer_quality(self, answer: str, query: str) -> bool:
        """
        检查答案质量（从Casco完全移植）
        
        参数:
            answer: 生成的答案
            query: 原始问题
            
        返回:
            质量是否合格
        """
        # 检查长度
        if not answer or len(answer.strip()) < 10:
            return False
        
        # 检查否定词
        negative_phrases = ['不知道', '未找到', '无法回答', '没有找到', '数据库中没有', '出错']
        if any(phrase in answer for phrase in negative_phrases):
            return False
        
        return True

    def answer_question(
        self, query: str, chat_history: Optional[List[Dict]] = None, 
        top_k: int = TOP_K, max_retries: int = 2,
        image: Optional[str] = None,  # 图片路径或base64
        file_content: Optional[str] = None,  # 文件内容
        enable_socratic: bool = False,  # 苏格拉底模式
    ) -> Dict[str, any]:
        """
        回答问题（完整流程，按照新的多模态处理逻辑）
        
        处理逻辑：
        1. 纯文本输入：文字+图片库检索 → 文本模型
        2. 有图片输入：描述图片 → 用增强query检索 → 原图+context → 多模态模型
        3. 有文件输入：用原始query检索 → 文件内容+context → 多模态模型
        
        参数:
            query: 用户问题
            chat_history: 对话历史
            top_k: 检索文档数量
            max_retries: 最大重试次数
            image: 图片路径或base64（可选）
            file_content: 文件内容（可选）
            
        返回:
            生成的回答
        """
        self.query_count += 1
        
        # 创建推理链
        self.current_reasoning_chain = ReasoningChain(query)
        
        # ========== 根据输入类型确定处理策略 ==========
        
        if image:
            # ===== 情况2: 有图片输入 =====
            print("\n📷 检测到图片输入，使用多模态处理流程")
            
            # 2.1 描述图片
            from multimodal_input_handler import MultimodalInputHandler
            handler = MultimodalInputHandler()
            
            # 如果是base64，先转换为PIL Image
            if image.startswith('data:image'):
                import base64
                import io
                image_data = image.split('base64,')[1]
                image_bytes = base64.b64decode(image_data)
                from PIL import Image as PILImage
                pil_image = PILImage.open(io.BytesIO(image_bytes))
                result = handler.handle_image_input(pil_image, query)
            else:
                # 本地路径
                from PIL import Image as PILImage
                pil_image = PILImage.open(image)
                result = handler.handle_image_input(pil_image, query)
            
            enhanced_query = result['enhanced_query']
            image_path = result['image_path']
            
            # 2.2 用增强的query检索（包含图片描述）
            query_type = self.analyze_query_type(enhanced_query)
            context, retrieved_docs = self.retrieve_context(enhanced_query, top_k=top_k)
            
            # 2.3 生成回答：原图 + context → 多模态模型
            answer = self.generate_response(
                query, context, chat_history, query_type,
                image=image_path,  # 传原图
                file_content=None,
                use_multimodal_model=True,  # 强制使用多模态模型
                enable_socratic=enable_socratic
            )
            
        elif file_content:
            # ===== 情况3: 有文件输入 =====
            print("\n📄 检测到文件输入，使用多模态处理流程")
            
            # 3.1 用原始query检索
            query_type = self.analyze_query_type(query)
            context, retrieved_docs = self.retrieve_context(query, top_k=top_k)
            
            # 3.2 生成回答：文件内容 + context → 多模态模型
            answer = self.generate_response(
                query, context, chat_history, query_type,
                image=None,
                file_content=file_content,  # 传文件内容
                use_multimodal_model=True,  # 强制使用多模态模型
                enable_socratic=enable_socratic
            )
            
        else:
            # ===== 情况1: 纯文本输入 =====
            print("\n📝 纯文本输入，使用文本模型")
            
            # 1.1 分析问题类型
            query_type = self.analyze_query_type(query)
            
            # 1.2 在文字和图片库都检索
            context, retrieved_docs = self.retrieve_context(query, top_k=top_k)
            
            # 1.3 生成回答：使用纯文本模型
            answer = self.generate_response(
                query, context, chat_history, query_type,
                image=None,
                file_content=None,
                use_multimodal_model=False,  # 强制使用文本模型
                enable_socratic=enable_socratic
            )
        
        if not context:
            context = "（未检索到特别相关的课程材料）"
        
        # 设置最终答案和结论
        if self.current_reasoning_chain:
            self.current_reasoning_chain.set_final_answer(answer)
            self.current_reasoning_chain.add_conclusion_step(
                f"查询完成，共{len(self.current_reasoning_chain.steps)}个推理步骤"
            )
        
        # 记录查询日志
        if self.token_tracker:
            self.token_tracker.log_query(
                query, answer, query_type, len(retrieved_docs),
                self.token_tracker.usage
            )
        
        # 保存检索结果供外部访问（用于API citations）
        self.last_context_docs = retrieved_docs
        self.last_retrieval_results = retrieved_docs

        return answer

    # ==================== 便捷方法 ====================
    
    def get_reasoning_chain(self) -> Optional[ReasoningChain]:
        """获取当前推理链"""
        return self.current_reasoning_chain
    
    def get_token_report(self) -> str:
        """获取Token使用报告"""
        if self.token_tracker:
            return self.token_tracker.get_report()
        return "Token追踪未启用"
    
    def save_token_report(self, output_path: str = "token_report.json"):
        """保存Token使用报告"""
        if self.token_tracker:
            self.token_tracker.save_report(output_path)
        else:
            print("Token追踪未启用")
    
    def get_performance_summary(self) -> Dict:
        """获取性能摘要"""
        summary = {
            'query_count': self.query_count,
        }
        
        if self.token_tracker:
            summary['token_usage'] = self.token_tracker.get_summary()
        
        if self.current_reasoning_chain:
            summary['last_reasoning'] = {
                'steps': len(self.current_reasoning_chain.steps),
                'confidence': self.current_reasoning_chain.get_average_confidence(),
                'duration': self.current_reasoning_chain.get_duration()
            }
        
        return summary

    def chat(self) -> None:
        """交互式对话（增强版）"""
        print("=" * 60)
        print("欢迎使用智能课程助教系统！（Casco增强版）")
        print("=" * 60)
        print("\n✨ 功能亮点：")
        print("  • 智能问题分类")
        print("  • 多查询增强检索")
        print("  • 答案质量检查和重试")
        if self.enable_cot:
            print("  • Auto-CoT推理")
        if self.token_tracker:
            print("  • Token追踪和优化")
        print("\n输入 '/reasoning' 查看推理过程")
        print("输入 '/tokens' 查看Token统计")
        print("输入 'quit' 退出\n")

        chat_history = []

        while True:
            try:
                query = input("\n学生: ").strip()

                if not query:
                    continue
                
                # 特殊命令
                if query.lower() == 'quit':
                    if self.token_tracker:
                        print("\n" + self.get_token_report())
                    print("\n再见！")
                    break
                
                if query == '/reasoning':
                    if self.current_reasoning_chain:
                        print("\n" + self.current_reasoning_chain.format_chain(detailed=True))
                    else:
                        print("\n暂无推理记录")
                    continue
                
                if query == '/tokens':
                    print("\n" + self.get_token_report())
                    continue

                answer = self.answer_question(query, chat_history=chat_history)

                print(f"\n助教: {answer}")

                chat_history.append({"role": "user", "content": query})
                chat_history.append({"role": "assistant", "content": answer})

            except KeyboardInterrupt:
                if self.token_tracker:
                    print("\n\n" + self.get_token_report())
                print("\n\n再见！")
                break
            except Exception as e:
                print(f"\n错误: {str(e)}")
