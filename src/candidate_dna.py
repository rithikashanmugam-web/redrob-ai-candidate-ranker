def generate_dna(candidate):

    profile = candidate["profile"]
    signals = candidate["redrob_signals"]

    dna = {

        "candidate_id":
        candidate["candidate_id"],

        "current_title":
        profile["current_title"],

        "years_of_experience":
        profile["years_of_experience"],

        "current_company":
        profile["current_company"],

        "industry":
        profile["current_industry"],

        "skills":
        [
            skill["name"]
            for skill in candidate["skills"]
        ],

        "github_score":
        signals["github_activity_score"],

        "notice_period":
        signals["notice_period_days"],

        "open_to_work":
        signals["open_to_work_flag"]

    }

    return dna