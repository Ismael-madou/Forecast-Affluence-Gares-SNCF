import requests
import pandas as pd
from pathlib import Path
# (ajoute aussi json/datetime/etc. si tu les utilises)

# Récupérer la liste des fichiers ZIP disponibles via l'API IDFM
URL = "https://data.iledefrance-mobilites.fr/api/explore/v2.1/catalog/datasets/histo-validations-reseau-ferre/records"
print("Récupération de la liste des fichiers disponibles...")
r = requests.get(URL, timeout=60)
r.raise_for_status()

response_data = r.json()
records = response_data.get("results", [])
print(f"Nombre de fichiers trouvés: {len(records)}")

# Créer un DataFrame avec les métadonnées
data = []
for record in records:
 data.append({
 'annee': int(record.get('annee')),
 'filename': record.get('reseau_ferre', {}).get('filename'),
 'url': record.get('reseau_ferre', {}).get('url')})

df_metadata = pd.DataFrame(data)
print("\nFichiers disponibles:")
print(df_metadata)