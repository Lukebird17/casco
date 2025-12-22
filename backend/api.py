"""
FastAPI 后端 API
为 React 前端提供 RESTful 接口
"""

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, HTMLResponse
from pydantic import BaseModel
from typing import List, Dict, Optional, Tuple
from contextlib import asynccontextmanager
import sys
import os
import json
import asyncio

# 添加父目录到路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 导入核心模块
from src.core.rag_agent import RAGAgent
from src.utils.session_manager import SessionManager
from src.evaluators.confidence_calculator import ConfidenceCalculator
from src.features.quiz_generator import QuizGenerator
from src.features.flashcard_system import FlashcardSystem
from src.features.knowledge_graph import KnowledgeGraph

# 尝试导入 LlamaIndex 版本
try:
    from src.features.knowledge_graph_llamaindex import LlamaIndexKnowledgeGraph
    USE_LLAMAINDEX_KG = True
    print("✅ LlamaIndex 知识图谱可用")
except ImportError:
    USE_LLAMAINDEX_KG = False
    print("⚠️  LlamaIndex 知识图谱不可用，使用标准版本")

from src.evaluators.quality_evaluator import QualityEvaluator
from config import *

# ============================================================
# 全局实例
# ============================================================

rag_agent = None
session_manager = None
confidence_calculator = None
quiz_generator = None
flashcard_system = None
knowledge_graph = None
quality_evaluator = None  # 新增：质量评估器

# 全局变量：跟踪正在运行的评估任务（每个会话一个）
active_evaluation_tasks = {}  # {session_id: asyncio.Task}

# ============================================================
# Lifespan 事件处理（替代 on_event）
# ============================================================

@asynccontextmanager
async def lifespan(app: FastAPI):
    """应用生命周期管理"""
    global rag_agent, session_manager, confidence_calculator, quiz_generator, flashcard_system, knowledge_graph, quality_evaluator
    
    # 启动时初始化
    try:
        print("🚀 正在初始化 RAG Agent...")
        
        # 调试：检查数据库路径
        from config import VECTOR_DB_PATH
        import os
        abs_db_path = os.path.abspath(VECTOR_DB_PATH)
        print(f"📂 数据库路径: {abs_db_path}")
        db_file = os.path.join(abs_db_path, "chroma.sqlite3")
        db_exists = os.path.exists(db_file)
        if db_exists:
            db_size = os.path.getsize(db_file) / (1024*1024)  # MB
            print(f"✅ 数据库文件存在: {db_size:.2f} MB")
        else:
            print(f"❌ 数据库文件不存在！")
        
        rag_agent = RAGAgent(
            model=MODEL_NAME,
            enable_tracking=True,
            enable_cot=True,
            use_multimodal=True
        )
        
        session_manager = SessionManager()
        confidence_calculator = ConfidenceCalculator()
        quiz_generator = QuizGenerator()
        flashcard_system = FlashcardSystem()
        # 根据可用性选择知识图谱实现
        if USE_LLAMAINDEX_KG:
            knowledge_graph = LlamaIndexKnowledgeGraph()
            print("✅ 使用 LlamaIndex 知识图谱")
        else:
            knowledge_graph = KnowledgeGraph()
            print("✅ 使用标准知识图谱")
        
        # 初始化质量评估器（使用简单快速版本）
        quality_evaluator = QualityEvaluator()
        print("✅ 质量评估器初始化成功（简单版）")
        
        # 如果没有会话，创建一个默认会话
        if not session_manager.sessions:
            default_session = session_manager.create_session("欢迎对话")
            print(f"✅ 创建默认会话: {default_session.session_id}")
        
        print("✅ RAG Agent 和所有工具初始化成功")
    except Exception as e:
        print(f"❌ 初始化失败: {e}")
        raise
    
    yield
    
    # 关闭时清理（如果需要）
    print("🛑 正在关闭 RAG Agent...")

# ============================================================
# 应用初始化
# ============================================================

app = FastAPI(
    title="RAG Agent API",
    description="智能问答系统 API",
    version="2.0.0",
    lifespan=lifespan
)

# 挂载静态文件服务（用于文档图片）
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
if not os.path.exists(static_dir):
    os.makedirs(static_dir, exist_ok=True)
    doc_images_dir = os.path.join(static_dir, "doc_images")
    os.makedirs(doc_images_dir, exist_ok=True)
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# CORS 配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生产环境应该限制具体域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================
# 数据模型
# ============================================================

class InitRequest(BaseModel):
    """初始化请求"""
    pass

class ChatRequest(BaseModel):
    """聊天请求"""
    message: str
    session_id: str
    enable_socratic: bool = False
    thinking_mode: str = 'fast'  # 'fast' 或 'thinking'
    knowledge_base_id: str = 'default'  # 知识库ID
    image_base64: Optional[str] = None
    file_content: Optional[str] = None  # 文件内容
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 2000
    retrieval_k: Optional[int] = 5

class SessionResponse(BaseModel):
    """会话响应"""
    session_id: str
    name: str
    created_at: str
    is_current: bool = False

class MessageResponse(BaseModel):
    """消息响应"""
    role: str
    content: str
    timestamp: str

# ============================================================
# API 端点
# ============================================================

# ============ 辅助函数 ============

def extract_headings_from_pdf(doc):
    """
    基于字体和格式的启发式PDF标题提取
    
    逻辑：
    1. 分析每页的文本块
    2. 根据字体大小、加粗属性、行间距判断标题
    3. 最大字体的加粗行视为一级标题
    """
    import fitz
    
    headings = []
    font_sizes = []
    
    # 第一遍扫描：收集字体大小信息
    for page_num in range(min(50, doc.page_count)):  # 只扫描前50页
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]
        
        for block in blocks:
            if block.get("type") == 0:  # 文本块
                for line in block.get("lines", []):
                    for span in line.get("spans", []):
                        font_size = span.get("size", 0)
                        if font_size > 0:
                            font_sizes.append(font_size)
    
    if not font_sizes:
        return []
    
    # 计算字体大小阈值
    font_sizes.sort(reverse=True)
    avg_font_size = sum(font_sizes) / len(font_sizes)
    max_font_size = font_sizes[0]
    
    # 标题阈值：大于平均字体的1.2倍
    title_threshold = avg_font_size * 1.2
    
    print(f"📊 字体分析: 平均={avg_font_size:.1f}, 最大={max_font_size:.1f}, 阈值={title_threshold:.1f}")
    
    # 第二遍扫描：提取标题
    heading_id = 0
    for page_num in range(doc.page_count):
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]
        
        for block in blocks:
            if block.get("type") == 0:  # 文本块
                for line in block.get("lines", []):
                    # 获取该行的最大字体
                    line_fonts = []
                    line_text = ""
                    is_bold = False
                    
                    for span in line.get("spans", []):
                        font_size = span.get("size", 0)
                        text = span.get("text", "").strip()
                        font_flags = span.get("flags", 0)
                        
                        line_fonts.append(font_size)
                        line_text += text
                        
                        # 检查是否加粗 (flags & 16 表示加粗)
                        if font_flags & 16:
                            is_bold = True
                    
                    if not line_text or not line_fonts:
                        continue
                    
                    max_line_font = max(line_fonts)
                    line_text = line_text.strip()
                    
                    # 判断是否为标题
                    # 条件：1. 字体大于阈值 2. 文本长度合适 3. 不以标点结尾
                    if (max_line_font >= title_threshold and 
                        3 < len(line_text) < 100 and
                        not line_text.endswith(('。', '.', '，', ',', '：', ':', '；', ';'))):
                        
                        # 确定标题级别（基于字体大小）
                        if max_line_font >= max_font_size * 0.95:
                            level = 1  # 一级标题
                        elif max_line_font >= max_font_size * 0.85:
                            level = 2  # 二级标题
                        else:
                            level = 3  # 三级标题
                        
                        # 加粗的文本更可能是标题，提升优先级
                        if is_bold and level > 1:
                            level -= 1
                        
                        headings.append({
                            "id": f"heading-{heading_id}",
                            "title": line_text,
                            "level": level,
                            "page": page_num + 1,
                            "font_size": round(max_line_font, 1),
                            "is_bold": is_bold,
                            "subsections": []
                        })
                        heading_id += 1
                        
                        # 限制提取数量
                        if heading_id >= 100:
                            break
                
                if heading_id >= 100:
                    break
        
        if heading_id >= 100:
            break
    
    print(f"✅ 智能提取了 {len(headings)} 个标题")
    return headings

# ============ API路由 ============

