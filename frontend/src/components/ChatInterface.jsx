/**
 * 聊天界面组件
 * 主对话区域
 */

import React, { useEffect, useRef } from 'react';
import MessageBubble from './MessageBubble';
import InputArea from './InputArea';
import ThinkingIndicator from './ThinkingIndicator';
import RetrievalResults from './RetrievalResults';
import { motion, AnimatePresence } from 'framer-motion';

const ChatInterface = ({ 
  messages, 
  loading, 
  onSendMessage,
  onStopGeneration,  // 新增：停止生成
  enableSocratic,
  currentSessionId,
  selectedKnowledgeBase,
  onKnowledgeBaseChange,
  retrievalCitations,
  showRetrievalResults,
  onCitationClick,
}) => {
  const messagesEndRef = useRef(null);
  const chatContainerRef = useRef(null);
  const prevMessagesLengthRef = useRef(0);
  const isUserScrollingRef = useRef(false);

  // 自动滚动到底部（只在新消息添加时，且用户没有主动向上滚动）
  useEffect(() => {
    // 只在消息数量增加时才滚动（新消息添加）
    if (messages.length > prevMessagesLengthRef.current) {
      setTimeout(() => {
        // 只在用户没有主动向上滚动时才自动滚动
        if (!isUserScrollingRef.current) {
          messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
        }
      }, 100);
      prevMessagesLengthRef.current = messages.length;
    }
  }, [messages]);

  // 检测用户是否主动滚动
  const handleScroll = (e) => {
    const element = e.target;
    const isAtBottom = element.scrollHeight - element.scrollTop - element.clientHeight < 100;
    isUserScrollingRef.current = !isAtBottom;
  };

  return (
    <div className="flex flex-col h-full bg-white">
      {/* 消息列表 */}
      <div className="flex-1 overflow-y-auto px-6 py-8" onScroll={handleScroll}>
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
                          if (citation) {
                            // 找到了citation对象，传递整个对象
                            onCitationClick && onCitationClick(citation);
                          } else {
                            // 没找到citation对象（可能是历史消息），直接传递cite_id字符串
                            // App.jsx中的handleJumpToCitation会处理字符串形式的cite_id
                            onCitationClick && onCitationClick(citeId);
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
        onStop={onStopGeneration}
        loading={loading}
        enableSocratic={enableSocratic}
        selectedKnowledgeBase={selectedKnowledgeBase}
        onKnowledgeBaseChange={onKnowledgeBaseChange}
      />
    </div>
  );
};

export default ChatInterface;

