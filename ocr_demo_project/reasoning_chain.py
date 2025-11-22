#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   reasoning_chain.py
@Time    :   2025/11/16
@Desc    :   推理链记录器 - 记录和展示推理过程
'''

from typing import List, Dict, Optional
from datetime import datetime
import json


class ReasoningStep:
    """单个推理步骤"""
    
    def __init__(self, step_type: str, description: str, 
                 evidence: str = "", confidence: float = 1.0):
        """
        初始化推理步骤
        Args:
            step_type: 步骤类型（如"问题分析"、"信息检索"、"逻辑推理"等）
            description: 步骤描述
            evidence: 支持证据
            confidence: 置信度(0-1)
        """
        self.step_type = step_type
        self.description = description
        self.evidence = evidence
        self.confidence = confidence
        self.timestamp = datetime.now()
    
    def to_dict(self) -> Dict:
        """转换为字典"""
        return {
            'type': self.step_type,
            'description': self.description,
            'evidence': self.evidence[:200] + '...' if len(self.evidence) > 200 else self.evidence,
            'confidence': self.confidence,
            'timestamp': self.timestamp.isoformat()
        }
    
    def __str__(self) -> str:
        """字符串表示"""
        confidence_bar = "█" * int(self.confidence * 10) + "░" * (10 - int(self.confidence * 10))
        return f"[{self.step_type}] {self.description} (置信度: {confidence_bar} {self.confidence:.1%})"


class ReasoningChain:
    """推理链记录器"""
    
    def __init__(self, query: str = ""):
        """
        初始化推理链
        Args:
            query: 用户查询
        """
        self.query = query
        self.steps: List[ReasoningStep] = []
        self.start_time = datetime.now()
        self.end_time = None
        self.final_answer = None
        
    def add_step(self, step_type: str, description: str, 
                 evidence: str = "", confidence: float = 1.0) -> 'ReasoningChain':
        """
        添加推理步骤
        Args:
            step_type: 步骤类型
            description: 描述
            evidence: 证据
            confidence: 置信度
        Returns:
            self，支持链式调用
        """
        step = ReasoningStep(step_type, description, evidence, confidence)
        self.steps.append(step)
        return self
    
    def add_analysis_step(self, description: str, evidence: str = "") -> 'ReasoningChain':
        """添加分析步骤"""
        return self.add_step("分析", description, evidence)
    
    def add_retrieval_step(self, description: str, evidence: str = "") -> 'ReasoningChain':
        """添加检索步骤"""
        return self.add_step("检索", description, evidence)
    
    def add_inference_step(self, description: str, evidence: str = "", 
                          confidence: float = 0.8) -> 'ReasoningChain':
        """添加推理步骤"""
        return self.add_step("推理", description, evidence, confidence)
    
    def add_verification_step(self, description: str, evidence: str = "") -> 'ReasoningChain':
        """添加验证步骤"""
        return self.add_step("验证", description, evidence)
    
    def add_conclusion_step(self, description: str, evidence: str = "") -> 'ReasoningChain':
        """添加结论步骤"""
        return self.add_step("结论", description, evidence)
    
    def set_final_answer(self, answer: str):
        """
        设置最终答案
        Args:
            answer: 最终答案
        """
        self.final_answer = answer
        self.end_time = datetime.now()
    
    def get_average_confidence(self) -> float:
        """获取平均置信度"""
        if not self.steps:
            return 0.0
        return sum(step.confidence for step in self.steps) / len(self.steps)
    
    def get_duration(self) -> float:
        """获取推理耗时（秒）"""
        end = self.end_time or datetime.now()
        return (end - self.start_time).total_seconds()
    
    def format_chain(self, detailed: bool = True, max_evidence_len: int = 100) -> str:
        """
        格式化推理链为可读文本
        Args:
            detailed: 是否显示详细信息
            max_evidence_len: 证据最大显示长度
        Returns:
            格式化的推理链
        """
        output = []
        output.append("╔══════════════════════════════════════════════════════╗")
        output.append("║                  推理过程记录                         ║")
        output.append("╚══════════════════════════════════════════════════════╝")
        output.append("")
        
        if self.query:
            output.append(f"【问题】{self.query}")
            output.append("")
        
        output.append(f"【推理步骤】共 {len(self.steps)} 步")
        output.append("")
        
        for i, step in enumerate(self.steps, 1):
            # 步骤类型图标
            icon = self._get_step_icon(step.step_type)
            
            # 基本信息
            output.append(f"{icon} 步骤 {i}: [{step.step_type}] {step.description}")
            
            if detailed and step.evidence:
                # 显示证据（截断）
                evidence = step.evidence[:max_evidence_len]
                if len(step.evidence) > max_evidence_len:
                    evidence += "..."
                output.append(f"   └─ 依据: {evidence}")
            
            # 置信度
            if step.confidence < 1.0:
                confidence_bar = "█" * int(step.confidence * 10) + "░" * (10 - int(step.confidence * 10))
                output.append(f"   └─ 置信度: {confidence_bar} {step.confidence:.0%}")
            
            output.append("")
        
        # 统计信息
        output.append("【推理统计】")
        output.append(f"  • 总步骤数: {len(self.steps)}")
        output.append(f"  • 平均置信度: {self.get_average_confidence():.1%}")
        output.append(f"  • 推理耗时: {self.get_duration():.2f} 秒")
        
        if self.final_answer:
            output.append("")
            output.append("【最终答案】")
            output.append(f"  {self.final_answer}")
        
        output.append("")
        output.append("╚══════════════════════════════════════════════════════╝")
        
        return "\n".join(output)
    
    def _get_step_icon(self, step_type: str) -> str:
        """获取步骤类型图标"""
        icons = {
            "分析": "🔍",
            "检索": "📚",
            "推理": "🧠",
            "验证": "✓",
            "结论": "💡",
            "对比": "⚖️",
            "提取": "📋"
        }
        return icons.get(step_type, "➤")
    
    def format_compact(self) -> str:
        """格式化为紧凑版本（用于日志）"""
        steps_summary = " → ".join([f"{s.step_type}" for s in self.steps])
        return f"推理链({len(self.steps)}步): {steps_summary} | 置信度: {self.get_average_confidence():.0%}"
    
    def to_dict(self) -> Dict:
        """转换为字典（用于JSON序列化）"""
        return {
            'query': self.query,
            'steps': [step.to_dict() for step in self.steps],
            'step_count': len(self.steps),
            'average_confidence': self.get_average_confidence(),
            'duration_seconds': self.get_duration(),
            'final_answer': self.final_answer,
            'start_time': self.start_time.isoformat(),
            'end_time': self.end_time.isoformat() if self.end_time else None
        }
    
    def to_json(self, indent: int = 2) -> str:
        """转换为JSON字符串"""
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=indent)
    
    def save(self, file_path: str):
        """保存推理链到文件"""
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(self.to_json())
        print(f"✅ 推理链已保存到: {file_path}")


class ReasoningChainManager:
    """推理链管理器 - 管理多个推理链"""
    
    def __init__(self):
        """初始化管理器"""
        self.chains: List[ReasoningChain] = []
        self.current_chain: Optional[ReasoningChain] = None
    
    def create_chain(self, query: str = "") -> ReasoningChain:
        """
        创建新的推理链
        Args:
            query: 查询问题
        Returns:
            新创建的推理链
        """
        chain = ReasoningChain(query)
        self.chains.append(chain)
        self.current_chain = chain
        return chain
    
    def get_current_chain(self) -> Optional[ReasoningChain]:
        """获取当前推理链"""
        return self.current_chain
    
    def get_all_chains(self) -> List[ReasoningChain]:
        """获取所有推理链"""
        return self.chains
    
    def get_statistics(self) -> Dict:
        """获取统计信息"""
        if not self.chains:
            return {
                'total_chains': 0,
                'total_steps': 0,
                'average_steps_per_chain': 0,
                'average_confidence': 0,
                'total_duration': 0
            }
        
        total_steps = sum(len(chain.steps) for chain in self.chains)
        total_confidence = sum(chain.get_average_confidence() for chain in self.chains)
        total_duration = sum(chain.get_duration() for chain in self.chains)
        
        return {
            'total_chains': len(self.chains),
            'total_steps': total_steps,
            'average_steps_per_chain': total_steps / len(self.chains),
            'average_confidence': total_confidence / len(self.chains),
            'total_duration': total_duration
        }
    
    def generate_report(self) -> str:
        """生成推理链报告"""
        stats = self.get_statistics()
        
        report = f"""
╔══════════════════════════════════════════════════════╗
║               推理链管理报告                          ║
╚══════════════════════════════════════════════════════╝

【统计概览】
  • 推理链总数: {stats['total_chains']}
  • 推理步骤总数: {stats['total_steps']}
  • 平均步骤数: {stats['average_steps_per_chain']:.1f} 步/链
  • 平均置信度: {stats['average_confidence']:.1%}
  • 总推理时长: {stats['total_duration']:.1f} 秒

【各推理链概况】
"""
        for i, chain in enumerate(self.chains, 1):
            report += f"\n{i}. {chain.query[:50]}{'...' if len(chain.query) > 50 else ''}\n"
            report += f"   {chain.format_compact()}\n"
        
        report += "\n╚══════════════════════════════════════════════════════╝"
        
        return report
    
    def save_all(self, output_dir: str = "reasoning_chains"):
        """保存所有推理链"""
        import os
        os.makedirs(output_dir, exist_ok=True)
        
        for i, chain in enumerate(self.chains, 1):
            file_path = os.path.join(output_dir, f"chain_{i}.json")
            chain.save(file_path)
        
        # 保存汇总报告
        summary_path = os.path.join(output_dir, "summary.txt")
        with open(summary_path, 'w', encoding='utf-8') as f:
            f.write(self.generate_report())
        
        print(f"✅ 所有推理链已保存到: {output_dir}")


# 便捷函数
def create_reasoning_chain(query: str = "") -> ReasoningChain:
    """创建推理链的便捷函数"""
    return ReasoningChain(query)


if __name__ == "__main__":
    # 测试推理链
    print("=== 测试推理链 ===\n")
    
    # 创建推理链
    chain = ReasoningChain("南京地铁S7号线的运营里程在江苏省内排第几？")
    
    # 添加推理步骤
    chain.add_analysis_step(
        "识别为排名类问题，需要查找多个地铁线路数据",
        "关键词: '排第几'、'运营里程'"
    )
    
    chain.add_retrieval_step(
        "检索江苏省地铁运营数据",
        "检索到5个相关文档片段"
    )
    
    chain.add_step(
        "提取",
        "从检索结果中提取各线路里程数据",
        "找到: 南京1号线38km, 2号线37.4km, S7号线30.2km..."
    )
    
    chain.add_inference_step(
        "对比分析各线路里程，确定排名",
        "共12条线路，S7号线30.2km，排名第8",
        confidence=0.9
    )
    
    chain.add_verification_step(
        "验证数据来源和准确性",
        "数据来源: 《城市轨道交通2024年度统计报告》"
    )
    
    chain.add_conclusion_step(
        "南京地铁S7号线运营里程为30.2公里，在江苏省已运营地铁中排名第8位"
    )
    
    chain.set_final_answer("南京地铁S7号线的运营里程为30.2公里，在江苏省已运营地铁长度中排第8位。")
    
    # 显示推理链
    print(chain.format_chain(detailed=True))
    
    # 测试管理器
    print("\n\n=== 测试推理链管理器 ===\n")
    
    manager = ReasoningChainManager()
    
    # 创建多个推理链
    for i in range(3):
        chain = manager.create_chain(f"测试问题 {i+1}")
        chain.add_analysis_step(f"分析问题 {i+1}")
        chain.add_retrieval_step(f"检索相关信息 {i+1}")
        chain.add_conclusion_step(f"得出结论 {i+1}")
    
    # 生成报告
    print(manager.generate_report())