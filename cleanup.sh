#!/bin/bash

# 🧹 OmniScry 仓库清理脚本
# 清理不必要的临时文件、备份文件和过时的文档

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "       🧹 OmniScry 仓库清理工具"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

cd /home/honglianglu/hdd/rag-agent

# 1. 删除过时的app文件
echo "📦 清理过时的应用文件..."
rm -f app_*.py app.py main.py 2>/dev/null
echo "✅ 清理完成"

# 2. 删除临时测试文件
echo "🧪 清理测试文件..."
rm -f test_*.py quick_test.py rebuild_kg.py process_data.py 2>/dev/null
echo "✅ 清理完成"

# 3. 删除过时的文档（保留重要的）
echo "📄 清理过时文档..."
rm -f \
    ALL_PANELS_UPDATED.md \
    BUG_FIX.md \
    CLEAN_LAYOUT_REDESIGN.md \
    CLEAR_BROWSER_CACHE.md \
    CLIP_MODEL_GUIDE.md \
    DEEPEVAL_DEADLOCK_DEBUG.md \
    DEEPEVAL_DEBUG_GUIDE.md \
    DEEPEVAL_FINAL_SUMMARY.md \
    FIX_*.md \
    IMPORT_FIX.md \
    KB_AND_UPLOAD_FIX.md \
    KG_*.md \
    LATEST_FIXES.md \
    LLM_ENHANCED_CONCEPTS.md \
    LOGO_DESIGN_UNIVERSE.md \
    MERGE_SUMMARY.md \
    OUTLINE_CONCEPT_*.md \
    QUALITY_METRICS_*.md \
    QUICK_*.md \
    QUIZ_FIX.md \
    README_*.md \
    REGENERATE_KG_GUIDE.md \
    SIGNAL_ERROR_FIX.md \
    SOCRATIC_MODE_EXPLAINED.md \
    TEST_*.md \
    TOOL_PANEL_TOGGLE_FIX.md \
    TWO_COLUMN_IMPROVEMENTS.md \
    UI_FIXES.md \
    URGENT_FIXES.md \
    UX_*.md \
    YZY_*.md \
    Z_INDEX_FIX.md \
    *最新*.md \
    *最终*.md \
    *前后端*.md \
    *功能*.md \
    *参数*.md \
    *向量库*.md \
    *启动*.md \
    *多模态*.md \
    *安装*.md \
    *完整*.md \
    *当前*.md \
    *快速*.md \
    *文档查看*.md \
    *新功能*.md \
    *无sudo*.md \
    *查询处理*.md \
    *现代化*.md \
    *目录结构*.md \
    *知识库*.md \
    *统一*.md \
    *重构*.md \
    *页码*.md \
    *项目文件*.md \
    *高级*.md \
    Gemini风格UI说明.md \
    MinerU*.md \
    RAGAgent参数说明.md \
    React前端*.md \
    UI*.md \
    LibreOffice*.md \
    2>/dev/null
echo "✅ 清理完成"

# 4. 删除临时脚本
echo "📜 清理临时脚本..."
rm -f \
    clear_kg_cache.sh \
    fix_directory_structure.sh \
    install_*.sh \
    migrate_to_new_structure.sh \
    setup_*.sh \
    stop_dev.sh \
    verify_*.sh \
    安装*.sh \
    2>/dev/null
echo "✅ 清理完成"

# 5. 删除临时Python文件
echo "🐍 清理临时Python文件..."
rm -f \
    auto_cot_*.py \
    demo_acceleration.py \
    document_heatmap.py \
    document_viewer.py \
    dynamic_db_manager.py \
    enhanced_*.py \
    hybrid_retriever.py \
    image_vector_store.py \
    quality_evaluator.py \
    reasoning_chain.py \
    snippet_manager.py \
    token_tracker.py \
    knowledge_graph.py \
    knowledge_graph_improved.py \
    knowledge_graph_llamaindex.py \
    2>/dev/null
echo "✅ 清理完成"

# 6. 删除备份目录和临时目录
echo "📁 清理备份和临时目录..."
rm -rf data_backup/ vector_db_backup/ vector_db_nlp/ output/ intermediate_data/ assets/ 2>/dev/null
echo "✅ 清理完成"

# 7. 删除临时文件
echo "🗑️  清理其他临时文件..."
rm -f \
    =0.1.0 =0.9.0 \
    auto_cot_demos.json \
    vector_db_metadata.json \
    backend.log \
    backend_new.log \
    LibreOffice*.tar.gz \
    2>/dev/null
echo "✅ 清理完成"

# 8. 清理Python缓存
echo "🧹 清理Python缓存..."
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
find . -type f -name "*.pyc" -delete 2>/dev/null
find . -type f -name "*.pyo" -delete 2>/dev/null
echo "✅ 清理完成"

# 9. 显示保留的重要文件
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "       ✅ 清理完成！"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📦 保留的重要文件："
echo "   - README.md                      (主文档)"
echo "   - INSTALLATION_GUIDE.md          (安装指南)"
echo "   - PROJECT_BRANDING.md            (品牌指南)"
echo "   - PERFORMANCE_OPTIMIZATION.md    (性能优化)"
echo "   - DEEPEVAL_IMPLEMENTATION.md     (DeepEval实现)"
echo "   - SOTA_RETRIEVAL_ENABLED.md      (SOTA检索)"
echo "   - QUIZ_COMPLETE_FIX.md          (智能出题修复)"
echo "   - FINAL_UPDATE_SUMMARY.md        (最终更新总结)"
echo "   - BRANDING_UPDATE_SUMMARY.md     (品牌更新)"
echo ""
echo "📂 保留的重要目录："
echo "   - backend/           (后端代码)"
echo "   - frontend/          (前端代码)"
echo "   - data/              (知识库数据)"
echo "   - vectordb/          (向量数据库)"
echo "   - sessions/          (会话历史)"
echo "   - static/            (静态文件)"
echo ""
echo "🚀 现在可以运行: ./start.sh"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

