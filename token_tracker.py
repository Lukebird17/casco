#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Token追踪器（从Casco移植）
用于追踪和优化Token使用
"""

import tiktoken
import json
from typing import Dict, List
from datetime import datetime


class TokenTracker:
    """Token使用追踪器（从Casco完全移植）"""
    
    def __init__(self, encoding_name: str = "cl100k_base"):
        """
        初始化Token追踪器
        Args:
            encoding_name: tiktoken编码名称
        """
        self.enc = tiktoken.get_encoding(encoding_name)
        self.usage = {
            'embedding': 0,
            'retrieval_context': 0,
            'llm_input': 0,
            'llm_output': 0,
            'total': 0
        }
        self.queries_log = []
        self.start_time = datetime.now()
    
    def count_tokens(self, text: str) -> int:
        """
        计算文本的token数量
        Args:
            text: 输入文本
        Returns:
            token数量
        """
        if not text:
            return 0
        return len(self.enc.encode(str(text)))
    
    def track_embedding(self, texts: List[str]) -> int:
        """
        追踪Embedding消耗
        Args:
            texts: 文本列表
        Returns:
            总token数
        """
        tokens = sum(self.count_tokens(t) for t in texts)
        self.usage['embedding'] += tokens
        self.usage['total'] += tokens
        return tokens
    
    def track_retrieval(self, context: str) -> int:
        """
        追踪检索上下文消耗
        Args:
            context: 检索到的上下文
        Returns:
            token数
        """
        tokens = self.count_tokens(context)
        self.usage['retrieval_context'] += tokens
        return tokens
    
    def track_llm(self, prompt: str, response: str) -> Dict[str, int]:
        """
        追踪LLM调用消耗
        Args:
            prompt: 输入提示词
            response: LLM响应
        Returns:
            包含输入输出token数的字典
        """
        input_tokens = self.count_tokens(prompt)
        output_tokens = self.count_tokens(response)
        
        self.usage['llm_input'] += input_tokens
        self.usage['llm_output'] += output_tokens
        self.usage['total'] += input_tokens + output_tokens
        
        return {
            'input': input_tokens,
            'output': output_tokens,
            'total': input_tokens + output_tokens
        }
    
    def log_query(self, query: str, answer: str, query_type: str, 
                  retrieval_count: int, token_usage: Dict[str, int]):
        """
        记录单次查询的详细信息
        Args:
            query: 查询问题
            answer: 生成的答案
            query_type: 问题类型
            retrieval_count: 检索文档数量
            token_usage: token使用详情
        """
        self.queries_log.append({
            'timestamp': datetime.now().isoformat(),
            'query': query[:100] + '...' if len(query) > 100 else query,
            'query_type': query_type,
            'retrieval_count': retrieval_count,
            'answer_length': len(answer),
            'token_usage': token_usage
        })
    
    def optimize_context(self, context: str, max_tokens: int = 3000, 
                        preserve_structure: bool = True) -> str:
        """
        优化上下文长度，控制token消耗
        Args:
            context: 原始上下文
            max_tokens: 最大允许token数
            preserve_structure: 是否保留结构标记
        Returns:
            优化后的上下文
        """
        current_tokens = self.count_tokens(context)
        
        if current_tokens <= max_tokens:
            return context
        
        print(f"  ⚠️  上下文过长({current_tokens} tokens)，优化至{max_tokens} tokens")
        
        if preserve_structure:
            # 保留结构化信息（如来源标记、表格等）
            return self._smart_truncate(context, max_tokens)
        else:
            # 简单截断
            return self._simple_truncate(context, max_tokens)
    
    def _smart_truncate(self, context: str, max_tokens: int) -> str:
        """
        智能截断：保留关键信息
        """
        lines = context.split('\n')
        
        # 识别重要行（来源标记、表格、标题等）
        important_lines = []
        normal_lines = []
        
        for i, line in enumerate(lines):
            if any(marker in line for marker in ['[材料', '来源：', '【', '===', '内容：']):
                important_lines.append((i, line))
            else:
                normal_lines.append((i, line))
        
        # 优先保留重要行
        result = []
        current_tokens = 0
        
        # 1. 添加重要行
        for i, line in important_lines:
            line_tokens = self.count_tokens(line)
            if current_tokens + line_tokens <= max_tokens * 0.3:  # 重要信息占30%
                result.append((i, line))
                current_tokens += line_tokens
        
        # 2. 添加普通行（均匀采样）
        remaining_tokens = max_tokens - current_tokens
        if normal_lines:
            sample_rate = max(1, len(normal_lines) // int(remaining_tokens / 50))
            for idx in range(0, len(normal_lines), sample_rate):
                i, line = normal_lines[idx]
                line_tokens = self.count_tokens(line)
                if current_tokens + line_tokens <= max_tokens:
                    result.append((i, line))
                    current_tokens += line_tokens
                else:
                    break
        
        # 3. 按原始顺序排序
        result.sort(key=lambda x: x[0])
        
        truncated_lines = [line for _, line in result]
        truncated_lines.insert(len(truncated_lines)//2, 
                             "\n... [为节省token，部分内容已省略] ...\n")
        
        return '\n'.join(truncated_lines)
    
    def _simple_truncate(self, context: str, max_tokens: int) -> str:
        """
        简单截断：保留开头和结尾
        """
        tokens = self.enc.encode(context)
        
        if len(tokens) <= max_tokens:
            return context
        
        # 保留前50%和后30%，中间20%省略
        keep_head = int(max_tokens * 0.5)
        keep_tail = int(max_tokens * 0.3)
        
        head_text = self.enc.decode(tokens[:keep_head])
        tail_text = self.enc.decode(tokens[-keep_tail:])
        
        return (
            head_text + 
            "\n\n... [为节省token，中间内容已省略] ...\n\n" + 
            tail_text
        )
    
    def get_report(self) -> str:
        """
        生成详细的使用报告
        Returns:
            格式化的报告字符串
        """
        duration = (datetime.now() - self.start_time).total_seconds()
        
        # 估算成本（基于DeepSeek定价）
        cost_embedding = self.usage['embedding'] / 1000 * 0.0001
        cost_llm_input = self.usage['llm_input'] / 1000 * 0.001
        cost_llm_output = self.usage['llm_output'] / 1000 * 0.002
        total_cost = cost_embedding + cost_llm_input + cost_llm_output
        
        report = f"""
