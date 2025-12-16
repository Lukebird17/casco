# build_storage_bge.py
import os
import re
from pathlib import Path
from typing import List
from tqdm import tqdm
from typing import List, Dict, Any, Tuple
# 导入现有模块和新写的 BGE 模块
from VectorBase import VectorStore
from my_BGE_embedding import BGEEmbedding
from LLM import OpenAIChat
SUPPORTED_LANGS = ['zh', 'en', 'es', 'fr', 'de', 'ja', 'ko']

# 新增：语言代码到名称的映射
LANGUAGE_NAMES = {
    'zh': '中文',
    'en': '英语',
    'es': '西班牙语',
    'fr': '法语',
    'de': '德语',
    'ja': '日语',
    'ko': '韩语',
    # 如果需要，可以添加更多语言
}

def predict_document_language(file_path: Path, llm_instance: OpenAIChat) -> str:
    """
    通过文件名和文档前100字符，结合LLM API推断文档语言。
    
    Args:
        file_path: 文档路径。
        llm_instance: 用于调用语言检测API的LLM实例 (e.g., OpenAIChat)。
        
    Returns:
        推断出的语言代码 ('zh', 'en', 等)。
    """
    file_name = file_path.name
    # 辅助函数：格式化输出结果
    def format_output(lang_code, reason):
        lang_name = LANGUAGE_NAMES.get(lang_code, f"未知 ({lang_code})")
        print(f"✅ 文件 '{file_name}' 语言识别成功: {lang_name} ({lang_code}) - 来源: {reason}")
        return lang_code
    
    # 检查 LLM 实例是否有效 (解决 NoneType 错误)
    if llm_instance is None:
        return 'zh' # LLM 失败时使用默认语言

    # 2. 读取文档内容 (用于LLM推断)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read(100) # 只读取前100个字符
    except Exception:
        content = ""

    # 3. LLM推断
    # 检查 llm_instance 是否有正确的完成方法
    if not hasattr(llm_instance, 'get_completion'):
        print(f"⚠️ LLM语言推断失败: LLM实例缺少 'get_completion' 方法，使用默认语言 'zh'")
        return 'zh'

    # 构建Prompt
    prompt = f"请严格根据以下文件内容片段，推断其主要语言。文件名为 {file_name}，内容为：'{content}'。请只输出语言代码，例如 'zh', 'en', 'ja'。"
    
    try:
        # **重要修改:** 将 llm_instance.invoke 改为 llm_instance.get_completion
        result = llm_instance.get_completion(prompt).strip().lower() 
        code_match = re.search(r'\b(zh|en|es|fr|de|ja|ko)\b', result)

        if code_match:
            final_code = code_match.group(1)
            return format_output(final_code, "LLM推断")
        else:
            print(f"⚠️ 文件 '{file_name}': LLM推断返回了不支持或不清晰的结果 '{result}'，使用默认语言 '中文 (zh)'")
            return 'zh'
            
    except Exception as e:
        # 捕获 LLM API 调用失败的异常 (包括网络错误、认证错误等)
        # 此时的 LLM 实例不是 None，而是调用失败
        print(f"⚠️ 文件 '{file_name}': LLM语言推断失败 (API 调用错误: {e})，使用默认语言 '中文 (zh)'")
        return 'zh'

def recursive_split_text(text: str, max_len: int = 500, overlap: int = 50) -> List[str]:
    """
    智能分段函数：优先在段落和句子结束符处切分，保证句子完整性
    """
    # 1. 如果文本本身很短，直接返回
    if len(text) <= max_len:
        return [text]
    
    # 2. 定义分隔符优先级：双换行(段落) > 单换行 > 中文句号等 > 英文句号 > 逗号 > 强制切分
    separators = ["\n\n", "\n", "。", "！", "？", ".", "!", "?", "；", ";", "，", ","]
    
    chunks = []
    
    # 尝试找到最佳切分点
    for sep in separators:
        if sep in text:
            # 按分隔符初步切分
            splits = text.split(sep)
            current_chunk = ""
            
            for split in splits:
                # 恢复分隔符（除了换行符，通常句号需要保留）
                token = sep if sep not in ["\n\n", "\n"] else " "
                segment = split + token
                
                if len(current_chunk) + len(segment) < max_len:
                    current_chunk += segment
                else:
                    if current_chunk:
                        chunks.append(current_chunk.strip())
                    # 处理重叠：取上一个 chunk 的后 overlap 个字符作为上下文（可选）
                    current_chunk = segment
            
            if current_chunk:
                chunks.append(current_chunk.strip())
                
            # 如果切分成功（产生了多个片段），则结束当前层级的切分
            if len(chunks) > 0:
                return chunks
    
    # 3. 如果所有分隔符都失效（比如一整段没有标点），只能强制按字符切分
    return [text[i:i+max_len] for i in range(0, len(text), max_len-overlap)]

# ❗ 修改函数签名和返回结构
def process_markdown_files(folder_path: str, llm_instance: OpenAIChat, max_len: int = 400) -> List[Dict[str, Any]]:
    """
    读取文件夹，处理文档，保留标题信息
    """
    all_chunks: List[Dict[str, Any]] = [] # 存储 List[Dict]
    md_files = list(Path(folder_path).rglob('*.md'))
    
    print(f"📂 扫描到 {len(md_files)} 个 Markdown 文件")
    
    for file_path in tqdm(list(Path(folder_path).glob('*.md')), desc="处理文档切分"):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            file_name = file_path.stem
            
            # ❗ 新增：推断文件语言
            file_lang = predict_document_language(file_path, llm_instance)

            # --- 核心策略：智能分段 ---
            raw_chunks = recursive_split_text(content, max_len=max_len, overlap=100)
            
            # --- 核心策略：注入元数据（内容 + 语言标签） ---
            for chunk in raw_chunks:
                if len(chunk.strip()) < 10:
                    continue
                # 存储为字典结构
                all_chunks.append({
                    'content': f"《{file_name}》\n{chunk}", # 保留文件名作为上下文
                    'lang': file_lang # 注入语言标签
                })
                
        except Exception as e:
            print(f"❌ 处理文件 {file_path} 失败: {e}")
            
    return all_chunks

def main():
    # 1. 配置路径
    INPUT_FOLDER = 'output_paddle_table/' #'output_paddle/'  # 你的 OCR 结果文件夹
    STORAGE_PATH = '../trial_bge'#'./storage_bge'   # 新的存储路径
    
    # 2. 处理文档与切分
    print("🚀 开始处理文档...")
    llm = OpenAIChat()
    documents = process_markdown_files(INPUT_FOLDER, llm)
    print(f"📊 文档处理完成，共生成 {len(documents)} 个向量片段")
    
    # 3. 初始化 BGE 模型
    # 注意：第一次运行会自动下载模型 (约 2GB)，请保持网络通畅
    embedding_model = BGEEmbedding()
    
    # 4. 创建向量库并生成向量
    print("⚡ 开始生成向量 (这可能需要几分钟)...")
    vector_store = VectorStore(documents)
    vector_store.get_vector(embedding_model)
    
    # 5. 持久化存储
    vector_store.persist(STORAGE_PATH)
    print(f"✅ 成功！向量库已保存至: {STORAGE_PATH}")
    print("提示：请在 demo_enhanced.py 中修改 vector_store.load_vector('./storage_bge') 以使用新库")

if __name__ == "__main__":
    main()
