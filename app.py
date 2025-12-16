#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
智能课程助教 - Gradio Web界面
功能完善、美观的UI
"""

import gradio as gr
import os
import json
from datetime import datetime
from typing import List, Tuple, Optional, Dict

from rag_agent import RAGAgent
from config import MODEL_NAME, VECTOR_DB_PATH


class ChatHistory:
    """对话历史管理器"""
    
    def __init__(self):
        self.sessions = {}  # session_id -> messages
        self.current_session = None
    
    def create_session(self) -> str:
        """创建新会话"""
        session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.sessions[session_id] = []
        self.current_session = session_id
        return session_id
    
    def add_message(self, session_id: str, role: str, content: str):
        """添加消息"""
        if session_id not in self.sessions:
            self.sessions[session_id] = []
        self.sessions[session_id].append({
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat()
        })
    
    def get_messages(self, session_id: str) -> List[dict]:
        """获取会话消息"""
        return self.sessions.get(session_id, [])
    
    def clear_session(self, session_id: str):
        """清空会话"""
        if session_id in self.sessions:
            self.sessions[session_id] = []
    
    def export_session(self, session_id: str, filepath: str):
        """导出会话"""
        messages = self.get_messages(session_id)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump({
                'session_id': session_id,
                'messages': messages,
                'export_time': datetime.now().isoformat()
            }, f, ensure_ascii=False, indent=2)


# 全局变量
agent = None
chat_history_manager = ChatHistory()
current_session_id = None


def initialize_agent():
    """初始化RAG Agent"""
    global agent
    
    if agent is None:
        if not os.path.exists(VECTOR_DB_PATH):
            return "❌ 向量数据库不存在！请先运行：python process_data.py"
        
        try:
            agent = RAGAgent(
                model=MODEL_NAME,
                enable_tracking=True,
                enable_cot=True
            )
            
            count = agent.vector_store.get_collection_count()
            return f"✅ 系统初始化成功！知识库包含 {count} 个文档片段"
        except Exception as e:
            return f"❌ 初始化失败: {str(e)}"
    
    return "✅ 系统已就绪"


def chat_interface(
    message: str,
    history: List[Dict],
    enable_reasoning: bool = False,
    enable_token_tracking: bool = True,
    max_retries: int = 2
) -> Tuple[str, List[Dict], str, str, str]:
    """
    聊天接口（使用Gradio 4.0+的消息格式）
    
    返回: (答案, 更新后的历史, 推理链, Token统计, 置信度)
    """
    global agent, chat_history_manager, current_session_id
    
    if agent is None:
        init_msg = initialize_agent()
        if "失败" in init_msg:
            return init_msg, history, "", "", ""
    
    # 创建会话（如果需要）
    if current_session_id is None:
        current_session_id = chat_history_manager.create_session()
    
    # 添加用户消息
    chat_history_manager.add_message(current_session_id, "user", message)
    
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
        
        # 添加助教消息
        chat_history_manager.add_message(current_session_id, "assistant", answer)
        
        # 更新历史（消息格式）
        history.append({"role": "user", "content": message})
        history.append({"role": "assistant", "content": answer})
        
        # 获取推理链
        reasoning_text = ""
        if enable_reasoning:
            reasoning = agent.get_reasoning_chain()
            if reasoning:
                reasoning_text = reasoning.format_chain(detailed=True)
        
        # 获取Token统计
        token_text = ""
        if enable_token_tracking:
            token_text = agent.get_token_report()
        
        # 计算置信度
        confidence_text = calculate_confidence(answer, agent)
        
        return answer, history, reasoning_text, token_text, confidence_text
        
    except Exception as e:
        error_msg = f"❌ 错误: {str(e)}"
        history.append({"role": "user", "content": message})
        history.append({"role": "assistant", "content": error_msg})
        return error_msg, history, "", "", ""


def calculate_confidence(answer: str, agent: RAGAgent) -> str:
    """
    计算答案置信度
    
    基于以下因素：
    1. 推理链的平均置信度
    2. 答案长度
    3. 检索结果相似度
    4. 答案质量检查
    """
    try:
        reasoning = agent.get_reasoning_chain()
        
        if reasoning:
            # 推理链置信度
            reasoning_conf = reasoning.get_average_confidence()
            
            # 答案质量
            quality_pass = agent.check_answer_quality(answer, "")
            quality_score = 0.9 if quality_pass else 0.5
            
            # 答案长度（适中为好）
            length = len(answer)
            if 50 <= length <= 500:
                length_score = 1.0
            elif length < 50:
                length_score = 0.6
            else:
                length_score = 0.8
            
            # 综合置信度
            total_confidence = (
                reasoning_conf * 0.5 +
                quality_score * 0.3 +
                length_score * 0.2
            )
            
            # 格式化输出
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

【推理步骤数】
  {len(reasoning.steps)} 步

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


def clear_chat():
    """清空对话"""
    global current_session_id, chat_history_manager
    
    if current_session_id:
        chat_history_manager.clear_session(current_session_id)
    
    # 创建新会话
    current_session_id = chat_history_manager.create_session()
    
    return [], "", "", ""


def export_chat():
    """导出对话历史"""
    global current_session_id, chat_history_manager
    
    if current_session_id:
        filepath = f"chat_history_{current_session_id}.json"
        chat_history_manager.export_session(current_session_id, filepath)
        return f"✅ 对话历史已导出到: {filepath}"
    return "⚠️ 没有对话历史可导出"


def get_system_status():
    """获取系统状态"""
    global agent
    
    if agent is None:
        return "系统未初始化"
    
    try:
        count = agent.vector_store.get_collection_count()
        status = f"""
