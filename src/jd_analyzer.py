def extract_requirements(jd_text):

    jd_lower = jd_text.lower()

    required_skills = []

    skill_keywords = [

        "embeddings",
        "retrieval",
        "ranking",
        "llms",
        "fine-tuning",
        "python",
        "vector",
        "matching",
        "evaluation",
        "search"

    ]

    for skill in skill_keywords:

        if skill in jd_lower:
            required_skills.append(skill)

    return required_skills