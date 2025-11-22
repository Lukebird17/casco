#!/bin/bash
# 一键运行脚本

set -e  # 遇到错误立即退出

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 打印带颜色的消息
print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# 显示标题
show_banner() {
    echo -e "${BLUE}"
    echo "======================================"
    echo "   RAG 问答智能体 - 一键启动"
    echo "======================================"
    echo -e "${NC}"
}

# 检查 Python
check_python() {
    print_info "检查 Python 环境..."
    if ! command -v python3 &> /dev/null; then
        print_error "未找到 Python3，请先安装 Python 3.8+"
        exit 1
    fi
    python_version=$(python3 --version)
    print_success "Python 已安装: $python_version"
}

# 检查环境变量
check_env() {
    print_info "检查环境变量..."
    
    if [ -f "env.sh" ]; then
        print_success "找到 env.sh 配置文件"
        source env.sh
        return 0
    fi
    
    if [ -z "$CLOUD_API_KEY" ] || [ -z "$OPENAI_API_KEY" ]; then
        print_warning "未找到环境变量配置"
        echo ""
        echo "请选择配置方式："
        echo "1. 创建 env.sh 配置文件（推荐）"
        echo "2. 跳过（如果已在其他地方配置）"
        echo "3. 退出"
        read -p "请选择 (1/2/3): " choice
        
        case $choice in
            1)
                if [ ! -f "env_example.sh" ]; then
                    print_error "找不到 env_example.sh 模板文件"
                    exit 1
                fi
                cp env_example.sh env.sh
                print_info "已创建 env.sh，请编辑此文件填入您的配置"
                print_info "编辑完成后重新运行此脚本"
                exit 0
                ;;
            2)
                print_warning "跳过环境变量检查"
                ;;
            3)
                print_info "退出"
                exit 0
                ;;
            *)
                print_error "无效的选择"
                exit 1
                ;;
        esac
    else
        print_success "环境变量已配置"
    fi
}

# 检查依赖
check_dependencies() {
    print_info "检查依赖..."
    
    python3 -c "import raganything" 2>/dev/null
    if [ $? -ne 0 ]; then
        print_warning "RAG-Anything 未安装"
        echo ""
        echo "是否现在安装依赖？(y/n)"
        read -p "选择: " install_choice
        
        if [ "$install_choice" == "y" ] || [ "$install_choice" == "Y" ]; then
            print_info "开始安装依赖..."
            if [ -f "install_dependencies.sh" ]; then
                chmod +x install_dependencies.sh
                ./install_dependencies.sh
                print_success "依赖安装完成"
            else
                print_error "找不到 install_dependencies.sh"
                exit 1
            fi
        else
            print_warning "跳过依赖安装"
        fi
    else
        print_success "依赖已安装"
    fi
}

# 显示菜单
show_menu() {
    echo ""
    echo "请选择运行模式："
    echo ""
    echo "1. 🔍 环境检查"
    echo "2. 🚀 快速启动（交互式）"
    echo "3. 📝 运行示例程序"
    echo "4. ⭐ 运行完整流程（主程序）"
    echo "5. 📖 查看文档"
    echo "0. 退出"
    echo ""
}

# 环境检查
run_env_check() {
    print_info "运行环境检查..."
    python3 check_environment.py
}

# 快速启动
run_quick_start() {
    print_info "启动快速启动程序..."
    python3 quick_start.py
}

# 运行示例
run_example() {
    print_info "运行示例程序..."
    python3 simple_qa_example.py
}

# 运行主程序
run_main() {
    print_info "运行主程序..."
    python3 rag_qa_agent.py
}

# 查看文档
view_docs() {
    echo ""
    echo "可用的文档："
    echo ""
    echo "1. README.md - 项目入口文档"
    echo "2. 使用说明.md - 完整使用指南（推荐）"
    echo "3. README_RAG_QA.md - 详细 API 文档"
    echo "4. PROJECT_SUMMARY.md - 项目总结"
    echo "0. 返回"
    echo ""
    read -p "请选择要查看的文档 (0-4): " doc_choice
    
    case $doc_choice in
        1) less README.md 2>/dev/null || cat README.md ;;
        2) less 使用说明.md 2>/dev/null || cat 使用说明.md ;;
        3) less README_RAG_QA.md 2>/dev/null || cat README_RAG_QA.md ;;
        4) less PROJECT_SUMMARY.md 2>/dev/null || cat PROJECT_SUMMARY.md ;;
        0) return ;;
        *) print_error "无效的选择" ;;
    esac
}

# 主函数
main() {
    # 显示标题
    show_banner
    
    # 检查 Python
    check_python
    
    # 检查环境变量
    check_env
    
    # 检查依赖
    check_dependencies
    
    # 主循环
    while true; do
        show_menu
        read -p "请选择 (0-5): " choice
        
        case $choice in
            1)
                run_env_check
                ;;
            2)
                run_quick_start
                ;;
            3)
                run_example
                ;;
            4)
                run_main
                ;;
            5)
                view_docs
                ;;
            0)
                print_success "再见！"
                exit 0
                ;;
            *)
                print_error "无效的选择，请重试"
                ;;
        esac
        
        echo ""
        read -p "按 Enter 继续..."
    done
}

# 运行主函数
main

