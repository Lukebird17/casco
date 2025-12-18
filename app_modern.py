#!/usr/bin/env python3
"""
RAG Agent - 现代化UI界面
专业、简约、多模态交互
"""

import gradio as gr
from typing import List, Dict, Optional, Tuple
from datetime import datetime
from pathlib import Path
import os

from rag_agent import RAGAgent
from dynamic_db_manager import DynamicDBManager
from vector_store import VectorStore
from image_vector_store import ImageVectorStore
from multimodal_input_handler import MultimodalInputHandler
from config import MODEL_NAME

# ============================================================
# 全局变量
# ============================================================
agent: Optional[RAGAgent] = None
db_manager: Optional[DynamicDBManager] = None
multimodal_handler: Optional[MultimodalInputHandler] = None
current_db_path = "vector_db"
available_dbs = []

# ============================================================
# 自定义CSS - 简约专业风格
# ============================================================
CUSTOM_CSS = """
/* 全局样式 */
#app-container {
    font-family: 'Inter', 'SF Pro Display', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* 移除默认的大块色块 */
.gradio-container {
    background: linear-gradient(135deg, #f5f7fa 0%, #ffffff 100%) !important;
}

/* 主标题样式 */
#main-title {
    font-size: 2rem;
    font-weight: 700;
    background: linear-gradient(120deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    padding: 1.5rem 0;
    margin-bottom: 1rem;
    border-bottom: 1px solid #e1e8ed;
}

/* 卡片样式 */
.card {
    background: rgba(255, 255, 255, 0.9);
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
    border: 1px solid rgba(0, 0, 0, 0.06);
    padding: 1.2rem;
    margin: 0.8rem 0;
    transition: all 0.3s ease;
}

.card:hover {
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
    transform: translateY(-2px);
}

/* 聊天窗口样式 */
.chatbot-container {
    border-radius: 12px;
    border: 1px solid #e1e8ed;
    background: white;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.05);
}

/* 输入框样式 */
.input-box {
    border-radius: 8px;
    border: 1px solid #e1e8ed;
    padding: 0.8rem;
    background: white;
    transition: all 0.2s ease;
}

.input-box:focus {
    border-color: #667eea;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

/* 按钮样式 */
.primary-btn {
    background: linear-gradient(120deg, #667eea 0%, #764ba2 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.7rem 1.5rem !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 2px 8px rgba(102, 126, 234, 0.3) !important;
}

.primary-btn:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4) !important;
}

.secondary-btn {
    background: white !important;
    color: #667eea !important;
    border: 1px solid #667eea !important;
    border-radius: 8px !important;
    padding: 0.7rem 1.5rem !important;
    font-weight: 500 !important;
    transition: all 0.2s ease !important;
}

.secondary-btn:hover {
    background: #f5f7ff !important;
}

/* 侧边栏样式 */
.sidebar {
    background: rgba(255, 255, 255, 0.95);
    border-radius: 12px;
    border: 1px solid #e1e8ed;
    padding: 1.5rem;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
}

/* 统计信息样式 */
.stats-box {
    background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%);
    border-radius: 8px;
    padding: 0.8rem;
    margin: 0.5rem 0;
    border-left: 3px solid #667eea;
}

/* 开关和选择框样式 */
.gr-checkbox, .gr-radio {
    border-radius: 6px;
}

/* 标签样式 */
label {
    font-weight: 500;
    color: #2d3748;
    font-size: 0.9rem;
    margin-bottom: 0.4rem;
}

/* 文件上传区域 */
.file-upload {
    border: 2px dashed #cbd5e0;
    border-radius: 8px;
    padding: 2rem;
    text-align: center;
    background: #fafbfc;
    transition: all 0.2s ease;
}

.file-upload:hover {
    border-color: #667eea;
    background: #f5f7ff;
}

/* 隐藏不必要的元素 */
.footer {
    display: none !important;
}

/* 响应式设计 */
@media (max-width: 768px) {
    #main-title {
        font-size: 1.5rem;
    }
}
"""

# ============================================================
# 初始化函数
# ============================================================

