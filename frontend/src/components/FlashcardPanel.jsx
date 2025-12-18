/**
 * 记忆闪卡面板
 */

import React, { useState, useEffect } from 'react';
import { X, Lightbulb, RotateCcw, Check, ArrowRight } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import toast from 'react-hot-toast';
import axios from 'axios';

const FlashcardPanel = ({ open, onClose }) => {
  const [cards, setCards] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [showAnswer, setShowAnswer] = useState(false);
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(false);

  // 加载到期闪卡
  useEffect(() => {
    if (open) {
      loadDueCards();
      loadStats();
    }
  }, [open]);

  const loadDueCards = async () => {
    setLoading(true);
    try {
      const response = await axios.get('http://localhost:8000/api/flashcards/due');
      if (response.data.success) {
        setCards(response.data.flashcards);
        setCurrentIndex(0);
        setShowAnswer(false);
      }
    } catch (error) {
      console.error('加载闪卡失败:', error);
      toast.error('加载闪卡失败');
    } finally {
      setLoading(false);
    }
  };

  const loadStats = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/flashcards/stats');
      if (response.data.success) {
        setStats(response.data);
      }
    } catch (error) {
      console.error('加载统计失败:', error);
    }
  };

  // 复习闪卡
  const handleReview = async (quality) => {
    const currentCard = cards[currentIndex];
    try {
      await axios.post('http://localhost:8000/api/flashcards/review', {
        card_id: currentCard.id,
        quality
      });

      toast.success('已记录');
      
      // 移动到下一张
      if (currentIndex < cards.length - 1) {
        setCurrentIndex(currentIndex + 1);
        setShowAnswer(false);
      } else {
        // 全部完成
        toast.success('今天的复习完成了！');
        loadDueCards();
        loadStats();
      }
    } catch (error) {
      console.error('复习失败:', error);
      toast.error('记录失败');
    }
  };

  const currentCard = cards[currentIndex];
  const progress = cards.length > 0 ? ((currentIndex + 1) / cards.length) * 100 : 0;

  return (
    <AnimatePresence>
      {open && (
        <motion.div
          initial={{ x: '100%' }}
          animate={{ x: 0 }}
          exit={{ x: '100%' }}
          transition={{ type: 'spring', damping: 25 }}
          className="fixed right-0 top-0 bottom-0 w-[480px] bg-white border-l 
                   border-google-gray-200 shadow-lg z-50 flex flex-col"
        >
          {/* 头部 */}
          <div className="sticky top-0 bg-white border-b border-google-gray-200 p-4">
            <div className="flex items-center justify-between mb-3">
              <div className="flex items-center gap-2">
                <Lightbulb size={20} className="text-google-blue-600" />
                <h2 className="font-semibold text-google-gray-900">记忆闪卡</h2>
              </div>
              <button
                onClick={onClose}
                className="btn-icon p-2 hover:bg-google-gray-100 rounded-lg"
              >
                <X size={20} />
              </button>
            </div>

            {/* 统计 */}
            {stats && (
              <div className="grid grid-cols-4 gap-2 text-center">
                <div className="bg-google-gray-50 rounded p-2">
                  <div className="text-lg font-bold text-google-blue-600">{stats.total_cards}</div>
                  <div className="text-xs text-google-gray-600">总数</div>
                </div>
                <div className="bg-google-gray-50 rounded p-2">
                  <div className="text-lg font-bold text-orange-600">{stats.due_today}</div>
                  <div className="text-xs text-google-gray-600">待复习</div>
                </div>
                <div className="bg-google-gray-50 rounded p-2">
                  <div className="text-lg font-bold text-green-600">{stats.mastered}</div>
                  <div className="text-xs text-google-gray-600">已掌握</div>
                </div>
                <div className="bg-google-gray-50 rounded p-2">
                  <div className="text-lg font-bold text-google-blue-600">{stats.average_accuracy}%</div>
                  <div className="text-xs text-google-gray-600">准确率</div>
                </div>
              </div>
            )}
          </div>

          {/* 内容区域 */}
          <div className="flex-1 overflow-y-auto p-4">
            {loading ? (
              <div className="text-center py-20 text-google-gray-500">
                <div className="animate-spin h-8 w-8 border-4 border-google-blue-500 border-t-transparent rounded-full mx-auto mb-2"></div>
                加载中...
              </div>
            ) : cards.length === 0 ? (
              <div className="text-center py-20 text-google-gray-500">
                <Lightbulb size={48} className="mx-auto mb-3 opacity-30" />
                <p>🎉 太棒了！</p>
                <p className="text-sm mt-1">暂时没有需要复习的卡片</p>
              </div>
            ) : currentCard ? (
              <div className="space-y-4">
                {/* 进度 */}
                <div>
                  <div className="flex items-center justify-between text-sm text-google-gray-600 mb-1">
                    <span>第 {currentIndex + 1} / {cards.length} 张</span>
                    <span>{Math.round(progress)}%</span>
                  </div>
                  <div className="w-full bg-google-gray-200 rounded-full h-2">
                    <div 
                      className="h-full bg-google-blue-500 rounded-full transition-all"
                      style={{ width: `${progress}%` }}
                    />
                  </div>
                </div>

                {/* 卡片 */}
                <div 
                  className="relative h-64 cursor-pointer"
                  onClick={() => setShowAnswer(!showAnswer)}
                >
                  <AnimatePresence mode="wait">
                    <motion.div
                      key={showAnswer ? 'back' : 'front'}
                      initial={{ rotateY: 90, opacity: 0 }}
                      animate={{ rotateY: 0, opacity: 1 }}
                      exit={{ rotateY: -90, opacity: 0 }}
                      transition={{ duration: 0.3 }}
                      className="absolute inset-0 bg-gradient-to-br from-google-blue-500 to-google-blue-600 
                               rounded-xl shadow-lg p-6 flex items-center justify-center text-white"
                    >
                      <div className="text-center">
                        <div className="text-sm mb-2 opacity-90">
                          {showAnswer ? '答案' : '问题'}
                        </div>
                        <div className="text-lg font-medium">
                          {showAnswer ? currentCard.back : currentCard.front}
                        </div>
                        <div className="text-xs mt-4 opacity-75">
                          点击翻转卡片
                        </div>
                      </div>
                    </motion.div>
                  </AnimatePresence>
                </div>

                {/* 评分按钮（仅在显示答案后） */}
                {showAnswer && (
                  <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    className="space-y-2"
                  >
                    <p className="text-sm text-google-gray-600 text-center mb-3">
                      你回答得怎么样？
                    </p>
                    
                    <button
                      onClick={() => handleReview(0)}
                      className="w-full py-3 bg-red-50 border border-red-200 rounded-lg
                               text-red-700 hover:bg-red-100 transition-colors"
                    >
                      😵 完全不记得
                    </button>
                    
                    <button
                      onClick={() => handleReview(3)}
                      className="w-full py-3 bg-yellow-50 border border-yellow-200 rounded-lg
                               text-yellow-700 hover:bg-yellow-100 transition-colors"
                    >
                      🤔 很困难
                    </button>
                    
                    <button
                      onClick={() => handleReview(4)}
                      className="w-full py-3 bg-green-50 border border-green-200 rounded-lg
                               text-green-700 hover:bg-green-100 transition-colors"
                    >
                      😊 有些犹豫
                    </button>
                    
                    <button
                      onClick={() => handleReview(5)}
                      className="w-full py-3 bg-google-blue-50 border border-google-blue-200 rounded-lg
                               text-google-blue-700 hover:bg-google-blue-100 transition-colors"
                    >
                      🎯 完全正确
                    </button>
                  </motion.div>
                )}

                {/* 卡片信息 */}
                {currentCard.source && (
                  <div className="text-xs text-google-gray-500 text-center">
                    来源: {currentCard.source}
                  </div>
                )}
              </div>
            ) : null}
          </div>
        </motion.div>
      )}
    </AnimatePresence>
  );
};

export default FlashcardPanel;