╔══════════════════════════════════════════════════════╗
║                  系统状态                             ║
╚══════════════════════════════════════════════════════╝

【知识库】
  • 文档片段数: {count}
  • 向量数据库: ChromaDB

【模型】
  • LLM: {agent.model}
  • Token追踪: {'启用' if agent.token_tracker else '禁用'}
  • Auto-CoT: {'启用' if agent.enable_cot else '禁用'}

【功能】
  ✓ 智能问题分类
  ✓ 多查询增强检索
  ✓ 结果重排序
  ✓ 分层检索策略
  ✓ 答案质量检查
  ✓ 推理链记录
  ✓ Token追踪和优化
  ✓ Auto-CoT推理

【统计】
  • 累计查询: {agent.query_count} 次
"""
        
        if agent.token_tracker:
            status += f"  • Token消耗: {agent.token_tracker.usage['total']:,} tokens\n"
        
        return status
    except Exception as e:
        return f"获取状态失败: {str(e)}"


# 创建Gradio界面
def create_ui():
    """创建Gradio界面"""
    
    # 自定义CSS
    custom_css = """
    .gradio-container {
        font-family: 'Arial', sans-serif;
    }
    .tab-label {
        font-size: 18px;
        font-weight: bold;
    }
    #chatbot {
        height: 500px;
    }
    #reasoning_output, #token_output, #confidence_output {
        font-family: 'Courier New', monospace;
        font-size: 12px;
    }
    """
    
    with gr.Blocks(title="智能课程助教", css=custom_css, theme=gr.themes.Soft()) as demo:
        
        gr.Markdown("""
        # 🎓 智能课程助教系统
        
        **功能特色：**
        - 🔍 智能检索和问题分类
        - 🧠 Auto-CoT推理增强
        - 📊 完整的推理链记录
        - 💰 Token使用追踪
        - ✅ 答案质量检查和重试
        - 📈 答案置信度评估
        """)
        
        # 初始化系统
        with gr.Row():
            init_btn = gr.Button("🚀 初始化系统", variant="primary")
            status_btn = gr.Button("📊 系统状态")
            export_btn = gr.Button("💾 导出对话")
        
        init_output = gr.Textbox(label="系统信息", lines=2)
        
        # 主界面
        with gr.Tab("💬 对话"):
            with gr.Row():
                with gr.Column(scale=2):
                    chatbot = gr.Chatbot(
                        label="对话窗口",
                        height=500,
                        elem_id="chatbot"
                    )
                    
                    with gr.Row():
                        msg = gr.Textbox(
                            label="输入问题",
                            placeholder="请输入你的问题...",
                            scale=4
                        )
                        submit_btn = gr.Button("📤 发送", variant="primary", scale=1)
                    
                    with gr.Row():
                        clear_btn = gr.Button("🗑️ 清空对话")
                        retry_slider = gr.Slider(
                            minimum=1,
                            maximum=5,
                            value=2,
                            step=1,
                            label="最大重试次数"
                        )
                
                with gr.Column(scale=1):
                    gr.Markdown("### ⚙️ 设置")
                    enable_reasoning = gr.Checkbox(
                        label="显示推理链",
                        value=True
                    )
                    enable_token = gr.Checkbox(
                        label="显示Token统计",
                        value=True
                    )
                    
                    gr.Markdown("### 📌 快速示例")
                    examples = gr.Examples(
                        examples=[
                            "什么是词向量？",
                            "BERT和GPT有什么区别？",
                            "解释一下Transformer的自注意力机制",
                            "如何计算两个词向量的相似度？",
                            "什么是预训练语言模型？"
                        ],
                        inputs=msg
                    )
        
        # 推理链标签页
        with gr.Tab("🔍 推理链"):
            reasoning_output = gr.Textbox(
                label="推理过程",
                lines=20,
                elem_id="reasoning_output"
            )
        
        # Token统计标签页
        with gr.Tab("💰 Token统计"):
            token_output = gr.Textbox(
                label="Token使用报告",
                lines=20,
                elem_id="token_output"
            )
        
        # 置信度标签页
        with gr.Tab("📈 置信度"):
            confidence_output = gr.Textbox(
                label="答案置信度",
                lines=15,
                elem_id="confidence_output"
            )
        
        # 系统状态标签页
        with gr.Tab("📊 系统状态"):
            status_output = gr.Textbox(
                label="系统状态",
                lines=20
            )
            refresh_status_btn = gr.Button("🔄 刷新状态")
        
        # 事件绑定
        init_btn.click(
            fn=initialize_agent,
            outputs=init_output
        )
        
        status_btn.click(
            fn=get_system_status,
            outputs=init_output
        )
        
        export_btn.click(
            fn=export_chat,
            outputs=init_output
        )
        
        submit_btn.click(
            fn=chat_interface,
            inputs=[msg, chatbot, enable_reasoning, enable_token, retry_slider],
            outputs=[init_output, chatbot, reasoning_output, token_output, confidence_output]
        ).then(
            fn=lambda: "",
            outputs=msg
        )
        
        msg.submit(
            fn=chat_interface,
            inputs=[msg, chatbot, enable_reasoning, enable_token, retry_slider],
            outputs=[init_output, chatbot, reasoning_output, token_output, confidence_output]
        ).then(
            fn=lambda: "",
            outputs=msg
        )
        
        clear_btn.click(
            fn=clear_chat,
            outputs=[chatbot, reasoning_output, token_output, confidence_output]
        )
        
        refresh_status_btn.click(
            fn=get_system_status,
            outputs=status_output
        )
        
        # 页脚
        gr.Markdown("""
        ---
        **💡 使用提示:**
        - 支持多轮对话，自动记录历史
        - 答案质量自动检查，低质量会自动重试
        - 推理链完整记录每一步思考过程
        - Token统计帮助你控制成本
        - 置信度评估帮助判断答案可靠性
        
        **🔧 技术栈:** RAG + ChromaDB + OpenAI API + Auto-CoT + Gradio
        """)
    
    return demo


if __name__ == "__main__":
    demo = create_ui()
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        show_error=True
    )

