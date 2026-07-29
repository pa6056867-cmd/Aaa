import sqlite3


def get_connection():

    return sqlite3.connect("cafinet.db")


def init_db():

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS orders(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        full_name TEXT,

        phone TEXT,

        service TEXT,

        description TEXT,

        status TEXT DEFAULT 'در انتظار',

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)

    conn.commit()

    conn.close()
