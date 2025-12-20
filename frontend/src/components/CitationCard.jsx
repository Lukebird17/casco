/**
 * 引用卡片组件
 * 显示检索到的文档片段（包含文本和图片）
 */

import React from 'react';
import { FileText, Image as ImageIcon } from 'lucide-react';
import { motion } from 'framer-motion';

const CitationCard = ({ citation, index, onClick }) => {
  const { filename, page, snippet, image_url, score, id } = citation;

  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.95 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ delay: index * 0.05, duration: 0.2 }}
      onClick={() => onClick && onClick(citation)}
      className="bg-white rounded-lg border border-google-gray-200 p-4 hover:border-google-blue-300 
                 hover:shadow-md transition-all cursor-pointer group"
    >
      {/* 头部：文件名和页码 */}
      <div className="flex items-start gap-3 mb-3">
        <div className="flex-shrink-0 w-8 h-8 rounded-full bg-google-blue-50 flex items-center justify-center text-google-blue-600 font-semibold text-sm">
          {index + 1}
        </div>
        <div className="flex-1 min-w-0">
          <div className="flex items-center gap-2 mb-1">
            <FileText size={16} className="text-google-gray-400 flex-shrink-0" />
            <span className="text-sm font-medium text-google-gray-900 truncate">
              {filename}
            </span>
          </div>
          <div className="flex items-center gap-3 text-xs text-google-gray-500">
            <span>第 {page} 页</span>
            {score > 0 && (
              <span className="px-2 py-0.5 bg-green-50 text-green-600 rounded">
                相关度: {score > 1 ? score.toFixed(0) : (score * 100).toFixed(0)}%
              </span>
            )}
          </div>
        </div>
      </div>

      {/* 图片预览 */}
      {image_url && (
        <div className="mb-3 relative rounded-lg overflow-hidden border border-google-gray-200 group-hover:border-google-blue-200 transition-colors">
          <img 
            src={image_url}
            alt={`${filename} 第${page}页`}
            className="w-full h-auto object-cover max-h-48"
            loading="eager"
            onError={(e) => {
              console.error('图片加载失败:', image_url);
              e.target.style.display = 'none';
            }}
          />
          {/* 悬浮提示 */}
          <div className="absolute inset-0 bg-black/0 group-hover:bg-black/5 transition-colors flex items-center justify-center opacity-0 group-hover:opacity-100">
            <span className="bg-black/60 text-white text-xs px-3 py-1.5 rounded backdrop-blur-sm">
              点击查看详情
            </span>
          </div>
        </div>
      )}

      {/* 文本摘要 */}
      {snippet && (
        <div className="text-xs text-google-gray-600 leading-relaxed line-clamp-3">
          "{snippet}"
        </div>
      )}

      {/* 引用ID（隐藏，用于点击跳转） */}
      <div className="hidden" data-cite-id={id}></div>
    </motion.div>
  );
};

export default CitationCard;

