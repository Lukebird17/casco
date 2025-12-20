#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
基于 LlamaIndex 的知识图谱实现
支持更智能的实体提取和关系识别
"""

import json
import os
from typing import List, Dict, Tuple, Optional
from pathlib import Path

try:
    from llama_index.core import Document, KnowledgeGraphIndex, StorageContext
    from llama_index.core.graph_stores import SimpleGraphStore
    from llama_index.llms.openai import OpenAI as LlamaOpenAI
    LLAMAINDEX_AVAILABLE = True
except ImportError:
    LLAMAINDEX_AVAILABLE = False
    print("⚠️  LlamaIndex 未安装，使用降级方案")

from openai import OpenAI
from config import OPENAI_API_KEY, OPENAI_API_BASE, MODEL_NAME


class LlamaIndexKnowledgeGraph:
    """基于 LlamaIndex 的知识图谱管理器"""
    
    def __init__(self, storage_file: str = "./knowledge_graph_llama.json"):
        self.storage_file = Path(storage_file)
        self.client = OpenAI(api_key=OPENAI_API_KEY, base_url=OPENAI_API_BASE)
        self.model = MODEL_NAME
        
        # 存储数据
        self.entities: Dict[str, Dict] = {}
        self.relationships: List[Dict] = []
        
        # 初始化 LlamaIndex（如果可用）
        if LLAMAINDEX_AVAILABLE:
            self._init_llamaindex()
        
        # 加载现有数据
        self._load_graph()
    
    def _init_llamaindex(self):
        """初始化 LlamaIndex 组件"""
        try:
            # 配置 LLM
            self.llm = LlamaOpenAI(
                api_key=OPENAI_API_KEY,
                api_base=OPENAI_API_BASE,
                model=MODEL_NAME,
                temperature=0.3
            )
            
            # 图存储
            self.graph_store = SimpleGraphStore()
            
            # 存储上下文
            self.storage_context = StorageContext.from_defaults(
                graph_store=self.graph_store
            )
            
            print("✅ LlamaIndex 初始化成功")
            
        except Exception as e:
            print(f"⚠️  LlamaIndex 初始化失败: {e}")
            self.llm = None
            self.graph_store = None
    
    def _load_graph(self):
        """加载图数据"""
        if self.storage_file.exists():
            try:
                with open(self.storage_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.entities = data.get('entities', {})
                    self.relationships = data.get('relationships', [])
                print(f"✅ 加载知识图谱: {len(self.entities)}个实体, {len(self.relationships)}条关系")
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
            print(f"✅ 保存知识图谱: {len(self.entities)}个实体, {len(self.relationships)}条关系")
        except Exception as e:
            print(f"⚠️  保存知识图谱失败: {e}")
    
    def extract_with_llamaindex(self, text: str, source: str = "") -> Tuple[List[Dict], List[Dict]]:
        """
        使用 LlamaIndex 提取实体和关系
        
        参数:
            text: 文本内容
            source: 来源
        
        返回:
            (实体列表, 关系列表)
        """
        if not LLAMAINDEX_AVAILABLE or self.llm is None:
            # 降级到 LLM 方法
            return self._extract_with_llm(text, source)
        
        try:
            print(f"🤖 使用 LlamaIndex 提取知识图谱...")
            
            # 创建文档
            documents = [Document(text=text, metadata={"source": source})]
            
            # 构建知识图谱索引
            index = KnowledgeGraphIndex.from_documents(
                documents,
                storage_context=self.storage_context,
                llm=self.llm,
                max_triplets_per_chunk=10,
                include_embeddings=False
            )
            
            # 从图存储中提取实体和关系
            entities = []
            relationships = []
            
            # 获取所有三元组
            if hasattr(self.graph_store, 'get_all'):
                triplets = self.graph_store.get_all()
                
                # 处理实体
                entity_set = set()
                for triplet in triplets:
                    # triplet 格式: (subject, relation, object)
                    if len(triplet) >= 3:
                        subject = str(triplet[0])
                        obj = str(triplet[2])
                        relation = str(triplet[1])
                        
                        # 添加实体
                        entity_set.add(subject)
                        entity_set.add(obj)
                        
                        # 添加关系
                        relationships.append({
                            'source': subject,
                            'target': obj,
                            'relation': relation,
                            'description': f'{subject} {relation} {obj}',
                            'weight': 1
                        })
                
                # 构建实体列表
                for entity_name in entity_set:
                    entities.append({
                        'name': entity_name,
                        'type': self._infer_entity_type(entity_name),
                        'description': f'来自文档: {source}',
                        'source': source,
                        'score': 0.9
                    })
            
            print(f"✅ LlamaIndex 提取: {len(entities)}个实体, {len(relationships)}条关系")
            
            return entities, relationships
            
        except Exception as e:
            print(f"⚠️  LlamaIndex 提取失败: {e}，降级到 LLM 方法")
            import traceback
            traceback.print_exc()
            return self._extract_with_llm(text, source)
    
    def _extract_with_llm(self, text: str, source: str = "") -> Tuple[List[Dict], List[Dict]]:
        """
        使用 LLM 直接提取（降级方案）
        
        参数:
            text: 文本内容
            source: 来源
        
        返回:
            (实体列表, 关系列表)
        """
        # 限制文本长度
        text_excerpt = text[:3000] if len(text) > 3000 else text
        
        prompt = f"""请从以下文本中提取关键实体和它们之间的关系，构建知识图谱。

