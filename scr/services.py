import pandas as pd
from scr.database import connect
from reportlab.pdfgen import canvas


def export_clients_excel():
    conn = connect()

    query = "SELECT * FROM clients"

    df = pd.read_sql(query, conn)

    df.to_excel(
        "exports/excel/clientes.xlsx",
        index=False
    )

    conn.close()