@app.post("/api/init")
async def initialize():
    """
    初始化系统
    """
    try:
        if rag_agent is None:
            raise HTTPException(status_code=500, detail="系统未正确初始化")
        
        return {
            "success": True,
            "message": "系统初始化成功"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/chat")
async def chat(request: ChatRequest):
    """
    处理聊天消息
    """
    try:
        if rag_agent is None:
            raise HTTPException(status_code=500, detail="RAG Agent 未初始化")
        
        # 获取或创建会话
        if session_manager is None:
            raise HTTPException(status_code=500, detail="会话管理器未初始化")
        
        session = session_manager.get_session(request.session_id)
        if not session:
            session = session_manager.create_session("新对话")
            request.session_id = session.session_id
        
        # 获取会话历史
        chat_history = session.messages
        is_first_message = len(chat_history) == 0
        
        # 打印思考模式和知识库
        print(f"\n{'='*80}")
        print(f"📝 用户问题: {request.message}")
        print(f"🧠 思考模式: {request.thinking_mode.upper()}")
        print(f"📚 知识库: {request.knowledge_base_id}")
        print(f"{'='*80}\n")
        
        # 切换到指定的知识库
        if request.knowledge_base_id:
            try:
                from config import get_kb_vector_dir, get_kb_data_dir, COLLECTION_NAME
                from src.core.vector_store import VectorStore
                from src.core.image_vector_store import ImageVectorStore
                
                kb_vector_path = get_kb_vector_dir(request.knowledge_base_id)
                kb_data_path = get_kb_data_dir(request.knowledge_base_id)
                
                if os.path.exists(kb_vector_path):
                    print(f"🔄 正在切换知识库...")
                    print(f"   目标库: {request.knowledge_base_id}")
                    print(f"   向量路径: {kb_vector_path}")
                    print(f"   数据路径: {kb_data_path}")
                    
                    # 1. 重新初始化 VectorStore（使用正确的collection名称）
                    new_vector_store = VectorStore(
                        db_path=kb_vector_path,
                        collection_name=COLLECTION_NAME  # 使用配置中的名称：course_documents
                    )
                    
                    # 检查collection的文档数量
                    doc_count = new_vector_store.get_collection_count()
                    print(f"   ✅ 文本向量库已更新")
                    print(f"   📊 Collection文档数量: {doc_count}")
                    print(f"   📂 数据库路径: {kb_vector_path}")
                    print(f"   📝 Collection名称: {COLLECTION_NAME}")
                    
                    if doc_count == 0:
                        print(f"   ⚠️  警告：该知识库为空！请先上传文档。")
                    
                    rag_agent.vector_store = new_vector_store
                    
                    # 2. 更新 HybridRetriever（如果启用）
                    if hasattr(rag_agent, 'hybrid_retriever') and rag_agent.hybrid_retriever:
                        # 更新text_store引用
                        rag_agent.hybrid_retriever.text_store = new_vector_store
                        rag_agent.hybrid_retriever.vector_store = new_vector_store  # 也更新这个引用
                        print(f"   ✅ HybridRetriever.text_store 已更新")
                        
                        # 更新image_store到对应的知识库图片库
                        images_dir = os.path.join(kb_data_path, "images")
                        image_vector_dir = os.path.join(kb_vector_path, "images")
                        
                        if os.path.exists(images_dir):
                            try:
                                new_image_store = ImageVectorStore(
                                    db_path=image_vector_dir,
                                    image_dir=images_dir
                                )
                                rag_agent.hybrid_retriever.image_store = new_image_store
                                print(f"   ✅ HybridRetriever.image_store 已更新: {images_dir}")
                            except Exception as img_err:
                                print(f"   ⚠️  图片库更新失败: {img_err}")
                        else:
                            print(f"   ℹ️  该知识库无图片目录: {images_dir}")
                    
                    print(f"✅ 已切换到知识库: {request.knowledge_base_id}")
                else:
                    print(f"⚠️  知识库路径不存在: {kb_vector_path}")
            except Exception as e:
                print(f"⚠️  切换知识库失败: {e}，使用当前库")
                import traceback
                traceback.print_exc()
        
        # 处理消息 - 根据输入类型调用不同逻辑
        # 1. 纯文本：文字+图片库检索 → 文本模型
        # 2. 有图片：描述图片 → 增强query检索 → 原图+context → 多模态模型
        # 3. 有文件：原始query检索 → 文件内容+context → 多模态模型
        
        response_text = rag_agent.answer_question(
            request.message,
            chat_history=chat_history,
            image=request.image_base64 if request.image_base64 else None,
            file_content=request.file_content if request.file_content else None,
            enable_socratic=request.enable_socratic,
            thinking_mode=request.thinking_mode,
            top_k=request.retrieval_k or 10,  # 使用前端传来的retrieval_k，默认10
            temperature=request.temperature or 0.7,
            max_tokens=request.max_tokens or 2000
        )
        
        # 提取引用（在添加消息之前）并去重
        # Context已经在rag_agent中打印，这里只收集用于前端展示
        citations = []
        seen_cite_ids = {}  # 用于去重
        if hasattr(rag_agent, 'last_context_docs') and rag_agent.last_context_docs:
            for doc in rag_agent.last_context_docs[:10]:  # 扩展到10个，去重后取前5
                filename = doc.get("filename", "未知")
                # 优先使用page_number（vector_store的标准字段）
                page_num = doc.get("page_number", doc.get("page_num", 0))
                section = doc.get("section", "")
                content_snippet = doc.get("content", "")[:200]
                
                # 【重要】从metadata中获取image_url
                metadata = doc.get("metadata", {})
                image_url = doc.get("image_url") or metadata.get("image_url")
                
                # 补全完整的 URL (如果前端和后端不同端口，需要加上后端域名)
                if image_url and not image_url.startswith("http"):
                    image_url = f"http://localhost:8000{image_url}"
                
                # 生成cite_id用于去重
                cite_id = f"{filename}_p{page_num}".replace(' ', '_').replace('.pdf', '').replace('.docx', '')
                score = doc.get("score", doc.get("rerank_score", 0))
                
                # 去重：保留分数更高的
                if cite_id not in seen_cite_ids or score > seen_cite_ids[cite_id]["score"]:
                    seen_cite_ids[cite_id] = {
                        "id": cite_id,
                        "filename": filename,
                        "page": page_num,
                        "section": section,
                        "snippet": content_snippet,
                        "image_url": image_url,
                        "score": score,
                        "kb_id": request.knowledge_base_id or "default"  # ✅ 添加知识库ID
                    }
            
            # 转换为列表，按分数排序，取前5个
            citations = sorted(seen_cite_ids.values(), key=lambda x: x["score"], reverse=True)[:5]
        
        # 计算置信度
        confidence = None
        if hasattr(rag_agent, 'last_retrieval_results') and rag_agent.last_retrieval_results:
            confidence = confidence_calculator.calculate(
                request.message,
                response_text,
                rag_agent.last_retrieval_results
            )
        
        # 添加消息到会话
        session.add_message("user", request.message)
        message_idx = len(session.messages) - 1
        session.add_message("assistant", response_text)
        
        # 保存引用信息
        if citations:
            session.add_citation(message_idx + 1, citations)
        
        # 如果是第一条消息，自动生成会话标题
        if is_first_message:
            # 从用户消息中提取标题（取前20个字符）
            auto_title = request.message.strip()[:20]
            if len(request.message) > 20:
                auto_title += "..."
            session_manager.update_session_title(session.session_id, auto_title)
        
        session_manager._save_session(session)
        
        return {
            "success": True,
            "response": response_text,
            "confidence": confidence,
            "citations": citations
        }
        
    except Exception as e:
        print(f"❌ 聊天错误: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/chat/stream")
async def chat_stream(request: ChatRequest):
    """
    流式处理聊天消息 - 先返回检索结果，再返回答案
    """
    async def generate():
        try:
            if rag_agent is None:
                yield f"data: {json.dumps({'type': 'error', 'data': 'RAG Agent 未初始化'})}\n\n"
                return
            
            # 获取或创建会话
            session = session_manager.get_session(request.session_id)
            if not session:
                session = session_manager.create_session("新对话")
                request.session_id = session.session_id
            
            chat_history = session.messages
            
            # ⚡ 取消该会话之前正在运行的评估任务
            if request.session_id in active_evaluation_tasks:
                old_task = active_evaluation_tasks[request.session_id]
                if not old_task.done():
                    print(f"🛑 检测到新问题，取消会话 {request.session_id} 的旧评估任务")
                    old_task.cancel()
                    try:
                        await old_task
                    except asyncio.CancelledError:
                        print("✅ 旧评估任务已取消")
                del active_evaluation_tasks[request.session_id]
            
            # 打印日志
            print(f"\n{'='*80}")
            print(f"📝 用户问题: {request.message}")
            print(f"🧠 思考模式: {request.thinking_mode.upper()}")
            print(f"📚 知识库: {request.knowledge_base_id}")
            print(f"{'='*80}\n")
            
            # 切换知识库（如果需要）
            if request.knowledge_base_id:
                try:
                    from config import get_kb_vector_dir, get_kb_data_dir, COLLECTION_NAME
                    from src.core.vector_store import VectorStore
                    from src.core.image_vector_store import ImageVectorStore
                    
                    kb_vector_path = get_kb_vector_dir(request.knowledge_base_id)
                    kb_data_path = get_kb_data_dir(request.knowledge_base_id)
                    
                    if os.path.exists(kb_vector_path):
                        new_vector_store = VectorStore(
                            db_path=kb_vector_path,
                            collection_name=COLLECTION_NAME
                        )
                        rag_agent.vector_store = new_vector_store
                        
                        if hasattr(rag_agent, 'hybrid_retriever') and rag_agent.hybrid_retriever:
                            rag_agent.hybrid_retriever.text_store = new_vector_store
                            rag_agent.hybrid_retriever.vector_store = new_vector_store
                except Exception as e:
                    print(f"⚠️  切换知识库失败: {e}")
            
            # === 第1步：发送"分析问题"状态 ===
            yield f"data: {json.dumps({'type': 'status', 'data': '正在分析问题类型...'}, ensure_ascii=False)}\n\n"
            
            # === 第2步：发送"检索中"状态 ===
            yield f"data: {json.dumps({'type': 'status', 'data': '正在检索知识库...'}, ensure_ascii=False)}\n\n"
            
            # === 第3步：先执行检索（在线程池中执行以避免阻塞） ===
            import concurrent.futures
            import time  # ✅ 添加time模块
            executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
            
            # 分析query类型
            query_type = await asyncio.get_event_loop().run_in_executor(
                executor, 
                rag_agent.analyze_query_type, 
                request.message
            )
            
            # ✅ 检索计时开始
            retrieval_start_time = time.time()
            
            # 执行SOTA检索
            def do_retrieval():
                context, retrieved_docs = rag_agent.retrieve_context_sota(
                    request.message, 
                    top_k=request.retrieval_k or 10
                )
                # 保存检索结果（供后续使用）
                rag_agent.last_context_docs = retrieved_docs
                rag_agent.last_retrieval_results = retrieved_docs
                return context, retrieved_docs
            
            context, retrieved_docs = await asyncio.get_event_loop().run_in_executor(
                executor,
                do_retrieval
            )
            
            # ✅ 检索计时结束
            retrieval_time = time.time() - retrieval_start_time
            print(f"⏱️  检索耗时: {retrieval_time:.2f}秒")
            
            # === 第4步：提取检索结果（包含图片URL）并去重 ===
            citations = []
            seen_cite_ids = {}  # 用于去重
            for doc in retrieved_docs:
                metadata = doc.get("metadata", {})
                image_url = doc.get("image_url") or metadata.get("image_url")
                
                if image_url and not image_url.startswith("http"):
                    image_url = f"http://localhost:8000{image_url}"
                
                # 生成cite_id（与后端格式化context时一致）
                filename = doc.get("filename", "未知")
                # 优先使用page_number（vector_store的标准字段）
                page_num = doc.get("page_number", doc.get("page_num", 0))
                cite_id = f"{filename}_p{page_num}".replace(' ', '_').replace('.pdf', '').replace('.docx', '')
                
                # 去重：如果已存在相同cite_id，保留分数更高的
                score = doc.get("score", doc.get("rerank_score", 0))
                if cite_id in seen_cite_ids:
                    if score > seen_cite_ids[cite_id]["score"]:
                        # 替换为分数更高的
                        seen_cite_ids[cite_id] = {
                            "id": cite_id,
                            "filename": filename,
                            "page": page_num,
                            "snippet": doc.get("content", "")[:200],
                            "image_url": image_url,
                            "score": score,
                            "kb_id": request.knowledge_base_id or "default"  # ✅ 添加知识库ID
                        }
                else:
                    # 首次出现，直接添加
                    seen_cite_ids[cite_id] = {
                        "id": cite_id,
                        "filename": filename,
                        "page": page_num,
                        "snippet": doc.get("content", "")[:200],
                        "image_url": image_url,
                        "score": score,
                        "kb_id": request.knowledge_base_id or "default"  # ✅ 添加知识库ID
                    }
            
            # 转换为列表，按分数排序
            citations = sorted(seen_cite_ids.values(), key=lambda x: x["score"], reverse=True)
            
            # === 第5步：发送检索结果（让用户看到找到的文档）+ 检索时间 ===
            yield f"data: {json.dumps({'type': 'citations', 'data': citations, 'retrieval_time': round(retrieval_time, 2)}, ensure_ascii=False)}\n\n"
            
            # === 第6步：发送"生成中"状态 ===
            yield f"data: {json.dumps({'type': 'status', 'data': '正在整合信息并生成回答...'}, ensure_ascii=False)}\n\n"
            
            # ✅ 生成计时开始
            generation_start_time = time.time()
            
            # === 第7步：生成答案（在线程池中执行） ===
            def do_generation():
                return rag_agent.generate_response(
                    request.message,
                    context,
                    chat_history,
                    query_type,
                    image=request.image_base64 if request.image_base64 else None,
                    file_content=request.file_content if request.file_content else None,
                    use_multimodal_model=bool(request.image_base64 or request.file_content),
                    enable_socratic=request.enable_socratic,
                    thinking_mode=request.thinking_mode,
                    temperature=request.temperature or 0.7,
                    max_tokens=request.max_tokens or 2000
                )
            
            response_text = await asyncio.get_event_loop().run_in_executor(
                executor,
                do_generation
            )
            
            # ✅ 生成计时结束
            generation_time = time.time() - generation_start_time
            print(f"⏱️  生成耗时: {generation_time:.2f}秒")
            
            # === 第8步：发送答案 + 生成时间 ===
            yield f"data: {json.dumps({'type': 'answer', 'data': response_text, 'generation_time': round(generation_time, 2)}, ensure_ascii=False)}\n\n"
            
            # === 第9步：质量评估（雷达图）- 完全后台运行，不阻塞 ===
            # ⚡ 先发送"评估中"状态，告诉前端正在评估
            yield f"data: {json.dumps({'type': 'quality_metrics', 'data': {'status': 'evaluating'}}, ensure_ascii=False)}\n\n"
            
            # ⚡ 评估完全在后台进行，这里只是启动任务，不等待结果
            if quality_evaluator and hasattr(rag_agent, 'last_context_docs') and rag_agent.last_context_docs:
                # 记录当前消息的索引（评估结果将关联到这条消息）
                current_message_idx = len(session.messages)  # 当前user消息的索引
                print(f"🔍 准备启动质量评估，消息索引: {current_message_idx}")
                print(f"🔍 quality_evaluator: {quality_evaluator is not None}")
                print(f"🔍 last_context_docs数量: {len(rag_agent.last_context_docs)}")
                
                # 定义后台评估函数
                async def run_background_evaluation():
                    eval_start_time = time.time()
                    try:
                        print("📊 后台质量评估开始...")
                        quality_metrics = await asyncio.wait_for(
                            quality_evaluator.evaluate(
                                query=request.message,
                                answer=response_text,
                                retrieved_context=rag_agent.last_context_docs,
                                chat_history=chat_history
                            ),
                            timeout=120.0  # ⚡ 增加到120秒，给LLM更多时间
                        )
                        eval_time = time.time() - eval_start_time
                        print(f"✅ 后台评估完成: 总分 {quality_metrics.get('overall_score', 0)}, 耗时 {eval_time:.2f}秒")
                        print(f"📊 雷达图数据: {quality_metrics.get('radar_data', [])}")
                        quality_metrics['eval_time'] = round(eval_time, 2)
                        
                        # ✅ 保存到对应消息的评估结果（而不是session级别）
                        if session:
                            session.add_quality_metrics(current_message_idx + 1, quality_metrics)  # +1 是assistant消息的索引
                            session_manager._save_session(session)
                            print(f"✅ 评估结果已保存到消息索引 {current_message_idx + 1}")
                    except asyncio.CancelledError:
                        print("🛑 后台评估已被取消（新问题到来）")
                        raise  # 重新抛出，让任务正常取消
                    except asyncio.TimeoutError:
                        eval_time = time.time() - eval_start_time
                        print(f"⚠️  后台评估超时（120秒），可能是LLM响应太慢")
                        print(f"    建议：检查模型配置或网络连接")
                    except Exception as e:
                        print(f"❌ 后台评估错误: {e}")
                        import traceback
                        traceback.print_exc()
                    finally:
                        # 清理任务记录
                        if request.session_id in active_evaluation_tasks:
                            del active_evaluation_tasks[request.session_id]
                
                # ⚡ 启动后台任务（fire-and-forget），不阻塞主流程
                eval_task = asyncio.create_task(run_background_evaluation())
                active_evaluation_tasks[request.session_id] = eval_task  # ✅ 记录任务
                print(f"✅ 后台评估任务已启动")
                
                # ⚡ 不再等待快速评估，直接让评估在后台运行
                # 用户可以立即继续操作，评估完成后结果会保存到session中
            else:
                print(f"⚠️  跳过质量评估: quality_evaluator={quality_evaluator is not None}, has_docs={hasattr(rag_agent, 'last_context_docs') and bool(rag_agent.last_context_docs)}")
            
            # === 第10步：保存会话 ===
            session.add_message("user", request.message)
            message_idx = len(session.messages) - 1
            session.add_message("assistant", response_text)
            
            # 保存引用信息
            if citations:
                session.add_citation(message_idx + 1, citations)
            
            is_first_message = len(session.messages) == 2
            if is_first_message:
                auto_title = request.message[:20]
                if len(request.message) > 20:
                    auto_title += "..."
                session_manager.update_session_title(session.session_id, auto_title)
            
            session_manager._save_session(session)
            
            # 发送完成信号
            yield f"data: {json.dumps({'type': 'done'})}\n\n"
            
        except Exception as e:
            print(f"❌ 流式聊天错误: {e}")
            import traceback
            traceback.print_exc()
            yield f"data: {json.dumps({'type': 'error', 'data': str(e)}, ensure_ascii=False)}\n\n"
    
    return StreamingResponse(generate(), media_type="text/event-stream")

@app.get("/api/sessions/{session_id}/quality-metrics")
async def get_quality_metrics(session_id: str, message_idx: int = None):
    """
    获取会话的质量评估结果
    - 如果提供message_idx，返回该消息的评估结果
    - 如果不提供，返回最新消息的评估结果
    """
    try:
        session = session_manager.get_session(session_id)
        if not session:
            raise HTTPException(status_code=404, detail="会话不存在")
        
        # 获取quality_metrics字典
        quality_metrics_dict = getattr(session, 'quality_metrics', {})
        
        if message_idx is not None:
            # 返回指定消息的评估结果
            quality_metrics = quality_metrics_dict.get(str(message_idx))
        else:
            # 返回最新消息的评估结果（最大的索引）
            if quality_metrics_dict:
                latest_idx = max([int(k) for k in quality_metrics_dict.keys()])
                quality_metrics = quality_metrics_dict.get(str(latest_idx))
            else:
                quality_metrics = None
        
        if quality_metrics:
            return {"success": True, "data": quality_metrics}
        else:
            # 检查是否有正在运行的评估任务
            if session_id in active_evaluation_tasks and not active_evaluation_tasks[session_id].done():
                return {"success": False, "status": "evaluating", "message": "评估进行中"}
            else:
                return {"success": False, "status": "pending", "message": "评估尚未完成"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/sessions")
async def get_sessions():
    """
    获取所有会话列表
    """
    try:
        sessions = session_manager.list_sessions()
        current_id = session_manager.current_session_id
        
        result = []
        for session_info in sessions:
            result.append({
                "session_id": session_info["session_id"],
                "name": session_info["title"],
                "created_at": session_info["updated_at"],
                "is_current": session_info["session_id"] == current_id
            })
        
        return result
    except Exception as e:
        print(f"❌ 获取会话列表错误: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/sessions/new")
async def create_new_session():
    """
    创建新会话
    """
    try:
        session = session_manager.create_session("新对话")
        
        return {
            "success": True,
            "session_id": session.session_id
        }
    except Exception as e:
        print(f"❌ 创建会话错误: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/sessions/{session_id}/messages")
async def get_session_messages(session_id: str):
    """
    获取会话消息历史
    """
    try:
        session = session_manager.get_session(session_id)
        if not session:
            return {
                "success": True,
                "messages": []
            }
        
        return {
            "success": True,
            "messages": session.messages
        }
    except Exception as e:
        print(f"❌ 获取会话消息错误: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/sessions/{session_id}")
async def delete_session(session_id: str):
    """
    删除会话
    """
    try:
        success = session_manager.delete_session(session_id)
        if success:
            # 获取新的当前会话ID
            current_session = session_manager.get_current_session()
            return {
                "success": True,
                "message": "会话已删除",
                "current_session_id": current_session.session_id if current_session else None
            }
        else:
            raise HTTPException(status_code=404, detail="会话不存在")
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ 删除会话错误: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/api/sessions/{session_id}/rename")
async def rename_session(session_id: str, request: dict):
    """
    重命名会话
    """
    try:
        new_name = request.get("name", "").strip()
        if not new_name:
            raise HTTPException(status_code=400, detail="会话名称不能为空")
        
        session_manager.update_session_title(session_id, new_name)
        
        return {
            "success": True,
            "message": "会话已重命名",
            "name": new_name
        }
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ 重命名会话错误: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/upload")
async def upload_file(file: UploadFile = File(...)):
    """
    上传文件并返回文件内容
    支持 PDF, DOCX, TXT, MD 等文件
    """
    try:
        print(f"📤 接收文件上传: {file.filename}")
        
        # 读取文件内容
        content = await file.read()
        file_size = len(content) / (1024 * 1024)  # MB
        print(f"   文件大小: {file_size:.2f} MB")
        
        # 根据文件类型处理
        file_ext = os.path.splitext(file.filename)[1].lower()
        file_content = ""
        
        if file_ext == '.txt' or file_ext == '.md':
            # 纯文本文件
            try:
                file_content = content.decode('utf-8')
            except:
                file_content = content.decode('gbk', errors='ignore')
        
        elif file_ext == '.pdf':
            # PDF 文件 - 使用 PyPDF2
            try:
                from io import BytesIO
                import PyPDF2
                pdf_file = BytesIO(content)
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                pages_text = []
                for page_num, page in enumerate(pdf_reader.pages, 1):
                    text = page.extract_text()
                    pages_text.append(f"[第 {page_num} 页]\n{text}")
                file_content = "\n\n".join(pages_text)
            except Exception as e:
                print(f"   ⚠️ PDF解析失败: {e}")
                file_content = f"[PDF文件: {file.filename}, 无法提取文本内容]"
        
        elif file_ext == '.docx':
            # DOCX 文件 - 使用 python-docx
            try:
                from io import BytesIO
                import docx
                doc_file = BytesIO(content)
                doc = docx.Document(doc_file)
                paragraphs = [para.text for para in doc.paragraphs if para.text.strip()]
                file_content = "\n\n".join(paragraphs)
            except Exception as e:
                print(f"   ⚠️ DOCX解析失败: {e}")
                file_content = f"[DOCX文件: {file.filename}, 无法提取文本内容]"
        
        else:
            # 不支持的文件类型
            file_content = f"[不支持的文件类型: {file_ext}]"
        
        print(f"   ✅ 文件内容提取完成: {len(file_content)} 字符")
        
        return {
            "success": True,
            "filename": file.filename,
            "content": file_content[:100000],  # 限制最多10万字符
            "size": file_size,
            "type": file_ext
        }
    except Exception as e:
        print(f"❌ 上传文件错误: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

class QuizRequest(BaseModel):
    """测验生成请求"""
    kb_id: str  # ✅ 改为知识库ID
    num_questions: int = 5
    difficulty: str = "medium"

@app.post("/api/quiz/generate")
async def generate_quiz(request: QuizRequest):
    """
    生成测验 - 基于知识库内容
    """
    try:
        if quiz_generator is None:
            raise HTTPException(status_code=500, detail="测验生成器未初始化")
        
        # ✅ 从向量库获取文档内容作为context
        from pathlib import Path
        kb_vector_dir = Path(get_kb_vector_dir(request.kb_id))
        if not kb_vector_dir.exists():
            raise HTTPException(status_code=404, detail=f"知识库 {request.kb_id} 不存在或未初始化")
        
        # 从向量库中获取所有文档
        try:
            # 临时创建一个向量存储实例来获取文档
            from src.core.vector_store import VectorStore
            temp_vector_store = VectorStore(
                db_path=str(kb_vector_dir),  # ✅ 使用db_path参数
                collection_name=COLLECTION_NAME
            )
            
            # 获取所有文档（通过查询一个空字符串或通用术语）
            all_docs = temp_vector_store.collection.get(
                limit=100,  # 获取最多100个文档片段
                include=['documents', 'metadatas']
            )
            
            context_parts = []
            if all_docs and all_docs.get('documents'):
                for doc in all_docs['documents'][:20]:  # 取前20个片段
                    if doc and len(doc.strip()) > 50:  # 确保文档有实质内容
                        context_parts.append(doc[:800])  # 每个片段最多800字符
            
            context = "\n\n".join(context_parts)
            if not context.strip():
                raise HTTPException(status_code=400, detail="知识库中没有可用内容生成测验。请先上传文档到该知识库。")
        except Exception as e:
            print(f"⚠️ 从向量库获取文档失败: {e}")
            raise HTTPException(status_code=400, detail=f"获取知识库内容失败: {str(e)}")
        
        print(f"📝 准备生成测验，上下文长度: {len(context)} 字符")
        
        questions = quiz_generator.generate_quiz(
            context,
            request.num_questions,
            request.difficulty
        )
        
        return {
            "success": True,
            "questions": questions
        }
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ 生成测验错误: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

class GradeRequest(BaseModel):
    """评分请求"""
    question: Dict
    user_answer: str

@app.post("/api/quiz/grade")
async def grade_answer(request: GradeRequest):
    """
    评分答案
    """
    try:
        if quiz_generator is None:
            raise HTTPException(status_code=500, detail="测验生成器未初始化")
        
        result = quiz_generator.grade_answer(request.question, request.user_answer)
        
        return {
            "success": True,
            **result
        }
    except Exception as e:
        print(f"❌ 评分错误: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/flashcards/due")
async def get_due_flashcards(limit: int = 20):
    """
    获取待复习闪卡
    """
    try:
        if flashcard_system is None:
            raise HTTPException(status_code=500, detail="闪卡系统未初始化")
        
        due_cards = flashcard_system.get_due_cards(limit)
        cards_data = [card.to_dict() for card in due_cards]
        
        return {
            "success": True,
            "flashcards": cards_data,
            "count": len(cards_data)
        }
    except Exception as e:
        print(f"❌ 获取闪卡错误: {e}")
        raise HTTPException(status_code=500, detail=str(e))

class FlashcardCreateRequest(BaseModel):
    """创建闪卡请求"""
    front: str
    back: str
    source: str = ""
    tags: List[str] = []

@app.post("/api/flashcards")
async def create_flashcard(request: FlashcardCreateRequest):
    """
    创建闪卡
    """
    try:
        if flashcard_system is None:
            raise HTTPException(status_code=500, detail="闪卡系统未初始化")
        
        card = flashcard_system.create_card(
            request.front,
            request.back,
            request.source,
            request.tags
        )
        
        return {
            "success": True,
            "card": card.to_dict()
        }
    except Exception as e:
        print(f"❌ 创建闪卡错误: {e}")
        raise HTTPException(status_code=500, detail=str(e))

class FlashcardReviewRequest(BaseModel):
    """复习闪卡请求"""
    card_id: str
    quality: int

@app.post("/api/flashcards/review")
async def review_flashcard(request: FlashcardReviewRequest):
    """
    复习闪卡
    """
    try:
        if flashcard_system is None:
            raise HTTPException(status_code=500, detail="闪卡系统未初始化")
        
        flashcard_system.update_card_review(request.card_id, request.quality)
        
        return {
            "success": True,
            "message": "复习记录已更新"
        }
    except Exception as e:
        print(f"❌ 复习闪卡错误: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/flashcards/stats")
async def get_flashcard_stats():
    """
    获取闪卡统计
    """
    try:
        if flashcard_system is None:
            raise HTTPException(status_code=500, detail="闪卡系统未初始化")
        
        stats = flashcard_system.get_statistics()
        
        return {
            "success": True,
            **stats
        }
    except Exception as e:
        print(f"❌ 获取统计错误: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/snippets")
async def get_snippets(session_id: Optional[str] = None):
    """
    获取片段列表
    """
    try:
        if session_id:
            session = session_manager.get_session(session_id)
            if session:
                return {
                    "success": True,
                    "snippets": session.snippets
                }
        
        # 返回所有会话的片段
        all_snippets = []
        for session in session_manager.sessions.values():
            all_snippets.extend(session.snippets)
        
        # 按时间倒序排序
        all_snippets.sort(key=lambda x: x.get('created_at', ''), reverse=True)
        
        return {
            "success": True,
            "snippets": all_snippets
        }
    except Exception as e:
        print(f"❌ 获取片段错误: {e}")
        raise HTTPException(status_code=500, detail=str(e))

class SnippetRequest(BaseModel):
    """片段保存请求"""
    session_id: str
    content: str
    source: str
    tags: List[str] = []

@app.post("/api/snippets")
async def save_snippet(snippet: SnippetRequest):
    """
    保存片段
    """
    try:
        session = session_manager.get_session(snippet.session_id)
        if not session:
            raise HTTPException(status_code=404, detail="会话不存在")
        
        session.add_snippet(snippet.content, snippet.source, snippet.tags)
        session_manager._save_session(session)
        
        return {
            "success": True,
            "message": "片段已保存"
        }
    except Exception as e:
        print(f"❌ 保存片段错误: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/heatmap")
async def get_heatmap():
    """
    获取文档热力图数据
    """
    try:
        # 统计所有会话中的文档引用
        doc_citations = {}
        page_citations = {}
        
        for session in session_manager.sessions.values():
            for msg_idx, citations in session.citations.items():
                for citation in citations:
                    filename = citation.get('filename', '未知')
                    page = citation.get('page', 0)
                    
                    # 统计文档引用次数
                    if filename not in doc_citations:
                        doc_citations[filename] = 0
                    doc_citations[filename] += 1
                    
                    # 统计页面引用次数
                    page_key = f"{filename}:{page}"
                    if page_key not in page_citations:
                        page_citations[page_key] = 0
                    page_citations[page_key] += 1
        
        # 转换为列表格式，按引用次数排序
        top_docs = sorted(
            [{"filename": k, "count": v} for k, v in doc_citations.items()],
            key=lambda x: x['count'],
            reverse=True
        )[:10]  # 取前10
        
        top_pages = sorted(
            [{"location": k, "count": v} for k, v in page_citations.items()],
            key=lambda x: x['count'],
            reverse=True
        )[:20]  # 取前20
        
        return {
            "success": True,
            "heatmap": {
                "top_documents": top_docs,
                "top_pages": top_pages,
                "total_citations": sum(doc_citations.values())
            }
        }
    except Exception as e:
        print(f"❌ 获取热力图错误: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/knowledge-graph")
async def get_knowledge_graph():
    """
    获取知识图谱数据
    """
    try:
        if knowledge_graph is None:
            raise HTTPException(status_code=500, detail="知识图谱未初始化")
        
        return {
            "success": True,
            "entities": knowledge_graph.entities,
            "relationships": knowledge_graph.relationships,
            "stats": knowledge_graph.get_statistics()
        }
    except Exception as e:
        print(f"❌ 获取知识图谱错误: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/knowledge-graph/visualize")
async def visualize_knowledge_graph(max_nodes: int = 50):
    """
    生成知识图谱可视化HTML
    """
    try:
        if knowledge_graph is None:
            raise HTTPException(status_code=500, detail="知识图谱未初始化")
        
        html = knowledge_graph.visualize_graph(max_nodes)
        
        from fastapi.responses import HTMLResponse
        return HTMLResponse(content=html)
    except Exception as e:
        print(f"❌ 可视化知识图谱错误: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/documents")
async def list_documents():
    """
    获取data目录下的所有文档列表
    """
    try:
        from config import DATA_DIR
        
        if not os.path.exists(DATA_DIR):
            return {
                "success": True,
                "documents": []
            }
        
        documents = []
        for filename in os.listdir(DATA_DIR):
            filepath = os.path.join(DATA_DIR, filename)
            if os.path.isfile(filepath):
                ext = os.path.splitext(filename)[1].lower()
                if ext in ['.pdf', '.docx', '.txt', '.md', '.pptx']:
                    file_size = os.path.getsize(filepath) / (1024 * 1024)  # MB
                    documents.append({
                        "filename": filename,
                        "path": filepath,
                        "size": round(file_size, 2),
                        "type": ext[1:]  # 去掉点号
                    })
        
        documents.sort(key=lambda x: x['filename'])
        
        return {
            "success": True,
            "documents": documents,
            "count": len(documents)
        }
    except Exception as e:
        print(f"❌ 获取文档列表错误: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/documents/{filename}")
async def get_document_content(filename: str):
    """
    获取指定文档的内容
    """
    try:
        from config import DATA_DIR
        filepath = os.path.join(DATA_DIR, filename)
        
        if not os.path.exists(filepath):
            raise HTTPException(status_code=404, detail="文件不存在")
        
        # 读取文件内容
        file_ext = os.path.splitext(filename)[1].lower()
        content = ""
        
        if file_ext == '.txt' or file_ext == '.md':
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        
        elif file_ext == '.pdf':
            try:
                import PyPDF2
                with open(filepath, 'rb') as f:
                    pdf_reader = PyPDF2.PdfReader(f)
                    pages_text = []
                    for page_num, page in enumerate(pdf_reader.pages, 1):
                        text = page.extract_text()
                        pages_text.append(f"[第 {page_num} 页]\n{text}")
                    content = "\n\n".join(pages_text)
            except Exception as e:
                content = f"[PDF解析失败: {e}]"
        
        elif file_ext == '.docx':
            try:
                import docx
                doc = docx.Document(filepath)
                paragraphs = [para.text for para in doc.paragraphs if para.text.strip()]
                content = "\n\n".join(paragraphs)
            except Exception as e:
                content = f"[DOCX解析失败: {e}]"
        
        return {
            "success": True,
            "filename": filename,
            "content": content,
            "size": len(content)
        }
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ 获取文档内容错误: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/documents/{filename}/raw")
async def get_document_raw(filename: str):
    """
    获取文档原始文件（支持PDF、图片、TXT等）
    """
    try:
        from config import DATA_DIR
        from fastapi.responses import FileResponse
        
        filepath = os.path.join(DATA_DIR, filename)
        
        if not os.path.exists(filepath):
            raise HTTPException(status_code=404, detail="文件不存在")
        
        file_ext = os.path.splitext(filename)[1].lower()
        
        # 根据文件类型设置MIME类型
        mime_types = {
            '.pdf': 'application/pdf',
            '.txt': 'text/plain; charset=utf-8',
            '.md': 'text/markdown; charset=utf-8',
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.png': 'image/png',
            '.gif': 'image/gif',
            '.webp': 'image/webp',
            '.bmp': 'image/bmp',
            '.svg': 'image/svg+xml',
        }
        
        media_type = mime_types.get(file_ext, 'application/octet-stream')
        
        # 使用URL编码处理中文文件名（RFC 5987）
        from urllib.parse import quote
        encoded_filename = quote(filename)
        
        return FileResponse(
            filepath,
            media_type=media_type,
            headers={
                "Content-Disposition": f"inline; filename*=UTF-8''{encoded_filename}"
                # inline 而不是 attachment，这样浏览器会尝试在线显示
            }
        )
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ 获取文件错误: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/documents/{filename}/preview/docx")
async def preview_docx(filename: str):
    """
    将DOCX转换为HTML预览
    """
    try:
        from config import DATA_DIR
        from fastapi.responses import HTMLResponse
        import mammoth  # 需要安装: pip install mammoth
        
        filepath = os.path.join(DATA_DIR, filename)
        
        if not os.path.exists(filepath):
            raise HTTPException(status_code=404, detail="文件不存在")
        
        file_ext = os.path.splitext(filename)[1].lower()
        if file_ext != '.docx':
            raise HTTPException(status_code=400, detail="只支持DOCX文件")
        
        # 使用mammoth转换DOCX到HTML
        with open(filepath, 'rb') as docx_file:
            result = mammoth.convert_to_html(docx_file)
            html_content = result.value
        
        # 包装成完整的HTML页面
        full_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{filename}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            line-height: 1.6;
            max-width: 900px;
            margin: 0 auto;
            padding: 40px 20px;
            background: #ffffff;
            color: #1f2937;
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: #111827;
            margin-top: 1.5em;
            margin-bottom: 0.5em;
        }}
        p {{
            margin-bottom: 1em;
        }}
        img {{
            max-width: 100%;
            height: auto;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 1em 0;
        }}
        table, th, td {{
            border: 1px solid #d1d5db;
            padding: 8px;
        }}
        th {{
            background-color: #f3f4f6;
        }}
    </style>
</head>
<body>
    <h1 style="border-bottom: 2px solid #e5e7eb; padding-bottom: 10px;">{filename}</h1>
    {html_content}
</body>
</html>
"""
        
        return HTMLResponse(content=full_html)
        
    except ImportError:
        print("❌ mammoth未安装，请运行: pip install mammoth")
        raise HTTPException(status_code=500, detail="DOCX转换功能未启用，请安装mammoth库")
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ DOCX预览错误: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/documents/{filename}/preview/pptx")
async def preview_pptx(filename: str, page: int = 1):
    """
    将PPTX转换为图片预览
    """
    try:
        from config import DATA_DIR
        from pptx import Presentation
        from PIL import Image
        import io
        from fastapi.responses import StreamingResponse
        
        filepath = os.path.join(DATA_DIR, filename)
        
        if not os.path.exists(filepath):
            raise HTTPException(status_code=404, detail="文件不存在")
        
        file_ext = os.path.splitext(filename)[1].lower()
        if file_ext != '.pptx':
            raise HTTPException(status_code=400, detail="只支持PPTX文件")
        
        # 注意：Python-pptx无法直接将幻灯片转为图片
        # 需要使用其他方法，如LibreOffice或pdf2image
        # 这里返回幻灯片的文本内容作为备选方案
        
        prs = Presentation(filepath)
        
        if page < 1 or page > len(prs.slides):
            raise HTTPException(status_code=400, detail="页码超出范围")
        
        slide = prs.slides[page - 1]
        
        # 提取幻灯片文本
        slide_text = []
        for shape in slide.shapes:
            if hasattr(shape, "text"):
                slide_text.append(shape.text)
        
        # 生成HTML预览
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{filename} - 第{page}页</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            max-width: 1000px;
            margin: 0 auto;
            padding: 40px 20px;
            background: #f9fafb;
        }}
        .slide {{
            background: white;
            padding: 60px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            min-height: 400px;
        }}
        .slide-header {{
            text-align: center;
            margin-bottom: 40px;
            padding-bottom: 20px;
            border-bottom: 2px solid #e5e7eb;
        }}
        .slide-content {{
            font-size: 18px;
            line-height: 1.8;
        }}
        .slide-content p {{
            margin: 15px 0;
        }}
        .page-nav {{
            text-align: center;
            margin-top: 30px;
            color: #6b7280;
        }}
    </style>
</head>
<body>
    <div class="slide">
        <div class="slide-header">
            <h2>{filename}</h2>
            <p class="page-nav">第 {page} 页 / 共 {len(prs.slides)} 页</p>
        </div>
        <div class="slide-content">
            {'<p>' + '</p><p>'.join(slide_text) + '</p>' if slide_text else '<p style="color:#9ca3af;">此幻灯片无文本内容</p>'}
        </div>
    </div>
    <div class="page-nav">
        <p>💡 提示：当前显示PPTX的文本内容。完整的图文预览需要安装LibreOffice。</p>
    </div>
</body>
</html>
"""
        
        return HTMLResponse(content=html_content)
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ PPTX预览错误: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/documents/{filename}/search")
async def search_in_document(filename: str, query: str, kb_id: str = 'default'):
    """
    在文档中搜索概念/关键词（支持知识库）
    """
    try:
        from config import get_kb_data_dir
        
        data_dir = get_kb_data_dir(kb_id)
        filepath = os.path.join(data_dir, filename)
        
        if not os.path.exists(filepath):
            raise HTTPException(status_code=404, detail="文件不存在")
        
        file_ext = os.path.splitext(filename)[1].lower()
        results = []
        
        if file_ext == '.pdf':
            # PDF文件搜索（使用pymupdf）
            import fitz
            doc = fitz.open(filepath)
            
            for page_num in range(len(doc)):
                page = doc[page_num]
                text = page.get_text()
                
                # 查找所有匹配项
                if query.lower() in text.lower():
                    # 提取匹配位置的上下文
                    idx = text.lower().find(query.lower())
                    start = max(0, idx - 50)
                    end = min(len(text), idx + len(query) + 50)
                    context = text[start:end].replace('\n', ' ')
                    
                    results.append({
                        "page": page_num + 1,
                        "context": context,
                        "match": query
                    })
            
            doc.close()
        else:
            # 文本文件搜索
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
                
                for line_num, line in enumerate(lines, 1):
                    if query.lower() in line.lower():
                        # 获取上下文
                        start = max(0, line_num - 2)
                        end = min(len(lines), line_num + 2)
                        context = ''.join(lines[start:end])
                        
                        results.append({
                            "line": line_num,
                            "context": context.strip(),
                            "match": query
                        })
        
        return {
            "success": True,
            "query": query,
            "document": filename,
            "results": results[:50],  # 限制返回前50个结果
            "total": len(results)
        }
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ 搜索文档错误: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

async def _llm_filter_concepts(candidates: List[Tuple[str, int]], client, target_count: int = 30) -> List[Tuple[str, int]]:
    """
    使用LLM智能筛选概念
    
    参数:
        candidates: 候选概念列表 [(word, count), ...]
        client: OpenAI客户端
        target_count: 目标返回数量
    
    返回:
        筛选后的概念列表
    """
    try:
        # 准备候选列表
        candidate_list = [f"{word} ({count}次)" for word, count in candidates[:50]]  # 只取前50个给LLM
        candidate_str = "\n".join([f"{i+1}. {c}" for i, c in enumerate(candidate_list)])
        
        prompt = f"""请从以下候选概念中，筛选出最有价值、最有意义的专业术语和概念。

候选概念列表：
{candidate_str}

✅ 必须保留：
- 专业学术术语（如"隐马尔可夫模型"、"卷积神经网络"）
- 核心技术概念（如"深度学习"、"Transformer"）
- 重要算法名称（如"梯度下降"、"反向传播"）
- 专有名词（如"BERT"、"GPT"、"ResNet"）

❌ 必须排除：
- 通用词汇（如"方法"、"系统"、"问题"、"研究"）
- 单字词（如"学"、"习"、"数"、"据"）
- 不完整的词（如"马尔"、"可夫"而不是"隐马尔可夫模型"）
- HTML/LaTeX标记
- 文件格式名
- 纯数字或代码片段

请返回最有价值的 {target_count} 个概念，用JSON格式：
{{
  "selected": ["隐马尔可夫模型", "卷积神经网络", "深度学习", ...]
}}

要求：
- 只返回JSON，不要其他说明
- 概念名称要与候选列表中的完全一致（不包括次数）
- 优先选择完整的、长的专业术语
- 按重要性和专业度排序
"""
        
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "你是一位知识管理专家，擅长识别有价值的专业概念。"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=1000
        )
        
        result_text = response.choices[0].message.content.strip()
        
        # 提取JSON
        if '```json' in result_text:
            result_text = result_text.split('```json')[1].split('```')[0].strip()
        elif '```' in result_text:
            result_text = result_text.split('```')[1].split('```')[0].strip()
        
        import json
        data = json.loads(result_text)
        selected_names = data.get('selected', [])
        
        print(f"✅ LLM筛选: {len(candidates)} → {len(selected_names)} 个概念")
        
        # 根据LLM选择的概念，从原始列表中提取（保留count信息）
        candidates_dict = {word: count for word, count in candidates}
        filtered = []
        for name in selected_names:
            if name in candidates_dict:
                filtered.append((name, candidates_dict[name]))
        
        # 如果LLM返回的太少，补充一些高频词
        if len(filtered) < target_count // 2:
            print(f"⚠️  LLM返回数量不足，补充高频词")
            for word, count in candidates:
                if word not in [w for w, _ in filtered]:
                    filtered.append((word, count))
                    if len(filtered) >= target_count:
                        break
        
        return filtered
        
    except Exception as e:
        print(f"⚠️  LLM筛选失败: {e}，返回原始列表")
        import traceback
        traceback.print_exc()
        return candidates  # 失败时返回原始列表

