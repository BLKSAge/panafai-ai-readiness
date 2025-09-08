## Cleaning 
import os
import pandas as pd

# Directories
raw_dir = "../data/raw/"
clean_dir = "../data/clean/"
os.makedirs(clean_dir, exist_ok=True)

def clean_wb_df(file_name, indicator_name, skiprows=4):
    """
    Cleans World Bank-style CSV:
    - Melt wide → long
    - Standardize columns
    - Filter Year >= 1990
    """
    df = pd.read_csv(os.path.join(raw_dir, file_name), skiprows=skiprows)
    
    # Standard World Bank layout
    df_long = df.melt(
        id_vars=["Country Name", "Country Code"],
        var_name="Year", value_name="Value"
    )
    
    # Convert year to numeric
    df_long["Year"] = pd.to_numeric(df_long["Year"], errors="coerce")
    df_long = df_long[df_long["Year"] >= 1990]
    
    # Tag with indicator name
    df_long["Indicator"] = indicator_name
    
    return df_long[["Country Name", "Country Code", "Year", "Indicator", "Value"]]

if __name__ == "__main__":
    # Correct file dictionary
    files = {
        "electricity": "API_EG.ELC.ACCS.ZS_DS2_en_csv_v2_38353.csv",
        "internet": "API_IT.NET.USER.ZS_DS2_en_csv_v2_112825.csv",
        "mobile": "API_IT.CEL.SETS.P2_DS2_en_csv_v2_37045.csv",
        "literacy": "API_SE.ADT.LITR.ZS_DS2_en_csv_v2_37553.csv",
        "tertiary": "API_SE.TER.ENRR_DS2_en_csv_v2_399842.csv",
        "researchers": "API_SP.POP.SCIE.RD.P6_DS2_en_csv_v2_463385.csv",
        "rnd_gdp": "API_GB.XPD.RSDV.GD.ZS_DS2_en_csv_v2_464376.csv",
        "gdp_ppp": "API_NY.GDP.PCAP.PP.KD_DS2_en_csv_v2_406489.csv",
        "gov_effect": "5a88699c-e86d-490a-8c9e-c070313913df_Data.csv"
    }

    for indicator, fname in files.items():
        try:
            # Some non-WB files (like gov_effect) may not need skiprows=4
            skip = 0 if indicator == "gov_effect" else 4
            
            cleaned = clean_wb_df(fname, indicator, skiprows=skip)
            
            out_path = os.path.join(clean_dir, f"{indicator}_clean.csv")
            cleaned.to_csv(out_path, index=False)
            print(f"Saved {out_path} ({len(cleaned)} rows)")
        except Exception as e:
            print(f"Failed on {indicator}: {e}")
