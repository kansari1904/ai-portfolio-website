from pathlib import Path

from app.rag.loader import (
    load_portfolio_json,
    portfolio_to_documents,
)

from app.rag.splitter import split_documents


BASE_DIR = Path(__file__).resolve().parent.parent

PORTFOLIO_PATH = (
    BASE_DIR
    / "data"
    / "knowledge"
    / "portfolio.json"
)


def main():

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

    print("\n")

    for index, chunk in enumerate(
        chunks,
        start=1
    ):

        print("=" * 70)

        print(
            f"CHUNK {index}"
        )

        print("-" * 70)

        print(
            f"Section: "
            f"{chunk.metadata.get('section')}"
        )

        print(
            f"Metadata: "
            f"{chunk.metadata}"
        )

        print(
            f"Characters: "
            f"{len(chunk.page_content)}"
        )

        print("-" * 70)

        print(
            chunk.page_content
        )

        print()


if __name__ == "__main__":
    main()