#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
完整功能版 - 高级学习辅助系统
集成所有功能：PDF阅览、热力图、片段收藏、测验、苏格拉底模式、知识图谱、闪卡
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

# 当前状态
current_quiz: Optional[Dict] = None
current_flashcard_idx: int = 0


# ============================================================
# 初始化
# ============================================================
def initialize_system():
    """初始化所有系统组件"""
    global agent, session_manager, confidence_calculator, multimodal_handler
    global doc_viewer, heatmap, snippet_mgr, quiz_gen, socratic, knowledge_graph, flashcard_sys
    
    try:
        print("🚀 初始化完整功能系统...")
        
        # 核心组件
        agent = RAGAgent(
            model=TEXT_MODEL_NAME,
            text_model=TEXT_MODEL_NAME,
            multimodal_model=MULTIMODAL_MODEL_NAME,
            enable_tracking=True,
            enable_cot=True,
            use_multimodal=True
        )
        print("✅ RAG Agent")
        
        session_manager = SessionManager()
        print("✅ 会话管理器")
        
        confidence_calculator = ConfidenceCalculator()
        print("✅ 置信度计算器")
        
        multimodal_handler = MultimodalInputHandler()
        print("✅ 多模态处理器")
        
        # 高级功能组件
        doc_viewer = DocumentViewer()
        print("✅ 文档查看器")
        
        heatmap = DocumentHeatmap()
        print("✅ 热力图")
        
        snippet_mgr = SnippetManager()
        print("✅ 片段收藏")
        
        quiz_gen = QuizGenerator()
        print("✅ 测验生成器")
        
        socratic = SocraticMode()
        print("✅ 苏格拉底模式")
        
        knowledge_graph = KnowledgeGraph()
        print("✅ 知识图谱")
        
        flashcard_sys = FlashcardSystem()
        print("✅ 闪卡系统")
        
        # 创建默认会话
        if not session_manager.sessions:
            session_manager.create_session("第一次对话")
        else:
            latest = list(session_manager.sessions.keys())[-1]
            session_manager.switch_session(latest)
        
        return "✅ 系统初始化成功！所有功能已就绪。"
    
    except Exception as e:
        import traceback
        error_msg = f"❌ 初始化失败: {str(e)}\n{traceback.format_exc()}"
        print(error_msg)
        return error_msg


