EVIDENCE_KEYWORDS = {

    "retrieval": 25,
    "ranking": 25,
    "matching": 20,
    "search": 20,
    "recommendation": 20,

    "embedding": 15,
    "embeddings": 15,
    "vector": 15,
    "semantic": 15,

    "llm": 10,
    "fine-tuning": 10
}


def career_evidence_score(candidate):

    score = 0

    career_text = ""

    for job in candidate["career_history"]:

        career_text += (
            job["title"] + " " +
            job["description"] + " "
        ).lower()

    matched_keywords = []

    for keyword, points in EVIDENCE_KEYWORDS.items():

        if keyword in career_text:

            score += points
            matched_keywords.append(keyword)

    return min(score, 100), matched_keywords