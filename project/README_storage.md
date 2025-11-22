# New_Storage_Gen

## Environment
```bash
pip install -U FlagEmbedding
```

## Run Instructions
```bash
cd .../casco/project
python markdown_table_processor.py # from /output_paddle to /output_paddle_table
python my_tokenize.py  # from /output_paddle_table to /storage
python demo_enhanced.py # need /storage 
```

主要改动：
目前我的pipeline: 拿到OCR提取的md文件，处理表格（markdown_table_processor.py/table_prompt.txt），经过BGE获得向量库, QT 增强查询。