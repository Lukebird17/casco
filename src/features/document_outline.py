#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文档智能大纲
自动生成文档结构树、概念索引
"""

from typing import List, Dict, Optional
from openai import OpenAI
from config import OPENAI_API_KEY, OPENAI_API_BASE, TEXT_MODEL_NAME
import json
import re


class DocumentOutline:
    """文档大纲生成器"""
    
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY, base_url=OPENAI_API_BASE)
        self.model = TEXT_MODEL_NAME
        self.outlines: Dict[str, Dict] = {}  # {doc_name: outline_data}
        
    def generate_outline(self, doc_name: str, content: str) -> Dict:
        """
        生成文档大纲
        
        Args:
            doc_name: 文档名称
            content: 文档内容
            
        Returns:
            {
                "title": "文档标题",
                "summary": "概要",
                "structure": [章节结构],
                "concepts": [概念列表]
            }
        """
        
        prompt = f"""请为以下文档生成结构化大纲。

文档名称：{doc_name}

文档内容（节选）：
{content[:3000]}

请生成：
1. 文档标题（如果内容中有）
2. 简短概要（1-2句话）
3. 章节结构（包括标题和主要内容）
4. 关键概念列表

以JSON格式输出：
```json
{{
  "title": "文档标题",
  "summary": "文档概要",
  "structure": [
    {{
      "level": 1,
      "title": "第一章",
      "summary": "本章概要",
      "subsections": [
        {{
          "level": 2,
          "title": "1.1 小节",
          "summary": "小节概要"
        }}
      ]
    }}
  ],
  "concepts": [
    {{
      "name": "概念名",
      "definition": "定义",
      "importance": "high/medium/low"
    }}
  ]
}}
```

