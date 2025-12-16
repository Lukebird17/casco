#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
智能课程助教 - 完整增强版Gradio界面
集成所有功能：OCR、动态数据库、多模态输入、历史对话、置信度评估
"""

import gradio as gr
import os
import json
from datetime import datetime
from typing import List, Tuple, Optional, Dict
from PIL import Image

from rag_agent import RAGAgent
from dynamic_db_manager import DynamicDBManager
from enhanced_ocr import EnhancedOCRProcessor
from config import MODEL_NAME, VECTOR_DB_PATH


# 全局变量
agent = None
db_manager = None
ocr_processor = None
chat_history_sessions = {}
current_session_id = None


def initialize_system():
    """初始化系统"""
    global agent, db_manager, ocr_processor
    
    try:
        # 初始化RAG Agent
        agent = RAGAgent(
            model=MODEL_NAME,
            enable_tracking=True,
            enable_cot=True
        )
        
        # 初始化数据库管理器
        db_manager = DynamicDBManager(agent.vector_store)
        
        # 初始化OCR处理器
        ocr_processor = EnhancedOCRProcessor(ocr_engine="paddleocr")
        
        # 统计信息
        stats = db_manager.get_statistics()
        count = agent.vector_store.get_collection_count()
        
        return f"""✅ 系统初始化成功！

📊 知识库统计:
  • 总文档片段: {count}
  • 课程数量: {stats['total_courses']}
  • 文件数量: {stats['total_files']}

🔧 功能模块:
  ✓ RAG智能检索
  ✓ Auto-CoT推理
  ✓ Token追踪优化
  ✓ 答案质量检查
  ✓ OCR图文识别
  ✓ 动态数据库管理
  ✓ 多模态输入
"""
    except Exception as e:
        return f"❌ 初始化失败: {str(e)}"


def chat_with_text(
    message: str,
    history: List[Dict],
    enable_reasoning: bool,
    enable_token: bool,
    max_retries: int,
    selected_course: str = "全部课程"
) -> Tuple:
    """
    文本对话接口（使用Gradio 4.0+的消息格式）
    """
    global agent, current_session_id, chat_history_sessions
    
    if agent is None:
        return "❌ 系统未初始化", history, "", "", ""
    
    # 创建会话
    if current_session_id is None:
        current_session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        chat_history_sessions[current_session_id] = []
    
    try:
        # 准备对话历史（从消息格式转换）
        chat_hist = []
        for msg in history:
            if isinstance(msg, dict) and "role" in msg:
                chat_hist.append(msg)
        
        # 生成回答
        answer = agent.answer_question(
            message,
            chat_history=chat_hist,
            max_retries=max_retries
        )
        
        # 保存历史
        chat_history_sessions[current_session_id].append({
            "user": message,
            "assistant": answer,
            "timestamp": datetime.now().isoformat()
        })
        
        # 添加到历史（消息格式）
        history.append({"role": "user", "content": message})
        history.append({"role": "assistant", "content": answer})
        
        # 获取推理链
        reasoning_text = ""
        if enable_reasoning and agent.get_reasoning_chain():
            reasoning_text = agent.get_reasoning_chain().format_chain(detailed=True)
        
        # 获取Token统计
        token_text = ""
        if enable_token:
            token_text = agent.get_token_report()
        
        # 计算置信度
        confidence_text = calculate_confidence(answer, agent)
        
        return answer, history, reasoning_text, token_text, confidence_text
        
    except Exception as e:
        error_msg = f"❌ 错误: {str(e)}"
        history.append({"role": "user", "content": message})
        history.append({"role": "assistant", "content": error_msg})
        return error_msg, history, "", "", ""


def chat_with_image(
    image: Image.Image,
    question: str,
    history: List[Dict],
    enable_reasoning: bool,
    enable_token: bool
) -> Tuple:
    """
    图片对话接口（多模态输入）
    """
    global agent, ocr_processor
    
    if agent is None:
        return "❌ 系统未初始化", history, "", "", ""
    
    if image is None:
        return "❌ 请上传图片", history, "", "", ""
    
    try:
        # OCR识别图片
        import io
        img_bytes = io.BytesIO()
        image.save(img_bytes, format='PNG')
        img_bytes = img_bytes.getvalue()
        
        ocr_text = ocr_processor._ocr_image(img_bytes)
        
        # 构造增强问题
        enhanced_question = f"""{question}

【图片OCR识别内容】
{ocr_text}

