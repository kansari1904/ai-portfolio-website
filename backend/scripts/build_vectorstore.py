from pathlib import Path

from app.rag.loader import (
    load_portfolio_json,
    portfolio_to_documents,
)

from app.rag.splitter import split_documents

from app.rag.vectorstore import create_vectorstore


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

    print("Converting portfolio to documents...")

    documents = portfolio_to_documents(
        portfolio
    )

    print(
        f"Created {len(documents)} documents."
    )

    print("Splitting documents...")

    chunks = split_documents(
        documents
    )

    print(
        f"Created {len(chunks)} chunks."
    )

    print(
        "\nBuilding Chroma vector store..."
    )

    create_vectorstore(
        chunks
    )

    print(
        "\nVector store created successfully."
    )


if __name__ == "__main__":
    main()