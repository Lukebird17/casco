/**
 * 聊天 Hook
 * 管理聊天状态和消息发送
 */

import { useState, useCallback } from 'react';
import { sendMessage } from '../api/client';
import toast from 'react-hot-toast';

export const useChat = (currentSessionId) => {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [citations, setCitations] = useState([]);
  const [confidence, setConfidence] = useState(null);

  const sendChatMessage = useCallback(async (message, options = {}) => {
    const { 
      image, 
      file, 
      enableSocratic = false, 
      thinkingMode = 'fast', 
      knowledgeBaseId = 'default',
      temperature = 0.7,
      maxTokens = 2000,
      retrievalK = 5
    } = options;

    // 准备用户消息内容
    let displayMessage = message;
    if (file) {
      displayMessage = `${message}\n\n📎 附件: ${file.filename}`;
    }

    // 添加用户消息到界面
    const userMessage = {
      role: 'user',
      content: displayMessage,
      timestamp: new Date().toISOString(),
    };
    
    setMessages((prev) => [...prev, userMessage]);
    setLoading(true);
    setCitations([]);
    setConfidence(null);

    try {
      // 构建请求参数
      const requestData = {
        message: message,
        session_id: currentSessionId,
        enable_socratic: enableSocratic,
        thinking_mode: thinkingMode,
        knowledge_base_id: knowledgeBaseId,
        temperature: temperature,
        max_tokens: maxTokens,
        retrieval_k: retrievalK,
      };

      // 如果有图片，添加图片数据
      if (image) {
        requestData.image_base64 = image;
      }

      // 如果有文件，添加文件内容
      if (file && file.content) {
        requestData.file_content = file.content;
      }

      const response = await sendMessage(requestData);

      if (response.success) {
        // 添加 AI 回复
        const assistantMessage = {
          role: 'assistant',
          content: response.response,
          timestamp: new Date().toISOString(),
        };
        
        setMessages((prev) => [...prev, assistantMessage]);
        
        // 更新引用和置信度
        if (response.citations) {
          setCitations(response.citations);
        }
        
        if (response.confidence) {
          setConfidence(response.confidence);
        }
        
        return response;
      } else {
        throw new Error('发送消息失败');
      }
    } catch (error) {
      console.error('发送消息错误:', error);
      toast.error('发送失败，请重试');
      
      // 添加错误消息
      const errorMessage = {
        role: 'assistant',
        content: '抱歉，发送消息时出错了。请稍后重试。',
        timestamp: new Date().toISOString(),
        error: true,
      };
      
      setMessages((prev) => [...prev, errorMessage]);
      
      throw error;
    } finally {
      setLoading(false);
    }
  }, [currentSessionId]);

  const clearMessages = useCallback(() => {
    setMessages([]);
    setCitations([]);
    setConfidence(null);
  }, []);

  const setInitialMessages = useCallback((msgs) => {
    setMessages(msgs);
  }, []);

  return {
    messages,
    loading,
    citations,
    confidence,
    sendChatMessage,
    clearMessages,
    setInitialMessages,
  };
};

export default useChat;


