#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文档热力图
追踪和可视化常被引用的文档区域
"""

import json
from pathlib import Path
from typing import Dict, List, Optional
from collections import defaultdict
from datetime import datetime


class DocumentHeatmap:
    """文档热力图管理器"""
    
    def __init__(self, storage_path: str = "./heatmap_data.json"):
        self.storage_path = Path(storage_path)
        self.heatmap_data: Dict = self._load_data()
        
    def _load_data(self) -> Dict:
        """加载热力图数据"""
        if self.storage_path.exists():
            try:
                with open(self.storage_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                pass
        
        return {
            "documents": {},  # {filename: {page: count}}
            "citations": [],  # 引用历史
            "last_updated": datetime.now().isoformat()
        }
    
    def _save_data(self):
        """保存热力图数据"""
        self.heatmap_data["last_updated"] = datetime.now().isoformat()
        with open(self.storage_path, 'w', encoding='utf-8') as f:
            json.dump(self.heatmap_data, f, ensure_ascii=False, indent=2)
    
    def record_citation(self, filename: str, page: int, content: str = ""):
        """
        记录一次引用
        
        Args:
            filename: 文件名
            page: 页码
            content: 引用内容
        """
        # 更新文档热力图
        if filename not in self.heatmap_data["documents"]:
            self.heatmap_data["documents"][filename] = {}
        
        page_key = str(page)
        if page_key not in self.heatmap_data["documents"][filename]:
            self.heatmap_data["documents"][filename][page_key] = 0
        
        self.heatmap_data["documents"][filename][page_key] += 1
        
        # 记录引用历史
        self.heatmap_data["citations"].append({
            "filename": filename,
            "page": page,
            "content": content[:100],  # 只保存前100字符
            "timestamp": datetime.now().isoformat()
        })
        
        # 只保留最近1000条引用
        if len(self.heatmap_data["citations"]) > 1000:
            self.heatmap_data["citations"] = self.heatmap_data["citations"][-1000:]
        
        self._save_data()
    
    def get_document_hotspots(self, filename: str, top_k: int = 10) -> List[Dict]:
        """
        获取文档的热点页面
        
        Args:
            filename: 文件名
            top_k: 返回前 k 个热点
            
        Returns:
            [{"page": 1, "count": 10}, ...]
        """
        if filename not in self.heatmap_data["documents"]:
            return []
        
        pages = self.heatmap_data["documents"][filename]
        hotspots = [
            {"page": int(page), "count": count}
            for page, count in pages.items()
        ]
        
        return sorted(hotspots, key=lambda x: x["count"], reverse=True)[:top_k]
    
    def get_all_hotspots(self, top_k: int = 20) -> List[Dict]:
        """获取所有文档的热点"""
        all_hotspots = []
        
        for filename, pages in self.heatmap_data["documents"].items():
            for page, count in pages.items():
                all_hotspots.append({
                    "filename": filename,
                    "page": int(page),
                    "count": count
                })
        
        return sorted(all_hotspots, key=lambda x: x["count"], reverse=True)[:top_k]
    
    def render_heatmap(self, filename: Optional[str] = None) -> str:
        """
        渲染热力图 HTML
        
        Args:
            filename: 特定文档，None 表示所有文档
        """
        if filename:
            hotspots = self.get_document_hotspots(filename)
            title = f"📊 {filename} 热力图"
        else:
            hotspots = self.get_all_hotspots()
            title = "📊 全局文档热力图"
        
        if not hotspots:
            return '''
            <div style="padding: 40px; text-align: center; color: #9ca3af;">
                📭 暂无引用数据
            </div>
            '''
        
        # 找到最大值用于归一化
        max_count = max(h["count"] for h in hotspots)
        
        html = f'''
        <div style="padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    border-radius: 12px; color: white;">
            <h3 style="margin-bottom: 20px;">{title}</h3>
            <div style="font-size: 12px; opacity: 0.9; margin-bottom: 15px;">
                🔥 显示最常被引用的内容区域
            </div>
        '''
        
        for i, hotspot in enumerate(hotspots[:10]):  # 只显示前10个
            intensity = hotspot["count"] / max_count
            
            # 根据强度选择颜色
            if intensity >= 0.8:
                color = "#ef4444"  # 红色 - 极热
                emoji = "🔴"
            elif intensity >= 0.6:
                color = "#f59e0b"  # 橙色 - 很热
                emoji = "🟠"
            elif intensity >= 0.4:
                color = "#fbbf24"  # 黄色 - 热
                emoji = "🟡"
            elif intensity >= 0.2:
                color = "#34d399"  # 绿色 - 温
                emoji = "🟢"
            else:
                color = "#60a5fa"  # 蓝色 - 冷
                emoji = "🔵"
            
            display_name = hotspot.get("filename", "未知文档")
            if len(display_name) > 30:
                display_name = display_name[:27] + "..."
            
            html += f'''
            <div style="background: rgba(255,255,255,0.1); padding: 12px; margin: 8px 0; 
                        border-left: 4px solid {color}; border-radius: 6px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div style="flex: 1;">
                        <div style="font-weight: 600; margin-bottom: 4px;">
                            {emoji} #{i+1}. {display_name if filename else hotspot['filename']}
                        </div>
                        <div style="font-size: 13px; opacity: 0.9;">
                            第 {hotspot['page']} 页
                        </div>
                    </div>
                    <div style="text-align: right;">
                        <div style="font-size: 24px; font-weight: bold;">
                            {hotspot['count']}
                        </div>
                        <div style="font-size: 11px; opacity: 0.8;">
                            次引用
                        </div>
                    </div>
                </div>
                <div style="margin-top: 8px; background: rgba(255,255,255,0.2); height: 6px; border-radius: 3px; overflow: hidden;">
                    <div style="background: {color}; height: 100%; width: {intensity*100}%; transition: width 0.3s;"></div>
                </div>
            </div>
            '''
        
        html += '</div>'
        return html
    
    def get_statistics(self) -> Dict:
        """获取统计信息"""
        total_citations = sum(
            sum(pages.values())
            for pages in self.heatmap_data["documents"].values()
        )
        
        total_docs = len(self.heatmap_data["documents"])
        total_pages = sum(
            len(pages)
            for pages in self.heatmap_data["documents"].values()
        )
        
        return {
            "total_citations": total_citations,
            "total_documents": total_docs,
            "total_pages_cited": total_pages,
            "last_updated": self.heatmap_data.get("last_updated", "N/A")
        }


