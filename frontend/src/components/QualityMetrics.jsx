/**
 * 质量评估雷达图组件
 * 显示答案质量的多维度评估
 */

import React from 'react';
import { 
  Radar, 
  RadarChart, 
  PolarGrid, 
  PolarAngleAxis, 
  PolarRadiusAxis, 
  ResponsiveContainer 
} from 'recharts';
import { TrendingUp, CheckCircle2, Target, Database, Clock } from 'lucide-react';

// ✅ 三个指标的详细描述
const METRIC_DESCRIPTIONS = {
  faithfulness: {
    name: "忠实度 (Faithfulness)",
    icon: CheckCircle2,
    color: "text-green-600",
    bgColor: "bg-green-50",
    borderColor: "border-green-200",
    description: "AI回答是否忠实于检索到的原始资料",
    details: [
      "✓ 检查答案中的每个陈述是否有源材料支撑",
      "✓ 评估是否存在无依据的推测或臆造",
      "✓ 确保答案没有歪曲或误读原文"
    ],
    interpretation: {
      high: "答案完全基于提供的资料，没有添加外部信息",
      medium: "答案大部分基于资料，少量合理推论",
      low: "答案包含较多无依据内容，建议核查"
    }
  },
  answer_relevancy: {
    name: "相关性 (Answer Relevancy)",
    icon: Target,
    color: "text-blue-600",
    bgColor: "bg-blue-50",
    borderColor: "border-blue-200",
    description: "AI回答是否直接且准确地回应了用户问题",
    details: [
      "✓ 评估答案是否切中用户提问的核心",
      "✓ 检查是否包含了用户期待的关键信息",
      "✓ 判断答案是否有偏题或冗余内容"
    ],
    interpretation: {
      high: "答案完美契合问题，信息精准到位",
      medium: "答案回应了问题，但可能略有偏离",
      low: "答案与问题关联度不高，建议重新提问"
    }
  },
  contextual_relevancy: {
    name: "检索质量 (Contextual Relevancy)",
    icon: Database,
    color: "text-purple-600",
    bgColor: "bg-purple-50",
    borderColor: "border-purple-200",
    description: "检索到的文档与用户问题的匹配程度",
    details: [
      "✓ 评估检索到的资料是否包含问题相关信息",
      "✓ 检查是否有无关文档混入",
      "✓ 判断知识库的覆盖范围是否合适"
    ],
    interpretation: {
      high: "检索精准，找到的资料高度相关",
      medium: "检索结果基本相关，但可能有改进空间",
      low: "检索质量不佳，建议调整关键词或知识库"
    }
  }
};

const QualityRadarChart = ({ data }) => {
  if (!data || data.length === 0) {
    return (
      <div className="text-xs text-gray-400 text-center py-4 bg-gray-50 rounded">
        暂无详细维度数据
      </div>
    );
  }

  return (
    <div className="w-full h-48 sm:h-56 mt-2 -ml-2">
      <ResponsiveContainer width="100%" height="100%">
        <RadarChart cx="50%" cy="50%" outerRadius="70%" data={data}>
          <PolarGrid stroke="#e5e7eb" />
          <PolarAngleAxis 
            dataKey="subject" 
            tick={{ fill: '#4b5563', fontSize: 11 }} 
          />
          <PolarRadiusAxis 
            angle={30} 
            domain={[0, 100]} 
            tick={false} 
            axisLine={false} 
          />
          <Radar
            name="质量评分"
            dataKey="A"
            stroke="#4285f4"
            strokeWidth={2}
            fill="#4285f4"
            fillOpacity={0.4}
          />
        </RadarChart>
      </ResponsiveContainer>
    </div>
  );
};

/**
 * 质量评估显示组件
 * 包含总分、雷达图和详细说明
 */
