/**
 * 主应用组件
 * 整合所有功能模块
 */

import React, { useState, useEffect } from 'react';
import { Toaster } from 'react-hot-toast';
import toast from 'react-hot-toast';
import { motion, AnimatePresence } from 'framer-motion';
import Sidebar from './components/Sidebar';
import ChatInterface from './components/ChatInterface';
import ToolPanel from './components/ToolPanel';
import SnippetsPanel from './components/SnippetsPanel';
import HeatmapPanel from './components/HeatmapPanel';
import QuizPanel from './components/QuizPanel';
import FlashcardPanel from './components/FlashcardPanel';
// import KnowledgeGraphPanel from './components/KnowledgeGraphPanel';  // ✅ 已删除
import DocumentViewer from './components/DocumentViewer';
// import ConfidencePanel from './components/ConfidencePanel';  // ✅ 已删除，功能整合到ToolPanel
import DocumentOutlinePanel from './components/DocumentOutlinePanel';
import ConceptSearchPanel from './components/ConceptSearchPanel';
import KnowledgeBasePanel from './components/KnowledgeBasePanel';
import SettingsPanel from './components/SettingsPanel';
import WelcomeGuide from './components/WelcomeGuide';
import { useChat } from './hooks/useChat';
import { useSessions } from './hooks/useSessions';
import { initializeSystem, getSessionMessages } from './api/client';
import { initSettings, getSettings } from './utils/settings';
import { Info, Loader2, X } from 'lucide-react';

