/**
 * 侧边栏组件
 * 会话管理和导航
 */

import React, { useState } from 'react';
import { 
  Plus, 
  MessageSquare, 
  Settings, 
  Database,
  BookOpen,
  Brain,
  LineChart,
  FileText,
  Award,
  Lightbulb,
  TrendingUp,
  Hash,
  Zap,
  Trash2,
  Edit2,
  Check,
  X,
} from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

const Sidebar = ({ 
  sessions, 
  currentSessionId, 
  onNewSession, 
  onSwitchSession,
  onDeleteSession,
  onRenameSession,
  onOpenTool,
  onOpenSettings,
}) => {
  const [collapsed, setCollapsed] = useState(false);
  const [editingId, setEditingId] = useState(null);
  const [editingName, setEditingName] = useState('');

  const handleStartEdit = (session, e) => {
    e.stopPropagation();
    setEditingId(session.session_id);
    setEditingName(session.name);
  };

  const handleSaveEdit = async (sessionId, e) => {
    e?.stopPropagation();
    if (editingName.trim() && editingName !== sessions.find(s => s.session_id === sessionId)?.name) {
      await onRenameSession(sessionId, editingName.trim());
    }
    setEditingId(null);
    setEditingName('');
  };

  const handleCancelEdit = (e) => {
    e?.stopPropagation();
    setEditingId(null);
    setEditingName('');
  };

  const handleDelete = async (sessionId, e) => {
    e.stopPropagation();
    if (window.confirm('确定要删除这个对话吗？')) {
      await onDeleteSession(sessionId);
    }
  };

  const tools = [
    { id: 'database', name: '知识库', icon: Database },
    { id: 'documents', name: '文档查看', icon: BookOpen },
    { id: 'confidence', name: '置信度分析', icon: TrendingUp },
    { id: 'outline', name: '文档大纲', icon: Hash },
    { id: 'concept-search', name: '概念定位', icon: Zap },
    { id: 'knowledge-graph', name: '知识图谱', icon: Brain },
    { id: 'heatmap', name: '热力图', icon: LineChart },
    { id: 'snippets', name: '片段收藏', icon: FileText },
    { id: 'quiz', name: '智能测验', icon: Award },
    { id: 'flashcards', name: '记忆闪卡', icon: Lightbulb },
  ];

  return (
    <motion.div
      initial={false}
      animate={{ width: collapsed ? '80px' : '280px' }}
      className="h-full bg-google-gray-50 border-r border-google-gray-200 flex flex-col"
    >
      {/* 顶部 Logo */}
      <div className="p-4 border-b border-google-gray-200">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-lg bg-gradient-to-br from-google-blue-500 to-google-blue-600 flex items-center justify-center">
            <span className="text-white text-xl font-bold">R</span>
          </div>
          <AnimatePresence>
            {!collapsed && (
              <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                exit={{ opacity: 0 }}
              >
                <h1 className="text-lg font-semibold text-google-gray-900">
                  RAG Agent
                </h1>
              </motion.div>
            )}
          </AnimatePresence>
        </div>
      </div>

      {/* 新建对话按钮 */}
      <div className="p-3">
        <button
          onClick={onNewSession}
          className="w-full btn-primary flex items-center justify-center gap-2 py-3"
          title="新建对话"
        >
          <Plus size={20} />
          <AnimatePresence>
            {!collapsed && (
              <motion.span
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                exit={{ opacity: 0 }}
              >
                新建对话
              </motion.span>
            )}
          </AnimatePresence>
        </button>
      </div>

      {/* 会话列表 */}
      <div className="flex-1 overflow-y-auto px-3">
        <div className="space-y-1">
          {sessions.map((session) => (
            <div
              key={session.session_id}
              className={`group relative w-full rounded-lg transition-colors ${
                currentSessionId === session.session_id
                  ? 'bg-google-blue-50'
                  : 'hover:bg-google-gray-100'
              }`}
            >
              {editingId === session.session_id && !collapsed ? (
                // 编辑模式
                <div className="flex items-center gap-1 px-2 py-2" onClick={(e) => e.stopPropagation()}>
                  <MessageSquare size={16} className="flex-shrink-0 text-google-gray-500" />
                  <input
                    type="text"
                    value={editingName}
                    onChange={(e) => setEditingName(e.target.value)}
                    onKeyDown={(e) => {
                      if (e.key === 'Enter') handleSaveEdit(session.session_id, e);
                      if (e.key === 'Escape') handleCancelEdit(e);
                    }}
                    className="flex-1 text-sm px-2 py-1 border border-google-blue-300 rounded focus:outline-none focus:ring-2 focus:ring-google-blue-500"
                    autoFocus
                    onClick={(e) => e.stopPropagation()}
                  />
                  <button
                    onClick={(e) => handleSaveEdit(session.session_id, e)}
                    className="p-1 hover:bg-google-blue-100 rounded"
                    title="保存"
                  >
                    <Check size={14} className="text-google-green-600" />
                  </button>
                  <button
                    onClick={handleCancelEdit}
                    className="p-1 hover:bg-google-gray-200 rounded"
                    title="取消"
                  >
                    <X size={14} className="text-google-gray-600" />
                  </button>
                </div>
              ) : (
                // 正常模式
                <div
                  onClick={() => onSwitchSession(session.session_id)}
                  className="w-full text-left px-3 py-2 rounded-lg cursor-pointer hover:bg-google-gray-100 dark:hover:bg-gray-700 transition-colors"
                  title={session.name}
                >
                  <div className="flex items-center justify-between gap-2">
                    <div className="flex items-center gap-2 flex-1 min-w-0">
                      <MessageSquare size={16} className="flex-shrink-0" />
                      <AnimatePresence>
                        {!collapsed && (
                          <motion.span
                            initial={{ opacity: 0 }}
                            animate={{ opacity: 1 }}
                            exit={{ opacity: 0 }}
                            className={`text-sm truncate ${
                              currentSessionId === session.session_id
                                ? 'text-google-blue-700'
                                : 'text-google-gray-700'
                            }`}
                          >
                            {session.name || '新对话'}
                          </motion.span>
                        )}
                      </AnimatePresence>
                    </div>
                    
                    {!collapsed && (
                      <div className="flex items-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity">
                        <button
                          onClick={(e) => handleStartEdit(session, e)}
                          className="p-1 hover:bg-google-blue-100 rounded"
                          title="重命名"
                        >
                          <Edit2 size={14} className="text-google-gray-600" />
                        </button>
                        <button
                          onClick={(e) => handleDelete(session.session_id, e)}
                          className="p-1 hover:bg-google-red-100 rounded"
                          title="删除"
                        >
                          <Trash2 size={14} className="text-google-red-600" />
                        </button>
                      </div>
                    )}
                  </div>
                </div>
              )}
            </div>
          ))}
        </div>
      </div>

      {/* 工具面板 */}
      <div className="border-t border-google-gray-200 p-3">
        <AnimatePresence>
          {!collapsed && (
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              className="mb-2"
            >
              <h3 className="text-xs font-medium text-google-gray-500 px-2 mb-2">
                工具面板
              </h3>
            </motion.div>
          )}
        </AnimatePresence>
        
        <div className="space-y-1">
          {tools.map((tool) => {
            const Icon = tool.icon;
            return (
              <button
                key={tool.id}
                onClick={() => onOpenTool(tool.id)}
                className="w-full text-left px-3 py-2 rounded-lg hover:bg-google-gray-100 
                         text-google-gray-700 transition-colors flex items-center gap-2"
                title={tool.name}
              >
                <Icon size={16} className="flex-shrink-0" />
                <AnimatePresence>
                  {!collapsed && (
                    <motion.span
                      initial={{ opacity: 0 }}
                      animate={{ opacity: 1 }}
                      exit={{ opacity: 0 }}
                      className="text-sm"
                    >
                      {tool.name}
                    </motion.span>
                  )}
                </AnimatePresence>
              </button>
            );
          })}
        </div>
      </div>

      {/* 设置按钮 */}
      <div className="border-t border-google-gray-200 p-3">
        <button
          onClick={() => onOpenSettings?.()}
          className="w-full text-left px-3 py-2 rounded-lg hover:bg-google-gray-100 
                   text-google-gray-700 transition-colors flex items-center gap-2"
          title="设置"
        >
          <Settings size={16} className="flex-shrink-0" />
          <AnimatePresence>
            {!collapsed && (
              <motion.span
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                exit={{ opacity: 0 }}
                className="text-sm"
              >
                设置
              </motion.span>
            )}
          </AnimatePresence>
        </button>
      </div>
    </motion.div>
  );
};

export default Sidebar;


