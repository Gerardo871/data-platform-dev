from datetime import datetime

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