/**
 * 置信度详情面板
 * 显示答案置信度和详细评分指标
 */

import React from 'react';
import { X, TrendingUp, AlertTriangle, CheckCircle, Info } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

const ConfidencePanel = ({ open, onClose, confidence }) => {
  if (!confidence) return null;

  const getScoreColor = (score) => {
    if (score >= 0.8) return 'text-green-600';
    if (score >= 0.6) return 'text-yellow-600';
    return 'text-red-600';
  };

  const getScoreBackground = (score) => {
    if (score >= 0.8) return 'bg-green-50';
    if (score >= 0.6) return 'bg-yellow-50';
    return 'bg-red-50';
  };

  const getScoreBorder = (score) => {
    if (score >= 0.8) return 'border-green-200';
    if (score >= 0.6) return 'border-yellow-200';
    return 'border-red-200';
  };

  const getReliabilityLabel = (score) => {
    if (score >= 0.8) return { label: '高可靠', icon: CheckCircle, color: 'green' };
    if (score >= 0.6) return { label: '中等可靠', icon: Info, color: 'yellow' };
    return { label: '低可靠', icon: AlertTriangle, color: 'red' };
  };

  const reliability = getReliabilityLabel(confidence.score);
  const ReliabilityIcon = reliability.icon;

  // 阈值说明表
  const thresholds = [
    { range: '≥ 80%', label: '高可靠', description: '答案基于充分的文档证据，可直接使用', color: 'green' },
    { range: '60-79%', label: '中等可靠', description: '答案有一定依据，建议对照原文确认', color: 'yellow' },
    { range: '< 60%', label: '低可靠', description: '证据不足或相关性较弱，需谨慎对待', color: 'red' },
  ];

  // 评分维度
  const dimensions = confidence.dimensions || {
    retrieval_quality: confidence.score,
    context_relevance: confidence.score,
    answer_completeness: confidence.score,
  };

  return (
    <AnimatePresence>
      {open && (
        <>
          {/* 背景遮罩 */}
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={onClose}
            className="fixed inset-0 bg-black/30 z-40"
          />

          {/* 面板主体 */}
          <motion.div
            initial={{ x: '100%' }}
            animate={{ x: 0 }}
            exit={{ x: '100%' }}
            transition={{ type: 'spring', damping: 25 }}
            className="fixed right-0 top-0 bottom-0 w-[420px] bg-white shadow-2xl z-50 
                     overflow-y-auto"
          >
            {/* 头部 */}
            <div className="sticky top-0 bg-white border-b border-google-gray-200 p-6 flex items-center justify-between z-10">
              <div className="flex items-center gap-3">
                <TrendingUp size={24} className="text-google-blue-600" />
                <h2 className="text-xl font-semibold text-google-gray-900">答案置信度</h2>
              </div>
              <button
                onClick={onClose}
                className="btn-icon p-2 hover:bg-google-gray-100 rounded-lg"
              >
                <X size={20} />
              </button>
            </div>

            <div className="p-6 space-y-6">
              {/* 总体置信度 */}
              <div className={`rounded-2xl p-6 border-2 ${getScoreBackground(confidence.score)} ${getScoreBorder(confidence.score)}`}>
                <div className="flex items-center justify-between mb-4">
                  <span className="text-sm font-medium text-google-gray-600">综合置信度</span>
                  <div className={`flex items-center gap-2 px-3 py-1 rounded-full ${
                    reliability.color === 'green' ? 'bg-green-100 text-green-700' :
                    reliability.color === 'yellow' ? 'bg-yellow-100 text-yellow-700' :
                    'bg-red-100 text-red-700'
                  }`}>
                    <ReliabilityIcon size={14} />
                    <span className="text-xs font-semibold">{reliability.label}</span>
                  </div>
                </div>

                <div className="flex items-end gap-3 mb-2">
                  <span className={`text-5xl font-bold ${getScoreColor(confidence.score)}`}>
                    {(confidence.score * 100).toFixed(0)}
                  </span>
                  <span className="text-2xl font-medium text-google-gray-500 pb-2">%</span>
                </div>

                {/* 进度条 */}
                <div className="relative h-3 bg-google-gray-200 rounded-full overflow-hidden">
                  <motion.div
                    initial={{ width: 0 }}
                    animate={{ width: `${confidence.score * 100}%` }}
                    transition={{ duration: 1, ease: 'easeOut' }}
                    className={`h-full rounded-full ${
                      confidence.score >= 0.8 ? 'bg-green-500' :
                      confidence.score >= 0.6 ? 'bg-yellow-500' :
                      'bg-red-500'
                    }`}
                  />
                </div>

                {confidence.explanation && (
                  <p className="mt-4 text-sm text-google-gray-700 leading-relaxed">
                    {confidence.explanation}
                  </p>
                )}
              </div>

              {/* 评分维度 */}
              <div className="space-y-3">
                <h3 className="text-sm font-semibold text-google-gray-900 mb-3">评分维度</h3>
                
                <div className="space-y-3">
                  <DimensionScore
                    label="检索质量"
                    score={dimensions.retrieval_quality}
                    description="检索到的文档与问题的相关度"
                  />
                  <DimensionScore
                    label="上下文相关性"
                    score={dimensions.context_relevance}
                    description="上下文与问题的契合程度"
                  />
                  <DimensionScore
                    label="答案完整性"
                    score={dimensions.answer_completeness}
                    description="答案是否全面回答了问题"
                  />
                </div>
              </div>

              {/* 阈值说明表 */}
              <div className="bg-google-gray-50 rounded-xl p-5">
                <h3 className="text-sm font-semibold text-google-gray-900 mb-4 flex items-center gap-2">
                  <Info size={16} />
                  置信度阈值说明
                </h3>
                <div className="space-y-3">
                  {thresholds.map((threshold, index) => (
                    <div key={index} className="flex gap-3">
                      <div className={`w-16 flex-shrink-0 text-center py-1 px-2 rounded-lg text-xs font-semibold ${
                        threshold.color === 'green' ? 'bg-green-100 text-green-700' :
                        threshold.color === 'yellow' ? 'bg-yellow-100 text-yellow-700' :
                        'bg-red-100 text-red-700'
                      }`}>
                        {threshold.range}
                      </div>
                      <div className="flex-1">
                        <div className="text-sm font-medium text-google-gray-900">
                          {threshold.label}
                        </div>
                        <div className="text-xs text-google-gray-600 mt-0.5">
                          {threshold.description}
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              </div>

              {/* 使用建议 */}
              <div className={`rounded-xl p-5 border ${
                confidence.score >= 0.8 ? 'bg-green-50 border-green-200' :
                confidence.score >= 0.6 ? 'bg-yellow-50 border-yellow-200' :
                'bg-red-50 border-red-200'
              }`}>
                <h3 className="text-sm font-semibold text-google-gray-900 mb-2">💡 使用建议</h3>
                <p className="text-sm text-google-gray-700 leading-relaxed">
                  {confidence.score >= 0.8
                    ? '本答案基于充分的文档证据生成，可以直接使用。如需深入了解，可查看引用来源。'
                    : confidence.score >= 0.6
                    ? '本答案有一定的文档依据，但建议您对照右侧的引用来源进行确认，确保理解准确。'
                    : '检索到的文档与问题相关性较弱，建议您查看原始文档或尝试换一个表述重新提问。'}
                </p>
              </div>
            </div>
          </motion.div>
        </>
      )}
    </AnimatePresence>
  );
};

// 维度评分子组件
const DimensionScore = ({ label, score, description }) => {
  const getColor = (score) => {
    if (score >= 0.8) return 'bg-green-500';
    if (score >= 0.6) return 'bg-yellow-500';
    return 'bg-red-500';
  };

  return (
    <div className="bg-white rounded-lg p-4 border border-google-gray-200">
      <div className="flex items-center justify-between mb-2">
        <span className="text-sm font-medium text-google-gray-900">{label}</span>
        <span className="text-sm font-bold text-google-gray-700">
          {(score * 100).toFixed(0)}%
        </span>
      </div>
      <div className="relative h-2 bg-google-gray-200 rounded-full overflow-hidden mb-2">
        <motion.div
          initial={{ width: 0 }}
          animate={{ width: `${score * 100}%` }}
          transition={{ duration: 0.8, ease: 'easeOut' }}
          className={`h-full rounded-full ${getColor(score)}`}
        />
      </div>
      <p className="text-xs text-google-gray-600">{description}</p>
    </div>
  );
};

export default ConfidencePanel;




