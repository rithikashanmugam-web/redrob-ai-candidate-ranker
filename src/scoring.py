def final_score(

    semantic_score,

    evidence_score,

    recruiter_score,

    title_score

):

    return (

        semantic_score * 0.50 +

        evidence_score * 0.20 +

        recruiter_score * 0.15 +

        title_score * 0.15

    )