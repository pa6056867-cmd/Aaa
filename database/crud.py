import sqlite3

DB_NAME = "cafinet.db"


def add_order(full_name, phone, service, description):

    conn = sqlite3.connect(DB_NAME)

    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO orders
        (full_name, phone, service, description)
        VALUES (?, ?, ?, ?)
        """,
        (
            full_name,
            phone,
            service,
            description
        )
    )

    conn.commit()

    order_id = cur.lastrowid

    conn.close()

    return order_id
