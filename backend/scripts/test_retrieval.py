from app.services.retrieval_service import (
    infer_section,
    retrieve_documents,
)


QUERIES = [
    "What AI projects has Khalid built?",
    "Where did Khalid work as an AI Engineer?",
    "What technologies does Khalid know?",
    "Where did Khalid study?",
    "How many DSA problems has Khalid solved?",
    "Tell me about Khalid's experience with LangGraph.",
]


def main():

    for query in QUERIES:

        print("=" * 80)
        print(f"QUERY: {query}")
        print("=" * 80)

        section = infer_section(query)

        print(f"Inferred section: {section}")

        documents = retrieve_documents(
            query,
            k=3,
        )

        print(
            f"Retrieved documents: {len(documents)}"
        )

        for index, document in enumerate(
            documents,
            start=1,
        ):
            print(f"\n--- RESULT {index} ---")
            print(
                f"Section: "
                f"{document.metadata.get('section')}"
            )
            print(document.page_content)

        print()


if __name__ == "__main__":
    main()