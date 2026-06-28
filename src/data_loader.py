import json


def load_candidates(filepath):

    candidates = []

    with open(filepath, "r", encoding="utf-8") as file:

        for line in file:

            line = line.strip()

            if line:
                candidates.append(
                    json.loads(line)
                )

    return candidates