from sklearn.metrics.pairwise import cosine_similarity

from src.semantic_ranker import (
    model
)

from src.career_evidence import (
    career_evidence_score
)

from src.final_ranker import (
    title_score,
    recruiter_signal_score
)

from src.scoring import (
    final_score
)

from src.explainer import (
    generate_explanation
)

from src.fit_report import (
    generate_fit_report,
    hiring_recommendation
)


def rank_candidates(
    jd_text,
    candidates,
    candidate_embeddings
):

    results = []

    jd_embedding = model.encode(
        jd_text
    )

    for candidate, embedding in zip(
        candidates,
        candidate_embeddings
    ):

        # Semantic Similarity
        semantic_score = (
            cosine_similarity(
                [jd_embedding],
                [embedding]
            )[0][0]
        ) * 100

        # Career Evidence
        evidence_score, evidence_keywords = (
            career_evidence_score(
                candidate
            )
        )

        # Recruiter Signals
        recruiter_score = (
            recruiter_signal_score(
                candidate
            )
        )

        # Title Relevance
        title_relevance = (
            title_score(
                candidate
            )
        )

        # Final Score
        score = final_score(
            semantic_score,
            evidence_score,
            recruiter_score,
            title_relevance
        )

        # Explanations
        explanation = (
            generate_explanation(
                candidate,
                semantic_score,
                evidence_keywords
            )
        )

        # Fit Report
        strengths, missing = (
            generate_fit_report(
                jd_text,
                candidate
            )
        )

        recommendation = (
            hiring_recommendation(
                score
            )
        )

        results.append({

            "candidate_id":
            candidate["candidate_id"],

            "final_score":
            float(round(score, 2)),

            "semantic_score":
            float(round(semantic_score, 2)),

            "evidence_score":
            evidence_score,

            "explanation":
            explanation,

            "strengths":
            strengths,

            "missing":
            missing,

            "recommendation":
            recommendation
        })

    results.sort(
        key=lambda x:
        x["final_score"],
        reverse=True
    )

    return results