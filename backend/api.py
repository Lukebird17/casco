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
            use_multimodal=True  # 暂时禁用多模态以修复检索问题
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
    image_base64: Optional[str] = None

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
        session = session_manager.get_session(request.session_id)
        if not session:
            session = session_manager.create_session("新对话")
            request.session_id = session.session_id
        
        # 获取会话历史
        chat_history = session.messages
        
        # 处理消息（这里简化处理，实际应该根据是否有图片等做不同处理）
        response_text = rag_agent.answer_question(
            request.message,
            chat_history=chat_history
        )
        
        # 提取引用（在添加消息之前）
        citations = []
        if hasattr(rag_agent, 'last_context_docs') and rag_agent.last_context_docs:
            for doc in rag_agent.last_context_docs[:5]:  # 最多5个引用
                citations.append({
                    "filename": doc.get("filename", "未知"),
                    "page": doc.get("page_num", 0),
                    "snippet": doc.get("content", "")[:200]
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
