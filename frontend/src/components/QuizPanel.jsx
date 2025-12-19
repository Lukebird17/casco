/**
 * 智能测验面板
 */

import React, { useState } from 'react';
import { X, Award, CheckCircle, XCircle, Loader2 } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import toast from 'react-hot-toast';
import axios from 'axios';

const QuizPanel = ({ open, onClose }) => {
  const [quizMode, setQuizMode] = useState('setup'); // setup, quiz, result
  const [numQuestions, setNumQuestions] = useState(5);
  const [difficulty, setDifficulty] = useState('medium');
  const [questions, setQuestions] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [userAnswers, setUserAnswers] = useState({});
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  // 生成测验
  const generateQuiz = async () => {
    setLoading(true);
    try {
      // 这里应该从当前会话的上下文生成
      const context = "基于操作系统课程内容..."; // 简化示例
      
      const response = await axios.post('http://localhost:8000/api/quiz/generate', {
        context,
        num_questions: numQuestions,
        difficulty
      });

      if (response.data.success) {
        setQuestions(response.data.questions);
        setQuizMode('quiz');
        setCurrentIndex(0);
        toast.success('测验已生成');
      }
    } catch (error) {
      console.error('生成测验失败:', error);
      toast.error('生成测验失败');
    } finally {
      setLoading(false);
    }
  };

  // 提交答案
  const handleSubmit = async () => {
    setLoading(true);
    const newResults = [];

    for (let i = 0; i < questions.length; i++) {
      const question = questions[i];
      const userAnswer = userAnswers[i] || '';

      try {
        const response = await axios.post('http://localhost:8000/api/quiz/grade', {
          question,
          user_answer: userAnswer
        });

        if (response.data.success) {
          newResults.push({
            question,
            userAnswer,
            ...response.data
          });
        }
      } catch (error) {
        console.error('评分失败:', error);
        newResults.push({
          question,
          userAnswer,
          is_correct: false,
          feedback: '评分失败'
        });
      }
    }

    setResults(newResults);
    setQuizMode('result');
    setLoading(false);
  };

  // 重置
  const handleReset = () => {
    setQuizMode('setup');
    setQuestions([]);
    setUserAnswers({});
    setResults([]);
    setCurrentIndex(0);
  };

  const currentQuestion = questions[currentIndex];
  const score = results.reduce((sum, r) => sum + (r.is_correct ? 1 : 0), 0);
  const totalQuestions = results.length;

  return (
    <AnimatePresence>
      {open && (
        <motion.div
          initial={{ width: 0, opacity: 0 }}
          animate={{ width: 500, opacity: 1 }}
          exit={{ width: 0, opacity: 0 }}
          transition={{ type: 'spring', damping: 30, stiffness: 300 }}
          className="fixed left-[280px] top-0 bottom-0 bg-white border-r 
                   border-google-gray-200 shadow-lg z-20 flex flex-col"
        >
          {/* 头部 */}
          <div className="flex-shrink-0 bg-white border-b border-google-gray-200 p-4">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-2">
                <Award size={20} className="text-google-blue-600" />
                <h2 className="font-semibold text-google-gray-900">智能测验</h2>
              </div>
              <button
                onClick={onClose}
                className="btn-icon p-2 hover:bg-google-gray-100 rounded-lg"
              >
                <X size={20} />
              </button>
            </div>
          </div>

          {/* 内容区域 */}
          <div className="flex-1 overflow-y-auto p-4">
            {/* 设置模式 */}
            {quizMode === 'setup' && (
              <div className="space-y-4">
                <div>
                  <label className="block text-sm font-medium text-google-gray-700 mb-2">
                    题目数量
                  </label>
                  <select
                    value={numQuestions}
                    onChange={(e) => setNumQuestions(parseInt(e.target.value))}
                    className="w-full px-3 py-2 border border-google-gray-300 rounded-lg
                             focus:outline-none focus:ring-2 focus:ring-google-blue-500"
                  >
                    <option value={3}>3 题</option>
                    <option value={5}>5 题</option>
                    <option value={10}>10 题</option>
                  </select>
                </div>

                <div>
                  <label className="block text-sm font-medium text-google-gray-700 mb-2">
                    难度
                  </label>
                  <div className="grid grid-cols-3 gap-2">
                    {['easy', 'medium', 'hard'].map(level => (
                      <button
                        key={level}
                        onClick={() => setDifficulty(level)}
                        className={`py-2 px-4 rounded-lg border transition-colors ${
                          difficulty === level
                            ? 'bg-google-blue-500 text-white border-google-blue-500'
                            : 'bg-white text-google-gray-700 border-google-gray-300 hover:border-google-blue-300'
                        }`}
                      >
                        {level === 'easy' ? '简单' : level === 'medium' ? '中等' : '困难'}
                      </button>
                    ))}
                  </div>
                </div>

                <button
                  onClick={generateQuiz}
                  disabled={loading}
                  className="w-full btn-primary py-3 flex items-center justify-center gap-2"
                >
                  {loading ? (
                    <>
                      <Loader2 size={20} className="animate-spin" />
                      生成中...
                    </>
                  ) : (
                    '开始测验'
                  )}
                </button>
              </div>
            )}

            {/* 测验模式 */}
            {quizMode === 'quiz' && currentQuestion && (
              <div className="space-y-4">
                {/* 进度 */}
                <div className="flex items-center justify-between text-sm text-google-gray-600">
                  <span>第 {currentIndex + 1} / {questions.length} 题</span>
                  <span>{Math.round(((currentIndex + 1) / questions.length) * 100)}%</span>
                </div>

                {/* 题目 */}
                <div className="bg-google-gray-50 rounded-lg p-4">
                  <div className="text-sm text-google-blue-600 mb-2">
                    {currentQuestion.type === 'choice' ? '选择题' : 
                     currentQuestion.type === 'true_false' ? '判断题' : '简答题'}
                  </div>
                  <p className="text-google-gray-900 font-medium">
                    {currentQuestion.question}
                  </p>
                </div>

                {/* 答案选项 */}
                {currentQuestion.type === 'choice' && (
                  <div className="space-y-2">
                    {currentQuestion.options.map((option, idx) => (
                      <button
                        key={idx}
                        onClick={() => setUserAnswers({...userAnswers, [currentIndex]: option[0]})}
                        className={`w-full text-left p-3 rounded-lg border transition-colors ${
                          userAnswers[currentIndex] === option[0]
                            ? 'bg-google-blue-50 border-google-blue-500'
                            : 'bg-white border-google-gray-300 hover:border-google-blue-300'
                        }`}
                      >
                        {option}
                      </button>
                    ))}
                  </div>
                )}

                {currentQuestion.type === 'true_false' && (
                  <div className="grid grid-cols-2 gap-3">
                    <button
                      onClick={() => setUserAnswers({...userAnswers, [currentIndex]: 'true'})}
                      className={`py-3 rounded-lg border transition-colors ${
                        userAnswers[currentIndex] === 'true'
                          ? 'bg-green-50 border-green-500'
                          : 'bg-white border-google-gray-300 hover:border-green-300'
                      }`}
                    >
                      ✓ 正确
                    </button>
                    <button
                      onClick={() => setUserAnswers({...userAnswers, [currentIndex]: 'false'})}
                      className={`py-3 rounded-lg border transition-colors ${
                        userAnswers[currentIndex] === 'false'
                          ? 'bg-red-50 border-red-500'
                          : 'bg-white border-google-gray-300 hover:border-red-300'
                      }`}
                    >
                      × 错误
                    </button>
                  </div>
                )}

                {currentQuestion.type === 'short_answer' && (
                  <textarea
                    value={userAnswers[currentIndex] || ''}
                    onChange={(e) => setUserAnswers({...userAnswers, [currentIndex]: e.target.value})}
                    placeholder="输入你的答案..."
                    rows={5}
                    className="w-full px-3 py-2 border border-google-gray-300 rounded-lg
                             focus:outline-none focus:ring-2 focus:ring-google-blue-500"
                  />
                )}

                {/* 导航按钮 */}
                <div className="flex gap-3">
                  {currentIndex > 0 && (
                    <button
                      onClick={() => setCurrentIndex(currentIndex - 1)}
                      className="flex-1 py-2 border border-google-gray-300 rounded-lg hover:bg-google-gray-50"
                    >
                      上一题
                    </button>
                  )}
                  {currentIndex < questions.length - 1 ? (
                    <button
                      onClick={() => setCurrentIndex(currentIndex + 1)}
                      className="flex-1 btn-primary py-2"
                    >
                      下一题
                    </button>
                  ) : (
                    <button
                      onClick={handleSubmit}
                      disabled={loading}
                      className="flex-1 btn-primary py-2 flex items-center justify-center gap-2"
                    >
                      {loading ? (
                        <>
                          <Loader2 size={16} className="animate-spin" />
                          评分中...
                        </>
                      ) : (
                        '提交答案'
                      )}
                    </button>
                  )}
                </div>
              </div>
            )}

            {/* 结果模式 */}
            {quizMode === 'result' && (
              <div className="space-y-4">
                {/* 成绩 */}
                <div className="bg-gradient-to-br from-google-blue-500 to-google-blue-600 rounded-lg p-6 text-white text-center">
                  <div className="text-4xl font-bold mb-2">
                    {Math.round((score / totalQuestions) * 100)}%
                  </div>
                  <div className="text-lg">
                    {score} / {totalQuestions} 正确
                  </div>
                </div>

                {/* 详细结果 */}
                <div className="space-y-3">
                  {results.map((result, idx) => (
                    <div
                      key={idx}
                      className={`p-4 rounded-lg border ${
                        result.is_correct
                          ? 'bg-green-50 border-green-200'
                          : 'bg-red-50 border-red-200'
                      }`}
                    >
                      <div className="flex items-start gap-2 mb-2">
                        {result.is_correct ? (
                          <CheckCircle size={20} className="text-green-600 flex-shrink-0 mt-0.5" />
                        ) : (
                          <XCircle size={20} className="text-red-600 flex-shrink-0 mt-0.5" />
                        )}
                        <div className="flex-1">
                          <p className="font-medium text-google-gray-900 mb-1">
                            第 {idx + 1} 题
                          </p>
                          <p className="text-sm text-google-gray-700 mb-2">
                            {result.question.question}
                          </p>
                          {!result.is_correct && (
                            <div className="text-sm">
                              <p className="text-red-700">
                                你的答案: {result.userAnswer || '未作答'}
                              </p>
                              <p className="text-green-700">
                                正确答案: {result.correct_answer}
                              </p>
                            </div>
                          )}
                          {result.feedback && (
                            <p className="text-xs text-google-gray-600 mt-2">
                              💡 {result.feedback}
                            </p>
                          )}
                        </div>
                      </div>
                    </div>
                  ))}
                </div>

                <button
                  onClick={handleReset}
                  className="w-full btn-primary py-3"
                >
                  重新开始
                </button>
              </div>
            )}
          </div>
        </motion.div>
      )}
    </AnimatePresence>
  );
};

export default QuizPanel;





