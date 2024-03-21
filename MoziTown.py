from tkinter import *
from ttkbootstrap import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import *
import sqlite3

root = Window(themename="superhero")
root.configure(background="#181D31")
root.title("MoziTown")
root.geometry("1440x900")
root.resizable(False, False)

con = sqlite3.connect("mozitown.db")
cur = con.cursor()
cur.execute("PRAGMA foreign_keys = ON;")
try:
    cur.execute("""CREATE TABLE termek(
                Teremszam INT
                Filmcim VARCHAR(32)
                Filmev DATE
                Filmmufaj VARCHAR(16)
                Fimhossz INT
                Teremkapacitas INT
    """)
    cur.execute("""CREATE TABLE foglalasok(
                Sorszam INT AUTO_INCREMENT PRIMARY KEY
                Keresztnev VARCHAR(32)
                Vezeteknev VARCHAR(32)
                Teremszam ADD INDEX
                Szekszam INT
    """)
    cur.execute("CREATE UNIQUE INDEX teremindex ON foglalasok (Teremszam)")
except FileExistsError:
    pass

def foglal_ablak():
    fog_ablak = Toplevel(root)
    fog_ablak.geometry("1000x650")
    fog_ablak.title("<Film>: Foglalás")

    fcimkeret = LabelFrame(fog_ablak)
    fcimkeret.grid(row=0, column=0, columnspan=2)
    Label.columnconfigure(fcimkeret, 1, weight=1)
    fcim = Label(fcimkeret, text="<Filmcím>", font=("Terminal", 20, "bold"), justify="center", anchor="center", width=90)
    fcim.grid(row=0, column=0, pady=5, sticky="nesw")

    fkeret = LabelFrame(fog_ablak)
    fkeret.grid(row=1, column=1, padx=20, pady=20, sticky="nse")

    fleiras = Label(fkeret, text="<Film leírása>", font=("Times", 12, "bold"))
    fleiras.grid(row=0, column=0)
    fszekek = Checkbutton(fkeret)
    fszekek.grid(row=1, column=0)
    ffoglal = Button(fkeret, text="Helyet foglalok")
    ffoglal.grid(row=2, column=0)

foglalas = Button(root, text="Foglalás", bootstyle="warning", command=lambda: foglal_ablak())
foglalas.grid(row=0, column=0)

root.mainloop()