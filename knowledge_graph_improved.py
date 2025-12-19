#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
改进的知识图谱系统
使用jieba的高级功能和词性标注
"""

import json
import re
from collections import Counter, defaultdict
from typing import List, Dict, Tuple, Set
from pathlib import Path
import jieba
import jieba.analyse
import jieba.posseg as pseg
from openai import OpenAI
from config import OPENAI_API_KEY, OPENAI_API_BASE, MODEL_NAME


class ImprovedKnowledgeGraph:
    """改进的知识图谱管理器"""
    
    def __init__(self, storage_file: str = "./knowledge_graph.json", model: str = MODEL_NAME):
        self.storage_file = Path(storage_file)
        self.client = OpenAI(api_key=OPENAI_API_KEY, base_url=OPENAI_API_BASE)
        self.model = model
        
        # 图数据结构
        self.entities: Dict[str, Dict] = {}  # {实体名: {type, properties}}
        self.relationships: List[Dict] = []  # [{source, target, relation, properties}]
        
        # 初始化jieba
        self._init_jieba()
        
        # 扩展的停用词表
        self.stopwords = self._load_stopwords()
        
        self._load_graph()
    
    def _init_jieba(self):
        """初始化jieba分词器"""
        # 启用并行分词（可选）
        # jieba.enable_parallel(4)
        
        # 添加自定义词典（可选，根据领域添加专业词汇）
        # jieba.load_userdict("custom_dict.txt")
        pass
    
    def _load_stopwords(self) -> Set[str]:
        """加载扩展的停用词表"""
        stopwords = {
            # 中文基础停用词
            '的', '了', '是', '在', '和', '有', '与', '等', '中', '对', '为', '都', 
            '可以', '这', '就', '也', '我', '你', '他', '她', '我们', '一个', '一些', 
            '这个', '那个', '什么', '怎么', '如何', '能够', '可能', '因此', '所以',
            '但是', '然后', '如果', '或者', '因为', '已经', '需要', '通过', '进行',
            '使用', '表示', '包括', '具有', '成为', '没有', '非常', '一般', '主要',
            
            # HTML/CSS/编程相关
            'span', 'div', 'class', 'style', 'html', 'body', 'table', 'thead', 'tbody',
            'colspan', 'rowspan', 'cellpadding', 'cellspacing', 'img', 'src', 'href',
            'width', 'height', 'border', 'padding', 'margin', 'align', 'valign',
            
            # 图片格式和文件扩展名
            'jpg', 'jpeg', 'png', 'gif', 'bmp', 'svg', 'webp', 'pdf', 'doc', 'docx',
            'ppt', 'pptx', 'xls', 'xlsx', 'txt', 'csv', 'xml', 'json', 'html', 'css',
            'images', 'image', 'img', 'pic', 'picture', 'photo', 'file', 'files',
            
            # LaTeX命令
            'mathbb', 'mathbf', 'mathit', 'mathrm', 'mathcal', 'mathfrak',
            'frac', 'sqrt', 'sum', 'int', 'prod', 'lim', 'infty', 'partial',
            'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'theta', 'lambda', 'sigma',
            'begin', 'end', 'left', 'right', 'cdot', 'times', 'equiv', 'approx',
            
            # 文档结构词
            'chapter', 'section', 'subsection', 'paragraph', 'figure', 'table',
            'caption', 'label', 'ref', 'cite', 'bibliography', 'footnote',
            '章节', '小节', '段落', '图表', '表格', '图片', '页', '页面', '内容',
            
            # 数字和单位（单独的）
            '年', '月', '日', '时', '分', '秒', '个', '位', '次', '度', '米', '千米',
            '克', '千克', '升', '毫升', '元', '块', '毛', '分',
        }
        
        return stopwords
    
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
    
    def extract_keywords_advanced(self, text: str, source: str = "", top_n: int = 15) -> Tuple[List[Dict], List[Dict]]:
        """
        使用jieba的高级功能提取关键词
        
        方法：
        1. 使用TextRank算法提取关键词
        2. 使用词性标注过滤无意义词
        3. 分析词语共现关系
        
        参数:
            text: 文本内容
            source: 来源
            top_n: 提取前N个关键词
        
        返回:
            (实体列表, 关系列表)
        """
        if not text or len(text) < 10:
            return [], []
        
        # 方法1: TextRank算法提取关键词（更准确）
        try:
            keywords_textrank = jieba.analyse.textrank(text, topK=top_n, withWeight=True)
        except:
            keywords_textrank = []
        
        # 方法2: TF-IDF算法提取关键词（作为补充）
        try:
            keywords_tfidf = jieba.analyse.extract_tags(text, topK=top_n, withWeight=True)
        except:
            keywords_tfidf = []
        
        # 合并两种方法的结果
        keyword_scores = defaultdict(float)
        for keyword, weight in keywords_textrank:
            keyword_scores[keyword] += weight * 0.6  # TextRank权重60%
        for keyword, weight in keywords_tfidf:
            keyword_scores[keyword] += weight * 0.4  # TF-IDF权重40%
        
        # 词性标注过滤
        filtered_keywords = []
        for keyword, score in keyword_scores.items():
            # 跳过停用词
            if keyword in self.stopwords:
                continue
            
            # 跳过单字词（通常不是好的关键词）
            if len(keyword) < 2:
                continue
            
            # 跳过纯数字和纯字母
            if re.match(r'^[\d\.]+$', keyword) or re.match(r'^[a-zA-Z]+$', keyword):
                continue
            
            # 跳过包含特殊字符的词
            if re.search(r'[<>{}()\[\]\\\/\|\"\']', keyword):
                continue
            
            # 进行词性标注
            words_pos = pseg.cut(keyword)
            for word, pos in words_pos:
                # 只保留名词(n)、动词(v)、形容词(a)、专有名词(ns/nr/nt)等
                if pos in ['n', 'nr', 'ns', 'nt', 'nz', 'v', 'vn', 'a', 'an', 'eng']:
                    filtered_keywords.append((keyword, score))
                    break
        
        # 排序并取前N个
        filtered_keywords.sort(key=lambda x: x[1], reverse=True)
        top_keywords = filtered_keywords[:top_n]
        
        # 构建实体列表
        entities = []
        for keyword, score in top_keywords:
            # 确定实体类型
            words_pos = list(pseg.cut(keyword))
            entity_type = self._determine_entity_type(words_pos)
            
            entities.append({
                'name': keyword,
                'type': entity_type,
                'description': f'重要度: {score:.3f}',
                'source': source,
                'score': score
            })
        
        # 构建关系（基于共现和句法分析）
        relationships = self._extract_relationships(text, top_keywords)
        
        return entities, relationships
    
    def _determine_entity_type(self, words_pos: List[Tuple[str, str]]) -> str:
        """根据词性判断实体类型"""
        if not words_pos:
            return '概念'
        
        pos = words_pos[0][1]
        
        if pos in ['nr', 'nrfg', 'nrt']:
            return '人物'
        elif pos in ['ns', 'nsf']:
            return '地点'
        elif pos in ['nt', 'ntc', 'ntcf']:
            return '组织'
        elif pos in ['n', 'nz']:
            return '概念'
        elif pos in ['v', 'vn']:
            return '动作'
        elif pos == 'eng':
            return '术语'
        else:
            return '关键词'
    
    def _extract_relationships(self, text: str, keywords: List[Tuple[str, float]]) -> List[Dict]:
        """提取关键词之间的关系"""
        relationships = []
        keyword_list = [kw for kw, _ in keywords[:10]]  # 只用前10个
        
        # 按句子分割
        sentences = re.split(r'[。！？；\n]+', text)
        sentences = [s.strip() for s in sentences if s.strip() and len(s.strip()) > 5]
        
        # 分析共现关系
        cooccurrence = defaultdict(int)
        for sentence in sentences:
            # 找出在当前句子中出现的关键词
            present_keywords = [kw for kw in keyword_list if kw in sentence]
            
            # 记录两两共现
            for i, kw1 in enumerate(present_keywords):
                for kw2 in present_keywords[i+1:]:
                    pair = tuple(sorted([kw1, kw2]))
                    cooccurrence[pair] += 1
        
        # 构建关系
        for (kw1, kw2), count in cooccurrence.items():
            if count > 0:  # 至少共现一次
                # 尝试判断关系类型
                relation_type = self._infer_relation_type(kw1, kw2, text)
                
                relationships.append({
                    'source': kw1,
                    'target': kw2,
                    'relation': relation_type,
                    'description': f'共现{count}次',
                    'weight': count
                })
        
        return relationships
    
    def _infer_relation_type(self, entity1: str, entity2: str, text: str) -> str:
        """尝试推断两个实体之间的关系类型"""
        # 在文本中查找包含两个实体的句子
        sentences = re.split(r'[。！？；\n]+', text)
        
        for sentence in sentences:
            if entity1 in sentence and entity2 in sentence:
                # 查找连接词
                if '包括' in sentence or '包含' in sentence:
                    return '包含'
                elif '属于' in sentence:
                    return '属于'
                elif '使用' in sentence or '采用' in sentence:
                    return '使用'
                elif '实现' in sentence or '完成' in sentence:
                    return '实现'
                elif '基于' in sentence or '依据' in sentence:
                    return '基于'
                elif '产生' in sentence or '生成' in sentence:
                    return '产生'
                elif '导致' in sentence or '引起' in sentence:
                    return '导致'
                elif '定义为' in sentence or '是' in sentence:
                    return '定义'
        
        return '相关'
    
    def extract_entities_and_relations(self, text: str, source: str = "", use_simple: bool = False, use_llm: bool = True) -> Tuple[List[Dict], List[Dict]]:
        """
        从文本中提取实体和关系
        
        参数:
            text: 文本内容
            source: 来源
            use_simple: 是否使用简单提取（默认False）
            use_llm: 是否使用LLM增强（默认True）
        
        返回:
            (实体列表, 关系列表)
        """
        if use_simple:
            # 降级到简单方法
            from knowledge_graph import KnowledgeGraph
            kg = KnowledgeGraph()
            return kg.extract_keywords_simple(text, source)
        
        # 先用统计方法提取基础实体
        entities_base, relations_base = self.extract_keywords_advanced(text, source)
        
        # 如果启用LLM，用LLM进行增强和优化
        if use_llm and len(text) > 50:
            try:
                print(f"🤖 使用LLM增强知识图谱提取...")
                entities_llm, relations_llm = self._extract_with_llm(text, source, entities_base)
                
                # 合并结果：LLM为主，统计方法补充
                entities_merged = self._merge_entities(entities_llm, entities_base)
                relations_merged = self._merge_relations(relations_llm, relations_base)
                
                return entities_merged, relations_merged
            except Exception as e:
                print(f"⚠️  LLM提取失败: {e}，使用统计方法结果")
                return entities_base, relations_base
        
        # 不使用LLM，直接返回统计方法的结果
        return entities_base, relations_base
    
    def _extract_with_llm(self, text: str, source: str, base_entities: List[Dict]) -> Tuple[List[Dict], List[Dict]]:
        """
        使用LLM提取实体和关系
        
        参数:
            text: 文本内容
            source: 来源
            base_entities: 统计方法提取的基础实体（作为参考）
        
        返回:
            (实体列表, 关系列表)
        """
        # 限制文本长度
        text_excerpt = text[:3000] if len(text) > 3000 else text
        
        # 准备基础实体列表作为参考
        base_entity_names = [e['name'] for e in base_entities[:15]]
        base_entities_str = "、".join(base_entity_names) if base_entity_names else "无"
        
        prompt = f"""请从以下文本中提取关键实体和它们之间的关系，构建专业的知识图谱。

