import matplotlib.pyplot as plt
from scr.database import connect


def show_graph():

    conn = connect()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        health_plan,
        COUNT(*)
    FROM clients
    GROUP BY health_plan
    """)

    data = cursor.fetchall()

    conn.close()

    plans = [x[0] for x in data]

    totals = [x[1] for x in data]

    plt.figure(figsize=(8, 5))

    plt.bar(plans, totals)

    plt.title(
        "Clientes por Plano"
    )

    plt.xlabel("Plano")
    plt.ylabel("Quantidade")

    plt.show()