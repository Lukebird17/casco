#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
知识图谱系统
提取实体和关系，构建知识图谱
"""

import json
from typing import List, Dict, Tuple
from pathlib import Path
from openai import OpenAI
from config import OPENAI_API_KEY, OPENAI_API_BASE, MODEL_NAME


class KnowledgeGraph:
    """知识图谱管理器"""
    
    def __init__(self, storage_file: str = "./knowledge_graph.json", model: str = MODEL_NAME):
        self.storage_file = Path(storage_file)
        self.client = OpenAI(api_key=OPENAI_API_KEY, base_url=OPENAI_API_BASE)
        self.model = model
        
        # 图数据结构
        self.entities: Dict[str, Dict] = {}  # {实体名: {type, properties}}
        self.relationships: List[Dict] = []  # [{source, target, relation, properties}]
        
        self._load_graph()
    
    def _load_graph(self):
        """加载图数据"""
        if self.storage_file.exists():
            try:
                with open(self.storage_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.entities = data.get('entities', {})
                    self.relationships = data.get('relationships', [])
            except Exception as e:
                print(f"⚠️  加载知识图谱失败: {e}")
    
    def _save_graph(self):
        """保存图数据"""
        try:
            with open(self.storage_file, 'w', encoding='utf-8') as f:
                data = {
                    'entities': self.entities,
                    'relationships': self.relationships
                }
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"⚠️  保存知识图谱失败: {e}")
    
    def extract_entities_and_relations(self, text: str, source: str = "") -> Tuple[List[Dict], List[Dict]]:
        """
        从文本中提取实体和关系
        
        参数:
            text: 文本内容
            source: 来源
        
        返回:
            (实体列表, 关系列表)
        """
        prompt = f"""请从以下文本中提取关键实体和它们之间的关系。

文本：
{text[:2000]}

请以JSON格式返回，格式如下：
{{
  "entities": [
    {{
      "name": "实体名称",
      "type": "概念/人物/技术/术语",
      "description": "简短描述"
    }}
  ],
  "relationships": [
    {{
      "source": "源实体",
      "target": "目标实体",
      "relation": "关系类型（如：包含/属于/使用/实现等）",
      "description": "关系描述"
    }}
  ]
}}

要求：
1. 提取最重要的5-10个实体
2. 提取实体间的主要关系
3. 实体和关系要准确、清晰

