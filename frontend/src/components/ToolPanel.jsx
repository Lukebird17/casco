/**
 * 工具面板组件
 * 右侧工具栏（置信度、引用、片段等）
 */

import React from 'react';
import { X, TrendingUp, Quote, Bookmark, Info } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import { QualityMetricsDisplay } from './QualityMetrics';

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
            <div className="flex items-start gap-2 mb-2">
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
              </div>
            </div>
            
            {/* 图片预览 */}
            {citation.image_url && (
              <div className="mb-2 rounded overflow-hidden border border-google-gray-200 group-hover:border-google-blue-200 transition-colors">
                <img 
                  src={citation.image_url} 
                  alt={`${citation.filename} 第${citation.page}页`}
                  className="w-full h-auto object-cover max-h-48"
                  loading="lazy"
                  onError={(e) => {
                    e.target.style.display = 'none';
                  }}
                />
                {/* 悬浮提示 */}
                <div className="absolute inset-0 bg-black/0 group-hover:bg-black/5 transition-colors flex items-center justify-center opacity-0 group-hover:opacity-100">
                  <span className="bg-black/60 text-white text-xs px-2 py-1 rounded backdrop-blur-sm">
                    点击查看详情
                  </span>
                </div>
              </div>
            )}
            
            {/* 文本摘要 */}
            {citation.snippet && (
              <div className="text-xs text-google-gray-600 line-clamp-2">
                {citation.snippet}
              </div>
            )}
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
  qualityMetrics,  // 新增：质量评估数据
}) => {
  return (
    <AnimatePresence>
      {open && (
        <motion.div
          initial={{ width: 0, opacity: 0 }}
          animate={{ width: 384, opacity: 1 }}
          exit={{ width: 0, opacity: 0 }}
          transition={{ type: 'spring', damping: 30, stiffness: 300 }}
          className="fixed left-[280px] top-0 bottom-0 bg-google-gray-50 border-r 
                   border-google-gray-200 shadow-lg z-20 flex flex-col"
        >
          {/* 头部 */}
          <div className="flex-shrink-0 bg-white border-b border-google-gray-200 p-4 flex items-center justify-between">
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

          {/* 内容 - 可滚动 */}
          <div className="flex-1 overflow-y-auto p-4 space-y-4">
            {/* ✅ 优先显示质量评估（雷达图） */}
            {qualityMetrics && <QualityMetricsDisplay metrics={qualityMetrics} />}
            
            {/* ✅ 如果没有质量评估且答案已生成，显示"正在生成"提示 */}
            {!qualityMetrics && citations && citations.length > 0 && (
              <div className="bg-white rounded-xl shadow-sm border border-google-gray-200 p-5">
                <div className="flex items-center gap-2 mb-3">
                  <TrendingUp size={20} className="text-google-blue-600 animate-pulse" />
                  <h3 className="font-semibold text-google-gray-900">AI 自省报告</h3>
                </div>
                <div className="flex flex-col items-center justify-center py-8">
                  <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-google-blue-600 mb-4"></div>
                  <p className="text-sm text-google-gray-600">正在生成质量评估报告...</p>
                  <p className="text-xs text-google-gray-500 mt-2">
                    这可能需要10-30秒，请稍候
                  </p>
                </div>
              </div>
            )}
            
            {/* 如果没有质量评估也没有引用，显示简单的置信度 */}
            {!qualityMetrics && !citations && confidence && <ConfidenceDisplay confidence={confidence} />}
            
            {/* 引用列表 */}
            <CitationsList citations={citations} onJump={onJumpToCitation} />
          </div>
        </motion.div>
      )}
    </AnimatePresence>
  );
};

export default ToolPanel;





