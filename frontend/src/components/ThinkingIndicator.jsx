/**
 * 思考指示器组件
 * 显示 AI 正在思考的动画和推理过程
 */

import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Brain, Search, Sparkles, FileText, Zap, Check } from 'lucide-react';

const ThinkingIndicator = ({ reasoningSteps = [] }) => {
  const [currentStep, setCurrentStep] = useState(0);
  const [displayedSteps, setDisplayedSteps] = useState([]);

  // 模拟推理步骤（如果后端没有提供）
  const defaultSteps = [
    { icon: Search, text: '正在分析问题类型...', type: 'analyze' },
    { icon: FileText, text: '正在检索知识库...', type: 'retrieve' },
    { icon: Sparkles, text: '找到 3 个相关文档片段', type: 'found' },
    { icon: Brain, text: '正在整合信息并生成回答...', type: 'generate' },
  ];

  const steps = reasoningSteps.length > 0 ? reasoningSteps : defaultSteps;

  useEffect(() => {
    if (currentStep < steps.length) {
      const timer = setTimeout(() => {
        setDisplayedSteps(prev => [...prev, steps[currentStep]]);
        setCurrentStep(prev => prev + 1);
      }, 800);
      return () => clearTimeout(timer);
    }
  }, [currentStep, steps]);

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
          <div className="space-y-2">
            <AnimatePresence>
              {displayedSteps.map((step, index) => {
                const Icon = step.icon || Search;
                const isCompleted = index < displayedSteps.length - 1;
                const isCurrent = index === displayedSteps.length - 1;

                return (
                  <motion.div
                    key={index}
                    initial={{ opacity: 0, x: -10 }}
                    animate={{ opacity: 1, x: 0 }}
                    exit={{ opacity: 0 }}
                    transition={{ duration: 0.3 }}
                    className="flex items-center gap-2"
                  >
                    {isCompleted ? (
                      <Check size={16} className="text-green-500 flex-shrink-0" />
                    ) : (
                      <motion.div
                        animate={isCurrent ? { opacity: [0.5, 1, 0.5] } : {}}
                        transition={{ duration: 1.5, repeat: Infinity }}
                      >
                        <Icon size={16} className={`${
                          step.type === 'found' ? 'text-google-blue-600' :
                          step.type === 'generate' ? 'text-purple-600' :
                          'text-google-gray-600'
                        } flex-shrink-0`} />
                      </motion.div>
                    )}
                    <span className={`text-sm ${
                      isCompleted ? 'text-google-gray-500' : 'text-google-gray-700'
                    }`}>
                      {step.text}
                    </span>
                    {step.type === 'found' && isCurrent && (
                      <motion.div
                        initial={{ scale: 0 }}
                        animate={{ scale: 1 }}
                        className="ml-auto"
                      >
                        <Zap size={14} className="text-yellow-500" />
                      </motion.div>
                    )}
                  </motion.div>
                );
              })}
            </AnimatePresence>

            {/* 闪烁动画（仅在最后一步） */}
            {currentStep >= steps.length && (
              <div className="flex items-center gap-2 mt-3 pt-3 border-t border-google-gray-200">
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
            )}
          </div>
        </div>
      </div>
    </motion.div>
  );
};

export default ThinkingIndicator;


