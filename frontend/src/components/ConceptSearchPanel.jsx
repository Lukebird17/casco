/**
 * 概念快速定位面板
 * 快速搜索和定位文档中的概念、公式、关键词
 */

import React, { useState, useEffect } from 'react';
import { X, Search, Zap, BookOpen, Hash, AlertCircle, Loader2 } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import toast from 'react-hot-toast';

const ConceptSearchPanel = ({ open, onClose, onJumpTo, currentKBId = 'default' }) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [searching, setSearching] = useState(false);
  const [results, setResults] = useState([]);
  const [recentSearches, setRecentSearches] = useState([]);
  const [hotConcepts, setHotConcepts] = useState([]);
  const [knowledgeBases, setKnowledgeBases] = useState([]);
  const [selectedKB, setSelectedKB] = useState(currentKBId);

  // 加载知识库列表
  useEffect(() => {
    if (open) {
      loadKnowledgeBases();
    }
  }, [open]);

  // 当知识库变化时，重新加载热门概念
  useEffect(() => {
    if (open && selectedKB) {
      loadHotConcepts();
      loadRecentSearches();
    }
  }, [open, selectedKB]);

  const loadKnowledgeBases = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/knowledge-bases');
      const data = await response.json();
      
      if (data.success) {
        setKnowledgeBases(data.knowledge_bases);
      }
    } catch (error) {
      console.error('加载知识库列表失败:', error);
    }
  };

  const loadHotConcepts = async () => {
    try {
      const response = await fetch(`http://localhost:8000/api/concepts/hot?kb_id=${selectedKB}&limit=10`);
      if (response.ok) {
        const data = await response.json();
        if (data.success) {
          setHotConcepts(data.concepts);
        }
      } else {
        // 如果后端未实现，使用模拟数据
        setHotConcepts([
          { name: 'SLUB分配器', count: 15, relevance: 0.9 },
          { name: '内存管理', count: 12, relevance: 0.85 },
          { name: 'Buddy系统', count: 10, relevance: 0.8 },
          { name: '缓存行', count: 8, relevance: 0.75 },
          { name: '虚拟内存', count: 7, relevance: 0.7 },
        ]);
      }
    } catch (error) {
      console.error('加载热门概念失败:', error);
    }
  };

  const loadRecentSearches = () => {
    const recent = JSON.parse(localStorage.getItem('recentConceptSearches') || '[]');
    setRecentSearches(recent.slice(0, 5));
  };

  const saveToRecentSearches = (term) => {
    const recent = JSON.parse(localStorage.getItem('recentConceptSearches') || '[]');
    const updated = [term, ...recent.filter(t => t !== term)].slice(0, 10);
    localStorage.setItem('recentConceptSearches', JSON.stringify(updated));
    setRecentSearches(updated.slice(0, 5));
  };

  const handleSearch = async (term = searchTerm) => {
    if (!term.trim()) {
      toast.error('请输入搜索关键词');
      return;
    }

    setSearching(true);
    saveToRecentSearches(term);

    try {
      const response = await fetch(`http://localhost:8000/api/concepts/search?q=${encodeURIComponent(term)}&kb_id=${selectedKB}&limit=20`);
      
      if (response.ok) {
        const data = await response.json();
        if (data.success) {
          setResults(data.results);
          if (data.results.length === 0) {
            toast('未找到相关概念', { icon: '🔍' });
          } else {
            toast.success(`找到 ${data.results.length} 个结果`);
          }
        }
      } else {
        toast.error('搜索失败');
      }
    } catch (error) {
      console.error('搜索失败:', error);
      toast.error('搜索失败，请重试');
    } finally {
      setSearching(false);
    }
  };


  const handleResultClick = (result) => {
    if (onJumpTo) {
      onJumpTo({
        filename: result.filename,
        line: result.line,
        page: result.page,  // 传递PDF页码
        highlight: searchTerm,
        isPDF: result.isPDF
      });
    }
    const location = result.page ? `第${result.page}页` : `第${result.line}行`;
    toast.success(`跳转到: ${result.filename} ${location}`);
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter') {
      handleSearch();
    }
  };

  return (
    <AnimatePresence>
      {open && (
        <>
          {/* 面板主体 - 紧贴Sidebar，无遮罩 */}
          <motion.div
            initial={{ width: 0, opacity: 0 }}
            animate={{ width: 380, opacity: 1 }}
            exit={{ width: 0, opacity: 0 }}
            transition={{ type: 'spring', damping: 30, stiffness: 300 }}
            className="fixed left-[280px] top-0 bottom-0 bg-white shadow-lg z-20
                     border-r border-google-gray-200 flex flex-col"
          >
            {/* 头部 */}
            <div className="flex-shrink-0 bg-white border-b border-google-gray-200 p-4">
              <div className="flex items-center justify-between mb-4">
                <div className="flex items-center gap-3">
                  <Zap size={24} className="text-google-blue-600" />
                  <h2 className="text-xl font-semibold text-google-gray-900">概念定位</h2>
                </div>
                <button
                  onClick={onClose}
                  className="btn-icon p-2 hover:bg-google-gray-100 rounded-lg"
                >
                  <X size={20} />
                </button>
              </div>

              {/* 知识库选择 */}
              {knowledgeBases.length > 1 && (
                <div className="mb-3">
                  <select
                    value={selectedKB}
                    onChange={(e) => setSelectedKB(e.target.value)}
                    className="w-full px-3 py-2 text-sm border border-google-gray-300 rounded-lg 
                             focus:outline-none focus:ring-2 focus:ring-google-blue-500 bg-white"
                  >
                    {knowledgeBases.map((kb) => (
                      <option key={kb.id} value={kb.id}>
                        📚 {kb.name} ({kb.document_count} 文档)
                      </option>
                    ))}
                  </select>
                </div>
              )}

              {/* 搜索框 */}
              <div className="relative">
                <Search size={18} className="absolute left-3 top-1/2 -translate-y-1/2 text-google-gray-400" />
                <input
                  type="text"
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                  onKeyDown={handleKeyDown}
                  placeholder="搜索概念、关键词、公式..."
                  className="w-full pl-10 pr-24 py-3 rounded-lg border border-google-gray-300 
                           focus:outline-none focus:ring-2 focus:ring-google-blue-500 
                           focus:border-transparent"
                />
                <button
                  onClick={() => handleSearch()}
                  disabled={searching}
                  className="absolute right-2 top-1/2 -translate-y-1/2 px-4 py-1.5 
                           bg-google-blue-600 text-white rounded-md text-sm font-medium
                           hover:bg-google-blue-700 disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  {searching ? <Loader2 size={16} className="animate-spin" /> : '搜索'}
                </button>
              </div>
            </div>

            {/* 内容区 - 可滚动 */}
            <div className="flex-1 overflow-y-auto p-6 space-y-6">
              {/* 搜索结果 */}
              {results.length > 0 && (
                <div>
                  <h3 className="text-sm font-semibold text-google-gray-900 mb-3">
                    搜索结果 ({results.length})
                  </h3>
                  <div className="space-y-2">
                    {results.map((result, index) => (
                      <motion.button
                        key={index}
                        initial={{ opacity: 0, y: 10 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: index * 0.05 }}
                        onClick={() => handleResultClick(result)}
                        className="w-full text-left p-3 rounded-lg border border-google-gray-200 
                                 hover:border-google-blue-300 hover:bg-google-blue-50 
                                 transition-colors group"
                      >
                        <div className="flex items-start gap-2 mb-1">
                          <BookOpen size={14} className="text-google-blue-600 mt-0.5 flex-shrink-0" />
                          <span className="text-sm font-medium text-google-gray-900 group-hover:text-google-blue-600">
                            {result.filename}
                          </span>
                        </div>
                        {result.page ? (
                          <div className="text-xs text-google-gray-500 mb-1">
                            第 {result.page} 页
                          </div>
                        ) : result.line && (
                          <div className="text-xs text-google-gray-500 mb-1">
                            第 {result.line} 行
                          </div>
                        )}
                        <div className="text-xs text-google-gray-700 line-clamp-2">
                          {result.context}
                        </div>
                        {result.relevance && (
                          <div className="mt-2">
                            <div className="flex items-center gap-2">
                              <div className="flex-1 h-1.5 bg-google-gray-200 rounded-full overflow-hidden">
                                <div
                                  className="h-full bg-google-blue-500 rounded-full"
                                  style={{ width: `${result.relevance * 100}%` }}
                                />
                              </div>
                              <span className="text-xs text-google-gray-500">
                                {(result.relevance * 100).toFixed(0)}%
                              </span>
                            </div>
                          </div>
                        )}
                      </motion.button>
                    ))}
                  </div>
                </div>
              )}

              {/* 最近搜索 */}
              {recentSearches.length > 0 && results.length === 0 && (
                <div>
                  <h3 className="text-sm font-semibold text-google-gray-900 mb-3">
                    最近搜索
                  </h3>
                  <div className="flex flex-wrap gap-2">
                    {recentSearches.map((term, index) => (
                      <button
                        key={index}
                        onClick={() => { setSearchTerm(term); handleSearch(term); }}
                        className="px-3 py-1.5 bg-google-gray-100 hover:bg-google-blue-50 
                                 text-sm text-google-gray-700 hover:text-google-blue-600 
                                 rounded-full transition-colors"
                      >
                        {term}
                      </button>
                    ))}
                  </div>
                </div>
              )}

              {/* 热门概念 */}
              {hotConcepts.length > 0 && results.length === 0 && (
                <div>
                  <h3 className="text-sm font-semibold text-google-gray-900 mb-3 flex items-center gap-2">
                    <Hash size={16} />
                    热门概念
                  </h3>
                  <div className="space-y-2">
                    {hotConcepts.map((concept, index) => (
                      <button
                        key={index}
                        onClick={() => { setSearchTerm(concept.name); handleSearch(concept.name); }}
                        className="w-full text-left p-3 rounded-lg border border-google-gray-200 
                                 hover:border-google-blue-300 hover:bg-google-blue-50 
                                 transition-colors group flex items-center justify-between"
                      >
                        <div className="flex items-center gap-2">
                          <Zap size={14} className="text-yellow-500" />
                          <span className="text-sm font-medium text-google-gray-900 group-hover:text-google-blue-600">
                            {concept.name}
                          </span>
                        </div>
                        <span className="text-xs text-google-gray-500">
                          {concept.count} 次引用
                        </span>
                      </button>
                    ))}
                  </div>
                </div>
              )}

              {/* 空状态 */}
              {results.length === 0 && !searching && searchTerm && (
                <div className="text-center py-8">
                  <AlertCircle size={48} className="mx-auto mb-3 text-google-gray-300" />
                  <p className="text-google-gray-600">未找到 "{searchTerm}"</p>
                  <p className="text-xs text-google-gray-500 mt-1">
                    尝试换个关键词或查看热门概念
                  </p>
                </div>
              )}
            </div>
          </motion.div>
        </>
      )}
    </AnimatePresence>
  );
};

export default ConceptSearchPanel;