# ============================================================
# 对话功能
# ============================================================
def chat_with_all_features(
    message: str,
    image: Optional[object],
    file: Optional[object],
    history: List[Dict],
    show_thinking: bool,
    show_confidence: bool,
    socratic_enabled: bool
) -> Tuple:
    """完整功能的对话"""
    global agent, session_manager, confidence_calculator, multimodal_handler, heatmap, socratic
    
    if not agent:
        error = "❌ 系统未初始化"
        history.append({"role": "user", "content": message or "上传了内容"})
        history.append({"role": "assistant", "content": error})
        return history, "", "", "", "", error
    
    try:
        user_message = message if message else "请分析上传的内容"
        query_for_rag = user_message
        image_path = None
        file_content = None
        thinking_steps = []
        
        # 处理图片
        if image is not None:
            thinking_steps.append("📷 正在分析图片...")
            image_result = multimodal_handler.handle_image_input(image, user_message)
            query_for_rag = image_result['enhanced_query']
            image_path = image_result['image_path']
            thinking_steps.append(f"✅ 图片分析完成")
        
        # 处理文件
        elif file is not None:
            thinking_steps.append(f"📄 正在读取文件...")
            file_result = multimodal_handler.handle_file_input(file.name, user_message)
            if file_result.get('error'):
                raise Exception(file_result['error'])
            query_for_rag = file_result['query']
            file_content = file_result['file_content']
            thinking_steps.append(f"✅ 文件读取完成")
        
        # 检索
        thinking_steps.append("🔍 正在检索知识...")
        thinking_html = _format_thinking(thinking_steps)
        yield history, thinking_html, "", "", "", "检索中..."
        
        # 调用 RAG（苏格拉底模式或正常模式）
        if socratic_enabled and socratic and socratic.is_enabled():
            # 苏格拉底模式
            thinking_steps.append("🧙‍♂️ 启用苏格拉底引导模式...")
            result = agent.answer_question(query_for_rag, chat_history=history, image=image_path, file_content=file_content)
            
            if isinstance(result, dict):
                answer = result.get('answer', str(result))
                retrieved_docs = result.get('context', [])
                query_type = result.get('query_type', 'basic')
            else:
                answer = str(result)
                retrieved_docs = []
                query_type = 'basic'
            
            # 生成苏格拉底式回应
            socratic_response = socratic.generate_socratic_response(
                query_for_rag,
                answer,  # 使用检索到的内容作为参考
                history[-6:]
            )
            
            answer = socratic_response['response']
            socratic_html = socratic.render_socratic_ui(socratic_response)
        else:
            # 正常模式
            result = agent.answer_question(query_for_rag, chat_history=history, image=image_path, file_content=file_content)
            
            if isinstance(result, dict):
                answer = result.get('answer', str(result))
                retrieved_docs = result.get('context', [])
                query_type = result.get('query_type', 'basic')
            else:
                answer = str(result)
                retrieved_docs = []
                query_type = 'basic'
            
            socratic_html = ""
        
        thinking_steps.append(f"✅ 检索完成")
        
        # 记录热力图
        if isinstance(retrieved_docs, list) and heatmap:
            for doc in retrieved_docs:
                metadata = doc.get('metadata', {})
                filename = metadata.get('filename', '')
                page = metadata.get('page', 1)
                if filename and page:
                    heatmap.record_citation(filename, page, doc.get('content', '')[:100])
        
        # 计算置信度
        confidence_info = ""
        if show_confidence and confidence_calculator:
            thinking_steps.append("📊 计算置信度...")
            docs_list = retrieved_docs if isinstance(retrieved_docs, list) else []
            conf_result = confidence_calculator.calculate(query_for_rag, answer, docs_list, query_type)
            confidence_info = _format_confidence(conf_result)
            thinking_steps.append(f"✅ 置信度: {conf_result['emoji']} {conf_result['level']}")
        
        # 文档预览
        doc_preview = _format_doc_preview(retrieved_docs if isinstance(retrieved_docs, list) else [])
        
        # 更新历史
        history.append({"role": "user", "content": user_message})
        history.append({"role": "assistant", "content": answer})
        
        # 保存会话
        if session_manager:
            session_manager.add_message_to_current("user", user_message)
            session_manager.add_message_to_current("assistant", answer, {
                "confidence": conf_result if show_confidence else None
            })
        
        thinking_steps.append("✅ 完成！")
        final_thinking = _format_thinking(thinking_steps) if show_thinking else ""
        
        yield history, final_thinking, confidence_info, doc_preview, socratic_html, "✅ 完成"
        
    except Exception as e:
        import traceback
        error_msg = f"❌ 错误: {str(e)}"
        print(f"\n{error_msg}\n{traceback.format_exc()}")
        history.append({"role": "user", "content": message or "上传了内容"})
        history.append({"role": "assistant", "content": error_msg})
        yield history, "", "", "", "", error_msg


def _format_thinking(steps: List[str]) -> str:
    """格式化思维过程"""
    html = '<div style="padding: 15px; background: #f8f9fa; border-radius: 8px; font-family: monospace;">'
    for i, step in enumerate(steps):
        html += f'<div style="margin: 8px 0; padding: 8px; background: white; border-left: 3px solid #6366f1; border-radius: 4px;">'
        html += f'<span style="color: #6366f1; font-weight: bold;">{i+1}.</span> {step}'
        html += '</div>'
    html += '</div>'
    return html


def _format_confidence(conf: Dict) -> str:
    """格式化置信度"""
    return f'''
    <div style="padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 12px; color: white;">
        <div style="font-size: 24px; font-weight: bold; margin-bottom: 10px;">
            {conf['emoji']} 置信度：{conf['level']}
        </div>
        <div style="font-size: 48px; font-weight: bold; margin: 15px 0;">
            {conf['score']:.0%}
        </div>
        <div style="font-size: 14px; opacity: 0.9; margin-top: 15px;">
            {conf['explanation']}
        </div>
    </div>
    '''


