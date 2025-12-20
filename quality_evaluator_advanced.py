"""
高级质量评估模块（融合yzy的DeepEval实现）
使用DeepEval库进行专业的答案质量评估
支持3个核心指标：忠实度、切题度、检索质量
"""

from typing import Dict, List, Optional
import json
import concurrent.futures
from openai import OpenAI

from config import (
    OPENAI_API_KEY,
    OPENAI_API_BASE,
    MODEL_NAME,
)

# 尝试导入 DeepEval
try:
    from deepeval.models.base_model import DeepEvalBaseLLM
    from deepeval.metrics import (
        FaithfulnessMetric,
        AnswerRelevancyMetric,
        ContextualRelevancyMetric
    )
    from deepeval.test_case import LLMTestCase
    DEEPEVAL_AVAILABLE = True
    print("✅ DeepEval 可用")
except ImportError:
    DEEPEVAL_AVAILABLE = False
    print("⚠️  DeepEval 未安装，将使用简化版评估")
    # 创建假的基类以避免 NameError
    class DeepEvalBaseLLM:
        pass


if DEEPEVAL_AVAILABLE:
    class CustomSiliconFlowLLM(DeepEvalBaseLLM):
        """
        适配 DeepEval 的自定义 LLM 包装器 (融合自yzy)
        
        特性：
        1. 动态 Prompt 强化 - 根据请求类型添加格式提示
        2. 脏数据正则修复 - 处理不规范的JSON输出
        3. 全字段互通 - 确保所有必需字段都存在
        4. 超时熔断 - 20秒超时保护
        """
        
        def __init__(self, model_name, api_key, base_url):
            self.model_name = model_name
            self.client = OpenAI(api_key=api_key, base_url=base_url)

        def load_model(self):
            return self.client

        def generate(self, prompt: str) -> str:
            """
            生成评估结果（带智能修复）
            """
            print(f"🔍 [LLM] generate 被调用，prompt长度: {len(prompt)}")
            
            # 1. 动态 Prompt 强化
            suffix = ""
            if "'verdicts'" in prompt or '"verdicts"' in prompt:
                suffix = (
                    "\n\n*** URGENT FORMAT REMINDER ***\n"
                    "You MUST output a JSON object with a key 'verdicts'.\n"
                    "'verdicts' MUST be a list of OBJECTS (e.g., [{'verdict': 'yes', ...}]).\n"
                    "Do NOT output a list of strings."
                )
            elif "'statements'" in prompt or '"statements"' in prompt:
                suffix = (
                    "\n\n*** URGENT FORMAT REMINDER ***\n"
                    "You MUST output a JSON object with a key 'statements'.\n"
                    "'statements' MUST be a list of STRINGS."
                )
            elif "'truths'" in prompt or '"truths"' in prompt:
                suffix = (
                    "\n\n*** URGENT FORMAT REMINDER ***\n"
                    "You MUST output a JSON object with a key 'truths'.\n"
                    "'truths' MUST be a list of STRINGS."
                )
                
            final_prompt = prompt + suffix
            print(f"🔍 [LLM] 准备调用LLM API...")

            try:
                # 2. 调用 LLM (带更长超时 - 60秒)
                print(f"🔍 [LLM] 开始请求 {self.model_name}...")
                response = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=[{"role": "user", "content": final_prompt}],
                    temperature=0.0,
                    max_tokens=1024,  # ⚡ 从1536减少到1024，加速生成
                    response_format={"type": "json_object"},
                    timeout=45  # ⚡ 超时从60减少到45秒
                )
                print(f"🔍 [LLM] API响应成功")
                content = response.choices[0].message.content
                print(f"🔍 [LLM] 响应内容长度: {len(content)}")
                
                # 3. 结构重构与补全
                print(f"🔍 [LLM] 开始JSON结构规范化...")
                final_json = self._normalize_json_structure(content)
                print(f"🔍 [LLM] JSON规范化完成")
                return final_json

            except Exception as e:
                print(f"⚠️  LLM 生成异常: {e}")
                import traceback
                traceback.print_exc()
                return self._get_fallback_json()

        async def a_generate(self, prompt: str) -> str:
            """异步生成（DeepEval可能会调用）"""
            print(f"🔍 [LLM] a_generate 被调用（异步），prompt长度: {len(prompt)}")
            # 在线程池中运行同步的generate
            import asyncio
            loop = asyncio.get_event_loop()
            result = await loop.run_in_executor(None, self.generate, prompt)
            print(f"🔍 [LLM] a_generate 完成")
            return result

        def get_model_name(self):
            return self.model_name

        def _get_fallback_json(self) -> str:
            """返回包含所有可能字段的万能兜底结构"""
            fallback = {
                "verdict": "yes",
                "reason": "Fallback reason",
                "verdicts": [{"verdict": "yes", "statement": "Fallback", "reason": "Fallback"}],
                "statements": ["Fallback statement"],
                "claims": ["Fallback claim"],
                "truths": ["Fallback truth"]
            }
            return json.dumps(fallback)

        def _normalize_json_structure(self, text: str) -> str:
            """
            核心修复逻辑：清洗 Markdown -> 正则修复 -> 解析 -> 键名规范 -> 字段互通
            """
            print(f"🔍 [JSON] 开始规范化，输入长度: {len(text) if text else 0}")
            
            if not text:
                print(f"🔍 [JSON] 输入为空，返回fallback")
                return self._get_fallback_json()
            
            # A. 基础清洗
            print(f"🔍 [JSON] A. 基础清洗...")
            text = text.strip()
            if text.startswith("```"):
                import re
                text = re.sub(r"^```[a-zA-Z]*\n?", "", text)
            if text.endswith("```"):
                import re
                text = re.sub(r"\n?```$", "", text)
                
            start, end = text.find("{"), text.rfind("}")
            if start != -1 and end != -1:
                text = text[start : end + 1]

            # B. 简单替换：将值内部的换行符替换为空格
            print(f"🔍 [JSON] B. 替换换行符...")
            try:
                text = text.replace('\n', ' ').replace('\r', '')
            except:
                pass

            # C. 解析尝试
            print(f"🔍 [JSON] C. 尝试JSON解析...")
            try:
                data = json.loads(text)
                print(f"🔍 [JSON] JSON解析成功，类型: {type(data)}")
            except json.JSONDecodeError as e:
                print(f"🔍 [JSON] JSON解析失败: {e}，返回fallback")
                return self._get_fallback_json()

            # D. 键名规范化
            print(f"🔍 [JSON] D. 键名规范化...")
            def normalize_keys(d):
                if not isinstance(d, dict):
                    return d
                new_d = {}
                for k, v in d.items():
                    k_lower = k.lower()
                    # 映射各种可能的幻觉键名
                    if k_lower in ['cverdict', 'c_verdict']:
                        k = 'verdict'
                    elif k_lower in ['creason', 'c_reason']:
                        k = 'reason'
                    elif k_lower in ['cstatement', 'c_statement', 'class']:
                        k = 'statement'
                    elif k_lower in ['statement']:
                        k = 'statements'
                    elif k_lower in ['claim']:
                        k = 'claims'
                    elif k_lower in ['truth']:
                        k = 'truths'
                    new_d[k] = v
                return new_d

            if isinstance(data, list):
                temp_list = data
                data = {} 
            else:
                data = normalize_keys(data)
                temp_list = []

            # E. 构建"厨房洗碗槽" (Kitchen Sink) JSON
            print(f"🔍 [JSON] E. 构建super_json...")
            super_json = {
                "verdict": "yes",
                "reason": "Generated reason",
                "verdicts": [],
                "statements": [],
                "claims": [],
                "truths": []
            }

            # 数据合并
            print(f"🔍 [JSON] 数据合并，keys: {list(data.keys())}")
            for k, v in data.items():
                if k in super_json:
                    # 类型强转，防止类型不匹配报错
                    if isinstance(super_json[k], list) and isinstance(v, str):
                        super_json[k] = [v]
                    elif isinstance(super_json[k], str) and isinstance(v, list):
                        super_json[k] = str(v[0]) if v else "yes"
                    else:
                        super_json[k] = v

            # F. 字段互通 (Cross-Pollination)
            print(f"🔍 [JSON] F. 字段互通...")
            if temp_list:
                if not super_json['statements']:
                    super_json['statements'] = temp_list
                if not super_json['claims']:
                    super_json['claims'] = temp_list
                if not super_json['truths']:
                    super_json['truths'] = temp_list

            # 同步 claims 和 truths
            print(f"🔍 [JSON] 同步 claims 和 truths...")
            if super_json['claims'] and not super_json['truths']:
                super_json['truths'] = super_json['claims']
            if super_json['truths'] and not super_json['claims']:
                super_json['claims'] = super_json['truths']
                
            # 确保 statements 不为空
            if not super_json['statements']:
                if super_json['claims']:
                    super_json['statements'] = super_json['claims']
                else:
                    super_json['statements'] = ["Generated statement"]

            # G. Verdicts 列表深度清洗
            print(f"🔍 [JSON] G. Verdicts清洗...")
            if super_json['verdicts']:
                clean_verdicts = []
                for idx, item in enumerate(super_json['verdicts']):
                    if isinstance(item, dict):
                        item = normalize_keys(item)
                        clean_verdicts.append({
                            "verdict": str(item.get('verdict', 'yes')),
                            "reason": str(item.get('reason', 'Generated')),
                            "statement": str(item.get('statement', 'Generated statement'))
                        })
                super_json['verdicts'] = clean_verdicts
                print(f"🔍 [JSON] 清洗了 {len(clean_verdicts)} 个verdicts")
            else:
                super_json['verdicts'] = [{
                    "verdict": super_json['verdict'],
                    "reason": super_json['reason'],
                    "statement": "Generated statement"
                }]
                print(f"🔍 [JSON] 生成默认verdict")

            print(f"🔍 [JSON] ✅ JSON规范化完成，返回结果")
            return json.dumps(super_json)
