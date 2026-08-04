def retrieve_contexts(query: str, vector_db, k: int = 5) -> list[str]:
    """Retrieve top-K semantic contexts from vector database."""
    return vector_db.similarity_search(query, k=k)
