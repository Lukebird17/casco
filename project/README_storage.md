# New_Storage_Gen

## Environment
```bash
pip install -U FlagEmbedding
```

## Run
```bash
cd .../casco/project
python my_tokenize.py  # need md repository first, in my circumstance it's /output_paddle
python demo_enhanced.py # need storage repository generated from the code above, remember to change it
```

主要改动：
用了新版示例输出，在enhanced_agent.py里改了。 只调用BGE模型，然后切了块，把文档名称贴在每块开头。（因为看问题中很多涉及文档名称）

目前生成的回答信息检索很全面。答错是因为它以为“快轨”不属于“地铁”，这个涉及审题，我认为可能可以在COT中处理？关于问题语言严谨性我们或许需要多加考虑或者私信赛方。。

我还没有加入md表格/语言处理代码，今晚写好。调一个好一点的提示词用来修改表格。