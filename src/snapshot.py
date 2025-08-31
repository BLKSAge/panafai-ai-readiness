## Snapshot
import os
import pandas as pd

# Directories
clean_dir = "../data/clean/"
snapshot_dir = "../data/snapshot/"
os.makedirs(snapshot_dir, exist_ok=True)

def extract_latest(df, indicator_name):
    """
    Extracts most recent non-null per country for an indicator.
    Adds a 'Year_Observed' column.
    """
    df_sorted = df.sort_values(["Country Name", "Year"])
    latest = df_sorted.dropna(subset=["Value"]).groupby("Country Name").tail(1)
    latest["Year_Observed"] = latest["Year"]
    latest["Indicator"] = indicator_name
    return latest

if __name__ == "__main__":
    for fname in os.listdir(clean_dir):
        if fname.endswith("_clean.csv"):
            indicator = fname.replace("_clean.csv", "")
            try:
                df = pd.read_csv(os.path.join(clean_dir, fname))
                snapshot = extract_latest(df, indicator)
                out_path = os.path.join(snapshot_dir, f"{indicator}_snapshot.csv")
                snapshot.to_csv(out_path, index=False)
                print(f"✔ Saved {out_path} ({len(snapshot)} rows)")
            except Exception as e:
                print(f"✘ Failed on {indicator}: {e}")