请结合图片内容和知识库信息回答问题。"""
        
        # 调用文本对话
        return chat_with_text(
            enhanced_question,
            history,
            enable_reasoning,
            enable_token,
            max_retries=2
        )
        
    except Exception as e:
        error_msg = f"❌ 图片处理失败: {str(e)}"
        history.append({"role": "user", "content": question})
        history.append({"role": "assistant", "content": error_msg})
        return error_msg, history, "", "", ""


def add_file_to_db(
    file,
    course_name: str,
    use_ocr: bool
) -> str:
    """添加文件到数据库"""
    global db_manager
    
    if db_manager is None:
        return "❌ 系统未初始化"
    
    if file is None:
        return "❌ 请选择文件"
    
    if not course_name:
        return "❌ 请输入课程名称"
    
    try:
        result = db_manager.add_file(
            file.name,
            course_name,
            use_ocr
        )
        
        if result['success']:
            return f"""✅ 文件添加成功！

📄 文件名: {result['filename']}
📚 课程: {result['course']}
📊 文本块数: {result['chunks']}
🔑 文件哈希: {result['file_hash'][:8]}...

数据库已更新，可以立即查询相关内容。"""
        else:
            return f"❌ 添加失败: {result.get('error', '未知错误')}"
    
    except Exception as e:
        return f"❌ 处理失败: {str(e)}"


def add_directory_to_db(
    directory_path: str,
    course_name: str,
    use_ocr: bool
) -> str:
    """批量添加目录到数据库"""
    global db_manager
    
    if db_manager is None:
        return "❌ 系统未初始化"
    
    if not directory_path or not os.path.exists(directory_path):
        return "❌ 目录不存在"
    
    if not course_name:
        return "❌ 请输入课程名称"
    
    try:
        result = db_manager.add_directory(
            directory_path,
            course_name,
            use_ocr
        )
        
        return f"""✅ 批量处理完成！

📊 统计:
  • 总计: {result['total']} 个文件
  • 成功: {result['success']} 个
  • 失败: {result['failed']} 个
  • 跳过: {result['skipped']} 个

数据库已更新。"""
    
    except Exception as e:
        return f"❌ 处理失败: {str(e)}"


def get_db_statistics() -> str:
    """获取数据库统计"""
    global db_manager
    
    if db_manager is None:
        return "系统未初始化"
    
    try:
        stats = db_manager.get_statistics()
        
        output = [
            "╔══════════════════════════════════════════════════════╗",
            "║                数据库统计信息                         ║",
            "╚══════════════════════════════════════════════════════╝",
            "",
            "【总体统计】",
            f"  • 课程总数: {stats['total_courses']}",
            f"  • 文件总数: {stats['total_files']}",
            f"  • 文档块总数: {stats['total_chunks']}",
            "",
            "【课程详情】"
        ]
        
        for course_name, course_info in stats['courses'].items():
            output.append(f"\n  📚 {course_name}")
            output.append(f"     文件数: {course_info['files']}")
            output.append(f"     文档块: {course_info['chunks']}")
        
        return "\n".join(output)
    
    except Exception as e:
        return f"获取统计失败: {str(e)}"


def list_all_courses() -> str:
    """列出所有课程"""
    global db_manager
    
    if db_manager is None:
        return "系统未初始化"
    
    try:
        courses = db_manager.list_courses()
        
        if not courses:
            return "📝 数据库中暂无课程"
        
        output = ["📚 课程列表:\n"]
        for course_name, course_info in courses.items():
            output.append(f"  • {course_name}")
            output.append(f"    文件: {', '.join(course_info['files'][:3])}")
            if len(course_info['files']) > 3:
                output.append(f"    还有 {len(course_info['files']) - 3} 个文件...")
            output.append(f"    文档块: {course_info['doc_count']}\n")
        
        return "\n".join(output)
    
    except Exception as e:
        return f"获取课程列表失败: {str(e)}"


def calculate_confidence(answer: str, agent: RAGAgent) -> str:
    """计算答案置信度"""
    try:
        reasoning = agent.get_reasoning_chain()
        
        if reasoning:
            reasoning_conf = reasoning.get_average_confidence()
            quality_pass = agent.check_answer_quality(answer, "")
            quality_score = 0.9 if quality_pass else 0.5
            
            length = len(answer)
            if 50 <= length <= 500:
                length_score = 1.0
            elif length < 50:
                length_score = 0.6
            else:
                length_score = 0.8
            
            total_confidence = (
                reasoning_conf * 0.5 +
                quality_score * 0.3 +
                length_score * 0.2
            )
            
            confidence_bar = "█" * int(total_confidence * 20) + "░" * (20 - int(total_confidence * 20))
            
            result = f"""
╔══════════════════════════════════════════════════════╗
║                  答案置信度评估                       ║
╚══════════════════════════════════════════════════════╝

【总体置信度】
  {confidence_bar} {total_confidence:.1%}

