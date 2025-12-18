/**
 * 会话管理 Hook
 */

import { useState, useCallback, useEffect } from 'react';
import { getSessions, createSession, getSessionMessages } from '../api/client';
import toast from 'react-hot-toast';

export const useSessions = () => {
  const [sessions, setSessions] = useState([]);
  const [currentSessionId, setCurrentSessionId] = useState(null);
  const [loading, setLoading] = useState(false);

  // 加载会话列表
  const loadSessions = useCallback(async () => {
    setLoading(true);
    try {
      const data = await getSessions();
      setSessions(data);
      
      // 设置当前会话
      if (data.length > 0 && !currentSessionId) {
        const currentSession = data.find(s => s.is_current);
        if (currentSession) {
          setCurrentSessionId(currentSession.session_id);
        } else {
          setCurrentSessionId(data[0].session_id);
        }
      }
    } catch (error) {
      console.error('加载会话失败:', error);
      toast.error('加载会话列表失败');
    } finally {
      setLoading(false);
    }
  }, [currentSessionId]);

  // 创建新会话
  const newSession = useCallback(async () => {
    try {
      const data = await createSession();
      toast.success('创建新对话');
      
      // 重新加载会话列表
      await loadSessions();
      
      // 切换到新会话
      setCurrentSessionId(data.session_id);
      
      return data.session_id;
    } catch (error) {
      console.error('创建会话失败:', error);
      toast.error('创建新对话失败');
      throw error;
    }
  }, [loadSessions]);

  // 切换会话
  const switchSession = useCallback(async (sessionId) => {
    setCurrentSessionId(sessionId);
    
    try {
      // 加载会话消息
      const data = await getSessionMessages(sessionId);
      return data.messages;
    } catch (error) {
      console.error('切换会话失败:', error);
      toast.error('切换对话失败');
      return [];
    }
  }, []);

  // 初始加载
  useEffect(() => {
    loadSessions();
  }, []);

  return {
    sessions,
    currentSessionId,
    loading,
    loadSessions,
    newSession,
    switchSession,
  };
};

export default useSessions;


