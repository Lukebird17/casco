"""
图片描述生成器
使用多模态大模型为图片生成简洁、准确的描述
"""

import os
import base64
from typing import Dict, List, Optional
from PIL import Image
from openai import OpenAI

from config import OPENAI_API_KEY, OPENAI_API_BASE, MULTIMODAL_MODEL_NAME


class ImageDescriber:
    """使用多模态大模型生成图片描述"""
    
    def __init__(self, api_key: str = OPENAI_API_KEY, api_base: str = OPENAI_API_BASE):
        self.client = OpenAI(api_key=api_key, base_url=api_base)
        self.model = MULTIMODAL_MODEL_NAME
        
    def encode_image_to_base64(self, image_path: str) -> str:
        """将图片编码为base64"""
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    
    def describe_image(self, image_path: str, context: str = "") -> str:
        """
        为图片生成简洁描述
        
        Args:
            image_path: 图片路径
            context: 图片上下文（如周围文字）
            
        Returns:
            简洁的图片描述（50-150字）
        """
        try:
            # 读取图片
            image = Image.open(image_path)
            
            # 转换为base64
            base64_image = self.encode_image_to_base64(image_path)
            
            # 构建prompt
            system_prompt = """你是一个专业的图片描述生成器。请为提供的图片生成简洁、准确的描述。

要求：
1. 描述长度：50-150字
2. 客观准确：只描述看到的内容，不要添加推测或想象
3. 重点突出：优先描述关键信息（如图表数据、公式、架构图的核心概念）
4. 避免幻觉：如果看不清楚某个细节，不要编造
5. 结构化：如果是图表，说明类型和主要数据；如果是架构图，说明主要组件和关系
6. 学术风格：使用专业术语，适合用于学术文档"""
            
            user_prompt = "请为这张图片生成简洁准确的描述。"
            if context:
                user_prompt += f"\n\n图片上下文（周围文字）：\n{context[:200]}"
            
            # 调用多模态模型
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": user_prompt},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{base64_image}"
                                }
                            }
                        ]
                    }
                ],
                temperature=0.3,  # 低温度，减少幻觉
                max_tokens=300    # 限制长度
            )
            
            description = response.choices[0].message.content.strip()
            
            # 验证描述长度（防止太长被截断）
            if len(description) > 200:
                print(f"   ⚠️  描述过长({len(description)}字)，截断到150字")
                description = description[:150] + "..."
            
            return description
            
        except Exception as e:
            print(f"   ❌ 图片描述生成失败: {e}")
            # 返回基础描述
            return f"[图片：{os.path.basename(image_path)}]"
    
    def batch_describe_images(self, images_info: List[Dict], max_workers: int = 3) -> List[Dict]:
        """
        批量为图片生成描述
        
        Args:
            images_info: 图片信息列表，包含 image_path, context 等字段
            max_workers: 最大并发数
            
        Returns:
            更新后的图片信息列表（添加 description 字段）
        """
        from concurrent.futures import ThreadPoolExecutor, as_completed
        
        print(f"\n📝 开始为 {len(images_info)} 张图片生成描述...")
        
        def process_single_image(img_info: Dict, idx: int) -> Dict:
            """处理单张图片"""
            try:
                image_path = img_info.get('image_path')
                context = img_info.get('context', '')
                
                if not image_path or not os.path.exists(image_path):
                    print(f"   [{idx+1}/{len(images_info)}] ⚠️  图片不存在: {image_path}")
                    img_info['description'] = "[图片缺失]"
                    return img_info
                
                print(f"   [{idx+1}/{len(images_info)}] 🖼️  处理: {os.path.basename(image_path)}")
                description = self.describe_image(image_path, context)
                img_info['description'] = description
                print(f"   [{idx+1}/{len(images_info)}] ✅ 完成: {description[:50]}...")
                
            except Exception as e:
                print(f"   [{idx+1}/{len(images_info)}] ❌ 失败: {e}")
                img_info['description'] = f"[图片：{os.path.basename(image_path)}]"
            
            return img_info
        
        # 使用线程池并发处理
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {
                executor.submit(process_single_image, img_info, idx): idx
                for idx, img_info in enumerate(images_info)
            }
            
            results = []
            for future in as_completed(futures):
                try:
                    result = future.result()
                    results.append(result)
                except Exception as e:
                    print(f"   ❌ 任务执行失败: {e}")
        
        # 按原始顺序排序
        results.sort(key=lambda x: images_info.index(x) if x in images_info else 999)
        
        print(f"✅ 图片描述生成完成！")
        return results


if __name__ == "__main__":
    # 测试
    describer = ImageDescriber()
    
    # 测试单张图片
    test_image = "data/images/test.png"
    if os.path.exists(test_image):
        desc = describer.describe_image(test_image)
        print(f"描述: {desc}")


