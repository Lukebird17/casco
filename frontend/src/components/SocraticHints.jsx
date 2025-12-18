/**
 * 苏格拉底模式提示组件
 * 显示线索和引导性问题
 */

import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Lightbulb, ChevronDown, ChevronUp, Sparkles } from 'lucide-react';

const SocraticHints = ({ visible, query, hints = [] }) => {
  const [expanded, setExpanded] = useState(true);
  const [displayedHints, setDisplayedHints] = useState([]);

  // 默认提示
  const defaultHints = [
    { type: 'question', text: '你知道这个概念的基本定义吗？', icon: '🤔' },
    { type: 'direction', text: '尝试在文档的前几页寻找相关说明', icon: '📖' },
    { type: 'comparison', text: '它与其他相似概念有什么区别？', icon: '🔍' },
  ];

  const activeHints = hints.length > 0 ? hints : defaultHints;

  useEffect(() => {
    if (visible) {
      // 逐步显示提示
      setDisplayedHints([]);
      activeHints.forEach((hint, index) => {
        setTimeout(() => {
          setDisplayedHints(prev => [...prev, hint]);
        }, index * 500);
      });
    }
  }, [visible, query]);

  if (!visible) return null;

  return (
    <motion.div
      initial={{ opacity: 0, y: -10 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -10 }}
      className="bg-gradient-to-r from-purple-50 to-indigo-50 border-2 border-purple-200 
                 rounded-2xl p-4 mb-4 shadow-sm"
    >
      <div className="flex items-center justify-between mb-3">
        <div className="flex items-center gap-2">
          <div className="w-8 h-8 rounded-full bg-purple-500 flex items-center justify-center">
            <Lightbulb size={18} className="text-white" />
          </div>
          <h3 className="text-sm font-semibold text-purple-900">
            🧙‍♂️ 苏格拉底模式 - 思考线索
          </h3>
        </div>
        <button
          onClick={() => setExpanded(!expanded)}
          className="p-1 hover:bg-purple-100 rounded-lg transition-colors"
        >
          {expanded ? (
            <ChevronUp size={18} className="text-purple-600" />
          ) : (
            <ChevronDown size={18} className="text-purple-600" />
          )}
        </button>
      </div>

      <AnimatePresence>
        {expanded && (
          <motion.div
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: 'auto', opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            className="space-y-2"
          >
            <p className="text-xs text-purple-700 mb-3">
              💡 我不会直接告诉你答案，但可以给你一些思考方向：
            </p>

            {displayedHints.map((hint, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: 0.1 }}
                className="flex items-start gap-2 p-2 bg-white/60 rounded-lg"
              >
                <span className="text-lg flex-shrink-0">{hint.icon}</span>
                <div className="flex-1">
                  <span className="text-sm text-purple-900">{hint.text}</span>
                  {hint.type === 'direction' && (
                    <div className="mt-1">
                      <Sparkles size={12} className="inline text-yellow-500 mr-1" />
                      <span className="text-xs text-purple-600">点击"文档查看"可以浏览相关内容</span>
                    </div>
                  )}
                </div>
              </motion.div>
            ))}

            <div className="mt-3 pt-3 border-t border-purple-200">
              <p className="text-xs text-purple-600 italic">
                "我不能给你知识，但我可以引导你自己发现它" — 苏格拉底
              </p>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </motion.div>
  );
};

export default SocraticHints;




