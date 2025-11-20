# build_storage_bge.py
import os
import re
from pathlib import Path
from typing import List
from tqdm import tqdm

# 导入现有模块和新写的 BGE 模块
from VectorBase import VectorStore
from my_BGE_embedding import BGEEmbedding

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

def process_markdown_files(folder_path: str, max_len: int = 600):
    """
    读取文件夹，处理文档，保留标题信息
    """
    all_chunks = []
    md_files = list(Path(folder_path).rglob('*.md'))
    
    print(f"📂 扫描到 {len(md_files)} 个 Markdown 文件")
    
    for file_path in tqdm(md_files, desc="处理文档切分"):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # 获取文件名作为标题（去除后缀）
            file_name = file_path.stem
            
            # --- 核心策略：智能分段 ---
            raw_chunks = recursive_split_text(content, max_len=max_len, overlap=100)
            
            # --- 核心策略：注入元数据 ---
            # 在每个片段前加上文件名，确保 Embedding 包含了文档来源信息
            # 这样检索 "S7号线" 时，即使片段里只有 "最高时速100"，加上标题后也能匹配上
            for chunk in raw_chunks:
                if len(chunk.strip()) < 10: # 过滤过短的噪点
                    continue
                enhanced_chunk = f"《{file_name}》\n{chunk}"
                all_chunks.append(enhanced_chunk)
                
        except Exception as e:
            print(f"❌ 处理文件 {file_path} 失败: {e}")
            
    return all_chunks

def main():
    # 1. 配置路径
    INPUT_FOLDER = 'trial/' #'output_paddle/'  # 你的 OCR 结果文件夹
    STORAGE_PATH = './trial_bge'#'./storage_bge'   # 新的存储路径
    
    # 2. 处理文档与切分
    print("🚀 开始处理文档...")
    documents = process_markdown_files(INPUT_FOLDER)
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
