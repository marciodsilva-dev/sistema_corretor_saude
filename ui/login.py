import ttkbootstrap as tb
from tkinter import messagebox
from ui.dashboard import Dashboard

class LoginPage:

    def __init__(self, root):

        self.root = root
        self.frame = tb.Frame(root)
        self.frame.pack(expand=True)

        tb.Label(
            self.frame,
            text="Sistema Corretor de Saúde",
            font=("Arial", 30, "bold")
        ).pack(pady=30)

        tb.Label(
            self.frame,
            text="Usuário"
        ).pack()

        self.user = tb.Entry(
            self.frame,
            width=40
        )

        self.user.pack(pady=10)

        tb.Label(
            self.frame,
            text="Senha"
        ).pack()

        self.password = tb.Entry(
            self.frame,
            width=40,
            show="*"
        )

        self.password.pack(pady=10)

        tb.Button(
            self.frame,
            text="Entrar",
            bootstyle="success",
            command=self.login
        ).pack(pady=20)

    def login(self):

        if (
            self.user.get() == "admin"
            and
            self.password.get() == "123"
        ):

            self.frame.destroy()

            Dashboard(self.root)

        else:

            messagebox.showerror(
                "Erro",
                "Usuário ou senha inválidos"
            )