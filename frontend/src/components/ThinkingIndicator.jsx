/**
 * 思考指示器组件
 * 显示 AI 正在思考的动画
 */

import React from 'react';
import { motion } from 'framer-motion';
import { Brain, Search, Sparkles } from 'lucide-react';

const ThinkingIndicator = () => {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0 }}
      className="flex justify-start mb-4"
    >
      <div className="flex gap-3 max-w-[85%]">
        {/* 头像 */}
        <div className="flex-shrink-0 w-8 h-8 rounded-full bg-google-gray-700 flex items-center justify-center">
          <motion.div
            animate={{ rotate: 360 }}
            transition={{ duration: 2, repeat: Infinity, ease: "linear" }}
          >
            <Brain size={18} className="text-white" />
          </motion.div>
        </div>

        {/* 思考内容 */}
        <div className="message-bubble message-assistant">
          <div className="flex items-center gap-3">
            <motion.div
              animate={{ opacity: [0.5, 1, 0.5] }}
              transition={{ duration: 1.5, repeat: Infinity }}
              className="flex items-center gap-2 text-google-gray-600"
            >
              <Search size={16} />
              <span className="text-sm">正在检索相关文档...</span>
            </motion.div>
          </div>
          
          <div className="flex items-center gap-2 mt-2">
            <motion.div
              animate={{ scale: [1, 1.2, 1] }}
              transition={{ duration: 0.8, repeat: Infinity }}
            >
              <Sparkles size={14} className="text-google-blue-500" />
            </motion.div>
            <motion.div
              animate={{ scale: [1, 1.2, 1] }}
              transition={{ duration: 0.8, repeat: Infinity, delay: 0.2 }}
            >
              <Sparkles size={14} className="text-google-blue-500" />
            </motion.div>
            <motion.div
              animate={{ scale: [1, 1.2, 1] }}
              transition={{ duration: 0.8, repeat: Infinity, delay: 0.4 }}
            >
              <Sparkles size={14} className="text-google-blue-500" />
            </motion.div>
          </div>
        </div>
      </div>
    </motion.div>
  );
};

export default ThinkingIndicator;


