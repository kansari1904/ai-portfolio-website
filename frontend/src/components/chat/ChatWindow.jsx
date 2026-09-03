import { useEffect, useRef, useState } from "react";

import ChatMessage from "./ChatMessage";
import ChatInput from "./ChatInput";
import SuggestedQuestions from "./SuggestedQuestions";

import {
  getFaqSuggestions,
  streamQuestion,
} from "../../services/chatApi";

/*
 * Creates a unique message object.
 */
const createMessage = (role, content = "", extra = {}) => ({
  id: crypto.randomUUID(),
  role,
  content,
  ...extra,
});

const ChatWindow = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [suggestedQuestions, setSuggestedQuestions] =
    useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [failedQuestion, setFailedQuestion] =
    useState("");

  const messagesEndRef = useRef(null);

  /*
   * Scroll to the latest content.
   *
   * This runs while streaming, so the recruiter
   * can follow the generated response.
   */
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({
      behavior: "smooth",
      block: "end",
    });
  }, [messages]);

  /*
   * Load the featured FAQ suggestions once.
   */
  useEffect(() => {
    const loadSuggestions = async () => {
      try {
        const data = await getFaqSuggestions();

        setSuggestedQuestions(
          data.suggestions ?? []
        );
      } catch (error) {
        console.error(
          "Failed to load FAQ suggestions:",
          error
        );
      }
    };

    loadSuggestions();
  }, []);

  /*
   * Send question and stream the response.
   */
  const handleQuestion = async (question) => {
    if (!question || isLoading) {
      return;
    }

    setError(null);
    setFailedQuestion("");

    const userMessage = createMessage(
      "user",
      question
    );

    const assistantMessage = createMessage(
      "assistant",
      "",
      {
        isStreaming: true,
      }
    );

    /*
     * Add both messages immediately.
     */
    setMessages((previous) => [
      ...previous,
      userMessage,
      assistantMessage,
    ]);

    setIsLoading(true);

    try {
      await streamQuestion(question, (chunk) => {
        setMessages((previous) =>
          previous.map((message) =>
            message.id === assistantMessage.id
              ? {
                  ...message,
                  content:
                    message.content + chunk,
                }
              : message
          )
        );
      });

      /*
       * Mark the exact assistant message as complete.
       */
      setMessages((previous) =>
        previous.map((message) =>
          message.id === assistantMessage.id
            ? {
                ...message,
                isStreaming: false,
              }
            : message
        )
      );
    } catch (error) {
      console.error("Chat error:", error);

      setError(
        error.message ||
          "Something went wrong while getting the answer."
      );

      setFailedQuestion(question);

      /*
       * If no response was received, remove the
       * empty assistant bubble.
       *
       * If partial content exists, keep it visible
       * but stop its streaming state.
       */
      setMessages((previous) => {
        const assistant = previous.find(
          (message) =>
            message.id === assistantMessage.id
        );

        if (assistant && !assistant.content) {
          return previous.filter(
            (message) =>
              message.id !== assistantMessage.id
          );
        }

        return previous.map((message) =>
          message.id === assistantMessage.id
            ? {
                ...message,
                isStreaming: false,
              }
            : message
        );
      });
    } finally {
      setIsLoading(false);
    }
  };

  /*
   * Retry the failed question.
   */
  const handleRetry = () => {
    if (!failedQuestion || isLoading) {
      return;
    }

    const question = failedQuestion;

    setError(null);
    setFailedQuestion("");

    handleQuestion(question);
  };

  /*
   * Clear the entire conversation.
   */
  const handleNewChat = () => {
    if (isLoading) {
      return;
    }

    setMessages([]);
    setInput("");
    setError(null);
    setFailedQuestion("");
  };

  /*
   * Handle suggested FAQ.
   */
  const handleQuestionClick = (question) => {
    handleQuestion(question.question);
  };

  /*
   * Handle manual input.
   */
  const handleSubmit = (event) => {
    event.preventDefault();

    const question = input.trim();

    if (!question || isLoading) {
      return;
    }

    setInput("");
    handleQuestion(question);
  };

  /*
   * Show the typing indicator only before
   * the first streamed chunk arrives.
   */
  const isWaitingForResponse =
    isLoading &&
    messages.length > 0 &&
    messages[messages.length - 1]?.role ===
      "assistant" &&
    !messages[messages.length - 1]?.content;

  return (
    <section
      id="chat"
      className="border-t border-slate-900 bg-slate-950 py-16 sm:py-20"
    >
      <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">

        {/* Section Header */}
        <div className="text-center">
          <p className="text-xs font-semibold uppercase tracking-[0.2em] text-blue-400 sm:text-sm">
            AI Recruiter Assistant
          </p>

          <h2 className="mt-3 text-3xl font-bold tracking-tight text-white sm:text-4xl">
            Ask me anything about Khalid
          </h2>

          <p className="mx-auto mt-4 max-w-2xl text-sm leading-6 text-slate-400 sm:text-base">
            Ask about my projects, technical skills,
            education, or AI engineering work.
          </p>
        </div>

        {/* Chat Card */}
        <div className="mt-8 overflow-hidden rounded-2xl border border-slate-800 bg-slate-900/30 shadow-2xl shadow-black/10 sm:mt-10">

          {/* Chat Header */}
          <div className="flex items-center justify-between border-b border-slate-800/80 px-4 py-3 sm:px-5">

            <div className="flex min-w-0 items-center gap-2.5">

              <span className="relative flex h-2.5 w-2.5 shrink-0">
                <span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-emerald-400 opacity-50" />
                <span className="relative inline-flex h-2.5 w-2.5 rounded-full bg-emerald-400" />
              </span>

              <span className="truncate text-sm font-medium text-slate-300">
                Khalid's AI Assistant
              </span>

            </div>

            <button
              type="button"
              onClick={handleNewChat}
              disabled={
                isLoading || messages.length === 0
              }
              className="shrink-0 rounded-lg border border-slate-800 px-2.5 py-1.5 text-xs font-medium text-slate-400 transition hover:border-slate-700 hover:bg-slate-800 hover:text-white disabled:cursor-not-allowed disabled:opacity-30 sm:px-3"
            >
              New Chat
            </button>

          </div>

          {/* Conversation Area */}
          <div
            className="chat-scrollbar max-h-[520px] min-h-[320px] overflow-y-auto p-4 sm:p-6"
          >
            {messages.length === 0 ? (

              /* Empty State */
              <div className="flex min-h-[280px] items-center justify-center px-4">
                <div className="max-w-md text-center">

                  <div className="mx-auto flex h-12 w-12 items-center justify-center rounded-full border border-slate-800 bg-slate-900 shadow-sm">
                    <span className="text-lg text-blue-400">
                      ✦
                    </span>
                  </div>

                  <h3 className="mt-4 text-sm font-semibold text-white sm:text-base">
                    Recruiter-friendly AI assistant
                  </h3>

                  <p className="mt-2 text-sm leading-6 text-slate-500">
                    Choose a suggested question or ask
                    something about Khalid.
                  </p>

                </div>
              </div>

            ) : (

              /* Conversation */
              <div className="relative">

                <div className="space-y-4">

                  {messages.map((message) => (
                    <ChatMessage
                      key={message.id}
                      message={message}
                    />
                  ))}

                  {/* Initial Loading Indicator */}
                  {isWaitingForResponse && (
                    <div className="flex items-end gap-2">

                      <div className="mb-1 flex h-8 w-8 shrink-0 items-center justify-center rounded-full border border-slate-700 bg-slate-900 text-sm text-blue-400 shadow-sm">
                        ✦
                      </div>

                      <div className="flex items-center gap-1 rounded-2xl rounded-bl-md border border-slate-800 bg-slate-900/90 px-4 py-3">

                        <span className="h-1.5 w-1.5 animate-bounce rounded-full bg-slate-500" />

                        <span
                          className="h-1.5 w-1.5 animate-bounce rounded-full bg-slate-500"
                          style={{
                            animationDelay: "150ms",
                          }}
                        />

                        <span
                          className="h-1.5 w-1.5 animate-bounce rounded-full bg-slate-500"
                          style={{
                            animationDelay: "300ms",
                          }}
                        />

                      </div>
                    </div>
                  )}

                  {/* Scroll Target */}
                  <div
                    ref={messagesEndRef}
                    className="h-px"
                  />

                </div>
              </div>
            )}
          </div>

          {/* Error */}
          {error && (
            <div className="border-t border-red-900/40 bg-red-950/20 px-4 py-3 sm:px-5">

              <div className="flex items-center gap-3">

                <div className="flex h-7 w-7 shrink-0 items-center justify-center rounded-full border border-red-900/60 bg-red-950/40 text-xs font-semibold text-red-400">
                  !
                </div>

                <div className="min-w-0 flex-1">
                  <p className="text-sm font-medium text-red-300">
                    Unable to generate a response
                  </p>

                  <p className="mt-0.5 truncate text-xs text-red-400/70">
                    {error}
                  </p>
                </div>

                {failedQuestion && (
                  <button
                    type="button"
                    onClick={handleRetry}
                    disabled={isLoading}
                    className="shrink-0 rounded-lg border border-red-900/60 bg-red-950/30 px-3 py-1.5 text-xs font-medium text-red-300 transition hover:bg-red-950/60 hover:text-red-200 disabled:cursor-not-allowed disabled:opacity-50"
                  >
                    Retry
                  </button>
                )}

              </div>
            </div>
          )}

          {/* Suggested Questions */}
          <div className="border-t border-slate-800/80 p-4 sm:p-5">

            <p className="mb-3 text-[11px] font-semibold uppercase tracking-[0.15em] text-slate-500">
              Suggested questions
            </p>

            <SuggestedQuestions
              questions={suggestedQuestions}
              onQuestionClick={handleQuestionClick}
              disabled={isLoading}
            />

          </div>

          {/* Input */}
          <div className="border-t border-slate-800/80 p-4 sm:p-5">

            <ChatInput
              value={input}
              onChange={setInput}
              onSubmit={handleSubmit}
              disabled={isLoading}
            />

            <p className="mt-2 text-center text-[10px] text-slate-600 sm:text-[11px]">
              Enter to send · Shift + Enter for a new line
            </p>

          </div>

        </div>
      </div>
    </section>
  );
};

export default ChatWindow;
