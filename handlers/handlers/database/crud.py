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
