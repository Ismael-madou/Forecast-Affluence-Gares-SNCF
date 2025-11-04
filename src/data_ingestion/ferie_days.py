# feries_idf_all_years.py
import requests, pandas as pd
from datetime import date
from pathlib import Path

OUT = Path("data/processed/jours_feries_idf"); OUT.mkdir(parents=True, exist_ok=True)
for y in range(2000, date.today().year + 2):  # balaye large; 404 ignorés
    url = f"https://calendrier.api.gouv.fr/jours-feries/metropole/{y}.json"
    r = requests.get(url, timeout=20)
    if r.status_code == 404:  # pas de fichier pour cette année
        continue
    r.raise_for_status()
    data = r.json() or {}
    if not data: 
        continue
    pd.DataFrame([{"date": d, "label": lbl, "annee": y} for d, lbl in data.items()]) \
      .sort_values("date") \
      .to_csv(OUT / f"jours_feries_idf_{y}.csv", index=False, encoding="utf-8")
    print(f"OK -> {OUT / f'jours_feries_idf_{y}.csv'}")
