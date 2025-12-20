/**
 * 检索结果展示组件
 * 在等待AI回答时显示检索到的文档
 */

import React from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Search, Sparkles, Clock } from 'lucide-react';
import CitationCard from './CitationCard';

const RetrievalResults = ({ citations, onCitationClick, visible = true }) => {
  if (!visible || !citations || citations.length === 0) {
    return null;
  }

  // ✅ 获取检索时间（从第一个citation中获取，所有citation共享同一个检索时间）
  const retrievalTime = citations[0]?.retrievalTime;

  return (
    <AnimatePresence>
      <motion.div
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        exit={{ opacity: 0, y: -20 }}
        transition={{ duration: 0.3 }}
        className="my-6 bg-gradient-to-br from-google-blue-50 to-purple-50 rounded-xl p-6 border border-google-blue-100"
      >
        {/* 标题 */}
        <div className="flex items-center gap-3 mb-4">
          <div className="flex items-center justify-center w-10 h-10 rounded-full bg-google-blue-500 text-white">
            <Search size={20} />
          </div>
          <div className="flex-1">
            <h3 className="text-lg font-semibold text-google-gray-900 flex items-center gap-2">
              找到相关文档
              <Sparkles size={16} className="text-yellow-500" />
            </h3>
            <p className="text-sm text-google-gray-600 flex items-center gap-2">
              正在基于以下 {citations.length} 个文档生成回答...
              {/* ✅ 显示检索时间 */}
              {retrievalTime !== undefined && (
                <span className="inline-flex items-center gap-1 text-google-blue-600 font-medium">
                  <Clock size={14} />
                  检索耗时 {retrievalTime}秒
                </span>
              )}
            </p>
          </div>
        </div>

        {/* 引用卡片网格 */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {citations.map((citation, index) => (
            <CitationCard
              key={`${citation.id}-${index}`}
              citation={citation}
              index={index}
              onClick={onCitationClick}
            />
          ))}
        </div>

        {/* 底部提示 */}
        <div className="mt-4 text-xs text-google-gray-500 text-center">
          💡 点击卡片可以查看完整文档内容
        </div>
      </motion.div>
    </AnimatePresence>
  );
};

export default RetrievalResults;