def scan_available_dbs():
    """扫描可用的向量数据库"""
    dbs = []
    
    # 默认数据库
    if os.path.exists("vector_db"):
        dbs.append(("默认数据库", "vector_db"))
    
    # 扫描其他数据库目录
    for item in Path(".").glob("*_vector_db"):
        if item.is_dir():
            dbs.append((item.name, str(item)))
    
    return dbs if dbs else [("默认数据库", "vector_db")]


def initialize_system(db_path: str = "vector_db"):
    """初始化系统（自动执行）"""
    global agent, db_manager, multimodal_handler, current_db_path, available_dbs
    
    try:
        # 扫描可用数据库
        available_dbs = scan_available_dbs()
        current_db_path = db_path
        
        # 初始化向量存储
        vector_store = VectorStore(db_path=db_path)
        image_vector_store = ImageVectorStore()
        
        # 初始化 RAG Agent（启用多模态）
        agent = RAGAgent(
            model=MODEL_NAME,
            enable_tracking=True,
            enable_cot=True,
            use_multimodal=True  # 正确的参数名
        )
        
        # 初始化数据库管理器
        db_manager = DynamicDBManager(vector_store)
        
        # 初始化多模态输入处理器
        multimodal_handler = MultimodalInputHandler(
            image_store=image_vector_store,
            text_store=vector_store
        )
        
        # 获取统计信息
        doc_count = vector_store.collection.count()
        img_count = image_vector_store.collection.count()
        
        return (
            f"✅ 系统已就绪 | 文档: {doc_count} | 图片: {img_count}",
            gr.update(choices=[name for name, _ in available_dbs], value="默认数据库")
        )
    except Exception as e:
        return f"❌ 初始化失败: {str(e)}", gr.update(choices=["默认数据库"])


# ============================================================
# 对话功能
# ============================================================

def chat(
    message: str,
    image: Optional[object],
    file: Optional[object],
    history: List[Dict],
    show_reasoning: bool,
    show_tokens: bool
) -> Tuple:
    """多模态聊天"""
    global agent, multimodal_handler
    
    if agent is None or multimodal_handler is None:
        error_msg = "❌ 系统未初始化"
        history.append({"role": "user", "content": message or "上传了文件/图片"})
        history.append({"role": "assistant", "content": error_msg})
        return history, "", "", ""
    
    try:
        # 构建用户输入
        user_message = message if message else "请分析上传的内容"
        query_for_rag = user_message  # 用于检索的查询
        image_path = None  # 图片路径（传给多模态模型）
        file_content = None  # 文件内容（传给多模态模型）
        
        # 【1. 图片输入】使用多模态模型
        if image is not None:
            print("\n📷 处理用户上传的图片...")
            image_result = multimodal_handler.handle_image_input(
                image=image,
                text_query=user_message
            )
            
            # 使用增强后的query进行检索
            query_for_rag = image_result['enhanced_query']
            image_path = image_result['image_path']
            
            print(f"   ✅ 图片已保存: {image_path}")
            print(f"   ✅ 图片描述: {image_result['image_description'][:50]}...")
        
        # 【2. 文件输入】使用多模态模型
        elif file is not None:
            print("\n📄 处理用户上传的文件...")
            file_result = multimodal_handler.handle_file_input(
                file_path=file.name,
                text_query=user_message
            )
            
            if file_result.get('error'):
                raise Exception(file_result['error'])
            
            # 使用原始query检索，文件内容直接传给LLM
            query_for_rag = file_result['query']
            file_content = file_result['file_content']
            
            print(f"   ✅ 文件: {file_result['file_name']}")
            print(f"   ✅ 内容长度: {len(file_content)} 字符")
        
        # 【3. 生成回答】
        # 纯文本：使用文本模型
        # 图片/文件：使用多模态模型
        result = agent.answer_question(
            query_for_rag, 
            chat_history=history,
            image=image_path,
            file_content=file_content
        )
        
        # 提取答案
        if isinstance(result, dict):
            answer = result.get('answer', str(result))
        else:
            answer = str(result)
        
        # 更新历史
        history.append({"role": "user", "content": user_message})
        history.append({"role": "assistant", "content": answer})
        
        # 获取推理链和token统计
        reasoning = ""
        tokens = ""
        
        if show_reasoning and agent.get_reasoning_chain():
            reasoning = agent.get_reasoning_chain().format_chain(detailed=True)
        
        if show_tokens:
            tokens = agent.get_token_report()
        
        return history, reasoning, tokens, ""
        
    except Exception as e:
        import traceback
        error_msg = f"❌ 错误: {str(e)}"
        print(f"\n{error_msg}")
        print(traceback.format_exc())
        history.append({"role": "user", "content": message or "上传了文件/图片"})
        history.append({"role": "assistant", "content": error_msg})
        return history, "", "", ""


