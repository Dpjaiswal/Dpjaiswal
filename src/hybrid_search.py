def reciprocal_rank_fusion(dense_ranks: list[int], sparse_ranks: list[int], k: int = 60) -> float:
    """Calculate Reciprocal Rank Fusion (RRF) score for hybrid search retrieval."""
    rrf_score = 0.0
    for rank in dense_ranks:
        rrf_score += 1.0 / (k + rank)
    for rank in sparse_ranks:
        rrf_score += 1.0 / (k + rank)
    return rrf_score
