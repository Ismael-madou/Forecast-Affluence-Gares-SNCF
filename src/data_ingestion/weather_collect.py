import requests, pandas as pd

# 1. Appel de l'API météo Open-Meteo (pas besoin de clé)
url = "https://api.open-meteo.com/v1/forecast"
params = {"latitude": 48.8566,        
    "longitude": 2.3522,          
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
    "timezone": "Europe/Paris"}

# 2. Envoi de la requête
r = requests.get(url, params=params, timeout=30)
r.raise_for_status()

# 3. Extraction des données JSON et transformation en DataFrame
d = r.json()["daily"]
df = pd.DataFrame({"date": d["time"],
    "tmax": d["temperature_2m_max"],
    "tmin": d["temperature_2m_min"],
    "precipitation": d["precipitation_sum"]})

# 4. Sauvegarde en CSV
df.to_csv("weather_paris.csv", index=False)
print("OK -> weather_paris.csv")

