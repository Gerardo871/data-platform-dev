from extract.bcrp import fetch_bcrp_data
from transform.dates import parse_bcrp_date
from load.postgres import insert_records

SERIE_ID = "PN01271PM"

def run_pipeline():
    data = fetch_bcrp_data()

    periods = data["periods"]

    rows = []

    for item in periods:
        date = parse_bcrp_date(item["name"])
        value = item["values"][0]

        rows.append((SERIE_ID, value, date))

    insert_records(rows)

    print("ETL ejecutado correctamente")

if __name__ == "__main__":
    run_pipeline()