文本内容：
{text_excerpt}

请以JSON格式返回：
{{
  "entities": [
    {{
      "name": "实体名称（必须完整，如'隐马尔可夫模型'而不是'马尔可夫'）",
      "type": "人物|地点|组织|概念|技术|术语|动作",
      "description": "简短描述"
    }}
  ],
  "relationships": [
    {{
      "source": "源实体名称",
      "target": "目标实体名称",
      "relation": "包含|属于|使用|实现|基于|产生|导致|定义|相关",
      "description": "关系描述"
    }}
  ]
}}

要求：
1. 实体名称必须完整（如"隐马尔可夫模型"7个字，不要截断）
2. 提取5-20个最重要的实体
3. 提取5-30条主要关系
4. 只返回JSON，不要其他说明
5. 确保source和target都在entities中
"""
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "你是一位知识图谱专家，擅长从文本中提取完整的实体和准确的关系。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=2000
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
                if 'score' not in entity:
                    entity['score'] = 0.8
            
            for rel in relationships:
                if 'weight' not in rel:
                    rel['weight'] = 1
            
            print(f"✅ LLM提取: {len(entities)}个实体, {len(relationships)}条关系")
            
            return entities, relationships
            
        except Exception as e:
            print(f"❌ LLM提取失败: {e}")
            return [], []
    
    def _infer_entity_type(self, entity_name: str) -> str:
        """推断实体类型"""
        # 简单的启发式规则
        if len(entity_name) <= 3:
            # 短名称可能是人名或缩写
            if entity_name.isupper():
                return '术语'
            else:
                return '概念'
        elif '模型' in entity_name or '算法' in entity_name:
            return '技术'
        elif '网络' in entity_name or '系统' in entity_name:
            return '技术'
        elif entity_name[0].isupper():
            return '术语'
        else:
            return '概念'
    
    def add_entities_and_relations(self, text: str, source: str = "") -> Tuple[int, int]:
        """
        提取并添加实体和关系到图中
        
        参数:
            text: 文本内容
            source: 来源
        
        返回:
            (新增实体数, 新增关系数)
        """
        # 提取
        entities, relationships = self.extract_with_llamaindex(text, source)
        
        # 统计新增数量
        new_entities = 0
        new_relationships = 0
        
        # 添加实体
        for entity in entities:
            name = entity.get('name', '')
            if not name:
                continue
            
            if name not in self.entities:
                self.entities[name] = {
                    'type': entity.get('type', '概念'),
                    'description': entity.get('description', ''),
                    'score': entity.get('score', 0.8),
                    'sources': [entity.get('source', '')]
                }
                new_entities += 1
            else:
                # 更新已有实体
                if entity.get('source') and entity['source'] not in self.entities[name].get('sources', []):
                    if 'sources' not in self.entities[name]:
                        self.entities[name]['sources'] = []
                    self.entities[name]['sources'].append(entity['source'])
        
        # 添加关系
        for rel in relationships:
            source_entity = rel.get('source', '')
            target_entity = rel.get('target', '')
            relation = rel.get('relation', '相关')
            
            if not source_entity or not target_entity:
                continue
            
            # 确保实体存在
            if source_entity not in self.entities or target_entity not in self.entities:
                continue
            
            # 检查是否已存在
            exists = any(
                r.get('source') == source_entity and 
                r.get('target') == target_entity and 
                r.get('relation') == relation
                for r in self.relationships
            )
            
            if not exists:
                self.relationships.append({
                    'source': source_entity,
                    'target': target_entity,
                    'relation': relation,
                    'description': rel.get('description', ''),
                    'weight': rel.get('weight', 1)
                })
                new_relationships += 1
        
        # 保存
        self._save_graph()
        
        return new_entities, new_relationships
    
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
    
    def visualize_graph(self, max_nodes: int = 50) -> str:
        """生成可视化HTML"""
        # 限制节点数量
        entities_to_show = list(self.entities.items())[:max_nodes]
        
        # 构建nodes和edges
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
    <title>知识图谱 (LlamaIndex)</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/vis-network/9.1.2/standalone/umd/vis-network.min.js"></script>
    <style>
        #mynetwork {{
            width: 100%;
            height: 900px;
            border: 1px solid #ddd;
        }}
        body {{
            font-family: 'Microsoft YaHei', Arial, sans-serif;
            margin: 20px;
        }}
        h1 {{
            color: #333;
            font-size: 28px;
        }}
        .info {{
            background: #f0f0f0;
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 5px;
            font-size: 16px;
        }}
        .badge {{
            background: #4CAF50;
            color: white;
            padding: 5px 10px;
            border-radius: 3px;
            font-size: 12px;
            margin-left: 10px;
        }}
    </style>
</head>
<body>
    <h1>🧠 知识图谱可视化 <span class="badge">LlamaIndex</span></h1>
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
                size: 30,
                font: {{
                    size: 18,
                    color: '#000',
                    face: 'Microsoft YaHei, Arial'
                }},
                borderWidth: 2
            }},
            edges: {{
                arrows: 'to',
                smooth: true,
                width: 2,
                font: {{
                    size: 16,
                    align: 'middle',
                    color: '#666',
                    face: 'Microsoft YaHei, Arial'
                }}
            }},
            physics: {{
                enabled: true,
                barnesHut: {{
                    gravitationalConstant: -40000,
                    springLength: 200,
                    springConstant: 0.01
                }},
                stabilization: {{
                    iterations: 200
                }}
            }},
            groups: {{
                '概念': {{color: {{background: '#97C2FC', border: '#2B7CE9'}}}},
                '技术': {{color: {{background: '#FFCC99', border: '#FF9933'}}}},
                '术语': {{color: {{background: '#C2FABC', border: '#74D66A'}}}},
                '人物': {{color: {{background: '#FFC0CB', border: '#FF69B4'}}}},
                '组织': {{color: {{background: '#FFD700', border: '#FFA500'}}}},
                '地点': {{color: {{background: '#87CEEB', border: '#4682B4'}}}},
                '动作': {{color: {{background: '#DDA0DD', border: '#BA55D3'}}}}
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


if __name__ == "__main__":
    # 测试
    print("=" * 60)
    print("🧪 测试 LlamaIndex 知识图谱")
    print("=" * 60)
    
    kg = LlamaIndexKnowledgeGraph()
    
    test_text = """
    隐马尔可夫模型（HMM）是一种统计模型，用于描述一个含有隐含未知参数的马尔可夫过程。
    卷积神经网络（CNN）是深度学习的重要组成部分，特别适合处理图像识别任务。
    循环神经网络（RNN）用于处理序列数据，如文本和时间序列。
    Transformer架构革新了自然语言处理领域，引入了注意力机制。
    BERT模型由Google开发，使用双向编码器。
    GPT模型由OpenAI开发，使用自回归解码器。
    """
    
    print(f"\n📄 测试文本长度: {len(test_text)} 字符\n")
    
    num_e, num_r = kg.add_entities_and_relations(test_text, "测试文档")
    
    print(f"\n✅ 提取完成: {num_e}个新实体, {num_r}个新关系")
    print(f"\n📊 总计: {len(kg.entities)}个实体, {len(kg.relationships)}条关系")
    
    print(f"\n📝 提取的实体（按名称长度排序）：\n")
    entities_sorted = sorted(kg.entities.items(), key=lambda x: len(x[0]), reverse=True)
    for i, (name, info) in enumerate(entities_sorted[:15], 1):
        char_count = len(name)
        entity_type = info.get('type', '未知')
        mark = "✨" if char_count >= 5 else "  "
        print(f"   {mark} {i:2d}. {name} ({char_count}字) - {entity_type}")
    
    print(f"\n🔗 提取的关系（前10条）：\n")
    for i, rel in enumerate(kg.relationships[:10], 1):
        print(f"   {i:2d}. {rel['source']} --[{rel['relation']}]--> {rel['target']}")
    
    print("\n" + "=" * 60)
    print("💡 检查是否有完整的长实体（如'隐马尔可夫模型'）")
    print("=" * 60)

