const SuggestedQuestions = ({
    questions,
    onQuestionClick,
    disabled = false,
}) => {
    if (!questions.length) {
        return null;
    }

    return (
        <div className="grid gap-3 sm:grid-cols-2">
            {questions.map((question) => (
                <button
                    key={question.id}
                    type="button"
                    onClick={() => onQuestionClick(question)}
                    disabled={disabled}
                    className="rounded-xl border border-slate-800 bg-slate-900/50 p-4 text-left text-sm text-slate-300 transition hover:border-slate-700 hover:bg-slate-900 hover:text-white disabled:cursor-not-allowed disabled:opacity-50"
                >
                    {question.question}
                </button>
            ))}
        </div>
    );
};

export default SuggestedQuestions;