/**
 * 聊天界面组件
 * 主对话区域
 */

import React, { useEffect, useRef } from 'react';
import MessageBubble from './MessageBubble';
import InputArea from './InputArea';
import ThinkingIndicator from './ThinkingIndicator';
import SocraticHints from './SocraticHints';
import { motion, AnimatePresence } from 'framer-motion';

const ChatInterface = ({ 
  messages, 
  loading, 
  onSendMessage, 
  enableSocratic,
  currentSessionId,
  selectedKnowledgeBase,
  onKnowledgeBaseChange,
}) => {
  const messagesEndRef = useRef(null);

  // 自动滚动到底部
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  return (
    <div className="flex flex-col h-full bg-white">
      {/* 消息列表 */}
      <div className="flex-1 overflow-y-auto px-6 py-8">
        <div className="max-w-4xl mx-auto">
          {/* 苏格拉底模式欢迎消息 */}
          {messages.length === 0 ? (
            <div className="h-full flex items-center justify-center">
              <div className="text-center">
                <div className={`text-6xl mb-4 ${enableSocratic ? 'animate-bounce' : ''}`}>
                  {enableSocratic ? '🧙‍♂️' : '🤖'}
                </div>
                <h2 className={`text-2xl font-medium mb-2 ${
                  enableSocratic ? 'text-purple-700' : 'text-google-gray-700'
                }`}>
                  {enableSocratic 
                    ? '苏格拉底模式已启用！' 
                    : '您好！有什么可以帮助您的吗？'}
                </h2>
                <p className={enableSocratic ? 'text-purple-600' : 'text-google-gray-500'}>
                  {enableSocratic
                    ? '我将通过提问引导你自己找到答案'
                    : '输入问题或上传文档开始对话'}
                </p>
              </div>
            </div>
          ) : (
            <>
              {/* 苏格拉底模式提示（在对话中显示） */}
              {enableSocratic && loading && (
                <SocraticHints 
                  visible={true} 
                  query={messages[messages.length - 1]?.content}
                />
              )}

              <AnimatePresence>
                {messages.map((message, index) => (
                  <MessageBubble
                    key={`${message.timestamp}-${index}`}
                    message={message}
                    isLatest={index === messages.length - 1}
                    sessionId={currentSessionId}
                  />
                ))}
              </AnimatePresence>
            </>
          )}

          {/* 加载指示器 */}
          {loading && <ThinkingIndicator />}

          <div ref={messagesEndRef} />
        </div>
      </div>

      {/* 输入区域 */}
      <InputArea 
        onSend={onSendMessage} 
        loading={loading}
        enableSocratic={enableSocratic}
        selectedKnowledgeBase={selectedKnowledgeBase}
        onKnowledgeBaseChange={onKnowledgeBaseChange}
      />
    </div>
  );
};

export default ChatInterface;

