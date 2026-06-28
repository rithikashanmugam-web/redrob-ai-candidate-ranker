JD_CRITICAL_KEYWORDS = {
    "retrieval",
    "ranking",
    "search",
    "recommendation",
    "matching",
    "vector",
    "embedding",
    "embeddings",
    "semantic"
}


def contradiction_penalty(candidate):

    skill_text = " ".join(
        skill["name"]
        for skill in candidate["skills"]
    ).lower()

    career_text = ""

    for job in candidate["career_history"]:
        career_text += (
            job["title"] + " " +
            job["description"] + " "
        ).lower()

    skill_matches = 0

    for keyword in JD_CRITICAL_KEYWORDS:
        if keyword in skill_text:
            skill_matches += 1

    career_matches = 0

    for keyword in JD_CRITICAL_KEYWORDS:
        if keyword in career_text:
            career_matches += 1

    if skill_matches >= 2 and career_matches == 0:
        return 30

    return 0