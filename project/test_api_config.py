#!/usr/bin/env python3
"""
PaddleX API配置测试脚本

这个脚本用于测试你的PaddleX API配置是否正确。

使用方法：
1. 设置环境变量：
   export PADDLEOCR_API_URL="你的API地址"
   export PADDLEOCR_API_TOKEN="你的TOKEN"

2. 运行脚本：
   python test_api_config.py
"""

import os
import sys
import base64
import requests

def main():
    print("=" * 60)
    print("🔍 PaddleX API配置测试")
    print("=" * 60)
    print()
    
    # 1. 检查环境变量
    print("📋 第1步：检查环境变量配置")
    print("-" * 60)
    
    API_URL = os.getenv('PADDLEOCR_API_URL', '')
    TOKEN = os.getenv('PADDLEOCR_API_TOKEN', '')
    
    if not API_URL:
        print("❌ PADDLEOCR_API_URL 未设置")
        print()
        print("请设置环境变量：")
        print("  export PADDLEOCR_API_URL='你的API地址'")
        print()
        return False
    else:
        print(f"✅ PADDLEOCR_API_URL: {API_URL}")
    
    if not TOKEN:
        print("❌ PADDLEOCR_API_TOKEN 未设置")
        print()
        print("请设置环境变量：")
        print("  export PADDLEOCR_API_TOKEN='你的TOKEN'")
        print()
        return False
    else:
        # 只显示TOKEN的前10个字符
        print(f"✅ PADDLEOCR_API_TOKEN: {TOKEN[:10]}... (已隐藏)")
    
    print()
    
    # 2. 检查URL格式
    print("📋 第2步：检查URL格式")
    print("-" * 60)
    
    # 检查是否包含必需的路径
    if '/layout-parsing' not in API_URL:
        print(f"⚠️  警告：URL可能不正确")
        print(f"   当前URL: {API_URL}")
        print(f"   正确格式应该包含: /layout-parsing")
        print(f"   例如: https://your-domain.com/layout-parsing")
        print()
    else:
        print(f"✅ URL格式看起来正确")
        print()
    
    # 检查是否是错误的千帆URL
    if 'qianfan.baidubce.com' in API_URL:
        print("❌ 错误：这是百度千帆的URL，不是PaddleX的URL！")
        print()
        print("你需要的是PaddleX PP-StructureV3的API，而不是千帆大模型。")
        print("请参考文档获取正确的API地址。")
        print()
        return False
    
    # 3. 测试连接
    print("📋 第3步：测试API连接")
    print("-" * 60)
    
    # 创建一个1x1像素的测试图片（PNG格式）
    # 这是一个最小的有效PNG图片
    test_image_base64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg=="
    
    headers = {
        "Authorization": f"token {TOKEN}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "file": test_image_base64,
        "fileType": 1,  # 1表示图像
        "useDocOrientationClassify": False,
        "useDocUnwarping": False,
        "useTextlineOrientation": False,
    }
    
    print(f"📤 发送测试请求到: {API_URL}")
    print("   (使用1x1像素测试图片)")
    print()
    
    try:
        response = requests.post(API_URL, json=payload, headers=headers, timeout=30)
        
        print(f"📥 收到响应")
        print(f"   状态码: {response.status_code}")
        print()
        
        if response.status_code == 200:
            print("✅ API连接成功！")
            print()
            
            try:
                result = response.json()
                if 'result' in result and 'layoutParsingResults' in result['result']:
                    print("✅ API响应格式正确！")
                    print()
                    print("🎉 恭喜！你的API配置完全正确，可以正常使用了！")
                    print()
                    return True
                else:
                    print("⚠️  警告：API响应格式不符合预期")
                    print(f"   响应内容: {result}")
                    print()
            except Exception as e:
                print(f"⚠️  警告：解析响应失败: {e}")
                print()
        
        elif response.status_code == 401:
            print("❌ 认证失败 (401)")
            print()
            print("可能的原因：")
            print("1. TOKEN不正确")
            print("2. TOKEN已过期")
            print("3. TOKEN没有访问权限")
            print()
            print("请检查你的TOKEN是否正确。")
            print()
            return False
        
        elif response.status_code == 404:
            print("❌ 资源未找到 (404)")
            print()
            print("可能的原因：")
            print("1. API_URL不正确")
            print("2. 服务未部署或已下线")
            print()
            print(f"当前URL: {API_URL}")
            print()
            try:
                error_msg = response.json()
                print(f"错误详情: {error_msg}")
            except:
                print(f"响应内容: {response.text}")
            print()
            return False
        
        else:
            print(f"❌ 请求失败 ({response.status_code})")
            print()
            try:
                error_msg = response.json()
                print(f"错误信息: {error_msg}")
            except:
                print(f"响应内容: {response.text}")
            print()
            return False
    
    except requests.exceptions.Timeout:
        print("❌ 请求超时")
        print()
        print("可能的原因：")
        print("1. 网络连接不稳定")
        print("2. API服务响应慢")
        print("3. URL不正确")
        print()
        return False
    
    except requests.exceptions.ConnectionError as e:
        print("❌ 连接失败")
        print()
        print(f"错误详情: {e}")
        print()
        print("可能的原因：")
        print("1. 网络连接问题")
        print("2. URL不正确")
        print("3. 防火墙阻止")
        print()
        return False
    
    except Exception as e:
        print(f"❌ 未知错误: {e}")
        print()
        return False


if __name__ == '__main__':
    print()
    success = main()
    print("=" * 60)
    
    if success:
        print("✅ 测试通过！")
        print()
        print("下一步：")
        print("  python run_competition.py")
        print()
        sys.exit(0)
    else:
        print("❌ 测试失败")
        print()
        print("下一步：")
        print("1. 检查API配置是否正确")
        print("2. 参考文档: 使用在线API.md")
        print("3. 或者使用本地模式（功能受限）：")
        print("   unset PADDLEOCR_API_URL")
        print("   unset PADDLEOCR_API_TOKEN")
        print("   python run_competition.py")
        print()
        sys.exit(1)




