import psycopg2
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD
from load.postgres import get_connection

def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

def insert_records(rows):
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