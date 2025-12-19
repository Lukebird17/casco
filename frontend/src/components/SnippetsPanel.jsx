/**
 * 片段收藏面板
 */

import React, { useState, useEffect } from 'react';
import { X, Bookmark, Tag, Search, Copy, Check } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import toast from 'react-hot-toast';
import { getSnippets } from '../api/client';

const SnippetsPanel = ({ open, onClose, currentSessionId }) => {
  const [snippets, setSnippets] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [copiedId, setCopiedId] = useState(null);
  const [loading, setLoading] = useState(false);

  // 加载片段
  useEffect(() => {
    if (open) {
      loadSnippets();
    }
  }, [open]);

  const loadSnippets = async () => {
    setLoading(true);
    try {
      const data = await getSnippets();
      if (data.success) {
        setSnippets(data.snippets);
      }
    } catch (error) {
      console.error('加载片段失败:', error);
      toast.error('加载片段失败');
    } finally {
      setLoading(false);
    }
  };

  // 搜索过滤
  const filteredSnippets = snippets.filter(snippet =>
    snippet.content.toLowerCase().includes(searchQuery.toLowerCase()) ||
    snippet.source.toLowerCase().includes(searchQuery.toLowerCase()) ||
    (snippet.tags && snippet.tags.some(tag => tag.toLowerCase().includes(searchQuery.toLowerCase())))
  );

  // 复制到剪贴板
  const copyToClipboard = (text, id) => {
    navigator.clipboard.writeText(text);
    setCopiedId(id);
    toast.success('已复制到剪贴板');
    setTimeout(() => setCopiedId(null), 2000);
  };

  return (
    <AnimatePresence>
      {open && (
        <motion.div
          initial={{ width: 0, opacity: 0 }}
          animate={{ width: 384, opacity: 1 }}
          exit={{ width: 0, opacity: 0 }}
          transition={{ type: 'spring', damping: 30, stiffness: 300 }}
          className="fixed left-[280px] top-0 bottom-0 bg-white border-r 
                   border-google-gray-200 shadow-lg z-20 flex flex-col"
        >
          {/* 头部 */}
          <div className="flex-shrink-0 bg-white border-b border-google-gray-200 p-4">
            <div className="flex items-center justify-between mb-3">
              <div className="flex items-center gap-2">
                <Bookmark size={20} className="text-google-blue-600" />
                <h2 className="font-semibold text-google-gray-900">我的片段</h2>
              </div>
              <button
                onClick={onClose}
                className="btn-icon p-2 hover:bg-google-gray-100 rounded-lg"
              >
                <X size={20} />
              </button>
            </div>

            {/* 搜索框 */}
            <div className="relative">
              <Search size={16} className="absolute left-3 top-1/2 transform -translate-y-1/2 text-google-gray-500" />
              <input
                type="text"
                placeholder="搜索片段..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="w-full pl-10 pr-3 py-2 border border-google-gray-300 rounded-lg
                         focus:outline-none focus:ring-2 focus:ring-google-blue-500 text-sm"
              />
            </div>
          </div>

          {/* 片段列表 */}
          <div className="flex-1 overflow-y-auto p-4">
            {loading ? (
              <div className="text-center py-8 text-google-gray-500">
                <div className="animate-spin h-8 w-8 border-4 border-google-blue-500 border-t-transparent rounded-full mx-auto mb-2"></div>
                加载中...
              </div>
            ) : filteredSnippets.length === 0 ? (
              <div className="text-center py-8 text-google-gray-500">
                <Bookmark size={48} className="mx-auto mb-3 opacity-30" />
                <p>{searchQuery ? '没有找到匹配的片段' : '还没有收藏片段'}</p>
                <p className="text-xs mt-1">在对话中点击「收藏」按钮保存有用的内容</p>
              </div>
            ) : (
              <div className="space-y-3">
                {filteredSnippets.map((snippet, index) => (
                  <motion.div
                    key={snippet.id || index}
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: index * 0.05 }}
                    className="bg-google-gray-50 rounded-lg p-3 border border-google-gray-200
                             hover:border-google-blue-300 hover:shadow-sm transition-all"
                  >
                    {/* 片段内容 */}
                    <p className="text-sm text-google-gray-800 mb-2 line-clamp-4">
                      {snippet.content}
                    </p>

                    {/* 来源 */}
                    <div className="text-xs text-google-gray-600 mb-2">
                      来源: {snippet.source}
                    </div>

                    {/* 标签 */}
                    {snippet.tags && snippet.tags.length > 0 && (
                      <div className="flex flex-wrap gap-1 mb-2">
                        {snippet.tags.map((tag, idx) => (
                          <span
                            key={idx}
                            className="inline-flex items-center gap-1 px-2 py-0.5 
                                     bg-google-blue-50 text-google-blue-700 rounded text-xs"
                          >
                            <Tag size={10} />
                            {tag}
                          </span>
                        ))}
                      </div>
                    )}

                    {/* 底部操作 */}
                    <div className="flex items-center justify-between">
                      <span className="text-xs text-google-gray-500">
                        {new Date(snippet.created_at).toLocaleDateString('zh-CN')}
                      </span>
                      <button
                        onClick={() => copyToClipboard(snippet.content, snippet.id)}
                        className="btn-icon p-1.5 hover:bg-google-blue-50 rounded transition-colors"
                        title="复制"
                      >
                        {copiedId === snippet.id ? (
                          <Check size={14} className="text-green-600" />
                        ) : (
                          <Copy size={14} className="text-google-gray-600" />
                        )}
                      </button>
                    </div>
                  </motion.div>
                ))}
              </div>
            )}
          </div>
        </motion.div>
      )}
    </AnimatePresence>
  );
};

export default SnippetsPanel;





