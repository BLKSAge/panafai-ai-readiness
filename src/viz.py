## Viz
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Directories
score_dir = "../data/scores/"
img_dir = "../images/"
os.makedirs(img_dir, exist_ok=True)

def plot_distribution(df, column, title, fname):
    """
    Plots distribution of a score or indicator across countries.
    """
    plt.figure(figsize=(10,6))
    sns.histplot(df[column].dropna(), kde=True)
    plt.title(title)
    out_path = os.path.join(img_dir, fname)
    plt.savefig(out_path)
    plt.close()
    print(f"✔ Saved {out_path}")

if __name__ == "__main__":
    try:
        weighted = pd.read_csv(os.path.join(score_dir, "weighted_scores.csv"))
        equal = pd.read_csv(os.path.join(score_dir, "equal_scores.csv"))

        plot_distribution(weighted, "AI_Readiness_Score",
                          "Distribution of Weighted AI Readiness Scores",
                          "weighted_scores_dist.png")

        plot_distribution(equal, "AI_Readiness_Score",
                          "Distribution of Equal AI Readiness Scores",
                          "equal_scores_dist.png")
    except Exception as e:
        print(f"✘ Visualization failed: {e}")