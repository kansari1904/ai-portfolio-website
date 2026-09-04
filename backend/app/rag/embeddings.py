from functools import lru_cache

from langchain_huggingface import HuggingFaceEmbeddings


MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


@lru_cache(maxsize=1)
def get_embeddings() -> HuggingFaceEmbeddings:
    """
    Create and cache the local embedding model.

    The model is loaded only once per application process.
    Subsequent calls reuse the same instance.
    """
    return HuggingFaceEmbeddings(
        model_name=MODEL_NAME
    )