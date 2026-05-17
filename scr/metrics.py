from scr.database import connect


def get_metrics():

    conn = connect()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM clients
    """)

    total_clients = cursor.fetchone()[0]

    cursor.execute("""
    SELECT COUNT(*)
    FROM clients
    WHERE strftime('%m', created_at)
    =
    strftime('%m', 'now')
    """)

    month_clients = cursor.fetchone()[0]

    cursor.execute("""
    SELECT COUNT(health_plan)
    FROM clients
    WHERE health_plan IS NOT NULL
    """)

    total_plans = cursor.fetchone()[0]

    conn.close()

    return (
        total_clients,
        month_clients,
        total_plans
    )