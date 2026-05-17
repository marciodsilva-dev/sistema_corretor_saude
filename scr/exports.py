import pandas as pd
from reportlab.pdfgen import canvas
from scr.database import connect


def export_excel():

    conn = connect()

    df = pd.read_sql_query(
        "SELECT * FROM clients",
        conn
    )

    df.to_excel(
        "exports/clientes.xlsx",
        index=False
    )

    conn.close()


def export_pdf():

    pdf = canvas.Canvas(
        "reports/clientes.pdf"
    )

    pdf.drawString(
        100,
        800,
        "Relatório de Clientes"
    )

    conn = connect()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        name,
        age,
        health_plan,
        city,
        phone
    FROM clients
    """)

    data = cursor.fetchall()

    y = 760

    for client in data:

        pdf.drawString(
            100,
            y,
            str(client)
        )

        y -= 20

    pdf.save()

    conn.close()