╔══════════════════════════════════════════════════════╗
║            Token使用统计报告                          ║
╚══════════════════════════════════════════════════════╝

【使用统计】
  • Embedding:      {self.usage['embedding']:>10,} tokens
  • 检索上下文:      {self.usage['retrieval_context']:>10,} tokens
  • LLM输入:        {self.usage['llm_input']:>10,} tokens
  • LLM输出:        {self.usage['llm_output']:>10,} tokens
  ─────────────────────────────────────────────────────
  • 总计:           {self.usage['total']:>10,} tokens

【成本估算】
  • Embedding:      ¥{cost_embedding:>8.4f}
  • LLM输入:        ¥{cost_llm_input:>8.4f}
  • LLM输出:        ¥{cost_llm_output:>8.4f}
  ─────────────────────────────────────────────────────
  • 总成本:         ¥{total_cost:>8.4f}

【效率指标】
  • 查询次数:       {len(self.queries_log)}
  • 运行时长:       {duration:.1f} 秒
  • 平均每查询:     {self.usage['total'] / len(self.queries_log) if self.queries_log else 0:,.0f} tokens
  

╚══════════════════════════════════════════════════════╝
"""
        return report
    
    def get_summary(self) -> Dict:
        """
        获取摘要信息（用于JSON输出）
        Returns:
            摘要字典
        """
        return {
            'total_tokens': self.usage['total'],
            'embedding_tokens': self.usage['embedding'],
            'llm_input_tokens': self.usage['llm_input'],
            'llm_output_tokens': self.usage['llm_output'],
            'query_count': len(self.queries_log),
            'queries': self.queries_log
        }
    
    def save_report(self, output_path: str = 'token_usage_report.json'):
        """
        保存详细报告到文件
        Args:
            output_path: 输出文件路径
        """
        report_data = {
            'summary': self.get_summary(),
            'usage_breakdown': self.usage,
            'queries': self.queries_log,
            'start_time': self.start_time.isoformat(),
            'end_time': datetime.now().isoformat()
        }
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Token使用报告已保存到: {output_path}")
    
    def reset(self):
        """重置统计"""
        self.usage = {
            'embedding': 0,
            'retrieval_context': 0,
            'llm_input': 0,
            'llm_output': 0,
            'total': 0
        }
        self.queries_log = []
        self.start_time = datetime.now()


if __name__ == "__main__":
    # 测试代码
    tracker = TokenTracker()
    
    # 测试计数
    test_text = "这是一个测试文本，用来计算token数量。"
    tokens = tracker.count_tokens(test_text)
    print(f"文本token数: {tokens}")
    
    # 测试追踪
    tracker.track_embedding([test_text])
    tracker.track_llm("测试提示词", "测试响应")
    
    # 测试报告
    print(tracker.get_report())

