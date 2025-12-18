/**
 * 文档热力图面板
 */

import React, { useState, useEffect } from 'react';
import { X, TrendingUp, FileText, MapPin } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import toast from 'react-hot-toast';
import { getHeatmap } from '../api/client';

const HeatmapPanel = ({ open, onClose }) => {
  const [heatmapData, setHeatmapData] = useState(null);
  const [loading, setLoading] = useState(false);

  // 加载热力图数据
  useEffect(() => {
    if (open) {
      loadHeatmap();
    }
  }, [open]);

  const loadHeatmap = async () => {
    setLoading(true);
    try {
      const data = await getHeatmap();
      if (data.success) {
        setHeatmapData(data.heatmap);
      }
    } catch (error) {
      console.error('加载热力图失败:', error);
      toast.error('加载热力图失败');
    } finally {
      setLoading(false);
    }
  };

  // 获取进度条宽度百分比
  const getBarWidth = (count, maxCount) => {
    return (count / maxCount) * 100;
  };

  // 获取颜色类
  const getColorClass = (count, maxCount) => {
    const percentage = (count / maxCount) * 100;
    if (percentage >= 80) return 'bg-red-500';
    if (percentage >= 60) return 'bg-orange-500';
    if (percentage >= 40) return 'bg-yellow-500';
    if (percentage >= 20) return 'bg-google-blue-500';
    return 'bg-google-blue-300';
  };

  const maxDocCount = heatmapData?.top_documents?.[0]?.count || 1;
  const maxPageCount = heatmapData?.top_pages?.[0]?.count || 1;

  return (
    <AnimatePresence>
      {open && (
        <motion.div
          initial={{ x: '100%' }}
          animate={{ x: 0 }}
          exit={{ x: '100%' }}
          transition={{ type: 'spring', damping: 25 }}
          className="fixed right-0 top-0 bottom-0 w-96 bg-white border-l 
                   border-google-gray-200 shadow-lg z-50 flex flex-col"
        >
          {/* 头部 */}
          <div className="sticky top-0 bg-white border-b border-google-gray-200 p-4">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-2">
                <TrendingUp size={20} className="text-google-blue-600" />
                <h2 className="font-semibold text-google-gray-900">文档热力图</h2>
              </div>
              <button
                onClick={onClose}
                className="btn-icon p-2 hover:bg-google-gray-100 rounded-lg"
              >
                <X size={20} />
              </button>
            </div>
          </div>

          {/* 内容 */}
          <div className="flex-1 overflow-y-auto p-4">
            {loading ? (
              <div className="text-center py-8 text-google-gray-500">
                <div className="animate-spin h-8 w-8 border-4 border-google-blue-500 border-t-transparent rounded-full mx-auto mb-2"></div>
                加载中...
              </div>
            ) : heatmapData ? (
              <div className="space-y-6">
                {/* 总览 */}
                <div className="bg-google-blue-50 rounded-lg p-4">
                  <div className="text-center">
                    <div className="text-3xl font-bold text-google-blue-700">
                      {heatmapData.total_citations}
                    </div>
                    <div className="text-sm text-google-gray-600 mt-1">
                      总引用次数
                    </div>
                  </div>
                </div>

                {/* 热门文档 */}
                <div>
                  <div className="flex items-center gap-2 mb-3">
                    <FileText size={16} className="text-google-blue-600" />
                    <h3 className="font-medium text-google-gray-900">
                      热门文档 TOP 10
                    </h3>
                  </div>
                  
                  {heatmapData.top_documents && heatmapData.top_documents.length > 0 ? (
                    <div className="space-y-3">
                      {heatmapData.top_documents.map((doc, index) => (
                        <motion.div
                          key={index}
                          initial={{ opacity: 0, x: -20 }}
                          animate={{ opacity: 1, x: 0 }}
                          transition={{ delay: index * 0.05 }}
                          className="bg-google-gray-50 rounded-lg p-3"
                        >
                          <div className="flex items-center justify-between mb-2">
                            <span className="text-sm font-medium text-google-gray-800 truncate flex-1">
                              {doc.filename}
                            </span>
                            <span className="text-sm font-bold text-google-blue-700 ml-2">
                              {doc.count}次
                            </span>
                          </div>
                          <div className="w-full bg-google-gray-200 rounded-full h-2 overflow-hidden">
                            <motion.div
                              initial={{ width: 0 }}
                              animate={{ width: `${getBarWidth(doc.count, maxDocCount)}%` }}
                              transition={{ duration: 0.5, delay: index * 0.05 }}
                              className={`h-full ${getColorClass(doc.count, maxDocCount)} rounded-full`}
                            />
                          </div>
                        </motion.div>
                      ))}
                    </div>
                  ) : (
                    <p className="text-sm text-google-gray-500">暂无数据</p>
                  )}
                </div>

                {/* 热门页面 */}
                <div>
                  <div className="flex items-center gap-2 mb-3">
                    <MapPin size={16} className="text-google-blue-600" />
                    <h3 className="font-medium text-google-gray-900">
                      热门页面 TOP 20
                    </h3>
                  </div>
                  
                  {heatmapData.top_pages && heatmapData.top_pages.length > 0 ? (
                    <div className="space-y-2">
                      {heatmapData.top_pages.map((page, index) => (
                        <motion.div
                          key={index}
                          initial={{ opacity: 0, x: -20 }}
                          animate={{ opacity: 1, x: 0 }}
                          transition={{ delay: index * 0.03 }}
                          className="flex items-center justify-between p-2 bg-google-gray-50 
                                   rounded hover:bg-google-gray-100 transition-colors"
                        >
                          <span className="text-xs text-google-gray-700 truncate flex-1">
                            {page.location}
                          </span>
                          <span className="text-xs font-medium text-google-blue-600 ml-2">
                            {page.count}
                          </span>
                        </motion.div>
                      ))}
                    </div>
                  ) : (
                    <p className="text-sm text-google-gray-500">暂无数据</p>
                  )}
                </div>
              </div>
            ) : (
              <div className="text-center py-8 text-google-gray-500">
                <TrendingUp size={48} className="mx-auto mb-3 opacity-30" />
                <p>暂无热力图数据</p>
              </div>
            )}
          </div>
        </motion.div>
      )}
    </AnimatePresence>
  );
};

export default HeatmapPanel;