def _format_doc_preview(docs: List[Dict]) -> str:
    """格式化文档预览"""
    if not docs:
        return '<div style="padding: 20px; text-align: center; color: #999;">暂无引用文档</div>'
    
    html = f'<div style="padding: 15px;"><h3 style="color: #6366f1;">📚 引用来源 ({len(docs)})</h3>'
    for doc in docs[:5]:
        content = doc.get('content', '')
        metadata = doc.get('metadata', {})
        html += f'''
        <div style="margin: 10px 0; padding: 15px; background: #f8f9fa; border-left: 4px solid #6366f1; border-radius: 6px;">
            <div style="font-weight: bold; color: #6366f1;">📄 {metadata.get('filename', '未知')} - 第 {metadata.get('page', 'N/A')} 页</div>
            <div style="font-size: 14px; margin-top: 8px;">{content[:200]}...</div>
        </div>
        '''
    html += '</div>'
    return html


# ============================================================
# 片段收藏
# ============================================================
def save_snippet(content: str, source: str, tags: str):
    """保存片段"""
    if not snippet_mgr or not content:
        return "❌ 请输入内容", snippet_mgr.render_snippets() if snippet_mgr else ""
    
    tag_list = [t.strip() for t in tags.split(',') if t.strip()]
    snippet_id = snippet_mgr.add_snippet(content, source, tag_list)
    
    return f"✅ 已收藏片段 {snippet_id}", snippet_mgr.render_snippets()


def search_snippets_ui(query: str, tags: str, favorites_only: bool):
    """搜索片段"""
    if not snippet_mgr:
        return ""
    
    tag_list = [t.strip() for t in tags.split(',') if t.strip()] if tags else None
    results = snippet_mgr.search_snippets(query if query else None, tag_list, favorites_only)
    
    return snippet_mgr.render_snippets(results)


# ============================================================
# 测验生成
# ============================================================
def generate_quiz_ui(topic: str, num_questions: int, difficulty: str):
    """生成测验"""
    global current_quiz, agent
    
    if not quiz_gen or not agent:
        return "❌ 系统未初始化"
    
    if not topic:
        return "❌ 请输入测验主题"
    
    # 检索相关内容
    result = agent.answer_question(f"请总结关于{topic}的核心知识点")
    if isinstance(result, dict):
        context = result.get('answer', '')
    else:
        context = str(result)
    
    # 生成测验
    current_quiz = quiz_gen.generate_quiz(topic, context, num_questions, difficulty.lower())
    
    return quiz_gen.render_quiz(current_quiz, show_answers=False)


def show_quiz_answers():
    """显示测验答案"""
    if not quiz_gen or not current_quiz:
        return "❌ 请先生成测验"
    
    return quiz_gen.render_quiz(current_quiz, show_answers=True)


# ============================================================
# 苏格拉底模式
# ============================================================
def toggle_socratic_mode():
    """切换苏格拉底模式"""
    if not socratic:
        return False, "❌ 系统未初始化"
    
    enabled = socratic.toggle_mode()
    status = "✅ 苏格拉底模式已启用" if enabled else "✅ 苏格拉底模式已关闭"
    
    return enabled, status


# ============================================================
# 知识图谱
# ============================================================
def build_knowledge_graph_ui():
    """构建知识图谱"""
    if not knowledge_graph or not agent:
        return "❌ 系统未初始化"
    
    # 获取一些文档内容
    try:
        # 这里简化处理，实际应该从向量库获取
        result = agent.answer_question("请列举主要的概念")
        if isinstance(result, dict):
            content = result.get('answer', '')
        else:
            content = str(result)
        
        knowledge_graph.build_graph_from_documents([content])
        
        return knowledge_graph.render_graph_simple()
    except Exception as e:
        return f"❌ 构建失败: {str(e)}"


# ============================================================
# 闪卡系统
# ============================================================
def generate_flashcards_ui(content: str, num_cards: int):
    """生成闪卡"""
    if not flashcard_sys or not content:
        return "❌ 请输入学习内容"
    
    cards = flashcard_sys.generate_flashcards(content, num_cards)
    
    if cards:
        return f"✅ 生成了 {len(cards)} 张闪卡", flashcard_sys.render_review_session()
    else:
        return "❌ 生成失败", ""


def start_review_session():
    """开始复习"""
    if not flashcard_sys:
        return ""
    
    return flashcard_sys.render_review_session()


# ============================================================
# 热力图和文档查看
# ============================================================
def show_heatmap_ui():
    """显示热力图"""
    if not heatmap:
        return ""
    
    return heatmap.render_heatmap()


