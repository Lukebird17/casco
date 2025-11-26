# Instructions
```bash
cd OCR_DEMO_PROJECT
python extract_questions.py # 从指定文档中读取题目并进行预处理（把双引号改成单引号）生成questions_list.txt
python demo_enhanced.py # 没用_fixed版，有需要的手动一下私密马赛
```

# 主要修改：
## demo_enhanced.py
- 从文档questions_list.txt中读取问题，生成enhanced_demo_results.json和reasoning_log.txt。都是一次运行过程中增量式保存（生成一题存一题），不同运行轮次覆盖式保存。
- 有保护性编码，没有读到文档也留了黏贴问题的入口，想要小范围测试可以不运行extract_questions.py或者删掉questions_list.txt，贴自己的问题

## enhanced_agent.py
- 增加逻辑链日志输出，便于调试（关键词识别，语料语言，问题类型判断即原因等）
- 修改输出代码，使生成的答案更美观

目前用的是字典版storage_bge_hierarchy，感觉高级题性能略有倒退，懂行的可以看一下。。。