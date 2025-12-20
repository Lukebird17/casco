#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
会话管理器
管理多轮对话、历史记录、会话切换
"""

import json
import time
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime


class Session:
    """单个会话"""
    
    def __init__(self, session_id: str, title: str = "新对话"):
        self.session_id = session_id
        self.title = title
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.messages: List[Dict] = []
        self.context_docs: List[str] = []  # 当前会话相关的文档
        self.citations: Dict = {}  # 引用信息
        self.snippets: List[Dict] = []  # 收藏的片段
        self.quality_metrics: Dict = {}  # 每条消息的质量评估
        self.last_quality_metrics = None  # 兼容旧代码
        
    def add_message(self, role: str, content: str, metadata: Optional[Dict] = None):
        """添加消息"""
        message = {
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat(),
            "metadata": metadata or {}
        }
        self.messages.append(message)
        self.updated_at = datetime.now()
        
    def add_citation(self, message_idx: int, citations: List[Dict]):
        """添加引用信息"""
        self.citations[str(message_idx)] = citations
    
    def add_quality_metrics(self, message_idx: int, metrics: Dict):
        """添加质量评估信息"""
        self.quality_metrics[str(message_idx)] = metrics
        self.last_quality_metrics = metrics  # 同时更新last（兼容旧代码）
        
    def add_snippet(self, content: str, source: str, tags: List[str] = None):
        """添加收藏片段"""
        snippet = {
            "id": f"snippet_{len(self.snippets)}",
            "content": content,
            "source": source,
            "tags": tags or [],
            "created_at": datetime.now().isoformat()
        }
        self.snippets.append(snippet)
        
    def to_dict(self) -> Dict:
        """转换为字典"""
        return {
            "session_id": self.session_id,
            "title": self.title,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "messages": self.messages,
            "context_docs": self.context_docs,
            "citations": self.citations,
            "snippets": self.snippets,
            "quality_metrics": getattr(self, 'quality_metrics', {})
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Session':
        """从字典创建"""
        session = cls(data["session_id"], data.get("title", "新对话"))
        session.created_at = datetime.fromisoformat(data["created_at"])
        session.updated_at = datetime.fromisoformat(data["updated_at"])
        session.messages = data.get("messages", [])
        session.context_docs = data.get("context_docs", [])
        session.citations = data.get("citations", {})
        session.snippets = data.get("snippets", [])
        session.quality_metrics = data.get("quality_metrics", {})
        return session


class SessionManager:
    """会话管理器"""
    
    def __init__(self, storage_dir: str = "./sessions"):
        self.storage_dir = Path(storage_dir)
        self.storage_dir.mkdir(exist_ok=True)
        self.sessions: Dict[str, Session] = {}
        self.current_session_id: Optional[str] = None
        self._load_sessions()
        
    def _load_sessions(self):
        """加载所有会话"""
        for file_path in self.storage_dir.glob("*.json"):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    session = Session.from_dict(data)
                    self.sessions[session.session_id] = session
            except Exception as e:
                print(f"⚠️  加载会话失败 {file_path}: {e}")
                
    def _save_session(self, session: Session):
        """保存单个会话"""
        file_path = self.storage_dir / f"{session.session_id}.json"
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(session.to_dict(), f, ensure_ascii=False, indent=2)
            
    def create_session(self, title: str = "新对话") -> Session:
        """创建新会话"""
        session_id = f"session_{int(time.time() * 1000)}"
        session = Session(session_id, title)
        self.sessions[session_id] = session
        self.current_session_id = session_id
        self._save_session(session)
        return session
        
    def get_session(self, session_id: str) -> Optional[Session]:
        """获取会话"""
        return self.sessions.get(session_id)
        
    def get_current_session(self) -> Optional[Session]:
        """获取当前会话"""
        if self.current_session_id:
            return self.sessions.get(self.current_session_id)
        return None
        
    def switch_session(self, session_id: str) -> bool:
        """切换会话"""
        if session_id in self.sessions:
            self.current_session_id = session_id
            return True
        return False
        
    def delete_session(self, session_id: str) -> bool:
        """删除会话"""
        if session_id in self.sessions:
            # 删除文件
            file_path = self.storage_dir / f"{session_id}.json"
            if file_path.exists():
                file_path.unlink()
            
            # 删除内存中的会话
            del self.sessions[session_id]
            
            # 如果删除的是当前会话，切换到其他会话
            if self.current_session_id == session_id:
                if self.sessions:
                    self.current_session_id = list(self.sessions.keys())[-1]
                else:
                    self.current_session_id = None
            return True
        return False
        
    def list_sessions(self) -> List[Dict]:
        """列出所有会话"""
        sessions = []
        for session in sorted(self.sessions.values(), 
                            key=lambda s: s.updated_at, 
                            reverse=True):
            sessions.append({
                "session_id": session.session_id,
                "title": session.title,
                "updated_at": session.updated_at.strftime("%Y-%m-%d %H:%M"),
                "message_count": len(session.messages)
            })
        return sessions
        
    def update_session_title(self, session_id: str, title: str):
        """更新会话标题"""
        session = self.get_session(session_id)
        if session:
            session.title = title
            session.updated_at = datetime.now()
            self._save_session(session)
            
    def add_message_to_current(self, role: str, content: str, 
                              metadata: Optional[Dict] = None):
        """向当前会话添加消息"""
        session = self.get_current_session()
        if not session:
            session = self.create_session()
        
        session.add_message(role, content, metadata)
        self._save_session(session)
        
    def save_current_session(self):
        """保存当前会话"""
        session = self.get_current_session()
        if session:
            self._save_session(session)





