/**
 * 知识库管理面板
 * 支持创建、切换、删除知识库，上传文件在线生成向量库，查看和删除文件
 */

import React, { useState, useEffect } from 'react';
import { 
  X, Database, Plus, Upload, Trash2, Check, Loader2, FileText, 
  AlertCircle, File, Image, ChevronDown, ChevronUp 
} from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import toast from 'react-hot-toast';

const KnowledgeBasePanel = ({ open, onClose, onSwitch }) => {
  const [knowledgeBases, setKnowledgeBases] = useState([]);
  const [loading, setLoading] = useState(false);
  const [creating, setCreating] = useState(false);
  const [uploading, setUploading] = useState(false);
  const [showCreateForm, setShowCreateForm] = useState(false);
  const [newKBName, setNewKBName] = useState('');
  const [selectedFiles, setSelectedFiles] = useState([]);
  const [currentKBId, setCurrentKBId] = useState('default');
  
  // 新增：文件列表相关状态
  const [currentKBFiles, setCurrentKBFiles] = useState([]);
  const [loadingFiles, setLoadingFiles] = useState(false);
  const [showFiles, setShowFiles] = useState(true);

  useEffect(() => {
    if (open) {
      loadKnowledgeBases();
    }
  }, [open]);

  // 当前知识库改变时，加载其文件列表
  useEffect(() => {
    if (currentKBId && open) {
      loadKBFiles(currentKBId);
    }
  }, [currentKBId, open]);

  const loadKnowledgeBases = async (preserveCurrentId = false) => {
    setLoading(true);
    try {
      const response = await fetch('http://localhost:8000/api/knowledge-bases');
      const data = await response.json();
      
      if (data.success) {
        setKnowledgeBases(data.knowledge_bases);
        // 只在初次加载时设置currentKBId，切换后不要覆盖
        if (!preserveCurrentId) {
          const current = data.knowledge_bases.find(kb => kb.is_current);
          if (current) {
            setCurrentKBId(current.id);
          }
        }
      }
    } catch (error) {
      console.error('加载知识库列表失败:', error);
      toast.error('加载知识库列表失败');
    } finally {
      setLoading(false);
    }
  };

  // 新增：加载知识库文件列表
  const loadKBFiles = async (kbId) => {
    if (!kbId) {
      console.warn('loadKBFiles: kbId为空');
      return;
    }
    
    setLoadingFiles(true);
    console.log(`加载知识库文件: ${kbId}`);
    
    try {
      const response = await fetch(
        `http://localhost:8000/api/knowledge-bases/${kbId}/files`
      );
      const data = await response.json();
      
      if (data.success) {
        console.log(`知识库 ${kbId} 包含 ${data.files.length} 个文件`);
        setCurrentKBFiles(data.files || []);
      } else {
        console.error('API返回失败:', data);
        setCurrentKBFiles([]);
      }
    } catch (error) {
      console.error(`加载文件列表失败 (${kbId}):`, error);
      setCurrentKBFiles([]);
    } finally {
      setLoadingFiles(false);
    }
  };

  const handleCreateKB = async () => {
    if (!newKBName.trim()) {
      toast.error('请输入知识库名称');
      return;
    }

    setCreating(true);
    try {
      const response = await fetch('http://localhost:8000/api/knowledge-bases', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          name: newKBName,
          files: []
        })
      });

      const data = await response.json();
      
      if (data.success) {
        toast.success(`知识库 "${newKBName}" 创建成功`);
        setNewKBName('');
        setShowCreateForm(false);
        loadKnowledgeBases();
      } else {
        throw new Error(data.detail || '创建失败');
      }
    } catch (error) {
      console.error('创建知识库失败:', error);
      toast.error(error.message || '创建知识库失败');
    } finally {
      setCreating(false);
    }
  };

  const handleSwitchKB = async (kbId) => {
    try {
      const response = await fetch(
        `http://localhost:8000/api/knowledge-bases/${kbId}/switch`, 
        { method: 'POST' }
      );

      const data = await response.json();
      
      if (data.success) {
        setCurrentKBId(kbId);  // 先更新本地状态
        toast.success(`已切换到: ${kbId === 'default' ? '默认知识库' : kbId}`);
        if (onSwitch) {
          onSwitch(kbId);
        }
        // 重新加载知识库列表，但保留当前选中的ID
        loadKnowledgeBases(true);
      } else {
        throw new Error(data.detail || '切换失败');
      }
    } catch (error) {
      console.error('切换知识库失败:', error);
      toast.error('切换知识库失败');
    }
  };

  const handleDeleteKB = async (kbId, kbName) => {
    if (kbId === 'default') {
      toast.error('不能删除默认知识库');
      return;
    }

    if (!confirm(`确定要删除知识库 "${kbName}" 吗？此操作不可恢复。`)) {
      return;
    }

    try {
      const response = await fetch(
        `http://localhost:8000/api/knowledge-bases/${kbId}`,
        { method: 'DELETE' }
      );

      const data = await response.json();
      
      if (data.success) {
        toast.success(`知识库 "${kbName}" 已删除`);
        if (currentKBId === kbId) {
          setCurrentKBId('default');
          handleSwitchKB('default');
        }
        loadKnowledgeBases();
      } else {
        throw new Error(data.detail || '删除失败');
      }
    } catch (error) {
      console.error('删除知识库失败:', error);
      toast.error('删除知识库失败');
    }
  };

  // 新增：删除文件
  const handleDeleteFile = async (filename) => {
    if (!confirm(`确定要删除文件 "${filename}" 吗？\n将同时删除原文件和向量记录。`)) {
      return;
    }

    try {
      const response = await fetch(
        `http://localhost:8000/api/knowledge-bases/${currentKBId}/files/${encodeURIComponent(filename)}`,
        { method: 'DELETE' }
      );

      const data = await response.json();
      
      if (data.success) {
        toast.success(`文件 "${filename}" 已删除`);
        loadKBFiles(currentKBId);  // 重新加载文件列表
      } else {
        throw new Error(data.detail || '删除失败');
      }
    } catch (error) {
      console.error('删除文件失败:', error);
      toast.error('删除文件失败');
    }
  };

  const handleFileSelect = (event) => {
    const files = Array.from(event.target.files);
    setSelectedFiles(files);
  };

  const handleUploadFiles = async (kbId) => {
    if (selectedFiles.length === 0) {
      toast.error('请选择要上传的文件');
      return;
    }

    setUploading(true);
    const toastId = toast.loading(`正在处理 ${selectedFiles.length} 个文件...`);

    try {
      const formData = new FormData();
      selectedFiles.forEach(file => {
        formData.append('files', file);
      });

      const response = await fetch(
        `http://localhost:8000/api/knowledge-bases/${kbId}/upload`,
        {
          method: 'POST',
          body: formData
        }
      );

      const data = await response.json();
      
      if (data.success) {
        toast.success(
          `成功！文档: ${data.documents_added}, 图片: ${data.images_added}`,
          { id: toastId }
        );
        setSelectedFiles([]);
        loadKnowledgeBases(true);  // 保持当前选中的知识库
        loadKBFiles(kbId);  // 重新加载文件列表
      } else {
        throw new Error(data.detail || '上传失败');
      }
    } catch (error) {
      console.error('上传文件失败:', error);
      toast.error(error.message || '上传文件失败', { id: toastId });
    } finally {
      setUploading(false);
    }
  };

  // 获取文件类型图标
  const getFileIcon = (type) => {
    if (['pdf'].includes(type)) return <FileText size={14} className="text-red-600" />;
    if (['jpg', 'jpeg', 'png', 'gif', 'webp', 'bmp'].includes(type)) 
      return <Image size={14} className="text-green-600" />;
    if (['txt', 'md'].includes(type)) return <FileText size={14} className="text-blue-600" />;
    if (['docx'].includes(type)) return <FileText size={14} className="text-indigo-600" />;
    if (['pptx'].includes(type)) return <FileText size={14} className="text-orange-600" />;
    return <File size={14} className="text-google-gray-400" />;
  };

  return (
    <AnimatePresence>
      {open && (
        <>
          {/* 面板主体 - 紧贴Sidebar，无遮罩 */}
          <motion.div
            initial={{ width: 0, opacity: 0 }}
            animate={{ width: 400, opacity: 1 }}
            exit={{ width: 0, opacity: 0 }}
            transition={{ type: 'spring', damping: 30, stiffness: 300 }}
            className="fixed left-[280px] top-0 bottom-0 bg-white shadow-lg z-20
                     border-r border-google-gray-200 flex flex-col"
          >
            {/* 头部 */}
            <div className="flex-shrink-0 bg-white border-b border-google-gray-200 p-4">
              <div className="flex items-center justify-between mb-4">
                <div className="flex items-center gap-3">
                  <Database size={24} className="text-google-blue-600" />
                  <h2 className="text-xl font-semibold text-google-gray-900">知识库管理</h2>
                </div>
                <button
                  onClick={onClose}
                  className="btn-icon p-2 hover:bg-google-gray-100 rounded-lg"
                >
                  <X size={20} />
                </button>
              </div>

              <button
                onClick={() => setShowCreateForm(!showCreateForm)}
                className="w-full btn-primary flex items-center justify-center gap-2 py-2.5"
              >
                <Plus size={18} />
                创建新知识库
              </button>
            </div>

            {/* 内容区 - 可滚动 */}
            <div className="flex-1 overflow-y-auto p-6 space-y-6">
              {/* 创建表单 */}
              <AnimatePresence>
                {showCreateForm && (
                  <motion.div
                    initial={{ opacity: 0, height: 0 }}
                    animate={{ opacity: 1, height: 'auto' }}
                    exit={{ opacity: 0, height: 0 }}
                    className="bg-google-blue-50 border border-google-blue-200 rounded-xl p-4"
                  >
                    <h3 className="text-sm font-semibold text-google-gray-900 mb-3">
                      新建知识库
                    </h3>
                    <input
                      type="text"
                      value={newKBName}
                      onChange={(e) => setNewKBName(e.target.value)}
                      placeholder="输入知识库名称（如：物理课程、编程资料）"
                      className="w-full px-3 py-2 rounded-lg border border-google-gray-300 
                               focus:outline-none focus:ring-2 focus:ring-google-blue-500 mb-3"
                    />
                    <div className="flex gap-2">
                      <button
                        onClick={handleCreateKB}
                        disabled={creating || !newKBName.trim()}
                        className="flex-1 bg-google-blue-600 text-white py-2 rounded-lg 
                                 hover:bg-google-blue-700 disabled:opacity-50 disabled:cursor-not-allowed
                                 flex items-center justify-center gap-2"
                      >
                        {creating ? (
                          <>
                            <Loader2 size={16} className="animate-spin" />
                            创建中...
                          </>
                        ) : (
                          <>
                            <Check size={16} />
                            确认创建
                          </>
                        )}
                      </button>
                      <button
                        onClick={() => setShowCreateForm(false)}
                        className="px-4 py-2 text-google-gray-600 hover:bg-google-gray-100 rounded-lg"
                      >
                        取消
                      </button>
                    </div>
                  </motion.div>
                )}
              </AnimatePresence>

              {/* 上传文件区域 */}
              <div className="bg-google-gray-50 border-2 border-dashed border-google-gray-300 
                            rounded-xl p-6">
                <h3 className="text-sm font-semibold text-google-gray-900 mb-3 flex items-center gap-2">
                  <Upload size={16} />
                  上传文件到当前知识库
                </h3>
                
                <input
                  type="file"
                  multiple
                  accept=".pdf,.docx,.txt,.md,.pptx"
                  onChange={handleFileSelect}
                  className="hidden"
                  id="file-upload"
                />
                
                <label
                  htmlFor="file-upload"
                  className="block w-full p-4 text-center border-2 border-dashed 
                           border-google-gray-300 rounded-lg cursor-pointer
                           hover:border-google-blue-400 hover:bg-google-blue-50 transition-colors"
                >
                  <FileText size={32} className="mx-auto mb-2 text-google-gray-400" />
                  <p className="text-sm text-google-gray-600">
                    点击选择文件或拖拽到此处
                  </p>
                  <p className="text-xs text-google-gray-500 mt-1">
                    支持 PDF, DOCX, TXT, MD, PPTX
                  </p>
                </label>

                {selectedFiles.length > 0 && (
                  <div className="mt-3 space-y-2">
                    {selectedFiles.map((file, index) => (
                      <div key={index} className="flex items-center justify-between p-2 
                                                bg-white rounded-lg border border-google-gray-200">
                        <span className="text-sm text-google-gray-700 truncate">
                          {file.name}
                        </span>
                        <span className="text-xs text-google-gray-500">
                          {(file.size / 1024).toFixed(1)} KB
                        </span>
                      </div>
                    ))}
                    
                    <button
                      onClick={() => handleUploadFiles(currentKBId)}
                      disabled={uploading}
                      className="w-full mt-2 bg-google-blue-600 text-white py-2 rounded-lg 
                               hover:bg-google-blue-700 disabled:opacity-50 disabled:cursor-not-allowed
                               flex items-center justify-center gap-2"
                    >
                      {uploading ? (
                        <>
                          <Loader2 size={16} className="animate-spin" />
                          处理中...
                        </>
                      ) : (
                        <>
                          <Upload size={16} />
                          上传并处理 ({selectedFiles.length} 个文件)
                        </>
                      )}
                    </button>
                  </div>
                )}
              </div>

              {/* 知识库列表 */}
              {loading ? (
                <div className="flex items-center justify-center py-8">
                  <Loader2 className="animate-spin text-google-blue-600" size={32} />
                </div>
              ) : knowledgeBases.length > 0 ? (
                <div>
                  <h3 className="text-sm font-semibold text-google-gray-900 mb-3">
                    已有知识库 ({knowledgeBases.length})
                  </h3>
                  <div className="space-y-2">
                    {knowledgeBases.map((kb) => (
                      <div
                        key={kb.id}
                        className={`p-4 rounded-xl border-2 transition-all ${
                          kb.id === currentKBId
                            ? 'border-google-blue-500 bg-google-blue-50 shadow-sm'
                            : 'border-google-gray-200 hover:border-google-gray-300'
                        }`}
                      >
                        <div className="flex items-start justify-between">
                          <div className="flex-1">
                            <div className="flex items-center gap-2 mb-1">
                              <h4 className="text-sm font-semibold text-google-gray-900">
                                {kb.name}
                              </h4>
                              {kb.id === currentKBId && (
                                <span className="px-2 py-0.5 bg-google-blue-600 text-white 
                                               text-xs rounded-full">
                                  当前
                                </span>
                              )}
                            </div>
                            <p className="text-xs text-google-gray-600">
                              大小: {kb.size} MB
                            </p>
                          </div>

                          <div className="flex gap-1">
                            {kb.id !== currentKBId && (
                              <button
                                onClick={() => handleSwitchKB(kb.id)}
                                className="p-2 hover:bg-google-blue-100 rounded-lg 
                                         text-google-blue-600 transition-colors"
                                title="切换到此知识库"
                              >
                                <Check size={16} />
                              </button>
                            )}
                            
                            {kb.id !== 'default' && (
                              <button
                                onClick={() => handleDeleteKB(kb.id, kb.name)}
                                className="p-2 hover:bg-red-100 rounded-lg 
                                         text-red-600 transition-colors"
                                title="删除知识库"
                              >
                                <Trash2 size={16} />
                              </button>
                            )}
                          </div>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              ) : (
                <div className="text-center py-8">
                  <AlertCircle size={48} className="mx-auto mb-3 text-google-gray-300" />
                  <p className="text-google-gray-600">暂无知识库</p>
                  <p className="text-xs text-google-gray-500 mt-1">
                    点击上方按钮创建第一个知识库
                  </p>
                </div>
              )}

              {/* 当前知识库文件列表 */}
              {currentKBId && (
                <div className="border-t border-google-gray-200 pt-6">
                  <button
                    onClick={() => setShowFiles(!showFiles)}
                    className="w-full flex items-center justify-between mb-3 text-left"
                  >
                    <h3 className="text-sm font-semibold text-google-gray-900 flex items-center gap-2">
                      <FileText size={16} />
                      当前知识库文件 ({currentKBFiles.length})
                    </h3>
                    {showFiles ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
                  </button>

                  <AnimatePresence>
                    {showFiles && (
                      <motion.div
                        initial={{ opacity: 0, height: 0 }}
                        animate={{ opacity: 1, height: 'auto' }}
                        exit={{ opacity: 0, height: 0 }}
                      >
                        {loadingFiles ? (
                          <div className="flex items-center justify-center py-4">
                            <Loader2 className="animate-spin text-google-blue-600" size={20} />
                          </div>
                        ) : currentKBFiles.length > 0 ? (
                          <div className="space-y-2 max-h-96 overflow-y-auto">
                            {currentKBFiles.map((file, index) => (
                              <div
                                key={index}
                                className="flex items-center justify-between p-3 
                                         bg-white border border-google-gray-200 rounded-lg
                                         hover:border-google-blue-300 transition-colors group"
                              >
                                <div className="flex items-center gap-2 flex-1 min-w-0">
                                  {getFileIcon(file.type)}
                                  <div className="flex-1 min-w-0">
                                    <p className="text-sm text-google-gray-900 truncate">
                                      {file.name}
                                    </p>
                                    <p className="text-xs text-google-gray-500">
                                      {file.size} MB • {file.type.toUpperCase()}
                                    </p>
                                  </div>
                                </div>
                                <button
                                  onClick={() => handleDeleteFile(file.name)}
                                  className="p-2 opacity-0 group-hover:opacity-100 
                                           hover:bg-red-100 rounded-lg text-red-600 
                                           transition-all"
                                  title="删除文件"
                                >
                                  <Trash2 size={16} />
                                </button>
                              </div>
                            ))}
                          </div>
                        ) : (
                          <div className="text-center py-8 text-google-gray-500">
                            <FileText size={32} className="mx-auto mb-2 opacity-30" />
                            <p className="text-sm">此知识库暂无文件</p>
                            <p className="text-xs mt-1">上传文件后将在此显示</p>
                          </div>
                        )}
                      </motion.div>
                    )}
                  </AnimatePresence>
                </div>
              )}
            </div>
          </motion.div>
        </>
      )}
    </AnimatePresence>
  );
};

export default KnowledgeBasePanel;
