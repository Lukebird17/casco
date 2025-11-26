#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   extract_questions.py
@Desc    :   从Markdown文件中提取题目并格式化为纯文本列表 (修复版：兼容无空格格式)
'''

import re

def extract_and_save_questions(input_file, output_file):
    questions = []
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        print(f"📂 正在读取文件: {input_file}")
        
        for line in lines:
            line = line.strip()
            if not line:
                continue

            # === 修改点：将 \s+ 改为 \s*，允许数字点号后没有空格 ===
            # 模式1: 匹配 "### 1.题目" 或 "### 3.北京..."
            match = re.match(r'^###\s*\d+\.\s*(.*)', line) 
            
            # 模式2: 匹配 "1.题目" (没有###的情况)
            if not match:
                match = re.match(r'^\d+\.\s*(.*)', line)
                
            if match:
                # 提取题目内容
                q_text = match.group(1).strip()
                
                # 2. 处理双引号：将英文双引号 " 替换为单引号 '
                # 这一步是为了防止 Python 字符串嵌套错误
                q_text = q_text.replace('"', "'")
                # 处理中文双引号 “ ” 为单引号 ' '
                q_text = q_text.replace('“', "'").replace('”', "'")
                
                # 简单的长度检查，防止提取到空标题
                if len(q_text) > 2:
                    questions.append(q_text)
                    print(f"  - [提取成功] {q_text[:20]}...")
                else:
                    print(f"  - [跳过短行] {line}")

        # 3. 保存到文件
        with open(output_file, 'w', encoding='utf-8') as f:
            for q in questions:
                f.write(q + "\n")
                
        print(f"\n✅ 成功提取 {len(questions)} 道题目")
        print(f"💾 已保存到: {output_file}")
        
    except FileNotFoundError:
        print(f"❌ 错误: 找不到文件 {input_file}")
    except Exception as e:
        print(f"❌ 发生错误: {e}")

if __name__ == "__main__":
    # 请确保这里的文件名和你本地的一致
    INPUT_MD = "初赛一期题目.md" 
    OUTPUT_TXT = "questions_list.txt"
    
    extract_and_save_questions(INPUT_MD, OUTPUT_TXT)