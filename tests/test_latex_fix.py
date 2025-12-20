#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试LaTeX修复函数
验证各种不规范格式是否能正确转换
"""

import re

def _fix_latex_format(text: str) -> str:
    """
    修复LLM输出的LaTeX格式问题
    将不规范的公式格式转换为标准的 \\( \\) 和 \\[ \\] 格式
    """
    
    # 策略：分步骤处理，每次处理一种情况
    
    # 第1步：修复 \ ) 和 \ ] 这种奇怪的格式
    text = text.replace('\\ )', '\\)')
    text = text.replace('\\ ]', '\\]')
    text = text.replace('\\ (', '\\(')
    text = text.replace('\\ [', '\\[')
    
    # 第2步：修复独立公式 [ formula ] → \\[ formula \\]
    # 只处理包含LaTeX命令或数学符号的方括号
    def replace_brackets(match):
        content = match.group(1)
        # 检查是否包含LaTeX命令或数学符号
        if re.search(r'\\[a-zA-Z]+|\\frac|\\sum|\\prod|\\int|_|\^|=|\+|-|\*|/', content):
            return f'\\[ {content} \\]'
        return match.group(0)  # 不是公式，保持原样
    
    text = re.sub(r'(?<!\\)\[\s*([^\[\]]+?)\s*\]', replace_brackets, text)
    
    # 第3步：修复行内公式 ( formula ) → \\( formula \\)
    # 只处理包含LaTeX命令或数学符号的圆括号
    def replace_parens(match):
        content = match.group(1)
        # 检查是否包含LaTeX命令、下标、上标，或者像 P(w|h) 这样的概率符号
        if re.search(r'\\[a-zA-Z]+|\\frac|_|\^|[A-Z]\([^)]+\|[^)]+\)', content):
            return f'\\( {content} \\)'
        return match.group(0)  # 不是公式，保持原样
    
    text = re.sub(r'(?<!\\)\(\s*([^\(\)]+?)\s*\)', replace_parens, text)
    
    return text


# 测试用例
test_cases = [
    # 格式1：\( y_{i-1} \ )（奇怪的反斜杠空格）
    {
        "input": "标签 \\( y_{i-1} \\ ) 转移到标签 \\( y_i \\ )",
        "expected": "标签 \\( y_{i-1} \\) 转移到标签 \\( y_i \\)",
        "description": "修复反斜杠空格问题"
    },
    
    # 格式2：[ ... ]（独立公式）
    {
        "input": "公式为 [ r^* = (r + 1) \\frac{N_{r+1}}{N_r} ]",
        "expected": "公式为 \\[ r^* = (r + 1) \\frac{N_{r+1}}{N_r} \\]",
        "description": "修复独立公式"
    },
    
    # 格式3：( ... )（行内公式）
    {
        "input": "概率 ( P(w|h) ) 表示",
        "expected": "概率 \\( P(w|h) \\) 表示",
        "description": "修复行内公式"
    },
    
    # 格式4：已经正确的格式（不应该被修改）
    {
        "input": "已经正确 \\( P(w|h) \\) 的格式",
        "expected": "已经正确 \\( P(w|h) \\) 的格式",
        "description": "保持已正确的格式"
    },
    
    # 格式5：普通括号（不应该被修改）
    {
        "input": "普通括号 (这是说明) 不是公式",
        "expected": "普通括号 (这是说明) 不是公式",
        "description": "不修改普通括号"
    },
    
    # 格式6：用户提到的实际例子
    {
        "input": "矩阵 \\( m \\times m \\ ) 的维度 \\( \\mathbb{R} \\ )",
        "expected": "矩阵 \\( m \\times m \\) 的维度 \\( \\mathbb{R} \\)",
        "description": "用户实际例子"
    },
]

print("="*80)
print("LaTeX格式修复测试")
print("="*80)

passed = 0
failed = 0

for i, test in enumerate(test_cases, 1):
    print(f"\n测试 {i}: {test['description']}")
    print(f"  输入:  {repr(test['input'])}")
    
    result = _fix_latex_format(test['input'])
    
    print(f"  输出:  {repr(result)}")
    print(f"  期望:  {repr(test['expected'])}")
    
    if result == test['expected']:
        print("  ✅ 通过")
        passed += 1
    else:
        print("  ❌ 失败")
        failed += 1

print("\n" + "="*80)
print(f"测试结果: {passed} 通过, {failed} 失败")
print("="*80)

