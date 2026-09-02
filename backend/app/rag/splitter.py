# from langchain_text_splitters import RecursiveCharacterTextSplitter


# def split_documents(documents):
#     """
#     Split LangChain documents into smaller chunks.
#     """

#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=800,
#         chunk_overlap=100,
#     )

#     return splitter.split_documents(documents)

def split_documents(documents):
    """
    Keep each portfolio section as a single document.

    The portfolio knowledge base is small and already
    organized into meaningful semantic sections, so
    additional chunking would unnecessarily separate
    related information.
    """

    return documents