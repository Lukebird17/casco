/**
 * 文档查看器组件
 * 支持PDF、文本文件显示和引用高亮
 */

import React, { useState, useEffect, useRef } from 'react';
import { X, FileText, ExternalLink, Search, ZoomIn, ZoomOut } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import toast from 'react-hot-toast';

const DocumentViewer = ({ 
  open, 
  onClose, 
  filename = null,
  highlightText = null  // 要高亮的文本
}) => {
  const [documents, setDocuments] = useState([]);
  const [selectedDoc, setSelectedDoc] = useState(filename);
  const [content, setContent] = useState('');
  const [loading, setLoading] = useState(false);
  const [searchTerm, setSearchTerm] = useState('');
  const contentRef = useRef(null);

  // 获取文档列表
  useEffect(() => {
    if (open) {
      loadDocuments();
    }
  }, [open]);

  // 加载选中文档的内容
  useEffect(() => {
    if (selectedDoc) {
      loadDocumentContent(selectedDoc);
    }
  }, [selectedDoc]);

  // 高亮文本
  useEffect(() => {
    if (highlightText && content && contentRef.current) {
      setTimeout(() => {
        scrollToHighlight(highlightText);
      }, 500);
    }
  }, [highlightText, content]);

  const loadDocuments = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/documents');
      const data = await response.json();
      
      if (data.success) {
        setDocuments(data.documents);
        
        // 如果有指定文档，选中它
        if (filename && !selectedDoc) {
          setSelectedDoc(filename);
        }
      }
    } catch (error) {
      console.error('加载文档列表失败:', error);
      toast.error('加载文档列表失败');
    }
  };

  const loadDocumentContent = async (docFilename) => {
    setLoading(true);
    try {
      const response = await fetch(`http://localhost:8000/api/documents/${encodeURIComponent(docFilename)}`);
      const data = await response.json();
      
      if (data.success) {
        setContent(data.content);
      } else {
        toast.error('加载文档内容失败');
      }
    } catch (error) {
      console.error('加载文档内容失败:', error);
      toast.error('加载文档内容失败');
    } finally {
      setLoading(false);
    }
  };

  const scrollToHighlight = (text) => {
    if (!contentRef.current || !text) return;
    
    const contentElement = contentRef.current;
    const textContent = contentElement.textContent;
    const index = textContent.toLowerCase().indexOf(text.toLowerCase());
    
    if (index !== -1) {
      // 查找包含该文本的元素
      const walker = document.createTreeWalker(
        contentElement,
        NodeFilter.SHOW_TEXT,
        null,
        false
      );
      
      let currentPos = 0;
      let targetNode = null;
      
      while (walker.nextNode()) {
        const node = walker.currentNode;
        const nodeLength = node.textContent.length;
        
        if (currentPos + nodeLength > index) {
          targetNode = node.parentElement;
          break;
        }
        
        currentPos += nodeLength;
      }
      
      if (targetNode) {
        // 高亮并滚动到目标位置
        targetNode.style.backgroundColor = '#fef3c7';
        targetNode.style.padding = '2px 4px';
        targetNode.style.borderRadius = '4px';
        targetNode.scrollIntoView({ behavior: 'smooth', block: 'center' });
        
        // 3秒后移除高亮
        setTimeout(() => {
          targetNode.style.backgroundColor = '';
          targetNode.style.padding = '';
          targetNode.style.borderRadius = '';
        }, 3000);
      }
    }
  };

  const highlightSearchTerm = (text) => {
    if (!searchTerm) return text;
    
    const regex = new RegExp(`(${searchTerm})`, 'gi');
    return text.split(regex).map((part, index) => {
      if (part.toLowerCase() === searchTerm.toLowerCase()) {
        return <mark key={index} className="bg-yellow-200">{part}</mark>;
      }
      return part;
    });
  };

  const formatFileSize = (sizeMB) => {
    if (sizeMB < 1) {
      return `${(sizeMB * 1024).toFixed(0)} KB`;
    }
    return `${sizeMB.toFixed(2)} MB`;
  };

  return (
    <AnimatePresence>
      {open && (
        <>
          {/* 背景遮罩 */}
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={onClose}
            className="fixed inset-0 bg-black/50 z-50"
          />

          {/* 文档查看器主体 */}
          <motion.div
            initial={{ scale: 0.9, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            exit={{ scale: 0.9, opacity: 0 }}
            className="fixed inset-8 bg-white rounded-2xl shadow-2xl z-50 flex"
          >
            {/* 左侧：文档列表 */}
            <div className="w-72 border-r border-google-gray-200 flex flex-col">
              {/* 头部 */}
              <div className="p-4 border-b border-google-gray-200">
                <h3 className="text-lg font-semibold text-google-gray-900 flex items-center gap-2">
                  <FileText size={20} className="text-google-blue-600" />
                  文档库
                </h3>
                <p className="text-sm text-google-gray-600 mt-1">
                  共 {documents.length} 个文档
                </p>
              </div>

              {/* 文档列表 */}
              <div className="flex-1 overflow-y-auto p-2">
                {documents.map((doc) => (
                  <button
                    key={doc.filename}
                    onClick={() => setSelectedDoc(doc.filename)}
                    className={`w-full text-left p-3 rounded-lg mb-1 transition-colors ${
                      selectedDoc === doc.filename
                        ? 'bg-google-blue-50 border border-google-blue-300'
                        : 'hover:bg-google-gray-50 border border-transparent'
                    }`}
                  >
                    <div className="text-sm font-medium text-google-gray-900 truncate">
                      {doc.filename}
                    </div>
                    <div className="text-xs text-google-gray-500 mt-1">
                      {doc.type.toUpperCase()} • {formatFileSize(doc.size)}
                    </div>
                  </button>
                ))}
              </div>
            </div>

            {/* 右侧：文档内容 */}
            <div className="flex-1 flex flex-col">
              {/* 头部工具栏 */}
              <div className="p-4 border-b border-google-gray-200 flex items-center justify-between">
                <div className="flex-1 max-w-md">
                  <div className="relative">
                    <Search size={18} className="absolute left-3 top-1/2 -translate-y-1/2 text-google-gray-400" />
                    <input
                      type="text"
                      value={searchTerm}
                      onChange={(e) => setSearchTerm(e.target.value)}
                      placeholder="搜索文档内容..."
                      className="w-full pl-10 pr-4 py-2 rounded-lg border border-google-gray-300 
                               focus:outline-none focus:ring-2 focus:ring-google-blue-500"
                    />
                  </div>
                </div>

                <button
                  onClick={onClose}
                  className="btn-icon p-2 hover:bg-google-gray-100 rounded-lg ml-4"
                  title="关闭"
                >
                  <X size={20} />
                </button>
              </div>

              {/* 文档内容区域 */}
              <div className="flex-1 overflow-y-auto p-6">
                {loading ? (
                  <div className="flex items-center justify-center h-full">
                    <div className="text-center">
                      <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-google-blue-600 mx-auto mb-4"></div>
                      <p className="text-google-gray-600">加载中...</p>
                    </div>
                  </div>
                ) : selectedDoc ? (
                  <div 
                    ref={contentRef}
                    className="prose prose-sm max-w-none"
                  >
                    <h2 className="text-2xl font-bold text-google-gray-900 mb-4">
                      {selectedDoc}
                    </h2>
                    <div className="whitespace-pre-wrap text-google-gray-700 leading-relaxed">
                      {searchTerm ? highlightSearchTerm(content) : content}
                    </div>
                  </div>
                ) : (
                  <div className="flex items-center justify-center h-full">
                    <div className="text-center">
                      <FileText size={64} className="text-google-gray-300 mx-auto mb-4" />
                      <p className="text-google-gray-500">请从左侧选择一个文档</p>
                    </div>
                  </div>
                )}
              </div>
            </div>
          </motion.div>
        </>
      )}
    </AnimatePresence>
  );
};

export default DocumentViewer;

