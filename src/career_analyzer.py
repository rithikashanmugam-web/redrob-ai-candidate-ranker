KEYWORDS = {

    "retrieval",
    "ranking",
    "search",
    "recommendation",

    "embedding",
    "embeddings",

    "vector",

    "semantic",

    "matching",

    "relevance"

}


def career_relevance_score(candidate):

    score = 0

    for job in candidate["career_history"]:

        description = job["description"].lower()

        for keyword in KEYWORDS:

            if keyword in description:

                score += 15

    return min(score, 100)