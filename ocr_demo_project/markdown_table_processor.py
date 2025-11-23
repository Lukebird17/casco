#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   markdown_table_processor.py
@Time    :   2025/11/21
@Desc    :   Markdown文件批量表格识别、转换和替换工具
'''
import json  # 新增
import os
import re
import shutil
from typing import List
from LLM import OpenAIChat  # 假设您的OpenAIChat类位于LLM.py中
from dotenv import load_dotenv, find_dotenv

# 加载环境变量 (确保您的 .env 文件中配置了 DeepSeek API 信息)
_ = load_dotenv(find_dotenv())

# --- 配置 ---
# 新的输出文件夹
OUTPUT_FOLDER = "./output_paddle_table"
# Zero-Shot 提示词文件
PROMPT_FILE = "table_prompt.txt"

# 优化后的正则表达式：允许表格独立存在，或被特定标题 DIV 包裹
# 捕获整个表格块 (包含可选的 DIV 标题和 TABLE)
TABLE_BLOCK_PATTERN = re.compile(
    r'((?:<div\s+style="text-align:\s*center;">.*?<\/div>\s*)?<table\b.*?<\/table>)',
    re.DOTALL | re.IGNORECASE
)

# --- 工具函数 ---

def load_prompt_template(file_path: str) -> str:
    """从文件中读取Zero-Shot提示词模板"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            template = f.read()
            if "{html_table_content}" not in template:
                raise ValueError("Prompt 文件中必须包含占位符 {html_table_content}")
            return template
    except FileNotFoundError:
        print(f"❌ 错误：未找到提示词文件 '{file_path}'。请创建此文件。")
        exit(1)
    except ValueError as e:
        print(f"❌ 错误：提示词文件格式不正确。{e}")
        exit(1)
    except Exception as e:
        print(f"❌ 读取提示词文件失败: {e}")
        exit(1)

def html_table_to_natural_language(html_content: str) -> str:
    """
    通用表格转换函数 (硬编码逻辑)：
    将包含 rowspan / colspan 的 HTML 表格转换为【行级字典列表】的 JSON 字符串。
    每一行数据 -> 一个字典，形如：
    {"城市": "南京", "线路数(条)": "15", "线路名称": "S7号线", "运营里程(公里)": "30.20", ...}

    :param html_content: 完整的 <table>...</table> HTML 字符串。
    :return: JSON 数组字符串，如：
             [
               {"城市": "...", "线路数(条)": "...", ...},
               ...
             ]
             如果无法识别为有效表格，则返回空字符串 ""（触发 LLM 兜底）。
    """
    # 1. 匹配所有 <tr>...</tr>
    match_rows = re.findall(r'<tr[^>]*>(.*?)</tr>', html_content, re.DOTALL | re.IGNORECASE)
    if not match_rows:
        return ""

    # 2. 匹配单元格 <td>/<th>，解析 colspan、rowspan、内容
    #   group 1: colspan 数值（可空）
    #   group 2: rowspan 数值（可空）
    #   group 3: 单元格内部 HTML
    cell_pattern = re.compile(
        r'<t[dh][^>]*?(?:\s*colspan=["\']?(\d+)["\']?)?(?:\s*rowspan=["\']?(\d+)["\']?)?[^>]*>\s*(.*?)\s*</t[dh]>',
        re.DOTALL | re.IGNORECASE
    )

    # --- 1. 提取并确定表头 ---
    header_row_content = match_rows[0]
    header_cells = cell_pattern.findall(header_row_content)

    headers: List[str] = []
    for colspan_str, rowspan_str, inner_html in header_cells:
        colspan = int(colspan_str) if colspan_str else 1
        header_text = re.sub(r'<[^>]+>', '', inner_html).strip()

        # 忽略“序号”列：用空字符串占位，后续跳过这一列
        if header_text in ("序号", "序号 "):
            headers.extend([""] * colspan)
        else:
            headers.extend([header_text] * colspan)

    num_cols = len(headers)
    if num_cols == 0:
        # 表头都没识别出来，视为失败，交给 LLM
        return ""

    # --- 2. 处理数据行 ---
    data_rows_content = match_rows[1:]

    # 记录 rowSpan 状态：每列一个 dict，value/剩余行数
    span_state = {i: {'value': None, 'count': 0} for i in range(num_cols)}

    row_dicts = []  # 要返回的字典列表

    for row_content in data_rows_content:
        # 2.1 先继承 rowspan 留下的值
        current_logical_row = [None] * num_cols
        for i in range(num_cols):
            if span_state[i]['count'] > 0:
                current_logical_row[i] = span_state[i]['value']
                span_state[i]['count'] -= 1

        # 2.2 解析本行新出现的单元格
        cells = cell_pattern.findall(row_content)
        col_idx = 0

        for colspan_str, rowspan_str, inner_html in cells:
            # 跳过已经被 rowSpan 占用的位置
            while col_idx < num_cols and current_logical_row[col_idx] is not None:
                col_idx += 1
            if col_idx >= num_cols:
                break

            colspan = int(colspan_str) if colspan_str else 1
            rowspan = int(rowspan_str) if rowspan_str else 1

            value = re.sub(r'<[^>]+>', '', inner_html).strip()

            # 写入当前行的逻辑单元格（考虑 colspan）
            for offset in range(colspan):
                current_col = col_idx + offset
                if current_col < num_cols:
                    current_logical_row[current_col] = value

            # 记录 rowspan 状态：后续几行沿用同样的值
            if rowspan > 1:
                for offset in range(colspan):
                    current_col = col_idx + offset
                    if current_col < num_cols:
                        span_state[current_col] = {'value': value, 'count': rowspan - 1}

            col_idx += colspan

        # 2.3 把当前逻辑行转成 dict（key: 表头文本；value: 单元格文本）
        row_dict = {}
        for h, c in zip(headers, current_logical_row):
            # 被忽略的列（如“序号”），或真正为空的列，直接跳过
            if not h or c is None or c == "":
                continue
            key = h.strip()
            val = str(c).strip()
            row_dict[key] = val

        # 整行如果没有任何有效键值对，就跳过
        if not row_dict:
            continue

        row_dicts.append(row_dict)

    # 没有有效数据行，视为失败，交给 LLM
    if not row_dicts:
        return ""

    # 3. 转成 JSON 字符串（行级字典列表）
    return json.dumps(row_dicts, ensure_ascii=False, indent=2)

# def convert_table_to_nl(llm: OpenAIChat, html_table_content: str, prompt_template: str) -> str:
#     """
#     调用LLM将HTML表格内容转换为自然语言。
#     """
#     print("   -> 正在调用 LLM 进行转换...")
    
#     # 使用传入的模板格式化Prompt
#     prompt = prompt_template.format(html_table_content=html_table_content)
    
#     try:
#         natural_language_output = llm.chat(prompt=prompt, history=[], content="")
#         print("   -> 转换完成。")
#         return natural_language_output.strip()
#     except Exception as e:
#         print(f"   ❌ LLM 调用失败: {e}")
#         return ""


def process_markdown_file(file_path: str, llm, prompt_template: str):
    """
    处理单个Markdown文件，优先使用硬编码转换表格，失败后回退到LLM。
    """
    
    # 确定输出路径
    file_name = os.path.basename(file_path)
    output_file_path = os.path.join(OUTPUT_FOLDER, file_name)

    # 1. 目标文档出现过直接跳过
    if os.path.exists(output_file_path):
        print(f"✅ 跳过文件: '{file_name}' (目标文件已存在)")
        return

    # 读取文件内容
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ 错误: 读取文件 '{file_name}' 失败: {e}")
        return

    # 2. 识别表格块
    table_blocks = TABLE_BLOCK_PATTERN.findall(content)
    
    # 识别不到表格的直接跳过
    if not table_blocks:
        print(f"ℹ️ 文件: '{file_name}' (未识别到表格，直接复制原内容)")
        try:
            with open(output_file_path, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
             print(f"❌ 错误: 写入文件 '{file_name}' 失败: {e}")
        return

    new_content = content
    table_count = 0
    
    for table_block in table_blocks:
        table_count += 1
        
        # 提取 TABLE HTML
        table_html_match = re.search(r'<table\b.*</table>', table_block, re.DOTALL | re.IGNORECASE)
        if not table_html_match:
            print(f"⚠️ 文件 '{file_name}', 块 {table_count}: 警告: 找到 DIV 块但未找到 TABLE 标签，保留原样。")
            continue
        table_html = table_html_match.group(0)
        
        converted_text = ""
        method = "Unprocessed"
        
        # --- 3. 硬编码转换 (优先) ---
        hardcoded_result = html_table_to_natural_language(table_html)
        
        if hardcoded_result.strip():
            converted_text = hardcoded_result
            method = "Hardcoded"
        else:
            row_tags = re.findall(r'<tr\b', table_html, flags=re.IGNORECASE)
            if len(row_tags) <= 1:
                print(f"⚠️ 文件 '{file_name}', 块 {table_count}: 检测到单行元数据表格，跳过（不调用 LLM，保留原表格）。")
                continue
            # --- 4. LLM 转换 (作为后备) ---
            print(f"🔄 文件 '{file_name}', 块 {table_count}: 硬编码失败或结果为空，尝试调用 LLM...")
            
            # 使用包含可选 DIV 标题的完整 table_block 作为 LLM 的输入
            full_prompt = prompt_template.replace("{html_table_content}", table_block)
            try:
                # 假设 llm.get_completion 是调用 LLM 的方法
                llm_result = llm.get_completion(full_prompt)
                
                # LLM结果可能包含Prompt中的其他文本，这里尝试提取最后的输出部分
                output_match = re.search(r'【输出】\s*(.*)', llm_result, re.DOTALL)
                if output_match:
                    converted_text = output_match.group(1).strip()
                else:
                    converted_text = llm_result.strip()
                    
                if converted_text:
                    method = "LLM Fallback"
                else:
                    print(f"❌ 文件 '{file_name}', 块 {table_count}: LLM 返回空结果，保留原表格。")
                    continue
            except Exception as e:
                print(f"❌ 文件 '{file_name}', 块 {table_count}: LLM 调用失败: {e}，保留原表格。")
                continue # 跳过此表格块，保留原 HTML

        # 5. 替换内容
        # 替换原始的 table_block (包括可选的 DIV 标题)
        new_content = new_content.replace(table_block, converted_text, 1)
        print(f"✅ 文件 '{file_name}', 块 {table_count}: 转换成功 ({method})")

    # 6. 写入新文件
    try:
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"🎉 文件 '{file_name}' 处理完成，已保存到 '{OUTPUT_FOLDER}'")
    except Exception as e:
        print(f"❌ 错误: 写入文件 '{file_name}' 失败: {e}")


def main(folder_path: str):
    """
    主函数：遍历文件夹并处理Markdown文件。
    """
    print("╔══════════════════════════════════════════════════════╗")
    print("║         Markdown 表格批量处理工具 V3.0 (硬编码优先)  ║")
    print("╚══════════════════════════════════════════════════════╝")
    
    # 1. 初始化LLM模型
    try:
        llm = OpenAIChat() 
        print(f"🤖 LLM 初始化成功 (Model: {llm.model})")
    except Exception as e:
        print(f"❌ LLM 初始化失败，硬编码模式将不会有 LLM 兜底功能: {e}")
        llm = None # 允许在没有LLM的情况下运行硬编码部分

    # 2. 加载Prompt模板
    prompt_template = load_prompt_template(PROMPT_FILE)
    if not prompt_template and llm:
        print("❌ 错误: 无法加载 Prompt 模板，LLM 兜底功能将无法使用。")
        
    # 3. 创建输出文件夹
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
        print(f"📂 创建输出文件夹: {OUTPUT_FOLDER}")
    
    # 4. 遍历文件夹
    if not os.path.isdir(folder_path):
        print(f"❌ 错误：路径 '{folder_path}' 不是一个有效的文件夹。")
        return
        
    print(f"📥 正在从 '{folder_path}' 扫描 Markdown 文件...")
    
    for filename in os.listdir(folder_path):
        if filename.endswith(('.md', '.markdown')):
            file_path = os.path.join(folder_path, filename)
            print(f"\n>>>> 正在处理文件: {filename} <<<<")
            # 只有在 LLM 存在 *且* 提示词模板加载成功时，才启用 LLM 兜底
            if llm and prompt_template:
                process_markdown_file(file_path, llm, prompt_template)
            else:
                # 即使没有 LLM 也能运行，但无法处理硬编码失败的表格
                process_markdown_file(file_path, None, "")

if __name__ == '__main__':
    # 请将此处修改为您存放Markdown文件的实际文件夹路径
    main("./output_paddle")
    print("请调用 main(folder_path) 函数并传入您的 Markdown 文件夹路径。")