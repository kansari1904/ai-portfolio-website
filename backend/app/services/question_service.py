import json
from functools import lru_cache
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parents[2]
FAQ_PATH = BASE_DIR / "data" / "knowledge" / "faq.json"


class FAQNotFoundError(LookupError):
    """Raised when a requested FAQ does not exist."""


@lru_cache(maxsize=1)
def _load_faq_data() -> dict[str, Any]:
    """
    Load FAQ data from faq.json.

    The result is cached so the file is not read from disk
    for every API request.
    """
    if not FAQ_PATH.exists():
        raise FileNotFoundError(
            f"FAQ knowledge base not found: {FAQ_PATH}"
        )

    with FAQ_PATH.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, dict):
        raise ValueError("FAQ knowledge base must be a JSON object.")

    faqs = data.get("faqs")

    if not isinstance(faqs, list):
        raise ValueError(
            "FAQ knowledge base must contain a 'faqs' list."
        )

    return data


@lru_cache(maxsize=1)
def _build_faq_index() -> dict[str, dict[str, str]]:
    """
    Build an in-memory FAQ index.

    Example:

        {
            "faq_001": {...},
            "faq_002": {...}
        }

    This gives us O(1) FAQ lookup by ID.
    """
    faqs = _load_faq_data()["faqs"]

    index: dict[str, dict[str, str]] = {}

    for faq in faqs:
        if not isinstance(faq, dict):
            raise ValueError(
                "Every FAQ entry must be a JSON object."
            )

        faq_id = faq.get("id")
        category = faq.get("category")
        question = faq.get("question")
        answer = faq.get("answer")

        if not all(
            isinstance(value, str) and value.strip()
            for value in (
                faq_id,
                category,
                question,
                answer,
            )
        ):
            raise ValueError(
                "Every FAQ must contain non-empty "
                "id, category, question and answer."
            )

        if faq_id in index:
            raise ValueError(
                f"Duplicate FAQ ID found: {faq_id}"
            )

        index[faq_id] = {
            "id": faq_id,
            "category": category,
            "question": question,
            "answer": answer,
        }

    return index


def get_faq_suggestions() -> list[dict[str, str]]:
    """
    Return FAQ questions for the frontend.

    Answers are intentionally excluded.
    """
    return [
        {
            "id": faq["id"],
            "category": faq["category"],
            "question": faq["question"],
        }
        for faq in _build_faq_index().values()
    ]


def get_faq_by_id(faq_id: str) -> dict[str, str]:
    """
    Return a single FAQ and its pre-written answer.

    This function does NOT call:
    - an LLM
    - an embedding model
    - ChromaDB
    """
    faq = _build_faq_index().get(faq_id)

    if faq is None:
        raise FAQNotFoundError(
            f"FAQ not found: {faq_id}"
        )

    return faq