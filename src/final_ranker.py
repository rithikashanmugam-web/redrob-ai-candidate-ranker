def title_score(candidate):

    title = candidate["profile"]["current_title"].lower()

    if "ml engineer" in title:
        return 25

    if "ai engineer" in title:
        return 25

    if "data scientist" in title:
        return 20

    if "backend engineer" in title:
        return 10

    if "software engineer" in title:
        return 10

    return 0


def recruiter_signal_score(candidate):

    signals = candidate["redrob_signals"]

    score = 0

    if signals["open_to_work_flag"]:
        score += 10

    score += min(
        signals["saved_by_recruiters_30d"],
        20
    )

    score += int(
        signals["recruiter_response_rate"] * 20
    )

    return score