#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
片段收藏管理器
管理用户收藏的知识片段
"""

import json
from pathlib import Path
from typing import List, Dict, Optional
from datetime import datetime
import hashlib


class SnippetManager:
    """片段收藏管理器"""
    
    def __init__(self, storage_path: str = "./snippets.json"):
        self.storage_path = Path(storage_path)
        self.snippets: List[Dict] = self._load_snippets()
        self.tags: set = self._extract_tags()
        
    def _load_snippets(self) -> List[Dict]:
        """加载收藏片段"""
        if self.storage_path.exists():
            try:
                with open(self.storage_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                pass
        return []
    
    def _save_snippets(self):
        """保存收藏片段"""
        with open(self.storage_path, 'w', encoding='utf-8') as f:
            json.dump(self.snippets, f, ensure_ascii=False, indent=2)
    
    def _extract_tags(self) -> set:
        """提取所有标签"""
        tags = set()
        for snippet in self.snippets:
            tags.update(snippet.get('tags', []))
        return tags
    
    def add_snippet(
        self, 
        content: str, 
        source: str = "", 
        tags: List[str] = None,
        metadata: Optional[Dict] = None
    ) -> str:
        """
        添加收藏片段
        
        Args:
            content: 片段内容
            source: 来源（文件名、页码等）
            tags: 标签列表
            metadata: 其他元数据
            
        Returns:
            snippet_id
        """
        # 生成唯一ID
        snippet_id = hashlib.md5(
            f"{content}{datetime.now().isoformat()}".encode()
        ).hexdigest()[:12]
        
        snippet = {
            "id": snippet_id,
            "content": content,
            "source": source,
            "tags": tags or [],
            "metadata": metadata or {},
            "created_at": datetime.now().isoformat(),
            "favorite": False
        }
        
        self.snippets.insert(0, snippet)  # 新的在前面
        self._save_snippets()
        self.tags.update(tags or [])
        
        return snippet_id
    
    def delete_snippet(self, snippet_id: str) -> bool:
        """删除片段"""
        for i, snippet in enumerate(self.snippets):
            if snippet['id'] == snippet_id:
                self.snippets.pop(i)
                self._save_snippets()
                self.tags = self._extract_tags()
                return True
        return False
    
    def toggle_favorite(self, snippet_id: str) -> bool:
        """切换收藏状态"""
        for snippet in self.snippets:
            if snippet['id'] == snippet_id:
                snippet['favorite'] = not snippet.get('favorite', False)
                self._save_snippets()
                return True
        return False
    
    def add_tag(self, snippet_id: str, tag: str) -> bool:
        """添加标签"""
        for snippet in self.snippets:
            if snippet['id'] == snippet_id:
                if tag not in snippet['tags']:
                    snippet['tags'].append(tag)
                    self._save_snippets()
                    self.tags.add(tag)
                return True
        return False
    
    def remove_tag(self, snippet_id: str, tag: str) -> bool:
        """移除标签"""
        for snippet in self.snippets:
            if snippet['id'] == snippet_id:
                if tag in snippet['tags']:
                    snippet['tags'].remove(tag)
                    self._save_snippets()
                    self.tags = self._extract_tags()
                return True
        return False
    
    def search_snippets(
        self, 
        query: Optional[str] = None,
        tags: Optional[List[str]] = None,
        favorites_only: bool = False
    ) -> List[Dict]:
        """
        搜索片段
        
        Args:
            query: 搜索关键词
            tags: 标签筛选
            favorites_only: 只显示收藏的
            
        Returns:
            匹配的片段列表
        """
        results = self.snippets.copy()
        
        # 按收藏筛选
        if favorites_only:
            results = [s for s in results if s.get('favorite', False)]
        
        # 按标签筛选
        if tags:
            results = [
                s for s in results 
                if any(tag in s.get('tags', []) for tag in tags)
            ]
        
        # 按关键词搜索
        if query:
            query_lower = query.lower()
            results = [
                s for s in results
                if query_lower in s['content'].lower() or 
                   query_lower in s.get('source', '').lower()
            ]
        
        return results
    
    def get_all_tags(self) -> List[str]:
        """获取所有标签"""
        return sorted(list(self.tags))
    
    def render_snippets(
        self, 
        snippets: Optional[List[Dict]] = None,
        max_display: int = 50
    ) -> str:
        """
        渲染片段列表为 HTML
        
        Args:
            snippets: 要显示的片段，None 表示全部
            max_display: 最多显示数量
        """
        if snippets is None:
            snippets = self.snippets
        
        if not snippets:
            return '''
            <div style="padding: 40px; text-align: center; color: #9ca3af;">
                📭 还没有收藏任何片段<br>
                <span style="font-size: 14px;">在对话中点击 ⭐ 按钮收藏优质内容</span>
            </div>
            '''
        
        html = f'''
        <div style="padding: 15px; background: #f9fafb; border-radius: 12px; max-height: 600px; overflow-y: auto;">
            <h3 style="color: #6366f1; margin-bottom: 15px; position: sticky; top: 0; background: #f9fafb; padding: 10px 0;">
                ⭐ 收藏片段 ({len(snippets)})
            </h3>
        '''
        
        for i, snippet in enumerate(snippets[:max_display]):
            is_favorite = snippet.get('favorite', False)
            favorite_icon = "⭐" if is_favorite else "☆"
            favorite_color = "#fbbf24" if is_favorite else "#d1d5db"
            
            tags_html = ""
            for tag in snippet.get('tags', []):
                tags_html += f'''
                <span style="background: #e0e7ff; color: #6366f1; padding: 3px 8px; 
                             border-radius: 12px; font-size: 11px; margin-right: 5px;">
                    #{tag}
                </span>
                '''
            
            # 截断内容
            content = snippet['content']
            if len(content) > 300:
                content = content[:300] + "..."
            
            # 格式化时间
            created = snippet.get('created_at', '')
            if created:
                try:
                    dt = datetime.fromisoformat(created)
                    created = dt.strftime("%Y-%m-%d %H:%M")
                except:
                    pass
            
            html += f'''
            <div style="background: white; padding: 15px; margin: 10px 0; border-radius: 8px; 
                        box-shadow: 0 1px 3px rgba(0,0,0,0.1); transition: all 0.2s;"
                 onmouseover="this.style.boxShadow='0 4px 12px rgba(0,0,0,0.15)'"
                 onmouseout="this.style.boxShadow='0 1px 3px rgba(0,0,0,0.1)'">
                
                <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 10px;">
                    <div style="flex: 1;">
                        <div style="font-size: 13px; color: #6b7280; margin-bottom: 5px;">
                            {snippet.get('source', '未知来源')}
                        </div>
                        {tags_html}
                    </div>
                    <button style="background: none; border: none; font-size: 20px; cursor: pointer; color: {favorite_color};"
                            onclick="alert('toggle_favorite_{snippet['id']}')"
                            title="{'取消收藏' if is_favorite else '设为重要'}">
                        {favorite_icon}
                    </button>
                </div>
                
                <div style="color: #1f2937; line-height: 1.6; margin-bottom: 10px; white-space: pre-wrap;">
                    {content}
                </div>
                
                <div style="display: flex; justify-content: space-between; align-items: center; 
                            padding-top: 10px; border-top: 1px solid #e5e7eb;">
                    <div style="font-size: 11px; color: #9ca3af;">
                        {created}
                    </div>
                    <div style="display: flex; gap: 8px;">
                        <button style="padding: 4px 10px; background: #f3f4f6; color: #6b7280; 
                                       border: none; border-radius: 4px; cursor: pointer; font-size: 11px;"
                                onclick="alert('copy_{snippet['id']}')">
                            📋 复制
                        </button>
                        <button style="padding: 4px 10px; background: #fef2f2; color: #ef4444; 
                                       border: none; border-radius: 4px; cursor: pointer; font-size: 11px;"
                                onclick="alert('delete_{snippet['id']}')">
                            🗑️ 删除
                        </button>
                    </div>
                </div>
            </div>
            '''
        
        if len(snippets) > max_display:
            html += f'''
            <div style="text-align: center; color: #9ca3af; margin-top: 15px; font-size: 13px;">
                还有 {len(snippets) - max_display} 个片段未显示
            </div>
            '''
        
        html += '</div>'
        return html
    
    def export_to_markdown(self, snippets: Optional[List[Dict]] = None) -> str:
        """导出为 Markdown 格式"""
        if snippets is None:
            snippets = self.snippets
        
        md = "# 我的知识片段\n\n"
        md += f"总共 {len(snippets)} 个片段\n\n"
        md += "---\n\n"
        
        for i, snippet in enumerate(snippets, 1):
            md += f"## {i}. {snippet.get('source', '未知来源')}\n\n"
            
            if snippet.get('tags'):
                md += "**标签**: " + ", ".join(f"`{tag}`" for tag in snippet['tags']) + "\n\n"
            
            md += snippet['content'] + "\n\n"
            
            if snippet.get('created_at'):
                md += f"*收藏时间: {snippet['created_at']}*\n\n"
            
            md += "---\n\n"
        
        return md