function App() {
  const [initializing, setInitializing] = useState(true);
  const [showWelcome, setShowWelcome] = useState(false);
  const [assistantConfig, setAssistantConfig] = useState(null);
  const [enableSocratic, setEnableSocratic] = useState(false);
  const [darkMode, setDarkMode] = useState(false);
  const [toolPanelOpen, setToolPanelOpen] = useState(false);
  const [snippetsPanelOpen, setSnippetsPanelOpen] = useState(false);
  const [heatmapPanelOpen, setHeatmapPanelOpen] = useState(false);
  const [quizPanelOpen, setQuizPanelOpen] = useState(false);
  const [flashcardPanelOpen, setFlashcardPanelOpen] = useState(false);
  // const [knowledgeGraphPanelOpen, setKnowledgeGraphPanelOpen] = useState(false);  // 已移除
  const [documentViewerOpen, setDocumentViewerOpen] = useState(false);
  // const [confidencePanelOpen, setConfidencePanelOpen] = useState(false);  // ✅ 已删除
  const [outlinePanelOpen, setOutlinePanelOpen] = useState(false);
  const [conceptSearchPanelOpen, setConceptSearchPanelOpen] = useState(false);
  const [knowledgeBasePanelOpen, setKnowledgeBasePanelOpen] = useState(false);
  const [settingsPanelOpen, setSettingsPanelOpen] = useState(false);
  const [activeTool, setActiveTool] = useState(null);
  const [viewerDocument, setViewerDocument] = useState(null);
  const [viewerHighlight, setViewerHighlight] = useState(null);
  const [viewerPage, setViewerPage] = useState(null);
  const [selectedKnowledgeBase, setSelectedKnowledgeBase] = useState('default'); // 全局知识库选择

  // 会话管理
  const {
    sessions,
    currentSessionId,
    loading: sessionsLoading,
    newSession,
    switchSession,
    deleteSession,
    renameSession,
  } = useSessions();

  // 聊天管理
  const {
    messages,
    loading: chatLoading,
    citations,
    confidence,
    qualityMetrics, // 新增：质量评估（雷达图）
    retrievalCitations,
    showRetrievalResults,
    sendChatMessage,
    clearMessages,
    setInitialMessages,
    stopGeneration,  // 新增：停止生成
  } = useChat(currentSessionId);

  // 初始化系统
  useEffect(() => {
    const init = async () => {
      try {
        // 初始化设置
        initSettings();
        
        // 加载dark模式设置
        const settings = getSettings();
        setDarkMode(settings.theme === 'dark');
        
        // 初始化后端
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
  
  // 监听会话切换，自动加载历史消息
  useEffect(() => {
    const loadSessionHistory = async () => {
      if (currentSessionId && !initializing) {
        try {
          const data = await getSessionMessages(currentSessionId);
          if (data.messages && data.messages.length > 0) {
            setInitialMessages(data.messages);
            console.log(`✅ 加载会话历史: ${data.messages.length} 条消息`);
          }
        } catch (error) {
          console.error('加载会话历史失败:', error);
        }
      }
    };
    
    loadSessionHistory();
  }, [currentSessionId, initializing]);
  
  // 应用dark模式
  useEffect(() => {
    if (darkMode) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [darkMode]);

  // 处理新会话
  const handleNewSession = async () => {
    try {
      // 显示引导界面
      setShowWelcome(true);
    } catch (error) {
      console.error('创建新会话失败:', error);
    }
  };

  // 处理引导完成
  const handleWelcomeComplete = async (config) => {
    try {
      setAssistantConfig(config);
      setShowWelcome(false);
      
      // 创建新会话
      await newSession();
      clearMessages();
      
      // 存储配置到localStorage
      localStorage.setItem('assistantConfig', JSON.stringify(config));
      
      toast.success(`已配置 ${config.personality} 风格助教`);
    } catch (error) {
      console.error('创建新会话失败:', error);
      toast.error('创建会话失败');
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

  // 处理删除会话
  const handleDeleteSession = async (sessionId) => {
    try {
      const historyMessages = await deleteSession(sessionId);
      setInitialMessages(historyMessages || []);
    } catch (error) {
      console.error('删除会话失败:', error);
    }
  };

  // 处理重命名会话
  const handleRenameSession = async (sessionId, newName) => {
    try {
      await renameSession(sessionId, newName);
    } catch (error) {
      console.error('重命名会话失败:', error);
    }
  };

  // 处理发送消息
  const handleSendMessage = async (message, options) => {
    try {
      // 获取设置
      const settings = getSettings();
      
      await sendChatMessage(message, {
        ...options,
        enableSocratic: settings.enableSocratic || enableSocratic,
        temperature: settings.temperature,
        maxTokens: settings.maxTokens,
        retrievalK: settings.retrievalK,
        knowledgeBaseId: selectedKnowledgeBase, // 使用全局知识库选择
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
    // 检查是否点击了已打开的工具，如果是则关闭它
    const isAlreadyOpen = (
      (toolId === 'snippets' && snippetsPanelOpen) ||
      (toolId === 'heatmap' && heatmapPanelOpen) ||
      (toolId === 'quiz' && quizPanelOpen) ||
      (toolId === 'flashcards' && flashcardPanelOpen) ||
      // (toolId === 'knowledge-graph' && knowledgeGraphPanelOpen) ||  // ✅ 已删除
      (toolId === 'database' && knowledgeBasePanelOpen) ||
      // (toolId === 'confidence' && confidencePanelOpen) ||  // ✅ 已删除
      (toolId === 'outline' && outlinePanelOpen) ||
      (toolId === 'concept-search' && conceptSearchPanelOpen) ||
      (toolId === 'settings' && settingsPanelOpen)
    );

    if (isAlreadyOpen) {
      // 如果已经打开，就关闭它
      switch(toolId) {
        case 'snippets': setSnippetsPanelOpen(false); break;
        case 'heatmap': setHeatmapPanelOpen(false); break;
        case 'quiz': setQuizPanelOpen(false); break;
        case 'flashcards': setFlashcardPanelOpen(false); break;
        // case 'knowledge-graph': setKnowledgeGraphPanelOpen(false); break;  // ✅ 已删除
        case 'database': setKnowledgeBasePanelOpen(false); break;
        // case 'confidence': setConfidencePanelOpen(false); break;  // ✅ 已删除
        case 'outline': setOutlinePanelOpen(false); break;
        case 'concept-search': setConceptSearchPanelOpen(false); break;
        case 'settings': setSettingsPanelOpen(false); break;
      }
      setActiveTool(null);
      return;
    }

    setActiveTool(toolId);
    
    // 关闭所有工具面板（但不关闭文档查看器，因为它在右侧）
    setToolPanelOpen(false);
    setSnippetsPanelOpen(false);
    setHeatmapPanelOpen(false);
    setQuizPanelOpen(false);
    setFlashcardPanelOpen(false);
    // setKnowledgeGraphPanelOpen(false);  // ✅ 已删除
    // setConfidencePanelOpen(false);  // ✅ 已删除
    setOutlinePanelOpen(false);
    setConceptSearchPanelOpen(false);
    setKnowledgeBasePanelOpen(false);
    setSettingsPanelOpen(false);
    
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
      // case 'knowledge-graph':  // ✅ 已删除
      //   setKnowledgeGraphPanelOpen(true);
      //   break;
      case 'database':
        setKnowledgeBasePanelOpen(true);
        break;
      case 'documents':
        setViewerDocument(null);
        setViewerHighlight(null);
        setDocumentViewerOpen(true);
        break;
      // case 'confidence':  // ✅ 已删除
      //   setConfidencePanelOpen(true);
      //   break;
      case 'outline':
        setOutlinePanelOpen(true);
        break;
      case 'concept-search':
        setConceptSearchPanelOpen(true);
        break;
      case 'settings':
        setSettingsPanelOpen(true);
        break;
      default:
        toast.success(`打开工具: ${toolId}`);
    }
  };

  // 处理跳转到引用
  const handleJumpToCitation = (citationOrId) => {
    console.log('跳转到引用:', citationOrId);
    
    // ✅ 判断输入类型：可能是citation对象，也可能是cite_id字符串
    let citation;
    if (typeof citationOrId === 'string') {
      // 从retrievalCitations中查找对应的citation
      citation = retrievalCitations.find(c => c.id === citationOrId);
      if (!citation) {
        console.warn('未找到引用:', citationOrId);
        toast.error('未找到该引用');
        return;
      }
    } else {
      citation = citationOrId;
    }
    
    // ✅ 使用 citation 中的 kb_id，如果没有则使用当前选中的知识库
    const targetKbId = citation.kb_id || selectedKnowledgeBase;
    
    // ✅ 如果目标知识库与当前不同，先切换知识库
    if (targetKbId !== selectedKnowledgeBase) {
      console.log(`切换知识库: ${selectedKnowledgeBase} -> ${targetKbId}`);
      setSelectedKnowledgeBase(targetKbId);
    }
    
    // 设置文档、页码和高亮文本
    setViewerDocument(citation.filename);
    setViewerPage(citation.page || null);
    setViewerHighlight(citation.snippet || '');
    
    // 打开文档查看器
    setDocumentViewerOpen(true);
    
    const pageInfo = citation.page ? ` 第${citation.page}页` : '';
    const kbInfo = targetKbId !== 'default' ? ` (知识库: ${targetKbId})` : '';
    toast.success(`正在打开: ${citation.filename}${pageInfo}${kbInfo}`, { icon: '📄' });
  };

  // 加载界面
  if (initializing) {
    return (
      <div className="h-screen flex items-center justify-center bg-google-gray-50 dark:bg-gray-900">
        <div className="text-center">
          <Loader2 size={48} className="animate-spin text-google-blue-600 mx-auto mb-4" />
          <p className="text-google-gray-600 dark:text-gray-300">正在初始化系统...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="h-screen flex bg-google-gray-50 dark:bg-gray-900">
      {/* 侧边栏 */}
      <Sidebar
        sessions={sessions}
        currentSessionId={currentSessionId}
        onNewSession={handleNewSession}
        onSwitchSession={handleSwitchSession}
        onDeleteSession={handleDeleteSession}
        onRenameSession={handleRenameSession}
        onOpenTool={handleOpenTool}
        onOpenSettings={() => handleOpenTool('settings')}
      />

      {/* 主内容区 - 支持两栏布局 */}
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
          <div className="flex items-center gap-2">
            {/* 文档查看器开关按钮 */}
            {documentViewerOpen && (
              <button
                onClick={() => setDocumentViewerOpen(false)}
                className="btn-icon p-2 rounded-lg hover:bg-google-gray-100 text-google-gray-700"
                title="关闭文档查看器"
              >
                <X size={20} />
              </button>
            )}
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
        </div>

        {/* 两栏布局：聊天界面 + 文档查看器 */}
        <div className="flex-1 flex overflow-hidden">
          {/* 聊天界面 */}
          <div className={`flex-1 overflow-hidden transition-all duration-300 flex flex-col ${
            documentViewerOpen ? 'border-r border-google-gray-200' : ''
          }`}>
            {/* 欢迎引导界面 */}
            <AnimatePresence>
              {showWelcome && (
                <div className="p-6 overflow-y-auto">
                  <WelcomeGuide onComplete={handleWelcomeComplete} />
                </div>
              )}
            </AnimatePresence>

            {/* 聊天界面 */}
            {!showWelcome && (
              <ChatInterface
                messages={messages}
                loading={chatLoading}
                onSendMessage={handleSendMessage}
                onStopGeneration={stopGeneration}
                enableSocratic={enableSocratic}
                currentSessionId={currentSessionId}
                selectedKnowledgeBase={selectedKnowledgeBase}
                onKnowledgeBaseChange={setSelectedKnowledgeBase}
                retrievalCitations={retrievalCitations}
                showRetrievalResults={showRetrievalResults}
                onCitationClick={handleJumpToCitation}
              />
            )}
          </div>

          {/* 文档查看器（内嵌版本） */}
          {documentViewerOpen && (
            <div className="w-[45%] flex flex-col bg-white">
              <DocumentViewer
                open={true}
                onClose={() => setDocumentViewerOpen(false)}
                filename={viewerDocument}
                highlightText={viewerHighlight}
                page={viewerPage}
                embedded={true}
                selectedKnowledgeBase={selectedKnowledgeBase}
              />
            </div>
          )}
        </div>
      </div>

      {/* 工具面板 */}
      <ToolPanel
        open={toolPanelOpen}
        onClose={() => setToolPanelOpen(false)}
        confidence={confidence}
        qualityMetrics={qualityMetrics} // 新增：传递质量评估数据
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

      {/* 知识图谱面板 - ✅ 已删除 */}
      {/* <KnowledgeGraphPanel
        open={knowledgeGraphPanelOpen}
        onClose={() => setKnowledgeGraphPanelOpen(false)}
      /> */}

      {/* 文档查看器已移至主内容区两栏布局中 */}

      {/* 独立面板 - 从左侧显示，避免遮挡右侧文档查看器 */}
      {/* <ConfidencePanel  // ✅ 已删除，功能整合到ToolPanel的AI自省报告中
        open={confidencePanelOpen}
        onClose={() => setConfidencePanelOpen(false)}
        confidence={confidence}
      /> */}

      <DocumentOutlinePanel
        open={outlinePanelOpen}
        onClose={() => setOutlinePanelOpen(false)}
        onJumpToSection={(section) => {
          // ✅ 如果传入的知识库与当前不同，先切换
          if (section.kb_id && section.kb_id !== selectedKnowledgeBase) {
            console.log(`切换知识库: ${selectedKnowledgeBase} -> ${section.kb_id}`);
            setSelectedKnowledgeBase(section.kb_id);
          }
          
          setViewerDocument(section.filename);
          setViewerHighlight(section.section);
          setViewerPage(section.page || null);
          setDocumentViewerOpen(true);
        }}
        currentKBId={selectedKnowledgeBase}
      />

      <ConceptSearchPanel
        open={conceptSearchPanelOpen}
        onClose={() => setConceptSearchPanelOpen(false)}
        onJumpTo={(location) => {
          // ✅ 如果传入的知识库与当前不同，先切换
          if (location.kb_id && location.kb_id !== selectedKnowledgeBase) {
            console.log(`切换知识库: ${selectedKnowledgeBase} -> ${location.kb_id}`);
            setSelectedKnowledgeBase(location.kb_id);
          }
          
          setViewerDocument(location.filename);
          setViewerHighlight(location.highlight);
          setViewerPage(location.page || null);
          setDocumentViewerOpen(true);
        }}
        currentKBId={selectedKnowledgeBase}
      />

      <KnowledgeBasePanel
        open={knowledgeBasePanelOpen}
        onClose={() => setKnowledgeBasePanelOpen(false)}
        onSwitch={(kbId) => {
          toast.success(`已切换到知识库: ${kbId}`);
          setSelectedKnowledgeBase(kbId);
        }}
      />

      {/* 设置面板 */}
      <SettingsPanel
        open={settingsPanelOpen}
        onClose={() => setSettingsPanelOpen(false)}
        darkMode={darkMode}
        onDarkModeChange={setDarkMode}
      />

      {/* Toast 通知 */}
      <Toaster position="bottom-right" />
    </div>
  );
}

export default App;