@app.get("/api/concepts/hot")
async def get_hot_concepts(kb_id: str = 'default', limit: int = 10):
    """
    获取热门概念（基于向量库中的高频词）
    """
    try:
        # 从向量库中提取高频概念
        if rag_agent and hasattr(rag_agent, 'vector_store'):
            collection = rag_agent.vector_store.collection
            
            # 获取所有文档的内容
            results = collection.get(limit=1000, include=['documents'])
            
            if not results or not results.get('documents'):
                return {
                    "success": True,
                    "concepts": []
                }
            
            # 简单的关键词提取：统计高频词
            from collections import Counter
            import re
            
            all_text = ' '.join(results['documents'])
            # 提取中文词（2-8个字，允许更长的专业术语如"隐马尔可夫模型"）和英文词（3+字母）
            chinese_words = re.findall(r'[\u4e00-\u9fa5]{2,8}', all_text)
            english_words = re.findall(r'\b[A-Za-z]{3,}\b', all_text)
            
            # 统计词频
            word_counts = Counter(chinese_words + english_words)
            
            # 扩展的停用词列表（包括文档处理相关词）
            stopwords = {
                # 中文停用词
                '这个', '那个', '可以', '已经', '没有', '什么', '怎么', '现在', '因为', '所以', 
                '但是', '如果', '虽然', '然而', '一个', '不是', '就是', '还是', '或者', '而且',
                '因此', '所以', '于是', '其中', '之间', '通过', '根据', '关于', '我们', '他们',
                '进行', '实现', '主要', '重要', '不同', '各种', '许多', '一些', '这些', '那些',
                '具有', '包括', '使用', '需要', '应该', '能够', '可能', '以及', '或者', '还有',
                
                # 英文停用词
                'the', 'and', 'for', 'that', 'with', 'from', 'this', 'are', 'was', 'were',
                'been', 'have', 'has', 'had', 'will', 'would', 'can', 'could', 'may', 'might',
                'should', 'must', 'shall', 'there', 'their', 'they', 'them', 'these', 'those',
                'what', 'which', 'who', 'when', 'where', 'why', 'how', 'all', 'each', 'every',
                'some', 'any', 'many', 'much', 'more', 'most', 'other', 'such', 'than', 'then',
                'very', 'only', 'just', 'about', 'into', 'over', 'after', 'before', 'during',
                
                # 文档处理相关词（关键！）
                'table', 'figure', 'page', 'section', 'chapter', 'content', 'image', 'text',
                'document', 'file', 'data', 'information', 'result', 'results', 'example',
                'examples', 'note', 'notes', 'reference', 'references', 'appendix', 'index',
                'list', 'item', 'items', 'number', 'numbers', 'value', 'values', 'type', 'types',
                'name', 'names', 'description', 'descriptions', 'summary', 'conclusion',
                'introduction', 'abstract', 'title', 'author', 'date', 'source', 'link',
                
                # HTML/CSS/编程相关词
                'span', 'div', 'class', 'style', 'font', 'color', 'width', 'height', 'size',
                'html', 'body', 'head', 'meta', 'script', 'code', 'function', 'return',
                'var', 'const', 'let', 'array', 'object', 'string', 'boolean', 'null',
                'undefined', 'none', 'true', 'false', 'void', 'break', 'continue', 'else',
                
                # HTML表格属性
                'colspan', 'rowspan', 'cellpadding', 'cellspacing', 'thead', 'tbody', 'tfoot',
                'colgroup', 'valign', 'halign', 'nowrap',
                
                # 图片和媒体格式
                'jpg', 'jpeg', 'png', 'gif', 'bmp', 'svg', 'webp', 'ico', 'tiff',
                'mp3', 'mp4', 'avi', 'mov', 'wmv', 'flv', 'wav', 'pdf', 'doc', 'docx',
                'images', 'image', 'img', 'pic', 'picture', 'photo', 'media', 'video', 'audio',
                
                # LaTeX数学命令
                'mathbb', 'mathbf', 'mathit', 'mathrm', 'mathcal', 'mathfrak', 'mathsf',
                'mathtt', 'frac', 'sqrt', 'sum', 'int', 'prod', 'lim', 'infty', 'partial',
                'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'theta', 'lambda', 'sigma',
                'begin', 'end', 'left', 'right', 'cdot', 'times', 'equiv', 'approx',
                
                # 词性标注词（来自NLP处理）
                'noun', 'verb', 'adj', 'adv', 'prep', 'conj', 'pron', 'det', 'num',
                'NN', 'VB', 'JJ', 'RB', 'IN', 'DT', 'PRP', 'CC', 'CD',
                
                # 格式标记词
                'bold', 'italic', 'underline', 'normal', 'left', 'right', 'center',
                'align', 'margin', 'padding', 'border', 'background', 'line', 'space',
                
                # 中文文档处理词
                '图表', '表格', '图片', '页面', '章节', '内容', '文档', '文件', '数据', '信息',
                '结果', '示例', '注释', '参考', '附录', '索引', '列表', '项目', '数字', '数值',
                '类型', '名称', '描述', '摘要', '结论', '引言', '标题', '作者', '日期', '来源',
                
                # 中文常见无意义词
                '东西', '方面', '情况', '问题', '时候', '地方', '方法', '系统', '部分', '过程',
                '方式', '状态', '位置', '作用', '功能', '特点', '性质', '关系', '形式', '意义'
            }
            
            # 过滤：1.停用词 2.纯数字 3.太短的词 4.出现次数太少
            filtered_words = []
            for word, count in word_counts.most_common(200):
                # 转换为小写进行判断
                word_lower = word.lower()
                
                # 跳过条件
                if (word_lower in stopwords or  # 停用词
                    word.isdigit() or  # 纯数字
                    len(word) < 2 or  # 太短
                    count < 3 or  # 出现次数太少
                    word.startswith('http') or  # URL
                    word.startswith('www')):  # 网址
                    continue
                
                filtered_words.append((word, count))
                
                if len(filtered_words) >= 100:
                    break
            
            # 使用LLM进行智能筛选（可选，提升质量）
            use_llm_filter = True  # 可配置开关
            if use_llm_filter and filtered_words and rag_agent:
                print(f"🤖 使用LLM智能筛选概念（候选：{len(filtered_words)}个）...")
                filtered_words = await _llm_filter_concepts(filtered_words, rag_agent.client, limit * 3)
            
            # 转换为概念格式
            concepts = []
            for word, count in filtered_words[:limit]:
                concepts.append({
                    "name": word,
                    "count": count,
                    "relevance": min(1.0, count / max(filtered_words[0][1], 1))
                })
            
            return {
                "success": True,
                "concepts": concepts
            }
        
        return {
            "success": True,
            "concepts": []
        }
        
    except Exception as e:
        print(f"❌ 获取热门概念错误: {e}")
        import traceback
        traceback.print_exc()
        return {
            "success": False,
            "concepts": []
        }

