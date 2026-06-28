def generate_explanation(
    candidate,
    semantic_score,
    evidence_keywords
):

    reasons = []

    if semantic_score >= 55:
        reasons.append(
            "Strong semantic match with job description"
        )

    elif semantic_score >= 45:
        reasons.append(
            "Good semantic alignment with role requirements"
        )

    if len(evidence_keywords) > 0:

        reasons.append(
            "Relevant production experience in: "
            + ", ".join(evidence_keywords[:5])
        )

    signals = candidate["redrob_signals"]

    if signals["open_to_work_flag"]:
        reasons.append(
            "Currently open to work"
        )

    if signals["saved_by_recruiters_30d"] >= 20:
        reasons.append(
            "Frequently shortlisted by recruiters"
        )

    if signals["recruiter_response_rate"] >= 0.6:
        reasons.append(
            "High recruiter response rate"
        )

    return reasons