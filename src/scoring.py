## Scoring
import os
import pandas as pd

# Directories
norm_dir = "../data/normalized/"
score_dir = "../data/scored/"
os.makedirs(score_dir, exist_ok=True)

# Default weights (Qubit Hub pillars)
weights = {
    "literacy": 0.20,
    "tertiary": 0.20,   # together = Skills 40%
    "electricity": 0.15,
    "internet": 0.10,
    "mobile": 0.10,     # together = Infra 35%
    "gov_effect": 0.25  # Governance 25%
    # R&D + GDP PPP optional — could be added here
}

def compute_scores(norm_dfs, weights=None):
    """
    Combines normalized indicators into composite scores.
    - Equal-weight if weights=None
    - Weighted if dict provided
    """
    merged = pd.concat(norm_dfs, axis=0)
    pivot = merged.pivot_table(
        index=["Country Name", "Country Code"],
        columns="Indicator", values="Normalized"
    )

    if weights:
        score = sum(pivot.get(col, 0) * w for col, w in weights.items())
    else:
        score = pivot.mean(axis=1)

    pivot["AI_Readiness_Score"] = score
    return pivot.reset_index()

if __name__ == "__main__":
    norm_dfs = []
    for fname in os.listdir(norm_dir):
        if fname.endswith("_normalized.csv"):
            df = pd.read_csv(os.path.join(norm_dir, fname))
            norm_dfs.append(df)

    if not norm_dfs:
        print("No normalized files found")
    else:
        try:
            # Equal-weight scores
            equal_scores = compute_scores(norm_dfs, weights=None)
            equal_scores.to_csv(os.path.join(score_dir, "equal_scores.csv"), index=False)
            print("Saved equal_scores.csv")

            # Weighted scores
            weighted_scores = compute_scores(norm_dfs, weights=weights)
            weighted_scores.to_csv(os.path.join(score_dir, "weighted_scores.csv"), index=False)
            print("Saved weighted_scores.csv")
        except Exception as e:
            print(f"Failed scoring: {e}")