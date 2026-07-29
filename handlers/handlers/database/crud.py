from .database import get_connection


def add_order(

    full_name,

    phone,

    service,

    description

):

    conn = get_connection()

    cur = conn.cursor()

    cur.execute(

        """
        INSERT INTO orders(

        full_name,

        phone,

        service,

        description

        )

        VALUES(?,?,?,?)

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
def get_order(order_id):

    conn = get_connection()

    cur = conn.cursor()

    cur.execute(

        """
        SELECT *

        FROM orders

        WHERE id=?
        """,

        (order_id,)

    )

    order = cur.fetchone()

    conn.close()

    return order
def get_order(order_id):

    conn = sqlite3.connect(DB_NAME)

    cur = conn.cursor()

    cur.execute(
        """
        SELECT id, full_name, phone, service, description, status
        FROM orders
        WHERE id=?
        """,
        (order_id,)
    )

    order = cur.fetchone()

    conn.close()

    return order
