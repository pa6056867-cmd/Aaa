import sqlite3

DB_NAME = "cafinet.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        phone TEXT NOT NULL,
        service TEXT NOT NULL,
        description TEXT,
        status TEXT DEFAULT 'در انتظار',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()
import sqlite3


DB_NAME = "cafinet.db"


def init_db():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

user_id INTEGER,
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        full_name TEXT,

        phone TEXT,

        service TEXT,

        description TEXT,

        status TEXT DEFAULT 'در انتظار',

        created_at DATETIME DEFAULT CURRENT_TIMESTAMP

    )
    """)


    conn.commit()

    conn.close()
