AI_SKILLS = {

    "NLP",
    "Embeddings",
    "Milvus",
    "Qdrant",
    "Pinecone",
    "Weaviate",
    "FAISS",

    "Fine-tuning LLMs",
    "LoRA",

    "BentoML",

    "Python",

    "Ranking Systems",
    "Recommendation Systems"

}


def technical_fit_score(candidate):

    skills = {
        skill["name"]
        for skill in candidate["skills"]
    }

    matches = len(
        skills.intersection(AI_SKILLS)
    )

    score = matches * 10

    return min(score, 100)