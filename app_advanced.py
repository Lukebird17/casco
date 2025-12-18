#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
高级学习辅助 UI
类似Gemini的现代化界面，包含：
- 双栏布局（文档预览 + 对话）
- 会话管理
- 流式输出
- 思维链显示
- 信源追踪
- 置信度显示
"""

import gradio as gr
from typing import List, Dict, Optional, Tuple
import json
from pathlib import Path

from rag_agent import RAGAgent
from session_manager import SessionManager
from confidence_calculator import ConfidenceCalculator
from multimodal_input_handler import MultimodalInputHandler
from config import TEXT_MODEL_NAME, MULTIMODAL_MODEL_NAME


# ============================================================
# 全局变量
# ============================================================
agent: Optional[RAGAgent] = None
session_manager: Optional[SessionManager] = None
confidence_calculator: Optional[ConfidenceCalculator] = None
multimodal_handler: Optional[MultimodalInputHandler] = None


# ============================================================
# 初始化
# ============================================================
def initialize_system():
    """初始化系统"""
    global agent, session_manager, confidence_calculator, multimodal_handler
    
    try:
        print("🚀 初始化高级学习辅助系统...")
        
        # 初始化RAG Agent
        agent = RAGAgent(
            model=TEXT_MODEL_NAME,
            text_model=TEXT_MODEL_NAME,
            multimodal_model=MULTIMODAL_MODEL_NAME,
            enable_tracking=True,
            enable_cot=True,
            use_multimodal=True
        )
        print(f"✅ RAG Agent 初始化完成")
        
        # 初始化会话管理器
        session_manager = SessionManager()
        print(f"✅ 会话管理器初始化完成")
        
        # 初始化置信度计算器
        confidence_calculator = ConfidenceCalculator()
        print(f"✅ 置信度计算器初始化完成")
        
        # 初始化多模态处理器
        multimodal_handler = MultimodalInputHandler()
        print(f"✅ 多模态处理器初始化完成")
        
        # 创建默认会话
        if not session_manager.sessions:
            session_manager.create_session("第一次对话")
            print(f"✅ 创建默认会话")
        else:
            # 切换到最新会话
            latest = list(session_manager.sessions.keys())[-1]
            session_manager.switch_session(latest)
            print(f"✅ 加载最新会话")
        
        return "✅ 系统初始化成功！"
    
    except Exception as e:
        import traceback
        error_msg = f"❌ 初始化失败: {str(e)}\n{traceback.format_exc()}"
        print(error_msg)
        return error_msg


# ============================================================
# 对话功能
# ============================================================
def chat_with_streaming(
    message: str,
    image: Optional[object],
    file: Optional[object],
    history: List[Dict],
    show_thinking: bool,
    show_confidence: bool
) -> Tuple:
    """
    对话功能（支持流式输出）
    
    Returns:
        (history, thinking_process, confidence_info, doc_preview, status)
    """
    global agent, session_manager, confidence_calculator, multimodal_handler
    
    if not agent or not session_manager:
        error = "❌ 系统未初始化"
        history.append({"role": "user", "content": message or "上传了内容"})
        history.append({"role": "assistant", "content": error})
        return history, "", "", "", error
    
    try:
        # 【步骤1】处理输入
        user_message = message if message else "请分析上传的内容"
        query_for_rag = user_message
        image_path = None
        file_content = None
        thinking_steps = []
        
        # 图片输入
        if image is not None:
            thinking_steps.append("📷 正在分析上传的图片...")
            print("\n" + thinking_steps[-1])
            
            image_result = multimodal_handler.handle_image_input(image, user_message)
            query_for_rag = image_result['enhanced_query']
            image_path = image_result['image_path']
            
            thinking_steps.append(f"✅ 图片分析完成：{image_result['image_description'][:50]}...")
        
        # 文件输入
        elif file is not None:
            thinking_steps.append(f"📄 正在读取文件: {file.name}...")
            print("\n" + thinking_steps[-1])
            
            file_result = multimodal_handler.handle_file_input(file.name, user_message)
            if file_result.get('error'):
                raise Exception(file_result['error'])
            
            query_for_rag = file_result['query']
            file_content = file_result['file_content']
            
            thinking_steps.append(f"✅ 文件读取完成（{len(file_content)} 字符）")
        
        # 【步骤2】检索
        thinking_steps.append("🔍 正在检索相关知识...")
        print("\n" + thinking_steps[-1])
        
        # 显示当前思维过程
        thinking_html = _format_thinking_process(thinking_steps)
        yield history, thinking_html, "", "", "检索中..."
        
        # 调用RAG
        result = agent.answer_question(
            query_for_rag,
            chat_history=history,
            image=image_path,
            file_content=file_content
        )
        
        # 提取结果
        if isinstance(result, dict):
            answer = result.get('answer', str(result))
            retrieved_docs = result.get('context', [])
            query_type = result.get('query_type', 'basic')
        else:
            answer = str(result)
            retrieved_docs = []
            query_type = 'basic'
        
        thinking_steps.append(f"✅ 检索完成，找到 {len(retrieved_docs) if isinstance(retrieved_docs, list) else '若干'} 个相关文档")
        
        # 【步骤3】生成答案
        thinking_steps.append("✍️ 正在生成答案...")
        thinking_html = _format_thinking_process(thinking_steps)
        yield history, thinking_html, "", "", "生成中..."
        
        # 【步骤4】计算置信度
        confidence_info = ""
        if show_confidence and confidence_calculator:
            thinking_steps.append("📊 正在计算置信度...")
            
            # 解析retrieved_docs
            docs_list = []
            if isinstance(retrieved_docs, list):
                docs_list = retrieved_docs
            elif isinstance(retrieved_docs, str):
                # 如果是字符串，尝试解析
                docs_list = []
            
            conf_result = confidence_calculator.calculate(
                query_for_rag, answer, docs_list, query_type
            )
            
            confidence_info = _format_confidence(conf_result)
            thinking_steps.append(f"✅ 置信度: {conf_result['emoji']} {conf_result['level']} ({conf_result['score']:.0%})")
        
        # 【步骤5】格式化文档预览
        doc_preview = _format_doc_preview(retrieved_docs if isinstance(retrieved_docs, list) else [])
        
        # 【步骤6】更新历史
        history.append({"role": "user", "content": user_message})
        history.append({"role": "assistant", "content": answer})
        
        # 保存到会话
        session_manager.add_message_to_current("user", user_message)
        session_manager.add_message_to_current("assistant", answer, {
            "confidence": conf_result if show_confidence else None,
            "retrieved_docs": len(retrieved_docs) if isinstance(retrieved_docs, list) else 0
        })
        
        # 最终结果
        thinking_steps.append("✅ 完成！")
        final_thinking = _format_thinking_process(thinking_steps) if show_thinking else ""
        
        yield history, final_thinking, confidence_info, doc_preview, "✅ 完成"
        
    except Exception as e:
        import traceback
        error_msg = f"❌ 错误: {str(e)}"
        print(f"\n{error_msg}\n{traceback.format_exc()}")
        
        history.append({"role": "user", "content": message or "上传了内容"})
        history.append({"role": "assistant", "content": error_msg})
        
        yield history, "", "", "", error_msg


def _format_thinking_process(steps: List[str]) -> str:
    """格式化思维过程"""
    html = '<div style="padding: 15px; background: #f8f9fa; border-radius: 8px; font-family: monospace;">'
    for i, step in enumerate(steps):
        html += f'<div style="margin: 8px 0; padding: 8px; background: white; border-left: 3px solid #6366f1; border-radius: 4px;">'
        html += f'<span style="color: #6366f1; font-weight: bold;">{i+1}.</span> {step}'
        html += '</div>'
    html += '</div>'
    return html


def _format_confidence(conf: Dict) -> str:
    """格式化置信度信息"""
    html = f'''
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
        <div style="margin-top: 20px; padding-top: 15px; border-top: 1px solid rgba(255,255,255,0.3);">
            <div style="font-size: 12px; margin: 5px 0;">
                🔍 检索质量: <strong>{conf['factors']['retrieval_quality']:.0%}</strong>
            </div>
            <div style="font-size: 12px; margin: 5px 0;">
                ✍️ 答案完整性: <strong>{conf['factors']['answer_completeness']:.0%}</strong>
            </div>
            <div style="font-size: 12px; margin: 5px 0;">
                📚 来源可靠性: <strong>{conf['factors']['source_reliability']:.0%}</strong>
            </div>
            <div style="font-size: 12px; margin: 5px 0;">
                🔗 一致性: <strong>{conf['factors']['consistency']:.0%}</strong>
            </div>
        </div>
    </div>
    '''
    return html


def _format_doc_preview(docs: List[Dict]) -> str:
    """格式化文档预览"""
    if not docs:
        return '<div style="padding: 20px; text-align: center; color: #999;">暂无引用文档</div>'
    
    html = '<div style="padding: 15px;">'
    html += f'<h3 style="color: #6366f1; margin-bottom: 15px;">📚 引用来源 ({len(docs)})</h3>'
    
    for i, doc in enumerate(docs[:5]):  # 最多显示5个
        content = doc.get('content', 'N/A')
        metadata = doc.get('metadata', {})
        
        filename = metadata.get('filename', metadata.get('source', '未知来源'))
        page = metadata.get('page', 'N/A')
        
        html += f'''
        <div style="margin: 10px 0; padding: 15px; background: #f8f9fa; border-left: 4px solid #6366f1; border-radius: 6px;">
            <div style="font-weight: bold; color: #6366f1; margin-bottom: 8px;">
                📄 {filename} - 第 {page} 页
            </div>
            <div style="font-size: 14px; color: #555; line-height: 1.6;">
                {content[:200]}{"..." if len(content) > 200 else ""}
            </div>
        </div>
        '''
    
    if len(docs) > 5:
        html += f'<div style="text-align: center; color: #999; margin-top: 10px;">还有 {len(docs) - 5} 个文档...</div>'
    
    html += '</div>'
    return html


# ============================================================
# 会话管理
# ============================================================
def create_new_session(title: str = "新对话"):
    """创建新会话"""
    global session_manager
    
    if not session_manager:
        return [], "❌ 系统未初始化"
    
    session = session_manager.create_session(title or "新对话")
    sessions_list = session_manager.list_sessions()
    
    return [], _format_sessions_list(sessions_list), f"✅ 创建新会话: {session.title}"


def switch_to_session(session_id: str):
    """切换会话"""
    global session_manager
    
    if not session_manager or not session_id:
        return [], "❌ 无效的会话"
    
    success = session_manager.switch_session(session_id)
    if success:
        session = session_manager.get_current_session()
        history = session.messages if session else []
        return history, f"✅ 已切换到: {session.title}"
    
    return [], "❌ 切换失败"


def delete_current_session():
    """删除当前会话"""
    global session_manager
    
    if not session_manager:
        return [], "", "❌ 系统未初始化"
    
    current = session_manager.get_current_session()
    if not current:
        return [], "", "❌ 没有当前会话"
    
    session_manager.delete_session(current.session_id)
    sessions_list = session_manager.list_sessions()
    
    new_current = session_manager.get_current_session()
    history = new_current.messages if new_current else []
    
    return history, _format_sessions_list(sessions_list), f"✅ 已删除会话"


def _format_sessions_list(sessions: List[Dict]) -> str:
    """格式化会话列表"""
    html = '<div style="padding: 10px;">'
    
    for session in sessions:
        html += f'''
        <div style="padding: 12px; margin: 8px 0; background: #f8f9fa; border-radius: 8px; cursor: pointer; transition: all 0.2s;"
             onmouseover="this.style.background='#e9ecef'" 
             onmouseout="this.style.background='#f8f9fa'"
             onclick="alert('Session: {session["session_id"]}')">
            <div style="font-weight: bold; color: #333; margin-bottom: 4px;">
                💬 {session['title']}
            </div>
            <div style="font-size: 12px; color: #666;">
                {session['updated_at']} · {session['message_count']} 条消息
            </div>
        </div>
        '''
    
    html += '</div>'
    return html


# ============================================================
# 构建UI
# ============================================================
def build_ui():
    """构建UI"""
    
    custom_css = """
    .gradio-container {
        font-family: 'Inter', sans-serif;
    }
    .main-container {
        max-width: 100% !important;
        padding: 0 !important;
    }
    .sidebar {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 12px;
        color: white;
    }
    .chat-container {
        height: 600px;
        overflow-y: auto;
    }
    .doc-preview {
        height: 600px;
        overflow-y: auto;
        border-left: 2px solid #e5e7eb;
        padding-left: 20px;
    }
    """
    
    with gr.Blocks(
        title="🎓 高级学习辅助系统",
        theme=gr.themes.Soft(primary_hue="indigo"),
        css=custom_css
    ) as app:
        
        # 标题
        gr.Markdown("""
        # 🎓 高级学习辅助系统
        ### 类似 Gemini 的智能学习助手 - 支持多模态、会话管理、置信度分析
        """)
        
        # 初始化状态
        with gr.Row():
            init_button = gr.Button("🚀 初始化系统", variant="primary", scale=1)
            init_status = gr.Textbox(label="状态", value="未初始化", scale=3, interactive=False)
        
        # 主布局：三栏
        with gr.Row():
            # 【左侧】会话列表 + 控制
            with gr.Column(scale=2):
                gr.Markdown("## 💬 会话管理")
                
                with gr.Row():
                    new_session_btn = gr.Button("➕ 新对话", size="sm")
                    delete_session_btn = gr.Button("🗑️ 删除", size="sm", variant="stop")
                
                sessions_display = gr.HTML(label="会话列表")
                
                gr.Markdown("### ⚙️ 显示选项")
                show_thinking = gr.Checkbox(label="显示思维过程", value=True)
                show_confidence = gr.Checkbox(label="显示置信度", value=True)
            
            # 【中间】对话区域（主要）
            with gr.Column(scale=5):
                chatbot = gr.Chatbot(
                    label="对话",
                    type="messages",
                    height=500,
                    bubble_full_width=False
                )
                
                with gr.Row():
                    message_input = gr.Textbox(
                        label="输入消息",
                        placeholder="输入你的问题...",
                        scale=6
                    )
                    image_input = gr.Image(label="上传图片", type="pil", scale=2)
                    file_input = gr.File(label="上传文件", scale=2)
                
                with gr.Row():
                    send_btn = gr.Button("📤 发送", variant="primary", scale=1)
                    clear_btn = gr.Button("🔄 清空", scale=1)
                
                status_text = gr.Textbox(label="状态", interactive=False)
            
            # 【右侧】文档预览 + 辅助信息
            with gr.Column(scale=3):
                gr.Markdown("## 📊 分析信息")
                
                with gr.Accordion("🧠 思维过程", open=True):
                    thinking_display = gr.HTML()
                
                with gr.Accordion("📈 置信度分析", open=True):
                    confidence_display = gr.HTML()
                
                with gr.Accordion("📚 引用文档", open=True):
                    doc_preview = gr.HTML()
        
        # ============================================================
        # 事件绑定
        # ============================================================
        
        # 初始化
        init_button.click(
            fn=initialize_system,
            outputs=[init_status]
        ).then(
            fn=lambda: session_manager.list_sessions() if session_manager else [],
            outputs=[sessions_display],
            queue=False
        )
        
        # 发送消息
        send_btn.click(
            fn=chat_with_streaming,
            inputs=[
                message_input,
                image_input,
                file_input,
                chatbot,
                show_thinking,
                show_confidence
            ],
            outputs=[
                chatbot,
                thinking_display,
                confidence_display,
                doc_preview,
                status_text
            ]
        ).then(
            fn=lambda: ("", None, None),
            outputs=[message_input, image_input, file_input],
            queue=False
        )
        
        # 回车发送
        message_input.submit(
            fn=chat_with_streaming,
            inputs=[
                message_input,
                image_input,
                file_input,
                chatbot,
                show_thinking,
                show_confidence
            ],
            outputs=[
                chatbot,
                thinking_display,
                confidence_display,
                doc_preview,
                status_text
            ]
        ).then(
            fn=lambda: ("", None, None),
            outputs=[message_input, image_input, file_input],
            queue=False
        )
        
        # 清空
        clear_btn.click(
            fn=lambda: [],
            outputs=[chatbot],
            queue=False
        )
        
        # 新建会话
        new_session_btn.click(
            fn=create_new_session,
            outputs=[chatbot, sessions_display, status_text]
        )
        
        # 删除会话
        delete_session_btn.click(
            fn=delete_current_session,
            outputs=[chatbot, sessions_display, status_text]
        )
    
    return app


# ============================================================
# 启动
# ============================================================
if __name__ == "__main__":
    app = build_ui()
    app.queue()  # 启用队列以支持流式输出
    app.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        show_error=True
    )





