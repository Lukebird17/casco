/**
 * 聊天界面组件
 * 主对话区域
 */

import React, { useEffect, useRef } from 'react';
import MessageBubble from './MessageBubble';
import InputArea from './InputArea';
import ThinkingIndicator from './ThinkingIndicator';
import SocraticHints from './SocraticHints';
import RetrievalResults from './RetrievalResults';
import { motion, AnimatePresence } from 'framer-motion';

const ChatInterface = ({ 
  messages, 
  loading, 
  onSendMessage, 
  enableSocratic,
  currentSessionId,
  selectedKnowledgeBase,
  onKnowledgeBaseChange,
  retrievalCitations,
  showRetrievalResults,
  onCitationClick,
}) => {
  const messagesEndRef = useRef(null);

  // 自动滚动到底部（当消息、检索结果或loading状态变化时）
  useEffect(() => {
    // 使用setTimeout确保DOM已更新
    setTimeout(() => {
      messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    }, 100);
  }, [messages, retrievalCitations, loading]);

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
              {/* 苏格拉底模式提示（始终显示，不消失） */}
              {enableSocratic && messages.length > 0 && (
                <SocraticHints 
                  visible={true} 
                  query={messages[messages.length - 1]?.content}
                />
              )}

              <AnimatePresence>
                {messages.map((message, index) => {
                  const isLastMessage = index === messages.length - 1;
                  const isAssistantMessage = message.role === 'assistant';
                  
                  return (
                    <React.Fragment key={`${message.timestamp}-${index}`}>
                      {/* 如果是最后一条助手消息，先显示检索结果 */}
                      {isLastMessage && isAssistantMessage && showRetrievalResults && retrievalCitations && retrievalCitations.length > 0 && (
                        <RetrievalResults 
                          citations={retrievalCitations}
                          onCitationClick={onCitationClick}
                          visible={showRetrievalResults}
                        />
                      )}
                      
                      {/* 然后显示消息本身 */}
                      <MessageBubble
                        message={message}
                        isLatest={isLastMessage}
                        sessionId={currentSessionId}
                        onCitationClick={(citeId) => {
                          // 从cite_id找到对应的citation对象
                          const citation = retrievalCitations?.find(c => c.id === citeId);
                          if (citation && onCitationClick) {
                            onCitationClick(citation);
                          }
                        }}
                      />
                    </React.Fragment>
                  );
                })}
              </AnimatePresence>
              
              {/* ✅ 重要：在loading期间也显示Context（在消息列表之后，加载指示器之前） */}
              {loading && showRetrievalResults && retrievalCitations && retrievalCitations.length > 0 && (
                <RetrievalResults 
                  citations={retrievalCitations}
                  onCitationClick={onCitationClick}
                  visible={true}
                />
              )}
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

