#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
记忆闪卡系统
使用 SM-2 算法实现间隔重复学习
"""

import json
import time
from pathlib import Path
from typing import List, Dict, Optional
from datetime import datetime, timedelta


class Flashcard:
    """单个闪卡"""
    
    def __init__(self, front: str, back: str, source: str = "", tags: List[str] = None):
        self.id = f"card_{int(time.time() * 1000)}"
        self.front = front  # 正面（问题）
        self.back = back    # 背面（答案）
        self.source = source  # 来源
        self.tags = tags or []
        
        # SM-2 算法参数
        self.easiness_factor = 2.5  # 容易度因子 (2.5是初始值)
        self.interval = 0           # 复习间隔（天）
        self.repetitions = 0        # 重复次数
        self.next_review = datetime.now()  # 下次复习时间
        
        # 统计信息
        self.created_at = datetime.now()
        self.total_reviews = 0
        self.correct_reviews = 0
    
    def to_dict(self) -> Dict:
        """转换为字典"""
        return {
            'id': self.id,
            'front': self.front,
            'back': self.back,
            'source': self.source,
            'tags': self.tags,
            'easiness_factor': self.easiness_factor,
            'interval': self.interval,
            'repetitions': self.repetitions,
            'next_review': self.next_review.isoformat(),
            'created_at': self.created_at.isoformat(),
            'total_reviews': self.total_reviews,
            'correct_reviews': self.correct_reviews
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Flashcard':
        """从字典创建"""
        card = cls(data['front'], data['back'], data.get('source', ''), data.get('tags', []))
        card.id = data['id']
        card.easiness_factor = data.get('easiness_factor', 2.5)
        card.interval = data.get('interval', 0)
        card.repetitions = data.get('repetitions', 0)
        card.next_review = datetime.fromisoformat(data['next_review'])
        card.created_at = datetime.fromisoformat(data['created_at'])
        card.total_reviews = data.get('total_reviews', 0)
        card.correct_reviews = data.get('correct_reviews', 0)
        return card


class FlashcardSystem:
    """闪卡系统管理器"""
    
    def __init__(self, storage_file: str = "./flashcards.json"):
        self.storage_file = Path(storage_file)
        self.cards: Dict[str, Flashcard] = {}
        self._load_cards()
    
    def _load_cards(self):
        """加载闪卡"""
        if self.storage_file.exists():
            try:
                with open(self.storage_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for card_data in data:
                        card = Flashcard.from_dict(card_data)
                        self.cards[card.id] = card
            except Exception as e:
                print(f"⚠️  加载闪卡失败: {e}")
    
    def _save_cards(self):
        """保存闪卡"""
        try:
            with open(self.storage_file, 'w', encoding='utf-8') as f:
                cards_data = [card.to_dict() for card in self.cards.values()]
                json.dump(cards_data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"⚠️  保存闪卡失败: {e}")
    
    def create_card(self, front: str, back: str, source: str = "", tags: List[str] = None) -> Flashcard:
        """创建新闪卡"""
        card = Flashcard(front, back, source, tags)
        self.cards[card.id] = card
        self._save_cards()
        return card
    
    def get_card(self, card_id: str) -> Optional[Flashcard]:
        """获取闪卡"""
        return self.cards.get(card_id)
    
    def get_due_cards(self, limit: int = 20) -> List[Flashcard]:
        """获取到期需要复习的闪卡"""
        now = datetime.now()
        due_cards = [
            card for card in self.cards.values()
            if card.next_review <= now
        ]
        # 按到期时间排序，越早到期的越靠前
        due_cards.sort(key=lambda c: c.next_review)
        return due_cards[:limit]
    
    def update_card_review(self, card_id: str, quality: int):
        """
        更新闪卡复习记录（SM-2算法）
        
        参数:
            card_id: 闪卡ID
            quality: 回答质量 (0-5)
                0: 完全不记得
                1: 错误，但看到答案后想起来了
                2: 错误，但很接近
                3: 正确，但很困难
                4: 正确，有些犹豫
                5: 完全正确，毫不费力
        """
        card = self.cards.get(card_id)
        if not card:
            return
        
        # 更新统计
        card.total_reviews += 1
        if quality >= 3:
            card.correct_reviews += 1
        
        # SM-2 算法
        if quality < 3:
            # 回答错误，重置
            card.repetitions = 0
            card.interval = 0
            card.next_review = datetime.now()
        else:
            # 回答正确
            if card.repetitions == 0:
                card.interval = 1
            elif card.repetitions == 1:
                card.interval = 6
            else:
                card.interval = int(card.interval * card.easiness_factor)
            
            card.repetitions += 1
            card.next_review = datetime.now() + timedelta(days=card.interval)
        
        # 更新容易度因子
        card.easiness_factor = max(1.3, card.easiness_factor + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02)))
        
        self._save_cards()
    
    def get_statistics(self) -> Dict:
        """获取学习统计"""
        total = len(self.cards)
        if total == 0:
            return {
                'total_cards': 0,
                'due_today': 0,
                'mastered': 0,
                'learning': 0,
                'average_accuracy': 0
            }
        
        now = datetime.now()
        due_today = sum(1 for card in self.cards.values() if card.next_review <= now)
        mastered = sum(1 for card in self.cards.values() if card.repetitions >= 5)
        learning = total - mastered
        
        total_reviews = sum(card.total_reviews for card in self.cards.values())
        correct_reviews = sum(card.correct_reviews for card in self.cards.values())
        average_accuracy = (correct_reviews / total_reviews * 100) if total_reviews > 0 else 0
        
        return {
            'total_cards': total,
            'due_today': due_today,
            'mastered': mastered,
            'learning': learning,
            'average_accuracy': round(average_accuracy, 1)
        }
    
    def search_cards(self, query: str) -> List[Flashcard]:
        """搜索闪卡"""
        query_lower = query.lower()
        results = []
        for card in self.cards.values():
            if (query_lower in card.front.lower() or 
                query_lower in card.back.lower() or 
                query_lower in card.source.lower() or
                any(query_lower in tag.lower() for tag in card.tags)):
                results.append(card)
        return results
    
    def delete_card(self, card_id: str) -> bool:
        """删除闪卡"""
        if card_id in self.cards:
            del self.cards[card_id]
            self._save_cards()
            return True
        return False


if __name__ == "__main__":
    # 测试
    system = FlashcardSystem("./test_flashcards.json")
    
    # 创建测试卡片
    card1 = system.create_card(
        "什么是虚拟内存？",
        "虚拟内存是一种内存管理技术，使应用程序认为它拥有连续可用的内存。",
        "操作系统课程",
        ["内存管理", "虚拟内存"]
    )
    
    print(f"创建闪卡: {card1.id}")
    print(f"统计: {system.get_statistics()}")
    
    # 获取到期卡片
    due_cards = system.get_due_cards()
    print(f"\n到期卡片数: {len(due_cards)}")
    
    if due_cards:
        # 模拟复习
        card = due_cards[0]
        print(f"\n复习: {card.front}")
        print(f"答案: {card.back}")
        
        # 模拟回答质量为4（正确但有些犹豫）
        system.update_card_review(card.id, quality=4)
        print(f"下次复习: {card.next_review}")
