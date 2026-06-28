from src.jd_analyzer import extract_requirements


SKILL_MAP = {

    "llms": [
        "llama",
        "gpt",
        "mistral",
        "llm"
    ],

    "fine-tuning": [
        "lora",
        "qlora",
        "peft",
        "fine-tuning"
    ],

    "retrieval": [
        "information retrieval",
        "retrieval",
        "rag"
    ],

    "ranking": [
        "learning to rank",
        "ranking"
    ],

    "vector": [
        "pinecone",
        "qdrant",
        "weaviate",
        "faiss"
    ],

    "embeddings": [
        "embedding",
        "embeddings",
        "sentence transformers"
    ],

    "matching": [
        "matching",
        "candidate-jd matching"
    ],

    "evaluation": [
        "evaluation",
        "eval",
        "a/b test",
        "metrics"
    ],
    "python": [
        "python",
        "pytorch",
        "scikit-learn",
        "pandas",
        "numpy"
    ]
}


def generate_fit_report(
    jd_text,
    candidate
):

    jd_skills = extract_requirements(
        jd_text
    )

    candidate_text = ""

    # Skills
    for skill in candidate["skills"]:

        candidate_text += (
            skill["name"].lower()
            + " "
        )

    # Career history descriptions
    for job in candidate[
        "career_history"
    ]:

        candidate_text += (
            job["description"].lower()
            + " "
        )

    strengths = []
    missing = []

    for skill in jd_skills:

        matched = False

        # Direct match
        if skill in candidate_text:

            matched = True

        # Synonym match
        elif skill in SKILL_MAP:

            for synonym in SKILL_MAP[
                skill
            ]:

                if synonym in candidate_text:

                    matched = True
                    break

        if matched:

            strengths.append(
                skill
            )

        else:

            missing.append(
                skill
            )

    return strengths, missing


def hiring_recommendation(
    score
):

    if score >= 55:
        return "STRONG HIRE"

    elif score >= 45:
        return "HIRE"

    elif score >= 35:
        return "CONSIDER"

    else:
        return "REJECT"