#!/bin/bash
# 快速验证YZY融合功能

echo "🚀 YZY功能融合验证脚本"
echo "============================================================"
echo ""

cd /home/honglianglu/hdd/rag-agent

# 颜色定义
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo "📋 检查项目列表："
echo ""

# 1. 检查高级评估器文件
echo -n "1️⃣  检查 quality_evaluator_advanced.py ... "
if [ -f "quality_evaluator_advanced.py" ]; then
    echo -e "${GREEN}✅ 存在${NC}"
else
    echo -e "${RED}❌ 不存在${NC}"
fi

# 2. 检查配置文件中的BGE Reranker
echo -n "2️⃣  检查 BGE Reranker 配置 ... "
if grep -q "bge-reranker-v2-m3" config.py; then
    echo -e "${GREEN}✅ 已配置${NC}"
else
    echo -e "${RED}❌ 未配置${NC}"
fi

# 3. 检查RRF融合函数
echo -n "3️⃣  检查 RRF 融合实现 ... "
if grep -q "_rrf_fusion" rag_agent.py; then
    echo -e "${GREEN}✅ 已实现${NC}"
else
    echo -e "${RED}❌ 未实现${NC}"
fi

# 4. 检查SOTA检索函数
echo -n "4️⃣  检查 SOTA 检索实现 ... "
if grep -q "retrieve_context_sota" rag_agent.py; then
    echo -e "${GREEN}✅ 已实现${NC}"
else
    echo -e "${RED}❌ 未实现${NC}"
fi

# 5. 检查BM25搜索
echo -n "5️⃣  检查 BM25 搜索实现 ... "
if grep -q "search_bm25" vector_store.py; then
    echo -e "${GREEN}✅ 已实现${NC}"
else
    echo -e "${RED}❌ 未实现${NC}"
fi

# 6. 检查backend/api.py是否使用新评估器
echo -n "6️⃣  检查 backend/api.py 集成 ... "
if grep -q "AdvancedQualityEvaluator" backend/api.py; then
    echo -e "${GREEN}✅ 已集成${NC}"
else
    echo -e "${YELLOW}⚠️  使用旧版评估器${NC}"
fi

# 7. 检查前端recharts依赖
echo -n "7️⃣  检查 recharts 依赖 ... "
if [ -f "frontend/package.json" ]; then
    if grep -q "recharts" frontend/package.json; then
        echo -e "${GREEN}✅ 已添加${NC}"
        
        # 检查是否已安装
        echo -n "    检查是否已安装 ... "
        if [ -d "frontend/node_modules/recharts" ]; then
            echo -e "${GREEN}✅ 已安装${NC}"
        else
            echo -e "${YELLOW}⚠️  未安装（需要运行 npm install）${NC}"
        fi
    else
        echo -e "${RED}❌ 未添加到 package.json${NC}"
    fi
else
    echo -e "${RED}❌ package.json 不存在${NC}"
fi

echo ""
echo "============================================================"
echo ""

# Python依赖检查
echo "📦 Python依赖检查："
echo ""

echo -n "  • deepeval ... "
python3 -c "import deepeval" 2>/dev/null && echo -e "${GREEN}✅ 已安装${NC}" || echo -e "${YELLOW}⚠️  未安装（可选）${NC}"

echo -n "  • jieba ... "
python3 -c "import jieba" 2>/dev/null && echo -e "${GREEN}✅ 已安装${NC}" || echo -e "${RED}❌ 未安装${NC}"

echo -n "  • rank_bm25 ... "
python3 -c "import rank_bm25" 2>/dev/null && echo -e "${GREEN}✅ 已安装${NC}" || echo -e "${RED}❌ 未安装${NC}"

echo -n "  • chromadb ... "
python3 -c "import chromadb" 2>/dev/null && echo -e "${GREEN}✅ 已安装${NC}" || echo -e "${RED}❌ 未安装${NC}"

echo -n "  • openai ... "
python3 -c "import openai" 2>/dev/null && echo -e "${GREEN}✅ 已安装${NC}" || echo -e "${RED}❌ 未安装${NC}"

echo ""
echo "============================================================"
echo ""

# 功能说明
echo "📚 功能清单："
echo ""
echo "✅ DeepEval质量评估（3个指标）"
echo "   ├─ Faithfulness (忠实度)"
echo "   ├─ Answer Relevancy (切题度)"
echo "   └─ Contextual Relevancy (检索质量)"
echo ""
echo "✅ SOTA检索架构"
echo "   ├─ Query Expansion (查询扩展)"
echo "   ├─ Parallel Search (Vector + BM25)"
echo "   ├─ RRF Fusion (倒数排名融合)"
echo "   └─ BGE Reranker (精排)"
echo ""
echo "✅ 前端可视化"
echo "   ├─ 实时检索结果显示"
echo "   ├─ 雷达图质量评估"
echo "   ├─ 可点击引用跳转"
echo "   └─ 文档查看器"
echo ""
echo "============================================================"
echo ""

# 下一步提示
echo "🎯 下一步操作："
echo ""

# 检查是否需要安装前端依赖
if [ ! -d "frontend/node_modules/recharts" ] && grep -q "recharts" frontend/package.json 2>/dev/null; then
    echo "1️⃣  安装前端依赖："
    echo "   cd frontend && npm install"
    echo ""
fi

# 检查是否需要安装Python依赖
need_python_deps=false
python3 -c "import deepeval" 2>/dev/null || need_python_deps=true

if [ "$need_python_deps" = true ]; then
    echo "2️⃣  安装Python依赖（可选，用于DeepEval评估）："
    echo "   pip install deepeval"
    echo ""
fi

echo "3️⃣  启动系统："
echo "   # 终端1 - 启动后端"
echo "   cd /home/honglianglu/hdd/rag-agent"
echo "   ./start_backend.sh"
echo ""
echo "   # 终端2 - 启动前端"
echo "   cd /home/honglianglu/hdd/rag-agent"
echo "   ./start_frontend.sh"
echo ""

echo "4️⃣  测试功能："
echo "   • 上传文档到知识库"
echo "   • 提问并观察："
echo "     - 检索过程（SOTA架构）"
echo "     - 质量评估（雷达图）"
echo "     - 引用跳转"
echo ""

echo "============================================================"
echo "✨ 验证完成！"
echo "============================================================"

