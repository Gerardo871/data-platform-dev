# pyrefly: ignore [missing-import]
from extract.bcrp import fetch_bcrp_data
from transform.dates import parse_bcrp_date
from load.postgres import insert_records
from transform.missing import fill_missing_with_avg
import argparse

#PD04647PDTC Euro (S/ por Euro) — Compra
#PD04648PDTC Euro (S/ por Euro) — Venta

def run_pipeline(start_date:str, end_date:str, serie_id:str)->None:
    """
    Ejecuta el pipeline de ETL para obtener datos del BCRP e insertarlos en la base de datos.
    """
    data:dict = fetch_bcrp_data(serie_id, start_date, end_date)

    periods:list = data["periods"]

    rows:list = []

    for item in periods:
        date:date = parse_bcrp_date(item["name"])
        value:float = item["values"][0]

        rows.append((serie_id, value, date))
    rows = fill_missing_with_avg(rows)
    insert_records(rows)

    print("ETL ejecutado correctamente")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ETL para obtener datos del BCRP")
    parser.add_argument("--start_date", type=str, required=True, help="Fecha de inicio en formato YYYY-MM-DD")
    parser.add_argument("--end_date", type=str, required=True, help="Fecha de fin en formato YYYY-MM-DD")
    parser.add_argument("--serie_id", type=str, required=True, help="ID de la serie del BCRP")
    args = parser.parse_args()
    run_pipeline(args.start_date, args.end_date, args.serie_id)