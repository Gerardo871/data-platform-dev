from datetime import datetime, date

def parse_bcrp_date(date_str: str) -> date:
    months = {
        "Ene": 1, "Feb": 2, "Mar": 3, "Abr": 4,
        "May": 5, "Jun": 6, "Jul": 7, "Ago": 8,
        "Sep": 9, "Set": 9, "Oct": 10, "Nov": 11, "Dic": 12
    }

    parts = date_str.split(".")

    if len(parts) == 3:
        day_str, month_str, year_str = parts
        day = int(day_str)
    elif len(parts) == 2:
        month_str, year_str = parts
        day = 1
    else:
        raise ValueError(f"Formato de fecha BCRP no reconocido: {date_str}")

    month: int = months.get(month_str)

    if not month:
        raise ValueError(f"Mes inválido: {month_str}")
    year = int(year_str)
    year = 2000 + year if year < 100 else year
    return datetime(year, month, day).date()