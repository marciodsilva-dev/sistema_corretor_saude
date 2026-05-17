from tkinter import *
from tkinter import ttk
from scr.database import connect

class ProposalScreen:
    
    def __init__(self, root):
        self.root = root
        
        Label(self.root, text="Plano").pack()

        self.plan = ttk.Combobox(
            self.root,
            values=[
                "Amil",
                "Bradesco",
                "Sulamérica",
                "Hapvida",
                "MedTour Saúde"
            ]
        )
        self.plan.pack()

        Label(self.root, text="Valor").pack()
        self.value = Entry(self.root)
        self.value.pack()

        Button(
            self.root,
            text="Enviar Proposta",
            command=self.save_proposal
        ).pack(pady=20)

    def save_proposal(self):
        conn = connect()
        cursor = conn.cursor()

        cursor.execute(
            '''
            INSERT INTO proposals(plan, value, status)
            VALUES (?, ?, ?)
            ''',
            (
                self.plan.get(),
                self.value.get(),
                "Em análise"
            )
        )

        conn.commit()
        conn.close()
