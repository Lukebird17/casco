/**
 * 主应用组件
 * 整合所有功能模块
 */

import React, { useState, useEffect } from 'react';
import { Toaster } from 'react-hot-toast';
import toast from 'react-hot-toast';
import Sidebar from './components/Sidebar';
import ChatInterface from './components/ChatInterface';
import ToolPanel from './components/ToolPanel';
import SnippetsPanel from './components/SnippetsPanel';
import HeatmapPanel from './components/HeatmapPanel';
import QuizPanel from './components/QuizPanel';
import FlashcardPanel from './components/FlashcardPanel';
import KnowledgeGraphPanel from './components/KnowledgeGraphPanel';
import DocumentViewer from './components/DocumentViewer';
import { useChat } from './hooks/useChat';
import { useSessions } from './hooks/useSessions';
import { initializeSystem } from './api/client';
import { Info, Loader2 } from 'lucide-react';

function App() {
  const [initializing, setInitializing] = useState(true);
  const [enableSocratic, setEnableSocratic] = useState(false);
  const [toolPanelOpen, setToolPanelOpen] = useState(false);
  const [snippetsPanelOpen, setSnippetsPanelOpen] = useState(false);
  const [heatmapPanelOpen, setHeatmapPanelOpen] = useState(false);
  const [quizPanelOpen, setQuizPanelOpen] = useState(false);
  const [flashcardPanelOpen, setFlashcardPanelOpen] = useState(false);
  const [knowledgeGraphPanelOpen, setKnowledgeGraphPanelOpen] = useState(false);
  const [documentViewerOpen, setDocumentViewerOpen] = useState(false);
  const [activeTool, setActiveTool] = useState(null);
  const [viewerDocument, setViewerDocument] = useState(null);
  const [viewerHighlight, setViewerHighlight] = useState(null);

  // 会话管理
  const {
    sessions,
    currentSessionId,
    loading: sessionsLoading,
    newSession,
    switchSession,
  } = useSessions();

  // 聊天管理
  const {
    messages,
    loading: chatLoading,
    citations,
    confidence,
    sendChatMessage,
    clearMessages,
    setInitialMessages,
  } = useChat(currentSessionId);

  // 初始化系统
  useEffect(() => {
    const init = async () => {
      try {
        const result = await initializeSystem();
        if (result.success) {
          toast.success('系统初始化成功');
        }
      } catch (error) {
        console.error('初始化失败:', error);
        toast.error('系统初始化失败');
      } finally {
        setInitializing(false);
      }
    };

    init();
  }, []);

  // 处理新会话
  const handleNewSession = async () => {
    try {
      await newSession();
      clearMessages();
    } catch (error) {
      console.error('创建新会话失败:', error);
    }
  };

  // 处理切换会话
  const handleSwitchSession = async (sessionId) => {
    try {
      const historyMessages = await switchSession(sessionId);
      setInitialMessages(historyMessages || []);
    } catch (error) {
      console.error('切换会话失败:', error);
    }
  };

  // 处理发送消息
  const handleSendMessage = async (message, options) => {
    try {
      await sendChatMessage(message, {
        ...options,
        enableSocratic,
      });
      
      // 如果有引用，自动打开工具面板
      if (citations && citations.length > 0) {
        setToolPanelOpen(true);
      }
    } catch (error) {
      console.error('发送消息失败:', error);
    }
  };

  // 处理打开工具
  const handleOpenTool = (toolId) => {
    setActiveTool(toolId);
    
    // 关闭所有面板
    setToolPanelOpen(false);
    setSnippetsPanelOpen(false);
    setHeatmapPanelOpen(false);
    setQuizPanelOpen(false);
    setFlashcardPanelOpen(false);
    setKnowledgeGraphPanelOpen(false);
    setDocumentViewerOpen(false);
    
    // 打开对应工具
    switch(toolId) {
      case 'snippets':
        setSnippetsPanelOpen(true);
        break;
      case 'heatmap':
        setHeatmapPanelOpen(true);
        break;
      case 'quiz':
        setQuizPanelOpen(true);
        break;
      case 'flashcards':
        setFlashcardPanelOpen(true);
        break;
      case 'knowledge-graph':
        setKnowledgeGraphPanelOpen(true);
        break;
      case 'database':
        toast('知识库管理功能开发中...', { icon: '🚧' });
        break;
      case 'documents':
        setViewerDocument(null);
        setViewerHighlight(null);
        setDocumentViewerOpen(true);
        break;
      default:
        toast.success(`打开工具: ${toolId}`);
    }
  };

  // 处理跳转到引用
  const handleJumpToCitation = (citation) => {
    console.log('跳转到引用:', citation);
    
    // 设置文档和高亮文本
    setViewerDocument(citation.filename);
    setViewerHighlight(citation.snippet || '');
    
    // 打开文档查看器
    setDocumentViewerOpen(true);
    
    toast.success(`正在打开: ${citation.filename}`, { icon: '📄' });
  };

  // 加载界面
  if (initializing) {
    return (
      <div className="h-screen flex items-center justify-center bg-google-gray-50">
        <div className="text-center">
          <Loader2 size={48} className="animate-spin text-google-blue-600 mx-auto mb-4" />
          <p className="text-google-gray-600">正在初始化系统...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="h-screen flex bg-google-gray-50">
      {/* Toast 通知 */}
      <Toaster 
        position="top-right"
        toastOptions={{
          duration: 3000,
          style: {
            background: '#fff',
            color: '#1f2937',
            boxShadow: '0 4px 6px -1px rgb(0 0 0 / 0.1)',
          },
          success: {
            iconTheme: {
              primary: '#4285f4',
              secondary: '#fff',
            },
          },
        }}
      />

      {/* 侧边栏 */}
      <Sidebar
        sessions={sessions}
        currentSessionId={currentSessionId}
        onNewSession={handleNewSession}
        onSwitchSession={handleSwitchSession}
        onOpenTool={handleOpenTool}
      />

      {/* 主内容区 */}
      <div className="flex-1 flex flex-col">
        {/* 顶部工具栏 */}
        <div className="bg-white border-b border-google-gray-200 px-6 py-3 flex items-center justify-between">
          <div className="flex items-center gap-4">
            <h2 className="text-lg font-medium text-google-gray-900">
              {sessions.find(s => s.session_id === currentSessionId)?.name || '新对话'}
            </h2>
            
            {/* 苏格拉底模式开关 */}
            <label className="flex items-center gap-2 cursor-pointer">
              <input
                type="checkbox"
                checked={enableSocratic}
                onChange={(e) => setEnableSocratic(e.target.checked)}
                className="sr-only"
              />
              <div className={`relative w-11 h-6 rounded-full transition-colors ${
                enableSocratic ? 'bg-purple-600' : 'bg-google-gray-300'
              }`}>
                <div className={`absolute top-0.5 left-0.5 w-5 h-5 bg-white rounded-full transition-transform ${
                  enableSocratic ? 'transform translate-x-5' : ''
                }`} />
              </div>
              <span className="text-sm text-google-gray-700">
                🧙‍♂️ 苏格拉底模式
              </span>
            </label>
          </div>

          {/* 右侧按钮 */}
          <button
            onClick={() => setToolPanelOpen(!toolPanelOpen)}
            className={`btn-icon p-2 rounded-lg ${
              toolPanelOpen ? 'bg-google-blue-50 text-google-blue-600' : 'hover:bg-google-gray-100'
            }`}
            title="详细信息"
          >
            <Info size={20} />
          </button>
        </div>

        {/* 聊天界面 */}
        <div className="flex-1 overflow-hidden">
          <ChatInterface
            messages={messages}
            loading={chatLoading}
            onSendMessage={handleSendMessage}
            enableSocratic={enableSocratic}
            currentSessionId={currentSessionId}
          />
        </div>
      </div>

      {/* 工具面板 */}
      <ToolPanel
        open={toolPanelOpen}
        onClose={() => setToolPanelOpen(false)}
        confidence={confidence}
        citations={citations}
        onJumpToCitation={handleJumpToCitation}
      />

      {/* 片段收藏面板 */}
      <SnippetsPanel
        open={snippetsPanelOpen}
        onClose={() => setSnippetsPanelOpen(false)}
        currentSessionId={currentSessionId}
      />

      {/* 热力图面板 */}
      <HeatmapPanel
        open={heatmapPanelOpen}
        onClose={() => setHeatmapPanelOpen(false)}
      />

      {/* 智能测验面板 */}
      <QuizPanel
        open={quizPanelOpen}
        onClose={() => setQuizPanelOpen(false)}
      />

      {/* 记忆闪卡面板 */}
      <FlashcardPanel
        open={flashcardPanelOpen}
        onClose={() => setFlashcardPanelOpen(false)}
      />

      {/* 知识图谱面板 */}
      <KnowledgeGraphPanel
        open={knowledgeGraphPanelOpen}
        onClose={() => setKnowledgeGraphPanelOpen(false)}
      />

      {/* 文档查看器 */}
      <DocumentViewer
        open={documentViewerOpen}
        onClose={() => setDocumentViewerOpen(false)}
        filename={viewerDocument}
        highlightText={viewerHighlight}
      />
    </div>
  );
}

export default App;

