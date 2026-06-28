import pandas as pd

def export_results(results, filename):

    submission = []

    rank = 1

    for row in results:

        submission.append({
            "rank": rank,
            "candidate_id": row["candidate_id"],
            "final_score": round(
                row["final_score"], 2
            )
        })

        rank += 1

    pd.DataFrame(
        submission
    ).to_csv(
        filename,
        index=False
    )

    print(f"Saved {filename}")