现在开始提取："""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "你是一位知识图谱专家，擅长从文本中提取实体和关系。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=1500
            )
            
            result_text = response.choices[0].message.content.strip()
            
            # 提取JSON
            if '```json' in result_text:
                result_text = result_text.split('```json')[1].split('```')[0].strip()
            elif '```' in result_text:
                result_text = result_text.split('```')[1].split('```')[0].strip()
            
            data = json.loads(result_text)
            entities = data.get('entities', [])
            relationships = data.get('relationships', [])
            
            # 添加来源信息
            for entity in entities:
                entity['source'] = source
            for rel in relationships:
                rel['source'] = source
            
            return entities, relationships
            
        except Exception as e:
            print(f"提取实体和关系失败: {e}")
            return [], []
    
    def add_entities_and_relations(self, text: str, source: str = ""):
        """提取并添加实体和关系到图中"""
        entities, relationships = self.extract_entities_and_relations(text, source)
        
        # 添加实体
        for entity in entities:
            name = entity['name']
            if name not in self.entities:
                self.entities[name] = {
                    'type': entity.get('type', '未知'),
                    'description': entity.get('description', ''),
                    'sources': [source]
                }
            else:
                # 合并来源
                if source not in self.entities[name]['sources']:
                    self.entities[name]['sources'].append(source)
        
        # 添加关系
        for rel in relationships:
            # 检查是否已存在相同关系
            exists = any(
                r['source'] == rel['source'] and 
                r['target'] == rel['target'] and 
                r['relation'] == rel['relation']
                for r in self.relationships
            )
            if not exists:
                self.relationships.append(rel)
        
        self._save_graph()
        
        return len(entities), len(relationships)
    
    def get_related_entities(self, entity_name: str, max_depth: int = 2) -> List[Dict]:
        """获取与指定实体相关的实体"""
        related = []
        visited = set()
        
        def dfs(name: str, depth: int):
            if depth > max_depth or name in visited:
                return
            visited.add(name)
            
            # 查找所有相关关系
            for rel in self.relationships:
                if rel['source'] == name and rel['target'] not in visited:
                    related.append({
                        'entity': rel['target'],
                        'relation': rel['relation'],
                        'depth': depth
                    })
                    dfs(rel['target'], depth + 1)
                elif rel['target'] == name and rel['source'] not in visited:
                    related.append({
                        'entity': rel['source'],
                        'relation': f"被{rel['relation']}",
                        'depth': depth
                    })
                    dfs(rel['source'], depth + 1)
        
        dfs(entity_name, 0)
        return related
    
    def visualize_graph(self, max_nodes: int = 50) -> str:
        """
        生成图的可视化HTML（使用vis.js）
        
        返回:
            HTML字符串
        """
        # 限制节点数量
        entities_to_show = list(self.entities.items())[:max_nodes]
        
        # 构建nodes和edges数据
        nodes = []
        for name, info in entities_to_show:
            nodes.append({
                'id': name,
                'label': name,
                'title': info.get('description', ''),
                'group': info.get('type', '未知')
            })
        
        edges = []
        entity_names = set(name for name, _ in entities_to_show)
        for rel in self.relationships:
            if rel['source'] in entity_names and rel['target'] in entity_names:
                edges.append({
                    'from': rel['source'],
                    'to': rel['target'],
                    'label': rel['relation'],
                    'title': rel.get('description', '')
                })
        
        # 生成HTML
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>知识图谱</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/vis-network/9.1.2/standalone/umd/vis-network.min.js"></script>
    <style>
        #mynetwork {{
            width: 100%;
            height: 800px;
            border: 1px solid #ddd;
        }}
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
        }}
        h1 {{
            color: #333;
        }}
        .info {{
            background: #f0f0f0;
            padding: 10px;
            margin-bottom: 10px;
            border-radius: 5px;
        }}
    </style>
</head>
<body>
    <h1>🧠 知识图谱可视化</h1>
    <div class="info">
        <strong>实体数量:</strong> {len(self.entities)} | 
        <strong>关系数量:</strong> {len(self.relationships)} | 
        <strong>显示节点:</strong> {len(nodes)}
    </div>
    <div id="mynetwork"></div>
    
    <script>
        var nodes = new vis.DataSet({json.dumps(nodes, ensure_ascii=False)});
        var edges = new vis.DataSet({json.dumps(edges, ensure_ascii=False)});
        
        var container = document.getElementById('mynetwork');
        var data = {{
            nodes: nodes,
            edges: edges
        }};
        
        var options = {{
            nodes: {{
                shape: 'dot',
                size: 20,
                font: {{
                    size: 14,
                    color: '#000'
                }},
                borderWidth: 2
            }},
            edges: {{
                arrows: 'to',
                smooth: true,
                font: {{
                    size: 12,
                    align: 'middle'
                }}
            }},
            physics: {{
                enabled: true,
                barnesHut: {{
                    gravitationalConstant: -30000,
                    springLength: 150
                }}
            }},
            groups: {{
                '概念': {{color: {{background: '#97C2FC'}}}},
                '技术': {{color: {{background: '#FFCC99'}}}},
                '术语': {{color: {{background: '#C2FABC'}}}},
                '人物': {{color: {{background: '#FFC0CB'}}}}
            }}
        }};
        
        var network = new vis.Network(container, data, options);
        
        network.on("click", function(params) {{
            if (params.nodes.length > 0) {{
                var nodeId = params.nodes[0];
                console.log('点击节点:', nodeId);
            }}
        }});
    </script>
</body>
</html>
"""
        return html
    
    def search_entities(self, query: str) -> List[Dict]:
        """搜索实体"""
        query_lower = query.lower()
        results = []
        for name, info in self.entities.items():
            if (query_lower in name.lower() or 
                query_lower in info.get('description', '').lower()):
                results.append({
                    'name': name,
                    **info
                })
        return results
    
    def get_statistics(self) -> Dict:
        """获取统计信息"""
        entity_types = {}
        for entity in self.entities.values():
            entity_type = entity.get('type', '未知')
            entity_types[entity_type] = entity_types.get(entity_type, 0) + 1
        
        return {
            'total_entities': len(self.entities),
            'total_relationships': len(self.relationships),
            'entity_types': entity_types
        }


if __name__ == "__main__":
    # 测试
    kg = KnowledgeGraph("./test_kg.json")
    
    test_text = """
    操作系统是管理计算机硬件和软件资源的程序。
    Linux是一种开源操作系统，由Linus Torvalds创建。
    进程是操作系统中程序执行的实例。
    线程是进程内的执行单元。
    """
    
    print("提取知识...")
    num_entities, num_rels = kg.add_entities_and_relations(test_text, "测试文档")
    print(f"提取了 {num_entities} 个实体, {num_rels} 个关系")
    
    print(f"\n统计: {kg.get_statistics()}")
    
    # 生成可视化
    html = kg.visualize_graph()
    with open("./test_kg.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("\n可视化已保存到 test_kg.html")