# ============================================================
# 数据库管理功能
# ============================================================

def switch_database(db_name: str):
    """切换数据库"""
    global agent, db_manager, current_db_path
    
    # 查找对应的路径
    db_path = None
    for name, path in available_dbs:
        if name == db_name:
            db_path = path
            break
    
    if db_path is None:
        return "❌ 数据库不存在"
    
    try:
        # 重新初始化
        status, _ = initialize_system(db_path)
        return status
    except Exception as e:
        return f"❌ 切换失败: {str(e)}"


def create_new_database(db_name: str):
    """创建新数据库"""
    if not db_name or not db_name.strip():
        return "❌ 请输入数据库名称", gr.update()
    
    db_path = f"{db_name}_vector_db"
    
    if os.path.exists(db_path):
        return f"❌ 数据库 {db_name} 已存在", gr.update()
    
    try:
        # 创建新数据库
        os.makedirs(db_path, exist_ok=True)
        
        # 刷新列表
        global available_dbs
        available_dbs = scan_available_dbs()
        
        return (
            f"✅ 数据库 {db_name} 创建成功",
            gr.update(choices=[name for name, _ in available_dbs])
        )
    except Exception as e:
        return f"❌ 创建失败: {str(e)}", gr.update()


def add_file_to_db(file, course_name: str, use_ocr: bool):
    """添加文件到数据库"""
    global db_manager
    
    if db_manager is None:
        return "❌ 系统未初始化"
    
    if file is None:
        return "❌ 请选择文件"
    
    try:
        result = db_manager.add_file(
            file_path=file.name,
            course_name=course_name or "默认课程",
            use_ocr=use_ocr
        )
        
        if result.get('success'):
            return f"✅ 添加成功: {result.get('filename')} ({result.get('chunks_added', 0)} 个文档块)"
        else:
            return f"❌ 添加失败: {result.get('error')}"
            
    except Exception as e:
        return f"❌ 错误: {str(e)}"


# ============================================================
# Gradio UI
# ============================================================

