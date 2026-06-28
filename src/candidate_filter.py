RELEVANT_TITLES = {

    "ml engineer",
    "machine learning engineer",

    "ai engineer",

    "data scientist",

    "backend engineer",

    "software engineer",

    "search engineer",

    "relevance engineer",

    "recommendation engineer",

    "nlp engineer"

}


def is_relevant_candidate(candidate):

    title = (
        candidate["profile"]
        ["current_title"]
        .lower()
    )

    for role in RELEVANT_TITLES:

        if role in title:
            return True

    return False