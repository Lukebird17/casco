/**
 * 消息气泡组件
 * Gemini 风格的消息显示
 */

import React, { useState } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import 'katex/dist/katex.min.css'; // 导入KaTeX样式
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { vscDarkPlus } from 'react-syntax-highlighter/dist/esm/styles/prism';
import { User, Bot, AlertCircle, Bookmark, Check } from 'lucide-react';
import { motion } from 'framer-motion';
import toast from 'react-hot-toast';
import { saveSnippet } from '../api/client';
import AnswerWithCitations from './AnswerWithCitations';

const MessageBubble = ({ message, isLatest, sessionId, onCitationClick }) => {
  const isUser = message.role === 'user';
  const isError = message.error;
  const [isSaved, setIsSaved] = useState(false);
  
  // 保存片段
  const handleSaveSnippet = async () => {
    try {
      await saveSnippet({
        session_id: sessionId,
        content: message.content,
        source: "AI 回答",
        tags: ["对话", "AI"]
      });
      setIsSaved(true);
      toast.success('已添加到片段收藏');
    } catch (error) {
      console.error('保存片段失败:', error);
      toast.error('保存失败');
    }
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.3 }}
      className={`flex ${isUser ? 'justify-end' : 'justify-start'} mb-4`}
    >
      <div className={`flex gap-3 max-w-[85%] ${isUser ? 'flex-row-reverse' : 'flex-row'}`}>
        {/* 头像 */}
        <div className={`flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center ${
          isUser 
            ? 'bg-google-blue-500' 
            : isError 
              ? 'bg-red-500' 
              : 'bg-google-gray-700'
        }`}>
          {isUser ? (
            <User size={18} className="text-white" />
          ) : isError ? (
            <AlertCircle size={18} className="text-white" />
          ) : (
            <Bot size={18} className="text-white" />
          )}
        </div>

        {/* 消息内容 */}
        <div className={`message-bubble ${
          isUser ? 'message-user' : 'message-assistant'
        } ${isError ? 'bg-red-50 border-red-200' : ''}`}>
          {isUser ? (
            <p className="text-google-gray-900 whitespace-pre-wrap">{message.content}</p>
          ) : (
            <AnswerWithCitations 
              content={message.content} 
              onCitationClick={onCitationClick}
            />
          )}
          
          {/* 时间戳和操作按钮 */}
          <div className="flex items-center justify-between mt-2">
            {message.timestamp && (
              <div className="text-xs text-google-gray-500">
                {new Date(message.timestamp).toLocaleTimeString('zh-CN', {
                  hour: '2-digit',
                  minute: '2-digit',
                })}
              </div>
            )}
            
            {/* AI回答才显示收藏按钮 */}
            {!isUser && !isError && (
              <button
                onClick={handleSaveSnippet}
                disabled={isSaved}
                className={`btn-icon p-1.5 rounded transition-colors ${
                  isSaved 
                    ? 'text-green-600' 
                    : 'text-google-gray-500 hover:text-google-blue-600'
                }`}
                title={isSaved ? '已收藏' : '收藏到片段'}
              >
                {isSaved ? <Check size={14} /> : <Bookmark size={14} />}
              </button>
            )}
          </div>
        </div>
      </div>
    </motion.div>
  );
};

export default MessageBubble;

