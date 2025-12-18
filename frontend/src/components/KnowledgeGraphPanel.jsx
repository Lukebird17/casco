/**
 * 知识图谱面板
 */

import React, { useState, useEffect } from 'react';
import { X, Brain, ExternalLink } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import toast from 'react-hot-toast';
import axios from 'axios';

const KnowledgeGraphPanel = ({ open, onClose }) => {
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(false);
  const [knowledgeBases, setKnowledgeBases] = useState([]);
  const [selectedKB, setSelectedKB] = useState('default');

  // 加载统计
  useEffect(() => {
    if (open) {
      loadKnowledgeBases();
      loadStats();
    }
  }, [open, selectedKB]);

  const loadKnowledgeBases = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/knowledge-bases');
      if (response.data.success) {
        setKnowledgeBases(response.data.knowledge_bases);
      }
    } catch (error) {
      console.error('加载知识库列表失败:', error);
    }
  };

  const loadStats = async () => {
    setLoading(true);
    try {
      const response = await axios.get('http://localhost:8000/api/knowledge-graph');
      console.log('知识图谱数据:', response.data);
      if (response.data.success) {
        setStats(response.data.stats);
      }
    } catch (error) {
      console.error('加载知识图谱失败:', error);
      toast.error('加载知识图谱失败，请稍后重试');
    } finally {
      setLoading(false);
    }
  };

  // 打开可视化页面
  const handleVisualize = () => {
    window.open('http://localhost:8000/api/knowledge-graph/visualize', '_blank');
  };

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
                <Brain size={20} className="text-google-blue-600" />
                <h2 className="font-semibold text-google-gray-900">知识图谱</h2>
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
            {/* 知识库选择 */}
            {knowledgeBases.length > 0 && (
              <div className="mb-4">
                <label className="block text-sm font-medium text-google-gray-700 mb-2">
                  选择知识库
                </label>
                <select
                  value={selectedKB}
                  onChange={(e) => setSelectedKB(e.target.value)}
                  className="w-full px-3 py-2 border border-google-gray-300 rounded-lg 
                           focus:outline-none focus:ring-2 focus:ring-google-blue-500"
                >
                  {knowledgeBases.map((kb) => (
                    <option key={kb.id} value={kb.id}>
                      {kb.name} ({kb.document_count} 文档)
                    </option>
                  ))}
                </select>
              </div>
            )}

            {loading ? (
              <div className="text-center py-20 text-google-gray-500">
                <div className="animate-spin h-8 w-8 border-4 border-google-blue-500 border-t-transparent rounded-full mx-auto mb-2"></div>
                加载中...
              </div>
            ) : stats ? (
              <div className="space-y-6">
                {/* 统计卡片 */}
                <div className="bg-gradient-to-br from-google-blue-500 to-google-blue-600 rounded-lg p-6 text-white">
                  <div className="grid grid-cols-2 gap-4">
                    <div>
                      <div className="text-3xl font-bold">{stats.total_entities}</div>
                      <div className="text-sm opacity-90">实体节点</div>
                    </div>
                    <div>
                      <div className="text-3xl font-bold">{stats.total_relationships}</div>
                      <div className="text-sm opacity-90">关系连接</div>
                    </div>
                  </div>
                </div>

                {/* 实体类型分布 */}
                {stats.entity_types && Object.keys(stats.entity_types).length > 0 && (
                  <div>
                    <h3 className="font-medium text-google-gray-900 mb-3">实体类型分布</h3>
                    <div className="space-y-2">
                      {Object.entries(stats.entity_types).map(([type, count]) => (
                        <div key={type} className="flex items-center justify-between">
                          <span className="text-sm text-google-gray-700">{type}</span>
                          <div className="flex items-center gap-2">
                            <div className="w-24 h-2 bg-google-gray-200 rounded-full overflow-hidden">
                              <div 
                                className="h-full bg-google-blue-500 rounded-full"
                                style={{ 
                                  width: `${(count / stats.total_entities) * 100}%` 
                                }}
                              />
                            </div>
                            <span className="text-sm font-medium text-google-gray-900 w-8 text-right">
                              {count}
                            </span>
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                {/* 可视化按钮 */}
                <button
                  onClick={handleVisualize}
                  className="w-full btn-primary py-3 flex items-center justify-center gap-2"
                >
                  <ExternalLink size={18} />
                  打开可视化视图
                </button>

                {/* 说明 */}
                <div className="bg-google-blue-50 rounded-lg p-4">
                  <p className="text-sm text-google-gray-700">
                    💡 <strong>提示：</strong>
                  </p>
                  <ul className="text-xs text-google-gray-600 mt-2 space-y-1 list-disc list-inside">
                    <li>知识图谱会自动从文档中提取实体和关系</li>
                    <li>点击节点可以查看详细信息</li>
                    <li>拖拽节点可以调整布局</li>
                    <li>不同颜色代表不同类型的实体</li>
                  </ul>
                </div>
              </div>
            ) : (
              <div className="text-center py-20 text-google-gray-500">
                <Brain size={48} className="mx-auto mb-3 opacity-30" />
                <p>暂无知识图谱数据</p>
                <p className="text-sm mt-1">上传文档后自动构建</p>
              </div>
            )}
          </div>
        </motion.div>
      )}
    </AnimatePresence>
  );
};

export default KnowledgeGraphPanel;