只输出JSON，不要其他文字。
"""
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "你是文档分析专家，擅长提取结构化信息。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=2000
            )
            
            result = response.choices[0].message.content
            
            # 提取JSON
            json_match = re.search(r'```json\s*(.*?)\s*```', result, re.DOTALL)
            if json_match:
                json_str = json_match.group(1)
            else:
                json_str = result
            
            outline = json.loads(json_str)
            outline['doc_name'] = doc_name
            
            # 保存
            self.outlines[doc_name] = outline
            
            return outline
            
        except Exception as e:
            print(f"大纲生成失败: {e}")
            return {
                "title": doc_name,
                "summary": "大纲生成失败",
                "structure": [],
                "concepts": [],
                "error": str(e)
            }
    
    def get_outline(self, doc_name: str) -> Optional[Dict]:
        """获取已生成的大纲"""
        return self.outlines.get(doc_name)
    
    def search_concept(self, concept_name: str) -> List[Dict]:
        """跨文档搜索概念"""
        results = []
        
        for doc_name, outline in self.outlines.items():
            concepts = outline.get('concepts', [])
            for concept in concepts:
                if concept_name.lower() in concept.get('name', '').lower():
                    results.append({
                        "doc_name": doc_name,
                        "concept": concept['name'],
                        "definition": concept.get('definition', ''),
                        "importance": concept.get('importance', 'medium')
                    })
        
        return results
    
    def render_outline(self, doc_name: str) -> str:
        """渲染文档大纲为 HTML"""
        
        outline = self.outlines.get(doc_name)
        
        if not outline:
            return f'''
            <div style="padding: 40px; text-align: center; color: #9ca3af;">
                📭 暂无大纲<br>
                <span style="font-size: 14px;">请先生成大纲</span>
            </div>
            '''
        
        html = f'''
        <div style="padding: 20px; background: #f9fafb; border-radius: 12px;">
            <h2 style="color: #6366f1; margin-bottom: 10px;">
                📄 {outline.get('title', doc_name)}
            </h2>
            <div style="color: #6b7280; margin-bottom: 20px; padding: 10px; background: white; border-radius: 6px;">
                {outline.get('summary', '')}
            </div>
        '''
        
        # 章节结构
        if outline.get('structure'):
            html += '<h3 style="color: #6366f1; margin-top: 20px;">📑 章节结构</h3>'
            
            for section in outline['structure']:
                html += self._render_section(section)
        
        # 关键概念
        if outline.get('concepts'):
            html += '<h3 style="color: #6366f1; margin-top: 30px;">💡 关键概念</h3>'
            
            for concept in outline['concepts']:
                importance = concept.get('importance', 'medium')
                
                # 重要性颜色
                importance_colors = {
                    'high': '#ef4444',
                    'medium': '#f59e0b',
                    'low': '#10b981'
                }
                color = importance_colors.get(importance, '#6b7280')
                
                html += f'''
                <div style="padding: 12px; margin: 8px 0; background: white; 
                            border-left: 4px solid {color}; border-radius: 6px;">
                    <div style="font-weight: 600; color: #1f2937; margin-bottom: 4px;">
                        {concept['name']}
                        <span style="background: {color}; color: white; padding: 2px 8px; 
                                     border-radius: 10px; font-size: 11px; margin-left: 8px;">
                            {importance.upper()}
                        </span>
                    </div>
                    <div style="font-size: 14px; color: #6b7280;">
                        {concept.get('definition', '')}
                    </div>
                </div>
                '''
        
        html += '</div>'
        return html
    
    def _render_section(self, section: Dict, indent: int = 0) -> str:
        """递归渲染章节"""
        level = section.get('level', 1)
        title = section.get('title', '')
        summary = section.get('summary', '')
        
        # 根据层级调整样式
        if level == 1:
            style = "font-size: 18px; font-weight: 700; color: #1f2937; margin-top: 15px;"
        elif level == 2:
            style = "font-size: 16px; font-weight: 600; color: #374151; margin-top: 10px; margin-left: 20px;"
        else:
            style = "font-size: 14px; font-weight: 500; color: #6b7280; margin-top: 8px; margin-left: 40px;"
        
        html = f'''
        <div style="padding: 10px; margin: 5px 0; background: white; border-radius: 6px;">
            <div style="{style}">
                {'  ' * indent}{'📌' if level == 1 else '▪️'} {title}
            </div>
            {f'<div style="font-size: 13px; color: #9ca3af; margin-left: {20 * (indent + 1)}px; margin-top: 4px;">{summary}</div>' if summary else ''}
        </div>
        '''
        
        # 递归渲染子章节
        if section.get('subsections'):
            for subsection in section['subsections']:
                html += self._render_section(subsection, indent + 1)
        
        return html
    
    def render_all_outlines(self) -> str:
        """渲染所有文档大纲的目录"""
        
        if not self.outlines:
            return '''
            <div style="padding: 40px; text-align: center; color: #9ca3af;">
                📭 暂无文档大纲
            </div>
            '''
        
        html = '''
        <div style="padding: 20px; background: #f9fafb; border-radius: 12px;">
            <h2 style="color: #6366f1; margin-bottom: 20px;">📚 文档目录</h2>
        '''
        
        for doc_name, outline in self.outlines.items():
            html += f'''
            <div style="padding: 15px; margin: 10px 0; background: white; border-radius: 8px; 
                        box-shadow: 0 1px 3px rgba(0,0,0,0.1); cursor: pointer;"
                 onclick="alert('open_{doc_name}')"
                 onmouseover="this.style.boxShadow='0 4px 12px rgba(0,0,0,0.15)'"
                 onmouseout="this.style.boxShadow='0 1px 3px rgba(0,0,0,0.1)'">
                <div style="font-weight: 700; font-size: 16px; color: #1f2937; margin-bottom: 8px;">
                    📄 {outline.get('title', doc_name)}
                </div>
                <div style="font-size: 13px; color: #6b7280; margin-bottom: 10px;">
                    {outline.get('summary', '')[:100]}...
                </div>
                <div style="display: flex; gap: 15px; font-size: 12px; color: #9ca3af;">
                    <span>📑 {len(outline.get('structure', []))} 个章节</span>
                    <span>💡 {len(outline.get('concepts', []))} 个概念</span>
                </div>
            </div>
            '''
        
        html += '</div>'
        return html
    
    def render_concept_index(self) -> str:
        """渲染概念索引"""
        
        all_concepts = []
        
        for doc_name, outline in self.outlines.items():
            concepts = outline.get('concepts', [])
            for concept in concepts:
                all_concepts.append({
                    **concept,
                    'doc_name': doc_name,
                    'doc_title': outline.get('title', doc_name)
                })
        
        if not all_concepts:
            return '''
            <div style="padding: 40px; text-align: center; color: #9ca3af;">
                📭 暂无概念索引
            </div>
            '''
        
        # 按名称排序
        all_concepts.sort(key=lambda x: x.get('name', ''))
        
        html = '''
        <div style="padding: 20px; background: #f9fafb; border-radius: 12px;">
            <h2 style="color: #6366f1; margin-bottom: 20px;">🔖 概念索引</h2>
        '''
        
        current_letter = None
        
        for concept in all_concepts:
            name = concept.get('name', '')
            first_letter = name[0].upper() if name else '#'
            
            # 字母分组
            if first_letter != current_letter:
                current_letter = first_letter
                html += f'''
                <div style="font-size: 24px; font-weight: 700; color: #6366f1; 
                            margin: 20px 0 10px 0; padding-bottom: 5px; border-bottom: 2px solid #6366f1;">
                    {current_letter}
                </div>
                '''
            
            importance = concept.get('importance', 'medium')
            importance_colors = {
                'high': '#ef4444',
                'medium': '#f59e0b',
                'low': '#10b981'
            }
            color = importance_colors.get(importance, '#6b7280')
            
            html += f'''
            <div style="padding: 10px 15px; margin: 5px 0; background: white; 
                        border-left: 3px solid {color}; border-radius: 6px;">
                <div style="display: flex; justify-content: space-between; align-items: start;">
                    <div style="flex: 1;">
                        <div style="font-weight: 600; color: #1f2937; margin-bottom: 4px;">
                            {name}
                        </div>
                        <div style="font-size: 13px; color: #6b7280; margin-bottom: 4px;">
                            {concept.get('definition', '')[:100]}...
                        </div>
                        <div style="font-size: 11px; color: #9ca3af;">
                            📄 {concept.get('doc_title', '')}
                        </div>
                    </div>
                    <span style="background: {color}; color: white; padding: 4px 10px; 
                                 border-radius: 12px; font-size: 10px; white-space: nowrap;">
                        {importance.upper()}
                    </span>
                </div>
            </div>
            '''
        
        html += '</div>'
        return html