export const QualityMetricsDisplay = ({ metrics }) => {
  // 兼容旧版 confidence 结构
  if (!metrics) return null;
  
  // 适配不同的数据结构
  const score = metrics.overall_score !== undefined 
    ? metrics.overall_score 
    : (metrics.score || 0);
  const radarData = metrics.radar_data || [];
  const detailedScores = metrics.detailed_scores || {};
  const evalTime = metrics.eval_time;

  // 根据分数确定颜色和标签
  const getColor = (s) => {
    if (s >= 0.8) return 'text-green-600 bg-green-50 border-green-200';
    if (s >= 0.6) return 'text-yellow-600 bg-yellow-50 border-yellow-200';
    return 'text-red-600 bg-red-50 border-red-200';
  };

  const getLabel = (s) => {
    if (s >= 0.8) return '优秀';
    if (s >= 0.6) return '良好';
    return '需核查';
  };

  const getIcon = (s) => {
    if (s >= 0.8) return '⭐⭐⭐⭐⭐';
    if (s >= 0.6) return '⭐⭐⭐⭐';
    return '⭐⭐⭐';
  };

  // ✅ 获取分数级别描述
  const getScoreInterpretation = (metricKey, scoreValue) => {
    const desc = METRIC_DESCRIPTIONS[metricKey];
    if (!desc) return "";
    if (scoreValue >= 0.8) return desc.interpretation.high;
    if (scoreValue >= 0.6) return desc.interpretation.medium;
    return desc.interpretation.low;
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-google-gray-200 p-5">
      {/* 头部：标题和总分 */}
      <div className="flex items-center justify-between mb-2">
        <div className="flex items-center gap-2">
          <TrendingUp size={20} className="text-google-blue-600" />
          <h3 className="font-semibold text-google-gray-900">AI 自省报告</h3>
        </div>
        
        <div className={`px-3 py-1 rounded-full text-sm font-medium border ${getColor(score)}`}>
          {getIcon(score)} {getLabel(score)}: {(score * 100).toFixed(0)}分
        </div>
      </div>

      {/* ✅ 评估时间显示 */}
      {evalTime !== undefined && (
        <div className="flex items-center gap-1 text-xs text-google-gray-500 mb-3">
          <Clock size={12} />
          <span>评估耗时 {evalTime}秒</span>
        </div>
      )}

      {/* 雷达图区域 */}
      {radarData.length > 0 ? (
        <div className="bg-google-gray-50 rounded-lg border border-google-gray-100 p-2 mb-4">
          <QualityRadarChart data={radarData} />
        </div>
      ) : (
        <div className="text-xs text-gray-400 text-center py-4 bg-gray-50 rounded mb-4">
          暂无详细维度数据
        </div>
      )}

      {/* ✅ 详细指标说明 */}
      <div className="space-y-4 border-t border-gray-100 pt-4">
        <div className="text-sm font-semibold text-gray-700 mb-3">
          📊 三维质量评估详解
        </div>
        
        {Object.entries(detailedScores).map(([metricKey, scoreValue]) => {
          const desc = METRIC_DESCRIPTIONS[metricKey];
          if (!desc) return null;
          
          const Icon = desc.icon;
          const interpretation = getScoreInterpretation(metricKey, scoreValue);
          
          return (
            <div 
              key={metricKey} 
              className={`rounded-lg border ${desc.borderColor} ${desc.bgColor} p-3`}
            >
              {/* 指标名称和分数 */}
              <div className="flex items-center justify-between mb-2">
                <div className="flex items-center gap-2">
                  <Icon size={16} className={desc.color} />
                  <span className={`text-sm font-semibold ${desc.color}`}>
                    {desc.name}
                  </span>
                </div>
                <span className={`text-sm font-bold ${desc.color}`}>
                  {(scoreValue * 100).toFixed(0)}分
                </span>
              </div>
              
              {/* 指标描述 */}
              <p className="text-xs text-gray-700 mb-2">
                {desc.description}
              </p>
              
              {/* 评估要点 */}
              <div className="text-xs text-gray-600 space-y-1 mb-2">
                {desc.details.map((detail, idx) => (
                  <div key={idx}>{detail}</div>
                ))}
              </div>
              
              {/* 本次评估结果解读 */}
              <div className={`text-xs ${desc.color} font-medium bg-white rounded px-2 py-1 border ${desc.borderColor}`}>
                💡 {interpretation}
              </div>
            </div>
          );
        })}
      </div>

      {/* 底部提示 */}
      <div className="mt-4 text-xs text-gray-500 bg-gray-50 rounded-lg p-3 border border-gray-200">
        <strong>📖 使用建议：</strong>
        <ul className="list-disc list-inside mt-1 space-y-1">
          <li>总分70分以上表示答案质量可信</li>
          <li>如相关性较低，建议重新组织问题</li>
          <li>如检索质量不佳，可尝试添加更多关键词或切换知识库</li>
          <li>如忠实度偏低，建议交叉核对原始资料</li>
        </ul>
      </div>
    </div>
  );
};

export default QualityRadarChart;