def show_document_list():
    """显示文档列表"""
    if not doc_viewer:
        return ""
    
    return doc_viewer.render_document_list()


# ============================================================
# 构建完整 UI
# ============================================================
def build_complete_ui():
    """构建完整功能的UI"""
    
    custom_css = """
    .gradio-container {
        font-family: 'Inter', sans-serif;
    }
    """
    
    with gr.Blocks(
        title="🎓 完整功能学习辅助系统",
        theme=gr.themes.Soft(primary_hue="indigo"),
        css=custom_css
    ) as app:
        
        gr.Markdown("""
        # 🎓 完整功能学习辅助系统
        ### 集成所有高级功能的智能学习助手
        """)
        
        # 初始化
        with gr.Row():
            init_btn = gr.Button("🚀 初始化系统", variant="primary")
            init_status = gr.Textbox(label="状态", value="未初始化", interactive=False)
        
        # 主选项卡
        with gr.Tabs() as tabs:
            
            # ===== Tab 1: 对话 =====
            with gr.Tab("💬 对话"):
                with gr.Row():
                    with gr.Column(scale=7):
                        chatbot = gr.Chatbot(label="对话", type="messages", height=500)
                        
                        with gr.Row():
                            msg_input = gr.Textbox(label="消息", placeholder="输入问题...", scale=6)
                            img_input = gr.Image(label="图片", type="pil", scale=2)
                            file_input = gr.File(label="文件", scale=2)
                        
                        with gr.Row():
                            send_btn = gr.Button("📤 发送", variant="primary")
                            clear_btn = gr.Button("🔄 清空")
                        
                        status_box = gr.Textbox(label="状态", interactive=False)
                    
                    with gr.Column(scale=3):
                        gr.Markdown("### ⚙️ 选项")
                        show_thinking_check = gr.Checkbox(label="显示思维过程", value=True)
                        show_conf_check = gr.Checkbox(label="显示置信度", value=True)
                        socratic_check = gr.Checkbox(label="苏格拉底模式", value=False)
                        
                        with gr.Accordion("🧠 思维过程", open=True):
                            thinking_display = gr.HTML()
                        
                        with gr.Accordion("📈 置信度", open=True):
                            conf_display = gr.HTML()
            
            # ===== Tab 2: 文档与热力图 =====
            with gr.Tab("📚 文档"):
                with gr.Row():
                    with gr.Column(scale=1):
                        gr.Markdown("### 📄 文档列表")
                        doc_list_btn = gr.Button("刷新列表")
                        doc_list_display = gr.HTML()
                    
                    with gr.Column(scale=1):
                        gr.Markdown("### 🔥 热力图")
                        heatmap_btn = gr.Button("查看热力图")
                        heatmap_display = gr.HTML()
                    
                    with gr.Column(scale=2):
                        gr.Markdown("### 📚 引用文档")
                        doc_preview_display = gr.HTML()
            
            # ===== Tab 3: 片段收藏 =====
            with gr.Tab("⭐ 收藏"):
                with gr.Row():
                    with gr.Column(scale=1):
                        gr.Markdown("### 新建收藏")
                        snippet_content = gr.Textbox(label="内容", lines=5, placeholder="粘贴要收藏的内容...")
                        snippet_source = gr.Textbox(label="来源", placeholder="来源（可选）")
                        snippet_tags = gr.Textbox(label="标签", placeholder="标签1, 标签2")
                        save_snippet_btn = gr.Button("💾 保存", variant="primary")
                        save_status = gr.Textbox(label="状态", interactive=False)
                    
                    with gr.Column(scale=2):
                        gr.Markdown("### 我的收藏")
                        
                        with gr.Row():
                            search_query = gr.Textbox(label="搜索", placeholder="搜索关键词...")
                            search_tags = gr.Textbox(label="标签筛选", placeholder="标签1, 标签2")
                            favorites_only = gr.Checkbox(label="只看重要", value=False)
                        
                        search_btn = gr.Button("🔍 搜索")
                        snippets_display = gr.HTML()
            
            # ===== Tab 4: 测验 =====
            with gr.Tab("📝 测验"):
                gr.Markdown("### 🎯 生成测试题")
                
                with gr.Row():
                    quiz_topic = gr.Textbox(label="测验主题", placeholder="例如：操作系统进程管理")
                    quiz_num = gr.Slider(label="题目数量", minimum=1, maximum=10, value=5, step=1)
                    quiz_diff = gr.Dropdown(label="难度", choices=["Easy", "Medium", "Hard"], value="Medium")
                
                generate_quiz_btn = gr.Button("🎲 生成测验", variant="primary")
                show_answers_btn = gr.Button("👁️ 显示答案")
                
                quiz_display = gr.HTML()
            
            # ===== Tab 5: 知识图谱 =====
            with gr.Tab("🕸️ 知识图谱"):
                gr.Markdown("### 概念关系网络")
                build_graph_btn = gr.Button("🔨 构建知识图谱", variant="primary")
                graph_display = gr.HTML()
            
            # ===== Tab 6: 闪卡复习 =====
            with gr.Tab("📇 闪卡"):
                with gr.Row():
                    with gr.Column(scale=1):
                        gr.Markdown("### 生成闪卡")
                        flashcard_content = gr.Textbox(label="学习内容", lines=8, placeholder="粘贴要制作闪卡的内容...")
                        flashcard_num = gr.Slider(label="卡片数量", minimum=1, maximum=20, value=5, step=1)
                        generate_cards_btn = gr.Button("🎴 生成闪卡", variant="primary")
                        card_status = gr.Textbox(label="状态", interactive=False)
                    
                    with gr.Column(scale=2):
                        gr.Markdown("### 复习模式")
                        start_review_btn = gr.Button("📚 开始复习", variant="primary")
                        flashcard_display = gr.HTML()
        
        # ============================================================
        # 事件绑定
        # ============================================================
        
        # 初始化
        init_btn.click(fn=initialize_system, outputs=[init_status])
        
        # 对话
        send_btn.click(
            fn=chat_with_all_features,
            inputs=[msg_input, img_input, file_input, chatbot, show_thinking_check, show_conf_check, socratic_check],
            outputs=[chatbot, thinking_display, conf_display, doc_preview_display, gr.HTML(visible=False), status_box]
        ).then(
            fn=lambda: ("", None, None),
            outputs=[msg_input, img_input, file_input]
        )
        
        msg_input.submit(
            fn=chat_with_all_features,
            inputs=[msg_input, img_input, file_input, chatbot, show_thinking_check, show_conf_check, socratic_check],
            outputs=[chatbot, thinking_display, conf_display, doc_preview_display, gr.HTML(visible=False), status_box]
        ).then(
            fn=lambda: ("", None, None),
            outputs=[msg_input, img_input, file_input]
        )
        
        clear_btn.click(fn=lambda: [], outputs=[chatbot])
        
        # 文档和热力图
        doc_list_btn.click(fn=show_document_list, outputs=[doc_list_display])
        heatmap_btn.click(fn=show_heatmap_ui, outputs=[heatmap_display])
        
        # 片段收藏
        save_snippet_btn.click(
            fn=save_snippet,
            inputs=[snippet_content, snippet_source, snippet_tags],
            outputs=[save_status, snippets_display]
        )
        
        search_btn.click(
            fn=search_snippets_ui,
            inputs=[search_query, search_tags, favorites_only],
            outputs=[snippets_display]
        )
        
        # 测验
        generate_quiz_btn.click(
            fn=generate_quiz_ui,
            inputs=[quiz_topic, quiz_num, quiz_diff],
            outputs=[quiz_display]
        )
        
        show_answers_btn.click(
            fn=show_quiz_answers,
            outputs=[quiz_display]
        )
        
        # 知识图谱
        build_graph_btn.click(fn=build_knowledge_graph_ui, outputs=[graph_display])
        
        # 闪卡
        generate_cards_btn.click(
            fn=generate_flashcards_ui,
            inputs=[flashcard_content, flashcard_num],
            outputs=[card_status, flashcard_display]
        )
        
        start_review_btn.click(fn=start_review_session, outputs=[flashcard_display])
    
    return app


# ============================================================
# 启动
# ============================================================
if __name__ == "__main__":
    app = build_complete_ui()
    app.queue()
    app.launch(
        server_name="0.0.0.0",
        server_port=7861,
        share=False,
        show_error=True
    )


