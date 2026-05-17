import ttkbootstrap as tb
from tkinter import ttk
from tkinter import messagebox
from scr.database import connect


class ClientWindow:

    def __init__(
        self,
        root,
        reload_clients,
        reload_metrics
    ):

        self.reload_clients = reload_clients
        self.reload_metrics = reload_metrics
        self.window = tb.Toplevel(root)
        self.window.title(
            "Novo Cliente"
        )

        self.window.geometry(
            "450x650"
        )

        tb.Label(
            self.window,
            text="Nome"
        ).pack(pady=5)

        self.name = tb.Entry(
            self.window,
            width=40
        )

        self.name.pack()

        tb.Label(
            self.window,
            text="Idade"
        ).pack(pady=5)

        self.age = tb.Entry(
            self.window,
            width=40
        )

        self.age.pack()
        tb.Label(
            self.window,
            text="Plano"
        ).pack(pady=5)

        self.plan = ttk.Combobox(
            self.window,
            values=[
                "Amil",
                "Bradesco Saúde",
                "SulAmérica",
                "Unimed",
                "NotreDame Intermédica"
            ],
            width=37
        )

        self.plan.pack()
        tb.Label(
            self.window,
            text="Cidade"
        ).pack(pady=5)
        self.city = tb.Entry(
            self.window,
            width=40
        )

        self.city.pack()
        tb.Label(
            self.window,
            text="Telefone"
        ).pack(pady=5)

        self.phone = tb.Entry(
            self.window,
            width=40
        )

        self.phone.pack()

        tb.Label(
            self.window,
            text="Email"
        ).pack(pady=5)

        self.email = tb.Entry(
            self.window,
            width=40
        )

        self.email.pack()

        tb.Button(
            self.window,
            text="Salvar Cliente",
            bootstyle="success",
            command=self.save
        ).pack(pady=20)

    def save(self):
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO clients(
            name,
            age,
            health_plan,
            city,
            phone,
            email
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            self.name.get(),
            self.age.get(),
            self.plan.get(),
            self.city.get(),
            self.phone.get(),
            self.email.get()
        ))

        conn.commit()
        conn.close()
        messagebox.showinfo(
            "Sucesso",
            "Cliente cadastrado"
        )

        self.reload_clients()
        self.reload_metrics()
        self.window.destroy()