@app.get("/api/concepts/search")
async def search_concepts(q: str, kb_id: str = 'default', limit: int = 20):
    """
    搜索概念（在所有文档中搜索关键词）
    """
    try:
        from config import get_kb_data_dir
        
        if not q or len(q.strip()) == 0:
            return {
                "success": False,
                "results": [],
                "message": "搜索词为空"
            }
        
        data_dir = get_kb_data_dir(kb_id)
        
        if not os.path.exists(data_dir):
            return {
                "success": False,
                "results": [],
                "message": "知识库不存在"
            }
        
        # 遍历知识库中的所有文档
        all_results = []
        
        for filename in os.listdir(data_dir):
            filepath = os.path.join(data_dir, filename)
            
            if not os.path.isfile(filepath):
                continue
            
            file_ext = os.path.splitext(filename)[1].lower()
            
            try:
                if file_ext == '.pdf':
                    # PDF文件搜索
                    import fitz
                    doc = fitz.open(filepath)
                    
                    for page_num in range(len(doc)):
                        page = doc[page_num]
                        text = page.get_text()
                        
                        # 查找匹配
                        if q.lower() in text.lower():
                            # 提取上下文
                            idx = text.lower().find(q.lower())
                            start = max(0, idx - 50)
                            end = min(len(text), idx + len(q) + 50)
                            context = text[start:end].replace('\n', ' ')
                            
                            all_results.append({
                                "filename": filename,
                                "page": page_num + 1,
                                "context": context,
                                "relevance": 0.8,
                                "isPDF": True
                            })
                            
                            if len(all_results) >= limit:
                                break
                    
                    doc.close()
                    
                elif file_ext in ['.txt', '.md']:
                    # 文本文件搜索
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        lines = f.readlines()
                    
                    for line_num, line in enumerate(lines, 1):
                        if q.lower() in line.lower():
                            all_results.append({
                                "filename": filename,
                                "line": line_num,
                                "context": line.strip(),
                                "relevance": 0.8,
                                "isPDF": False
                            })
                            
                            if len(all_results) >= limit:
                                break
                
                if len(all_results) >= limit:
                    break
                    
            except Exception as file_error:
                print(f"搜索文件 {filename} 时出错: {file_error}")
                continue
        
        return {
            "success": True,
            "query": q,
            "results": all_results[:limit],
            "total": len(all_results)
        }
        
    except Exception as e:
        print(f"❌ 概念搜索错误: {e}")
        import traceback
        traceback.print_exc()
        return {
            "success": False,
            "results": [],
            "message": str(e)
        }

