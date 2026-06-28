from src.data_loader import (
    load_candidates
)

from src.jd_parser import (
    load_job_description
)

from src.candidate_filter import (
    is_relevant_candidate
)

from src.embedding_cache import (
    build_candidate_embeddings
)

from src.ranker import (
    rank_candidates
)

from src.exporter import (
    export_results
)

# ----------------------------------
# Load Candidates
# ----------------------------------

candidates = load_candidates(
    "data/candidates.jsonl"
)

print(
    f"Total Candidates: {len(candidates)}"
)

# ----------------------------------
# Filter Candidates
# ----------------------------------

relevant = []

for candidate in candidates:

    if is_relevant_candidate(
        candidate
    ):
        relevant.append(
            candidate
        )

print(
    f"Relevant Candidates: {len(relevant)}"
)

# ----------------------------------
# Load Job Description
# ----------------------------------

jd_text = load_job_description(
    "data/job_description.docx"
)

# ----------------------------------
# Build Embeddings
# ----------------------------------

print(
    "\nBuilding embeddings...\n"
)

candidate_embeddings = (
    build_candidate_embeddings(
        relevant
    )
)

# ----------------------------------
# Rank Candidates
# ----------------------------------

print(
    "\nRanking candidates...\n"
)

results = rank_candidates(
    jd_text,
    relevant,
    candidate_embeddings
)

# ----------------------------------
# Show Top 3 Candidates
# ----------------------------------

for row in results[:3]:

    print("\n")
    print("=" * 60)

    print(
        f"\nCandidate: {row['candidate_id']}"
    )

    print(
        f"Final Score: {row['final_score']:.2f}"
    )

    print(
        f"Semantic Score: {row['semantic_score']:.2f}"
    )

    print(
        f"Evidence Score: {row['evidence_score']}"
    )

    print(
        f"\nRecommendation: {row['recommendation']}"
    )

    print("\nStrengths:")

    if len(row["strengths"]) == 0:

        print("None")

    else:

        for skill in row["strengths"]:

            print(
                f"✓ {skill}"
            )

    print("\nMissing Skills:")

    if len(row["missing"]) == 0:

        print("None")

    else:

        for skill in row["missing"]:

            print(
                f"- {skill}"
            )

    print("\nExplanation:")

    for reason in row["explanation"]:

        print(
            f"✓ {reason}"
        )

# ----------------------------------
# Export Top 100
# ----------------------------------

top_100 = results[:100]

export_results(
    top_100,
    "submission.csv"
)

print(
    "\nsubmission.csv generated successfully!"
)