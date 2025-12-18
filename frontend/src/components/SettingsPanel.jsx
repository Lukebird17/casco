/**
 * 设置面板
 * 调整系统风格和功能参数
 */

import React, { useState, useEffect } from 'react';
import { X, Settings, Palette, Sliders, Save, RotateCcw } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import toast from 'react-hot-toast';
import { getSettings, saveSettings as saveSettingsUtil, resetSettings as resetSettingsUtil } from '../utils/settings';

const SettingsPanel = ({ open, onClose, darkMode, onDarkModeChange }) => {
  const [settings, setSettings] = useState({
    // 外观设置
    theme: 'light',
    fontSize: 'medium',
    compactMode: false,
    
    // 功能设置
    autoSave: true,
    showThinking: true,
    enableSocratic: false,
    retrievalK: 5,
    temperature: 0.7,
    maxTokens: 2000,
    
    // 高级设置
    enableCache: true,
    debugMode: false,
  });

  const [hasChanges, setHasChanges] = useState(false);

  // 加载设置
  useEffect(() => {
    if (open) {
      loadSettings();
    }
  }, [open]);

  const loadSettings = () => {
    const loadedSettings = getSettings();
    setSettings(loadedSettings);
  };

  const handleChange = (key, value) => {
    setSettings(prev => ({
      ...prev,
      [key]: value
    }));
    setHasChanges(true);
    
    // 立即应用dark模式变化
    if (key === 'theme' && onDarkModeChange) {
      onDarkModeChange(value === 'dark');
    }
  };

  const handleSave = () => {
    saveSettingsUtil(settings);
    toast.success('设置已保存并应用');
    setHasChanges(false);
  };

  const handleReset = () => {
    if (window.confirm('确定要重置所有设置吗？')) {
      const defaultSettings = resetSettingsUtil();
      setSettings(defaultSettings);
      toast.success('设置已重置');
      setHasChanges(false);
    }
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
            className="fixed inset-0 bg-black/30 z-40"
          />

          {/* 面板主体 */}
          <motion.div
            initial={{ x: '100%' }}
            animate={{ x: 0 }}
            exit={{ x: '100%' }}
            transition={{ type: 'spring', damping: 25 }}
            className="fixed right-0 top-0 bottom-0 w-[500px] bg-white shadow-2xl z-50 
                     overflow-y-auto"
          >
            {/* 头部 */}
            <div className="sticky top-0 bg-white border-b border-google-gray-200 p-6 flex items-center justify-between z-10">
              <div className="flex items-center gap-3">
                <Settings size={24} className="text-google-blue-600" />
                <h2 className="text-xl font-semibold text-google-gray-900">系统设置</h2>
              </div>
              <button
                onClick={onClose}
                className="btn-icon p-2 hover:bg-google-gray-100 rounded-lg"
              >
                <X size={20} />
              </button>
            </div>

            <div className="p-6 space-y-6">
              {/* 外观设置 */}
              <section>
                <div className="flex items-center gap-2 mb-4">
                  <Palette size={20} className="text-google-blue-600" />
                  <h3 className="text-lg font-semibold text-google-gray-900">外观设置</h3>
                </div>

                <div className="space-y-4">
                  {/* 主题 */}
                  <div>
                    <label className="block text-sm font-medium text-google-gray-700 mb-2">
                      主题
                    </label>
                    <div className="grid grid-cols-2 gap-2">
                      <button
                        onClick={() => handleChange('theme', 'light')}
                        className={`p-3 rounded-lg border-2 transition-colors ${
                          settings.theme === 'light'
                            ? 'border-google-blue-500 bg-google-blue-50'
                            : 'border-google-gray-200 hover:border-google-gray-300'
                        }`}
                      >
                        <div className="text-center">
                          <div className="text-2xl mb-1">☀️</div>
                          <div className="text-sm font-medium">浅色</div>
                        </div>
                      </button>
                      <button
                        onClick={() => handleChange('theme', 'dark')}
                        className={`p-3 rounded-lg border-2 transition-colors ${
                          settings.theme === 'dark'
                            ? 'border-google-blue-500 bg-google-blue-50'
                            : 'border-google-gray-200 hover:border-google-gray-300'
                        }`}
                      >
                        <div className="text-center">
                          <div className="text-2xl mb-1">🌙</div>
                          <div className="text-sm font-medium">深色</div>
                        </div>
                      </button>
                    </div>
                  </div>

                  {/* 字体大小 */}
                  <div>
                    <label className="block text-sm font-medium text-google-gray-700 mb-2">
                      字体大小
                    </label>
                    <div className="grid grid-cols-3 gap-2">
                      {['small', 'medium', 'large'].map((size) => (
                        <button
                          key={size}
                          onClick={() => handleChange('fontSize', size)}
                          className={`p-2 rounded-lg border-2 transition-colors ${
                            settings.fontSize === size
                              ? 'border-google-blue-500 bg-google-blue-50'
                              : 'border-google-gray-200 hover:border-google-gray-300'
                          }`}
                        >
                          <div className="text-sm font-medium">
                            {size === 'small' ? '小' : size === 'medium' ? '中' : '大'}
                          </div>
                        </button>
                      ))}
                    </div>
                  </div>

                  {/* 紧凑模式 */}
                  <div className="flex items-center justify-between">
                    <label className="text-sm font-medium text-google-gray-700">
                      紧凑模式
                    </label>
                    <button
                      onClick={() => handleChange('compactMode', !settings.compactMode)}
                      className={`relative inline-flex h-6 w-11 items-center rounded-full transition-colors ${
                        settings.compactMode ? 'bg-google-blue-600' : 'bg-google-gray-300'
                      }`}
                    >
                      <span
                        className={`inline-block h-4 w-4 transform rounded-full bg-white transition-transform ${
                          settings.compactMode ? 'translate-x-6' : 'translate-x-1'
                        }`}
                      />
                    </button>
                  </div>
                </div>
              </section>

              {/* 功能设置 */}
              <section>
                <div className="flex items-center gap-2 mb-4">
                  <Sliders size={20} className="text-google-blue-600" />
                  <h3 className="text-lg font-semibold text-google-gray-900">功能设置</h3>
                </div>

                <div className="space-y-4">
                  {/* 自动保存 */}
                  <div className="flex items-center justify-between">
                    <div>
                      <label className="text-sm font-medium text-google-gray-700">
                        自动保存
                      </label>
                      <p className="text-xs text-google-gray-500 mt-1">
                        自动保存对话记录
                      </p>
                    </div>
                    <button
                      onClick={() => handleChange('autoSave', !settings.autoSave)}
                      className={`relative inline-flex h-6 w-11 items-center rounded-full transition-colors ${
                        settings.autoSave ? 'bg-google-blue-600' : 'bg-google-gray-300'
                      }`}
                    >
                      <span
                        className={`inline-block h-4 w-4 transform rounded-full bg-white transition-transform ${
                          settings.autoSave ? 'translate-x-6' : 'translate-x-1'
                        }`}
                      />
                    </button>
                  </div>

                  {/* 显示思考过程 */}
                  <div className="flex items-center justify-between">
                    <div>
                      <label className="text-sm font-medium text-google-gray-700">
                        显示思考过程
                      </label>
                      <p className="text-xs text-google-gray-500 mt-1">
                        展示AI的推理步骤
                      </p>
                    </div>
                    <button
                      onClick={() => handleChange('showThinking', !settings.showThinking)}
                      className={`relative inline-flex h-6 w-11 items-center rounded-full transition-colors ${
                        settings.showThinking ? 'bg-google-blue-600' : 'bg-google-gray-300'
                      }`}
                    >
                      <span
                        className={`inline-block h-4 w-4 transform rounded-full bg-white transition-transform ${
                          settings.showThinking ? 'translate-x-6' : 'translate-x-1'
                        }`}
                      />
                    </button>
                  </div>

                  {/* 苏格拉底模式 */}
                  <div className="flex items-center justify-between">
                    <div>
                      <label className="text-sm font-medium text-google-gray-700">
                        苏格拉底模式
                      </label>
                      <p className="text-xs text-google-gray-500 mt-1">
                        通过反问引导学习
                      </p>
                    </div>
                    <button
                      onClick={() => handleChange('enableSocratic', !settings.enableSocratic)}
                      className={`relative inline-flex h-6 w-11 items-center rounded-full transition-colors ${
                        settings.enableSocratic ? 'bg-google-blue-600' : 'bg-google-gray-300'
                      }`}
                    >
                      <span
                        className={`inline-block h-4 w-4 transform rounded-full bg-white transition-transform ${
                          settings.enableSocratic ? 'translate-x-6' : 'translate-x-1'
                        }`}
                      />
                    </button>
                  </div>

                  {/* 检索数量 */}
                  <div>
                    <label className="block text-sm font-medium text-google-gray-700 mb-2">
                      检索文档数量：{settings.retrievalK}
                    </label>
                    <input
                      type="range"
                      min="1"
                      max="10"
                      value={settings.retrievalK}
                      onChange={(e) => handleChange('retrievalK', parseInt(e.target.value))}
                      className="w-full h-2 bg-google-gray-200 rounded-lg appearance-none cursor-pointer"
                    />
                    <div className="flex justify-between text-xs text-google-gray-500 mt-1">
                      <span>少 (1)</span>
                      <span>多 (10)</span>
                    </div>
                  </div>

                  {/* Temperature */}
                  <div>
                    <label className="block text-sm font-medium text-google-gray-700 mb-2">
                      回答创造性：{settings.temperature.toFixed(1)}
                    </label>
                    <input
                      type="range"
                      min="0"
                      max="1"
                      step="0.1"
                      value={settings.temperature}
                      onChange={(e) => handleChange('temperature', parseFloat(e.target.value))}
                      className="w-full h-2 bg-google-gray-200 rounded-lg appearance-none cursor-pointer"
                    />
                    <div className="flex justify-between text-xs text-google-gray-500 mt-1">
                      <span>保守 (0.0)</span>
                      <span>创新 (1.0)</span>
                    </div>
                  </div>

                  {/* Max Tokens */}
                  <div>
                    <label className="block text-sm font-medium text-google-gray-700 mb-2">
                      最大回答长度：{settings.maxTokens}
                    </label>
                    <input
                      type="range"
                      min="500"
                      max="4000"
                      step="100"
                      value={settings.maxTokens}
                      onChange={(e) => handleChange('maxTokens', parseInt(e.target.value))}
                      className="w-full h-2 bg-google-gray-200 rounded-lg appearance-none cursor-pointer"
                    />
                    <div className="flex justify-between text-xs text-google-gray-500 mt-1">
                      <span>简短 (500)</span>
                      <span>详细 (4000)</span>
                    </div>
                  </div>
                </div>
              </section>

              {/* 高级设置 */}
              <section>
                <div className="flex items-center gap-2 mb-4">
                  <Settings size={20} className="text-google-blue-600" />
                  <h3 className="text-lg font-semibold text-google-gray-900">高级设置</h3>
                </div>

                <div className="space-y-4">
                  {/* 启用缓存 */}
                  <div className="flex items-center justify-between">
                    <div>
                      <label className="text-sm font-medium text-google-gray-700">
                        启用缓存
                      </label>
                      <p className="text-xs text-google-gray-500 mt-1">
                        缓存检索结果以提升速度
                      </p>
                    </div>
                    <button
                      onClick={() => handleChange('enableCache', !settings.enableCache)}
                      className={`relative inline-flex h-6 w-11 items-center rounded-full transition-colors ${
                        settings.enableCache ? 'bg-google-blue-600' : 'bg-google-gray-300'
                      }`}
                    >
                      <span
                        className={`inline-block h-4 w-4 transform rounded-full bg-white transition-transform ${
                          settings.enableCache ? 'translate-x-6' : 'translate-x-1'
                        }`}
                      />
                    </button>
                  </div>

                  {/* 调试模式 */}
                  <div className="flex items-center justify-between">
                    <div>
                      <label className="text-sm font-medium text-google-gray-700">
                        调试模式
                      </label>
                      <p className="text-xs text-google-gray-500 mt-1">
                        显示详细的调试信息
                      </p>
                    </div>
                    <button
                      onClick={() => handleChange('debugMode', !settings.debugMode)}
                      className={`relative inline-flex h-6 w-11 items-center rounded-full transition-colors ${
                        settings.debugMode ? 'bg-google-blue-600' : 'bg-google-gray-300'
                      }`}
                    >
                      <span
                        className={`inline-block h-4 w-4 transform rounded-full bg-white transition-transform ${
                          settings.debugMode ? 'translate-x-6' : 'translate-x-1'
                        }`}
                      />
                    </button>
                  </div>
                </div>
              </section>

              {/* 底部按钮 */}
              <div className="flex gap-3 pt-4 border-t border-google-gray-200">
                <button
                  onClick={handleReset}
                  className="flex-1 btn-secondary flex items-center justify-center gap-2"
                >
                  <RotateCcw size={16} />
                  重置
                </button>
                <button
                  onClick={handleSave}
                  disabled={!hasChanges}
                  className={`flex-1 flex items-center justify-center gap-2 ${
                    hasChanges
                      ? 'btn-primary'
                      : 'bg-google-gray-200 text-google-gray-400 cursor-not-allowed'
                  }`}
                >
                  <Save size={16} />
                  保存设置
                </button>
              </div>
            </div>
          </motion.div>
        </>
      )}
    </AnimatePresence>
  );
};

export default SettingsPanel;

