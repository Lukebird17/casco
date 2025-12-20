/**
 * 文档查看器组件
 * 支持实时显示：PDF、DOCX、PPTX、TXT、MD、图片
 */

import React, { useState, useEffect, useRef } from 'react';
import { 
  X, FileText, Image as ImageIcon, File, Download, 
  ChevronLeft, ChevronRight, ZoomIn, ZoomOut, Database 
} from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import toast from 'react-hot-toast';

const DocumentViewer = ({ 
  open, 
  onClose, 
  filename = null,
  highlightText = null,
  page = null,  // PDF页码
  embedded = false,  // 是否为内嵌模式（两栏布局中）
  selectedKnowledgeBase = 'default'  // 当前选择的知识库
}) => {
  const [documents, setDocuments] = useState([]);
  const [selectedDoc, setSelectedDoc] = useState(filename);
  const [loading, setLoading] = useState(false);
  const [currentPage, setCurrentPage] = useState(page || 1);
  const [totalPages, setTotalPages] = useState(1);
  const [zoom, setZoom] = useState(100);
  
  // 新增：知识库相关状态
  const [knowledgeBases, setKnowledgeBases] = useState([]);
  const [selectedKB, setSelectedKB] = useState(selectedKnowledgeBase);  // 使用传入的知识库

  // 获取文件扩展名
  const getFileExtension = (filename) => {
    if (!filename) return '';
    return filename.toLowerCase().split('.').pop();
  };

  // 获取文件类型
  const getFileType = (filename) => {
    const ext = getFileExtension(filename);
    
    if (ext === 'pdf') return 'pdf';
    if (['txt', 'md'].includes(ext)) return 'text';
    if (['jpg', 'jpeg', 'png', 'gif', 'webp', 'bmp', 'svg'].includes(ext)) return 'image';
    if (ext === 'docx') return 'docx';
    if (ext === 'pptx') return 'pptx';
    return 'unknown';
  };

  // 获取知识库列表
  useEffect(() => {
    if (open) {
      loadKnowledgeBases();
    }
  }, [open]);

  // 当外部传入的知识库改变时，同步更新
  useEffect(() => {
    if (selectedKnowledgeBase) {
      setSelectedKB(selectedKnowledgeBase);
    }
  }, [selectedKnowledgeBase]);

  // 当知识库改变时，加载文档列表
  useEffect(() => {
    if (open && selectedKB) {
      loadDocuments(selectedKB);
    }
  }, [open, selectedKB]);

  const loadKnowledgeBases = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/knowledge-bases');
      const data = await response.json();
      
      if (data.success) {
        setKnowledgeBases(data.knowledge_bases);
        const current = data.knowledge_bases.find(kb => kb.is_current);
        if (current) {
          setSelectedKB(current.id);
        }
      }
    } catch (error) {
      console.error('加载知识库列表失败:', error);
    }
  };

  // 更新选中的文档
  useEffect(() => {
    if (filename) {
      setSelectedDoc(filename);
    }
  }, [filename]);

  // 更新页码
  useEffect(() => {
    if (page) {
      setCurrentPage(page);
    }
  }, [page]);

  const loadDocuments = async (kbId) => {
    if (!kbId) {
      console.warn('loadDocuments: kbId为空');
      return;
    }
    
    console.log(`加载文档列表: ${kbId}`);
    
    try {
      // 从指定知识库加载文档
      const response = await fetch(
        `http://localhost:8000/api/knowledge-bases/${kbId}/files`
      );
      const data = await response.json();
      
      if (data.success) {
        console.log(`知识库 ${kbId} 包含 ${data.files.length} 个文件`);
        // 转换格式以匹配原来的documents格式
        const docs = (data.files || []).map(file => ({
          filename: file.name,
          size: file.size,
          type: file.type
        }));
        setDocuments(docs);
        
        // 如果切换知识库导致当前文档不在新列表中，清除选择
        if (selectedDoc && !docs.find(d => d.filename === selectedDoc)) {
          setSelectedDoc(null);
        }
      } else {
        console.error('API返回失败:', data);
        setDocuments([]);
        setSelectedDoc(null);
      }
    } catch (error) {
      console.error(`加载文档列表失败 (${kbId}):`, error);
      toast.error('加载文档列表失败');
      setDocuments([]);
      setSelectedDoc(null);
    }
  };

  const handleDocumentSelect = (docFilename) => {
    setSelectedDoc(docFilename);
    setCurrentPage(1);
    setZoom(100);
  };

  const handleDownload = () => {
    if (!selectedDoc) return;
    
    const url = `http://localhost:8000/api/documents/${encodeURIComponent(selectedDoc)}/raw`;
    const link = document.createElement('a');
    link.href = url;
    link.download = selectedDoc;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    toast.success('开始下载');
  };

  // 渲染不同类型的文档查看器
  const renderViewer = () => {
    if (!selectedDoc) {
      return (
        <div className="flex items-center justify-center h-full">
          <div className="text-center">
            <FileText size={64} className="text-google-gray-300 mx-auto mb-4" />
            <p className="text-google-gray-500">请从左侧选择一个文档</p>
          </div>
        </div>
      );
    }

    const fileType = getFileType(selectedDoc);
    // 使用知识库专用的API路径
    const baseUrl = `http://localhost:8000/api/knowledge-bases/${selectedKB}/documents`;
    const encodedFilename = encodeURIComponent(selectedDoc);

    switch (fileType) {
      case 'pdf':
        return (
          <div className="h-full flex flex-col bg-google-gray-100">
            <div className="flex-1 overflow-hidden">
              <iframe
                src={`${baseUrl}/${encodedFilename}/raw${currentPage ? `#page=${currentPage}` : ''}`}
                className="w-full h-full border-0"
                title={selectedDoc}
                key={`${selectedDoc}-${currentPage}`}
                style={{ transform: `scale(${zoom / 100})`, transformOrigin: 'top center' }}
              />
            </div>
            
            {/* PDF控制栏 */}
            <div className="bg-white border-t border-google-gray-200 p-3 flex items-center justify-between">
              <div className="flex items-center gap-2">
                <button
                  onClick={() => setCurrentPage(Math.max(1, currentPage - 1))}
                  className="p-2 hover:bg-google-gray-100 rounded-lg disabled:opacity-50"
                  disabled={currentPage <= 1}
                >
                  <ChevronLeft size={18} />
                </button>
                <span className="text-sm text-google-gray-700 min-w-[100px] text-center">
                  第 {currentPage} 页
                </span>
                <button
                  onClick={() => setCurrentPage(currentPage + 1)}
                  className="p-2 hover:bg-google-gray-100 rounded-lg"
                >
                  <ChevronRight size={18} />
                </button>
              </div>
              
              <div className="flex items-center gap-2">
                <button
                  onClick={() => setZoom(Math.max(50, zoom - 10))}
                  className="p-2 hover:bg-google-gray-100 rounded-lg"
                  title="缩小"
                >
                  <ZoomOut size={18} />
                </button>
                <span className="text-sm text-google-gray-700 min-w-[60px] text-center">
                  {zoom}%
                </span>
                <button
                  onClick={() => setZoom(Math.min(200, zoom + 10))}
                  className="p-2 hover:bg-google-gray-100 rounded-lg"
                  title="放大"
                >
                  <ZoomIn size={18} />
                </button>
              </div>
            </div>
          </div>
        );

      case 'text':
        return (
          <div className="h-full overflow-auto p-6 bg-white">
            <iframe
              src={`${baseUrl}/${encodedFilename}/raw`}
              className="w-full h-full border-0"
              title={selectedDoc}
              style={{
                fontFamily: 'monospace',
                fontSize: `${zoom}%`,
                whiteSpace: 'pre-wrap'
              }}
            />
          </div>
        );

      case 'image':
        return (
          <div className="h-full flex flex-col items-center justify-center bg-google-gray-900 p-6">
            <div className="flex-1 flex items-center justify-center overflow-auto w-full">
              <img
                src={`${baseUrl}/${encodedFilename}/raw`}
                alt={selectedDoc}
                className="max-w-full max-h-full object-contain"
                style={{ transform: `scale(${zoom / 100})` }}
              />
            </div>
            
            {/* 图片控制栏 */}
            <div className="bg-white border-t border-google-gray-200 p-3 flex items-center justify-center gap-2 w-full">
              <button
                onClick={() => setZoom(Math.max(10, zoom - 10))}
                className="p-2 hover:bg-google-gray-100 rounded-lg"
                title="缩小"
              >
                <ZoomOut size={18} />
              </button>
              <span className="text-sm text-google-gray-700 min-w-[60px] text-center">
                {zoom}%
              </span>
              <button
                onClick={() => setZoom(Math.min(500, zoom + 10))}
                className="p-2 hover:bg-google-gray-100 rounded-lg"
                title="放大"
              >
                <ZoomIn size={18} />
              </button>
              <button
                onClick={() => setZoom(100)}
                className="px-3 py-1.5 hover:bg-google-gray-100 rounded-lg text-sm"
              >
                重置
              </button>
            </div>
          </div>
        );

      case 'docx':
        return (
          <div className="h-full overflow-auto bg-white">
            <iframe
              src={`${baseUrl}/${encodedFilename}/preview/docx`}
              className="w-full h-full border-0"
              title={selectedDoc}
              style={{ fontSize: `${zoom}%` }}
            />
          </div>
        );

      case 'pptx':
        return (
          <div className="h-full flex flex-col">
            <div className="flex-1 overflow-auto bg-google-gray-100">
              <iframe
                src={`${baseUrl}/${encodedFilename}/preview/pptx?page=${currentPage}`}
                className="w-full h-full border-0"
                title={selectedDoc}
                key={`${selectedDoc}-${currentPage}`}
              />
            </div>
            
            {/* PPTX控制栏 */}
            <div className="bg-white border-t border-google-gray-200 p-3 flex items-center justify-between">
              <div className="flex items-center gap-2">
                <button
                  onClick={() => setCurrentPage(Math.max(1, currentPage - 1))}
                  className="p-2 hover:bg-google-gray-100 rounded-lg disabled:opacity-50"
                  disabled={currentPage <= 1}
                >
                  <ChevronLeft size={18} />
                </button>
                <span className="text-sm text-google-gray-700 min-w-[100px] text-center">
                  第 {currentPage} 页
                </span>
                <button
                  onClick={() => setCurrentPage(currentPage + 1)}
                  className="p-2 hover:bg-google-gray-100 rounded-lg"
                >
                  <ChevronRight size={18} />
                </button>
              </div>
            </div>
          </div>
        );

      default:
        return (
          <div className="flex items-center justify-center h-full">
            <div className="text-center">
              <File size={64} className="text-google-gray-300 mx-auto mb-4" />
              <p className="text-google-gray-600 mb-2">不支持预览此文件类型</p>
              <p className="text-sm text-google-gray-500 mb-4">{selectedDoc}</p>
              <button
                onClick={handleDownload}
                className="px-4 py-2 bg-google-blue-600 text-white rounded-lg 
                         hover:bg-google-blue-700 inline-flex items-center gap-2"
              >
                <Download size={16} />
                下载文件
              </button>
            </div>
          </div>
        );
    }
  };

  // 文档列表和查看器的共享内容
  const viewerContent = (
    <>
      {/* 左侧文档列表 */}
      <div className="w-64 border-r border-google-gray-200 flex flex-col bg-google-gray-50">
              <div className="p-4 border-b border-google-gray-200">
                <h3 className="font-semibold text-google-gray-900 flex items-center gap-2">
                  <Database size={16} />
                  文档列表
                </h3>
                
                {/* 知识库选择下拉菜单 */}
                <div className="mt-3">
                  <label className="text-xs text-google-gray-600 block mb-1">
                    选择知识库
                  </label>
                  <select
                    value={selectedKB}
                    onChange={(e) => setSelectedKB(e.target.value)}
                    className="w-full px-2 py-1.5 text-sm border border-google-gray-300 
                             rounded-md focus:outline-none focus:ring-2 focus:ring-google-blue-500
                             bg-white"
                  >
                    {knowledgeBases.map((kb) => (
                      <option key={kb.id} value={kb.id}>
                        {kb.name}
                      </option>
                    ))}
                  </select>
                </div>
                
                <p className="text-xs text-google-gray-500 mt-2">
                  {documents.length} 个文档
                </p>
              </div>
              
              <div className="flex-1 overflow-y-auto">
                {documents.map((doc) => {
                  const fileType = getFileType(doc.filename);
                  const isSelected = selectedDoc === doc.filename;
                  
                  return (
                    <button
                      key={doc.filename}
                      onClick={() => handleDocumentSelect(doc.filename)}
                      className={`w-full text-left p-3 border-b border-google-gray-200 
                               hover:bg-google-blue-50 transition-colors ${
                                 isSelected ? 'bg-google-blue-100 border-l-4 border-google-blue-600' : ''
                               }`}
                    >
                      <div className="flex items-start gap-2">
                        {fileType === 'pdf' && <FileText size={16} className="text-red-600 mt-0.5 flex-shrink-0" />}
                        {fileType === 'image' && <ImageIcon size={16} className="text-green-600 mt-0.5 flex-shrink-0" />}
                        {fileType === 'text' && <FileText size={16} className="text-blue-600 mt-0.5 flex-shrink-0" />}
                        {fileType === 'docx' && <FileText size={16} className="text-indigo-600 mt-0.5 flex-shrink-0" />}
                        {fileType === 'pptx' && <FileText size={16} className="text-orange-600 mt-0.5 flex-shrink-0" />}
                        {fileType === 'unknown' && <File size={16} className="text-google-gray-400 mt-0.5 flex-shrink-0" />}
                        
                        <div className="flex-1 min-w-0">
                          <p className="text-sm font-medium text-google-gray-900 truncate">
                            {doc.filename}
                          </p>
                          <p className="text-xs text-google-gray-500">
                            {doc.size} MB
                          </p>
                        </div>
                      </div>
                    </button>
                  );
                })}
              </div>
            </div>

            {/* 右侧查看器 */}
            <div className="flex-1 flex flex-col">
              {/* 头部 */}
              <div className="bg-white border-b border-google-gray-200 p-4 flex items-center justify-between">
                <div className="flex items-center gap-3">
                  <FileText size={20} className="text-google-blue-600" />
                  <div>
                    <h2 className="text-lg font-semibold text-google-gray-900">
                      {selectedDoc || '文档查看器'}
                    </h2>
                    {selectedDoc && (
                      <p className="text-xs text-google-gray-500">
                        {getFileType(selectedDoc).toUpperCase()} 文件
                      </p>
                    )}
                  </div>
                </div>
                
                <div className="flex items-center gap-2">
                  {selectedDoc && (
                    <button
                      onClick={handleDownload}
                      className="p-2 hover:bg-google-gray-100 rounded-lg"
                      title="下载文件"
                    >
                      <Download size={18} />
                    </button>
                  )}
                  <button
                    onClick={onClose}
                    className="p-2 hover:bg-google-gray-100 rounded-lg"
                  >
                    <X size={20} />
                  </button>
                </div>
              </div>

              {/* 查看器内容 */}
              <div className="flex-1 overflow-hidden">
                {renderViewer()}
              </div>
            </div>
    </>
  );

  // 内嵌模式：直接渲染，不需要背景遮罩和动画
  if (embedded) {
    return open ? (
      <div className="h-full flex bg-white overflow-hidden">
        {viewerContent}
      </div>
    ) : null;
  }

  // 覆盖模式：带背景遮罩和动画
  return (
    <AnimatePresence>
      {open && (
        <>
          {/* 背景遮罩 - 半透明 */}
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={onClose}
            className="fixed inset-0 bg-black/30 z-40"
          />

          {/* 查看器主体 - 右侧面板 */}
          <motion.div
            initial={{ x: '100%' }}
            animate={{ x: 0 }}
            exit={{ x: '100%' }}
            transition={{ type: 'spring', damping: 25, stiffness: 200 }}
            className="fixed right-0 top-0 bottom-0 w-[90%] md:w-[75%] lg:w-[65%] bg-white shadow-2xl z-50 
                     overflow-hidden flex"
          >
            {viewerContent}
          </motion.div>
        </>
      )}
    </AnimatePresence>
  );
};

export default DocumentViewer;
