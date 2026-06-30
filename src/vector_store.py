from langchain_community.vectorstores import FAISS

from src.embeddings import get_embeddings


def create_vector_store(chunks):
    """
    Create a FAISS vector database from text chunks.
    """

    embeddings = get_embeddings()

    vector_store = FAISS.from_texts(
        texts=chunks,
        embedding=embeddings
    )

    return vector_store