@app.get("/api/documents/{filename}/outline")
async def get_document_outline(filename: str):
    """
    获取PDF文档大纲
    """
    try:
        from config import DATA_DIR
        import PyPDF2
        
        filepath = os.path.join(DATA_DIR, filename)
        
        if not os.path.exists(filepath):
            raise HTTPException(status_code=404, detail="文件不存在")
        
        file_ext = os.path.splitext(filename)[1].lower()
        
        if file_ext != '.pdf':
            # 非PDF文件，返回简单的文本大纲
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            lines = content.split('\n')
            sections = []
            for i, line in enumerate(lines):
                trimmed = line.strip()
                if trimmed.startswith('#') or (len(trimmed) > 5 and len(trimmed) < 100 and trimmed[0].isupper()):
                    sections.append({
                        "id": f"section-{i}",
                        "title": trimmed.replace('#', '').strip(),
                        "level": 1,
                        "page": i // 50 + 1  # 估算页码
                    })
            
            return {
                "success": True,
                "outline": {
                    "document": filename,
                    "sections": sections
                }
            }
        
        # PDF文件，提取实际大纲
        with open(filepath, 'rb') as f:
            pdf_reader = PyPDF2.PdfReader(f)
            num_pages = len(pdf_reader.pages)
            
            # 尝试获取PDF目录
            outlines = []
            if hasattr(pdf_reader, 'outline') and pdf_reader.outline:
                def extract_outlines(items, level=1):
                    result = []
                    for item in items:
                        if isinstance(item, list):
                            result.extend(extract_outlines(item, level + 1))
                        else:
                            try:
                                title = item.get('/Title', 'Untitled')
                                # 获取页码
                                if hasattr(item, 'page'):
                                    page_num = pdf_reader.pages.index(item.page) + 1
                                else:
                                    page_num = 1
                                
                                result.append({
                                    "id": f"outline-{len(result)}",
                                    "title": title,
                                    "level": level,
                                    "page": page_num
                                })
                            except:
                                pass
                    return result
                
                outlines = extract_outlines(pdf_reader.outline)
            
            # 如果没有目录，创建基于页数的简单大纲
            if not outlines:
                for i in range(1, num_pages + 1):
                    if i == 1 or i % 10 == 0:  # 每10页一个章节
                        outlines.append({
                            "id": f"page-{i}",
                            "title": f"第 {i} 页",
                            "level": 1,
                            "page": i
                        })
            
            return {
                "success": True,
                "outline": {
                    "document": filename,
                    "total_pages": num_pages,
                    "sections": outlines
                }
            }
            
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ 获取文档大纲错误: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

