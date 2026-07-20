import requests

SERIE_ID = "PN01271PM"

def fetch_bcrp_data():
    url = f"https://estadisticas.bcrp.gob.pe/estadisticas/series/api/{SERIE_ID}/json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()