/**
 * 新会话引导界面
 * 在新建会话时显示，让用户配置助教性格和风格
 */

import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { 
  Sparkles, 
  GraduationCap, 
  Heart, 
  Zap, 
  BookOpen,
  Target,
  MessageCircle,
  Settings,
  ChevronRight
} from 'lucide-react';

const WelcomeGuide = ({ onComplete }) => {
  const [step, setStep] = useState(1);
  const [config, setConfig] = useState({
    personality: 'professional', // professional, friendly, patient, strict
    language: 'formal',           // formal, casual, concise
    teachingStyle: 'socratic',    // socratic, direct, guided
    responseLength: 'balanced'    // concise, balanced, detailed
  });

  // 性格选项
  const personalities = [
    {
      id: 'professional',
      icon: GraduationCap,
      name: '专业严谨',
      desc: '准确、客观、学术化的表达',
      prompt: '你是一位专业、严谨的学术助教，注重准确性和学术规范。'
    },
    {
      id: 'friendly',
      icon: Heart,
      name: '友善耐心',
      desc: '温和、鼓励、易于理解',
      prompt: '你是一位友善、耐心的助教，善于用通俗易懂的方式解释复杂概念。'
    },
    {
      id: 'energetic',
      icon: Zap,
      name: '活力激励',
      desc: '积极、充满热情、激发兴趣',
      prompt: '你是一位充满活力的助教，善于用生动有趣的方式激发学生的学习兴趣。'
    },
    {
      id: 'patient',
      icon: BookOpen,
      name: '循序渐进',
      desc: '从基础开始，逐步深入',
      prompt: '你是一位循序渐进的助教，善于从基础概念开始，逐步引导学生深入理解。'
    }
  ];

  // 教学风格选项
  const teachingStyles = [
    {
      id: 'socratic',
      icon: MessageCircle,
      name: '苏格拉底式',
      desc: '通过提问引导思考',
      prompt: '采用苏格拉底式教学法，通过提问引导学生自主思考和发现答案。'
    },
    {
      id: 'direct',
      icon: Target,
      name: '直接讲解',
      desc: '清晰、直接地给出答案',
      prompt: '直接清晰地讲解知识点，提供明确的答案和解释。'
    },
    {
      id: 'guided',
      icon: ChevronRight,
      name: '引导式',
      desc: '提示方向，鼓励探索',
      prompt: '提供必要的提示和方向，鼓励学生自己探索和实践。'
    }
  ];

  // 语言风格选项
  const languageStyles = [
    { id: 'formal', name: '正式学术', desc: '使用标准学术语言' },
    { id: 'casual', name: '轻松对话', desc: '使用口语化表达' },
    { id: 'concise', name: '简洁精炼', desc: '言简意赅，直击要点' }
  ];

  // 回答长度选项
  const responseLengths = [
    { id: 'concise', name: '简洁', desc: '核心要点，快速回答' },
    { id: 'balanced', name: '适中', desc: '平衡详细度和简洁性' },
    { id: 'detailed', name: '详尽', desc: '深入展开，全面讲解' }
  ];

  const generateSystemPrompt = () => {
    const personality = personalities.find(p => p.id === config.personality);
    const teaching = teachingStyles.find(t => t.id === config.teachingStyle);
    
    const languageGuide = {
      formal: '使用正式的学术语言，保持专业性。',
      casual: '使用轻松的对话方式，让学生感到亲切。',
      concise: '表达简洁精炼，避免冗余。'
    };
    
    const lengthGuide = {
      concise: '回答要简明扼要，突出核心要点。',
      balanced: '在详细程度和简洁性之间取得平衡。',
      detailed: '提供详尽的解释和丰富的例子。'
    };

    return `${personality.prompt}\n\n${teaching.prompt}\n\n${languageGuide[config.language]}\n\n${lengthGuide[config.responseLength]}`;
  };

  const handleComplete = () => {
    const systemPrompt = generateSystemPrompt();
    onComplete({
      ...config,
      systemPrompt
    });
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: -20 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -20 }}
      className="w-full bg-white rounded-2xl shadow-xl p-8 mb-6"
    >
      <motion.div
        initial={{ scale: 0.95 }}
        animate={{ scale: 1 }}
      >
        {/* 头部 */}
        <div className="text-center mb-6">
          <div className="inline-flex items-center justify-center w-12 h-12 bg-gradient-to-br from-blue-500 to-indigo-600 rounded-full mb-3">
            <Sparkles className="w-6 h-6 text-white" />
          </div>
          <h1 className="text-2xl font-bold text-gray-900 mb-1">
            欢迎使用 RAG 智能助教
          </h1>
          <p className="text-sm text-gray-600">
            让我们先设置一下助教的风格，为你提供最佳的学习体验
          </p>
        </div>

        {/* 步骤指示器 */}
        <div className="flex justify-center mb-6">
          {[1, 2, 3, 4].map((s) => (
            <div key={s} className="flex items-center">
              <div
                className={`w-8 h-8 rounded-full flex items-center justify-center text-sm font-semibold
                  ${step >= s 
                    ? 'bg-blue-600 text-white' 
                    : 'bg-gray-200 text-gray-400'
                  }`}
              >
                {s}
              </div>
              {s < 4 && (
                <div
                  className={`w-12 h-1 mx-1 ${
                    step > s ? 'bg-blue-600' : 'bg-gray-200'
                  }`}
                />
              )}
            </div>
          ))}
        </div>

        {/* 配置内容 */}
        <div className="min-h-[320px]">
          {/* 步骤1：选择性格 */}
          {step === 1 && (
            <motion.div
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
            >
              <h2 className="text-xl font-semibold text-gray-900 mb-3">
                选择助教性格
              </h2>
              <p className="text-sm text-gray-600 mb-4">
                不同的性格会影响助教的回答方式和语气
              </p>
              <div className="grid grid-cols-2 gap-3">
                {personalities.map((p) => (
                  <motion.button
                    key={p.id}
                    whileHover={{ scale: 1.02 }}
                    whileTap={{ scale: 0.98 }}
                    onClick={() => setConfig({ ...config, personality: p.id })}
                    className={`p-4 rounded-xl border-2 text-left transition-all ${
                      config.personality === p.id
                        ? 'border-blue-600 bg-blue-50 shadow-md'
                        : 'border-gray-200 hover:border-gray-300'
                    }`}
                  >
                    <p.icon
                      className={`w-10 h-10 mb-2 ${
                        config.personality === p.id
                          ? 'text-blue-600'
                          : 'text-gray-400'
                      }`}
                    />
                    <h3 className="font-semibold mb-1">{p.name}</h3>
                    <p className="text-xs text-gray-600">{p.desc}</p>
                  </motion.button>
                ))}
              </div>
            </motion.div>
          )}

          {/* 步骤2：选择教学风格 */}
          {step === 2 && (
            <motion.div
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
            >
              <h2 className="text-xl font-semibold text-gray-900 mb-3">
                选择教学风格
              </h2>
              <p className="text-sm text-gray-600 mb-4">
                选择最适合你的学习方式
              </p>
              <div className="space-y-3">
                {teachingStyles.map((t) => (
                  <motion.button
                    key={t.id}
                    whileHover={{ scale: 1.01 }}
                    whileTap={{ scale: 0.99 }}
                    onClick={() => setConfig({ ...config, teachingStyle: t.id })}
                    className={`w-full p-4 rounded-xl border-2 text-left flex items-start gap-3 transition-all ${
                      config.teachingStyle === t.id
                        ? 'border-blue-600 bg-blue-50 shadow-md'
                        : 'border-gray-200 hover:border-gray-300'
                    }`}
                  >
                    <t.icon
                      className={`w-8 h-8 flex-shrink-0 ${
                        config.teachingStyle === t.id
                          ? 'text-blue-600'
                          : 'text-gray-400'
                      }`}
                    />
                    <div>
                      <h3 className="font-semibold mb-1">{t.name}</h3>
                      <p className="text-xs text-gray-600">{t.desc}</p>
                    </div>
                  </motion.button>
                ))}
              </div>
            </motion.div>
          )}

          {/* 步骤3：语言风格 */}
          {step === 3 && (
            <motion.div
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
            >
              <h2 className="text-xl font-semibold text-gray-900 mb-3">
                语言风格偏好
              </h2>
              <p className="text-sm text-gray-600 mb-4">
                选择你喜欢的语言表达方式
              </p>
              <div className="space-y-2">
                {languageStyles.map((l) => (
                  <button
                    key={l.id}
                    onClick={() => setConfig({ ...config, language: l.id })}
                    className={`w-full p-3 rounded-lg border-2 text-left transition-all ${
                      config.language === l.id
                        ? 'border-blue-600 bg-blue-50'
                        : 'border-gray-200 hover:border-gray-300'
                    }`}
                  >
                    <div className="flex items-center justify-between">
                      <div>
                        <h3 className="font-semibold text-sm">{l.name}</h3>
                        <p className="text-xs text-gray-600">{l.desc}</p>
                      </div>
                      {config.language === l.id && (
                        <div className="w-5 h-5 bg-blue-600 rounded-full flex items-center justify-center">
                          <svg className="w-3 h-3 text-white" fill="currentColor" viewBox="0 0 20 20">
                            <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                          </svg>
                        </div>
                      )}
                    </div>
                  </button>
                ))}
              </div>
            </motion.div>
          )}

          {/* 步骤4：回答长度 */}
          {step === 4 && (
            <motion.div
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
            >
              <h2 className="text-xl font-semibold text-gray-900 mb-3">
                回答详细程度
              </h2>
              <p className="text-sm text-gray-600 mb-4">
                根据你的偏好调整回答的详细程度
              </p>
              <div className="space-y-2">
                {responseLengths.map((r) => (
                  <button
                    key={r.id}
                    onClick={() => setConfig({ ...config, responseLength: r.id })}
                    className={`w-full p-3 rounded-lg border-2 text-left transition-all ${
                      config.responseLength === r.id
                        ? 'border-blue-600 bg-blue-50'
                        : 'border-gray-200 hover:border-gray-300'
                    }`}
                  >
                    <div className="flex items-center justify-between">
                      <div>
                        <h3 className="font-semibold text-sm">{r.name}</h3>
                        <p className="text-xs text-gray-600">{r.desc}</p>
                      </div>
                      {config.responseLength === r.id && (
                        <div className="w-5 h-5 bg-blue-600 rounded-full flex items-center justify-center">
                          <svg className="w-3 h-3 text-white" fill="currentColor" viewBox="0 0 20 20">
                            <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                          </svg>
                        </div>
                      )}
                    </div>
                  </button>
                ))}
              </div>

              {/* 预览 */}
              <div className="mt-4 p-3 bg-gray-50 rounded-lg">
                <h4 className="text-xs font-semibold text-gray-700 mb-1">
                  系统提示词预览：
                </h4>
                <p className="text-xs text-gray-600 whitespace-pre-line line-clamp-4">
                  {generateSystemPrompt()}
                </p>
              </div>
            </motion.div>
          )}
        </div>

        {/* 底部按钮 */}
        <div className="flex justify-between mt-6 pt-6 border-t border-gray-200">
          <button
            onClick={() => setStep(Math.max(1, step - 1))}
            disabled={step === 1}
            className={`px-5 py-2 rounded-lg font-medium transition-all ${
              step === 1
                ? 'text-gray-400 cursor-not-allowed'
                : 'text-gray-700 hover:bg-gray-100'
            }`}
          >
            上一步
          </button>

          {step < 4 ? (
            <button
              onClick={() => setStep(step + 1)}
              className="px-6 py-2 bg-gradient-to-r from-blue-600 to-indigo-600 text-white rounded-lg font-medium hover:shadow-lg transition-all"
            >
              下一步
            </button>
          ) : (
            <button
              onClick={handleComplete}
              className="px-6 py-2 bg-gradient-to-r from-green-600 to-emerald-600 text-white rounded-lg font-medium hover:shadow-lg transition-all flex items-center gap-2"
            >
              <span>开始使用</span>
              <ChevronRight size={18} />
            </button>
          )}
        </div>
      </motion.div>
    </motion.div>
  );

};

export default WelcomeGuide;
