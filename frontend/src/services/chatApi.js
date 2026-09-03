const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export const getFaqSuggestions = async () => {
    const response = await fetch(
        `${API_BASE_URL}/chat/suggestions`
    );

    if (!response.ok) {
        throw new Error("Failed to load suggested questions.");
    }

    return response.json();
};

export const getFaqAnswer = async (faqId) => {
    const response = await fetch(
        `${API_BASE_URL}/chat/faq/${faqId}`
    );

    if (!response.ok) {
        throw new Error("Failed to load FAQ answer.");
    }

    return response.json();
};

export const askQuestion = async (question) => {
    const response = await fetch(
        `${API_BASE_URL}/chat`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                question,
            }),
        }
    );

    if (!response.ok) {
        const errorData = await response.json().catch(() => null);

        throw new Error(
            errorData?.detail || "Failed to get an answer."
        );
    }

    return response.json();
};


/*
 * Stream an assistant response from the backend.
 *
 * onChunk receives each piece of text as it arrives.
 */
export const streamQuestion = async (
    question,
    onChunk
) => {
    const response = await fetch(
        `${API_BASE_URL}/chat/stream`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                question,
            }),
        }
    );

    if (!response.ok) {
        const errorData = await response.json().catch(() => null);

        throw new Error(
            errorData?.detail || "Failed to stream answer."
        );
    }

    if (!response.body) {
        throw new Error(
            "Streaming is not supported by this response."
        );
    }

    const reader = response.body.getReader();

    const decoder = new TextDecoder();

    try {
        while (true) {
            const { value, done } = await reader.read();

            if (done) {
                break;
            }

            const chunk = decoder.decode(value, {
                stream: true,
            });

            if (chunk) {
                onChunk(chunk);
            }
        }

        // Decode any remaining bytes.
        const remaining = decoder.decode();

        if (remaining) {
            onChunk(remaining);
        }
    } finally {
        reader.releaseLock();
    }
};