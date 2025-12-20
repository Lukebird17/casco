/**
 * 文档智能大纲面板
 * 自动提取文档结构和关键章节
 */

import React, { useState, useEffect } from 'react';
import { X, FileText, ChevronRight, ChevronDown, Loader2, Hash, BookOpen } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import toast from 'react-hot-toast';

const DocumentOutlinePanel = ({ open, onClose, onJumpToSection, currentKBId = 'default', embedded = false }) => {
  const [documents, setDocuments] = useState([]);
  const [knowledgeBases, setKnowledgeBases] = useState([]);
  const [selectedKB, setSelectedKB] = useState(currentKBId);
  const [selectedDoc, setSelectedDoc] = useState(null);
  const [outline, setOutline] = useState(null);
  const [loading, setLoading] = useState(false);
  const [loadingMessage, setLoadingMessage] = useState('');
  const [loadingProgress, setLoadingProgress] = useState(0);
  const [expandedSections, setExpandedSections] = useState({});

  // 获取知识库和文档列表
  useEffect(() => {
    if (open) {
      loadKnowledgeBases();
      loadDocuments();
    }
  }, [open, selectedKB]);

  const loadKnowledgeBases = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/knowledge-bases');
      const data = await response.json();
      
      if (data.success) {
        setKnowledgeBases(data.knowledge_bases);
      }
    } catch (error) {
      console.error('加载知识库列表失败:', error);
    }
  };

  const loadDocuments = async () => {
    try {
      const response = await fetch(`http://localhost:8000/api/knowledge-bases/${selectedKB}/files`);
      const data = await response.json();
      
      console.log('文档列表数据:', data);
      
      if (data.success) {
        // 转换文件数据格式
        const formattedFiles = (data.files || []).map(file => ({
          filename: file.name,
          size: file.size,
          type: file.type
        }));
        setDocuments(formattedFiles);
      }
    } catch (error) {
      console.error('加载文档列表失败:', error);
      toast.error('加载文档列表失败');
    }
  };

  const loadDocumentOutline = async (filename) => {
    setLoading(true);
    setLoadingMessage('正在分析文档...');
    setLoadingProgress(0);
    
    try {
      // 模拟进度更新
      const progressInterval = setInterval(() => {
        setLoadingProgress(prev => {
          if (prev >= 90) return prev;
          return prev + 10;
        });
      }, 200);
      
      setLoadingMessage('正在提取大纲结构...');
      const response = await fetch(`http://localhost:8000/api/knowledge-bases/${selectedKB}/documents/${encodeURIComponent(filename)}/outline`);
      
      clearInterval(progressInterval);
      setLoadingProgress(100);
      
      if (response.ok) {
        const data = await response.json();
        if (data.success) {
          setLoadingMessage('提取完成！');
          setTimeout(() => {
            setOutline(data.outline);
            setSelectedDoc(filename);
            toast.success(`提取了 ${data.outline.sections?.length || 0} 个章节`);
          }, 300);
        }
      } else {
        toast.error('无法加载文档大纲');
      }
    } catch (error) {
      console.error('加载大纲失败:', error);
      toast.error('加载文档大纲失败');
    } finally {
      setTimeout(() => {
        setLoading(false);
        setLoadingProgress(0);
        setLoadingMessage('');
      }, 500);
    }
  };

  // 简单的大纲生成逻辑（基于标题和段落）
  const generateSimpleOutline = (content) => {
    const lines = content.split('\n');
    const outline = [];
    let currentSection = null;
    let sectionIndex = 1;

    lines.forEach((line, index) => {
      const trimmed = line.trim();
      
      // 检测标题（以#开头或全大写或数字开头）
      if (trimmed.startsWith('#') || /^[A-Z\s]{10,}$/.test(trimmed) || /^\d+\.?\s/.test(trimmed)) {
        const level = trimmed.startsWith('#') ? trimmed.match(/^#+/)[0].length : 1;
        const title = trimmed.replace(/^#+\s*/, '').replace(/^\d+\.?\s*/, '');
        
        if (title.length > 0 && title.length < 100) {
          currentSection = {
            id: `section-${sectionIndex}`,
            title: title,
            level: level,
            line: index,
            subsections: []
          };
          outline.push(currentSection);
          sectionIndex++;
        }
      }
    });

    return {
      document: selectedDoc,
      sections: outline
    };
  };

  const toggleSection = (sectionId) => {
    setExpandedSections(prev => ({
      ...prev,
      [sectionId]: !prev[sectionId]
    }));
  };

  const handleSectionClick = (section) => {
    if (onJumpToSection) {
      // 判断是否是PDF，如果是则传递页码
      const isPDF = selectedDoc.toLowerCase().endsWith('.pdf');
      onJumpToSection({
        filename: selectedDoc,
        section: section.title,
        page: section.page,
        line: section.line,
        isPDF: isPDF,
        kb_id: selectedKB  // ✅ 添加知识库ID
      });
    }
    toast.success(`跳转到: ${section.title}${section.page ? ` (第${section.page}页)` : ''}`);
  };

  // 如果是嵌入模式，直接渲染内容
  if (embedded) {
    return (
      <div className="h-full flex flex-col bg-white">
        <div className="flex-1 overflow-y-auto p-4">{renderPanelContent()}</div>
      </div>
    );
  }

  // 独立面板模式
  return (
    <AnimatePresence>
      {open && (
        <>
          {/* 面板主体 - 紧贴Sidebar，无遮罩 */}
          <motion.div
            initial={{ width: 0, opacity: 0 }}
            animate={{ width: 350, opacity: 1 }}
            exit={{ width: 0, opacity: 0 }}
            transition={{ type: 'spring', damping: 30, stiffness: 300 }}
            className="fixed left-[280px] top-0 bottom-0 bg-white shadow-lg z-20
                     border-r border-google-gray-200 flex flex-col"
          >
            {/* 头部 */}
            <div className="flex-shrink-0 bg-white border-b border-google-gray-200 p-4 flex items-center justify-between">
              <div className="flex items-center gap-3">
                <BookOpen size={24} className="text-google-blue-600" />
                <h2 className="text-xl font-semibold text-google-gray-900">文档大纲</h2>
              </div>
              <button
                onClick={onClose}
                className="btn-icon p-2 hover:bg-google-gray-100 rounded-lg"
              >
                <X size={20} />
              </button>
            </div>

            {/* 内容区 - 可滚动 */}
            <div className="flex-1 overflow-y-auto p-6">
              {/* 知识库选择 */}
              {knowledgeBases.length > 0 && (
                <div className="mb-4">
                  <label className="block text-sm font-medium text-google-gray-700 mb-2">
                    知识库
                  </label>
                  <select
                    value={selectedKB}
                    onChange={(e) => {
                      setSelectedKB(e.target.value);
                      setSelectedDoc(null);
                      setOutline(null);
                    }}
                    className="w-full px-3 py-2 border border-google-gray-300 rounded-lg 
                             focus:outline-none focus:ring-2 focus:ring-google-blue-500"
                  >
                    {knowledgeBases.map((kb) => (
                      <option key={kb.id} value={kb.id}>
                        {kb.name} ({kb.document_count} 文档)
                      </option>
                    ))}
                  </select>
                </div>
              )}

              {/* 文档选择 */}
              {!selectedDoc ? (
                <div>
                  <h3 className="text-sm font-semibold text-google-gray-900 mb-3">
                    选择一个文档 ({documents.length})
                  </h3>
                  <div className="space-y-2">
                    {documents.length === 0 ? (
                      <div className="text-center py-8 text-google-gray-500">
                        <FileText size={48} className="mx-auto mb-3 opacity-30" />
                        <p>当前知识库没有文档</p>
                        <p className="text-xs mt-1">请先上传文档</p>
                      </div>
                    ) : (
                      documents.map((doc) => (
                        <button
                          key={doc.filename}
                          onClick={() => loadDocumentOutline(doc.filename)}
                          className="w-full text-left p-3 rounded-lg border border-google-gray-200 
                                   hover:border-google-blue-300 hover:bg-google-blue-50 
                                   transition-colors"
                        >
                          <div className="flex items-center gap-2">
                            <FileText size={16} className="text-google-blue-600" />
                            <span className="text-sm font-medium text-google-gray-900">
                              {doc.filename}
                            </span>
                          </div>
                          <div className="text-xs text-google-gray-500 mt-1">
                            {doc.type.toUpperCase()} • {doc.size} MB
                          </div>
                        </button>
                      ))
                    )}
                  </div>
                </div>
              ) : loading ? (
                <div className="flex flex-col items-center justify-center py-12 px-6">
                  <Loader2 className="animate-spin text-google-blue-600 mb-4" size={40} />
                  <p className="text-sm font-medium text-google-gray-700 mb-2">
                    {loadingMessage || '加载中...'}
                  </p>
                  {/* 进度条 */}
                  <div className="w-full max-w-xs bg-google-gray-200 rounded-full h-2 mb-2">
                    <div 
                      className="bg-google-blue-600 h-2 rounded-full transition-all duration-300"
                      style={{ width: `${loadingProgress}%` }}
                    />
                  </div>
                  <p className="text-xs text-google-gray-500">
                    {loadingProgress}%
                  </p>
                </div>
              ) : outline ? (
                <div>
                  {/* 当前文档 */}
                  <div className="mb-4 p-3 bg-google-blue-50 rounded-lg border border-google-blue-200">
                    <div className="flex items-center gap-2 mb-1">
                      <FileText size={16} className="text-google-blue-600" />
                      <span className="text-sm font-medium text-google-gray-900">
                        {selectedDoc}
                      </span>
                    </div>
                    <button
                      onClick={() => { setSelectedDoc(null); setOutline(null); }}
                      className="text-xs text-google-blue-600 hover:text-google-blue-700"
                    >
                      ← 返回文档列表
                    </button>
                  </div>

                  {/* 大纲树 */}
                  {outline.sections && outline.sections.length > 0 ? (
                    <div className="space-y-1">
                      <h3 className="text-sm font-semibold text-google-gray-900 mb-3 flex items-center gap-2">
                        <Hash size={16} />
                        章节目录 ({outline.sections.length})
                      </h3>
                      {outline.sections.map((section) => (
                        <OutlineSection
                          key={section.id}
                          section={section}
                          expanded={expandedSections[section.id]}
                          onToggle={() => toggleSection(section.id)}
                          onClick={() => handleSectionClick(section)}
                        />
                      ))}
                    </div>
                  ) : (
                    <div className="text-center py-8 text-google-gray-500">
                      <FileText size={48} className="mx-auto mb-3 text-google-gray-300" />
                      <p>未能提取文档大纲</p>
                      <p className="text-xs mt-1">可能文档格式不包含明确的章节结构</p>
                    </div>
                  )}
                </div>
              ) : null}
            </div>
          </motion.div>
        </>
      )}
    </AnimatePresence>
  );
};

// 大纲章节组件
const OutlineSection = ({ section, expanded, onToggle, onClick }) => {
  const hasSubsections = section.subsections && section.subsections.length > 0;
  const indent = (section.level - 1) * 16;

  return (
    <div>
      <motion.button
        whileHover={{ x: 2 }}
        onClick={onClick}
        className="w-full text-left p-2 rounded-lg hover:bg-google-gray-100 
                 transition-colors group"
        style={{ paddingLeft: `${indent + 8}px` }}
      >
        <div className="flex items-center gap-2">
          {hasSubsections && (
            <button
              onClick={(e) => { e.stopPropagation(); onToggle(); }}
              className="p-0.5 hover:bg-google-gray-200 rounded"
            >
              {expanded ? (
                <ChevronDown size={14} className="text-google-gray-600" />
              ) : (
                <ChevronRight size={14} className="text-google-gray-600" />
              )}
            </button>
          )}
          <span className={`text-sm ${
            section.level === 1 ? 'font-semibold text-google-gray-900' :
            section.level === 2 ? 'font-medium text-google-gray-800' :
            'text-google-gray-700'
          } group-hover:text-google-blue-600 transition-colors`}>
            {section.title}
          </span>
        </div>
      </motion.button>

      {hasSubsections && expanded && (
        <div className="ml-4">
          {section.subsections.map((subsection) => (
            <OutlineSection
              key={subsection.id}
              section={subsection}
              expanded={expanded}
              onToggle={onToggle}
              onClick={onClick}
            />
          ))}
        </div>
      )}
    </div>
  );
};

export default DocumentOutlinePanel;

