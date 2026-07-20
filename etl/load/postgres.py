import psycopg2
from config.config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD

def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

def insert_records(rows:list)->None:
    """
    Inserta registros en la tabla bcrp_indicator.
    
    Args:
        rows (list): Una lista de tuplas que contienen los datos a insertar.
    """
    conn = get_connection()
    cur = conn.cursor()

    query = """
        INSERT INTO bcrp_indicator (series_id, value, date)
        VALUES (%s, %s, %s)
    """

    cur.executemany(query, rows)

    conn.commit()
    cur.close()
    conn.close()