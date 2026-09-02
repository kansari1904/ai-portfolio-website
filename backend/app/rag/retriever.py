from langchain_chroma import Chroma

from app.rag.embeddings import get_embeddings
from app.rag.vectorstore import (
    COLLECTION_NAME,
    VECTORSTORE_PATH,
)


def get_vectorstore() -> Chroma:
    """
    Load the existing portfolio vector store.
    """
    embeddings = get_embeddings()

    return Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=VECTORSTORE_PATH,
    )


def get_retriever(k: int = 3):
    """
    Return a semantic retriever over portfolio knowledge.
    """
    if k < 1:
        raise ValueError(
            "k must be greater than or equal to 1."
        )

    vectorstore = get_vectorstore()

    return vectorstore.as_retriever(
        search_kwargs={
            "k": k
        }
    )