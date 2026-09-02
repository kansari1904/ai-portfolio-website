from app.services.chat_service import (
    classify_question,
    process_question,
)


QUERIES = [
    "What AI projects has Khalid built?",
    "Where did Khalid study?",
    "How many DSA problems has Khalid solved?",
    "What certifications does Khalid have?",
    "Tell me about Khalid's experience with LangGraph.",
]


def main():

    for query in QUERIES:

        print("=" * 80)
        print(f"QUERY: {query}")
        print("=" * 80)

        route = classify_question(query)

        print(f"Route: {route}")

        result = process_question(query)

        print(f"Answer:\n{result['answer']}")

        print()


if __name__ == "__main__":
    main()