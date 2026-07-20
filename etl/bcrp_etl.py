import requests
import psycopg2
from datetime import datetime

# =========================
# CONFIG POSTGRES (Docker)
# =========================
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="dataplatform",
    user="admin",
    password="admin"
)

cur = conn.cursor()

# =========================
# EJEMPLO BCRP (serie simple)
# =========================
SERIE_ID = "PN01271PM"  # ejemplo: tipo de cambio (puede variar)

url = f"https://estadisticas.bcrp.gob.pe/estadisticas/series/api/{SERIE_ID}/json"

response = requests.get(url)
data = response.json()

# =========================
# PARSEO (estructura BCRP)
# =========================
series = data["periods"]

rows = []


def parse_bcrp_date(date_str):
    months = {
        "Ene": 1, "Feb": 2, "Mar": 3, "Abr": 4,
        "May": 5, "Jun": 6, "Jul": 7, "Ago": 8,
        "Sep": 9, "Oct": 10, "Nov": 11, "Dic": 12
    }

    month_str, year_str = date_str.split(".")
    month = months.get(month_str)

    if not month:
        raise ValueError(f"Mes inválido: {month_str}")

    return datetime(int(year_str), month, 1).date()



for item in series:
    date = parse_bcrp_date(item["name"])  # formato YYYY.MM
    value = item["values"][0]

    rows.append((SERIE_ID, value, date))

# =========================
# INSERT EN POSTGRES
# =========================
for row in rows:
    cur.execute("""
        INSERT INTO bcrp_indicator (series_id, value, date)
        VALUES (%s, %s, %s)
    """, row)

conn.commit()

cur.close()
conn.close()

print("ETL BCRP completado correctamente")