"""
FastAPI 后端 API
为 React 前端提供 RESTful 接口
"""

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Optional
from contextlib import asynccontextmanager
import sys
import os

# 添加父目录到路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rag_agent import RAGAgent
from session_manager import SessionManager
from confidence_calculator import ConfidenceCalculator
from quiz_generator import QuizGenerator
from flashcard_system import FlashcardSystem
from knowledge_graph import KnowledgeGraph
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

# ============================================================
# Lifespan 事件处理（替代 on_event）
# ============================================================

@asynccontextmanager
async def lifespan(app: FastAPI):
    """应用生命周期管理"""
    global rag_agent, session_manager, confidence_calculator, quiz_generator, flashcard_system, knowledge_graph
    
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
        knowledge_graph = KnowledgeGraph()
        
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
                from vector_store import VectorStore
                from image_vector_store import ImageVectorStore
                
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
        
        # 提取引用（在添加消息之前）
        # Context已经在rag_agent中打印，这里只收集用于前端展示
        citations = []
        if hasattr(rag_agent, 'last_context_docs') and rag_agent.last_context_docs:
            for i, doc in enumerate(rag_agent.last_context_docs[:5], 1):  # 最多5个引用
                filename = doc.get("filename", "未知")
                page_num = doc.get("page_num", doc.get("page_number", 0))
                section = doc.get("section", "")
                content_snippet = doc.get("content", "")[:200]
                
                # 添加到引用列表（用于前端展示）
                citations.append({
                    "filename": filename,
                    "page": page_num,
                    "section": section,
                    "snippet": content_snippet
                })
        
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
    context: str
    num_questions: int = 5
    difficulty: str = "medium"

@app.post("/api/quiz/generate")
async def generate_quiz(request: QuizRequest):
    """
    生成测验
    """
    try:
        if quiz_generator is None:
            raise HTTPException(status_code=500, detail="测验生成器未初始化")
        
        questions = quiz_generator.generate_quiz(
            request.context,
            request.num_questions,
            request.difficulty
        )
        
        return {
            "success": True,
            "questions": questions
        }
    except Exception as e:
        print(f"❌ 生成测验错误: {e}")
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
async def search_in_document(filename: str, query: str):
    """
    在文档中搜索概念/关键词
    """
    try:
        from config import DATA_DIR
        import PyPDF2
        
        filepath = os.path.join(DATA_DIR, filename)
        
        if not os.path.exists(filepath):
            raise HTTPException(status_code=404, detail="文件不存在")
        
        file_ext = os.path.splitext(filename)[1].lower()
        results = []
        
        if file_ext == '.pdf':
            # PDF文件搜索
            with open(filepath, 'rb') as f:
                pdf_reader = PyPDF2.PdfReader(f)
                
                for page_num, page in enumerate(pdf_reader.pages, 1):
                    text = page.extract_text()
                    
                    # 查找所有匹配项
                    lines = text.split('\n')
                    for line_num, line in enumerate(lines):
                        if query.lower() in line.lower():
                            # 找到匹配项的上下文
                            start = max(0, line.find(query.lower()) - 50)
                            end = min(len(line), line.find(query.lower()) + len(query) + 50)
                            context = line[start:end]
                            
                            results.append({
                                "page": page_num,
                                "line": line_num,
                                "context": context,
                                "match": query
                            })
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
                    
                    knowledge_bases.append({
                        "id": kb_name,
                        "name": f"{kb_name}知识库" if kb_name == "default" else kb_name,
                        "path": kb_vector_path,
                        "size": round(size, 2),
                        "is_current": kb_name == "default",  # 默认选中default
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
        from document_loader import DocumentLoader
        from text_splitter import TextSplitter
        from vector_store import VectorStore
        from image_vector_store import ImageVectorStore
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
                                    "page": page_num,
                                    "subsections": []
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
        from document_loader import DocumentLoader
        from text_splitter import TextSplitter
        from vector_store import VectorStore
        from image_vector_store import ImageVectorStore
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
