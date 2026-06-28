from src.semantic_ranker import (
    model,
    candidate_text
)


def build_candidate_embeddings(
    candidates
):

    texts = []

    for candidate in candidates:

        texts.append(
            candidate_text(candidate)
        )

    embeddings = model.encode(
        texts,
        show_progress_bar=True
    )

    return embeddings