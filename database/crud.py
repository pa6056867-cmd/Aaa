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
def get_stats():

    conn = sqlite3.connect(DB_NAME)

    cur = conn.cursor()


    cur.execute(
        "SELECT COUNT(*) FROM orders"
    )

    orders = cur.fetchone()[0]


    cur.execute(
        "SELECT COUNT(DISTINCT user_id) FROM orders"
    )

    users = cur.fetchone()[0]


    cur.execute(
        """
        SELECT SUM(amount)
        FROM finance
        WHERE type='درآمد'
        """
    )

    income = cur.fetchone()[0]


    conn.close()


    return orders, users, income or 0
def get_all_users():

    conn = sqlite3.connect(DB_NAME)

    cur = conn.cursor()

    cur.execute("""
    SELECT DISTINCT user_id
    FROM orders
    """)

    users = cur.fetchall()

    conn.close()

    return users
