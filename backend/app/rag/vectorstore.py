from langchain_chroma import Chroma
from langchain_core.documents import Document

from app.rag.embeddings import get_embeddings


COLLECTION_NAME = "portfolio"
VECTORSTORE_PATH = "./storage/chroma"


def create_vectorstore(
    documents: list[Document],
) -> Chroma:
    """
    Create or rebuild the portfolio Chroma collection.

    The collection is cleared before indexing so repeated ingestion
    runs produce a deterministic vector store without duplicate data.
    """
    if not documents:
        raise ValueError(
            "Cannot create vector store from empty documents."
        )

    embeddings = get_embeddings()

    vectorstore = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=VECTORSTORE_PATH,
    )

    # Remove existing documents before rebuilding the collection.
    existing = vectorstore.get()

    existing_ids = existing.get("ids", [])

    if existing_ids:
        vectorstore.delete(ids=existing_ids)

    # Generate deterministic IDs based on document position.
    ids = [
        f"portfolio_doc_{index}"
        for index in range(len(documents))
    ]

    vectorstore.add_documents(
        documents=documents,
        ids=ids,
    )

    return vectorstore