def create_ui():
    """创建现代化UI"""
    
    with gr.Blocks(
        title="RAG Agent - 智能文档助手",
        css=CUSTOM_CSS,
        theme=gr.themes.Soft(
            primary_hue="indigo",
            secondary_hue="purple",
            neutral_hue="slate",
            font=["Inter", "sans-serif"]
        ),
        elem_id="app-container",
        head="""
        <link rel="icon" type="image/svg+xml" href="/file/assets/favicon.svg">
        """
    ) as app:
        
        # 标题和Logo
        with gr.Row():
            with gr.Column(scale=1):
                gr.Image(
                    value="assets/logo.svg",
                    width=80,
                    height=80,
                    show_label=False,
                    container=False,
                    interactive=False
                )
            with gr.Column(scale=9):
                gr.HTML("""
                    <div id="main-title">
                        <span>RAG Agent</span>
                        <div style="font-size: 0.9rem; font-weight: 400; color: #64748b; margin-top: 0.5rem;">
                            智能多模态文档助手 | Retrieval-Augmented Generation
                        </div>
                    </div>
                """)
        
        # 主布局
        with gr.Row():
            # 左侧：主交互区域（70%）
            with gr.Column(scale=7):
                # 状态栏
                status_display = gr.Markdown("🔄 正在初始化系统...", elem_classes="stats-box")
                
                # 聊天窗口
                chatbot = gr.Chatbot(
                    label="💬 对话窗口",
                    height=500,
                    type="messages",
                    elem_classes="chatbot-container",
                    show_label=False
                )
                
                # 输入区域
                with gr.Row():
                    with gr.Column(scale=8):
                        message_input = gr.Textbox(
                            label="",
                            placeholder="💬 输入问题，或上传图片/文件...",
                            lines=2,
                            elem_classes="input-box",
                            show_label=False
                        )
                    with gr.Column(scale=2):
                        send_btn = gr.Button("📤 发送", variant="primary", elem_classes="primary-btn")
                        clear_btn = gr.Button("🗑️ 清空", elem_classes="secondary-btn")
                
                # 多模态输入
                with gr.Row():
                    image_input = gr.Image(
                        label="📷 上传图片",
                        type="pil",
                        elem_classes="file-upload"
                    )
                    file_input = gr.File(
                        label="📎 上传文件",
                        elem_classes="file-upload"
                    )
                
                # 可选信息显示区域
                with gr.Accordion("🔍 详细信息", open=False):
                    reasoning_output = gr.Textbox(
                        label="💭 推理过程",
                        lines=5,
                        interactive=False
                    )
                    token_output = gr.Textbox(
                        label="📊 Token统计",
                        lines=3,
                        interactive=False
                    )
            
            # 右侧：管理面板（30%）
            with gr.Column(scale=3, elem_classes="sidebar"):
                gr.Markdown("### ⚙️ 系统管理")
                
                # 数据库选择
                with gr.Group(elem_classes="card"):
                    gr.Markdown("#### 📚 向量数据库")
                    db_selector = gr.Dropdown(
                        label="当前数据库",
                        choices=["默认数据库"],
                        value="默认数据库",
                        interactive=True
                    )
                    switch_btn = gr.Button("🔄 切换", size="sm", elem_classes="secondary-btn")
                    switch_status = gr.Markdown("")
                
                # 创建新数据库
                with gr.Group(elem_classes="card"):
                    gr.Markdown("#### ➕ 创建数据库")
                    new_db_name = gr.Textbox(
                        label="数据库名称",
                        placeholder="输入名称...",
                        scale=3
                    )
                    create_db_btn = gr.Button("创建", size="sm", elem_classes="primary-btn")
                    create_status = gr.Markdown("")
                
                # 添加文件
                with gr.Group(elem_classes="card"):
                    gr.Markdown("#### 📁 添加文件")
                    file_upload = gr.File(label="选择文件")
                    course_input = gr.Textbox(
                        label="课程标签",
                        placeholder="如：操作系统",
                        value="默认课程"
                    )
                    use_ocr_check = gr.Checkbox(
                        label="使用OCR（PDF/DOCX/PPTX）",
                        value=True
                    )
                    add_file_btn = gr.Button("添加", size="sm", elem_classes="primary-btn")
                    add_status = gr.Markdown("")
                
                # 显示选项
                with gr.Group(elem_classes="card"):
                    gr.Markdown("#### 🎛️ 显示选项")
                    show_reasoning = gr.Checkbox(label="显示推理过程", value=False)
                    show_tokens = gr.Checkbox(label="显示Token统计", value=False)
        
        # ============================================================
        # 事件绑定
        # ============================================================
        
        # 自动初始化
        app.load(
            fn=initialize_system,
            outputs=[status_display, db_selector]
        )
        
        # 发送消息
        send_btn.click(
            fn=chat,
            inputs=[
                message_input,
                image_input,
                file_input,
                chatbot,
                show_reasoning,
                show_tokens
            ],
            outputs=[chatbot, reasoning_output, token_output, message_input]
        )
        
        # 清空对话
        clear_btn.click(
            fn=lambda: ([], "", "", None, None),
            outputs=[chatbot, reasoning_output, token_output, image_input, file_input]
        )
        
        # 切换数据库
        switch_btn.click(
            fn=switch_database,
            inputs=[db_selector],
            outputs=[switch_status]
        )
        
        # 创建数据库
        create_db_btn.click(
            fn=create_new_database,
            inputs=[new_db_name],
            outputs=[create_status, db_selector]
        )
        
        # 添加文件
        add_file_btn.click(
            fn=add_file_to_db,
            inputs=[file_upload, course_input, use_ocr_check],
            outputs=[add_status]
        )
    
    return app


# ============================================================
# 启动应用
# ============================================================

if __name__ == "__main__":
    app = create_ui()
    app.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        show_error=True
    )

