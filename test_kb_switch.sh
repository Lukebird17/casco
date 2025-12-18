#!/bin/bash

echo "================================================"
echo "🧪 测试知识库切换功能"
echo "================================================"
echo ""

BASE_URL="http://localhost:8000"

echo "1️⃣ 测试获取知识库列表..."
echo ""
curl -s "$BASE_URL/api/knowledge-bases" | python3 -m json.tool
echo ""
echo ""

echo "2️⃣ 测试创建新知识库 'test_kb'..."
echo ""
curl -X POST -s "$BASE_URL/api/knowledge-bases" \
  -H "Content-Type: application/json" \
  -d '{"name": "test_kb"}' | python3 -m json.tool
echo ""
echo ""

echo "3️⃣ 再次获取知识库列表（应该包含test_kb）..."
echo ""
curl -s "$BASE_URL/api/knowledge-bases" | python3 -m json.tool
echo ""
echo ""

echo "4️⃣ 测试切换到test_kb..."
echo ""
curl -X POST -s "$BASE_URL/api/knowledge-bases/test_kb/switch" | python3 -m json.tool
echo ""
echo ""

echo "5️⃣ 测试切换回default..."
echo ""
curl -X POST -s "$BASE_URL/api/knowledge-bases/default/switch" | python3 -m json.tool
echo ""
echo ""

echo "6️⃣ 检查文件系统结构..."
echo ""
echo "data/ 目录："
ls -lh /home/honglianglu/hdd/rag-agent/data/ 2>/dev/null || echo "  (不存在)"
echo ""
echo "data/default/ 文件："
ls -lh /home/honglianglu/hdd/rag-agent/data/default/ 2>/dev/null || echo "  (不存在)"
echo ""
echo "data/test_kb/ 文件："
ls -lh /home/honglianglu/hdd/rag-agent/data/test_kb/ 2>/dev/null || echo "  (不存在)"
echo ""
echo "vector_db/ 目录："
ls -lh /home/honglianglu/hdd/rag-agent/vector_db/ 2>/dev/null || echo "  (不存在)"
echo ""

echo "================================================"
echo "✅ 测试完成！"
echo "================================================"
echo ""
echo "💡 如果看到错误，请检查："
echo "   1. 后端是否正在运行（./start_backend.sh）"
echo "   2. 后端日志输出"
echo "   3. vector_db/test_kb/ 目录是否创建成功"
echo ""



