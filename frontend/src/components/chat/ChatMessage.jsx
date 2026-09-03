import { useState } from "react";
import ReactMarkdown from "react-markdown";

const ChatMessage = ({ message }) => {
  const isUser = message.role === "user";

  const [copied, setCopied] = useState(false);

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(message.content);

      setCopied(true);

      setTimeout(() => {
        setCopied(false);
      }, 1500);
    } catch (error) {
      console.error("Failed to copy message:", error);
    }
  };

  return (
    <div
      className={`group flex w-full items-end gap-2 ${
    isUser ? "justify-end" : "justify-start"
} `}
    >
      {/* Assistant Avatar */}
      {!isUser && (
        <div className="mb-1 flex h-8 w-8 shrink-0 items-center justify-center rounded-full border border-slate-700 bg-slate-900 text-sm text-blue-400 shadow-sm">
          ✦
        </div>
      )}

      {/* Message + Actions */}
      <div
        className={`flex max-w-[85%] flex-col gap-2 sm:max-w-[75%] ${
    isUser ? "items-end" : "items-start"
} `}
      >
        {/* Message Bubble */}
        <div
          className={`w-fit px-4 py-3 text-sm leading-6 shadow-sm transition-colors duration-200 ${
    isUser
        ? "rounded-2xl rounded-br-md bg-white text-slate-950"
        : "rounded-2xl rounded-bl-md border border-slate-800 bg-slate-900/90 text-slate-300"
} `}
        >
          {isUser ? (
            <div className="whitespace-pre-wrap break-words">
              {message.content}
            </div>
          ) : (
            <div className="break-words">
              <ReactMarkdown
                components={{
                  p: ({ children }) => (
                    <p className="mb-3 last:mb-0">
                      {children}
                    </p>
                  ),

                  strong: ({ children }) => (
                    <strong className="font-semibold text-white">
                      {children}
                    </strong>
                  ),

                  em: ({ children }) => (
                    <em className="italic text-slate-200">
                      {children}
                    </em>
                  ),

                  ul: ({ children }) => (
                    <ul className="my-3 list-disc space-y-1.5 pl-5">
                      {children}
                    </ul>
                  ),

                  ol: ({ children }) => (
                    <ol className="my-3 list-decimal space-y-1.5 pl-5">
                      {children}
                    </ol>
                  ),

                  li: ({ children }) => (
                    <li className="pl-1">
                      {children}
                    </li>
                  ),

                  h1: ({ children }) => (
                    <h1 className="mb-3 text-lg font-semibold text-white">
                      {children}
                    </h1>
                  ),

                  h2: ({ children }) => (
                    <h2 className="mb-3 mt-4 text-base font-semibold text-white first:mt-0">
                      {children}
                    </h2>
                  ),

                  h3: ({ children }) => (
                    <h3 className="mb-2 mt-3 text-sm font-semibold text-white first:mt-0">
                      {children}
                    </h3>
                  ),

                  code: ({ children }) => (
                    <code className="rounded-md border border-slate-700 bg-slate-950 px-1.5 py-0.5 font-mono text-xs text-blue-300">
                      {children}
                    </code>
                  ),

                  blockquote: ({ children }) => (
                    <blockquote className="my-3 border-l-2 border-slate-700 pl-4 text-slate-400">
                      {children}
                    </blockquote>
                  ),

                  a: ({ href, children }) => (
                    <a
                      href={href}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-blue-400 underline decoration-blue-400/40 underline-offset-2 transition hover:text-blue-300"
                    >
                      {children}
                    </a>
                  ),

                  hr: () => (
                    <hr className="my-4 border-slate-800" />
                  ),
                }}
              >
                {message.content}
              </ReactMarkdown>

              {/* Streaming Cursor */}
              {message.isStreaming && (
                <span className="ml-1 inline-block h-4 w-1 animate-pulse rounded-sm bg-blue-400 align-middle" />
              )}
            </div>
          )}
        </div>

        {/* Message Actions */}
        {!isUser && !message.isStreaming && message.content && (
          <button
            type="button"
            onClick={handleCopy}
            className="flex items-center gap-1.5 rounded-md px-2 py-1 text-xs text-slate-500 opacity-0 transition-all duration-200 hover:bg-slate-900 hover:text-slate-300 group-hover:opacity-100"
            aria-label="Copy response"
          >
            {copied ? (
              <>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2"
                  className="h-3.5 w-3.5"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    d="M5 13l4 4L19 7"
                  />
                </svg>

                Copied
              </>
            ) : (
              <>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2"
                  className="h-3.5 w-3.5"
                >
                  <rect
                    width="13"
                    height="13"
                    x="9"
                    y="9"
                    rx="2"
                  />
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"
                  />
                </svg>

                Copy
              </>
            )}
          </button>
        )}
      </div>
    </div>
  );
};

export default ChatMessage;
