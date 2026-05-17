import ttkbootstrap as tb
from tkinter import ttk
from tkinter import messagebox
from ttkbootstrap.constants import *
from ui.clients import ClientWindow
from scr.metrics import get_metrics
from scr.exports import export_excel
from scr.exports import export_pdf
from scr.graphs import show_graph
from scr.database import connect


class Dashboard:

    def __init__(self, root):
        self.root = root
        self.main = tb.Frame(root)
        self.main.pack(fill=BOTH, expand=True)

        # SIDEBAR
        self.sidebar = tb.Frame(
            self.main,
            width=250,
            bootstyle="dark"
        )

        self.sidebar.pack(
            side=LEFT,
            fill=Y
        )

        tb.Label(
            self.sidebar,
            text="🏥 CRM Saúde",
            font=("Arial", 24, "bold")
        ).pack(pady=30)

        tb.Button(
            self.sidebar,
            text="Novo Cliente",
            bootstyle="success",
            width=25,
            command=self.new_client
        ).pack(pady=10)

        tb.Button(
            self.sidebar,
            text="Excluir Cliente",
            bootstyle="danger",
            width=25,
            command=self.delete_client
        ).pack(pady=10)

        tb.Button(
            self.sidebar,
            text="Exportar Excel",
            bootstyle="info",
            width=25,
            command=self.export_excel_file
        ).pack(pady=10)

        tb.Button(
            self.sidebar,
            text="Exportar PDF",
            bootstyle="warning",
            width=25,
            command=self.export_pdf_file
        ).pack(pady=10)

        tb.Button(
            self.sidebar,
            text="Mostrar Gráfico",
            bootstyle="primary",
            width=25,
            command=show_graph
        ).pack(pady=10)

        # CONTENT
        self.content = tb.Frame(self.main)
        self.content.pack(
            side=LEFT,
            fill=BOTH,
            expand=True
        )

        tb.Label(
            self.content,
            text="Dashboard Comercial",
            font=("Arial", 30, "bold")
        ).pack(pady=20)

        # CARDS
        cards = tb.Frame(self.content)
        cards.pack(fill=X, padx=20)
        self.total_clients = self.create_card(
            cards,
            "Clientes Totais",
            "0"
        )

        self.month_clients = self.create_card(
            cards,
            "Cadastros do Mês",
            "0"
        )

        self.total_plans = self.create_card(
            cards,
            "Planos Vendidos",
            "0"
        )

        # PESQUISA
        search_frame = tb.Frame(self.content)
        search_frame.pack(
            fill=X,
            padx=20,
            pady=20
        )

        self.search_entry = tb.Entry(
            search_frame,
            width=50
        )

        self.search_entry.pack(
            side=LEFT,
            padx=10
        )

        tb.Button(
            search_frame,
            text="Pesquisar",
            bootstyle="info",
            command=self.search_client
        ).pack(side=LEFT)

        tb.Button(
            search_frame,
            text="Atualizar",
            bootstyle="secondary",
            command=self.load_clients
        ).pack(side=LEFT, padx=10)

        # TABELA
        table_frame = tb.Frame(self.content)

        table_frame.pack(
            fill=BOTH,
            expand=True,
            padx=20,
            pady=20
        )

        self.tree = ttk.Treeview(
            table_frame,
            columns=(
                "ID",
                "Nome",
                "Idade",
                "Plano",
                "Cidade",
                "Telefone"
            ),
            show="headings"
        )

        for col in (
            "ID",
            "Nome",
            "Idade",
            "Plano",
            "Cidade",
            "Telefone"
        ):

            self.tree.heading(col, text=col)

        self.tree.pack(fill=BOTH, expand=True)
        self.load_clients()
        self.load_metrics()

    def create_card(
        self,
        parent,
        title,
        value
    ):

        frame = tb.Frame(
            parent,
            bootstyle="secondary"
        )

        frame.pack(
            side=LEFT,
            padx=10,
            pady=10,
            fill=X,
            expand=True
        )

        tb.Label(
            frame,
            text=title,
            font=("Arial", 14)
        ).pack(pady=10)

        label = tb.Label(
            frame,
            text=value,
            font=("Arial", 28, "bold")
        )

        label.pack(pady=10)

        return label

    def load_clients(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

        conn = connect()
        cursor = conn.cursor()
        cursor.execute("""
        SELECT
            id,
            name,
            age,
            health_plan,
            city,
            phone
        FROM clients
        """)

        data = cursor.fetchall()
        conn.close()
        for row in data:
            self.tree.insert(
                "",
                END,
                values=row
            )

    def load_metrics(self):

        (
            total,
            month,
            plans
        ) = get_metrics()

        self.total_clients.config(
            text=str(total)
        )

        self.month_clients.config(
            text=str(month)
        )

        self.total_plans.config(
            text=str(plans)
        )

    def new_client(self):

        ClientWindow(
            self.root,
            self.load_clients,
            self.load_metrics
        )

    def delete_client(self):

        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning(
                "Aviso",
                "Selecione um cliente"
            )

            return

        item = self.tree.item(selected)
        client_id = item["values"][0]
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM clients
        WHERE id=?
        """, (client_id,))

        conn.commit()
        conn.close()

        self.load_clients()
        self.load_metrics()
        
    def search_client(self):
        search = self.search_entry.get()
        for item in self.tree.get_children():
            self.tree.delete(item)

        conn = connect()
        cursor = conn.cursor()
        cursor.execute("""
        SELECT
            id,
            name,
            age,
            health_plan,
            city,
            phone
        FROM clients
        WHERE name LIKE ?
        """, (f"%{search}%",))

        data = cursor.fetchall()
        conn.close()

        for row in data:
            self.tree.insert(
                "",
                END,
                values=row
            )

    def export_excel_file(self):
        export_excel()
        messagebox.showinfo(
            "Excel",
            "Arquivo exportado"
        )

    def export_pdf_file(self):
        export_pdf()

        messagebox.showinfo(
            "PDF",
            "Arquivo gerado"
        )