from typing import List, Dict, Optional, Tuple
import re
import base64
import io
import os
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
from src.core.vector_store import VectorStore
from src.core.hybrid_retriever import HybridRetriever
from src.core.reranker import Reranker  # 使用API Reranker
from src.utils.token_tracker import TokenTracker
from src.features.reasoning_chain import ReasoningChain
from src.features.auto_cot_prompting import AutoCotPromptBuilder


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
        
        # 初始化 API Reranker (使用bge-reranker-v2-m3)
        try:
            self.reranker = Reranker()
            print("✅ API Reranker 已初始化")
        except Exception as e:
            print(f"⚠️  Reranker 初始化失败: {e}")
            self.reranker = None

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
        self.system_prompt = r"""你是一位专业、耐心的课程助教，你的任务是帮助学生理解课程内容。

【你的职责】
1. 根据提供的课程材料准确回答学生的问题
2. 如果课程材料中有相关内容，优先引用这些内容
3. 提供清晰、结构化的解答
4. 在回答中明确标注信息来源（文件名和页码）

【回答规范】
1. 准确性：确保回答基于课程材料，不编造信息
2. 完整性：提供充分的解释和必要的背景知识
3. 清晰性：使用易懂的语言，适当使用例子说明
4. 来源标注：在回答末尾单独一行注明来源
   - 格式：在答案结束后，**空一行**，然后写"根据"，后面紧跟引用标签（不换行）
   - 正确示例：
     ```
     PaLM的模型规模为540B。
     
     根据<cite id="文件_p13">、<cite id="文件_p15">和<cite id="文件_p16">。
     ```
   - ⚠️ **错误示例**（禁止这样）：
     ```
     根据
     
     <cite id="文件_p13">
     
     <cite id="文件_p15">
     ```
   - 要点：多个引用在同一行，用顿号（、）和"和"连接

【数学公式格式】⚠️ 极其重要，必须严格遵守
- **必须且只能使用以下格式：**
  - **行内公式**：`$公式内容$`（美元符号包裹）
    - ✅ 示例：`$P(w|h)$`、`$\mathbf{W}^{(\ell)}$`、`$\gamma_t(i)$`
  - **独立公式（换行居中）**：`$$公式内容$$`（双美元符号包裹，前后各空一行）
    - ✅ 示例：
      ```
      
      $$
      \hat{a}_{ij} = \frac{\sum_{t=1}^{N-1} \xi_t(i, j)}{\sum_{t=1}^{N-1} \gamma_t(i)}
      $$
      
      ```

- **严格禁止使用以下格式**（这些格式无法渲染）：
  - ❌ `\( ... \)` 或 `\\( ... \\)` - 禁止使用
  - ❌ `\[ ... \]` 或 `\\[ ... \\]` - 禁止使用
  - ❌ `( ... )` 包裹公式 - 禁止使用
  - ❌ `[ ... ]` 包裹公式 - 禁止使用

- **完整示例：**
  当你需要说"状态转移概率"时，这样写：
  ```
  状态转移概率：$\hat{a}_{ij} = P(h_{t+1} = j | h_t = i)$
  
  计算公式：
  
  $$
  \hat{a}_{ij} = \frac{\sum_{t=1}^{N-1} \xi_t(i, j)}{\sum_{t=1}^{N-1} \gamma_t(i)}
  $$
  
  其中，$\xi_t(i, j)$ 是联合后验概率。
  ```

【特殊情况处理】
- 如果课程材料中没有相关信息，诚实告知学生
- 如果问题不够清楚，可以请学生补充说明
- 如果涉及复杂概念，可以分步骤讲解

请始终保持专业、友好的态度，帮助学生更好地掌握课程知识。"""
    
    def _fix_latex_format(self, text: str) -> str:
        """
        强力修复LaTeX格式，统一转换为 $ $ 和 $$ $$ 格式
        
        ⚠️ 策略：
        1. 先处理已有反斜杠的格式（\(...\)、\[...\]）
        2. 再一次性扫描，优先处理方括号，然后处理圆括号
        3. 最后修复孤立的LaTeX命令（如单独的 \operatorname）
        """
        import re
        
        # 第1步：修复奇怪的空格（\ ) 这种）
        text = text.replace('\\ )', '\\)')
        text = text.replace('\\ ]', '\\]')
        text = text.replace('\\ (', '\\(')
        text = text.replace('\\ [', '\\[')
        
        # 第2步：将 \\( ... \\) 或 \( ... \) 转换为 $ ... $
        text = re.sub(r'\\\\?\(\s*([^()]+?)\s*\\\\?\)', r'$\1$', text)
        
        # 第3步：将 \\[ ... \\] 或 \[ ... \] 转换为 $$ ... $$
        text = re.sub(r'\\\\?\[\s*([^\[\]]+?)\s*\\\\?\]', r'\n$$\n\1\n$$\n', text)
        
        # 第4步：一次性扫描，优先处理方括号，再处理圆括号
        def find_matching(text, start_idx, open_char, close_char):
            """找到匹配的闭合符号"""
            depth = 1
            i = start_idx + 1
            while i < len(text) and depth > 0:
                if text[i] == open_char:
                    depth += 1
                elif text[i] == close_char:
                    depth -= 1
                i += 1
            return i - 1 if depth == 0 else -1
        
        result = []
        i = 0
        while i < len(text):
            # 检查是否是未转义的 [
            if text[i] == '[' and (i == 0 or text[i-1] not in ['\\', '\\\\']):
                end_idx = find_matching(text, i, '[', ']')
                if end_idx != -1:
                    content = text[i+1:end_idx].strip()
                    # 检查是否包含LaTeX命令
                    if re.search(r'\\[a-zA-Z]+|\\frac|\\sum|\\prod|\\int|\\mid', content):
                        result.append(f'\n$$\n{content}\n$$\n')
                        i = end_idx + 1
                        continue
            
            # 检查是否是未转义的 (
            elif text[i] == '(' and (i == 0 or text[i-1] not in ['\\', '\\\\']):
                end_idx = find_matching(text, i, '(', ')')
                if end_idx != -1:
                    content = text[i+1:end_idx].strip()
                    # 检查是否包含LaTeX命令
                    if re.search(r'\\[a-zA-Z]+|\\frac|\\sum|\\prod|\\int|\\hat|\\mathbf|\\xi|\\gamma|\\dots|\\mid', content):
                        result.append(f'${content}$')
                        i = end_idx + 1
                        continue
            
            result.append(text[i])
            i += 1
        
        text = ''.join(result)
        
        # 第5步：修复孤立的LaTeX命令行（如 \operatorname 开头的行）
        # 如果一行以LaTeX命令开头，且包含数学符号，将整行包裹为独立公式
        lines = text.split('\n')
        fixed_lines = []
        for line in lines:
            stripped = line.strip()
            # 检查是否以LaTeX命令开头，且不在 $ 或 $$ 中
            if (stripped and 
                re.match(r'^\\[a-zA-Z]+', stripped) and 
                not stripped.startswith('$$') and 
                not stripped.startswith('$') and
                '_' in stripped or '^' in stripped or '\\' in stripped):
                # 这是一个孤立的LaTeX命令行，包裹为独立公式
                fixed_lines.append(f'$$\n{stripped}\n$$')
            else:
                fixed_lines.append(line)
        text = '\n'.join(fixed_lines)
        
        # 第6步：清理多余的连续换行
        text = re.sub(r'\n{4,}', '\n\n', text)
        
        return text
    
    def _fix_citation_format(self, text: str) -> str:
        """
        修复引用格式，只移除cite标签之间的换行，保留"根据"前面的空行
        """
        import re
        
        # 只处理cite标签之间的换行，不处理"根据"前面的换行
        # 匹配：<cite ...> + 换行 + 根据/、
        text = re.sub(r'(<cite id="[^"]+">)\s*\n+\s*(根据|、)', r'\1\2', text)
        
        # 移除连续cite标签之间的所有换行
        # 匹配：</cite> 或 <cite> + 任意空白和换行 + <cite>
        text = re.sub(r'(<cite id="[^"]+">)\s*\n+\s*(<cite)', r'\1、\2', text)
        
        # 移除cite标签后面紧跟的"根据"前的换行（但保留正常段落的换行）
        # 不修改"根据"前面的换行，保持原有格式
        
        return text
    
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
    
    # ==================== 查询增强（LLM增强版） ====================
    
    def enhance_query(self, query: str) -> List[str]:
        """
        使用 LLM 进行查询扩展（替代旧的正则规则）
        
        策略：
        1. 使用LLM提取核心专业概念
        2. 如果涉及概念辨析，分别提出
        3. 保留部分正则提取作为兜底
        
        参数:
            query: 原始查询
            
        返回:
            增强后的查询列表
        """
        prompt = f"""作为一个搜索专家，请将用户的查询转换为 3 个更精准的搜索子问题。
策略：
1. 提取核心专业概念。
2. 如果涉及概念辨析，分别提出。
3. 仅返回逗号分隔的关键词列表，不要解释。

示例1:
用户查询: "Viterbi算法、前向算法和后向算法都有什么异同？"
转换结果: "Viterbi算法, 前向算法, 后向算法"

示例2:
用户查询: "下图是一个英语词频统计的示例图，如图所示，出现长尾现象，即许多单词的词频很低，部分单词词频很高。基于此思考如果直接用英文单词分词，会带来什么影响？"
转换结果: "英语词频统计, 长尾现象, 英文分词影响"

用户查询: "{query}"
"""
        try:
            print(f"  🤖 正在调用LLM进行查询扩展...")
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.5,
                timeout=10  # 添加10秒超时
            )
            content = response.choices[0].message.content
            print(f"  ✅ LLM返回: {content}")
            # 清洗结果
            keywords = [k.strip() for k in content.split(',') if k.strip()]
            queries = [query] + keywords  # 原始查询 + 扩展词
            
            # 保留部分正则提取作为兜底
            years = re.findall(r'\b(19|20)\d{2}\b', query)
            abbrs = re.findall(r'\b[A-Z]{2,}[\w\-\.]*\b', query)
            queries.extend(years + abbrs)
            
            # 去重
            unique = list(dict.fromkeys(queries))
            print(f"  🔍 查询增强: {unique[:4]}")
            return unique[:4]
        except Exception as e:
            print(f"  ⚠️  查询增强失败: {e}，使用原始查询")
            return [query]
    
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
    
    # ==================== RRF融合 + SOTA检索架构 ====================
    
    def _rrf_fusion(self, vector_results: List[Dict], bm25_results: List[Dict], k: int = 60) -> List[Dict]:
        """Reciprocal Rank Fusion 倒数排名融合
        
        Args:
            vector_results: 向量检索结果
            bm25_results: BM25检索结果
            k: RRF参数（默认60）
            
        Returns:
            融合后的结果列表
        """
        fused_scores = {}
        doc_map = {}

        def get_doc_id(doc):
            # 尝试构建唯一ID，支持文本和图片文档
            filename = doc.get('filename', '_')
            page_num = doc.get('page_number', doc.get('page', '_'))
            
            # 文本文档使用content，图片文档使用description或image_path
            if 'content' in doc and doc['content']:
                content_snippet = doc['content'][:50]
            elif 'description' in doc:
                content_snippet = doc.get('description', '')[:50]
            elif 'image_path' in doc:
                content_snippet = doc.get('image_path', '')[:50]
            else:
                content_snippet = str(hash(str(doc)))[:10]  # 兜底方案
            
            return f"{filename}_{page_num}_{content_snippet}"

        # 处理向量结果
        for rank, doc in enumerate(vector_results):
            did = get_doc_id(doc)
            if did not in fused_scores:
                fused_scores[did] = 0
                doc_map[did] = doc
            fused_scores[did] += 1 / (rank + k)

        # 处理 BM25 结果
        for rank, doc in enumerate(bm25_results):
            did = get_doc_id(doc)
            if did not in fused_scores:
                fused_scores[did] = 0
                doc_map[did] = doc
            fused_scores[did] += 1 / (rank + k)

        # 排序
        sorted_ids = sorted(fused_scores.keys(), key=lambda x: fused_scores[x], reverse=True)
        return [doc_map[did] for did in sorted_ids]
    
    def retrieve_context_sota(self, query: str, top_k: int = TOP_K) -> Tuple[str, List[Dict]]:
        """
        SOTA 统一检索入口: Expand -> Parallel Search -> RRF -> FlashRank
        
        这是从yzy版本移植的统一检索架构，相比原有的分层检索更现代化。
        
        Args:
            query: 用户问题
            top_k: 检索数量
            
        Returns:
            (上下文字符串, 检索结果列表)
        """
        print(f"\n{'='*40}\n🔎 开始增强检索 (SOTA)\n{'='*40}")
        
        # 1. Expand
        queries = self.enhance_query(query)
        
        raw_vec, raw_bm25 = [], []
        
        # 2. Parallel Search
        for i, q in enumerate(queries):
            limit = top_k if i == 0 else 3  # 主查询查多点，副查询查少点
            # 向量检索
            if self.use_multimodal and self.hybrid_retriever:
                search_results = self.hybrid_retriever.search(
                    query=q,
                    top_k=limit,
                    include_images=True
                )
                raw_vec.extend(search_results['combined'])
            else:
                raw_vec.extend(self.vector_store.search(q, top_k=limit))
            
            # BM25 检索
            if hasattr(self.vector_store, 'search_bm25'):
                raw_bm25.extend(self.vector_store.search_bm25(q, top_k=limit))
            
        print(f"  📥 粗排召回: Vector={len(raw_vec)}, BM25={len(raw_bm25)}")

        # 3. Fusion
        fused = self._rrf_fusion(raw_vec, raw_bm25)
        print(f"  🔗 RRF融合: {len(fused)} 条文档")
        
        # 4. Rerank (API Reranker)
        candidates = fused[:30]  # 截取前30个给精排模型
        final_results = candidates
        
        if self.reranker and candidates:
            print(f"  ⚡ API Rerank 精排中...")
            # 使用API Reranker进行重排序
            final_results = self.reranker.rerank(
                query=query,
                documents=candidates,
                top_k=top_k
            )
            
            # 如果rerank失败，使用原始候选结果
            if not final_results:
                final_results = candidates

        final_top_k = final_results[:top_k]
        
        # 格式化并缓存
        context_str = self._format_context(final_top_k)
        self.last_context_docs = final_top_k
        self.last_retrieval_results = final_top_k 
        
        print(f"  ✅ 最终选取 {len(final_top_k)} 个高质量片段")
        return context_str, final_top_k
    
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
        - 初始检索：15个文档
        - Rerank后返回：5个最相关文档
        - 适用于简单事实提取
        
        参数:
            query: 查询问题
            
        返回:
            (上下文字符串, 检索结果列表)
        """
        print(f"  📚 使用【基础检索】策略 (初始检索15个 → Rerank → 返回5个)")
        
        # 多查询检索（每个查询检索5个，通常生成3个查询 = 15个候选）
        results = self.multi_query_retrieve(query, k=5)
        
        # 重排序
        print(f"  🔄 正在重排序 {len(results)} 个结果...")
        results = self.rerank_results(query, results)
        
        # 格式化（取前5个）
        print(f"  📝 格式化上下文...")
        context = self._format_context(results[:5])
        
        return context, results[:5]
    
    def intermediate_retrieve(self, query: str) -> Tuple[str, List[Dict]]:
        """
        中级检索策略（移植自Casco）
        
        特点：
        - 初始检索：24个文档
        - Rerank后返回：8个最相关文档
        - 需要综合多个文档片段
        
        参数:
            query: 查询问题
            
        返回:
            (上下文字符串, 检索结果列表)
        """
        print(f"  📚 使用【中级检索】策略 (初始检索24个 → Rerank → 返回8个)")
        
        # 多查询检索（每个查询检索8个，通常生成3个查询 = 24个候选）
        results = self.multi_query_retrieve(query, k=8)
        
        # 重排序
        print(f"  🔄 正在重排序 {len(results)} 个结果...")
        results = self.rerank_results(query, results)
        
        # 格式化（取前8个）
        print(f"  📝 格式化上下文...")
        context = self._format_context(results[:8])
        
        return context, results[:8]
    
    def advanced_retrieve(self, query: str) -> Tuple[str, List[Dict]]:
        """
        高级检索策略（移植自Casco）
        
        特点：
        - 初始检索：30个文档
        - Rerank后返回：10个最相关文档
        - 支持跨文档分析和对比
        
        参数:
            query: 查询问题
            
        返回:
            (上下文字符串, 检索结果列表)
        """
        print(f"  📚 使用【高级检索】策略 (初始检索30个 → Rerank → 返回10个)")
        
        # 多查询检索（更多数量，每个查询检索10个 = 30个候选）
        results = self.multi_query_retrieve(query, k=10)
        
        # 重排序
        print(f"  🔄 正在重排序 {len(results)} 个结果...")
        results = self.rerank_results(query, results)
        
        # 构建结构化上下文（取前10个）
        print(f"  📝 构建结构化上下文...")
        context = self._build_structured_context(results[:10], query)
        
        return context, results[:10]
    
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
            score = doc.get('score', doc.get('rerank_score', 0))
            
            # 生成唯一引用ID（格式：filename_page）
            cite_id = f"{filename}_p{page_num}".replace(' ', '_').replace('.pdf', '').replace('.docx', '')
            
            # 优化格式：去掉"材料1"标记，使用cite_id
            context_parts.append(f"\n【来源：《{filename}》第{page_num}页】[ID:{cite_id}]")
            if score > 0:
                context_parts.append(f"(相关度: {score:.2f})")
            
            # 添加内容
            context_parts.append(f"\n{content}\n")
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

    def _print_retrieved_context(self, retrieved_docs: List[Dict]):
        """
        在检索完成后立即打印context详情
        
        参数:
            retrieved_docs: 检索到的文档列表
        """
        if not retrieved_docs:
            print(f"\n{'='*80}")
            print(f"⚠️  未检索到相关文档")
            print(f"{'='*80}\n")
            return
        
        print(f"\n{'='*80}")
        print(f"📚 检索到的Context详情: ({len(retrieved_docs)} 个文档)")
        print(f"{'='*80}\n")
        
        for i, doc in enumerate(retrieved_docs, 1):
            filename = doc.get("filename", "未知文件")
            page_num = doc.get("page_num", doc.get("page_number", "未知"))
            section = doc.get("section", "")
            content_snippet = doc.get("content", "")[:200].replace('\n', ' ')
            score = doc.get("distance", doc.get("rerank_score", "N/A"))
            
            print(f"  [{i}] 文件: {filename}")
            print(f"      页码: 第 {page_num} 页" + (f" ({section})" if section else ""))
            print(f"      相似度: {score}")
            print(f"      内容: {content_snippet}...")
            print(f"      {'-'*76}\n")
        
        print(f"{'='*80}\n")
    
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

    def _check_image_in_context(self, retrieved_docs: List[Dict]) -> bool:
        """
        检查检索到的context中是否包含图片
        
        Args:
            retrieved_docs: 检索到的文档列表
            
        Returns:
            True if有图片，False otherwise
        """
        if not retrieved_docs:
            return False
        
        for doc in retrieved_docs:
            # 检查是否是图片类型的文档
            if doc.get('type') == 'image':
                return True
            
            # 检查文本内容中是否有【图片描述】标记
            content = doc.get('content', '')
            if '【图片描述】' in content:
                return True
            
            # 检查是否有image_path字段
            if 'image_path' in doc:
                return True
        
        return False
    
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
        thinking_mode: str = 'fast',  # 新增：思考模式
        temperature: float = 0.7,  # LLM温度参数
        max_tokens: int = 2000,  # LLM最大token数
    ) -> str:
        """
        生成回答（集成Auto-CoT和Token追踪）
        
        参数:
            query: 用户问题
            context: 检索到的上下文
            chat_history: 对话历史
            query_type: 问题类型（用于选择温度）
            image: 图片路径或base64（可选）
            file_content: 文件内容（可选）
            use_multimodal_model: 是否使用多模态模型
            enable_socratic: 苏格拉底模式
            thinking_mode: 'fast' 或 'thinking'（thinking时使用CoT）
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
            # 【重要】验证并修复chat_history格式
            print(f"  🔍 Chat history格式验证:")
            validated_history = []
            for i, msg in enumerate(chat_history):
                role = msg.get('role', '')
                content = msg.get('content', '')
                
                # 检查role是否有效
                valid_roles = ['user', 'assistant', 'system', 'tool']
                if role not in valid_roles:
                    print(f"     ⚠️ 消息{i+1}格式错误: role='{role[:20]}...' (应为{valid_roles}之一)")
                    print(f"        尝试修复...")
                    # 尝试修复：如果role看起来像是内容，content像是role
                    if role and content in valid_roles:
                        # 参数颠倒了，交换它们
                        role, content = content, role
                        print(f"        ✅ 已修复：交换role和content")
                    else:
                        # 无法修复，跳过这条消息
                        print(f"        ❌ 无法修复，跳过此消息")
                        continue
                
                # 添加验证通过的消息
                validated_history.append({
                    "role": role,
                    "content": content,
                    "timestamp": msg.get("timestamp", "")
                })
            
            if len(validated_history) < len(chat_history):
                print(f"     ℹ️ 已过滤 {len(chat_history) - len(validated_history)} 条无效消息")
            
            messages.extend(validated_history)

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
            
        elif thinking_mode == 'thinking' and self.enable_cot and self.cot_builder:
            # 使用Auto-CoT构建提示词
            user_text = self.cot_builder.build_prompt(query, context, max_examples=2)
            
            if self.current_reasoning_chain:
                self.current_reasoning_chain.add_step(
                    "CoT",
                    f"启用Auto-CoT深度推理",
                    f"注入了 {len(self.cot_builder.examples)} 个推理示例"
                )
            
            print(f"  🧠 启用Thinking模式 (Auto-CoT推理)")
        else:
            # 使用标准提示词（优化引用格式）
            user_text = f"""{context}

【学生问题】
{query}

请根据上述课程材料回答学生的问题。回答时请遵循以下要求：

1. **引用格式**：当引用材料时，请使用格式：`<cite id="文件名_p页码">引用内容</cite>`
   - 例如：根据<cite id="操作系统_p23">虚拟内存是一种内存管理技术</cite>...
   - cite id必须与材料中的[ID:xxx]完全一致

2. **不要使用"材料1"、"材料2"**：直接引用内容，用cite标签标注来源即可

3. **准确性**：如果材料中有相关内容，请优先使用并标注来源；如果材料不足以完整回答，请诚实说明

4. **清晰度**：回答要清晰、有条理，必要时使用分点说明

现在请回答问题："""

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
            # 【智能模型选择】根据输入类型和context内容选择模型
            has_image_input = bool(image or file_content)
            has_image_in_context = self._check_image_in_context(self.last_context_docs) if hasattr(self, 'last_context_docs') and self.last_context_docs else False
            
            if has_image_input or has_image_in_context:
                selected_model = self.multimodal_model
                model_type = "多模态模型"
                if has_image_in_context:
                    print(f"  🖼️  检测到context中有图片引用，使用多模态模型")
                    # 【重要】如果context中有图片，需要将原图传给多模态模型
                    if not image:
                        # 从retrieved_docs中提取图片路径
                        for doc in self.last_context_docs:
                            if doc.get('type') == 'image' and 'image_path' in doc:
                                image = doc['image_path']
                                print(f"  📎 自动附加图片: {os.path.basename(image)}")
                                break
            else:
                selected_model = self.text_model
                model_type = "文本模型"
                print(f"  📝 纯文本context，使用文本模型")
            
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
                max_tokens=max_tokens
            )
            
            print(f"  ✅ 收到LLM响应")

            answer = response.choices[0].message.content
            
            # 【新增】修复LaTeX公式格式
            answer = self._fix_latex_format(answer)
            
            # 【新增】修复引用格式
            answer = self._fix_citation_format(answer)
            
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
        thinking_mode: str = 'fast',  # 'fast' 或 'thinking' (使用CoT)
        stream_thinking: bool = False,  # 是否流式输出思考过程
        temperature: float = 0.7,  # LLM温度参数
        max_tokens: int = 2000,  # LLM最大token数
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
            # 使用SOTA检索：BM25+向量+RRF+API Reranker
            context, retrieved_docs = self.retrieve_context_sota(enhanced_query, top_k=top_k)
            
            # 【立即打印检索结果】
            self._print_retrieved_context(retrieved_docs)
            
            # 2.3 生成回答：原图 + context → 多模态模型
            answer = self.generate_response(
                query, context, chat_history, query_type,
                image=image_path,  # 传原图
                file_content=None,
                use_multimodal_model=True,  # 强制使用多模态模型
                enable_socratic=enable_socratic,
                thinking_mode=thinking_mode,
                temperature=temperature,
                max_tokens=max_tokens
            )
            
        elif file_content:
            # ===== 情况3: 有文件输入 =====
            print("\n📄 检测到文件输入，使用多模态处理流程")
            
            # 3.1 用原始query检索
            query_type = self.analyze_query_type(query)
            # 使用SOTA检索：BM25+向量+RRF+API Reranker
            context, retrieved_docs = self.retrieve_context_sota(query, top_k=top_k)
            
            # 【立即打印检索结果】
            self._print_retrieved_context(retrieved_docs)
            
            # 3.2 生成回答：文件内容 + context → 多模态模型
            answer = self.generate_response(
                query, context, chat_history, query_type,
                image=None,
                file_content=file_content,  # 传文件内容
                use_multimodal_model=True,  # 强制使用多模态模型
                enable_socratic=enable_socratic,
                thinking_mode=thinking_mode,
                temperature=temperature,
                max_tokens=max_tokens
            )
            
        else:
            # ===== 情况1: 纯文本输入 =====
            print("\n📝 纯文本输入，使用文本模型")
            
            # 1.1 分析问题类型
            query_type = self.analyze_query_type(query)
            
            # 1.2 在文字和图片库都检索
            # 使用SOTA检索：BM25+向量+RRF+API Reranker
            context, retrieved_docs = self.retrieve_context_sota(query, top_k=top_k)
            
            # 【立即打印检索结果】
            self._print_retrieved_context(retrieved_docs)
            
            # 1.3 生成回答：使用纯文本模型
            answer = self.generate_response(
                query, context, chat_history, query_type,
                image=None,
                file_content=None,
                use_multimodal_model=False,  # 强制使用文本模型
                enable_socratic=enable_socratic,
                thinking_mode=thinking_mode,
                temperature=temperature,
                max_tokens=max_tokens
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