【详细评分】
  • 推理链置信度:  {reasoning_conf:.1%}
  • 答案质量:      {quality_score:.1%}
  • 答案长度:      {length_score:.1%}

【推理统计】
  • 推理步骤数: {len(reasoning.steps)}
  • 平均置信度: {reasoning_conf:.1%}
  • 推理耗时: {reasoning.get_duration():.2f} 秒

【置信度说明】
  • 90%+ : 高置信度，答案可靠
  • 70%-90% : 中等置信度，答案基本可信
  • 50%-70% : 低置信度，建议人工复核
  • <50% : 不确定，可能不准确
"""
            return result
        else:
            return "暂无推理链数据"
    
    except Exception as e:
        return f"计算置信度时出错: {str(e)}"


# 创建Gradio界面
def create_enhanced_ui():
    """创建完整增强版UI"""
    
    with gr.Blocks(title="智能课程助教 - 完整增强版") as demo:
        
        gr.Markdown("""
        # 🎓 智能课程助教系统 - 完整增强版
        
        **✨ 核心功能：**
        - 🔍 智能检索 + 多查询增强
        - 🧠 Auto-CoT推理
        - 📊 推理链记录 + Token追踪
        - ✅ 答案质量检查 + 置信度评估
        - 🖼️ OCR图文识别（PDF/DOCX/PPTX）
        - 📁 动态数据库管理（按课程标签）
        - 🎨 多模态输入（文本+图片）
        - 💬 历史对话记录
        """)
        
        # 初始化按钮
        with gr.Row():
            init_btn = gr.Button("🚀 初始化系统", variant="primary", scale=2)
            stats_btn = gr.Button("📊 数据库统计", scale=1)
            courses_btn = gr.Button("📚 课程列表", scale=1)
        
        init_output = gr.Textbox(label="系统信息", lines=6)
        
        # 主界面tabs
        with gr.Tabs():
            
            # Tab 1: 文本对话
            with gr.Tab("💬 文本对话"):
                with gr.Row():
                    with gr.Column(scale=2):
                        chatbot = gr.Chatbot(
                            label="对话窗口",
                            height=600,
                            elem_id="chatbot"
                        )
                        
                        with gr.Row():
                            msg = gr.Textbox(
                                label="输入问题",
                                placeholder="请输入你的问题...",
                                scale=4,
                                lines=2
                            )
                            submit_btn = gr.Button("📤 发送", variant="primary", scale=1)
                        
                        with gr.Row():
                            clear_btn = gr.Button("🗑️ 清空对话")
                            retry_slider = gr.Slider(1, 5, value=2, step=1, label="最大重试次数")
                    
                    with gr.Column(scale=1):
                        gr.Markdown("### ⚙️ 设置")
                        enable_reasoning_text = gr.Checkbox(label="显示推理链", value=True)
                        enable_token_text = gr.Checkbox(label="显示Token统计", value=True)
                        
                        gr.Markdown("### 📌 示例问题")
                        gr.Examples(
                            examples=[
                                "什么是词向量？",
                                "BERT和GPT有什么区别？",
                                "解释Transformer的自注意力机制",
                                "如何计算词向量相似度？",
                                "什么是预训练语言模型？"
                            ],
                            inputs=msg
                        )
            
            # Tab 2: 图片对话（多模态）
            with gr.Tab("🎨 图片对话"):
                with gr.Row():
                    with gr.Column():
                        image_input = gr.Image(label="上传图片", type="pil")
                        image_question = gr.Textbox(
                            label="关于图片的问题",
                            placeholder="例如：这张图片中的公式是什么意思？",
                            lines=2
                        )
                        image_submit = gr.Button("🖼️ 提交图片问题", variant="primary")
                        
                        gr.Markdown("""
                        **使用说明：**
                        1. 上传包含文字或公式的图片
                        2. 输入关于图片的问题
                        3. 系统会自动OCR识别图片内容
                        4. 结合知识库给出回答
                        """)
                    
                    with gr.Column():
                        image_chatbot = gr.Chatbot(label="图片对话", height=400)
                        enable_reasoning_img = gr.Checkbox(label="显示推理链", value=False)
                        enable_token_img = gr.Checkbox(label="显示Token统计", value=False)
            
            # Tab 3: 数据库管理
            with gr.Tab("📁 数据库管理"):
                gr.Markdown("### 添加文件到知识库")
                
                with gr.Row():
                    with gr.Column():
                        gr.Markdown("#### 单个文件添加")
                        file_input = gr.File(label="选择文件")
                        course_name_single = gr.Textbox(
                            label="课程名称",
                            placeholder="例如：自然语言处理"
                        )
                        use_ocr_single = gr.Checkbox(label="使用OCR识别图片", value=False)
                        add_file_btn = gr.Button("➕ 添加文件", variant="primary")
                        file_result = gr.Textbox(label="处理结果", lines=8)
                    
                    with gr.Column():
                        gr.Markdown("#### 批量目录添加")
                        dir_path = gr.Textbox(
                            label="目录路径",
                            placeholder="例如：data/NLP-Slides"
                        )
                        course_name_batch = gr.Textbox(
                            label="课程名称",
                            placeholder="例如：自然语言处理"
                        )
                        use_ocr_batch = gr.Checkbox(label="使用OCR识别图片", value=False)
                        add_dir_btn = gr.Button("📂 批量添加", variant="primary")
                        dir_result = gr.Textbox(label="处理结果", lines=8)
            
            # Tab 4: 推理链
            with gr.Tab("🔍 推理链"):
                reasoning_output = gr.Textbox(
                    label="推理过程详情",
                    lines=25,
                    elem_classes="output-text"
                )
            
            # Tab 5: Token统计
            with gr.Tab("💰 Token统计"):
                token_output = gr.Textbox(
                    label="Token使用报告",
                    lines=25,
                    elem_classes="output-text"
                )
            
            # Tab 6: 置信度
            with gr.Tab("📈 置信度评估"):
                confidence_output = gr.Textbox(
                    label="答案置信度分析",
                    lines=25,
                    elem_classes="output-text"
                )
            
            # Tab 7: 系统状态
            with gr.Tab("📊 系统状态"):
                status_output = gr.Textbox(
                    label="数据库统计",
                    lines=20,
                    elem_classes="output-text"
                )
                refresh_btn = gr.Button("🔄 刷新统计")
        
        # 事件绑定
        init_btn.click(
            fn=initialize_system,
            outputs=init_output
        )
        
        stats_btn.click(
            fn=get_db_statistics,
            outputs=init_output
        )
        
        courses_btn.click(
            fn=list_all_courses,
            outputs=init_output
        )
        
        # 文本对话
        submit_btn.click(
            fn=chat_with_text,
            inputs=[msg, chatbot, enable_reasoning_text, enable_token_text, retry_slider],
            outputs=[init_output, chatbot, reasoning_output, token_output, confidence_output]
        ).then(lambda: "", outputs=msg)
        
        msg.submit(
            fn=chat_with_text,
            inputs=[msg, chatbot, enable_reasoning_text, enable_token_text, retry_slider],
            outputs=[init_output, chatbot, reasoning_output, token_output, confidence_output]
        ).then(lambda: "", outputs=msg)
        
        clear_btn.click(
            fn=lambda: ([], "", "", ""),
            outputs=[chatbot, reasoning_output, token_output, confidence_output]
        )
        
        # 图片对话
        image_submit.click(
            fn=chat_with_image,
            inputs=[image_input, image_question, image_chatbot, enable_reasoning_img, enable_token_img],
            outputs=[init_output, image_chatbot, reasoning_output, token_output, confidence_output]
        )
        
        # 数据库管理
        add_file_btn.click(
            fn=add_file_to_db,
            inputs=[file_input, course_name_single, use_ocr_single],
            outputs=file_result
        )
        
        add_dir_btn.click(
            fn=add_directory_to_db,
            inputs=[dir_path, course_name_batch, use_ocr_batch],
            outputs=dir_result
        )
        
        refresh_btn.click(
            fn=get_db_statistics,
            outputs=status_output
        )
        
        gr.Markdown("""
        ---
        **💡 功能说明:**
        
        - **文本对话**: 标准的智能问答，支持多轮对话
        - **图片对话**: 上传图片，OCR识别后结合知识库回答
        - **数据库管理**: 动态添加文件和目录到知识库，支持课程标签分类
        - **推理链**: 查看完整的推理过程，包括检索、分析、生成等步骤
        - **Token统计**: 详细的Token使用统计和成本估算
        - **置信度评估**: 基于多个维度评估答案的可靠性
        - **系统状态**: 查看数据库统计和课程列表
        
        **🔧 技术特性:**
        - RAG检索增强生成
        - Auto-CoT推理
        - OCR图文识别（PDF/DOCX/PPTX）
        - 动态数据库（ChromaDB）
        - 多模态输入支持
        - 答案质量自动检查
        - Token优化和追踪
        
        **📦 由 OpenAI API + ChromaDB + PaddleOCR + Gradio 驱动**
        """)
    
    return demo


if __name__ == "__main__":
    custom_css = """
    .gradio-container {
        font-family: 'Arial', 'Microsoft YaHei', sans-serif;
    }
    #chatbot {
        height: 600px;
    }
    .output-text {
        font-family: 'Courier New', monospace;
        font-size: 13px;
    }
    """
    
    demo = create_enhanced_ui()
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        show_error=True
    )

