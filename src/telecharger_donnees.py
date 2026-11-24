from pathlib import Path
import requests
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "raw" / "world_bank_maroc_1990_2024.csv"
INDICATORS = {
    "gdp_growth": "NY.GDP.MKTP.KD.ZG",
    "unemployment": "SL.UEM.TOTL.ZS",
}

def fetch(code, name):
    url = f"https://api.worldbank.org/v2/country/MAR/indicator/{code}?date=1990:2024&format=json&per_page=200"
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    payload = response.json()
    frame = pd.DataFrame(payload[1])[["date", "value"]]
    frame["year"] = frame["date"].astype(int)
    return frame[["year", "value"]].rename(columns={"value": name})

if __name__ == "__main__":
    gdp = fetch(INDICATORS["gdp_growth"], "gdp_growth")
    unemployment = fetch(INDICATORS["unemployment"], "unemployment")
    data = gdp.merge(unemployment, on="year", how="inner").sort_values("year")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    data.to_csv(OUT, index=False)
    print(f"Fichier enregistré : {OUT} ({len(data)} lignes)")
