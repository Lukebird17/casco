#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gemini 风格学习辅助系统
模仿 Google Gemini 的简洁现代 UI
"""

import gradio as gr
from typing import List, Dict, Optional, Tuple
import json
from pathlib import Path

# 导入所有模块
from rag_agent import RAGAgent
from session_manager import SessionManager
from confidence_calculator import ConfidenceCalculator
from multimodal_input_handler import MultimodalInputHandler
from document_viewer import DocumentViewer
from document_heatmap import DocumentHeatmap
from snippet_manager import SnippetManager
from quiz_generator import QuizGenerator
from socratic_mode import SocraticMode
from knowledge_graph import KnowledgeGraph
from flashcard_system import FlashcardSystem
from document_outline import DocumentOutline
from config import TEXT_MODEL_NAME, MULTIMODAL_MODEL_NAME


# ============================================================
# 全局变量
# ============================================================
agent: Optional[RAGAgent] = None
session_manager: Optional[SessionManager] = None
confidence_calculator: Optional[ConfidenceCalculator] = None
multimodal_handler: Optional[MultimodalInputHandler] = None
doc_viewer: Optional[DocumentViewer] = None
heatmap: Optional[DocumentHeatmap] = None
snippet_mgr: Optional[SnippetManager] = None
quiz_gen: Optional[QuizGenerator] = None
socratic: Optional[SocraticMode] = None
knowledge_graph: Optional[KnowledgeGraph] = None
flashcard_sys: Optional[FlashcardSystem] = None
doc_outline: Optional[DocumentOutline] = None


# ============================================================
# 初始化
# ============================================================
def initialize_system():
    """初始化所有系统组件"""
    global agent, session_manager, confidence_calculator, multimodal_handler
    global doc_viewer, heatmap, snippet_mgr, quiz_gen, socratic, knowledge_graph, flashcard_sys, doc_outline
    
    try:
        print("🚀 初始化 Gemini 风格系统...")
        
        agent = RAGAgent(
            model=TEXT_MODEL_NAME,
            text_model=TEXT_MODEL_NAME,
            multimodal_model=MULTIMODAL_MODEL_NAME,
            enable_tracking=True,
            enable_cot=True,
            use_multimodal=True
        )
        session_manager = SessionManager()
        confidence_calculator = ConfidenceCalculator()
        multimodal_handler = MultimodalInputHandler()
        doc_viewer = DocumentViewer()
        heatmap = DocumentHeatmap()
        snippet_mgr = SnippetManager()
        quiz_gen = QuizGenerator()
        socratic = SocraticMode()
        knowledge_graph = KnowledgeGraph()
        flashcard_sys = FlashcardSystem()
        doc_outline = DocumentOutline()
        
        if not session_manager.sessions:
            session_manager.create_session("新对话")
        else:
            latest = list(session_manager.sessions.keys())[-1]
            session_manager.switch_session(latest)
        
        print("✅ 所有组件初始化完成")
        return True, "✅ 系统就绪", _render_session_list()
    
    except Exception as e:
        import traceback
        print(f"❌ 初始化失败: {traceback.format_exc()}")
        return False, f"❌ 初始化失败: {str(e)}", ""


# ============================================================
# 对话功能
# ============================================================
def chat_gemini_style(
    message: str,
    image: Optional[object],
    file: Optional[object],
    history: List[Dict],
    enable_socratic: bool
) -> Tuple:
    """Gemini 风格对话"""
    global agent, session_manager, multimodal_handler, heatmap, socratic
    
    if not agent:
        error_history = history + [
            {"role": "user", "content": message or "上传了内容"},
            {"role": "assistant", "content": "❌ 系统未初始化，请先点击初始化"}
        ]
        return error_history, ""
    
    try:
        user_message = message if message else "请分析上传的内容"
        query_for_rag = user_message
        image_path = None
        file_content = None
        
        # 处理图片
        if image is not None:
            print("📷 处理图片...")
            image_result = multimodal_handler.handle_image_input(image, user_message)
            query_for_rag = image_result['enhanced_query']
            image_path = image_result['image_path']
        
        # 处理文件
        elif file is not None:
            print("📄 处理文件...")
            file_result = multimodal_handler.handle_file_input(file.name, user_message)
            if file_result.get('error'):
                raise Exception(file_result['error'])
            query_for_rag = file_result['query']
            file_content = file_result['file_content']
        
        # 调用 RAG
        result = agent.answer_question(
            query_for_rag, 
            chat_history=history,
            image=image_path,
            file_content=file_content
        )
        
        if isinstance(result, dict):
            answer = result.get('answer', str(result))
            retrieved_docs = result.get('context', [])
        else:
            answer = str(result)
            retrieved_docs = []
        
        # 苏格拉底模式
        if enable_socratic and socratic and socratic.is_enabled():
            socratic_response = socratic.generate_socratic_response(
                query_for_rag, answer, history[-6:]
            )
            answer = socratic_response['response']
        
        # 记录热力图
        if isinstance(retrieved_docs, list) and heatmap:
            for doc in retrieved_docs:
                metadata = doc.get('metadata', {})
                filename = metadata.get('filename', '')
                page = metadata.get('page', 1)
                if filename and page:
                    heatmap.record_citation(filename, page)
        
        # 更新历史
        new_history = history + [
            {"role": "user", "content": user_message},
            {"role": "assistant", "content": answer}
        ]
        
        # 保存会话
        if session_manager:
            session_manager.add_message_to_current("user", user_message)
            session_manager.add_message_to_current("assistant", answer)
        
        # 生成引用信息
        citations_html = _format_citations_gemini(retrieved_docs if isinstance(retrieved_docs, list) else [])
        
        return new_history, citations_html
        
    except Exception as e:
        import traceback
        error_msg = f"❌ 错误: {str(e)}"
        print(f"\n{error_msg}\n{traceback.format_exc()}")
        error_history = history + [
            {"role": "user", "content": message or "上传了内容"},
            {"role": "assistant", "content": error_msg}
        ]
        return error_history, ""


def _format_citations_gemini(docs: List[Dict]) -> str:
    """Gemini 风格的引用格式"""
    if not docs:
        return ""
    
    html = '<div style="margin-top: 20px; padding: 16px; background: #f8f9fa; border-radius: 12px;">'
    html += '<div style="font-size: 13px; font-weight: 600; color: #5f6368; margin-bottom: 12px;">📚 来源</div>'
    
    for i, doc in enumerate(docs[:3], 1):  # 只显示前3个
        metadata = doc.get('metadata', {})
        filename = metadata.get('filename', '未知文档')
        page = metadata.get('page', 'N/A')
        content = doc.get('content', '')[:100]
        
        html += f'''
        <div style="padding: 12px; margin-bottom: 8px; background: white; border-radius: 8px; 
                    box-shadow: 0 1px 2px rgba(0,0,0,0.05); cursor: pointer;"
             onmouseover="this.style.boxShadow='0 2px 8px rgba(0,0,0,0.1)'"
             onmouseout="this.style.boxShadow='0 1px 2px rgba(0,0,0,0.05)'">
            <div style="font-size: 12px; font-weight: 600; color: #1967d2; margin-bottom: 4px;">
                [{i}] {filename} - 第 {page} 页
            </div>
            <div style="font-size: 11px; color: #5f6368; line-height: 1.5;">
                {content}...
            </div>
        </div>
        '''
    
    html += '</div>'
    return html


# ============================================================
# 会话管理
# ============================================================
def create_new_session():
    """创建新对话"""
    if not session_manager:
        return [], "❌ 未初始化", ""
    
    session = session_manager.create_session("新对话")
    return [], f"✅ 已创建新对话", _render_session_list()


def _render_session_list() -> str:
    """渲染会话列表（Gemini 风格）"""
    if not session_manager:
        return ""
    
    sessions = session_manager.list_sessions()
    current = session_manager.get_current_session()
    current_id = current.session_id if current else None
    
    html = '<div style="padding: 8px;">'
    
    for session in sessions[:20]:  # 最多显示20个
        is_current = session['session_id'] == current_id
        bg = "#e8f0fe" if is_current else "white"
        border = "2px solid #1967d2" if is_current else "1px solid #e8eaed"
        
        html += f'''
        <div style="padding: 12px 16px; margin-bottom: 8px; background: {bg}; 
                    border: {border}; border-radius: 8px; cursor: pointer;
                    transition: all 0.2s;"
             onmouseover="this.style.background='#f8f9fa'"
             onmouseout="this.style.background='{bg}'"
             onclick="alert('switch_{session['session_id']}')">
            <div style="font-size: 14px; font-weight: 500; color: #202124; margin-bottom: 4px;">
                💬 {session['title']}
            </div>
            <div style="font-size: 11px; color: #5f6368;">
                {session['updated_at']} · {session['message_count']} 条消息
            </div>
        </div>
        '''
    
    html += '</div>'
    return html


# ============================================================
# 工具功能
# ============================================================
def show_tool_panel(tool_name: str):
    """显示工具面板"""
    if tool_name == "quiz":
        return _render_quiz_tool()
    elif tool_name == "flashcard":
        return _render_flashcard_tool()
    elif tool_name == "graph":
        return _render_graph_tool()
    elif tool_name == "snippet":
        return _render_snippet_tool()
    else:
        return ""


def _render_quiz_tool() -> str:
    """测验工具"""
    return '''
    <div style="padding: 24px; background: white; border-radius: 16px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
        <h3 style="color: #1967d2; margin-bottom: 16px;">📝 生成测验</h3>
        <div style="font-size: 14px; color: #5f6368; margin-bottom: 20px;">
            基于学习内容自动生成测试题，帮助巩固知识
        </div>
        <!-- 这里可以添加更多控件 -->
    </div>
    '''


def _render_flashcard_tool() -> str:
    """闪卡工具"""
    if not flashcard_sys:
        return ""
    
    return flashcard_sys.render_review_session()


def _render_graph_tool() -> str:
    """知识图谱工具"""
    if not knowledge_graph:
        return ""
    
    return knowledge_graph.render_graph_simple()


def _render_snippet_tool() -> str:
    """片段收藏工具"""
    if not snippet_mgr:
        return ""
    
    return snippet_mgr.render_snippets()


# ============================================================
# 构建 Gemini 风格 UI
# ============================================================
def build_gemini_ui():
    """构建 Gemini 风格的 UI"""
    
    # Gemini 风格的 CSS
    gemini_css = """
    /* Gemini 风格全局样式 */
    .gradio-container {
        font-family: 'Google Sans', 'Roboto', sans-serif !important;
        background: #ffffff !important;
    }
    
    /* 隐藏 Gradio 默认的一些元素 */
    .gradio-container .footer {
        display: none !important;
    }
    
    /* 消息气泡样式 */
    .message {
        padding: 16px;
        border-radius: 18px;
        margin-bottom: 12px;
        max-width: 80%;
    }
    
    .user-message {
        background: #e8f0fe;
        margin-left: auto;
    }
    
    .assistant-message {
        background: #f8f9fa;
        margin-right: auto;
    }
    
    /* 输入框样式 */
    .input-container {
        position: sticky;
        bottom: 0;
        background: white;
        padding: 20px;
        border-top: 1px solid #e8eaed;
        box-shadow: 0 -2px 10px rgba(0,0,0,0.05);
    }
    
    /* 按钮样式 */
    .primary-button {
        background: linear-gradient(135deg, #1967d2 0%, #4285f4 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 24px !important;
        padding: 12px 24px !important;
        font-weight: 500 !important;
        transition: all 0.3s !important;
    }
    
    .primary-button:hover {
        box-shadow: 0 4px 12px rgba(25, 103, 210, 0.3) !important;
        transform: translateY(-1px) !important;
    }
    
    /* 侧边栏样式 */
    .sidebar {
        background: #f8f9fa;
        border-right: 1px solid #e8eaed;
        height: 100vh;
        overflow-y: auto;
    }
    
    /* 卡片样式 */
    .card {
        background: white;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        transition: all 0.2s;
    }
    
    .card:hover {
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    
    /* 滚动条样式 */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f3f4;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #dadce0;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #bdc1c6;
    }
    """
    
    with gr.Blocks(
        title="🤖 智能学习助手",
        theme=gr.themes.Soft(
            primary_hue="blue",
            secondary_hue="blue",
            neutral_hue="slate",
        ),
        css=gemini_css
    ) as app:
        
        # 状态变量
        system_initialized = gr.State(False)
        
        # ============================================================
        # 顶部导航栏
        # ============================================================
        with gr.Row(elem_classes="header"):
            with gr.Column(scale=1):
                gr.Markdown("# 🤖 智能学习助手")
            with gr.Column(scale=1):
                with gr.Row():
                    init_btn = gr.Button("🚀 初始化系统", size="sm", variant="primary")
                    new_chat_btn = gr.Button("➕ 新对话", size="sm")
        
        # ============================================================
        # 主布局：侧边栏 + 对话区
        # ============================================================
        with gr.Row():
            
            # 左侧边栏（历史对话 + 工具）
            with gr.Column(scale=2, elem_classes="sidebar"):
                gr.Markdown("### 💬 对话历史")
                session_list = gr.HTML()
                
                gr.Markdown("### 🛠️ 工具", elem_id="tools-header")
                
                with gr.Accordion("📝 测验", open=False):
                    quiz_topic = gr.Textbox(label="主题", placeholder="例如：操作系统")
                    quiz_btn = gr.Button("生成测验", size="sm")
                    quiz_display = gr.HTML()
                
                with gr.Accordion("📇 闪卡", open=False):
                    flashcard_btn = gr.Button("开始复习", size="sm")
                    flashcard_display = gr.HTML()
                
                with gr.Accordion("🕸️ 知识图谱", open=False):
                    graph_btn = gr.Button("构建图谱", size="sm")
                    graph_display = gr.HTML()
                
                with gr.Accordion("⭐ 收藏", open=False):
                    snippet_content = gr.Textbox(label="内容", lines=3)
                    snippet_btn = gr.Button("保存", size="sm")
                    snippet_display = gr.HTML()
            
            # 中间主对话区
            with gr.Column(scale=5):
                # 对话显示区
                chatbot = gr.Chatbot(
                    label="对话",
                    type="messages",
                    height=600,
                    show_label=False,
                    bubble_full_width=False,
                    avatar_images=(None, "🤖")
                )
                
                # 引用显示区
                citations = gr.HTML()
                
                # 底部输入区（固定）
                with gr.Row(elem_classes="input-container"):
                    with gr.Column(scale=10):
                        msg_input = gr.Textbox(
                            label="",
                            placeholder="向我提问任何问题...",
                            show_label=False,
                            container=False,
                            lines=1
                        )
                    with gr.Column(scale=1, min_width=100):
                        img_input = gr.Image(
                            label="",
                            type="pil",
                            show_label=False,
                            container=False,
                            height=40
                        )
                    with gr.Column(scale=1, min_width=100):
                        file_input = gr.File(
                            label="",
                            show_label=False,
                            container=False,
                            height=40
                        )
                
                with gr.Row():
                    send_btn = gr.Button(
                        "📤 发送",
                        variant="primary",
                        elem_classes="primary-button"
                    )
                    clear_btn = gr.Button("🔄 清空")
                    socratic_check = gr.Checkbox(
                        label="🧙‍♂️ 苏格拉底模式",
                        value=False
                    )
            
            # 右侧工具栏（可选）
            with gr.Column(scale=2, visible=False) as right_panel:
                gr.Markdown("### 📊 分析")
                
                with gr.Accordion("🎯 置信度", open=True):
                    confidence_display = gr.HTML()
                
                with gr.Accordion("🔥 热力图", open=False):
                    heatmap_btn = gr.Button("查看热力图", size="sm")
                    heatmap_display = gr.HTML()
        
        # ============================================================
        # 事件绑定
        # ============================================================
        
        # 初始化
        init_btn.click(
            fn=initialize_system,
            outputs=[system_initialized, gr.Textbox(visible=False), session_list]
        )
        
        # 新对话
        new_chat_btn.click(
            fn=create_new_session,
            outputs=[chatbot, gr.Textbox(visible=False), session_list]
        )
        
        # 发送消息
        send_btn.click(
            fn=chat_gemini_style,
            inputs=[msg_input, img_input, file_input, chatbot, socratic_check],
            outputs=[chatbot, citations]
        ).then(
            fn=lambda: ("", None, None),
            outputs=[msg_input, img_input, file_input]
        )
        
        # 回车发送
        msg_input.submit(
            fn=chat_gemini_style,
            inputs=[msg_input, img_input, file_input, chatbot, socratic_check],
            outputs=[chatbot, citations]
        ).then(
            fn=lambda: ("", None, None),
            outputs=[msg_input, img_input, file_input]
        )
        
        # 清空对话
        clear_btn.click(fn=lambda: [], outputs=[chatbot])
        
        # 工具按钮
        quiz_btn.click(
            fn=lambda topic: quiz_gen.generate_quiz(topic, "", 5, "medium") if quiz_gen else {},
            inputs=[quiz_topic],
            outputs=[quiz_display]
        )
        
        flashcard_btn.click(
            fn=lambda: flashcard_sys.render_review_session() if flashcard_sys else "",
            outputs=[flashcard_display]
        )
        
        graph_btn.click(
            fn=lambda: knowledge_graph.render_graph_simple() if knowledge_graph else "",
            outputs=[graph_display]
        )
        
        snippet_btn.click(
            fn=lambda content: (snippet_mgr.add_snippet(content, "", []), snippet_mgr.render_snippets()) if snippet_mgr and content else ("", ""),
            inputs=[snippet_content],
            outputs=[gr.Textbox(visible=False), snippet_display]
        )
        
        heatmap_btn.click(
            fn=lambda: heatmap.render_heatmap() if heatmap else "",
            outputs=[heatmap_display]
        )
    
    return app


# ============================================================
# 启动
# ============================================================
if __name__ == "__main__":
    app = build_gemini_ui()
    app.queue()
    app.launch(
        server_name="0.0.0.0",
        server_port=7862,
        share=False,
        show_error=True
    )





