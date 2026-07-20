import requests


def fetch_bcrp_data(SERIE_ID:str,start_date:str, end_date:str)->dict:
    """
    Obtiene datos de la API del BCRP para un ID de serie y rango de fechas dados.
    
    Args:
        SERIE_ID (str): El ID de serie para el cual se obtendrán los datos.
        start_date (str): La fecha de inicio en formato YYYY-MM-DD.
        end_date (str): La fecha de fin en formato YYYY-MM-DD.
    
    Returns:
        dict: Los datos de la API del BCRP.
    """
    #print(f"Obteniendo datos para la serie {SERIE_ID} desde {start_date} hasta {end_date}")
    url = f"https://estadisticas.bcrp.gob.pe/estadisticas/series/api/{SERIE_ID}/json/{start_date}/{end_date}/esp"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()