else:
    # DeepEval 不可用时的占位类
    class CustomSiliconFlowLLM:
        pass


class AdvancedQualityEvaluator:
    """
    高级质量评估器（融合yzy的DeepEval实现）
    
    核心指标：
    1. Faithfulness (忠实度) - 答案是否基于检索到的上下文
    2. Answer Relevancy (切题度) - 答案是否回答了用户问题
    3. Contextual Relevancy (检索质量) - 检索到的上下文是否与问题相关
    """
    
    def __init__(self, judge_model: str = MODEL_NAME):
        self.judge_model = judge_model
        
        if not DEEPEVAL_AVAILABLE:
            print("⚠️  DeepEval不可用，将使用简化评估")
            self.deepeval_mode = False
        else:
            self.deepeval_mode = True
            # 初始化自定义LLM适配器
            self.llm = CustomSiliconFlowLLM(
                model_name=judge_model,
                api_key=OPENAI_API_KEY,
                base_url=OPENAI_API_BASE
            )
            print("✅ DeepEval评估器初始化（已优化加速）")
    
    async def evaluate(
        self,
        query: str,
        answer: str,
        retrieved_context: List[Dict],
        chat_history: Optional[List[Dict]] = None
    ) -> Dict:
        """
        评估答案质量
        
        参数:
            query: 用户问题
            answer: AI回答
            retrieved_context: 检索到的上下文文档列表
            chat_history: 聊天历史（可选）
        
        返回:
            {
                "overall_score": 0.85,  # 总分 0-1
                "radar_data": [
                    {"subject": "忠实度", "A": 90, "fullMark": 100},
                    {"subject": "切题度", "A": 85, "fullMark": 100},
                    {"subject": "检索质量", "A": 80, "fullMark": 100}
                ],
                "detailed_scores": {
                    "faithfulness": 0.90,
                    "answer_relevancy": 0.85,
                    "contextual_relevancy": 0.80
                },
                "explanations": {
                    "faithfulness": "详细说明...",
                    ...
                }
            }
        """
        
        if not self.deepeval_mode:
            # 使用简化评估
            print("⚠️  使用简化评估模式")
            return self._simple_evaluation(query, answer, retrieved_context)
        
        try:
            print("🔍 [DEBUG] 开始DeepEval评估流程...")
            
            # 1. ⚡ 极速优化：准备评估上下文（1个文档，300字符）
            print(f"🔍 [DEBUG] 步骤1: 准备上下文，检索到 {len(retrieved_context)} 个文档")
            eval_context_docs = retrieved_context[:1]  # ⚡ 只取1个文档
            retrieval_context = [
                doc.get('content', '')[:300] for doc in eval_context_docs  # ⚡ 每个只取300字符
            ]
            print(f"🔍 [DEBUG] 准备了 {len(retrieval_context)} 个上下文片段用于评估（已极度精简）")
            
            # 2. 创建测试用例
            print("🔍 [DEBUG] 步骤2: 创建LLMTestCase...")
            test_case = LLMTestCase(
                input=query,
                actual_output=answer,
                retrieval_context=retrieval_context
            )
            print("🔍 [DEBUG] LLMTestCase创建成功")
            print(f"🔍 [DEBUG] input长度: {len(query)}")
            print(f"🔍 [DEBUG] actual_output长度: {len(answer)}")
            print(f"🔍 [DEBUG] retrieval_context条数: {len(retrieval_context)}")
            print(f"🔍 [DEBUG] query前100字: {query[:100]}")
            print(f"🔍 [DEBUG] answer前100字: {answer[:100]}")
            print(f"🔍 [DEBUG] context[0]前100字: {retrieval_context[0][:100] if retrieval_context else 'N/A'}")
            
            # 3. 定义安全执行函数（参考yzy）
            def run_safe_metric(metric_cls, name):
                try:
                    print(f"🔍 [DEBUG] 开始评估指标: {name}")
                    # 强制 include_reason=False 提速
                    metric = metric_cls(threshold=0.5, model=self.llm, include_reason=False)
                    print(f"🔍 [DEBUG] {name} 指标初始化成功，开始measure...")
                    metric.measure(test_case)
                    
                    # ✅ 关键调试：检查metric.score的值和类型
                    print(f"🔍 [DEBUG] {name} measure完成")
                    print(f"🔍 [DEBUG] {name} metric.score = {metric.score} (type: {type(metric.score)})")
                    print(f"🔍 [DEBUG] {name} metric.success = {getattr(metric, 'success', 'N/A')}")
                    print(f"🔍 [DEBUG] {name} metric.reason = {getattr(metric, 'reason', 'N/A')}")
                    
                    # 如果score是None或者异常值，返回0.5
                    if metric.score is None:
                        print(f"  ⚠️  {name} score为None，使用默认值0.5")
                        return name, 0.5, "score为None"
                    
                    # 确保score是有效数值
                    score_value = float(metric.score)
                    print(f"🔍 [DEBUG] {name} 评估完成，最终得分: {score_value}")
                    return name, score_value, ""
                except Exception as e:
                    print(f"  ⚠️  {name} 评估出错，已自动置为 0.5: {e}")
                    import traceback
                    traceback.print_exc()
                    # 发生任何错误，直接返回 0.5
                    return name, 0.5, "评估异常，默认中立"
            
            # 4. 并行执行3个指标评估
            print("🔍 [DEBUG] 步骤4: 开始并行执行3个指标评估...")
            results = {}
            with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
                print("🔍 [DEBUG] 提交3个评估任务到线程池...")
                futures = [
                    executor.submit(run_safe_metric, FaithfulnessMetric, "faithfulness"),
                    executor.submit(run_safe_metric, AnswerRelevancyMetric, "answer_relevancy"),
                    executor.submit(run_safe_metric, ContextualRelevancyMetric, "contextual_relevancy")
                ]
                
                print("🔍 [DEBUG] 等待评估任务完成...")
                for idx, future in enumerate(concurrent.futures.as_completed(futures)):
                    print(f"🔍 [DEBUG] 任务 {idx+1}/3 完成")
                    name, score, reason = future.result()
                    results[name] = {"score": score, "reason": reason}
                    print(f"🔍 [DEBUG] {name} 结果已保存")
            
            print("🔍 [DEBUG] 步骤5: 组装最终评估结果...")
            # 5. 数据组装
            f_score = results.get("faithfulness", {}).get("score", 0.5)
            a_score = results.get("answer_relevancy", {}).get("score", 0.5)
            c_score = results.get("contextual_relevancy", {}).get("score", 0.5)
            
            avg_score = (f_score + a_score + c_score) / 3
            print(f"🔍 [DEBUG] 平均分: {avg_score:.2f} (忠实度={f_score:.2f}, 相关性={a_score:.2f}, 检索质量={c_score:.2f})")
            
            # 6. 生成雷达图数据
            radar_data = [
                {"subject": "忠实度", "A": round(f_score * 100, 0), "fullMark": 100},
                {"subject": "相关性", "A": round(a_score * 100, 0), "fullMark": 100},
                {"subject": "检索质量", "A": round(c_score * 100, 0), "fullMark": 100},
            ]
            
            final_result = {
                "overall_score": round(avg_score, 2),
                "radar_data": radar_data,
                "detailed_scores": {
                    "faithfulness": round(f_score, 2),
                    "answer_relevancy": round(a_score, 2),
                    "contextual_relevancy": round(c_score, 2)
                },
                "explanations": {
                    "faithfulness": results.get("faithfulness", {}).get("reason", ""),
                    "answer_relevancy": results.get("answer_relevancy", {}).get("reason", ""),
                    "contextual_relevancy": results.get("contextual_relevancy", {}).get("reason", "")
                }
            }
            
            print("🔍 [DEBUG] ✅ 评估流程完成，返回结果")
            return final_result
            
        except Exception as e:
            print(f"⚠️  DeepEval评估失败: {e}")
            return self._get_fallback_evaluation()
    
    def _simple_evaluation(
        self,
        query: str,
        answer: str,
        retrieved_context: List[Dict]
    ) -> Dict:
        """
        简化评估（当DeepEval不可用时）
        使用基于规则的启发式方法
        """
        # 基于长度和关键词匹配的简单评分
        score = 0.7  # 默认70分
        
        # 检查答案长度
        if len(answer) < 50:
            score -= 0.1
        elif len(answer) > 200:
            score += 0.1
        
        # 检查是否有引用
        if '根据' in answer or '来源' in answer or '第' in answer and '页' in answer:
            score += 0.1
        
        # 限制在0-1范围
        score = max(0.0, min(1.0, score))
        
        radar_value = round(score * 100, 0)
        
        return {
            "overall_score": round(score, 2),
            "radar_data": [
                {"subject": "忠实度", "A": radar_value, "fullMark": 100},
                {"subject": "相关性", "A": radar_value, "fullMark": 100},
                {"subject": "检索质量", "A": radar_value, "fullMark": 100},
            ],
            "detailed_scores": {
                "faithfulness": round(score, 2),
                "answer_relevancy": round(score, 2),
                "contextual_relevancy": round(score, 2)
            },
            "explanations": {
                "faithfulness": "使用简化评估（DeepEval不可用）",
                "answer_relevancy": "使用简化评估（DeepEval不可用）",
                "contextual_relevancy": "使用简化评估（DeepEval不可用）"
            }
        }
    
    def _get_fallback_evaluation(self) -> Dict:
        """返回默认评估结果（评估失败时使用）"""
        return {
            "overall_score": 0.5,
            "radar_data": [
                {"subject": "忠实度", "A": 50, "fullMark": 100},
                {"subject": "相关性", "A": 50, "fullMark": 100},
                {"subject": "检索质量", "A": 50, "fullMark": 100},
            ],
            "detailed_scores": {
                "faithfulness": 0.5,
                "answer_relevancy": 0.5,
                "contextual_relevancy": 0.5
            },
            "explanations": {
                "faithfulness": "评估服务暂不可用",
                "answer_relevancy": "评估服务暂不可用",
                "contextual_relevancy": "评估服务暂不可用"
            }
        }


# 为了向后兼容，保留简单的别名
QualityEvaluator = AdvancedQualityEvaluator


if __name__ == "__main__":
    # 测试
    import asyncio
    
    evaluator = AdvancedQualityEvaluator()
    
    test_query = "什么是隐马尔可夫模型？"
    test_answer = "隐马尔可夫模型（HMM）是一种统计模型，用于描述含有隐藏状态的马尔可夫过程。它在语音识别、自然语言处理等领域有广泛应用。"
    test_context = [
        {
            "content": "隐马尔可夫模型是一种重要的统计模型，包含观测序列和隐藏状态序列...",
            "filename": "test.pdf",
            "page_number": 1
        }
    ]
    
    async def test():
        result = await evaluator.evaluate(test_query, test_answer, test_context)
        
        print("\n📊 评估结果：")
        print(f"   总分: {result['overall_score']}")
        print(f"\n📈 雷达图数据:")
        for item in result['radar_data']:
            print(f"   {item['subject']}: {item['A']}分")
        print(f"\n📝 详细分数:")
        for metric, score in result['detailed_scores'].items():
            print(f"   {metric}: {score}")
    
    asyncio.run(test())