class KnowledgeGraphExtractRequest(BaseModel):
    """知识提取请求"""
    text: str
    source: str = ""

@app.post("/api/knowledge-graph/extract")
async def extract_knowledge(request: KnowledgeGraphExtractRequest):
    """
    从文本提取知识
    """
    try:
        if knowledge_graph is None:
            raise HTTPException(status_code=500, detail="知识图谱未初始化")
        
        num_entities, num_relations = knowledge_graph.add_entities_and_relations(
            request.text,
            request.source
        )
        
        return {
            "success": True,
            "entities_added": num_entities,
            "relations_added": num_relations
        }
    except Exception as e:
        print(f"❌ 提取知识错误: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# ============================================================
# 知识库管理 API
# ============================================================

@app.get("/api/knowledge-bases")
async def list_knowledge_bases():
    """
    获取所有知识库列表
    """
    try:
        from config import VECTOR_DB_DIR
        
        knowledge_bases = []
        
        # 扫描vector_db/下的所有子目录
        if os.path.exists(VECTOR_DB_DIR):
            for kb_name in os.listdir(VECTOR_DB_DIR):
                kb_vector_path = os.path.join(VECTOR_DB_DIR, kb_name)
                
                if os.path.isdir(kb_vector_path):
                    db_file = os.path.join(kb_vector_path, "chroma.sqlite3")
                    
                    # 计算大小
                    size = 0
                    if os.path.exists(db_file):
                        size = os.path.getsize(db_file) / (1024 * 1024)
                        created_at = os.path.getctime(db_file)
                    else:
                        # 新建的空知识库
                        created_at = os.path.getctime(kb_vector_path)
                    
                    # ✅ 计算文档数量
                    data_dir = get_kb_data_dir(kb_name)
                    document_count = 0
                    if os.path.exists(data_dir):
                        # 统计data目录下的原始文件数（不包括.json和.md缓存文件）
                        import glob
                        for ext in ['*.pdf', '*.docx', '*.pptx', '*.txt']:
                            document_count += len(glob.glob(os.path.join(data_dir, ext)))
                    
                    # ✅ 判断是否为当前使用的知识库
                    # 检查rag_agent的向量库路径是否匹配
                    is_current_kb = False
                    if rag_agent and hasattr(rag_agent, 'vector_store'):
                        current_path = str(rag_agent.vector_store.db_path)
                        is_current_kb = kb_vector_path in current_path or current_path in kb_vector_path
                    
                    knowledge_bases.append({
                        "id": kb_name,
                        "name": f"{kb_name}知识库" if kb_name == "default" else kb_name,
                        "path": kb_vector_path,
                        "size": round(size, 2),
                        "document_count": document_count,  # ✅ 添加文档数量
                        "is_current": is_current_kb,  # ✅ 基于实际使用的知识库
                        "created_at": created_at
                    })
        
        # 按名称排序，default排在最前面
        knowledge_bases.sort(key=lambda x: (x['id'] != 'default', x['id']))
        
        return {
            "success": True,
            "knowledge_bases": knowledge_bases,
            "count": len(knowledge_bases)
        }
    except Exception as e:
        print(f"❌ 获取知识库列表错误: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

class CreateKBRequest(BaseModel):
    """创建知识库请求"""
    name: str
    files: List[str] = []  # 文件路径列表

@app.post("/api/knowledge-bases")
async def create_knowledge_base(request: CreateKBRequest):
    """
    创建新知识库
    """
    try:
        from src.processors.document_loader import DocumentLoader
        from src.processors.text_splitter import TextSplitter
        from src.core.vector_store import VectorStore
        from src.core.image_vector_store import ImageVectorStore
        from config import ensure_kb_dirs, get_kb_data_dir, get_kb_vector_dir
        
        # 检查知识库是否已存在
        kb_data_dir = get_kb_data_dir(request.name)
        kb_vector_dir = get_kb_vector_dir(request.name)
        
        if os.path.exists(kb_data_dir) or os.path.exists(kb_vector_dir):
            raise HTTPException(status_code=400, detail="知识库已存在")
        
        print(f"📦 创建知识库: {request.name}")
        
        # 创建目录
        data_dir, vector_dir = ensure_kb_dirs(request.name)
        print(f"   数据目录: {data_dir}")
        print(f"   向量库目录: {vector_dir}")
        
        # 创建向量存储（初始化数据库）
        text_vector_store = VectorStore(db_path=vector_dir)
        image_vector_store = ImageVectorStore(db_path=vector_dir)
        
        return {
            "success": True,
            "message": f"知识库 '{request.name}' 创建成功",
            "kb_id": request.name,
            "data_path": data_dir,
            "vector_path": vector_dir
        }
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ 创建知识库错误: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/knowledge-bases/{kb_id}/switch")
async def switch_knowledge_base(kb_id: str):
    """
    切换到指定知识库
    """
    try:
        global rag_agent
        from config import get_kb_vector_dir
        
        # 使用新的目录结构：vector_db/{kb_id}/
        kb_vector_path = get_kb_vector_dir(kb_id)
        
        # 检查向量库目录是否存在
        if not os.path.exists(kb_vector_path):
            print(f"❌ 知识库路径不存在: {kb_vector_path}")
            raise HTTPException(status_code=404, detail=f"知识库不存在: {kb_id}")
        
        print(f"🔄 切换到知识库: {kb_id}")
        print(f"   向量库路径: {kb_vector_path}")
        
        # TODO: 重新初始化RAG Agent以使用新的向量库
        # 这需要修改RAGAgent支持动态切换
        # 暂时返回成功
        
        return {
            "success": True,
            "message": f"已切换到知识库: {kb_id}",
            "kb_id": kb_id,
            "vector_path": kb_vector_path
        }
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ 切换知识库错误: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/knowledge-bases/{kb_id}")
async def delete_knowledge_base(kb_id: str):
    """
    删除指定知识库（同时删除数据和向量库）
    """
    try:
        if kb_id == "default":
            raise HTTPException(status_code=400, detail="不能删除默认知识库")
        
        from config import get_kb_data_dir, get_kb_vector_dir
        
        kb_data_dir = get_kb_data_dir(kb_id)
        kb_vector_dir = get_kb_vector_dir(kb_id)
        
        if not os.path.exists(kb_data_dir) and not os.path.exists(kb_vector_dir):
            raise HTTPException(status_code=404, detail="知识库不存在")
        
        print(f"🗑️  删除知识库: {kb_id}")
        
        import shutil
        
        # 删除数据目录
        if os.path.exists(kb_data_dir):
            shutil.rmtree(kb_data_dir)
            print(f"   ✅ 已删除数据目录: {kb_data_dir}")
        
        # 删除向量库目录
        if os.path.exists(kb_vector_dir):
            shutil.rmtree(kb_vector_dir)
            print(f"   ✅ 已删除向量库目录: {kb_vector_dir}")
        
        return {
            "success": True,
            "message": f"知识库 '{kb_id}' 已删除"
        }
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ 删除知识库错误: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/knowledge-bases/{kb_id}/files")
async def list_kb_files(kb_id: str):
    """
    获取指定知识库的文件列表
    """
    try:
        from config import get_kb_data_dir
        import glob
        
        data_dir = get_kb_data_dir(kb_id)
        
        if not os.path.exists(data_dir):
            return {
                "success": True,
                "kb_id": kb_id,
                "files": [],
                "count": 0
            }
        
        files = []
        for filepath in glob.glob(os.path.join(data_dir, "*")):
            if os.path.isfile(filepath):
                filename = os.path.basename(filepath)
                file_size = os.path.getsize(filepath) / (1024 * 1024)  # MB
                file_ext = os.path.splitext(filename)[1].lower()
                
                files.append({
                    "name": filename,
                    "size": round(file_size, 2),
                    "type": file_ext[1:] if file_ext else "unknown",
                    "path": filepath,
                    "created_at": os.path.getctime(filepath)
                })
        
        # 按创建时间倒序
        files.sort(key=lambda x: x['created_at'], reverse=True)
        
        return {
            "success": True,
            "kb_id": kb_id,
            "files": files,
            "count": len(files)
        }
        
    except Exception as e:
        print(f"❌ 获取文件列表错误: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/knowledge-bases/{kb_id}/documents/{filename}/outline")
async def get_kb_document_outline(kb_id: str, filename: str):
    """
    获取指定知识库中文档的大纲
    """
    try:
        from config import get_kb_data_dir
        import PyPDF2
        
        data_dir = get_kb_data_dir(kb_id)
        filepath = os.path.join(data_dir, filename)
        
        if not os.path.exists(filepath):
            raise HTTPException(status_code=404, detail="文件不存在")
        
        file_ext = os.path.splitext(filename)[1].lower()
        
        if file_ext != '.pdf':
            # 非PDF文件，返回简单的文本大纲
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            lines = content.split('\n')
            sections = []
            section_id = 0
            for i, line in enumerate(lines[:200]):  # 只处理前200行
                trimmed = line.strip()
                # 检测标题：以#开头，或长度适中且首字母大写
                if (trimmed.startswith('#') and len(trimmed) < 100) or \
                   (5 < len(trimmed) < 80 and trimmed[0].isupper() and not trimmed.endswith((',', '.', '!', '?'))):
                    sections.append({
                        "id": f"section-{section_id}",
                        "title": trimmed.replace('#', '').strip(),
                        "level": trimmed.count('#') if trimmed.startswith('#') else 1,
                        "line": i,
                        "subsections": []
                    })
                    section_id += 1
            
            return {
                "success": True,
                "outline": {
                    "document": filename,
                    "sections": sections[:50]  # 最多返回50个章节
                }
            }
        
        # PDF文件，使用pymupdf提取大纲（更强大）
        import fitz  # pymupdf
        doc = fitz.open(filepath)
        num_pages = doc.page_count
        
        # 获取PDF目录
        toc = doc.get_toc()  # 返回 [level, title, page]
        outlines = []
        
        if toc:
            for i, (level, title, page) in enumerate(toc):
                outlines.append({
                    "id": f"outline-{i}",
                    "title": title,
                    "level": level,
                    "page": page,
                    "subsections": []
                })
        
        # 如果没有目录，使用基于字体和格式的智能提取
        if not toc:
            print(f"📖 PDF无内置目录，使用智能提取...")
            outlines = extract_headings_from_pdf(doc)
            
        doc.close()
        
        # 如果智能提取也失败，使用简单的页码大纲
        if not outlines:
            print(f"📖 智能提取失败，使用页码大纲...")
            for i in range(1, num_pages + 1):
                if i == 1 or i % 10 == 0:  # 每10页一个章节
                    outlines.append({
                        "id": f"page-{i}",
                        "title": f"第 {i} 页",
                        "level": 1,
                        "page": i,
                        "subsections": []
                    })
        
        return {
            "success": True,
            "outline": {
                "document": filename,
                "total_pages": num_pages,
                "sections": outlines
            }
        }
            
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ 获取文档大纲错误: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/knowledge-bases/{kb_id}/documents/{filename}/raw")
async def get_kb_document_raw(kb_id: str, filename: str):
    """
    获取指定知识库中的文档原始文件
    """
    try:
        from config import get_kb_data_dir
        from fastapi.responses import FileResponse
        
        data_dir = get_kb_data_dir(kb_id)
        filepath = os.path.join(data_dir, filename)
        
        if not os.path.exists(filepath):
            raise HTTPException(status_code=404, detail="文件不存在")
        
        file_ext = os.path.splitext(filename)[1].lower()
        
        # 根据文件类型设置MIME类型
        mime_types = {
            '.pdf': 'application/pdf',
            '.txt': 'text/plain; charset=utf-8',
            '.md': 'text/markdown; charset=utf-8',
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.png': 'image/png',
            '.gif': 'image/gif',
            '.webp': 'image/webp',
            '.bmp': 'image/bmp',
            '.svg': 'image/svg+xml',
        }
        
        media_type = mime_types.get(file_ext, 'application/octet-stream')
        
        # 使用URL编码处理中文文件名（RFC 5987）
        from urllib.parse import quote
        encoded_filename = quote(filename)
        
        return FileResponse(
            filepath,
            media_type=media_type,
            headers={
                "Content-Disposition": f"inline; filename*=UTF-8''{encoded_filename}"
            }
        )
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ 获取文件错误: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/knowledge-bases/{kb_id}/documents/{filename}/preview/docx")
async def preview_kb_docx(kb_id: str, filename: str):
    """
    将指定知识库的DOCX转换为HTML预览
    """
    try:
        from config import get_kb_data_dir
        from fastapi.responses import HTMLResponse
        
        data_dir = get_kb_data_dir(kb_id)
        filepath = os.path.join(data_dir, filename)
        
        if not os.path.exists(filepath):
            raise HTTPException(status_code=404, detail="文件不存在")
        
        try:
            import mammoth
        except ImportError:
            raise HTTPException(
                status_code=500, 
                detail="DOCX转换功能未启用，请安装mammoth库: pip install mammoth"
            )
        
        file_ext = os.path.splitext(filename)[1].lower()
        if file_ext != '.docx':
            raise HTTPException(status_code=400, detail="只支持DOCX文件")
        
        with open(filepath, 'rb') as docx_file:
            result = mammoth.convert_to_html(docx_file)
            html_content = result.value
        
        full_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{filename}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            line-height: 1.6;
            max-width: 900px;
            margin: 0 auto;
            padding: 40px 20px;
            background: #ffffff;
            color: #1f2937;
        }}
        h1, h2, h3, h4, h5, h6 {{ color: #111827; margin-top: 1.5em; margin-bottom: 0.5em; }}
        p {{ margin-bottom: 1em; }}
        img {{ max-width: 100%; height: auto; }}
        table {{ border-collapse: collapse; width: 100%; margin: 1em 0; }}
        table, th, td {{ border: 1px solid #d1d5db; padding: 8px; }}
        th {{ background-color: #f3f4f6; }}
    </style>
</head>
<body>
    <h1 style="border-bottom: 2px solid #e5e7eb; padding-bottom: 10px;">{filename}</h1>
    {html_content}
</body>
</html>
"""
        return HTMLResponse(content=full_html)
        
    except ImportError:
        raise
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ DOCX预览错误: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/knowledge-bases/{kb_id}/documents/{filename}/preview/pptx")
async def preview_kb_pptx(kb_id: str, filename: str, page: int = 1):
    """
    显示指定知识库的PPTX文本内容
    """
    try:
        from config import get_kb_data_dir
        from fastapi.responses import HTMLResponse
        from pptx import Presentation
        
        data_dir = get_kb_data_dir(kb_id)
        filepath = os.path.join(data_dir, filename)
        
        if not os.path.exists(filepath):
            raise HTTPException(status_code=404, detail="文件不存在")
        
        file_ext = os.path.splitext(filename)[1].lower()
        if file_ext != '.pptx':
            raise HTTPException(status_code=400, detail="只支持PPTX文件")
        
        prs = Presentation(filepath)
        
        if page < 1 or page > len(prs.slides):
            raise HTTPException(status_code=400, detail="页码超出范围")
        
        slide = prs.slides[page - 1]
        slide_text = []
        for shape in slide.shapes:
            if hasattr(shape, "text"):
                slide_text.append(shape.text)
        
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{filename} - 第{page}页</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            max-width: 1000px;
            margin: 0 auto;
            padding: 40px 20px;
            background: #f9fafb;
        }}
        .slide {{
            background: white;
            padding: 60px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            min-height: 400px;
        }}
        .slide-header {{
            text-align: center;
            margin-bottom: 40px;
            padding-bottom: 20px;
            border-bottom: 2px solid #e5e7eb;
        }}
        .slide-content {{
            font-size: 18px;
            line-height: 1.8;
        }}
        .slide-content p {{ margin: 15px 0; }}
        .page-nav {{
            text-align: center;
            margin-top: 30px;
            color: #6b7280;
        }}
    </style>
</head>
<body>
    <div class="slide">
        <div class="slide-header">
            <h2>{filename}</h2>
            <p class="page-nav">第 {page} 页 / 共 {len(prs.slides)} 页</p>
        </div>
        <div class="slide-content">
            {'<p>' + '</p><p>'.join(slide_text) + '</p>' if slide_text else '<p style="color:#9ca3af;">此幻灯片无文本内容</p>'}
        </div>
    </div>
</body>
</html>
"""
        return HTMLResponse(content=html_content)
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ PPTX预览错误: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/knowledge-bases/{kb_id}/files/{filename}")
async def delete_kb_file(kb_id: str, filename: str):
    """
    删除指定知识库中的文件（原文件+向量记录）
    """
    try:
        from config import get_kb_data_dir, get_kb_vector_dir
        from vector_store import VectorStore
        
        # 1. 删除原文件
        data_dir = get_kb_data_dir(kb_id)
        file_path = os.path.join(data_dir, filename)
        
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail="文件不存在")
        
        os.remove(file_path)
        print(f"✅ 删除原文件: {file_path}")
        
        # 2. 删除向量记录
        vector_dir = get_kb_vector_dir(kb_id)
        
        try:
            vector_store = VectorStore(db_path=vector_dir)
            
            # 尝试根据filename删除向量记录
            # 注意：需要查询collection中filename匹配的所有记录
            collection = vector_store.collection
            
            # 使用where查询匹配filename的记录
            results = collection.get(
                where={"filename": filename}
            )
            
            if results and results['ids']:
                # 删除找到的所有记录
                collection.delete(ids=results['ids'])
                deleted_count = len(results['ids'])
                print(f"✅ 删除向量记录: {deleted_count} 条")
            else:
                print(f"⚠️  未找到文件 {filename} 的向量记录")
                deleted_count = 0
                
        except Exception as e:
            print(f"⚠️  删除向量记录失败: {e}")
            deleted_count = 0
        
        return {
            "success": True,
            "message": f"文件 '{filename}' 已删除",
            "kb_id": kb_id,
            "filename": filename,
            "vector_records_deleted": deleted_count
        }
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ 删除文件错误: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/knowledge-bases/{kb_id}/upload")
async def upload_to_knowledge_base(kb_id: str, files: List[UploadFile] = File(...)):
    """
    上传文件到指定知识库并处理
    """
    try:
        from src.processors.document_loader import DocumentLoader
        from src.processors.text_splitter import TextSplitter
        from src.core.vector_store import VectorStore
        from src.core.image_vector_store import ImageVectorStore
        import tempfile
        import shutil
        
        print(f"📤 上传文件到知识库: {kb_id}")
        print(f"   文件数量: {len(files)}")
        
        # 使用新的路径结构：data/{kb_id}/ 和 vector_db/{kb_id}/
        from config import get_kb_data_dir, get_kb_vector_dir, ensure_kb_dirs
        
        # 确保知识库目录存在（如果不存在会自动创建）
        kb_data_dir, kb_vector_dir = ensure_kb_dirs(kb_id)
        print(f"   数据目录: {kb_data_dir}")
        print(f"   向量库目录: {kb_vector_dir}")
        
        # 创建临时目录保存上传的文件（用于处理）
        temp_dir = tempfile.mkdtemp()
        saved_files = []
        permanent_files = []  # 保存到data的文件列表
        
        try:
            # 初始化DocumentLoader用于转换
            loader = DocumentLoader(data_dir=temp_dir)
            
            for file in files:
                print(f"\n   📄 处理文件: {file.filename}")
                
                # 保存到临时目录
                temp_path = os.path.join(temp_dir, file.filename)
                content = await file.read()
                
                with open(temp_path, 'wb') as f:
                    f.write(content)
                
                # 检查文件类型
                file_ext = os.path.splitext(file.filename)[1].lower()
                base_name = os.path.splitext(file.filename)[0]
                
                # 如果是PPTX或DOCX，转换为PDF后再保存
                if file_ext in ['.pptx', '.docx']:
                    print(f"      检测到 {file_ext.upper()} 文件，转换为PDF...")
                    
                    # 转换为PDF
                    pdf_path = loader.convert_to_pdf(temp_path)
                    
                    if pdf_path and os.path.exists(pdf_path):
                        # 转换成功，保存PDF
                        final_filename = f"{base_name}.pdf"
                        permanent_path = os.path.join(kb_data_dir, final_filename)
                        
                        # 如果文件已存在，添加时间戳
                        if os.path.exists(permanent_path):
                            import time
                            timestamp = int(time.time())
                            final_filename = f"{base_name}_{timestamp}.pdf"
                            permanent_path = os.path.join(kb_data_dir, final_filename)
                            print(f"      ⚠️  PDF已存在，重命名为: {final_filename}")
                        
                        # 复制转换后的PDF到data目录
                        shutil.copy2(pdf_path, permanent_path)
                        
                        # 也更新临时目录中的文件（用于向量化）
                        temp_pdf = os.path.join(temp_dir, final_filename)
                        shutil.copy2(pdf_path, temp_pdf)
                        saved_files.append(temp_pdf)
                        
                        # 删除临时目录中的原始PPTX/DOCX文件（避免重复处理）
                        if os.path.exists(temp_path):
                            os.remove(temp_path)
                            print(f"      🗑️  已删除临时目录中的原始文件")
                        
                        permanent_files.append(permanent_path)
                        print(f"      ✅ 已转换并保存为: {final_filename}")
                        print(f"         永久路径: {permanent_path}")
                    else:
                        # 转换失败，保存原文件
                        print(f"      ⚠️  转换失败，保存原始 {file_ext.upper()} 文件")
                        permanent_path = os.path.join(kb_data_dir, file.filename)
                        
                        if os.path.exists(permanent_path):
                            import time
                            timestamp = int(time.time())
                            new_filename = f"{base_name}_{timestamp}{file_ext}"
                            permanent_path = os.path.join(kb_data_dir, new_filename)
                            print(f"      ⚠️  文件已存在，重命名为: {new_filename}")
                        
                        with open(permanent_path, 'wb') as f:
                            f.write(content)
                        saved_files.append(temp_path)
                        permanent_files.append(permanent_path)
                        print(f"      ✅ 保存原文件: {os.path.basename(permanent_path)}")
                else:
                    # 其他类型文件（PDF、TXT、MD、图片）直接保存
                    saved_files.append(temp_path)
                    
                    permanent_path = os.path.join(kb_data_dir, file.filename)
                    
                    # 如果文件已存在，添加时间戳
                    if os.path.exists(permanent_path):
                        import time
                        timestamp = int(time.time())
                        new_filename = f"{base_name}_{timestamp}{file_ext}"
                        permanent_path = os.path.join(kb_data_dir, new_filename)
                        print(f"      ⚠️  文件已存在，重命名为: {new_filename}")
                    
                    with open(permanent_path, 'wb') as f:
                        f.write(content)
                    permanent_files.append(permanent_path)
                    print(f"      ✅ 保存: {os.path.basename(permanent_path)}")
            
            print(f"\n   🔄 开始向量化处理...")
            # 处理文件（从临时目录加载，包含转换后的PDF）
            splitter = TextSplitter(chunk_size=500, chunk_overlap=100)
            # 使用正确的向量库路径
            text_vector_store = VectorStore(db_path=kb_vector_dir)
            image_vector_store = ImageVectorStore(db_path=kb_vector_dir)
            
            documents, images = loader.load_all_documents()
            
            if documents:
                chunks = splitter.split_documents(documents)
                text_vector_store.add_documents(chunks)
                print(f"   ✅ 添加了 {len(chunks)} 个文本块")
            
            if images:
                image_vector_store.add_images(images)
                print(f"   ✅ 添加了 {len(images)} 张图片")
            
            # 提取知识图谱
            print(f"\n   🧠 提取知识图谱...")
            entities_count = 0
            relations_count = 0
            if documents and knowledge_graph:
                for doc in documents[:3]:  # 只处理前3个文档以节省时间
                    try:
                        text = doc.get('content', '')[:2000]  # 限制文本长度
                        if len(text) > 100:
                            entities, relations = knowledge_graph.extract_entities_and_relations(
                                text, 
                                source=doc.get('filename', 'unknown'),
                                use_simple=True  # 使用简单快速的关键词提取
                            )
                            # 添加到知识图谱
                            if entities or relations:
                                knowledge_graph.add_to_graph(entities, relations)
                            entities_count += len(entities)
                            relations_count += len(relations)
                    except Exception as e:
                        print(f"      ⚠️  提取失败: {e}")
                if entities_count > 0:
                    print(f"   ✅ 提取了 {entities_count} 个实体，{relations_count} 个关系")
            
            return {
                "success": True,
                "message": f"成功处理 {len(files)} 个文件",
                "documents_added": len(documents) if documents else 0,
                "images_added": len(images) if images else 0,
                "saved_to_data": len(permanent_files),
                "entities_extracted": entities_count,
                "relations_extracted": relations_count
            }
        
        finally:
            # 清理临时目录
            shutil.rmtree(temp_dir)
            
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ 上传文件错误: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

# ============================================================
# 主程序
# ============================================================

if __name__ == "__main__":
    import uvicorn
    
    print("=" * 60)
    print("🚀 启动 RAG Agent API 服务器")
    print("=" * 60)
    
    uvicorn.run(
        "api:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
