from pathlib import Path

from app.rag.loader import (
    load_portfolio_json,
    portfolio_to_documents,
)

from app.rag.splitter import split_documents

from app.rag.embeddings import get_embeddings


BASE_DIR = Path(__file__).resolve().parent.parent

PORTFOLIO_PATH = (
    BASE_DIR
    / "data"
    / "knowledge"
    / "portfolio.json"
)


def main():

    print("Loading portfolio...")

    portfolio = load_portfolio_json(
        str(PORTFOLIO_PATH)
    )

    documents = portfolio_to_documents(
        portfolio
    )

    print(
        f"Original documents: {len(documents)}"
    )

    chunks = split_documents(
        documents
    )

    print(
        f"Total chunks: {len(chunks)}"
    )

    print("\nLoading embedding model...")

    embeddings = get_embeddings()

    print("Embedding model loaded.")

    test_text = (
        "What experience does Khalid have "
        "with RAG and LangGraph?"
    )

    print(
        f"\nTest text:\n{test_text}"
    )

    vector = embeddings.embed_query(
        test_text
    )

    print(
        f"\nEmbedding dimensions: {len(vector)}"
    )

    print(
        "\nFirst 10 values:"
    )

    print(vector[:10])


if __name__ == "__main__":
    main()