文本内容：
{text_excerpt}

参考概念（可作为实体参考，但不限于此）：
{base_entities_str}

请以JSON格式返回：
{{
  "entities": [
    {{
      "name": "实体名称（必须完整，如'隐马尔可夫模型'而不是'马尔可夫'）",
      "type": "人物|地点|组织|概念|技术|术语|动作",
      "description": "简短描述（一句话）"
    }}
  ],
  "relationships": [
    {{
      "source": "源实体名称",
      "target": "目标实体名称",
      "relation": "包含|属于|使用|实现|基于|产生|导致|定义|相关",
      "description": "关系描述（一句话）"
    }}
  ]
}}

✅ 必须提取的实体：
- 完整的专业术语（如"隐马尔可夫模型"、"卷积神经网络"）
- 重要算法和技术（如"Transformer"、"BERT"）
- 核心概念（如"深度学习"、"自然语言处理"）
- 人名、组织名（如"Hinton"、"Google"）

❌ 不要提取的实体：
- 通用词汇（如"方法"、"系统"、"问题"）
- 不完整的词（如"马尔"、"可夫"）
- 单字词
- 动词、形容词（除非是专业术语的一部分）

要求：
1. 提取5-15个最重要的实体
2. 提取实体间的主要关系（5-20条）
3. 实体类型从给定的7种中选择
4. 关系类型从给定的9种中选择（尽量避免使用"相关"）
5. 只返回JSON，不要其他说明
6. 确保source和target都是entities中存在的实体名称
7. 实体名称必须完整且有意义
"""
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "你是一位知识图谱专家，擅长从文本中提取实体和关系，构建结构化的知识表示。"},
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
            
            # 添加来源信息和分数
            for entity in entities:
                entity['source'] = source
                entity['score'] = 0.8  # LLM提取的实体给予较高初始分数
            
            for rel in relationships:
                if 'weight' not in rel:
                    rel['weight'] = 2  # LLM识别的关系给予初始权重
            
            print(f"✅ LLM提取: {len(entities)}个实体, {len(relationships)}条关系")
            
            return entities, relationships
            
        except Exception as e:
            print(f"❌ LLM提取失败: {e}")
            raise
    
    def _merge_entities(self, entities_llm: List[Dict], entities_base: List[Dict]) -> List[Dict]:
        """
        合并LLM提取和统计方法提取的实体
        
        策略：
        - LLM提取的实体为主（质量更高）
        - 统计方法提取的高频实体作为补充
        - 去重（名称相同的只保留一个，取更高的分数）
        """
        entity_dict = {}
        
        # 先添加LLM提取的实体
        for entity in entities_llm:
            name = entity.get('name', '')
            if name:
                entity_dict[name] = entity
        
        # 补充统计方法的高分实体（如果不在LLM结果中）
        for entity in entities_base:
            name = entity.get('name', '')
            if name and name not in entity_dict:
                # 只添加分数较高的
                if entity.get('score', 0) > 0.5:
                    entity_dict[name] = entity
        
        merged = list(entity_dict.values())
        print(f"📊 实体合并: LLM({len(entities_llm)}) + 统计({len(entities_base)}) → {len(merged)}")
        
        return merged
    
    def _merge_relations(self, relations_llm: List[Dict], relations_base: List[Dict]) -> List[Dict]:
        """
        合并LLM提取和统计方法提取的关系
        
        策略：
        - LLM提取的关系为主（类型更准确）
        - 统计方法的共现关系作为补充
        - 去重（相同的source-target对只保留一个）
        """
        relation_dict = {}
        
        # 先添加LLM提取的关系
        for rel in relations_llm:
            source = rel.get('source', '')
            target = rel.get('target', '')
            if source and target:
                key = f"{source}||{target}"
                relation_dict[key] = rel
        
        # 补充统计方法的关系（如果不在LLM结果中）
        for rel in relations_base:
            source = rel.get('source', '')
            target = rel.get('target', '')
            if source and target:
                key = f"{source}||{target}"
                if key not in relation_dict:
                    # 只添加权重较高的
                    if rel.get('weight', 0) >= 2:
                        relation_dict[key] = rel
        
        merged = list(relation_dict.values())
        print(f"📊 关系合并: LLM({len(relations_llm)}) + 统计({len(relations_base)}) → {len(merged)}")
        
        return merged
    
    def add_to_graph(self, entities: List[Dict], relationships: List[Dict]):
        """将实体和关系添加到图中"""
        # 添加实体
        for entity in entities:
            name = entity.get('name', '')
            if not name:
                continue
            
            source = entity.get('source', '')
            score = entity.get('score', 1.0)
            
            if name not in self.entities:
                self.entities[name] = {
                    'type': entity.get('type', '关键词'),
                    'description': entity.get('description', ''),
                    'score': score,
                    'sources': [source] if source else []
                }
            else:
                # 更新分数（取平均）
                old_score = self.entities[name].get('score', 1.0)
                self.entities[name]['score'] = (old_score + score) / 2
                
                # 合并来源
                if source and source not in self.entities[name].get('sources', []):
                    if 'sources' not in self.entities[name]:
                        self.entities[name]['sources'] = []
                    self.entities[name]['sources'].append(source)
        
        # 添加关系
        for rel in relationships:
            source_entity = rel.get('source', '')
            target_entity = rel.get('target', '')
            
            if not source_entity or not target_entity:
                continue
            
            # 检查是否已存在相同关系
            exists = False
            for i, r in enumerate(self.relationships):
                if (r.get('source') == source_entity and 
                    r.get('target') == target_entity and 
                    r.get('relation') == rel.get('relation', '')):
                    # 更新权重
                    self.relationships[i]['weight'] = r.get('weight', 1) + rel.get('weight', 1)
                    exists = True
                    break
            
            if not exists:
                self.relationships.append({
                    'source': source_entity,
                    'target': target_entity,
                    'relation': rel.get('relation', '相关'),
                    'description': rel.get('description', ''),
                    'weight': rel.get('weight', 1)
                })
        
        # 保存图数据
        self._save_graph()
    
    def get_graph_data(self) -> Dict:
        """获取图数据（用于可视化）"""
        # 转换为可视化格式
        nodes = []
        for name, props in self.entities.items():
            nodes.append({
                'id': name,
                'label': name,
                'type': props.get('type', '关键词'),
                'score': props.get('score', 1.0),
                'sources_count': len(props.get('sources', []))
            })
        
        edges = []
        for rel in self.relationships:
            edges.append({
                'source': rel['source'],
                'target': rel['target'],
                'relation': rel.get('relation', '相关'),
                'weight': rel.get('weight', 1)
            })
        
        return {
            'nodes': nodes,
            'edges': edges,
            'stats': {
                'total_entities': len(self.entities),
                'total_relationships': len(self.relationships)
            }
        }
    
    def search_entity(self, query: str) -> List[Dict]:
        """搜索实体"""
        results = []
        query_lower = query.lower()
        
        for name, props in self.entities.items():
            if query_lower in name.lower():
                results.append({
                    'name': name,
                    **props
                })
        
        # 按分数排序
        results.sort(key=lambda x: x.get('score', 0), reverse=True)
        return results
    
    def get_related_entities(self, entity_name: str, max_depth: int = 2) -> Dict:
        """获取与指定实体相关的其他实体"""
        if entity_name not in self.entities:
            return {}
        
        related = {
            'entity': entity_name,
            'direct_relations': [],
            'indirect_relations': []
        }
        
        # 直接关系
        for rel in self.relationships:
            if rel['source'] == entity_name:
                related['direct_relations'].append({
                    'target': rel['target'],
                    'relation': rel['relation'],
                    'weight': rel.get('weight', 1)
                })
            elif rel['target'] == entity_name:
                related['direct_relations'].append({
                    'target': rel['source'],
                    'relation': f"被{rel['relation']}",
                    'weight': rel.get('weight', 1)
                })
        
        # 如果需要，可以扩展到间接关系
        if max_depth > 1:
            # TODO: 实现多跳关系查询
            pass
        
        return related


if __name__ == "__main__":
    # 测试代码
    print("=" * 60)
    print("🧪 测试改进的知识图谱系统")
    print("=" * 60)
    
    kg = ImprovedKnowledgeGraph()
    
    test_text = """
    深度学习是机器学习的一个分支，它使用神经网络来学习数据的表示。
    卷积神经网络（CNN）特别适合处理图像数据，能够自动提取特征。
    ResNet和VGG是著名的CNN架构，它们在ImageNet比赛中取得了突破性成果。
    循环神经网络（RNN）则用于处理序列数据，如文本和时间序列。
    Transformer架构革新了自然语言处理领域，引入了注意力机制。
    BERT和GPT是基于Transformer的著名模型，由Google和OpenAI分别开发。
    BERT使用双向编码器，而GPT使用自回归解码器。
    """
    
    print("\n" + "=" * 60)
    print("📊 方法1: 统计方法（jieba TextRank + TF-IDF）")
    print("=" * 60)
    entities_stat, relationships_stat = kg.extract_keywords_advanced(test_text, "测试文档")
    
    print(f"\n提取的实体（{len(entities_stat)}个）：")
    for entity in entities_stat[:10]:
        print(f"  ✅ {entity['name']} ({entity['type']}) - {entity['description']}")
    
    print(f"\n提取的关系（{len(relationships_stat)}条）：")
    for rel in relationships_stat[:10]:
        print(f"  ✅ {rel['source']} --[{rel['relation']}]--> {rel['target']}")
    
    print("\n" + "=" * 60)
    print("🤖 方法2: LLM增强（统计 + LLM优化）")
    print("=" * 60)
    entities_llm, relationships_llm = kg.extract_entities_and_relations(
        test_text, 
        "测试文档", 
        use_llm=True
    )
    
    print(f"\n提取的实体（{len(entities_llm)}个）：")
    for entity in entities_llm[:15]:
        print(f"  ✅ {entity['name']} ({entity['type']}) - {entity.get('description', 'N/A')}")
    
    print(f"\n提取的关系（{len(relationships_llm)}条）：")
    for rel in relationships_llm[:15]:
        print(f"  ✅ {rel['source']} --[{rel['relation']}]--> {rel['target']}")
        if rel.get('description'):
            print(f"      💡 {rel['description']}")
    
    # 添加到图中
    kg.add_to_graph(entities_llm, relationships_llm)
    
    print("\n" + "=" * 60)
    print("📈 对比总结")
    print("=" * 60)
    print(f"统计方法: {len(entities_stat)}个实体, {len(relationships_stat)}条关系")
    print(f"LLM增强:  {len(entities_llm)}个实体, {len(relationships_llm)}条关系")
    print("=" * 60)

