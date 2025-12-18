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
} from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

const Sidebar = ({ 
  sessions, 
  currentSessionId, 
  onNewSession, 
  onSwitchSession,
  onOpenTool,
}) => {
  const [collapsed, setCollapsed] = useState(false);

  const tools = [
    { id: 'database', name: '知识库', icon: Database },
    { id: 'documents', name: '文档查看', icon: BookOpen },
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
            <button
              key={session.session_id}
              onClick={() => onSwitchSession(session.session_id)}
              className={`w-full text-left px-3 py-2 rounded-lg transition-colors ${
                currentSessionId === session.session_id
                  ? 'bg-google-blue-50 text-google-blue-700'
                  : 'hover:bg-google-gray-100 text-google-gray-700'
              }`}
              title={session.name}
            >
              <div className="flex items-center gap-2">
                <MessageSquare size={16} className="flex-shrink-0" />
                <AnimatePresence>
                  {!collapsed && (
                    <motion.span
                      initial={{ opacity: 0 }}
                      animate={{ opacity: 1 }}
                      exit={{ opacity: 0 }}
                      className="text-sm truncate"
                    >
                      {session.name || '新对话'}
                    </motion.span>
                  )}
                </AnimatePresence>
              </div>
            </button>
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


