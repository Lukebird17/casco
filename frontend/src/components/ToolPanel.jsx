/**
 * 工具面板组件
 * 右侧工具栏（置信度、引用、片段等）
 */

import React from 'react';
import { X, TrendingUp, Quote, Bookmark, Info } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

const ConfidenceDisplay = ({ confidence }) => {
  if (!confidence) return null;

  const getColor = (score) => {
    if (score >= 0.8) return 'text-green-600 bg-green-50';
    if (score >= 0.6) return 'text-yellow-600 bg-yellow-50';
    return 'text-red-600 bg-red-50';
  };

  const getLabel = (score) => {
    if (score >= 0.8) return '高';
    if (score >= 0.6) return '中';
    return '低';
  };

  return (
    <div className="bg-white rounded-lg shadow-sm border border-google-gray-200 p-4">
      <div className="flex items-center gap-2 mb-3">
        <TrendingUp size={18} className="text-google-blue-600" />
        <h3 className="font-medium text-google-gray-900">答案置信度</h3>
      </div>

      <div className={`inline-flex items-center gap-2 px-3 py-2 rounded-lg ${getColor(confidence.score)}`}>
        <span className="text-2xl font-bold">{(confidence.score * 100).toFixed(0)}%</span>
        <span className="text-sm font-medium">{getLabel(confidence.score)}</span>
      </div>

      {confidence.explanation && (
        <p className="mt-3 text-sm text-google-gray-600">{confidence.explanation}</p>
      )}
    </div>
  );
};

const CitationsList = ({ citations, onJump }) => {
  if (!citations || citations.length === 0) return null;

  return (
    <div className="bg-white rounded-lg shadow-sm border border-google-gray-200 p-4">
      <div className="flex items-center gap-2 mb-3">
        <Quote size={18} className="text-google-blue-600" />
        <h3 className="font-medium text-google-gray-900">引用来源</h3>
      </div>

      <div className="space-y-2">
        {citations.map((citation, index) => (
          <button
            key={index}
            onClick={() => onJump && onJump(citation)}
            className="w-full text-left p-3 rounded-lg border border-google-gray-200 
                     hover:border-google-blue-300 hover:bg-google-blue-50 
                     transition-colors group"
          >
            <div className="flex items-start gap-2">
              <span className="text-xs font-medium text-google-gray-500 mt-0.5">
                [{index + 1}]
              </span>
              <div className="flex-1 min-w-0">
                <div className="text-sm font-medium text-google-gray-900 truncate">
                  {citation.filename || '未知文档'}
                </div>
                {citation.page && (
                  <div className="text-xs text-google-gray-500 mt-1">
                    第 {citation.page} 页
                  </div>
                )}
                {citation.snippet && (
                  <div className="text-xs text-google-gray-600 mt-2 line-clamp-2">
                    {citation.snippet}
                  </div>
                )}
              </div>
            </div>
          </button>
        ))}
      </div>
    </div>
  );
};

const ToolPanel = ({ 
  open, 
  onClose, 
  confidence, 
  citations, 
  onJumpToCitation,
}) => {
  return (
    <AnimatePresence>
      {open && (
        <motion.div
          initial={{ x: '100%' }}
          animate={{ x: 0 }}
          exit={{ x: '100%' }}
          transition={{ type: 'spring', damping: 25 }}
          className="fixed right-0 top-0 bottom-0 w-96 bg-google-gray-50 border-l 
                   border-google-gray-200 shadow-lg z-50 overflow-y-auto"
        >
          {/* 头部 */}
          <div className="sticky top-0 bg-white border-b border-google-gray-200 p-4 flex items-center justify-between">
            <div className="flex items-center gap-2">
              <Info size={20} className="text-google-blue-600" />
              <h2 className="font-semibold text-google-gray-900">详细信息</h2>
            </div>
            <button
              onClick={onClose}
              className="btn-icon p-2 hover:bg-google-gray-100 rounded-lg"
            >
              <X size={20} />
            </button>
          </div>

          {/* 内容 */}
          <div className="p-4 space-y-4">
            <ConfidenceDisplay confidence={confidence} />
            <CitationsList citations={citations} onJump={onJumpToCitation} />
          </div>
        </motion.div>
      )}
    </AnimatePresence>
  );
};

export default ToolPanel;


