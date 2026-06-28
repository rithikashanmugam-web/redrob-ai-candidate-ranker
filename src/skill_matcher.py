def dynamic_skill_match(candidate, jd_requirements):

    candidate_skills = {
        skill["name"].lower()
        for skill in candidate["skills"]
    }

    matches = []

    for requirement in jd_requirements:

        req = requirement.lower()

        for skill in candidate_skills:

            if req in skill or skill in req:
                matches.append(requirement)
                break

    score = len(matches) * 10

    return min(score, 100), matches