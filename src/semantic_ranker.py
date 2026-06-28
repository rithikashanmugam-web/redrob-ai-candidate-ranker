from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)
def candidate_text(candidate):

    profile = candidate["profile"]

    text = ""

    text += profile["headline"] + " "

    text += profile["summary"] + " "

    for job in candidate["career_history"]:

        text += (
            job["title"] + " "
        )

        text += (
            job["description"] + " "
        )

    for skill in candidate["skills"]:

        text += (
            skill["name"] + " "
        )

    return text
def semantic_match_score(
    jd_text,
    candidate
):

    candidate_profile = (
        candidate_text(candidate)
    )

    jd_embedding = model.encode(
        jd_text
    )

    candidate_embedding = model.encode(
        candidate_profile
    )

    similarity = cosine_similarity(
        [jd_embedding],
        [candidate_embedding]
    )[0][0]

    return round(
        similarity * 100,
        2
    )