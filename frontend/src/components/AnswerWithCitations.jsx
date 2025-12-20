/**
 * 带引用的答案组件
 * 解析<cite>标签并使其可点击
 */

import React from 'react';
import ReactMarkdown from 'react-markdown';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import 'katex/dist/katex.min.css'; // 导入KaTeX样式
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { vscDarkPlus } from 'react-syntax-highlighter/dist/esm/styles/prism';
import { FileText } from 'lucide-react';

const AnswerWithCitations = ({ content, onCitationClick }) => {
  // 解析<cite>标签
  const parseCitations = (text) => {
    const parts = [];
    const regex = /<cite id="([^"]+)">([^<]+)<\/cite>/g;
    let lastIndex = 0;
    let match;

    while ((match = regex.exec(text)) !== null) {
      // 添加cite标签之前的文本
      if (match.index > lastIndex) {
        parts.push({
          type: 'text',
          content: text.substring(lastIndex, match.index)
        });
      }

      // 添加cite标签
      parts.push({
        type: 'citation',
        id: match[1],
        content: match[2]
      });

      lastIndex = regex.lastIndex;
    }

    // 添加剩余文本
    if (lastIndex < text.length) {
      parts.push({
        type: 'text',
        content: text.substring(lastIndex)
      });
    }

    return parts.length > 0 ? parts : [{ type: 'text', content: text }];
  };

  const parts = parseCitations(content);

  // 如果没有cite标签，直接使用ReactMarkdown渲染
  if (parts.length === 1 && parts[0].type === 'text') {
    return (
      <div className="markdown-content prose prose-sm max-w-none">
        <ReactMarkdown
          remarkPlugins={[[remarkMath, { singleDollarTextMath: false }]]}
          rehypePlugins={[rehypeKatex]}
          components={{
            code({ node, inline, className, children, ...props }) {
              const match = /language-(\w+)/.exec(className || '');
              return !inline && match ? (
                <SyntaxHighlighter
                  style={vscDarkPlus}
                  language={match[1]}
                  PreTag="div"
                  {...props}
                >
                  {String(children).replace(/\n$/, '')}
                </SyntaxHighlighter>
              ) : (
                <code className={className} {...props}>
                  {children}
                </code>
              );
            },
          }}
        >
          {content}
        </ReactMarkdown>
      </div>
    );
  }

  // 有cite标签，需要特殊处理
  return (
    <div className="markdown-content prose prose-sm max-w-none">
      {parts.map((part, index) => {
        if (part.type === 'text') {
          return (
            <ReactMarkdown
              key={index}
              remarkPlugins={[[remarkMath, { singleDollarTextMath: false }]]}
              rehypePlugins={[rehypeKatex]}
              components={{
                code({ node, inline, className, children, ...props }) {
                  const match = /language-(\w+)/.exec(className || '');
                  return !inline && match ? (
                    <SyntaxHighlighter
                      style={vscDarkPlus}
                      language={match[1]}
                      PreTag="div"
                      {...props}
                    >
                      {String(children).replace(/\n$/, '')}
                    </SyntaxHighlighter>
                  ) : (
                    <code className={className} {...props}>
                      {children}
                    </code>
                  );
                },
              }}
            >
              {part.content}
            </ReactMarkdown>
          );
        } else if (part.type === 'citation') {
          // 可点击的引用
          return (
            <button
              key={index}
              onClick={() => onCitationClick && onCitationClick(part.id)}
              className="inline-flex items-center gap-1 px-2 py-0.5 mx-0.5 bg-google-blue-50 
                       hover:bg-google-blue-100 text-google-blue-700 rounded border border-google-blue-200 
                       hover:border-google-blue-400 transition-all text-sm font-medium cursor-pointer
                       hover:shadow-sm"
              title={`点击查看来源: ${part.id}`}
            >
              <FileText size={12} />
              <span>{part.content}</span>
            </button>
          );
        }
        return null;
      })}
    </div>
  );
};

export default AnswerWithCitations;



