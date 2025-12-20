/**
 * 聊天 Hook
 * 管理聊天状态和消息发送
 */

import { useState, useCallback, useRef } from 'react';
import { sendMessage } from '../api/client';
import toast from 'react-hot-toast';

export const useChat = (currentSessionId) => {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [citations, setCitations] = useState([]);
  const [confidence, setConfidence] = useState(null);
  const [qualityMetrics, setQualityMetrics] = useState(null); // 新增：质量评估（雷达图）
  const [retrievalCitations, setRetrievalCitations] = useState([]); // 新增：检索阶段的引用
  const [showRetrievalResults, setShowRetrievalResults] = useState(false); // 新增：是否显示检索结果
  
  // 轮询定时器引用
  let pollingInterval = null;
  
  // AbortController用于停止请求（使用useRef保持引用）
  const abortControllerRef = useRef(null);
  
  // 启动质量评估轮询
  const startQualityMetricsPolling = useCallback((sessionId, messageIdx) => {
    // 清除之前的轮询
    if (pollingInterval) {
      clearInterval(pollingInterval);
    }
    
    let attempts = 0;
    const maxAttempts = 20; // 最多轮询20次（60秒 / 3秒每次）
    
    console.log(`🔄 开始轮询质量评估: sessionId=${sessionId}, messageIdx=${messageIdx}`);
    
    pollingInterval = setInterval(async () => {
      attempts++;
      
      try {
        // ✅ 传递message_idx参数
        const url = messageIdx !== undefined 
          ? `http://localhost:8000/api/sessions/${sessionId}/quality-metrics?message_idx=${messageIdx}`
          : `http://localhost:8000/api/sessions/${sessionId}/quality-metrics`;
        const response = await fetch(url);
        const result = await response.json();
        
        if (result.success && result.data) {
          // 评估完成
          console.log('轮询获取到评估结果:', result.data);
          setQualityMetrics(result.data);
          const score = result.data.overall_score || 0;
          const evalTime = result.data.eval_time || 0;
          toast.success(`质量评估完成：${(score * 100).toFixed(0)}分 (${evalTime}秒)`, { duration: 2000 });
          
          // 停止轮询
          clearInterval(pollingInterval);
          pollingInterval = null;
        } else if (attempts >= maxAttempts) {
          // 超过最大次数，停止轮询
          console.log('质量评估轮询超时');
          toast.info('评估时间较长，已切换到后台运行', { duration: 2000 });
          clearInterval(pollingInterval);
          pollingInterval = null;
        }
      } catch (error) {
        console.error('轮询评估结果失败:', error);
        if (attempts >= maxAttempts) {
          clearInterval(pollingInterval);
          pollingInterval = null;
        }
      }
    }, 3000); // 每3秒轮询一次
  }, []);

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
    setRetrievalCitations([]); // 清空之前的检索结果
    // setShowRetrievalResults(false);  // ❌ 删除：不要隐藏
    
    // 显示处理中的提示
    const processingToast = toast.loading(
      '正在处理您的问题...\n' + 
      (thinkingMode === 'thinking' ? '🧠 深度思考模式，可能需要较长时间' : '⚡ 快速模式'),
      { duration: Infinity }
    );

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

      // === 使用流式API ===
      abortControllerRef.current = new AbortController();
      const response = await fetch('http://localhost:8000/api/chat/stream', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestData),
        signal: abortControllerRef.current.signal,  // 添加abort信号
      });

      if (!response.ok) {
        throw new Error('Stream request failed');
      }

      const reader = response.body.getReader();
      const decoder = new TextDecoder();
      let answerText = '';
      let receivedCitations = [];  // 用本地变量保存citations
      let retrievalTime = 0;  // ✅ 检索时间
      let generationTime = 0;  // ✅ 生成时间

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        const chunk = decoder.decode(value);
        const lines = chunk.split('\n');

        for (const line of lines) {
          if (line.startsWith('data: ')) {
            try {
              const data = JSON.parse(line.slice(6));
              
              switch (data.type) {
                case 'status':
                  // 更新状态提示
                  toast.dismiss(processingToast);
                  toast.loading(data.data, { duration: Infinity, id: processingToast });
                  break;
                  
                case 'citations':
                  // ✅ 收到检索结果和检索时间
                  console.log('收到检索结果:', data.data.length, '个文档', `耗时${data.retrieval_time}秒`);
                  receivedCitations = data.data;  // 保存到本地变量
                  retrievalTime = data.retrieval_time || 0;
                  setRetrievalCitations(data.data);
                  setShowRetrievalResults(true);
                  toast.dismiss(processingToast);
                  toast.success(`找到 ${data.data.length} 个相关文档 (${retrievalTime}秒)`, { duration: 2000 });
                  break;
                  
                case 'answer':
                  // ✅ 收到答案和生成时间 - 立即显示给用户
                  answerText = data.data;
                  generationTime = data.generation_time || 0;
                  console.log(`✅ 收到答案，立即显示给用户 (生成耗时: ${generationTime}秒)`);
                  
                  // ⚡ 关键优化：立即将答案添加到messages，不等待后续事件
                  const immediateMessage = {
                    role: 'assistant',
                    content: answerText,
                    timestamp: new Date().toISOString(),
                    generationTime: generationTime,
                  };
                  setMessages((prev) => [...prev, immediateMessage]);
                  
                  // 关闭loading，让用户看到答案
                  setLoading(false);
                  toast.dismiss(processingToast);
                  toast.success(`✅ 回答已生成 (${generationTime}秒)`, { duration: 1000 }); // 缩短到1秒，避免挡住UI
                  break;
                  
                case 'confidence':
                  // 收到置信度
                  setConfidence(data.data);
                  break;
                
                case 'quality_metrics':
                  // 收到质量评估（雷达图数据）
                  console.log('收到质量评估:', data.data);
                  if (data.data.status === 'evaluating') {
                    // 评估中，启动轮询
                    console.log('启动质量评估轮询...');
                    // ✅ 修复索引计算
                    // 后端逻辑：current_message_idx = len(session.messages)（添加前），保存到 current_message_idx + 1
                    // 前端逻辑：messages.length 对应 len(session.messages)，所以助手消息索引 = messages.length + 1
                    const currentMessageIdx = messages.length + 1;  // assistant message index
                    console.log(`📍 助手消息索引: ${currentMessageIdx} (messages.length=${messages.length})`);
                    startQualityMetricsPolling(currentSessionId, currentMessageIdx);
                  } else {
                    // 评估完成
                    setQualityMetrics(data.data);
                    toast.dismiss(processingToast);
                    const score = data.data.overall_score || 0;
                    const evalTime = data.data.eval_time || 0;
                    toast.success(`质量评估完成：${(score * 100).toFixed(0)}分 (${evalTime}秒)`, { duration: 2000 });
                  }
                  break;
                  
                case 'done':
                  // 完成
                  break;
                  
                case 'error':
                  throw new Error(data.data);
              }
            } catch (e) {
              console.error('解析SSE数据失败:', e);
            }
          }
        }
      }

      // ⚡ 答案已经在收到时立即显示，这里只需要更新引用
      if (receivedCitations.length > 0) {
        setCitations(receivedCitations.map(c => ({ ...c, retrievalTime })));
      }
      
      // 不再自动隐藏检索结果面板，让用户可以一直查看
      
      return { success: true, response: answerText };
    } catch (error) {
      console.error('发送消息错误:', error);
      
      // 检查是否是用户主动取消
      if (error.name === 'AbortError') {
        console.log('用户取消了请求');
        return { success: false, cancelled: true };
      }
      
      // 根据错误类型提供更具体的提示
      let errorMsg = '抱歉，发送消息时出错了。请稍后重试。';
      let toastMsg = '发送失败，请重试';
      
      if (error.code === 'ECONNABORTED') {
        errorMsg = '处理超时，您的问题可能较复杂。请尝试简化问题或稍后重试。';
        toastMsg = '处理超时（超过10分钟），请简化问题';
      } else if (error.response?.status === 500) {
        errorMsg = '服务器处理出错。' + (error.response?.data?.detail || '');
        toastMsg = '服务器错误';
      } else if (!error.response && !error.request) {
        errorMsg = '前端请求配置错误: ' + error.message;
        toastMsg = '前端错误';
      } else if (error.message?.includes('Network Error')) {
        errorMsg = '网络错误，请检查后端是否运行（http://localhost:8000）';
        toastMsg = '网络错误，检查后端';
      }
      
      toast.error(toastMsg);
      
      // 添加错误消息
      const errorMessage = {
        role: 'assistant',
        content: errorMsg,
        timestamp: new Date().toISOString(),
        error: true,
      };
      
      setMessages((prev) => [...prev, errorMessage]);
      
      throw error;
    } finally {
      setLoading(false);
      // 关闭处理中的提示
      if (processingToast) {
        toast.dismiss(processingToast);
      }
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
  
  // 停止生成
  const stopGeneration = useCallback(() => {
    if (abortControllerRef.current) {
      abortControllerRef.current.abort();
      abortControllerRef.current = null;
      setLoading(false);
      toast.success('已停止生成');
    }
  }, []);

  return {
    messages,
    loading,
    citations,
    confidence,
    qualityMetrics, // 新增：质量评估（雷达图）
    retrievalCitations, // 新增：检索阶段的引用
    showRetrievalResults, // 新增：是否显示检索结果
    sendChatMessage,
    clearMessages,
    setInitialMessages,
    stopGeneration,  // 导出停止函数
  };
};

export default useChat;


