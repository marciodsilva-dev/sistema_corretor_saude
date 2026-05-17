import ttkbootstrap as tb

from scr.database import create_tables
from ui.login import LoginPage

create_tables()

root = tb.Window(themename="superhero")
root.title("Sistema Corretor de Saúde")
root.geometry("1450x850")

LoginPage(root)
root.mainloop()