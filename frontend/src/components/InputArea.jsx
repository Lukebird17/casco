/**
 * 输入区域组件
 * Gemini 风格的底部输入框
 */

import React, { useState, useRef, useEffect } from 'react';
import { Send, Image, Paperclip, Loader2, Zap, Brain, Database } from 'lucide-react';
import toast from 'react-hot-toast';
import { listKnowledgeBases } from '../api/client';

const InputArea = ({ 
  onSend, 
  loading, 
  enableSocratic,
  selectedKnowledgeBase,
  onKnowledgeBaseChange 
}) => {
  const [message, setMessage] = useState('');
  const [imageFile, setImageFile] = useState(null);
  const [docFile, setDocFile] = useState(null);
  const [thinkingMode, setThinkingMode] = useState('fast'); // 'fast' 或 'thinking'
  const [knowledgeBases, setKnowledgeBases] = useState([]);
  const imageInputRef = useRef(null);
  const fileInputRef = useRef(null);

  // 加载知识库列表
  useEffect(() => {
    const loadKBs = async () => {
      try {
        const response = await listKnowledgeBases();
        if (response.success && response.knowledge_bases) {
          setKnowledgeBases(response.knowledge_bases);
        }
      } catch (error) {
        console.error('加载知识库列表失败:', error);
        // 如果加载失败，设置默认知识库
        setKnowledgeBases([{ id: 'default', name: '默认知识库' }]);
      }
    };
    loadKBs();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!message.trim() && !imageFile && !docFile) {
      toast.error('请输入消息或上传文件');
      return;
    }

    // 准备发送（不需要传递 knowledgeBaseId，因为 App.jsx 会自动添加）
    const options = {
      enableSocratic,
      thinkingMode, // 添加思考模式
    };

    // 处理图片
    if (imageFile) {
      const reader = new FileReader();
      reader.onload = () => {
        options.image = reader.result;
        sendMessage(options);
      };
      reader.readAsDataURL(imageFile);
    } else if (docFile) {
      // 处理文档上传
      const toastId = toast.loading('正在上传文件...');
      
      try {
        // 创建FormData上传文件
        const formData = new FormData();
        formData.append('file', docFile);
        
        // 调用上传API
        const response = await fetch('http://localhost:8000/api/upload', {
          method: 'POST',
          body: formData,
        });
        
        if (!response.ok) {
          throw new Error('文件上传失败');
        }
        
        const result = await response.json();
        
        if (result.success) {
          toast.success('文件上传成功', { id: toastId });
          
          // 将文件内容添加到选项中
          options.file = {
            filename: result.filename,
            content: result.content,
            type: result.type
          };
          
          sendMessage(options);
        } else {
          throw new Error(result.message || '文件上传失败');
        }
      } catch (error) {
        console.error('文件上传错误:', error);
        toast.error(error.message || '文件上传失败', { id: toastId });
        return;
      }
    } else {
      sendMessage(options);
    }
  };

  const sendMessage = (options) => {
    onSend(message, options);
    
    // 清空输入
    setMessage('');
    setImageFile(null);
    setDocFile(null);
  };

  const handleImageSelect = (e) => {
    const file = e.target.files?.[0];
    if (file) {
      if (file.size > 10 * 1024 * 1024) { // 10MB 限制
        toast.error('图片大小不能超过 10MB');
        return;
      }
      setImageFile(file);
      toast.success('图片已选择');
    }
  };

  const handleFileSelect = (e) => {
    const file = e.target.files?.[0];
    if (file) {
      if (file.size > 50 * 1024 * 1024) { // 50MB 限制
        toast.error('文件大小不能超过 50MB');
        return;
      }
      setDocFile(file);
      toast.success('文件已选择');
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(e);
    }
  };

  return (
    <div className="border-t border-google-gray-200 bg-white p-4 sticky bottom-0">
      <form onSubmit={handleSubmit} className="max-w-4xl mx-auto">
        {/* 文件预览 */}
        {(imageFile || docFile) && (
          <div className="mb-3 flex gap-2">
            {imageFile && (
              <div className="inline-flex items-center gap-2 px-3 py-2 bg-google-blue-50 rounded-lg text-sm">
                <Image size={16} className="text-google-blue-600" />
                <span className="text-google-gray-700">{imageFile.name}</span>
                <button
                  type="button"
                  onClick={() => setImageFile(null)}
                  className="text-google-gray-500 hover:text-google-gray-700"
                >
                  ×
                </button>
              </div>
            )}
            {docFile && (
              <div className="inline-flex items-center gap-2 px-3 py-2 bg-google-blue-50 rounded-lg text-sm">
                <Paperclip size={16} className="text-google-blue-600" />
                <span className="text-google-gray-700">{docFile.name}</span>
                <button
                  type="button"
                  onClick={() => setDocFile(null)}
                  className="text-google-gray-500 hover:text-google-gray-700"
                >
                  ×
                </button>
              </div>
            )}
          </div>
        )}

        {/* 知识库和思考模式选择器 */}
        <div className="mb-2 flex items-center gap-3">
          {/* 知识库选择 */}
          <div className="flex items-center gap-2 px-3 py-2 bg-gray-50 dark:bg-gray-800 rounded-full">
            <Database size={16} className="text-gray-600 dark:text-gray-400" />
            <select
              value={selectedKnowledgeBase}
              onChange={(e) => onKnowledgeBaseChange(e.target.value)}
              disabled={loading}
              className="bg-transparent text-sm font-medium text-gray-700 dark:text-gray-300 
                       border-none outline-none cursor-pointer disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {knowledgeBases.map(kb => (
                <option key={kb.id} value={kb.id}>
                  {kb.name}
                </option>
              ))}
            </select>
          </div>

          {/* 分隔符 */}
          <div className="h-6 w-px bg-gray-300 dark:bg-gray-600"></div>

          {/* 思考模式选择器 */}
          <div className="flex gap-2">
            <button
              type="button"
              onClick={() => setThinkingMode('fast')}
              disabled={loading}
              className={`flex items-center gap-2 px-4 py-2 rounded-full text-sm font-medium transition-all
                ${thinkingMode === 'fast' 
                  ? 'bg-google-blue-600 text-white shadow-md' 
                  : 'bg-gray-100 text-gray-600 hover:bg-gray-200 dark:bg-gray-700 dark:text-gray-300'
                }
                disabled:opacity-50 disabled:cursor-not-allowed`}
            >
              <Zap size={16} />
              <span>Fast</span>
            </button>
            <button
              type="button"
              onClick={() => setThinkingMode('thinking')}
              disabled={loading}
              className={`flex items-center gap-2 px-4 py-2 rounded-full text-sm font-medium transition-all
                ${thinkingMode === 'thinking' 
                  ? 'bg-purple-600 text-white shadow-md' 
                  : 'bg-gray-100 text-gray-600 hover:bg-gray-200 dark:bg-gray-700 dark:text-gray-300'
                }
                disabled:opacity-50 disabled:cursor-not-allowed`}
            >
              <Brain size={16} />
              <span>Thinking (CoT)</span>
            </button>
          </div>
        </div>

        {/* 输入框 */}
        <div className="flex gap-3 items-end">
          <div className="flex-1 relative">
            <textarea
              value={message}
              onChange={(e) => setMessage(e.target.value)}
              onKeyDown={handleKeyDown}
              placeholder={thinkingMode === 'fast' 
                ? '向我提问任何问题...' 
                : '提出复杂问题，我会深度思考...'}
              disabled={loading}
              rows={1}
              className="w-full px-5 py-4 rounded-3xl border border-google-gray-300 
                       focus:outline-none focus:ring-2 focus:ring-google-blue-500 
                       focus:border-transparent resize-none transition-all duration-200
                       disabled:bg-google-gray-50 disabled:cursor-not-allowed
                       text-base dark:bg-gray-800 dark:border-gray-600 dark:text-white"
              style={{ minHeight: '56px', maxHeight: '200px' }}
            />
          </div>

          {/* 附件按钮 */}
          <div className="flex gap-2">
            <input
              ref={imageInputRef}
              type="file"
              accept="image/*"
              onChange={handleImageSelect}
              className="hidden"
            />
            <button
              type="button"
              onClick={() => imageInputRef.current?.click()}
              disabled={loading}
              className="btn-icon w-12 h-12 flex items-center justify-center
                       text-google-gray-600 hover:text-google-blue-600
                       disabled:opacity-50 disabled:cursor-not-allowed"
              title="上传图片"
            >
              <Image size={20} />
            </button>

            <input
              ref={fileInputRef}
              type="file"
              accept=".pdf,.docx,.txt,.md"
              onChange={handleFileSelect}
              className="hidden"
            />
            <button
              type="button"
              onClick={() => fileInputRef.current?.click()}
              disabled={loading}
              className="btn-icon w-12 h-12 flex items-center justify-center
                       text-google-gray-600 hover:text-google-blue-600
                       disabled:opacity-50 disabled:cursor-not-allowed"
              title="上传文档"
            >
              <Paperclip size={20} />
            </button>

            {/* 发送按钮 */}
            <button
              type="submit"
              disabled={loading || (!message.trim() && !imageFile && !docFile)}
              className="btn-primary w-12 h-12 flex items-center justify-center
                       disabled:opacity-50 disabled:cursor-not-allowed
                       disabled:hover:transform-none"
            >
              {loading ? (
                <Loader2 size={20} className="animate-spin" />
              ) : (
                <Send size={20} />
              )}
            </button>
          </div>
        </div>

        {/* 提示文字 */}
        <div className="mt-2 text-xs text-google-gray-500 text-center">
          按 Enter 发送，Shift + Enter 换行
          {enableSocratic && (
            <span className="ml-2 text-purple-600">🧙‍♂️ 苏格拉底模式已启用</span>
          )}
        </div>
      </form>
    </div>
  );
};

export default InputArea;


