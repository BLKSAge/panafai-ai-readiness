## normalize.py
import os
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Directories
clean_dir = "../data/clean/"
norm_dir = "../data/normalized/"
os.makedirs(norm_dir, exist_ok=True)

# Custom ranges (indicator: (min, max))
custom_ranges = {
    "mobile": (0, 200),
    "gov_effect": (-2.5, 2.5)
}

def normalize_indicator(df, indicator_name, preview_rows=0):
    """
    Normalizes indicator values to 0–100 (or custom range).
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe with a 'Value' column.
    indicator_name : str
        Name of the indicator.
    preview_rows : int, default=0
        Number of rows to preview after normalization.
    """
    # Ensure Value column is numeric
    df["Value"] = pd.to_numeric(df["Value"], errors="coerce")

    if indicator_name in custom_ranges:
        min_val, max_val = custom_ranges[indicator_name]
        df["Normalized"] = (df["Value"] - min_val) / (max_val - min_val) * 100
    else:
        scaler = MinMaxScaler(feature_range=(0, 100))
        df["Normalized"] = scaler.fit_transform(df[["Value"]])
    
    df["Indicator"] = indicator_name

    if preview_rows > 0:
        print(f"Preview of {indicator_name}:")
        print(df.head(preview_rows))

    return df

if __name__ == "__main__":
    for fname in os.listdir(clean_dir):
        if fname.endswith("_clean.csv"):
            indicator = fname.replace("_clean.csv", "")
            try:
                df = pd.read_csv(os.path.join(clean_dir, fname))
                normalized = normalize_indicator(df, indicator, preview_rows=5)
                out_path = os.path.join(norm_dir, f"{indicator}_normalized.csv")
                normalized.to_csv(out_path, index=False)
                print(f"Saved {out_path} ({len(normalized)} rows)")
            except Exception as e:
                print(f"Failed on {indicator}: {e}")