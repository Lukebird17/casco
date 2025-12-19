/**
 * API 客户端
 * 与 FastAPI 后端通信
 */

import axios from 'axios';

const API_BASE = 'http://localhost:8000';

const client = axios.create({
  baseURL: API_BASE,
  timeout: 600000, // 600 秒超时（10分钟），因为图片描述+MinerU+检索+Rerank可能较慢
  headers: {
    'Content-Type': 'application/json',
  },
});

// 请求拦截器
client.interceptors.request.use(
  (config) => {
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// 响应拦截器
client.interceptors.response.use(
  (response) => {
    return response.data;
  },
  (error) => {
    console.error('API Error:', error);
    
    // 更详细的错误信息
    if (error.code === 'ECONNABORTED') {
      console.error('❌ 请求超时！处理时间过长。');
    } else if (error.response) {
      console.error('❌ 服务器错误:', error.response.status, error.response.data);
    } else if (error.request) {
      console.error('❌ 无响应，检查后端是否运行');
    } else {
      console.error('❌ 请求配置错误:', error.message);
    }
    
    return Promise.reject(error);
  }
);

// ============================================================
// API 方法
// ============================================================

/**
 * 初始化系统
 */
export const initializeSystem = async () => {
  return await client.post('/api/init');
};

/**
 * 发送聊天消息
 */
export const sendMessage = async (data) => {
  return await client.post('/api/chat', data);
};

/**
 * 获取会话列表
 */
export const getSessions = async () => {
  return await client.get('/api/sessions');
};

/**
 * 创建新会话
 */
export const createSession = async () => {
  return await client.post('/api/sessions/new');
};

/**
 * 获取会话消息
 */
export const getSessionMessages = async (sessionId) => {
  return await client.get(`/api/sessions/${sessionId}/messages`);
};

/**
 * 删除会话
 */
export const deleteSession = async (sessionId) => {
  return await client.delete(`/api/sessions/${sessionId}`);
};

/**
 * 重命名会话
 */
export const renameSession = async (sessionId, newName) => {
  return await client.put(`/api/sessions/${sessionId}/rename`, { name: newName });
};

/**
 * 生成测验
 */
export const generateQuiz = async (data) => {
  return await client.post('/api/quiz', data);
};

/**
 * 获取待复习闪卡
 */
export const getDueFlashcards = async () => {
  return await client.get('/api/flashcards/due');
};

/**
 * 保存片段
 */
export const saveSnippet = async (data) => {
  return await client.post('/api/snippets', data);
};

/**
 * 获取片段列表
 */
export const getSnippets = async (query = null) => {
  return await client.get('/api/snippets', { params: { query } });
};

/**
 * 获取热力图数据
 */
export const getHeatmap = async () => {
  return await client.get('/api/heatmap');
};

/**
 * 获取知识图谱
 */
export const getKnowledgeGraph = async () => {
  return await client.get('/api/knowledge-graph');
};

/**
 * 上传文件
 */
export const uploadFile = async (file) => {
  const formData = new FormData();
  formData.append('file', file);
  
  return await client.post('/api/upload', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
};

/**
 * 获取知识库列表
 */
export const listKnowledgeBases = async () => {
  return await client.get('/api/knowledge-bases');
};

/**
 * 创建知识库
 */
export const createKnowledgeBase = async (kbId, name) => {
  return await client.post('/api/knowledge-bases', { kb_id: kbId, name });
};

/**
 * 删除知识库
 */
export const deleteKnowledgeBase = async (kbId) => {
  return await client.delete(`/api/knowledge-bases/${kbId}`);
};

/**
 * 上传文件到知识库
 */
export const uploadToKnowledgeBase = async (kbId, file) => {
  const formData = new FormData();
  formData.append('file', file);
  
  return await client.post(`/api/knowledge-bases/${kbId}/upload`, formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
};

/**
 * 获取知识库文件列表
 */
export const getKnowledgeBaseFiles = async (kbId) => {
  return await client.get(`/api/knowledge-bases/${kbId}/files`);
};

/**
 * 获取知识库文档内容
 */
export const getKnowledgeBaseDocument = async (kbId, filename) => {
  return await client.get(`/api/knowledge-bases/${kbId}/documents/${encodeURIComponent(filename)}`);
};

/**
 * 获取知识库文档大纲
 */
export const getKnowledgeBaseOutline = async (kbId, filename) => {
  return await client.get(`/api/knowledge-bases/${kbId}/documents/${encodeURIComponent(filename)}/outline`);
};

/**
 * 获取知识库知识图谱
 */
export const getKnowledgeBaseGraph = async (kbId) => {
  return await client.get(`/api/knowledge-bases/${kbId}/knowledge-graph`);
};

/**
 * 创建闪卡
 */
export const createFlashcard = async (data) => {
  return await client.post('/api/flashcards', data);
};

/**
 * 复习闪卡
 */
export const reviewFlashcard = async (cardId, quality) => {
  return await client.post(`/api/flashcards/${cardId}/review`, { quality });
};

export default client;




