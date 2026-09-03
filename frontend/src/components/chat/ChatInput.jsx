import { useEffect, useRef } from "react";

const ChatInput = ({
  value,
  onChange,
  onSubmit,
  disabled = false,
}) => {
  const textareaRef = useRef(null);

  /*
   * Automatically adjust textarea height
   * based on its content.
   */
  useEffect(() => {
    const textarea = textareaRef.current;

    if (!textarea) {
      return;
    }

    textarea.style.height = "auto";

    textarea.style.height = `${
    Math.min(
        textarea.scrollHeight,
        160
    )
} px`;
  }, [value]);

  /*
   * Handle keyboard interaction.
   *
   * Enter       -> Submit
   * Shift+Enter -> New line
   */
  const handleKeyDown = (event) => {
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault();

      if (!disabled && value.trim()) {
        onSubmit(event);
      }
    }
  };

  return (
    <form
      onSubmit={onSubmit}
      className="flex items-end gap-3"
    >
      {/* Textarea */}
      <textarea
        ref={textareaRef}
        value={value}
        onChange={(event) =>
          onChange(event.target.value)
        }
        onKeyDown={handleKeyDown}
        placeholder="Ask me about Khalid..."
        disabled={disabled}
        rows={1}
        className="max-h-40 min-h-12 min-w-0 flex-1 resize-none overflow-y-auto rounded-xl border border-slate-800 bg-slate-900 px-4 py-3 text-sm leading-6 text-white outline-none placeholder:text-slate-500 transition focus:border-slate-600 disabled:cursor-not-allowed disabled:opacity-60"
      />

      {/* Send Button */}
      <button
        type="submit"
        disabled={disabled || !value.trim()}
        aria-label="Send message"
        className="flex h-12 w-12 shrink-0 items-center justify-center rounded-xl bg-white text-slate-950 transition hover:bg-slate-200 disabled:cursor-not-allowed disabled:opacity-40"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="2"
          className="h-5 w-5"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            d="M22 2L11 13"
          />

          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            d="M22 2L15 22L11 13L2 9L22 2Z"
          />
        </svg>
      </button>
    </form>
  );
};

export default ChatInput;