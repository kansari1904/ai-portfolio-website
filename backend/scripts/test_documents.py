from pathlib import Path

from app.rag.loader import (
    load_portfolio_json,
    portfolio_to_documents,
)


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
        f"\nCreated {len(documents)} documents.\n"
    )

    for index, document in enumerate(documents, start=1):

        print("=" * 70)

        print(f"DOCUMENT {index}")

        print("-" * 70)

        print(
            f"Section: "
            f"{document.metadata.get('section')}"
        )

        print(
            f"Metadata: "
            f"{document.metadata}"
        )

        print("-" * 70)

        print(document.page_content[:500])

        print()


if __name__ == "__main__":
    main()