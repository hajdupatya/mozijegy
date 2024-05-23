from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from PIL import Image
Image.CUBIC=Image.BICUBIC
from ttkbootstrap import *
from tkinter import PhotoImage
import datetime as dt
from time import strftime
import sqlite3
from fpdf import *
import unicodedata
import random

root = Window(themename="superhero")
root.title("MoziTown")
root.geometry("1400x762")
root.resizable(False,False)
root.configure(background="#181D31")
date=dt.datetime.now()

def unicode_normalize(s):
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore')

global img1, img2, img3, img4, img5, img6, img7, img8, email

dune_fog_szek=[]
godzill_fog_szek=[]
imadlak_fog_szek=[]
king_fog_szek=[]
mehesz_fog_szek=[]
most_fog_szek=[]
panda_fog_szek=[]
szellemirtok_fog_szek=[]

date = dt.datetime.now()

def register():
    global email
    global nev
    email=emailentry.get()
    nev=neventry.get()
    log_ablak.destroy()



def login():
    global log_ablak
    log_ablak = Toplevel(root)
    log_ablak.geometry("500x500")
    log_ablak.resizable(False,False)
    log_ablak.title("Regisztráció")

    reg=Label(log_ablak, text="Regisztráció",font=("Arial","30","bold"))
    reg.pack( pady=(90,10))
    log_frame=LabelFrame(log_ablak, padding=(85,20), border=5)
    log_frame.pack()
    n=Label(log_frame,text="Név: ",font=("Arial","18","bold"))
    n.pack(pady=(5,10))
    global neventry
    neventry=Entry(log_frame,font=("Arial","14"))
    neventry.pack(pady=(0,10))
    nev=neventry.get()
    e=Label(log_frame,text="E-mail cím: ",font=("Arial","18","bold"))
    e.pack(pady=10)
    global emailentry
    emailentry=Entry(log_frame,font=("Arial","14"))
    emailentry.pack(pady=(0,20))
    reg=Button(log_frame,text="Regisztráció",command=lambda:register())
    reg.pack()

login()

con = sqlite3.connect("mozitown.db")
cur = con.cursor()
def adatbazis():
    try:
        cur.execute("SELECT * FROM film")
        return
    except Exception:
        filmtable = """CREATE TABLE film (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cim VARCHAR(50) NOT NULL,
            hossz INT NOT NULL,
            date DATE NOT NULL,
            description TEXT NOT NULL );"""
        cur.execute(filmtable)
        vetitestable = """CREATE TABLE vetites (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            film_id INT NOT NULL,
            ido VARCHAR(10) NOT NULL,
            jegyar INT NOT NULL,
            FOREIGN KEY (film_id) REFERENCES film(id) );"""
        cur.execute(vetitestable)
        jegytable = """CREATE TABLE jegy (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vetites_id INT NOT NULL,
            nev VARCHAR(50) NOT NULL,
            hely INT NOT NULL,
            FOREIGN KEY (vetites_id) REFERENCES vetites(id) );"""
        cur.execute(jegytable)
        add_film(dunenev, dunehossz, dunedate, dunedesc)
        add_film(mostnev, mosthossz, mostdate, mostdesc)
        add_film(imadlaknev, imadlakhossz, imadlakdate, imadlakdesc)
        add_film(mehesznev, meheszhossz, meheszdate, meheszdesc)
        add_film(kingnev, kinghossz, kingdate, kingdesc)
        add_film(godzillanev, godzillahossz, godzilladate, godzilladesc)
        add_film(pandanev, pandahossz, pandadate, pandadesc)
        add_film(szellemirtoknev, szellemirtokhossz, szellemirtokdate, szellemirtokdesc)
        add_vetites(vetites1film, vetites1ido, vetites1ar)
        add_vetites(vetites2film, vetites2ido, vetites2ar)
        add_vetites(vetites3film, vetites3ido, vetites3ar)
        add_vetites(vetites4film, vetites4ido, vetites4ar)
        add_vetites(vetites5film, vetites5ido, vetites5ar)
        add_vetites(vetites6film, vetites6ido, vetites6ar)
        add_vetites(vetites7film, vetites7ido, vetites7ar)
        add_vetites(vetites8film, vetites8ido, vetites8ar)
        add_vetites(vetites9film, vetites9ido, vetites4ar)
        add_vetites(vetites10film, vetites10ido, vetites10ar)
        add_vetites(vetites11film, vetites11ido, vetites11ar)
        add_vetites(vetites12film, vetites12ido, vetites12ar)
        add_vetites(vetites13film, vetites13ido, vetites13ar)
        add_vetites(vetites14film, vetites14ido, vetites14ar)
        add_vetites(vetites15film, vetites15ido, vetites15ar)
        add_vetites(vetites16film, vetites16ido, vetites16ar)
        add_vetites(vetites17film, vetites17ido, vetites17ar)
        add_vetites(vetites18film, vetites18ido, vetites18ar)
        add_vetites(vetites19film, vetites19ido, vetites19ar)
        add_vetites(vetites20film, vetites20ido, vetites20ar)
        add_vetites(vetites21film, vetites21ido, vetites21ar)
        add_vetites(vetites22film, vetites22ido, vetites22ar)
        add_vetites(vetites23film, vetites23ido, vetites23ar)
        add_vetites(vetites24film, vetites24ido, vetites24ar)
        add_vetites(vetites25film, vetites25ido, vetites25ar)
        add_vetites(vetites26film, vetites26ido, vetites26ar)
        add_vetites(vetites27film, vetites27ido, vetites27ar)
        add_vetites(vetites28film, vetites28ido, vetites28ar)

def add_film(nev: str, hossz: int, date: str, description: str):
    command = f"""INSERT INTO film VALUES (NULL,'{nev}','{hossz}','{date}','{description}')"""
    cur.execute(command)
    con.commit()

def add_vetites(film_id: int, ido: str, jegyar: int):
    command = f"""INSERT INTO vetites VALUES (NULL,'{film_id}','{ido}','{jegyar}')"""
    cur.execute(command)
    con.commit()

def add_jegy(vetites_id: int, nev: str, hely: int):
    command = f"""INSERT INTO jegy VALUES (NULL,'{vetites_id}', '{nev}', '{hely}')"""
    cur.execute(command)
    con.commit()



def pdf_dune():
    try:

        title = "Foglalás"
        terem = "1"
    
        class PDF(FPDF):
            def header(self):
                self.image("logo.png", 5, 5, 50, 50)
                self.set_font("Helvetica", "BU", 20)
                self.cell(40)
                title_w = self.get_string_width(title) + 6
                doc_w = self.w
                self.set_x((doc_w - title_w) / 2)
                self.set_line_width(1)
                self.cell(title_w, 45, title, align="C")
                self.set_font("Helvetica", "", 10)
                self.cell(40)
                self.multi_cell(0, 7, "MoziTown Kft.\n8200, Veszprém, Iskola utca 4.\nMinden jog fenntartva!", align="R")
                self.ln(40)
            def body(self):
                self.set_font("Helvetica", "BU", 15)
                self.cell(0, 5, "Részletek:")
                self.ln(10)
                self.set_font("Times", "", 13)
                self.multi_cell(0, 10, "Vásárló E-mail címe: " + email + " \nFilm neve: DUNE - MÁSODIK RÉSZ\nFilm hossza: 166 perc\nIdopont: Valamikor\nTerem száma: " + terem +"\nSzékek száma: "+str(dune_fog_szek))
                self.image("dune.png", 130, 75, 70, 100)
                self.ln(40)
                self.set_font("Helvetica", "BU", 15)
                self.cell(0, 5, "Elérhetoségek:")
                self.ln(10)
                self.set_font("Times", "", 13)
                self.multi_cell(0, 10, "Telefonszám: +36208793145\nE-mail cím: mozitown@gmail.com")
                self.ln(10)
                self.set_font("Helvetica", "B", 13)
                self.multi_cell(0, 5, "A jegy módosítására vagy törlésére lehetoséget ajánlunk a jegy megvásárlását követo harmadik napig személyesen vagy emailben.. Ha a kiválasztott jegy korábbra szól, mint három nap, visszaváltásra csak mozinkban van lehetoség, a film kezdete elott legalább 3 órával.")
                self.ln(10)
                self.set_font("Times", "B", 15)
                self.set_text_color(255, 0, 0)
                self.cell(0, 5, "Köszönjük a vásárlást! Várjuk szeretettel!", align="C")
            def footer(self):
                self.set_y(-15)
                self.set_font("Helvetica", "I", 10)
                self.set_text_color(0, 0, 0)
                self.cell(0, 10, f"{date:%Y, %B, %d}", align="C")
        pdf = PDF("P", "mm", "A4")
        pdf.set_title(title)
        pdf.set_author("Mozitown csapata")
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.body()
        pdf.output("pdf_dune.pdf")
        siker=messagebox.showinfo("Sikeres foglalás","Foglalásodat sikeresen rögzítettük!")

    except:
        error=messagebox.showerror("Email cim","Adjon meg email címet!")

def pdf_most():
    try:
        title = "Foglalás"

        terem = "1"
        class PDF(FPDF):
            
            def header(self):
                self.image("logo.png", 5, 5, 50, 50)
                self.set_font("Helvetica", "BU", 20)
                self.cell(40)
                title_w = self.get_string_width(title) + 6
                doc_w = self.w
                self.set_x((doc_w - title_w) / 2)
                self.set_line_width(1)
                self.cell(title_w, 45, title, align="C")
                self.set_font("Helvetica", "", 10)
                self.cell(40)
                self.multi_cell(0, 7, "MoziTown Kft.\n8200, Veszprém, Iskola utca 4.\nMinden jog fenntartva!", align="R")
                self.ln(40)
            def body(self):
                self.set_font("Helvetica", "BU", 15)
                self.cell(0, 5, "Részletek:")
                self.ln(10)
                self.set_font("Times", "", 13)
                self.multi_cell(0, 10, "Vásárló E-mail címe: " + email +" \nFilm neve: MOST VAGY SOHA!\nFilm hossza: 135 perc\nIdopont: Valamikor\nTerem száma: " + terem +"\nSzékek száma: "+str(most_fog_szek))
                self.image("most.png", 130, 75, 70, 100)
                self.ln(40)
                self.set_font("Helvetica", "BU", 15)
                self.cell(0, 5, "Elérhetoségek:")
                self.ln(10)
                self.set_font("Times", "", 13)
                self.multi_cell(0, 10, "Telefonszám: +36208793145\nE-mail cím: mozitown@gmail.com")
                self.ln(10)
                self.set_font("Helvetica", "B", 13)
                self.multi_cell(0, 5, "A jegy módosítására vagy törlésére lehetoséget ajánlunk a jegy megvásárlását követo harmadik napig személyesen vagy emailben.. Ha a kiválasztott jegy korábbra szól, mint három nap, visszaváltásra csak mozinkban van lehetoség, a film kezdete elott legalább 3 órával.")
                self.ln(10)
                self.set_font("Times", "B", 15)
                self.set_text_color(255, 0, 0)
                self.cell(0, 5, "Köszönjük a vásárlást! Várjuk szeretettel!", align="C")
            def footer(self):
                self.set_y(-15)
                self.set_font("Helvetica", "I", 10)
                self.set_text_color(0, 0, 0)
                self.cell(0, 10, f"{date:%Y, %B, %d}", align="C")
        pdf = PDF("P", "mm", "A4")
        pdf.set_title(title)
        pdf.set_author("Mozitown csapata")
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.body()
        pdf.output("pdf_most.pdf")
        siker=messagebox.showinfo("Sikeres foglalás","Foglalásodat sikeresen rögzítettük!")
    except:
        error=messagebox.showerror("Email cim","Adjon meg email címet!")


def pdf_imadlak():
    try:
        title = "Foglalás"

        terem = "2"
        class PDF(FPDF):
            
            def header(self):
                self.image("logo.png", 5, 5, 50, 50)
                self.set_font("Helvetica", "BU", 20)
                self.cell(40)
                title_w = self.get_string_width(title) + 6
                doc_w = self.w
                self.set_x((doc_w - title_w) / 2)
                self.set_line_width(1)
                self.cell(title_w, 45, title, align="C")
                self.set_font("Helvetica", "", 10)
                self.cell(40)
                self.multi_cell(0, 7, "MoziTown Kft.\n8200, Veszprém, Iskola utca 4.\nMinden jog fenntartva!", align="R")
                self.ln(40)
            def body(self):
                self.set_font("Helvetica", "BU", 15)
                self.cell(0, 5, "Részletek:")
                self.ln(10)
                self.set_font("Times", "", 13)
                self.multi_cell(0, 10, "Vásárló E-mail címe: " + email +" \nFilm neve: IMÁDLAK UTÁLNI\nFilm hossza: 100 perc\nIdopont: Valamikor\nTerem száma:" + terem + "\nSzékek száma: "+str(imadlak_fog_szek))
                self.image("imadlak.png", 130, 75, 70, 100)
                self.ln(40)
                self.set_font("Helvetica", "BU", 15)
                self.cell(0, 5, "Elérhetoségek:")
                self.ln(10)
                self.set_font("Times", "", 13)
                self.multi_cell(0, 10, "Telefonszám: +36208793145\nE-mail cím: mozitown@gmail.com")
                self.ln(10)
                self.set_font("Helvetica", "B", 13)
                self.multi_cell(0, 5, "A jegy módosítására vagy törlésére lehetoséget ajánlunk a jegy megvásárlását követo harmadik napig személyesen vagy emailben.. Ha a kiválasztott jegy korábbra szól, mint három nap, visszaváltásra csak mozinkban van lehetoség, a film kezdete elott legalább 3 órával.")
                self.ln(10)
                self.set_font("Times", "B", 15)
                self.set_text_color(255, 0, 0)
                self.cell(0, 5, "Köszönjük a vásárlást! Várjuk szeretettel!", align="C")
            def footer(self):
                self.set_y(-15)
                self.set_font("Helvetica", "I", 10)
                self.set_text_color(0, 0, 0)
                self.cell(0, 10, f"{date:%Y, %B, %d}", align="C")
        pdf = PDF("P", "mm", "A4")
        pdf.set_title(title)
        pdf.set_author("Mozitown csapata")
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.body()
        pdf.output("pdf_imadlak.pdf")
        siker=messagebox.showinfo("Sikeres foglalás","Foglalásodat sikeresen rögzítettük!")
    except:
        error=messagebox.showerror("Email cim","Adjon meg email címet!")


def pdf_mehesz():
    try:
        title = "Foglalás"

        terem = "2"
        class PDF(FPDF):
            def header(self):
                self.image("logo.png", 5, 5, 50, 50)
                self.set_font("Helvetica", "BU", 20)
                self.cell(40)
                title_w = self.get_string_width(title) + 6
                doc_w = self.w
                self.set_x((doc_w - title_w) / 2)
                self.set_line_width(1)
                self.cell(title_w, 45, title, align="C")
                self.set_font("Helvetica", "", 10)
                self.cell(40)
                self.multi_cell(0, 7, "MoziTown Kft.\n8200, Veszprém, Iskola utca 4.\nMinden jog fenntartva!", align="R")
                self.ln(40)
            def body(self):
                self.set_font("Helvetica", "BU", 15)
                self.cell(0, 5, "Részletek:")
                self.ln(10)
                self.set_font("Times", "", 13)
                self.multi_cell(0, 10, "Vásárló E-mail címe: " + email +" \nFilm neve: A MÉHÉSZ\nFilm hossza: 105 perc\nIdopont: Valamikor\nTerem száma: " + terem +"\nSzékek száma: "+str(mehesz_fog_szek))
                self.image("mehesz.png", 130, 75, 70, 100)
                self.ln(40)
                self.set_font("Helvetica", "BU", 15)
                self.cell(0, 5, "Elérhetoségek:")
                self.ln(10)
                self.set_font("Times", "", 13)
                self.multi_cell(0, 10, "Telefonszám: +36208793145\nE-mail cím: mozitown@gmail.com")
                self.ln(10)
                self.set_font("Helvetica", "B", 13)
                self.multi_cell(0, 5, "A jegy módosítására vagy törlésére lehetoséget ajánlunk a jegy megvásárlását követo harmadik napig személyesen vagy emailben.. Ha a kiválasztott jegy korábbra szól, mint három nap, visszaváltásra csak mozinkban van lehetoség, a film kezdete elott legalább 3 órával.")
                self.ln(10)
                self.set_font("Times", "B", 15)
                self.set_text_color(255, 0, 0)
                self.cell(0, 5, "Köszönjük a vásárlást! Várjuk szeretettel!", align="C")
            def footer(self):
                self.set_y(-15)
                self.set_font("Helvetica", "I", 10)
                self.set_text_color(0, 0, 0)
                self.cell(0, 10, f"{date:%Y, %B, %d}", align="C")
        pdf = PDF("P", "mm", "A4")
        pdf.set_title(title)
        pdf.set_author("Mozitown csapata")
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.body()
        pdf.output("pdf_mehesz.pdf")
        siker=messagebox.showinfo("Sikeres foglalás","Foglalásodat sikeresen rögzítettük!")
    except:
        error=messagebox.showerror("Email cim","Adjon meg email címet!")


def pdf_king():
    try:
        title = "Foglalás"

        terem = "3"
        class PDF(FPDF):
            def header(self):
                self.image("logo.png", 5, 5, 50, 50)
                self.set_font("Helvetica", "BU", 20)
                self.cell(40)
                title_w = self.get_string_width(title) + 6
                doc_w = self.w
                self.set_x((doc_w - title_w) / 2)
                self.set_line_width(1)
                self.cell(title_w, 45, title, align="C")
                self.set_font("Helvetica", "", 10)
                self.cell(40)
                self.multi_cell(0, 7, "MoziTown Kft.\n8200, Veszprém, Iskola utca 4.\nMinden jog fenntartva!", align="R")
                self.ln(40)
            def body(self):
                self.set_font("Helvetica", "BU", 15)
                self.cell(0, 5, "Részletek:")
                self.ln(10)
                self.set_font("Times", "", 13)
                self.multi_cell(0, 10, "Vásárló E-mail címe: " + email +" \nFilm neve: ARTÚR, A KIRÁLY\nFilm hossza: 107 perc\nIdopont: Valamikor\nTerem száma: " + terem +"\nSzékek száma: "+str(king_fog_szek))
                self.image("king.png", 130, 75, 70, 100)
                self.ln(40)
                self.set_font("Helvetica", "BU", 15)
                self.cell(0, 5, "Elérhetoségek:")
                self.ln(10)
                self.set_font("Times", "", 13)
                self.multi_cell(0, 10, "Telefonszám: +36208793145\nE-mail cím: mozitown@gmail.com")
                self.ln(10)
                self.set_font("Helvetica", "B", 13)
                self.multi_cell(0, 5, "A jegy módosítására vagy törlésére lehetoséget ajánlunk a jegy megvásárlását követo harmadik napig személyesen vagy emailben.. Ha a kiválasztott jegy korábbra szól, mint három nap, visszaváltásra csak mozinkban van lehetoség, a film kezdete elott legalább 3 órával.")
                self.ln(10)
                self.set_font("Times", "B", 15)
                self.set_text_color(255, 0, 0)
                self.cell(0, 5, "Köszönjük a vásárlást! Várjuk szeretettel!", align="C")
            def footer(self):
                self.set_y(-15)
                self.set_font("Helvetica", "I", 10)
                self.set_text_color(0, 0, 0)
                self.cell(0, 10, f"{date:%Y, %B, %d}", align="C")
        pdf = PDF("P", "mm", "A4")
        pdf.set_title(title)
        pdf.set_author("Mozitown csapata")
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.body()
        pdf.output("pdf_king.pdf")
        siker=messagebox.showinfo("Sikeres foglalás","Foglalásodat sikeresen rögzítettük!")
    except:
        error=messagebox.showerror("Email cim","Adjon meg email címet!")    



def pdf_godzilla():
    try:
        title = "Foglalás"

        terem = "3"
        class PDF(FPDF):
            def header(self):
                self.image("logo.png", 5, 5, 50, 50)
                self.set_font("Helvetica", "BU", 20)
                self.cell(40)
                title_w = self.get_string_width(title) + 6
                doc_w = self.w
                self.set_x((doc_w - title_w) / 2)
                self.set_line_width(1)
                self.cell(title_w, 45, title, align="C")
                self.set_font("Helvetica", "", 10)
                self.cell(40)
                self.multi_cell(0, 7, "MoziTown Kft.\n8200, Veszprém, Iskola utca 4.\nMinden jog fenntartva!", align="R")
                self.ln(40)
            def body(self):
                self.set_font("Helvetica", "BU", 15)
                self.cell(0, 5, "Részletek:")
                self.ln(10)
                self.set_font("Times", "", 13)
                self.multi_cell(0, 10, "Vásárló E-mail címe: " + email +" \nFilm neve: GODZILLA X KONG: AZ ÚJ BIRODALOM\nFilm hossza: 115 perc\nIdopont: Valamikor\nTerem száma: " + terem +"\nSzékek száma: "+str(godzill_fog_szek))
                self.image("godzilla.png", 130, 75, 70, 100)
                self.ln(40)
                self.set_font("Helvetica", "BU", 15)
                self.cell(0, 5, "Elérhetoségek:")
                self.ln(10)
                self.set_font("Times", "", 13)
                self.multi_cell(0, 10, "Telefonszám: +36208793145\nE-mail cím: mozitown@gmail.com")
                self.ln(10)
                self.set_font("Helvetica", "B", 13)
                self.multi_cell(0, 5, "A jegy módosítására vagy törlésére lehetoséget ajánlunk a jegy megvásárlását követo harmadik napig személyesen vagy emailben.. Ha a kiválasztott jegy korábbra szól, mint három nap, visszaváltásra csak mozinkban van lehetoség, a film kezdete elott legalább 3 órával.")
                self.ln(10)
                self.set_font("Times", "B", 15)
                self.set_text_color(255, 0, 0)
                self.cell(0, 5, "Köszönjük a vásárlást! Várjuk szeretettel!", align="C")
            def footer(self):
                self.set_y(-15)
                self.set_font("Helvetica", "I", 10)
                self.set_text_color(0, 0, 0)
                self.cell(0, 10, f"{date:%Y, %B, %d}", align="C")
        pdf = PDF("P", "mm", "A4")
        pdf.set_title(title)
        pdf.set_author("Mozitown csapata")
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.body()
        pdf.output("pdf_godzilla.pdf")
        siker=messagebox.showinfo("Sikeres foglalás","Foglalásodat sikeresen rögzítettük!")
    except:
        error=messagebox.showerror("Email cim","Adjon meg email címet!")


def pdf_panda():
    try:
        title = "Foglalás"
        terem = "4"
        class PDF(FPDF):
            def header(self):
                self.image("logo.png", 5, 5, 50, 50)
                self.set_font("Helvetica", "BU", 20)
                self.cell(40)
                title_w = self.get_string_width(title) + 6
                doc_w = self.w
                self.set_x((doc_w - title_w) / 2)
                self.set_line_width(1)
                self.cell(title_w, 45, title, align="C")
                self.set_font("Helvetica", "", 10)
                self.cell(40)
                self.multi_cell(0, 7, "MoziTown Kft.\n8200, Veszprém, Iskola utca 4.\nMinden jog fenntartva!", align="R")
                self.ln(40)
            def body(self):
                self.set_font("Helvetica", "BU", 15)
                self.cell(0, 5, "Részletek:")
                self.ln(10)
                self.set_font("Times", "", 13)
                self.multi_cell(0, 10, "Vásárló E-mail címe: " + email +" \nFilm neve: KUNG FU PANDA 4\nFilm hossza: 94 perc\nIdopont: Valamikor\nTerem száma: " + terem + "\nSzékek száma: "+str(panda_fog_szek))
                self.image("panda.png", 130, 75, 70, 100)
                self.ln(40)
                self.set_font("Helvetica", "BU", 15)
                self.cell(0, 5, "Elérhetoségek:")
                self.ln(10)
                self.set_font("Times", "", 13)
                self.multi_cell(0, 10, "Telefonszám: +36208793145\nE-mail cím: mozitown@gmail.com")
                self.ln(10)
                self.set_font("Helvetica", "B", 13)
                self.multi_cell(0, 5, "A jegy módosítására vagy törlésére lehetoséget ajánlunk a jegy megvásárlását követo harmadik napig személyesen vagy emailben.. Ha a kiválasztott jegy korábbra szól, mint három nap, visszaváltásra csak mozinkban van lehetoség, a film kezdete elott legalább 3 órával.")
                self.ln(10)
                self.set_font("Times", "B", 15)
                self.set_text_color(255, 0, 0)
                self.cell(0, 5, "Köszönjük a vásárlást! Várjuk szeretettel!", align="C")
            def footer(self):
                self.set_y(-15)
                self.set_font("Helvetica", "I", 10)
                self.set_text_color(0, 0, 0)
                self.cell(0, 10, f"{date:%Y, %B, %d}", align="C")
        pdf = PDF("P", "mm", "A4")
        pdf.set_title(title)
        pdf.set_author("Mozitown csapata")
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.body()
        pdf.output("pdf_panda.pdf")
        siker=messagebox.showinfo("Sikeres foglalás","Foglalásodat sikeresen rögzítettük!")
    except:
        error=messagebox.showerror("Email cim","Adjon meg email címet!")


def pdf_szellemirtok():
    try:
        title = "Foglalás"
        terem = "4"
        class PDF(FPDF):
            def header(self):
                self.image("logo.png", 5, 5, 50, 50)
                self.set_font("Helvetica", "BU", 20)
                self.cell(40)
                title_w = self.get_string_width(title) + 6
                doc_w = self.w
                self.set_x((doc_w - title_w) / 2)
                self.set_line_width(1)
                self.cell(title_w, 45, title, align="C")
                self.set_font("Helvetica", "", 10)
                self.cell(40)
                self.multi_cell(0, 7, "MoziTown Kft.\n8200, Veszprém, Iskola utca 4.\nMinden jog fenntartva!", align="R")
                self.ln(40)
            def body(self):
                self.set_font("Helvetica", "BU", 15)
                self.cell(0, 5, "Részletek:")
                self.ln(10)
                self.set_font("Times", "", 13)
                self.multi_cell(0, 10, "Vásárló E-mail címe: " + email +" \nFilm neve: SZELLEMIRTÓK - A BORZONGÁS BIRODALMA\nFilm hossza: 125 perc\nIdopont: Valamikor\nTerem száma: " + terem + "\nSzékek száma: "+str(szellemirtok_fog_szek))
                self.image("szellemirtok.png", 130, 75, 70, 100)
                self.ln(40)
                self.set_font("Helvetica", "BU", 15)
                self.cell(0, 5, "Elérhetoségek:")
                self.ln(10)
                self.set_font("Times", "", 13)
                self.multi_cell(0, 10, "Telefonszám: +36208793145\nE-mail cím: mozitown@gmail.com")
                self.ln(10)
                self.set_font("Helvetica", "B", 13)
                self.multi_cell(0, 5, "A jegy módosítására vagy törlésére lehetoséget ajánlunk a jegy megvásárlását követo harmadik napig személyesen vagy emailben. Ha a kiválasztott jegy korábbra szól, mint három nap, visszaváltásra csak mozinkban van lehetoség, a film kezdete elott legalább 3 órával.")
                self.ln(10)
                self.set_font("Times", "B", 15)
                self.set_text_color(255, 0, 0)
                self.cell(0, 5, "Köszönjük a vásárlást! Várjuk szeretettel!", align="C")
            def footer(self):
                self.set_y(-15)
                self.set_font("Helvetica", "I", 10)
                self.set_text_color(0, 0, 0)
                self.cell(0, 10, f"{date:%Y, %B, %d}", align="C")
        pdf = PDF("P", "mm", "A4")
        pdf.set_title(title)
        pdf.set_author("Mozitown csapata")
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.body()
        pdf.output("pdf_szellemirtok.pdf")
        siker=messagebox.showinfo("Sikeres foglalás","Foglalásodat sikeresen rögzítettük!")
    except:
        error=messagebox.showerror("Email cim","Adjon meg email címet!")


def dune_foglal_ablak():
    fog_ablak = Toplevel(root)
    fog_ablak.geometry("1000x800")
    fog_ablak.title("DŰNE - MÁSODIK RÉSZ: Foglalás")
    
    global d
    d=0
    def foglal_sz1(b):
        global d
        if b==1:
            if d==0 or d%2==0:
                szek1.config(bootstyle="warning")
                dune_fog_szek.append("1")
            else:
                szek1.config(bootstyle="primary")
                dune_fog_szek.remove("1")
        d+=1

    global d2
    d2=0
    def foglal_sz2(b):
        global d2
        if b==2:
            if d2==0 or d2%2==0:
                szek2.config(bootstyle="warning")
                dune_fog_szek.append("2")
            else:
                szek2.config(bootstyle="primary")
                dune_fog_szek.remove("2")
                
        d2+=1

    global d3
    d3=0
    def foglal_sz3(b):
        global d3
        if b==3:
            if d3==0 or d3%2==0:
                szek3.config(bootstyle="warning")
                dune_fog_szek.append("3")
            else:
                szek3.config(bootstyle="primary")
                dune_fog_szek.remove("3")
        d3+=1

    global d4
    d4=0
    def foglal_sz4(b):
        global d4
        if b==4:
            if d4==0 or d4%2==0:
                szek4.config(bootstyle="warning")
                dune_fog_szek.append("4")
            else:
                szek4.config(bootstyle="primary")
                dune_fog_szek.remove("4")
        d4+=1


    global d5
    d5=0
    def foglal_sz5(b):
        global d5
        if b==5:
            if d5==0 or d5%2==0:
                szek7.config(bootstyle="warning")
                dune_fog_szek.append("5")
            else:
                szek7.config(bootstyle="primary")
                dune_fog_szek.remove("5")
        d5+=1

    global d6
    d6=0
    def foglal_sz6(b):
        global d6
        if b==6:
            if d6==0 or d6%2==0:
                szek8.config(bootstyle="warning")
                dune_fog_szek.append("6")
            else:
                szek8.config(bootstyle="primary")
                dune_fog_szek.remove("6")
        d6+=1

    global d7
    d7=0
    def foglal_sz7(b):
        global d7
        if b==7:
            if d7==0 or d7%2==0:
                szek9.config(bootstyle="warning")
                dune_fog_szek.append("7")
            else:
                szek9.config(bootstyle="primary")
                dune_fog_szek.remove("7")
        d7+=1

    global d8
    d8=0
    def foglal_sz8(b):
        global d8
        if b==8:
            if d8==0 or d8%2==0:
                szek10.config(bootstyle="warning")
                dune_fog_szek.append("8")
            else:
                szek10.config(bootstyle="primary")
                dune_fog_szek.remove("8")
        d8+=1

#sor2
    global d9
    d9=0
    def foglal_sz9(b):
        global d9
        if b==9:
            if d9==0 or d9%2==0:
                szek11.config(bootstyle="warning")
                dune_fog_szek.append("9")
            else:
                szek11.config(bootstyle="primary")
                dune_fog_szek.remove("9")
        d9+=1

    global d10
    d10=0
    def foglal_sz10(b):
        global d10
        if b==10:
            if d10==0 or d10%2==0:
                szek12.config(bootstyle="warning")
                dune_fog_szek.append("10")
            else:
                szek12.config(bootstyle="primary")
                dune_fog_szek.remove("10")
        d10+=1

    global d11
    d11=0
    def foglal_sz11(b):
        global d11
        if b==11:
            if d11==0 or d11%2==0:
                szek13.config(bootstyle="warning")
                dune_fog_szek.append("11")
            else:
                szek13.config(bootstyle="primary")
                dune_fog_szek.remove("11")
        d11+=1

    global d12
    d12=0
    def foglal_sz12(b):
        global d12
        if b==12:
            if d12==0 or d12%2==0:
                szek14.config(bootstyle="warning")
                dune_fog_szek.append("12")
            else:
                szek14.config(bootstyle="primary")
                dune_fog_szek.remove("12")
        d12+=1


    global d13
    d13=0
    def foglal_sz13(b):
        global d13
        if b==13:
            if d13==0 or d13%2==0:
                szek17.config(bootstyle="warning")
                dune_fog_szek.append("13")
            else:
                szek17.config(bootstyle="primary")
                dune_fog_szek.remove("13")
        d13+=1

    global d14
    d14=0
    def foglal_sz14(b):
        global d14
        if b==14:
            if d14==0 or d14%2==0:
                szek18.config(bootstyle="warning")
                dune_fog_szek.append("14")
            else:
                szek18.config(bootstyle="primary")
                dune_fog_szek.remove("14")
        d14+=1

    global d15
    d15=0
    def foglal_sz15(b):
        global d15
        if b==15:
            if d15==0 or d15%2==0:
                szek19.config(bootstyle="warning")
                dune_fog_szek.append("15")
            else:
                szek19.config(bootstyle="primary")
                dune_fog_szek.remove("15")
        d15+=1

    global d16
    d16=0
    def foglal_sz16(b):
        global d16
        if b==16:
            if d16==0 or d16%2==0:
                szek20.config(bootstyle="warning")
                dune_fog_szek.append("16")
            else:
                szek20.config(bootstyle="primary")
                dune_fog_szek.remove("16")
        d16+=1


#sor3
    global d17
    d17=0
    def foglal_sz17(b):
        global d17
        if b==17:
            if d17==0 or d17%2==0:
                szek21.config(bootstyle="warning")
                dune_fog_szek.append("17")
            else:
                szek21.config(bootstyle="primary")
                dune_fog_szek.remove("17")
        d17+=1

    global d18
    d18=0
    def foglal_sz18(b):
        global d18
        if b==18:
            if d18==0 or d18%2==0:
                szek22.config(bootstyle="warning")
                dune_fog_szek.append("18")
            else:
                szek22.config(bootstyle="primary")
                dune_fog_szek.remove("18")
        d18+=1

    global d19
    d19=0
    def foglal_sz19(b):
        global d19
        if b==19:
            if d19==0 or d19%2==0:
                szek23.config(bootstyle="warning")
                dune_fog_szek.append("19")
            else:
                szek23.config(bootstyle="primary")
                dune_fog_szek.remove("19")
        d19+=1

    global d20
    d20=0
    def foglal_sz20(b):
        global d20
        if b==20:
            if d20==0 or d20%2==0:
                szek24.config(bootstyle="warning")
                dune_fog_szek.append("20")
            else:
                szek24.config(bootstyle="primary")
                dune_fog_szek.remove("20")
            d20+=1


    global d21
    d21=0
    def foglal_sz21(b):
        global d21
        if b==21:
            if d21==0 or d21%2==0:
                szek27.config(bootstyle="warning")
                dune_fog_szek.append("21")
            else:
                szek27.config(bootstyle="primary")
                dune_fog_szek.remove("21")
        d21+=1

    global d22
    d22=0
    def foglal_sz22(b):
        global d22
        if b==22:
            if d22==0 or d22%2==0:
                szek28.config(bootstyle="warning")
                dune_fog_szek.append("22")
            else:
                szek28.config(bootstyle="primary")
                dune_fog_szek.remove("22")
        d22+=1

    global d23
    d23=0
    def foglal_sz23(b):
        global d23
        if b==23:
            if d23==0 or d23%2==0:
                szek29.config(bootstyle="warning")
                dune_fog_szek.append("23")
            else:
                szek29.config(bootstyle="primary")
                dune_fog_szek.remove("23")
        d23+=1

    global d24
    d24=0
    def foglal_sz24(b):
        global d24
        if b==24:
            if d24==0 or d24%2==0:
                szek30.config(bootstyle="warning")
                dune_fog_szek.append("24")
            else:
                szek30.config(bootstyle="primary")
                dune_fog_szek.remove("24")
        d24+=1

#sor4
    
    global d25
    d25=0
    def foglal_sz25(b):
        global d25
        if b==25:
            if d25==0 or d25%2==0:
                szek31.config(bootstyle="warning")
                dune_fog_szek.append("25")
            else:
                szek31.config(bootstyle="primary")
                dune_fog_szek.remove("25")
        d25+=1

    global d26
    d26=0
    def foglal_sz26(b):
        global d26
        if b==26:
            if d26==0 or d26%2==0:
                szek32.config(bootstyle="warning")
                dune_fog_szek.append("26")
            else:
                szek32.config(bootstyle="primary")
                dune_fog_szek.remove("26")
        d26+=1

    global d27
    d27=0
    def foglal_sz27(b):
        global d27
        if b==27:
            if d27==0 or d27%2==0:
                szek33.config(bootstyle="warning")
                dune_fog_szek.append("27")
            else:
                szek33.config(bootstyle="primary")
                dune_fog_szek.remove("27")
        d27+=1

    global d28
    d28=0
    def foglal_sz28(b):
        global d28
        if b==28:
            if d28==0 or d28%2==0:
                szek34.config(bootstyle="warning")
                dune_fog_szek.append("28")
            else:
                szek34.config(bootstyle="primary")
                dune_fog_szek.remove("28")
        d28+=1


    global d29
    d29=0
    def foglal_sz29(b):
        global d29
        if b==29:
            if d29==0 or d29%2==0:
                szek37.config(bootstyle="warning")
                dune_fog_szek.append("29")
            else:
                szek37.config(bootstyle="primary")
                dune_fog_szek.remove("29")
        d29+=1

    global d30
    d30=0
    def foglal_sz30(b):
        global d30
        if b==30:
            if d30==0 or d30%2==0:
                szek38.config(bootstyle="warning")
                dune_fog_szek.append("30")
            else:
                szek38.config(bootstyle="primary")
                dune_fog_szek.remove("30")
        d30+=1

    global d31
    d31=0
    def foglal_sz31(b):
        global d31
        if b==31:
            if d31==0 or d31%2==0:
                szek39.config(bootstyle="warning")
                dune_fog_szek.append("31")
            else:
                szek39.config(bootstyle="primary")
                dune_fog_szek.remove("31")
        d31+=1

    global d32
    d32=0
    def foglal_sz32(b):
        global d32
        if b==32:
            if d32==0 or d32%2==0:
                szek40.config(bootstyle="warning")
                dune_fog_szek.append("32")
            else:
                szek40.config(bootstyle="primary")
                dune_fog_szek.remove("32")
        d32+=1

#sor5
    global d33
    d33=0
    def foglal_sz33(b):
        global d33
        if b==33:
            if d33==0 or d33%2==0:
                szek41.config(bootstyle="warning")
                dune_fog_szek.append("33")
            else:
                szek41.config(bootstyle="primary")
                dune_fog_szek.remove("33")
        d33+=1

    global d34
    d34=0
    def foglal_sz34(b):
        global d34
        if b==34:
            if d34==0 or d34%2==0:
                szek42.config(bootstyle="warning")
                dune_fog_szek.append("34")
            else:
                szek42.config(bootstyle="primary")
                dune_fog_szek.remove("34")
        d34+=1

    global d35
    d35=0
    def foglal_sz35(b):
        global d35
        if b==35:
            if d35==0 or d35%2==0:
                szek43.config(bootstyle="warning")
                dune_fog_szek.append("35")
            else:
                szek43.config(bootstyle="primary")
                dune_fog_szek.remove("35")
        d35+=1

    global d36
    d36=0
    def foglal_sz36(b):
        global d36
        if b==36:
            if d36==0 or d36%2==0:
                szek44.config(bootstyle="warning")
                dune_fog_szek.append("36")
            else:
                szek44.config(bootstyle="primary")
                dune_fog_szek.remove("36")
        d36+=1


    global d37
    d37=0
    def foglal_sz37(b):
        global d37
        if b==37:
            if d37==0 or d37%2==0:
                szek45.config(bootstyle="warning")
                dune_fog_szek.append("37")
            else:
                szek45.config(bootstyle="primary")
                dune_fog_szek.remove("37")
        d37+=1

    global d38
    d38=0
    def foglal_sz38(b):
        global d38
        if b==38:
            if d38==0 or d38%2==0:
                szek46.config(bootstyle="warning")
                dune_fog_szek.append("38")
            else:
                szek46.config(bootstyle="primary")
                dune_fog_szek.remove("38")
        d38+=1

    global d39
    d39=0
    def foglal_sz39(b):
        global d39
        if b==39:
            if d39==0 or d39%2==0:
                szek47.config(bootstyle="warning")
                dune_fog_szek.append("39")
            else:
                szek47.config(bootstyle="primary")
                dune_fog_szek.remove("39")
        d39+=1

    global d40
    d40=0
    def foglal_sz40(b):
        global d40
        if b==40:
            if d40==0 or d40%2==0:
                szek48.config(bootstyle="warning")
                dune_fog_szek.append("40")
            else:
                szek48.config(bootstyle="primary")
                dune_fog_szek.remove("40")
        d40+=1

    global d41
    d41=0
    def foglal_sz41(b):
        global d41
        if b==41:
            if d41==0 or d41%2==0:
                szek49.config(bootstyle="warning")
                dune_fog_szek.append("41")
            else:
                szek49.config(bootstyle="primary")
                dune_fog_szek.remove("41")
        d41+=1

    global d42
    d42=0
    def foglal_sz42(b):
        global d42
        if b==42:
            if d42==0 or d42%2==0:
                szek50.config(bootstyle="warning")
                dune_fog_szek.append("42")
            else:
                szek50.config(bootstyle="primary")
                dune_fog_szek.remove("42")
        d42+=1

    fcimkeret = LabelFrame(fog_ablak, border=0, padding=0, borderwidth=0)
    fcimkeret.grid(row=0, column=0, columnspan=2)
    Label.columnconfigure(fcimkeret, 1, weight=1)
    fcim = Label(fcimkeret, text="DŰNE - MÁSODIK RÉSZ", font=("Terminal", 20, "bold"), justify="center", anchor="center", width=90)
    fcim.grid(row=0, column=0, pady=5, sticky="nesw")

    fkepkeret = LabelFrame(fog_ablak, height=370, border=0, padding=0, borderwidth=0)
    fkepkeret.grid(row=1, column=0, padx=50, pady=100)
    dune_al = Canvas(fkepkeret, width=250, height=370, bg='white')
    dune_al.grid(row=0, column=0)
    dune_al.create_image(0, 0, anchor=NW, image=img1)
    sadas=Meter(fkepkeret,bootstyle="warning")
    sadas.grid(row=1, column=0, pady=10)

    fkeret = LabelFrame(fog_ablak, padding=10)
    fkeret.grid(row=1, column=1)
    fleiras = Label(fkeret, text="A távoli jövőben, a bolygóközi királyságok korában játszódó történetben két nagyhatalmú uralkodóház harcol az Arrakis bolygó feletti hatalomért, mert az ismert univerzumban egyedül az itteni végtelen sivatagban bányászható az a fűszer, amely lehetővé teszi a csillagközi utazást. A Harkonnenek ura kiirtatta az Atreides családot. De Paul Atreides herceg (Timothée Chalamet) megmenekült: a pusztaságban bujkál egy titokzatos, nomád nép, a fremenek között, ahol megismerkedik egy lánnyal, Csanival (Zendaya). Az a sorsa, hogy bosszút álljon a családjáért, háborúba vezesse a hozzá hű seregeket. Döntenie kell, hogy élete nagy szerelmét választja-e, vagy beteljesíti a végzetét. Az univerzum sorsa múlik azon, hogy mit határoz: és végül olyan útra lép, amely megváltoztathatja azt a szörnyű jövőt, amelyet egyedül ő lát előre.", font=("Times", 12, "bold"), width=50, justify="left", wraplength=400)
    fleiras.grid(row=0, column=0, columnspan=10)
    szek1 = Button(fkeret, state=NORMAL, text="01" ,command=lambda:foglal_sz1(1))
    szek1.grid(row=1, column=0, pady=10)
    szek2 = Button(fkeret, state=NORMAL, text="02", command=lambda:foglal_sz2(2))
    szek2.grid(row=1, column=1)
    szek3 = Button(fkeret, state=NORMAL, text="03", command=lambda:foglal_sz3(3))
    szek3.grid(row=1, column=2)
    szek4 = Button(fkeret, state=NORMAL, text="04", command=lambda:foglal_sz4(4))
    szek4.grid(row=1, column=3)
    szek5 = Label(fkeret, width=0)
    szek5.grid(row=1, column=4)
    szek6 = Label(fkeret, width=0)
    szek6.grid(row=1, column=5)
    szek7 = Button(fkeret, state=NORMAL, text="05", command=lambda:foglal_sz5(5))
    szek7.grid(row=1, column=6)
    szek8 = Button(fkeret, state=NORMAL, text="06" , command=lambda:foglal_sz6(6))
    szek8.grid(row=1, column=7)
    szek9 = Button(fkeret, state=NORMAL, text="07" , command=lambda:foglal_sz7(7))
    szek9.grid(row=1, column=8)
    szek10 = Button(fkeret, state=NORMAL, text="08", command=lambda:foglal_sz8(8))
    szek10.grid(row=1, column=9)
    szek11 = Button(fkeret, state=NORMAL, text="09", command=lambda:foglal_sz9(9))
    szek11.grid(row=2, column=0, pady=10)
    szek12 = Button(fkeret, state=NORMAL, text="10", command=lambda:foglal_sz10(10))
    szek12.grid(row=2, column=1)
    szek13 = Button(fkeret, state=NORMAL, text="11" , command=lambda:foglal_sz11(11))
    szek13.grid(row=2, column=2)
    szek14 = Button(fkeret, state=NORMAL, text="12", command=lambda:foglal_sz12(12))
    szek14.grid(row=2, column=3)
    szek15 = Label(fkeret, width=0)
    szek15.grid(row=2, column=4)
    szek16 = Label(fkeret, width=0)
    szek16.grid(row=2, column=5)
    szek17 = Button(fkeret, state=NORMAL, text="13" , command=lambda:foglal_sz13(13))
    szek17.grid(row=2, column=6)
    szek18 = Button(fkeret, state=NORMAL, text="14" , command=lambda:foglal_sz14(14))
    szek18.grid(row=2, column=7)
    szek19 = Button(fkeret, state=NORMAL, text="15", command=lambda:foglal_sz15(15))
    szek19.grid(row=2, column=8)
    szek20 = Button(fkeret, state=NORMAL, text="16", command=lambda:foglal_sz16(16))
    szek20.grid(row=2, column=9)
    szek21 = Button(fkeret, state=NORMAL, text="17", command=lambda:foglal_sz17(17))
    szek21.grid(row=3, column=0, pady=10)
    szek22 = Button(fkeret, state=NORMAL, text="18", command=lambda:foglal_sz18(18))
    szek22.grid(row=3, column=1)
    szek23 = Button(fkeret, state=NORMAL, text="19", command=lambda:foglal_sz19(19))
    szek23.grid(row=3, column=2)
    szek24 = Button(fkeret, state=NORMAL, text="20", command=lambda:foglal_sz20(20))
    szek24.grid(row=3, column=3)
    szek25 = Label(fkeret, width=0)
    szek25.grid(row=3, column=4)
    szek26 = Label(fkeret, width=0)
    szek26.grid(row=3, column=5)
    szek27 = Button(fkeret, state=NORMAL, text="21", command=lambda:foglal_sz21(21))
    szek27.grid(row=3, column=6)
    szek28 = Button(fkeret, state=NORMAL, text="22", command=lambda:foglal_sz22(22))
    szek28.grid(row=3, column=7)
    szek29 = Button(fkeret, state=NORMAL, text="23", command=lambda:foglal_sz23(23))
    szek29.grid(row=3, column=8)
    szek30 = Button(fkeret, state=NORMAL, text="24", command=lambda:foglal_sz24(24))
    szek30.grid(row=3, column=9)
    szek31 = Button(fkeret, state=NORMAL, text="25", command=lambda:foglal_sz25(25))
    szek31.grid(row=4, column=0, pady=10)
    szek32 = Button(fkeret, state=NORMAL, text="26", command=lambda:foglal_sz26(26))
    szek32.grid(row=4, column=1)
    szek33 = Button(fkeret, state=NORMAL, text="27", command=lambda:foglal_sz27(27))
    szek33.grid(row=4, column=2)
    szek34 = Button(fkeret, state=NORMAL, text="28", command=lambda:foglal_sz28(28))
    szek34.grid(row=4, column=3)
    szek35 = Label(fkeret, width=0)
    szek35.grid(row=4, column=4)
    szek36 = Label(fkeret, width=0)
    szek36.grid(row=4, column=5)
    szek37 = Button(fkeret, state=NORMAL, text="29" , command=lambda:foglal_sz29(29))
    szek37.grid(row=4, column=6)
    szek38 = Button(fkeret, state=NORMAL, text="30", command=lambda:foglal_sz30(30))
    szek38.grid(row=4, column=7)
    szek39 = Button(fkeret, state=NORMAL, text="31" , command=lambda:foglal_sz31(31))
    szek39.grid(row=4, column=8)
    szek40 = Button(fkeret, state=NORMAL, text="32", command=lambda:foglal_sz32(32))
    szek40.grid(row=4, column=9)
    szek41 = Button(fkeret, state=NORMAL, text="33" , command=lambda:foglal_sz33(33))
    szek41.grid(row=5, column=0, pady=10)
    szek42 = Button(fkeret, state=NORMAL, text="34", command=lambda:foglal_sz34(34))
    szek42.grid(row=5, column=1)
    szek43 = Button(fkeret, state=NORMAL, text="35", command=lambda:foglal_sz35(35))
    szek43.grid(row=5, column=2)
    szek44 = Button(fkeret, state=NORMAL, text="36", command=lambda:foglal_sz36(36))
    szek44.grid(row=5, column=3)
    szek45 = Button(fkeret, state=NORMAL, text="37", command=lambda:foglal_sz37(37))
    szek45.grid(row=5, column=4)
    szek46 = Button(fkeret, state=NORMAL, text="38", command=lambda:foglal_sz38(38))
    szek46.grid(row=5, column=5)
    szek47 = Button(fkeret, state=NORMAL, text="39", command=lambda:foglal_sz39(39))
    szek47.grid(row=5, column=6)
    szek48 = Button(fkeret, state=NORMAL, text="40", command=lambda:foglal_sz40(40))
    szek48.grid(row=5, column=7)
    szek49 = Button(fkeret, state=NORMAL, text="41", command=lambda:foglal_sz41(41))
    szek49.grid(row=5, column=8)
    szek50 = Button(fkeret, state=NORMAL, text="42", command=lambda:foglal_sz42(42))
    szek50.grid(row=5, column=9)
    ffoglal = Button(fkeret, text="Helyet foglalok", bootstyle="info", command= lambda:pdf_dune())
    ffoglal.grid(row=6, column=0, columnspan=10, pady=10)

def most_foglal_ablak():

    fog_ablak = Toplevel(root)
    fog_ablak.geometry("1000x800")
    fog_ablak.title("MOST VAGY SOHA!: Foglalás")

    global mo
    mo=0
    def foglal_sz1(b):
        global mo
        if b==1:
            if mo==0 or mo%2==0:
                szek1.config(bootstyle="warning")
                most_fog_szek.append("1")
            else:
                szek1.config(bootstyle="primary")
                most_fog_szek.remove("1")
        mo+=1

    global mo2
    mo2=0
    def foglal_sz2(b):
        global mo2
        if b==2:
            if mo2==0 or mo2%2==0:
                szek2.config(bootstyle="warning")
                most_fog_szek.append("2")
            else:
                szek2.config(bootstyle="primary")
                most_fog_szek.remove("2")
        mo2+=1

    global mo3
    mo3=0
    def foglal_sz3(b):
        global mo3
        if b==3:
            if mo3==0 or mo3%2==0:
                szek3.config(bootstyle="warning")
                most_fog_szek.append("3")
            else:
                szek3.config(bootstyle="primary")
                most_fog_szek.remove("3")
        mo3+=1

    global mo4
    mo4=0
    def foglal_sz4(b):
        global mo4
        if b==4:
            if mo4==0 or mo4%2==0:
                szek4.config(bootstyle="warning")
                most_fog_szek.append("4")
            else:
                szek4.config(bootstyle="primary")
                most_fog_szek.remove("4")
        mo4+=1


    global mo5
    mo5=0
    def foglal_sz5(b):
        global mo5
        if b==5:
            if mo5==0 or mo5%2==0:
                szek7.config(bootstyle="warning")
                most_fog_szek.append("5")
            else:
                szek7.config(bootstyle="primary")
                most_fog_szek.remove("5")
        mo5+=1

    global mo6
    mo6=0
    def foglal_sz6(b):
        global mo6
        if b==6:
            if mo6==0 or mo6%2==0:
                szek8.config(bootstyle="warning")
                most_fog_szek.append("6")
            else:
                szek8.config(bootstyle="primary")
                most_fog_szek.remove("6")
        mo6+=1

    global mo7
    mo7=0
    def foglal_sz7(b):
        global mo7
        if b==7:
            if mo7==0 or mo7%2==0:
                szek9.config(bootstyle="warning")
                most_fog_szek.append("7")
            else:
                szek9.config(bootstyle="primary")
                most_fog_szek.remove("7")
        mo7+=1

    global mo8
    mo8=0
    def foglal_sz8(b):
        global mo8
        if b==8:
            if mo8==0 or mo8%2==0:
                szek10.config(bootstyle="warning")
                most_fog_szek.append("8")
            else:
                szek10.config(bootstyle="primary")
                most_fog_szek.remove("8")
        mo8+=1

#sor2
    global mo9
    mo9=0
    def foglal_sz9(b):
        global mo9
        if b==9:
            if mo9==0 or mo9%2==0:
                szek11.config(bootstyle="warning")
                most_fog_szek.append("9")
            else:
                szek11.config(bootstyle="primary")
                most_fog_szek.remove("9")
        mo9+=1

    global mo10
    mo10=0
    def foglal_sz10(b):
        global mo10
        if b==10:
            if mo10==0 or mo10%2==0:
                szek12.config(bootstyle="warning")
                most_fog_szek.append("10")
            else:
                szek12.config(bootstyle="primary")
                most_fog_szek.remove("10")
        mo10+=1

    global mo11
    mo11=0
    def foglal_sz11(b):
        global mo11
        if b==11:
            if mo11==0 or mo11%2==0:
                szek13.config(bootstyle="warning")
                most_fog_szek.append("11")
            else:
                szek13.config(bootstyle="primary")
                most_fog_szek.remove("11")
        mo11+=1

    global mo12
    mo12=0
    def foglal_sz12(b):
        global mo12
        if b==12:
            if mo12==0 or mo12%2==0:
                szek14.config(bootstyle="warning")
                most_fog_szek.append("12")
            else:
                szek14.config(bootstyle="primary")
                most_fog_szek.remove("12")
        mo12+=1


    global mo13
    mo13=0
    def foglal_sz13(b):
        global mo13
        if b==13:
            if mo13==0 or mo13%2==0:
                szek17.config(bootstyle="warning")
                most_fog_szek.append("13")
            else:
                szek17.config(bootstyle="primary")
                most_fog_szek.remove("13")
        mo13+=1

    global mo14
    mo14=0
    def foglal_sz14(b):
        global mo14
        if b==14:
            if mo14==0 or mo14%2==0:
                szek18.config(bootstyle="warning")
                most_fog_szek.append("14")
            else:
                szek18.config(bootstyle="primary")
                most_fog_szek.remove("14")
        mo14+=1

    global mo15
    mo15=0
    def foglal_sz15(b):
        global mo15
        if b==15:
            if mo15==0 or mo15%2==0:
                szek19.config(bootstyle="warning")
                most_fog_szek.append("15")
            else:
                szek19.config(bootstyle="primary")
                most_fog_szek.remove("15")
        mo15+=1

    global mo16
    mo16=0
    def foglal_sz16(b):
        global mo16
        if b==16:
            if mo16==0 or mo16%2==0:
                szek20.config(bootstyle="warning")
                most_fog_szek.append("16")
            else:
                szek20.config(bootstyle="primary")
                most_fog_szek.remove("16")
        mo16+=1


#sor3
    global mo17
    mo17=0
    def foglal_sz17(b):
        global mo17
        if b==17:
            if mo17==0 or mo17%2==0:
                szek21.config(bootstyle="warning")
                most_fog_szek.append("17")
            else:
                szek21.config(bootstyle="primary")
                most_fog_szek.remove("17")
        mo17+=1

    global mo18
    mo18=0
    def foglal_sz18(b):
        global mo18
        if b==18:
            if mo18==0 or mo18%2==0:
                szek22.config(bootstyle="warning")
                most_fog_szek.append("18")
            else:
                szek22.config(bootstyle="primary")
                most_fog_szek.remove("18")
        mo18+=1

    global mo19
    mo19=0
    def foglal_sz19(b):
        global mo19
        if b==19:
            if mo19==0 or mo19%2==0:
                szek23.config(bootstyle="warning")
                most_fog_szek.append("19")
            else:
                szek23.config(bootstyle="primary")
                most_fog_szek.remove("19")
        mo19+=1

    global mo20
    mo20=0
    def foglal_sz20(b):
        global mo20
        if b==20:
            if mo20==0 or mo20%2==0:
                szek24.config(bootstyle="warning")
                most_fog_szek.append("20")
            else:
                szek24.config(bootstyle="primary")
                most_fog_szek.remove("20")
        mo20+=1


    global mo21
    mo21=0
    def foglal_sz21(b):
        global mo21
        if b==21:
            if mo21==0 or mo21%2==0:
                szek27.config(bootstyle="warning")
                most_fog_szek.append("21")
            else:
                szek27.config(bootstyle="primary")
                most_fog_szek.remove("21")
        mo21+=1

    global mo22
    mo22=0
    def foglal_sz22(b):
        global mo22
        if b==22:
            if mo22==0 or mo22%2==0:
                szek28.config(bootstyle="warning")
                most_fog_szek.append("22")
            else:
                szek28.config(bootstyle="primary")
                most_fog_szek.remove("22")
        mo22+=1

    global mo23
    mo23=0
    def foglal_sz23(b):
        global mo23
        if b==23:
            if mo23==0 or mo23%2==0:
                szek29.config(bootstyle="warning")
                most_fog_szek.append("23")
            else:
                szek29.config(bootstyle="primary")
                most_fog_szek.remove("23")
        mo23+=1

    global mo24
    mo24=0
    def foglal_sz24(b):
        global mo24
        if b==24:
            if mo24==0 or mo24%2==0:
                szek30.config(bootstyle="warning")
                most_fog_szek.append("24")
            else:
                szek30.config(bootstyle="primary")
                most_fog_szek.remove("24")
        mo24+=1

#sor4
    
    global mo25
    mo25=0
    def foglal_sz25(b):
        global mo25
        if b==25:
            if mo25==0 or mo25%2==0:
                szek31.config(bootstyle="warning")
                most_fog_szek.append("25")
            else:
                szek31.config(bootstyle="primary")
                most_fog_szek.remove("25")
        mo25+=1

    global mo26
    mo26=0
    def foglal_sz26(b):
        global mo26
        if b==26:
            if mo26==0 or mo26%2==0:
                szek32.config(bootstyle="warning")
                most_fog_szek.append("26")
            else:
                szek32.config(bootstyle="primary")
                most_fog_szek.remove("26")
        mo26+=1

    global mo27
    mo27=0
    def foglal_sz27(b):
        global mo27
        if b==27:
            if mo27==0 or mo27%2==0:
                szek33.config(bootstyle="warning")
                most_fog_szek.append("27")
            else:
                szek33.config(bootstyle="primary")
                most_fog_szek.remove("27")
        mo27+=1

    global mo28
    mo28=0
    def foglal_sz28(b):
        global mo28
        if b==28:
            if mo28==0 or mo28%2==0:
                szek34.config(bootstyle="warning")
                most_fog_szek.append("28")
            else:
                szek34.config(bootstyle="primary")
                most_fog_szek.remove("28")
        mo28+=1


    global mo29
    mo29=0
    def foglal_sz29(b):
        global mo29
        if b==29:
            if mo29==0 or mo29%2==0:
                szek37.config(bootstyle="warning")
                most_fog_szek.append("29")
            else:
                szek37.config(bootstyle="primary")
                most_fog_szek.remove("29")
        mo29+=1

    global mo30
    mo30=0
    def foglal_sz30(b):
        global mo30
        if b==30:
            if mo30==0 or mo30%2==0:
                szek38.config(bootstyle="warning")
                most_fog_szek.append("30")
            else:
                szek38.config(bootstyle="primary")
                most_fog_szek.remove("30")
        mo30+=1

    global mo31
    mo31=0
    def foglal_sz31(b):
        global mo31
        if b==31:
            if mo31==0 or mo31%2==0:
                szek39.config(bootstyle="warning")
                most_fog_szek.append("31")
            else:
                szek39.config(bootstyle="primary")
                most_fog_szek.remove("31")
        mo31+=1

    global mo32
    mo32=0
    def foglal_sz32(b):
        global mo32
        if b==32:
            if mo32==0 or mo32%2==0:
                szek40.config(bootstyle="warning")
                most_fog_szek.append("32")
            else:
                szek40.config(bootstyle="primary")
                most_fog_szek.remove("32")
        mo32+=1

#sor5
    global mo33
    mo33=0
    def foglal_sz33(b):
        global mo33
        if b==33:
            if mo33==0 or mo33%2==0:
                szek41.config(bootstyle="warning")
                most_fog_szek.append("33")
            else:
                szek41.config(bootstyle="primary")
                most_fog_szek.remove("33")
            mo33+=1

    global mo34
    mo34=0
    def foglal_sz34(b):
        global mo34
        if b==34:
            if mo34==0 or mo34%2==0:
                szek42.config(bootstyle="warning")
                most_fog_szek.append("34")
            else:
                szek42.config(bootstyle="primary")
                most_fog_szek.remove("34")
        mo34+=1

    global mo35
    mo35=0
    def foglal_sz35(b):
        global mo35
        if b==35:
            if mo35==0 or mo35%2==0:
                szek43.config(bootstyle="warning")
                most_fog_szek.append("35")
            else:
                szek43.config(bootstyle="primary")
                most_fog_szek.remove("35")
        mo35+=1

    global mo36
    mo36=0
    def foglal_sz36(b):
        global mo36
        if b==36:
            if mo36==0 or mo36%2==0:
                szek44.config(bootstyle="warning")
                most_fog_szek.append("36")
            else:
                szek44.config(bootstyle="primary")
                most_fog_szek.remove("36")
        mo36+=1


    global mo37
    mo37=0
    def foglal_sz37(b):
        global mo37
        if b==37:
            if mo37==0 or mo37%2==0:
                szek45.config(bootstyle="warning")
                most_fog_szek.append("37")
            else:
                szek45.config(bootstyle="primary")
                most_fog_szek.remove("37")
        mo37+=1

    global mo38
    mo38=0
    def foglal_sz38(b):
        global mo38
        if b==38:
            if mo38==0 or mo38%2==0:
                szek46.config(bootstyle="warning")
                most_fog_szek.append("38")
            else:
                szek46.config(bootstyle="primary")
                most_fog_szek.remove("38")
        mo38+=1

    global mo39
    mo39=0
    def foglal_sz39(b):
        global mo39
        if b==39:
            if mo39==0 or mo39%2==0:
                szek47.config(bootstyle="warning")
                most_fog_szek.append("39")
            else:
                szek47.config(bootstyle="primary")
                most_fog_szek.remove("39")
        mo39+=1

    global mo40
    mo40=0
    def foglal_sz40(b):
        global mo40
        if b==40:
            if mo40==0 or mo40%2==0:
                szek48.config(bootstyle="warning")
                most_fog_szek.append("40")
            else:
                szek48.config(bootstyle="primary")
                most_fog_szek.remove("40")
        mo40+=1

    global mo41
    mo41=0
    def foglal_sz41(b):
        global mo41
        if b==41:
            if mo41==0 or mo41%2==0:
                szek49.config(bootstyle="warning")
                most_fog_szek.append("41")
            else:
                szek49.config(bootstyle="primary")
                most_fog_szek.remove("41")
        mo41+=1

    global mo42
    mo42=0
    def foglal_sz42(b):
        global mo42
        if b==42:
            if mo42==0 or mo42%2==0:
                szek50.config(bootstyle="warning")
                most_fog_szek.append("42")
            else:
                szek50.config(bootstyle="primary")
                most_fog_szek.remove("42")
        mo42+=1

    fcimkeret = LabelFrame(fog_ablak, border=0, padding=0, borderwidth=0)
    fcimkeret.grid(row=0, column=0, columnspan=2)
    Label.columnconfigure(fcimkeret, 1, weight=1)
    fcim = Label(fcimkeret, text="MOST VAGY SOHA!", font=("Terminal", 20, "bold"), justify="center", anchor="center", width=90)
    fcim.grid(row=0, column=0, pady=5, sticky="nesw")

    fkepkeret = LabelFrame(fog_ablak, height=370, border=0, padding=0, borderwidth=0)
    fkepkeret.grid(row=1, column=0, padx=50, pady=100)
    dune_al = Canvas(fkepkeret, width=250, height=370, bg='white')
    dune_al.grid(row=0, column=0)
    dune_al.create_image(0, 0, anchor=NW, image=img2)
    sadas=Meter(fkepkeret,bootstyle="warning")
    sadas.grid(row=1, column=0, pady=10)

    fkeret = LabelFrame(fog_ablak, padding=10)
    fkeret.grid(row=1, column=1)
    fleiras = Label(fkeret, text="Amikor 1848. március 15-én a lánglelkű költő, Petőfi Sándor költeményével, a Nemzeti Dallal kirobbantja a magyar forradalmat, az osztrák elnyomók egy titkosügynököt bíznak meg a feladattal, hogy állítsa meg a felkelést.", font=("Times", 12, "bold"), width=50, justify="left", wraplength=400)
    fleiras.grid(row=0, column=0, columnspan=10)
    szek1 = Button(fkeret, state=NORMAL, text="01" ,command=lambda:foglal_sz1(1))
    szek1.grid(row=1, column=0, pady=10)
    szek2 = Button(fkeret, state=NORMAL, text="02", command=lambda:foglal_sz2(2))
    szek2.grid(row=1, column=1)
    szek3 = Button(fkeret, state=NORMAL, text="03", command=lambda:foglal_sz3(3))
    szek3.grid(row=1, column=2)
    szek4 = Button(fkeret, state=NORMAL, text="04", command=lambda:foglal_sz4(4))
    szek4.grid(row=1, column=3)
    szek5 = Label(fkeret, width=0)
    szek5.grid(row=1, column=4)
    szek6 = Label(fkeret, width=0)
    szek6.grid(row=1, column=5)
    szek7 = Button(fkeret, state=NORMAL, text="05", command=lambda:foglal_sz5(5))
    szek7.grid(row=1, column=6)
    szek8 = Button(fkeret, state=NORMAL, text="06" , command=lambda:foglal_sz6(6))
    szek8.grid(row=1, column=7)
    szek9 = Button(fkeret, state=NORMAL, text="07" , command=lambda:foglal_sz7(7))
    szek9.grid(row=1, column=8)
    szek10 = Button(fkeret, state=NORMAL, text="08", command=lambda:foglal_sz8(8))
    szek10.grid(row=1, column=9)
    szek11 = Button(fkeret, state=NORMAL, text="09", command=lambda:foglal_sz9(9))
    szek11.grid(row=2, column=0, pady=10)
    szek12 = Button(fkeret, state=NORMAL, text="10", command=lambda:foglal_sz10(10))
    szek12.grid(row=2, column=1)
    szek13 = Button(fkeret, state=NORMAL, text="11" , command=lambda:foglal_sz11(11))
    szek13.grid(row=2, column=2)
    szek14 = Button(fkeret, state=NORMAL, text="12", command=lambda:foglal_sz12(12))
    szek14.grid(row=2, column=3)
    szek15 = Label(fkeret, width=0)
    szek15.grid(row=2, column=4)
    szek16 = Label(fkeret, width=0)
    szek16.grid(row=2, column=5)
    szek17 = Button(fkeret, state=NORMAL, text="13" , command=lambda:foglal_sz13(13))
    szek17.grid(row=2, column=6)
    szek18 = Button(fkeret, state=NORMAL, text="14" , command=lambda:foglal_sz14(14))
    szek18.grid(row=2, column=7)
    szek19 = Button(fkeret, state=NORMAL, text="15", command=lambda:foglal_sz15(15))
    szek19.grid(row=2, column=8)
    szek20 = Button(fkeret, state=NORMAL, text="16", command=lambda:foglal_sz16(16))
    szek20.grid(row=2, column=9)
    szek21 = Button(fkeret, state=NORMAL, text="17", command=lambda:foglal_sz17(17))
    szek21.grid(row=3, column=0, pady=10)
    szek22 = Button(fkeret, state=NORMAL, text="18", command=lambda:foglal_sz18(18))
    szek22.grid(row=3, column=1)
    szek23 = Button(fkeret, state=NORMAL, text="19", command=lambda:foglal_sz19(19))
    szek23.grid(row=3, column=2)
    szek24 = Button(fkeret, state=NORMAL, text="20", command=lambda:foglal_sz20(20))
    szek24.grid(row=3, column=3)
    szek25 = Label(fkeret, width=0)
    szek25.grid(row=3, column=4)
    szek26 = Label(fkeret, width=0)
    szek26.grid(row=3, column=5)
    szek27 = Button(fkeret, state=NORMAL, text="21", command=lambda:foglal_sz21(21))
    szek27.grid(row=3, column=6)
    szek28 = Button(fkeret, state=NORMAL, text="22", command=lambda:foglal_sz22(22))
    szek28.grid(row=3, column=7)
    szek29 = Button(fkeret, state=NORMAL, text="23", command=lambda:foglal_sz23(23))
    szek29.grid(row=3, column=8)
    szek30 = Button(fkeret, state=NORMAL, text="24", command=lambda:foglal_sz24(24))
    szek30.grid(row=3, column=9)
    szek31 = Button(fkeret, state=NORMAL, text="25", command=lambda:foglal_sz25(25))
    szek31.grid(row=4, column=0, pady=10)
    szek32 = Button(fkeret, state=NORMAL, text="26", command=lambda:foglal_sz26(26))
    szek32.grid(row=4, column=1)
    szek33 = Button(fkeret, state=NORMAL, text="27", command=lambda:foglal_sz27(27))
    szek33.grid(row=4, column=2)
    szek34 = Button(fkeret, state=NORMAL, text="28", command=lambda:foglal_sz28(28))
    szek34.grid(row=4, column=3)
    szek35 = Label(fkeret, width=0)
    szek35.grid(row=4, column=4)
    szek36 = Label(fkeret, width=0)
    szek36.grid(row=4, column=5)
    szek37 = Button(fkeret, state=NORMAL, text="29" , command=lambda:foglal_sz29(29))
    szek37.grid(row=4, column=6)
    szek38 = Button(fkeret, state=NORMAL, text="30", command=lambda:foglal_sz30(30))
    szek38.grid(row=4, column=7)
    szek39 = Button(fkeret, state=NORMAL, text="31" , command=lambda:foglal_sz31(31))
    szek39.grid(row=4, column=8)
    szek40 = Button(fkeret, state=NORMAL, text="32", command=lambda:foglal_sz32(32))
    szek40.grid(row=4, column=9)
    szek41 = Button(fkeret, state=NORMAL, text="33" , command=lambda:foglal_sz33(33))
    szek41.grid(row=5, column=0, pady=10)
    szek42 = Button(fkeret, state=NORMAL, text="34", command=lambda:foglal_sz34(34))
    szek42.grid(row=5, column=1)
    szek43 = Button(fkeret, state=NORMAL, text="35", command=lambda:foglal_sz35(35))
    szek43.grid(row=5, column=2)
    szek44 = Button(fkeret, state=NORMAL, text="36", command=lambda:foglal_sz36(36))
    szek44.grid(row=5, column=3)
    szek45 = Button(fkeret, state=NORMAL, text="37", command=lambda:foglal_sz37(37))
    szek45.grid(row=5, column=4)
    szek46 = Button(fkeret, state=NORMAL, text="38", command=lambda:foglal_sz38(38))
    szek46.grid(row=5, column=5)
    szek47 = Button(fkeret, state=NORMAL, text="39", command=lambda:foglal_sz39(39))
    szek47.grid(row=5, column=6)
    szek48 = Button(fkeret, state=NORMAL, text="40", command=lambda:foglal_sz40(40))
    szek48.grid(row=5, column=7)
    szek49 = Button(fkeret, state=NORMAL, text="41", command=lambda:foglal_sz41(41))
    szek49.grid(row=5, column=8)
    szek50 = Button(fkeret, state=NORMAL, text="42", command=lambda:foglal_sz42(42))
    szek50.grid(row=5, column=9)
    ffoglal = Button(fkeret, text="Helyet foglalok", bootstyle="info", command= lambda:pdf_most())
    ffoglal.grid(row=6, column=0, columnspan=10, pady=10)

def imadlak_foglal_ablak():
    fog_ablak = Toplevel(root)
    fog_ablak.geometry("1000x800")
    fog_ablak.title("IMÁDLAK UTÁLNI: Foglalás")

    global im
    im=0
    def foglal_sz1(b):
        global im
        if b==1:
            if im==0 or im%2==0:
                szek1.config(bootstyle="warning")
                imadlak_fog_szek.append("1")
            else:
                szek1.config(bootstyle="primary")
                imadlak_fog_szek.remove("1")

        im+=1

    global im2
    im2=0
    def foglal_sz2(b):
        global im2
        if b==2:
            if im2==0 or im2%2==0:
                szek2.config(bootstyle="warning")
                imadlak_fog_szek.append("2")
            else:
                szek2.config(bootstyle="primary")
                imadlak_fog_szek.remove("2")
        im2+=1

    global im3
    im3=0
    def foglal_sz3(b):
        global im3
        if b==3:
            if im3==0 or im3%2==0:
                szek3.config(bootstyle="warning")
                imadlak_fog_szek.append("3")
            else:
                szek3.config(bootstyle="primary")
                imadlak_fog_szek.remove("3")
        im3+=1

    global im4
    im4=0
    def foglal_sz4(b):
        global im4
        if b==4:
            if im4==0 or im4%2==0:
                szek4.config(bootstyle="warning")
                imadlak_fog_szek.append("4")
            else:
                szek4.config(bootstyle="primary")
                imadlak_fog_szek.remove("4")
        im4+=1


    global im5
    im5=0
    def foglal_sz5(b):
        global im5
        if b==5:
            if im5==0 or im5%2==0:
                szek7.config(bootstyle="warning")
                imadlak_fog_szek.append("5")
            else:
                szek7.config(bootstyle="primary")
                imadlak_fog_szek.remove("5")
        im5+=1

    global im6
    im6=0
    def foglal_sz6(b):
        global im6
        if b==6:
            if im6==0 or im6%2==0:
                szek8.config(bootstyle="warning")
                imadlak_fog_szek.append("6")
            else:
                szek8.config(bootstyle="primary")
                imadlak_fog_szek.remove("6")
        im6+=1

    global im7
    im7=0
    def foglal_sz7(b):
        global im7
        if b==7:
            if im7==0 or im7%2==0:
                szek9.config(bootstyle="warning")
                imadlak_fog_szek.append("7")
            else:
                szek9.config(bootstyle="primary")
                imadlak_fog_szek.remove("7")
        im7+=1

    global im8
    im8=0
    def foglal_sz8(b):
        global im8
        if b==8:
            if im8==0 or im8%2==0:
                szek10.config(bootstyle="warning")
                imadlak_fog_szek.append("8")
            else:
                szek10.config(bootstyle="primary")
                imadlak_fog_szek.remove("8")
        im8+=1

#sor2
    global im9
    im9=0
    def foglal_sz9(b):
        global im9
        if b==9:
            if im9==0 or im9%2==0:
                szek11.config(bootstyle="warning")
                imadlak_fog_szek.append("9")
            else:
                szek11.config(bootstyle="primary")
                imadlak_fog_szek.remove("9")
        im9+=1

    global im10
    im10=0
    def foglal_sz10(b):
        global im10
        if b==10:
            if im10==0 or im10%2==0:
                szek12.config(bootstyle="warning")
                imadlak_fog_szek.append("10")
            else:
                szek12.config(bootstyle="primary")
                imadlak_fog_szek.remove("10")
        im10+=1

    global im11
    im11=0
    def foglal_sz11(b):
        global im11
        if b==11:
            if im11==0 or im11%2==0:
                szek13.config(bootstyle="warning")
                imadlak_fog_szek.append("11")
            else:
                szek13.config(bootstyle="primary")
                imadlak_fog_szek.remove("11")
        im11+=1

    global im12
    im12=0
    def foglal_sz12(b):
        global im12
        if b==12:
            if im12==0 or im12%2==0:
                szek14.config(bootstyle="warning")
                imadlak_fog_szek.append("12")
            else:
                szek14.config(bootstyle="primary")
                imadlak_fog_szek.remove("12")
        im12+=1


    global im13
    im13=0
    def foglal_sz13(b):
        global im13
        if b==13:
            if im13==0 or im13%2==0:
                szek17.config(bootstyle="warning")
                imadlak_fog_szek.append("13")
            else:
                szek17.config(bootstyle="primary")
                imadlak_fog_szek.remove("13")
        im13+=1

    global im14
    im14=0
    def foglal_sz14(b):
        global im14
        if b==14:
            if im14==0 or im14%2==0:
                szek18.config(bootstyle="warning")
                imadlak_fog_szek.append("14")
            else:
                szek18.config(bootstyle="primary")
                imadlak_fog_szek.remove("14")
        im14+=1

    global im15
    im15=0
    def foglal_sz15(b):
        global im15
        if b==15:
            if im15==0 or im15%2==0:
                szek19.config(bootstyle="warning")
                imadlak_fog_szek.append("15")
            else:
                szek19.config(bootstyle="primary")
                imadlak_fog_szek.remove("15")
        im15+=1

    global im16
    im16=0
    def foglal_sz16(b):
        global im16
        if b==16:
            if im16==0 or im16%2==0:
                szek20.config(bootstyle="warning")
                imadlak_fog_szek.append("16")
            else:
                szek20.config(bootstyle="primary")
                imadlak_fog_szek.remove("16")
        im16+=1


#sor3
    global im17
    im17=0
    def foglal_sz17(b):
        global im17
        if b==17:
            if im17==0 or im17%2==0:
                szek21.config(bootstyle="warning")
                imadlak_fog_szek.append("17")
            else:
                szek21.config(bootstyle="primary")
                imadlak_fog_szek.remove("17")
        im17+=1

    global im18
    im18=0
    def foglal_sz18(b):
        global im18
        if b==18:
            if im18==0 or im18%2==0:
                szek22.config(bootstyle="warning")
                imadlak_fog_szek.append("18")
            else:
                szek22.config(bootstyle="primary")
                imadlak_fog_szek.remove("18")
        im18+=1

    global im19
    im19=0
    def foglal_sz19(b):
        global im19
        if b==19:
            if im19==0 or im19%2==0:
                szek23.config(bootstyle="warning")
                imadlak_fog_szek.append("19")
            else:
                szek23.config(bootstyle="primary")
                imadlak_fog_szek.remove("19")
        im19+=1

    global im20
    im20=0
    def foglal_sz20(b):
        global im20
        if b==20:
            if im20==0 or im20%2==0:
                szek24.config(bootstyle="warning")
                imadlak_fog_szek.append("20")
            else:
                szek24.config(bootstyle="primary")
                imadlak_fog_szek.remove("20")
        im20+=1


    global im21
    im21=0
    def foglal_sz21(b):
        global im21
        if b==21:
            if im21==0 or im21%2==0:
                szek27.config(bootstyle="warning")
                imadlak_fog_szek.append("21")
            else:
                szek27.config(bootstyle="primary")
                imadlak_fog_szek.remove("21")
        im21+=1

    global im22
    im22=0
    def foglal_sz22(b):
        global im22
        if b==22:
            if im22==0 or im22%2==0:
                szek28.config(bootstyle="warning")
                imadlak_fog_szek.append("22")
            else:
                szek28.config(bootstyle="primary")
                imadlak_fog_szek.remove("22")
        im22+=1

    global im23
    im23=0
    def foglal_sz23(b):
        global im23
        if b==23:
            if im23==0 or im23%2==0:
                szek29.config(bootstyle="warning")
                imadlak_fog_szek.append("23")
            else:
                szek29.config(bootstyle="primary")
                imadlak_fog_szek.remove("23")
        im23+=1

    global im24
    im24=0
    def foglal_sz24(b):
        global im24
        if b==24:
            if im24==0 or im24%2==0:
                szek30.config(bootstyle="warning")
                imadlak_fog_szek.append("24")
            else:
                szek30.config(bootstyle="primary")
                imadlak_fog_szek.remove("24")
        im24+=1

#sor4
    
    global im25
    im25=0
    def foglal_sz25(b):
        global im25
        if b==25:
            if im25==0 or im25%2==0:
                szek31.config(bootstyle="warning")
                imadlak_fog_szek.append("25")
            else:
                szek31.config(bootstyle="primary")
                imadlak_fog_szek.remove("25")
        im25+=1

    global im26
    im26=0
    def foglal_sz26(b):
        global im26
        if b==26:
            if im26==0 or im26%2==0:
                szek32.config(bootstyle="warning")
                imadlak_fog_szek.append("26")
            else:
                szek32.config(bootstyle="primary")
                imadlak_fog_szek.remove("26")
        im26+=1

    global im27
    im27=0
    def foglal_sz27(b):
        global im27
        if b==27:
            if im27==0 or im27%2==0:
                szek33.config(bootstyle="warning")
                imadlak_fog_szek.append("27")
            else:
                szek33.config(bootstyle="primary")
                imadlak_fog_szek.remove("27")
        im27+=1

    global im28
    im28=0
    def foglal_sz28(b):
        global im28
        if b==28:
            if im28==0 or im28%2==0:
                szek34.config(bootstyle="warning")
                imadlak_fog_szek.append("28")
            else:
                szek34.config(bootstyle="primary")
                imadlak_fog_szek.remove("28")
            im28+=1


    global im29
    im29=0
    def foglal_sz29(b):
        global im29
        if b==29:
            if im29==0 or im29%2==0:
                szek37.config(bootstyle="warning")
                imadlak_fog_szek.append("29")
            else:
                szek37.config(bootstyle="primary")
                imadlak_fog_szek.remove("29")
        im29+=1

    global im30
    im30=0
    def foglal_sz30(b):
        global im30
        if b==30:
            if im30==0 or im30%2==0:
                szek38.config(bootstyle="warning")
                imadlak_fog_szek.append("30")
            else:
                szek38.config(bootstyle="primary")
                imadlak_fog_szek.remove("30")
        im30+=1

    global im31
    im31=0
    def foglal_sz31(b):
        global im31
        if b==31:
            if im31==0 or im31%2==0:
                szek39.config(bootstyle="warning")
                imadlak_fog_szek.append("31")
            else:
                szek39.config(bootstyle="primary")
                imadlak_fog_szek.remove("31")
        im31+=1

    global im32
    im32=0
    def foglal_sz32(b):
        global im32
        if b==32:
            if im32==0 or im32%2==0:
                szek40.config(bootstyle="warning")
                imadlak_fog_szek.append("32")
            else:
                szek40.config(bootstyle="primary")
                imadlak_fog_szek.remove("32")
        im32+=1

#sor5
    global im33
    im33=0
    def foglal_sz33(b):
        global im33
        if b==33:
            if im33==0 or im33%2==0:
                szek41.config(bootstyle="warning")
                imadlak_fog_szek.append("33")
            else:
                szek41.config(bootstyle="primary")
                imadlak_fog_szek.remove("33")
        im33+=1

    global im34
    im34=0
    def foglal_sz34(b):
        global im34
        if b==34:
            if im34==0 or im34%2==0:
                szek42.config(bootstyle="warning")
                imadlak_fog_szek.append("34")
            else:
                szek42.config(bootstyle="primary")
                imadlak_fog_szek.remove("34")
        im34+=1

    global im35
    im35=0
    def foglal_sz35(b):
        global im35
        if b==35:
            if im35==0 or im35%2==0:
                szek43.config(bootstyle="warning")
                imadlak_fog_szek.append("35")
            else:
                szek43.config(bootstyle="primary")
                imadlak_fog_szek.remove("35")
        im35+=1

    global im36
    im36=0
    def foglal_sz36(b):
        global im36
        if b==36:
            if im36==0 or im36%2==0:
                szek44.config(bootstyle="warning")
                imadlak_fog_szek.append("36")
            else:
                szek44.config(bootstyle="primary")
                imadlak_fog_szek.remove("36")
        im36+=1


    global im37
    im37=0
    def foglal_sz37(b):
        global im37
        if b==37:
            if im37==0 or im37%2==0:
                szek45.config(bootstyle="warning")
                imadlak_fog_szek.append("37")
            else:
                szek45.config(bootstyle="primary")
                imadlak_fog_szek.remove("37")
        im37+=1

    global im38
    im38=0
    def foglal_sz38(b):
        global im38
        if b==38:
            if im38==0 or im38%2==0:
                szek46.config(bootstyle="warning")
                imadlak_fog_szek.append("38")
            else:
                szek46.config(bootstyle="primary")
                imadlak_fog_szek.remove("38")
        im38+=1

    global im39
    im39=0
    def foglal_sz39(b):
        global im39
        if b==39:
            if im39==0 or im39%2==0:
                szek47.config(bootstyle="warning")
                imadlak_fog_szek.append("39")
            else:
                szek47.config(bootstyle="primary")
                imadlak_fog_szek.remove("39")
        im39+=1

    global im40
    im40=0
    def foglal_sz40(b):
        global im40
        if b==40:
            if im40==0 or im40%2==0:
                szek48.config(bootstyle="warning")
                imadlak_fog_szek.append("40")
            else:
                szek48.config(bootstyle="primary")
                imadlak_fog_szek.remove("40")
        im40+=1

    global im41
    im41=0
    def foglal_sz41(b):
        global im41
        if b==41:
            if im41==0 or im41%2==0:
                szek49.config(bootstyle="warning")
                imadlak_fog_szek.append("41")
            else:
                szek49.config(bootstyle="primary")
                imadlak_fog_szek.remove("41")
        im41+=1

    global im42
    im42=0
    def foglal_sz42(b):
        global im42
        if b==42:
            if im42==0 or im42%2==0:
                szek50.config(bootstyle="warning")
                imadlak_fog_szek.append("42")
            else:
                szek50.config(bootstyle="primary")
                imadlak_fog_szek.remove("42")
        im42+=1

    fcimkeret = LabelFrame(fog_ablak, border=0, padding=0, borderwidth=0)
    fcimkeret.grid(row=0, column=0, columnspan=2)
    Label.columnconfigure(fcimkeret, 1, weight=1)
    fcim = Label(fcimkeret, text="IMÁDLAK UTÁLNI", font=("Terminal", 20, "bold"), justify="center", anchor="center", width=90)
    fcim.grid(row=0, column=0, pady=5, sticky="nesw")

    fkepkeret = LabelFrame(fog_ablak, height=370, border=0, padding=0, borderwidth=0)
    fkepkeret.grid(row=1, column=0, padx=50, pady=100)
    dune_al = Canvas(fkepkeret, width=250, height=370, bg='white')
    dune_al.grid(row=0, column=0)
    dune_al.create_image(0, 0, anchor=NW, image=img3)
    sadas=Meter(fkepkeret,bootstyle="warning")
    sadas.grid(row=1, column=0, pady=10)

    fkeret = LabelFrame(fog_ablak, padding=10)
    fkeret.grid(row=1, column=1)
    fleiras = Label(fkeret, text="Találkoztak, együtt töltöttek egy éjszakát, és azóta gyűlölik egymást. Van ilyen. Bea (Sydney Sweeney) és Ben (Glen Powell) biztos, hogy nem illenek össze. Ha néha véletlenül összefutnak valahol, tutira elszabadul a pokol: csak bántani tudják egymást. De lesz egy esküvő Ausztráliában, amin mindkettejüknek részt kell venniük. Nincs kibúvó, nincs duma: utazniuk kell. Néhány napon, néhány bulin, néhány vacsorán keresztül el kell viselniük egymás közelségét, miközben egy gyönyörű tengerparti házban ott kavarog körülöttük egy csomó régi szerelmük, néhány kíváncsi rokonuk és kavarni mindig kész felmenőjük. Szóval, azt teszik, amit két érett, felnőtt, felelősségteljes ember ilyenkor tehet: úgy tesznek, mintha szerelmespár lennének - azt remélik, hogy így mindenkinek könnyebb lesz. Nem is tévedhettek volna nagyobbat.", font=("Times", 12, "bold"), width=50, justify="left", wraplength=400)
    fleiras.grid(row=0, column=0, columnspan=10)
    szek1 = Button(fkeret, state=NORMAL, text="01" ,command=lambda:foglal_sz1(1))
    szek1.grid(row=1, column=0, pady=10)
    szek2 = Button(fkeret, state=NORMAL, text="02", command=lambda:foglal_sz2(2))
    szek2.grid(row=1, column=1)
    szek3 = Button(fkeret, state=NORMAL, text="03", command=lambda:foglal_sz3(3))
    szek3.grid(row=1, column=2)
    szek4 = Button(fkeret, state=NORMAL, text="04", command=lambda:foglal_sz4(4))
    szek4.grid(row=1, column=3)
    szek5 = Label(fkeret, width=0)
    szek5.grid(row=1, column=4)
    szek6 = Label(fkeret, width=0)
    szek6.grid(row=1, column=5)
    szek7 = Button(fkeret, state=NORMAL, text="05", command=lambda:foglal_sz5(5))
    szek7.grid(row=1, column=6)
    szek8 = Button(fkeret, state=NORMAL, text="06" , command=lambda:foglal_sz6(6))
    szek8.grid(row=1, column=7)
    szek9 = Button(fkeret, state=NORMAL, text="07" , command=lambda:foglal_sz7(7))
    szek9.grid(row=1, column=8)
    szek10 = Button(fkeret, state=NORMAL, text="08", command=lambda:foglal_sz8(8))
    szek10.grid(row=1, column=9)
    szek11 = Button(fkeret, state=NORMAL, text="09", command=lambda:foglal_sz9(9))
    szek11.grid(row=2, column=0, pady=10)
    szek12 = Button(fkeret, state=NORMAL, text="10", command=lambda:foglal_sz10(10))
    szek12.grid(row=2, column=1)
    szek13 = Button(fkeret, state=NORMAL, text="11" , command=lambda:foglal_sz11(11))
    szek13.grid(row=2, column=2)
    szek14 = Button(fkeret, state=NORMAL, text="12", command=lambda:foglal_sz12(12))
    szek14.grid(row=2, column=3)
    szek15 = Label(fkeret, width=0)
    szek15.grid(row=2, column=4)
    szek16 = Label(fkeret, width=0)
    szek16.grid(row=2, column=5)
    szek17 = Button(fkeret, state=NORMAL, text="13" , command=lambda:foglal_sz13(13))
    szek17.grid(row=2, column=6)
    szek18 = Button(fkeret, state=NORMAL, text="14" , command=lambda:foglal_sz14(14))
    szek18.grid(row=2, column=7)
    szek19 = Button(fkeret, state=NORMAL, text="15", command=lambda:foglal_sz15(15))
    szek19.grid(row=2, column=8)
    szek20 = Button(fkeret, state=NORMAL, text="16", command=lambda:foglal_sz16(16))
    szek20.grid(row=2, column=9)
    szek21 = Button(fkeret, state=NORMAL, text="17", command=lambda:foglal_sz17(17))
    szek21.grid(row=3, column=0, pady=10)
    szek22 = Button(fkeret, state=NORMAL, text="18", command=lambda:foglal_sz18(18))
    szek22.grid(row=3, column=1)
    szek23 = Button(fkeret, state=NORMAL, text="19", command=lambda:foglal_sz19(19))
    szek23.grid(row=3, column=2)
    szek24 = Button(fkeret, state=NORMAL, text="20", command=lambda:foglal_sz20(20))
    szek24.grid(row=3, column=3)
    szek25 = Label(fkeret, width=0)
    szek25.grid(row=3, column=4)
    szek26 = Label(fkeret, width=0)
    szek26.grid(row=3, column=5)
    szek27 = Button(fkeret, state=NORMAL, text="21", command=lambda:foglal_sz21(21))
    szek27.grid(row=3, column=6)
    szek28 = Button(fkeret, state=NORMAL, text="22", command=lambda:foglal_sz22(22))
    szek28.grid(row=3, column=7)
    szek29 = Button(fkeret, state=NORMAL, text="23", command=lambda:foglal_sz23(23))
    szek29.grid(row=3, column=8)
    szek30 = Button(fkeret, state=NORMAL, text="24", command=lambda:foglal_sz24(24))
    szek30.grid(row=3, column=9)
    szek31 = Button(fkeret, state=NORMAL, text="25", command=lambda:foglal_sz25(25))
    szek31.grid(row=4, column=0, pady=10)
    szek32 = Button(fkeret, state=NORMAL, text="26", command=lambda:foglal_sz26(26))
    szek32.grid(row=4, column=1)
    szek33 = Button(fkeret, state=NORMAL, text="27", command=lambda:foglal_sz27(27))
    szek33.grid(row=4, column=2)
    szek34 = Button(fkeret, state=NORMAL, text="28", command=lambda:foglal_sz28(28))
    szek34.grid(row=4, column=3)
    szek35 = Label(fkeret, width=0)
    szek35.grid(row=4, column=4)
    szek36 = Label(fkeret, width=0)
    szek36.grid(row=4, column=5)
    szek37 = Button(fkeret, state=NORMAL, text="29" , command=lambda:foglal_sz29(29))
    szek37.grid(row=4, column=6)
    szek38 = Button(fkeret, state=NORMAL, text="30", command=lambda:foglal_sz30(30))
    szek38.grid(row=4, column=7)
    szek39 = Button(fkeret, state=NORMAL, text="31" , command=lambda:foglal_sz31(31))
    szek39.grid(row=4, column=8)
    szek40 = Button(fkeret, state=NORMAL, text="32", command=lambda:foglal_sz32(32))
    szek40.grid(row=4, column=9)
    szek41 = Button(fkeret, state=NORMAL, text="33" , command=lambda:foglal_sz33(33))
    szek41.grid(row=5, column=0, pady=10)
    szek42 = Button(fkeret, state=NORMAL, text="34", command=lambda:foglal_sz34(34))
    szek42.grid(row=5, column=1)
    szek43 = Button(fkeret, state=NORMAL, text="35", command=lambda:foglal_sz35(35))
    szek43.grid(row=5, column=2)
    szek44 = Button(fkeret, state=NORMAL, text="36", command=lambda:foglal_sz36(36))
    szek44.grid(row=5, column=3)
    szek45 = Button(fkeret, state=NORMAL, text="37", command=lambda:foglal_sz37(37))
    szek45.grid(row=5, column=4)
    szek46 = Button(fkeret, state=NORMAL, text="38", command=lambda:foglal_sz38(38))
    szek46.grid(row=5, column=5)
    szek47 = Button(fkeret, state=NORMAL, text="39", command=lambda:foglal_sz39(39))
    szek47.grid(row=5, column=6)
    szek48 = Button(fkeret, state=NORMAL, text="40", command=lambda:foglal_sz40(40))
    szek48.grid(row=5, column=7)
    szek49 = Button(fkeret, state=NORMAL, text="41", command=lambda:foglal_sz41(41))
    szek49.grid(row=5, column=8)
    szek50 = Button(fkeret, state=NORMAL, text="42", command=lambda:foglal_sz42(42))
    szek50.grid(row=5, column=9)
    ffoglal = Button(fkeret, text="Helyet foglalok", bootstyle="info", command= lambda:pdf_imadlak())
    ffoglal.grid(row=6, column=0, columnspan=10, pady=10)

def mehesz_foglal_ablak():
    fog_ablak = Toplevel(root)
    fog_ablak.geometry("1000x800")
    fog_ablak.title("A MÉHÉSZ: Foglalás")

    global meh
    meh=0
    def foglal_sz1(b):
        global meh
        if b==1:
            if meh==0 or meh%2==0:
                szek1.config(bootstyle="warning")
                mehesz_fog_szek.append("1")
            else:
                szek1.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("1")
        meh+=1

    global meh2
    meh2=0
    def foglal_sz2(b):
        global meh2
        if b==2:
            if meh2==0 or meh2%2==0:
                szek2.config(bootstyle="warning")
                mehesz_fog_szek.append("2")
            else:
                szek2.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("2")
        meh2+=1

    global meh3
    meh3=0
    def foglal_sz3(b):
        global meh3
        if b==3:
            if meh3==0 or meh3%2==0:
                szek3.config(bootstyle="warning")
                mehesz_fog_szek.append("3")
            else:
                szek3.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("3")
        meh3+=1

    global meh4
    meh4=0
    def foglal_sz4(b):
        global meh4
        if b==4:
            if meh4==0 or meh4%2==0:
                szek4.config(bootstyle="warning")
                mehesz_fog_szek.append("4")
            else:
                szek4.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("4")
        meh4+=1


    global meh5
    meh5=0
    def foglal_sz5(b):
        global meh5
        if b==5:
            if meh5==0 or meh5%2==0:
                szek7.config(bootstyle="warning")
                mehesz_fog_szek.append("5")
            else:
                szek7.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("5")
        meh5+=1

    global meh6
    meh6=0
    def foglal_sz6(b):
        global meh6
        if b==6:
            if meh6==0 or meh6%2==0:
                szek8.config(bootstyle="warning")
                mehesz_fog_szek.append("6")
            else:
                szek8.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("6")
        meh6+=1

    global meh7
    meh7=0
    def foglal_sz7(b):
        global meh7
        if b==7:
            if meh7==0 or meh7%2==0:
                szek9.config(bootstyle="warning")
                mehesz_fog_szek.append("7")
            else:
                szek9.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("7")
        meh7+=1

    global meh8
    meh8=0
    def foglal_sz8(b):
        global meh8
        if b==8:
            if meh8==0 or meh8%2==0:
                szek10.config(bootstyle="warning")
                mehesz_fog_szek.append("8")
            else:
                szek10.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("8")
        meh8+=1

#sor2
    global meh9
    meh9=0
    def foglal_sz9(b):
        global meh9
        if b==9:
            if meh9==0 or meh9%2==0:
                szek11.config(bootstyle="warning")
                mehesz_fog_szek.append("9")
            else:
                szek11.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("9")
        meh9+=1

    global meh10
    meh10=0
    def foglal_sz10(b):
        global meh10
        if b==10:
            if meh10==0 or meh10%2==0:
                szek12.config(bootstyle="warning")
                mehesz_fog_szek.append("10")
            else:
                szek12.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("10")
        meh10+=1

    global meh11
    meh11=0
    def foglal_sz11(b):
        global meh11
        if b==11:
            if meh11==0 or meh11%2==0:
                szek13.config(bootstyle="warning")
                mehesz_fog_szek.append("11")
            else:
                szek13.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("11")
        meh11+=1

    global meh12
    meh12=0
    def foglal_sz12(b):
        global meh12
        if b==12:
            if meh12==0 or meh12%2==0:
                szek14.config(bootstyle="warning")
                mehesz_fog_szek.append("12")
            else:
                szek14.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("12")
        meh12+=1


    global meh13
    meh13=0
    def foglal_sz13(b):
        global meh13
        if b==13:
            if meh13==0 or meh13%2==0:
                szek17.config(bootstyle="warning")
                mehesz_fog_szek.append("13")
            else:
                szek17.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("13")
        meh13+=1

    global meh14
    meh14=0
    def foglal_sz14(b):
        global meh14
        if b==14:
            if meh14==0 or meh14%2==0:
                szek18.config(bootstyle="warning")
                mehesz_fog_szek.append("14")
            else:
                szek18.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("14")
        meh14+=1

    global meh15
    meh15=0
    def foglal_sz15(b):
        global meh15
        if b==15:
            if meh15==0 or meh15%2==0:
                szek19.config(bootstyle="warning")
                mehesz_fog_szek.append("15")
            else:
                szek19.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("15")
        meh15+=1

    global meh16
    meh16=0
    def foglal_sz16(b):
        global meh16
        if b==16:
            if meh16==0 or meh16%2==0:
                szek20.config(bootstyle="warning")
                mehesz_fog_szek.append("16")
            else:
                szek20.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("16")
        meh16+=1


#sor3
    global meh17
    meh17=0
    def foglal_sz17(b):
        global meh17
        if b==17:
            if meh17==0 or meh17%2==0:
                szek21.config(bootstyle="warning")
                mehesz_fog_szek.append("17")
            else:
                szek21.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("17")
        meh17+=1

    global meh18
    meh18=0
    def foglal_sz18(b):
        global meh18
        if b==18:
            if meh18==0 or meh18%2==0:
                szek22.config(bootstyle="warning")
                mehesz_fog_szek.append("18")
            else:
                szek22.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("18")
        meh18+=1

    global meh19
    meh19=0
    def foglal_sz19(b):
        global meh19
        if b==19:
            if meh19==0 or meh19%2==0:
                szek23.config(bootstyle="warning")
                mehesz_fog_szek.append("19")
            else:
                szek23.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("19")
        meh19+=1

    global meh20
    meh20=0
    def foglal_sz20(b):
        global meh20
        if b==20:
            if meh20==0 or meh20%2==0:
                szek24.config(bootstyle="warning")
                mehesz_fog_szek.append("20")
            else:
                szek24.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("20")
        meh20+=1


    global meh21
    meh21=0
    def foglal_sz21(b):
        global meh21
        if b==21:
            if meh21==0 or meh21%2==0:
                szek27.config(bootstyle="warning")
                mehesz_fog_szek.append("21")
            else:
                szek27.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("21")
        meh21+=1

    global meh22
    meh22=0
    def foglal_sz22(b):
        global meh22
        if b==22:
            if meh22==0 or meh22%2==0:
                szek28.config(bootstyle="warning")
                mehesz_fog_szek.append("22")
            else:
                szek28.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("22")
        meh22+=1

    global meh23
    meh23=0
    def foglal_sz23(b):
        global meh23
        if b==23:
            if meh23==0 or meh23%2==0:
                szek29.config(bootstyle="warning")
                mehesz_fog_szek.append("23")
            else:
                szek29.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("23")
        meh23+=1

    global meh24
    meh24=0
    def foglal_sz24(b):
        global meh24
        if b==24:
            if meh24==0 or meh24%2==0:
                szek30.config(bootstyle="warning")
                mehesz_fog_szek.append("24")
            else:
                szek30.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("24")
        meh24+=1

#sor4
    
    global meh25
    meh25=0
    def foglal_sz25(b):
        global meh25
        if b==25:
            if meh25==0 or meh25%2==0:
                szek31.config(bootstyle="warning")
                mehesz_fog_szek.append("25")
            else:
                szek31.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("25")
        meh25+=1

    global meh26
    meh26=0
    def foglal_sz26(b):
        global meh26
        if b==26:
            if meh26==0 or meh26%2==0:
                szek32.config(bootstyle="warning")
                mehesz_fog_szek.append("26")
            else:
                szek32.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("26")
        meh26+=1

    global meh27
    meh27=0
    def foglal_sz27(b):
        global meh27
        if b==27:
            if meh27==0 or meh27%2==0:
                szek33.config(bootstyle="warning")
                mehesz_fog_szek.append("27")
            else:
                szek33.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("27")
        meh27+=1

    global meh28
    meh28=0
    def foglal_sz28(b):
        global meh28
        if b==28:
            if meh28==0 or meh28%2==0:
                szek34.config(bootstyle="warning")
                mehesz_fog_szek.append("28")
            else:
                szek34.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("28")
        meh28+=1


    global meh29
    meh29=0
    def foglal_sz29(b):
        global meh29
        if b==29:
            if meh29==0 or meh29%2==0:
                szek37.config(bootstyle="warning")
                mehesz_fog_szek.append("29")
            else:
                szek37.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("29")
        meh29+=1

    global meh30
    meh30=0
    def foglal_sz30(b):
        global meh30
        if b==30:
            if meh30==0 or meh30%2==0:
                szek38.config(bootstyle="warning")
                mehesz_fog_szek.append("30")
            else:
                szek38.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("30")
        meh30+=1

    global meh31
    meh31=0
    def foglal_sz31(b):
        global meh31
        if b==31:
            if meh31==0 or meh31%2==0:
                szek39.config(bootstyle="warning")
                mehesz_fog_szek.append("31")
            else:
                szek39.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("31")
        meh31+=1

    global meh32
    meh32=0
    def foglal_sz32(b):
        global meh32
        if b==32:
            if meh32==0 or meh32%2==0:
                szek40.config(bootstyle="warning")
                mehesz_fog_szek.append("32")
            else:
                szek40.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("32")
        meh32+=1

#sor5
    global meh33
    meh33=0
    def foglal_sz33(b):
        global meh33
        if b==33:
            if meh33==0 or meh33%2==0:
                szek41.config(bootstyle="warning")
                mehesz_fog_szek.append("33")
            else:
                szek41.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("33")
        meh33+=1

    global meh34
    meh34=0
    def foglal_sz34(b):
        global meh34
        if b==34:
            if meh34==0 or meh34%2==0:
                szek42.config(bootstyle="warning")
                mehesz_fog_szek.append("34")
            else:
                szek42.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("34")
        meh34+=1

    global meh35
    meh35=0
    def foglal_sz35(b):
        global meh35
        if b==35:
            if meh35==0 or meh35%2==0:
                szek43.config(bootstyle="warning")
                mehesz_fog_szek.append("35")
            else:
                szek43.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("35")
        meh35+=1

    global meh36
    meh36=0
    def foglal_sz36(b):
        global meh36
        if b==36:
            if meh36==0 or meh36%2==0:
                szek44.config(bootstyle="warning")
                mehesz_fog_szek.append("36")
            else:
                szek44.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("36")
        meh36+=1


    global meh37
    meh37=0
    def foglal_sz37(b):
        global meh37
        if b==37:
            if meh37==0 or meh37%2==0:
                szek45.config(bootstyle="warning")
                mehesz_fog_szek.append("37")
            else:
                szek45.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("37")
        meh37+=1

    global meh38
    meh38=0
    def foglal_sz38(b):
        global meh38
        if b==38:
            if meh38==0 or meh38%2==0:
                szek46.config(bootstyle="warning")
                mehesz_fog_szek.append("38")
            else:
                szek46.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("38")
        meh38+=1

    global meh39
    meh39=0
    def foglal_sz39(b):
        global meh39
        if b==39:
            if meh39==0 or meh39%2==0:
                szek47.config(bootstyle="warning")
                mehesz_fog_szek.append("39")
            else:
                szek47.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("39")
        meh39+=1

    global meh40
    meh40=0
    def foglal_sz40(b):
        global meh40
        if b==40:
            if meh40==0 or meh40%2==0:
                szek48.config(bootstyle="warning")
                mehesz_fog_szek.append("40")
            else:
                szek48.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("40")
        meh40+=1

    global meh41
    meh41=0
    def foglal_sz41(b):
        global meh41
        if b==41:
            if meh41==0 or meh41%2==0:
                szek49.config(bootstyle="warning")
                mehesz_fog_szek.append("41")
            else:
                szek49.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("41")
        meh41+=1

    global meh42
    meh42=0
    def foglal_sz42(b):
        global meh42
        if b==42:
            if meh42==0 or meh42%2==0:
                szek50.config(bootstyle="warning")
                mehesz_fog_szek.append("42")
            else:
                szek50.config(bootstyle="prmehary")
                mehesz_fog_szek.remove("42")
        meh42+=1

    fcimkeret = LabelFrame(fog_ablak, border=0, padding=0, borderwidth=0)
    fcimkeret.grid(row=0, column=0, columnspan=2)
    Label.columnconfigure(fcimkeret, 1, weight=1)
    fcim = Label(fcimkeret, text="A MÉHÉSZ", font=("Terminal", 20, "bold"), justify="center", anchor="center", width=90)
    fcim.grid(row=0, column=0, pady=5, sticky="nesw")
    

    fkepkeret = LabelFrame(fog_ablak, height=370, border=0, padding=0, borderwidth=0)
    fkepkeret.grid(row=1, column=0, padx=50, pady=100)
    dune_al = Canvas(fkepkeret, width=250, height=370, bg='white')
    dune_al.grid(row=1, column=0)
    dune_al.create_image(0, 0, anchor=NW, image=img4)
    sadas=Meter(fkepkeret,bootstyle="warning")
    sadas.grid(row=2, column=0, pady=10)

    fkeret = LabelFrame(fog_ablak, padding=10)
    fkeret.grid(row=1, column=1)
    fleiras = Label(fkeret, text="Egy férfi egyszemélyes, brutális bosszúhadjáratának tétje országos szintűre nő, miután kiderül róla, hogy korábban a Méhészek néven ismert befolyásos és titkos szervezet ügynöke volt.", font=("Times", 12, "bold"), width=50, justify="left", wraplength=400)
    fleiras.grid(row=0, column=0, columnspan=10)
    szek1 = Button(fkeret, state=NORMAL, text="01" ,command=lambda:foglal_sz1(1))
    szek1.grid(row=1, column=0, pady=10)
    szek2 = Button(fkeret, state=NORMAL, text="02", command=lambda:foglal_sz2(2))
    szek2.grid(row=1, column=1)
    szek3 = Button(fkeret, state=NORMAL, text="03", command=lambda:foglal_sz3(3))
    szek3.grid(row=1, column=2)
    szek4 = Button(fkeret, state=NORMAL, text="04", command=lambda:foglal_sz4(4))
    szek4.grid(row=1, column=3)
    szek5 = Label(fkeret, width=0)
    szek5.grid(row=1, column=4)
    szek6 = Label(fkeret, width=0)
    szek6.grid(row=1, column=5)
    szek7 = Button(fkeret, state=NORMAL, text="05", command=lambda:foglal_sz5(5))
    szek7.grid(row=1, column=6)
    szek8 = Button(fkeret, state=NORMAL, text="06" , command=lambda:foglal_sz6(6))
    szek8.grid(row=1, column=7)
    szek9 = Button(fkeret, state=NORMAL, text="07" , command=lambda:foglal_sz7(7))
    szek9.grid(row=1, column=8)
    szek10 = Button(fkeret, state=NORMAL, text="08", command=lambda:foglal_sz8(8))
    szek10.grid(row=1, column=9)
    szek11 = Button(fkeret, state=NORMAL, text="09", command=lambda:foglal_sz9(9))
    szek11.grid(row=2, column=0, pady=10)
    szek12 = Button(fkeret, state=NORMAL, text="10", command=lambda:foglal_sz10(10))
    szek12.grid(row=2, column=1)
    szek13 = Button(fkeret, state=NORMAL, text="11" , command=lambda:foglal_sz11(11))
    szek13.grid(row=2, column=2)
    szek14 = Button(fkeret, state=NORMAL, text="12", command=lambda:foglal_sz12(12))
    szek14.grid(row=2, column=3)
    szek15 = Label(fkeret, width=0)
    szek15.grid(row=2, column=4)
    szek16 = Label(fkeret, width=0)
    szek16.grid(row=2, column=5)
    szek17 = Button(fkeret, state=NORMAL, text="13" , command=lambda:foglal_sz13(13))
    szek17.grid(row=2, column=6)
    szek18 = Button(fkeret, state=NORMAL, text="14" , command=lambda:foglal_sz14(14))
    szek18.grid(row=2, column=7)
    szek19 = Button(fkeret, state=NORMAL, text="15", command=lambda:foglal_sz15(15))
    szek19.grid(row=2, column=8)
    szek20 = Button(fkeret, state=NORMAL, text="16", command=lambda:foglal_sz16(16))
    szek20.grid(row=2, column=9)
    szek21 = Button(fkeret, state=NORMAL, text="17", command=lambda:foglal_sz17(17))
    szek21.grid(row=3, column=0, pady=10)
    szek22 = Button(fkeret, state=NORMAL, text="18", command=lambda:foglal_sz18(18))
    szek22.grid(row=3, column=1)
    szek23 = Button(fkeret, state=NORMAL, text="19", command=lambda:foglal_sz19(19))
    szek23.grid(row=3, column=2)
    szek24 = Button(fkeret, state=NORMAL, text="20", command=lambda:foglal_sz20(20))
    szek24.grid(row=3, column=3)
    szek25 = Label(fkeret, width=0)
    szek25.grid(row=3, column=4)
    szek26 = Label(fkeret, width=0)
    szek26.grid(row=3, column=5)
    szek27 = Button(fkeret, state=NORMAL, text="21", command=lambda:foglal_sz21(21))
    szek27.grid(row=3, column=6)
    szek28 = Button(fkeret, state=NORMAL, text="22", command=lambda:foglal_sz22(22))
    szek28.grid(row=3, column=7)
    szek29 = Button(fkeret, state=NORMAL, text="23", command=lambda:foglal_sz23(23))
    szek29.grid(row=3, column=8)
    szek30 = Button(fkeret, state=NORMAL, text="24", command=lambda:foglal_sz24(24))
    szek30.grid(row=3, column=9)
    szek31 = Button(fkeret, state=NORMAL, text="25", command=lambda:foglal_sz25(25))
    szek31.grid(row=4, column=0, pady=10)
    szek32 = Button(fkeret, state=NORMAL, text="26", command=lambda:foglal_sz26(26))
    szek32.grid(row=4, column=1)
    szek33 = Button(fkeret, state=NORMAL, text="27", command=lambda:foglal_sz27(27))
    szek33.grid(row=4, column=2)
    szek34 = Button(fkeret, state=NORMAL, text="28", command=lambda:foglal_sz28(28))
    szek34.grid(row=4, column=3)
    szek35 = Label(fkeret, width=0)
    szek35.grid(row=4, column=4)
    szek36 = Label(fkeret, width=0)
    szek36.grid(row=4, column=5)
    szek37 = Button(fkeret, state=NORMAL, text="29" , command=lambda:foglal_sz29(29))
    szek37.grid(row=4, column=6)
    szek38 = Button(fkeret, state=NORMAL, text="30", command=lambda:foglal_sz30(30))
    szek38.grid(row=4, column=7)
    szek39 = Button(fkeret, state=NORMAL, text="31" , command=lambda:foglal_sz31(31))
    szek39.grid(row=4, column=8)
    szek40 = Button(fkeret, state=NORMAL, text="32", command=lambda:foglal_sz32(32))
    szek40.grid(row=4, column=9)
    szek41 = Button(fkeret, state=NORMAL, text="33" , command=lambda:foglal_sz33(33))
    szek41.grid(row=5, column=0, pady=10)
    szek42 = Button(fkeret, state=NORMAL, text="34", command=lambda:foglal_sz34(34))
    szek42.grid(row=5, column=1)
    szek43 = Button(fkeret, state=NORMAL, text="35", command=lambda:foglal_sz35(35))
    szek43.grid(row=5, column=2)
    szek44 = Button(fkeret, state=NORMAL, text="36", command=lambda:foglal_sz36(36))
    szek44.grid(row=5, column=3)
    szek45 = Button(fkeret, state=NORMAL, text="37", command=lambda:foglal_sz37(37))
    szek45.grid(row=5, column=4)
    szek46 = Button(fkeret, state=NORMAL, text="38", command=lambda:foglal_sz38(38))
    szek46.grid(row=5, column=5)
    szek47 = Button(fkeret, state=NORMAL, text="39", command=lambda:foglal_sz39(39))
    szek47.grid(row=5, column=6)
    szek48 = Button(fkeret, state=NORMAL, text="40", command=lambda:foglal_sz40(40))
    szek48.grid(row=5, column=7)
    szek49 = Button(fkeret, state=NORMAL, text="41", command=lambda:foglal_sz41(41))
    szek49.grid(row=5, column=8)
    szek50 = Button(fkeret, state=NORMAL, text="42", command=lambda:foglal_sz42(42))
    szek50.grid(row=5, column=9)
    ffoglal = Button(fkeret, text="Helyet foglalok", bootstyle="info", command= lambda:pdf_mehesz())
    ffoglal.grid(row=6, column=0, columnspan=10, pady=10)

def king_foglal_ablak():
    fog_ablak = Toplevel(root)
    fog_ablak.geometry("1000x800")
    fog_ablak.title("ARTÚR, A KIRÁLY: Foglalás")

    global kin
    kin=0
    def foglal_sz1(b):
        global kin
        if b==1:
            if kin==0 or kin%2==0:
                szek1.config(bootstyle="warning")
                king_fog_szek.append("1")
            else:
                szek1.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
            kin+=1
    global kin2
    kin2=0
    def foglal_sz2(b):
        global kin2
        if b==2:
            if kin2==0 or kin2%2==0:
                szek2.config(bootstyle="warning")
                king_fog_szek.append("2")
            else:
                szek2.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin2+=1

    global kin3
    kin3=0
    def foglal_sz3(b):
        global kin3
        if b==3:
            if kin3==0 or kin3%2==0:
                szek3.config(bootstyle="warning")
                king_fog_szek.append("3")
            else:
                szek3.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin3+=1

    global kin4
    kin4=0
    def foglal_sz4(b):
        global kin4
        if b==4:
            if kin4==0 or kin4%2==0:
                szek4.config(bootstyle="warning")
                king_fog_szek.append("4")
            else:
                szek4.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin4+=1


    global kin5
    kin5=0
    def foglal_sz5(b):
        global kin5
        if b==5:
            if kin5==0 or kin5%2==0:
                szek7.config(bootstyle="warning")
                king_fog_szek.append("5")
            else:
                szek7.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin5+=1

    global kin6
    kin6=0
    def foglal_sz6(b):
        global kin6
        if b==6:
            if kin6==0 or kin6%2==0:
                szek8.config(bootstyle="warning")
                king_fog_szek.append("6")
            else:
                szek8.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin6+=1

    global kin7
    kin7=0
    def foglal_sz7(b):
        global kin7
        if b==7:
            if kin7==0 or kin7%2==0:
                szek9.config(bootstyle="warning")
                king_fog_szek.append("7")
            else:
                szek9.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin7+=1

    global kin8
    kin8=0
    def foglal_sz8(b):
        global kin8
        if b==8:
            if kin8==0 or kin8%2==0:
                szek10.config(bootstyle="warning")
                king_fog_szek.append("8")
            else:
                szek10.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin8+=1

#sor2
    global kin9
    kin9=0
    def foglal_sz9(b):
        global kin9
        if b==9:
            if kin9==0 or kin9%2==0:
                szek11.config(bootstyle="warning")
                king_fog_szek.append("9")
            else:
                szek11.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin9+=1

    global kin10
    kin10=0
    def foglal_sz10(b):
        global kin10
        if b==10:
            if kin10==0 or kin10%2==0:
                szek12.config(bootstyle="warning")
                king_fog_szek.append("10")
            else:
                szek12.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin10+=1

    global kin11
    kin11=0
    def foglal_sz11(b):
        global kin11
        if b==11:
            if kin11==0 or kin11%2==0:
                szek13.config(bootstyle="warning")
                king_fog_szek.append("11")
            else:
                szek13.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin11+=1

    global kin12
    kin12=0
    def foglal_sz12(b):
        global kin12
        if b==12:
            if kin12==0 or kin12%2==0:
                szek14.config(bootstyle="warning")
                king_fog_szek.append("12")
            else:
                szek14.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin12+=1


    global kin13
    kin13=0
    def foglal_sz13(b):
        global kin13
        if b==13:
            if kin13==0 or kin13%2==0:
                szek17.config(bootstyle="warning")
                king_fog_szek.append("13")
            else:
                szek17.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin13+=1

    global kin14
    kin14=0
    def foglal_sz14(b):
        global kin14
        if b==14:
            if kin14==0 or kin14%2==0:
                szek18.config(bootstyle="warning")
                king_fog_szek.append("14")
            else:
                szek18.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin14+=1

    global kin15
    kin15=0
    def foglal_sz15(b):
        global kin15
        if b==15:
            if kin15==0 or kin15%2==0:
                szek19.config(bootstyle="warning")
                king_fog_szek.append("15")
            else:
                szek19.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin15+=1

    global kin16
    kin16=0
    def foglal_sz16(b):
        global kin16
        if b==16:
            if kin16==0 or kin16%2==0:
                szek20.config(bootstyle="warning")
                king_fog_szek.append("16")
            else:
                szek20.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin16+=1


#sor3
    global kin17
    kin17=0
    def foglal_sz17(b):
        global kin17
        if b==17:
            if kin17==0 or kin17%2==0:
                szek21.config(bootstyle="warning")
                king_fog_szek.append("17")
            else:
                szek21.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin17+=1

    global kin18
    kin18=0
    def foglal_sz18(b):
        global kin18
        if b==18:
            if kin18==0 or kin18%2==0:
                szek22.config(bootstyle="warning")
                king_fog_szek.append("18")
            else:
                szek22.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin18+=1

    global kin19
    kin19=0
    def foglal_sz19(b):
        global kin19
        if b==19:
            if kin19==0 or kin19%2==0:
                szek23.config(bootstyle="warning")
                king_fog_szek.append("19")
            else:
                szek23.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin19+=1

    global kin20
    kin20=0
    def foglal_sz20(b):
        global kin20
        if b==20:
            if kin20==0 or kin20%2==0:
                szek24.config(bootstyle="warning")
                king_fog_szek.append("20")
            else:
                szek24.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin20+=1


    global kin21
    kin21=0
    def foglal_sz21(b):
        global kin21
        if b==21:
            if kin21==0 or kin21%2==0:
                szek27.config(bootstyle="warning")
                king_fog_szek.append("21")
            else:
                szek27.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin21+=1

    global kin22
    kin22=0
    def foglal_sz22(b):
        global kin22
        if b==22:
            if kin22==0 or kin22%2==0:
                szek28.config(bootstyle="warning")
                king_fog_szek.append("22")
            else:
                szek28.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin22+=1

    global kin23
    kin23=0
    def foglal_sz23(b):
        global kin23
        if b==23:
            if kin23==0 or kin23%2==0:
                szek29.config(bootstyle="warning")
                king_fog_szek.append("23")
            else:
                szek29.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin23+=1

    global kin24
    kin24=0
    def foglal_sz24(b):
        global kin24
        if b==24:
            if kin24==0 or kin24%2==0:
                szek30.config(bootstyle="warning")
                king_fog_szek.append("24")
            else:
                szek30.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin24+=1

#sor4
    
    global kin25
    kin25=0
    def foglal_sz25(b):
        global kin25
        if b==25:
            if kin25==0 or kin25%2==0:
                szek31.config(bootstyle="warning")
                king_fog_szek.append("25")
            else:
                szek31.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin25+=1

    global kin26
    kin26=0
    def foglal_sz26(b):
        global kin26
        if b==26:
            if kin26==0 or kin26%2==0:
                szek32.config(bootstyle="warning")
                king_fog_szek.append("26")
            else:
                szek32.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin26+=1

    global kin27
    kin27=0
    def foglal_sz27(b):
        global kin27
        if b==27:
            if kin27==0 or kin27%2==0:
                szek33.config(bootstyle="warning")
                king_fog_szek.append("27")
            else:
                szek33.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin27+=1

    global kin28
    kin28=0
    def foglal_sz28(b):
        global kin28
        if b==28:
            if kin28==0 or kin28%2==0:
                szek34.config(bootstyle="warning")
                king_fog_szek.append("28")
            else:
                szek34.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin28+=1


    global kin29
    kin29=0
    def foglal_sz29(b):
        global kin29
        if b==29:
            if kin29==0 or kin29%2==0:
                szek37.config(bootstyle="warning")
                king_fog_szek.append("29")
            else:
                szek37.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin29+=1

    global kin30
    kin30=0
    def foglal_sz30(b):
        global kin30
        if b==30:
            if kin30==0 or kin30%2==0:
                szek38.config(bootstyle="warning")
                king_fog_szek.append("30")
            else:
                szek38.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin30+=1

    global kin31
    kin31=0
    def foglal_sz31(b):
        global kin31
        if b==31:
            if kin31==0 or kin31%2==0:
                szek39.config(bootstyle="warning")
                king_fog_szek.append("31")
            else:
                szek39.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin31+=1

    global kin32
    kin32=0
    def foglal_sz32(b):
        global kin32
        if b==32:
            if kin32==0 or kin32%2==0:
                szek40.config(bootstyle="warning")
                king_fog_szek.append("32")
            else:
                szek40.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin32+=1

#sor5
    global kin33
    kin33=0
    def foglal_sz33(b):
        global kin33
        if b==33:
            if kin33==0 or kin33%2==0:
                szek41.config(bootstyle="warning")
                king_fog_szek.append("33")
            else:
                szek41.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin33+=1

    global kin34
    kin34=0
    def foglal_sz34(b):
        global kin34
        if b==34:
            if kin34==0 or kin34%2==0:
                szek42.config(bootstyle="warning")
                king_fog_szek.append("34")
            else:
                szek42.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin34+=1

    global kin35
    kin35=0
    def foglal_sz35(b):
        global kin35
        if b==35:
            if kin35==0 or kin35%2==0:
                szek43.config(bootstyle="warning")
                king_fog_szek.append("35")
            else:
                szek43.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin35+=1

    global kin36
    kin36=0
    def foglal_sz36(b):
        global kin36
        if b==36:
            if kin36==0 or kin36%2==0:
                szek44.config(bootstyle="warning")
                king_fog_szek.append("36")
            else:
                szek44.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin36+=1


    global kin37
    kin37=0
    def foglal_sz37(b):
        global kin37
        if b==37:
            if kin37==0 or kin37%2==0:
                szek45.config(bootstyle="warning")
                king_fog_szek.append("37")
            else:
                szek45.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin37+=1

    global kin38
    kin38=0
    def foglal_sz38(b):
        global kin38
        if b==38:
            if kin38==0 or kin38%2==0:
                szek46.config(bootstyle="warning")
                king_fog_szek.append("38")
            else:
                szek46.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin38+=1

    global kin39
    kin39=0
    def foglal_sz39(b):
        global kin39
        if b==39:
            if kin39==0 or kin39%2==0:
                szek47.config(bootstyle="warning")
                king_fog_szek.append("39")
            else:
                szek47.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin39+=1

    global kin40
    kin40=0
    def foglal_sz40(b):
        global kin40
        if b==40:
            if kin40==0 or kin40%2==0:
                szek48.config(bootstyle="warning")
                king_fog_szek.append("40")
            else:
                szek48.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin40+=1

    global kin41
    kin41=0
    def foglal_sz41(b):
        global kin41
        if b==41:
            if kin41==0 or kin41%2==0:
                szek49.config(bootstyle="warning")
                king_fog_szek.append("41")
            else:
                szek49.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin41+=1

    global kin42
    kin42=0
    def foglal_sz42(b):
        global kin42
        if b==42:
            if kin42==0 or kin42%2==0:
                szek50.config(bootstyle="warning")
                king_fog_szek.append("42")
            else:
                szek50.config(bootstyle="prkinary")
                king_fog_szek.remove(str(b))
        kin42+=1

    fcimkeret = LabelFrame(fog_ablak, border=0, padding=0, borderwidth=0)
    fcimkeret.grid(row=0, column=0, columnspan=2)
    Label.columnconfigure(fcimkeret, 1, weight=1)
    fcim = Label(fcimkeret, text="ARTÚR, A KIRÁLY", font=("Terminal", 20, "bold"), justify="center", anchor="center", width=90)
    fcim.grid(row=0, column=0, pady=5, sticky="nesw")

    fkepkeret = LabelFrame(fog_ablak, height=370, border=0, padding=0, borderwidth=0)
    fkepkeret.grid(row=1, column=0, padx=50, pady=100)
    dune_al = Canvas(fkepkeret, width=250, height=370, bg='white')
    dune_al.grid(row=0, column=0)
    dune_al.create_image(0, 0, anchor=NW, image=img5)
    sadas=Meter(fkepkeret,bootstyle="warning")
    sadas.grid(row=1, column=0, pady=10)

    fkeret = LabelFrame(fog_ablak, padding=10)
    fkeret.grid(row=1, column=1)
    fleiras = Label(fkeret, text="Michael Light (Mark Wahlberg) és elszánt csapata a Dominikai Köztársaság dzsungelében teszi próbára magát egy rendkívüli 10 napos, 700 kilométeres extrémsport-világbajnokságon. A kalandvágyó sportember életében ez az utolsó lehetőség, hogy a régen áhított első helyezést elérje, a túra során azonban váratlanul egy ágrólszakadt kóborkutya szegődik melléjük. Michael és a különös, mégis méltóságteljes állat között hamarosan megbonthatatlan barátság szövődik, és a verseny végére Michael számára a győzelem, a hűség és a barátság jelentése merőben új értelmet nyer.", font=("Times", 12, "bold"), width=50, justify="left", wraplength=400)
    fleiras.grid(row=0, column=0, columnspan=10)
    szek1 = Button(fkeret, state=NORMAL, text="01" ,command=lambda:foglal_sz1(1))
    szek1.grid(row=1, column=0, pady=10)
    szek2 = Button(fkeret, state=NORMAL, text="02", command=lambda:foglal_sz2(2))
    szek2.grid(row=1, column=1)
    szek3 = Button(fkeret, state=NORMAL, text="03", command=lambda:foglal_sz3(3))
    szek3.grid(row=1, column=2)
    szek4 = Button(fkeret, state=NORMAL, text="04", command=lambda:foglal_sz4(4))
    szek4.grid(row=1, column=3)
    szek5 = Label(fkeret, width=0)
    szek5.grid(row=1, column=4)
    szek6 = Label(fkeret, width=0)
    szek6.grid(row=1, column=5)
    szek7 = Button(fkeret, state=NORMAL, text="05", command=lambda:foglal_sz5(5))
    szek7.grid(row=1, column=6)
    szek8 = Button(fkeret, state=NORMAL, text="06" , command=lambda:foglal_sz6(6))
    szek8.grid(row=1, column=7)
    szek9 = Button(fkeret, state=NORMAL, text="07" , command=lambda:foglal_sz7(7))
    szek9.grid(row=1, column=8)
    szek10 = Button(fkeret, state=NORMAL, text="08", command=lambda:foglal_sz8(8))
    szek10.grid(row=1, column=9)
    szek11 = Button(fkeret, state=NORMAL, text="09", command=lambda:foglal_sz9(9))
    szek11.grid(row=2, column=0, pady=10)
    szek12 = Button(fkeret, state=NORMAL, text="10", command=lambda:foglal_sz10(10))
    szek12.grid(row=2, column=1)
    szek13 = Button(fkeret, state=NORMAL, text="11" , command=lambda:foglal_sz11(11))
    szek13.grid(row=2, column=2)
    szek14 = Button(fkeret, state=NORMAL, text="12", command=lambda:foglal_sz12(12))
    szek14.grid(row=2, column=3)
    szek15 = Label(fkeret, width=0)
    szek15.grid(row=2, column=4)
    szek16 = Label(fkeret, width=0)
    szek16.grid(row=2, column=5)
    szek17 = Button(fkeret, state=NORMAL, text="13" , command=lambda:foglal_sz13(13))
    szek17.grid(row=2, column=6)
    szek18 = Button(fkeret, state=NORMAL, text="14" , command=lambda:foglal_sz14(14))
    szek18.grid(row=2, column=7)
    szek19 = Button(fkeret, state=NORMAL, text="15", command=lambda:foglal_sz15(15))
    szek19.grid(row=2, column=8)
    szek20 = Button(fkeret, state=NORMAL, text="16", command=lambda:foglal_sz16(16))
    szek20.grid(row=2, column=9)
    szek21 = Button(fkeret, state=NORMAL, text="17", command=lambda:foglal_sz17(17))
    szek21.grid(row=3, column=0, pady=10)
    szek22 = Button(fkeret, state=NORMAL, text="18", command=lambda:foglal_sz18(18))
    szek22.grid(row=3, column=1)
    szek23 = Button(fkeret, state=NORMAL, text="19", command=lambda:foglal_sz19(19))
    szek23.grid(row=3, column=2)
    szek24 = Button(fkeret, state=NORMAL, text="20", command=lambda:foglal_sz20(20))
    szek24.grid(row=3, column=3)
    szek25 = Label(fkeret, width=0)
    szek25.grid(row=3, column=4)
    szek26 = Label(fkeret, width=0)
    szek26.grid(row=3, column=5)
    szek27 = Button(fkeret, state=NORMAL, text="21", command=lambda:foglal_sz21(21))
    szek27.grid(row=3, column=6)
    szek28 = Button(fkeret, state=NORMAL, text="22", command=lambda:foglal_sz22(22))
    szek28.grid(row=3, column=7)
    szek29 = Button(fkeret, state=NORMAL, text="23", command=lambda:foglal_sz23(23))
    szek29.grid(row=3, column=8)
    szek30 = Button(fkeret, state=NORMAL, text="24", command=lambda:foglal_sz24(24))
    szek30.grid(row=3, column=9)
    szek31 = Button(fkeret, state=NORMAL, text="25", command=lambda:foglal_sz25(25))
    szek31.grid(row=4, column=0, pady=10)
    szek32 = Button(fkeret, state=NORMAL, text="26", command=lambda:foglal_sz26(26))
    szek32.grid(row=4, column=1)
    szek33 = Button(fkeret, state=NORMAL, text="27", command=lambda:foglal_sz27(27))
    szek33.grid(row=4, column=2)
    szek34 = Button(fkeret, state=NORMAL, text="28", command=lambda:foglal_sz28(28))
    szek34.grid(row=4, column=3)
    szek35 = Label(fkeret, width=0)
    szek35.grid(row=4, column=4)
    szek36 = Label(fkeret, width=0)
    szek36.grid(row=4, column=5)
    szek37 = Button(fkeret, state=NORMAL, text="29" , command=lambda:foglal_sz29(29))
    szek37.grid(row=4, column=6)
    szek38 = Button(fkeret, state=NORMAL, text="30", command=lambda:foglal_sz30(30))
    szek38.grid(row=4, column=7)
    szek39 = Button(fkeret, state=NORMAL, text="31" , command=lambda:foglal_sz31(31))
    szek39.grid(row=4, column=8)
    szek40 = Button(fkeret, state=NORMAL, text="32", command=lambda:foglal_sz32(32))
    szek40.grid(row=4, column=9)
    szek41 = Button(fkeret, state=NORMAL, text="33" , command=lambda:foglal_sz33(33))
    szek41.grid(row=5, column=0, pady=10)
    szek42 = Button(fkeret, state=NORMAL, text="34", command=lambda:foglal_sz34(34))
    szek42.grid(row=5, column=1)
    szek43 = Button(fkeret, state=NORMAL, text="35", command=lambda:foglal_sz35(35))
    szek43.grid(row=5, column=2)
    szek44 = Button(fkeret, state=NORMAL, text="36", command=lambda:foglal_sz36(36))
    szek44.grid(row=5, column=3)
    szek45 = Button(fkeret, state=NORMAL, text="37", command=lambda:foglal_sz37(37))
    szek45.grid(row=5, column=4)
    szek46 = Button(fkeret, state=NORMAL, text="38", command=lambda:foglal_sz38(38))
    szek46.grid(row=5, column=5)
    szek47 = Button(fkeret, state=NORMAL, text="39", command=lambda:foglal_sz39(39))
    szek47.grid(row=5, column=6)
    szek48 = Button(fkeret, state=NORMAL, text="40", command=lambda:foglal_sz40(40))
    szek48.grid(row=5, column=7)
    szek49 = Button(fkeret, state=NORMAL, text="41", command=lambda:foglal_sz41(41))
    szek49.grid(row=5, column=8)
    szek50 = Button(fkeret, state=NORMAL, text="42", command=lambda:foglal_sz42(42))
    szek50.grid(row=5, column=9)
    ffoglal = Button(fkeret, text="Helyet foglalok", bootstyle="info", command= lambda:pdf_king())
    ffoglal.grid(row=6, column=0, columnspan=10, pady=10)

def godzilla_foglal_ablak():
    fog_ablak = Toplevel(root)
    fog_ablak.geometry("1000x800")
    fog_ablak.title("GODZILLA X KONG: AZ ÚJ BIRODALOM: Foglalás")

    global god
    god=0
    def foglal_sz1(b):
        global god
        if b==1:
            if god==0 or god%2==0:
                szek1.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek1.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god+=1

    global god2
    god2=0
    def foglal_sz2(b):
        global god2
        if b==2:
            if god2==0 or god2%2==0:
                szek2.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek2.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god2+=1

    global god3
    god3=0
    def foglal_sz3(b):
        global god3
        if b==3:
            if god3==0 or god3%2==0:
                szek3.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek3.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god3+=1

    global god4
    god4=0
    def foglal_sz4(b):
        global god4
        if b==4:
            if god4==0 or god4%2==0:
                szek4.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek4.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god4+=1


    global god5
    god5=0
    def foglal_sz5(b):
        global god5
        if b==5:
            if god5==0 or god5%2==0:
                szek7.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek7.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god5+=1

    global god6
    god6=0
    def foglal_sz6(b):
        global god6
        if b==6:
            if god6==0 or god6%2==0:
                szek8.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek8.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god6+=1

    global god7
    god7=0
    def foglal_sz7(b):
        global god7
        if b==7:
            if god7==0 or god7%2==0:
                szek9.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek9.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god7+=1

    global god8
    god8=0
    def foglal_sz8(b):
        global god8
        if b==8:
            if god8==0 or god8%2==0:
                szek10.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek10.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god8+=1

#sor2
    global god9
    god9=0
    def foglal_sz9(b):
        global god9
        if b==9:
            if god9==0 or god9%2==0:
                szek11.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek11.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god9+=1

    global god10
    god10=0
    def foglal_sz10(b):
        global god10
        if b==10:
            if god10==0 or god10%2==0:
                szek12.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek12.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god10+=1

    global god11
    god11=0
    def foglal_sz11(b):
        global god11
        if b==11:
            if god11==0 or god11%2==0:
                szek13.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek13.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god11+=1

    global god12
    god12=0
    def foglal_sz12(b):
        global god12
        if b==12:
            if god12==0 or god12%2==0:
                szek14.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek14.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god12+=1


    global god13
    god13=0
    def foglal_sz13(b):
        global god13
        if b==13:
            if god13==0 or god13%2==0:
                szek17.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek17.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god13+=1

    global god14
    god14=0
    def foglal_sz14(b):
        global god14
        if b==14:
            if god14==0 or god14%2==0:
                szek18.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek18.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god14+=1

    global god15
    god15=0
    def foglal_sz15(b):
        global god15
        if b==15:
            if god15==0 or god15%2==0:
                szek19.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek19.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god15+=1

    global god16
    god16=0
    def foglal_sz16(b):
        global god16
        if b==16:
            if god16==0 or god16%2==0:
                szek20.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek20.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god16+=1


#sor3
    global god17
    god17=0
    def foglal_sz17(b):
        global god17
        if b==17:
            if god17==0 or god17%2==0:
                szek21.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek21.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god17+=1

    global god18
    god18=0
    def foglal_sz18(b):
        global god18
        if b==18:
            if god18==0 or god18%2==0:
                szek22.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek22.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god18+=1

    global god19
    god19=0
    def foglal_sz19(b):
        global god19
        if b==19:
            if god19==0 or god19%2==0:
                szek23.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek23.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god19+=1

    global god20
    god20=0
    def foglal_sz20(b):
        global god20
        if b==20:
            if god20==0 or god20%2==0:
                szek24.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek24.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god20+=1


    global god21
    god21=0
    def foglal_sz21(b):
        global god21
        if b==21:
            if god21==0 or god21%2==0:
                szek27.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek27.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god21+=1

    global god22
    god22=0
    def foglal_sz22(b):
        global god22
        if b==22:
            if god22==0 or god22%2==0:
                szek28.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek28.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god22+=1

    global god23
    god23=0
    def foglal_sz23(b):
        global god23
        if b==23:
            if god23==0 or god23%2==0:
                szek29.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek29.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god23+=1

    global god24
    god24=0
    def foglal_sz24(b):
        global god24
        if b==24:
            if god24==0 or god24%2==0:
                szek30.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek30.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god24+=1

#sor4
    
    global god25
    god25=0
    def foglal_sz25(b):
        global god25
        if b==25:
            if god25==0 or god25%2==0:
                szek31.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek31.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god25+=1

    global god26
    god26=0
    def foglal_sz26(b):
        global god26
        if b==26:
            if god26==0 or god26%2==0:
                szek32.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek32.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god26+=1

    global god27
    god27=0
    def foglal_sz27(b):
        global god27
        if b==27:
            if god27==0 or god27%2==0:
                szek33.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))

            else:
                szek33.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god27+=1

    global god28
    god28=0
    def foglal_sz28(b):
        global god28
        if b==28:
            if god28==0 or god28%2==0:
                szek34.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek34.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god28+=1


    global god29
    god29=0
    def foglal_sz29(b):
        global god29
        if b==29:
            if god29==0 or god29%2==0:
                szek37.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek37.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god29+=1

    global god30
    god30=0
    def foglal_sz30(b):
        global god30
        if b==30:
            if god30==0 or god30%2==0:
                szek38.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek38.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god30+=1

    global god31
    god31=0
    def foglal_sz31(b):
        global god31
        if b==31:
            if god31==0 or god31%2==0:
                szek39.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek39.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god31+=1

    global god32
    god32=0
    def foglal_sz32(b):
        global god32
        if b==32:
            if god32==0 or god32%2==0:
                szek40.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek40.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god32+=1

#sor5
    global god33
    god33=0
    def foglal_sz33(b):
        global god33
        if b==33:
            if god33==0 or god33%2==0:
                szek41.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek41.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god33+=1

    global god34
    god34=0
    def foglal_sz34(b):
        global god34
        if b==34:
            if god34==0 or god34%2==0:
                szek42.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek42.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god34+=1

    global god35
    god35=0
    def foglal_sz35(b):
        global god35
        if b==35:
            if god35==0 or god35%2==0:
                szek43.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek43.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god35+=1

    global god36
    god36=0
    def foglal_sz36(b):
        global god36
        if b==36:
            if god36==0 or god36%2==0:
                szek44.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek44.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god36+=1


    global god37
    god37=0
    def foglal_sz37(b):
        global god37
        if b==37:
            if god37==0 or god37%2==0:
                szek45.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek45.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god37+=1

    global god38
    god38=0
    def foglal_sz38(b):
        global god38
        if b==38:
            if god38==0 or god38%2==0:
                szek46.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek46.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god38+=1

    global god39
    god39=0
    def foglal_sz39(b):
        global god39
        if b==39:
            if god39==0 or god39%2==0:
                szek47.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek47.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god39+=1

    global god40
    god40=0
    def foglal_sz40(b):
        global god40
        if b==40:
            if god40==0 or god40%2==0:
                szek48.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek48.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god40+=1

    global god41
    god41=0
    def foglal_sz41(b):
        global god41
        if b==41:
            if god41==0 or god41%2==0:
                szek49.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))
            else:
                szek49.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))
        god41+=1

    global god42
    god42=0
    def foglal_sz42(b):
        global god42
        if b==42:
            if god42==0 or god42%2==0:
                szek50.config(bootstyle="warning")
                godzill_fog_szek.append(str(b))

            else:
                szek50.config(bootstyle="prgodary")
                godzill_fog_szek.remove(str(b))

        god42+=1

    fcimkeret = LabelFrame(fog_ablak, border=0, padding=0, borderwidth=0)
    fcimkeret.grid(row=0, column=0, columnspan=2)
    Label.columnconfigure(fcimkeret, 1, weight=1)
    fcim = Label(fcimkeret, text="GODZILLA X KONG: AZ ÚJ BIRODALOM", font=("Terminal", 20, "bold"), justify="center", anchor="center", width=90)
    fcim.grid(row=0, column=0, pady=5, sticky="nesw")

    fkepkeret = LabelFrame(fog_ablak, height=370, border=0, padding=0, borderwidth=0)
    fkepkeret.grid(row=1, column=0, padx=50, pady=100)
    dune_al = Canvas(fkepkeret, width=250, height=370, bg='white')
    dune_al.grid(row=0, column=0)
    dune_al.create_image(0, 0, anchor=NW, image=img6)
    sadas=Meter(fkepkeret,bootstyle="warning")
    sadas.grid(row=1, column=0, pady=10)
    
    fkeret = LabelFrame(fog_ablak, padding=10)
    fkeret.grid(row=1, column=1)
    fleiras = Label(fkeret, text="A mindent eldöntő, minden eddiginél nagyobb háború nem ért véget azzal, hogy Kong és Godzilla szembetalálkozott és összemérte az erejét. Mert az ember most már kénytelen belenyugodni, hogy nem ő a legerősebb a földön. És nem ismeri igazán a saját világát: várja még néhány eddig rejtve maradt meglepetés. Bujkál még valami a föld alatt, ami felébredt, és pusztítani akar. Az emberiség képtelen megállítani. Talán Kong is képtelen volna. És Godzilla is. De ha ők ketten összefognának, akkor esetleg megmenekülhetnének ők is és mi is…", font=("Times", 12, "bold"), width=50, justify="left", wraplength=400)
    fleiras.grid(row=0, column=0, columnspan=10)
    szek1 = Button(fkeret, state=NORMAL, text="01" ,command=lambda:foglal_sz1(1))
    szek1.grid(row=1, column=0, pady=10)
    szek2 = Button(fkeret, state=NORMAL, text="02", command=lambda:foglal_sz2(2))
    szek2.grid(row=1, column=1)
    szek3 = Button(fkeret, state=NORMAL, text="03", command=lambda:foglal_sz3(3))
    szek3.grid(row=1, column=2)
    szek4 = Button(fkeret, state=NORMAL, text="04", command=lambda:foglal_sz4(4))
    szek4.grid(row=1, column=3)
    szek5 = Label(fkeret, width=0)
    szek5.grid(row=1, column=4)
    szek6 = Label(fkeret, width=0)
    szek6.grid(row=1, column=5)
    szek7 = Button(fkeret, state=NORMAL, text="05", command=lambda:foglal_sz5(5))
    szek7.grid(row=1, column=6)
    szek8 = Button(fkeret, state=NORMAL, text="06" , command=lambda:foglal_sz6(6))
    szek8.grid(row=1, column=7)
    szek9 = Button(fkeret, state=NORMAL, text="07" , command=lambda:foglal_sz7(7))
    szek9.grid(row=1, column=8)
    szek10 = Button(fkeret, state=NORMAL, text="08", command=lambda:foglal_sz8(8))
    szek10.grid(row=1, column=9)
    szek11 = Button(fkeret, state=NORMAL, text="09", command=lambda:foglal_sz9(9))
    szek11.grid(row=2, column=0, pady=10)
    szek12 = Button(fkeret, state=NORMAL, text="10", command=lambda:foglal_sz10(10))
    szek12.grid(row=2, column=1)
    szek13 = Button(fkeret, state=NORMAL, text="11" , command=lambda:foglal_sz11(11))
    szek13.grid(row=2, column=2)
    szek14 = Button(fkeret, state=NORMAL, text="12", command=lambda:foglal_sz12(12))
    szek14.grid(row=2, column=3)
    szek15 = Label(fkeret, width=0)
    szek15.grid(row=2, column=4)
    szek16 = Label(fkeret, width=0)
    szek16.grid(row=2, column=5)
    szek17 = Button(fkeret, state=NORMAL, text="13" , command=lambda:foglal_sz13(13))
    szek17.grid(row=2, column=6)
    szek18 = Button(fkeret, state=NORMAL, text="14" , command=lambda:foglal_sz14(14))
    szek18.grid(row=2, column=7)
    szek19 = Button(fkeret, state=NORMAL, text="15", command=lambda:foglal_sz15(15))
    szek19.grid(row=2, column=8)
    szek20 = Button(fkeret, state=NORMAL, text="16", command=lambda:foglal_sz16(16))
    szek20.grid(row=2, column=9)
    szek21 = Button(fkeret, state=NORMAL, text="17", command=lambda:foglal_sz17(17))
    szek21.grid(row=3, column=0, pady=10)
    szek22 = Button(fkeret, state=NORMAL, text="18", command=lambda:foglal_sz18(18))
    szek22.grid(row=3, column=1)
    szek23 = Button(fkeret, state=NORMAL, text="19", command=lambda:foglal_sz19(19))
    szek23.grid(row=3, column=2)
    szek24 = Button(fkeret, state=NORMAL, text="20", command=lambda:foglal_sz20(20))
    szek24.grid(row=3, column=3)
    szek25 = Label(fkeret, width=0)
    szek25.grid(row=3, column=4)
    szek26 = Label(fkeret, width=0)
    szek26.grid(row=3, column=5)
    szek27 = Button(fkeret, state=NORMAL, text="21", command=lambda:foglal_sz21(21))
    szek27.grid(row=3, column=6)
    szek28 = Button(fkeret, state=NORMAL, text="22", command=lambda:foglal_sz22(22))
    szek28.grid(row=3, column=7)
    szek29 = Button(fkeret, state=NORMAL, text="23", command=lambda:foglal_sz23(23))
    szek29.grid(row=3, column=8)
    szek30 = Button(fkeret, state=NORMAL, text="24", command=lambda:foglal_sz24(24))
    szek30.grid(row=3, column=9)
    szek31 = Button(fkeret, state=NORMAL, text="25", command=lambda:foglal_sz25(25))
    szek31.grid(row=4, column=0, pady=10)
    szek32 = Button(fkeret, state=NORMAL, text="26", command=lambda:foglal_sz26(26))
    szek32.grid(row=4, column=1)
    szek33 = Button(fkeret, state=NORMAL, text="27", command=lambda:foglal_sz27(27))
    szek33.grid(row=4, column=2)
    szek34 = Button(fkeret, state=NORMAL, text="28", command=lambda:foglal_sz28(28))
    szek34.grid(row=4, column=3)
    szek35 = Label(fkeret, width=0)
    szek35.grid(row=4, column=4)
    szek36 = Label(fkeret, width=0)
    szek36.grid(row=4, column=5)
    szek37 = Button(fkeret, state=NORMAL, text="29" , command=lambda:foglal_sz29(29))
    szek37.grid(row=4, column=6)
    szek38 = Button(fkeret, state=NORMAL, text="30", command=lambda:foglal_sz30(30))
    szek38.grid(row=4, column=7)
    szek39 = Button(fkeret, state=NORMAL, text="31" , command=lambda:foglal_sz31(31))
    szek39.grid(row=4, column=8)
    szek40 = Button(fkeret, state=NORMAL, text="32", command=lambda:foglal_sz32(32))
    szek40.grid(row=4, column=9)
    szek41 = Button(fkeret, state=NORMAL, text="33" , command=lambda:foglal_sz33(33))
    szek41.grid(row=5, column=0, pady=10)
    szek42 = Button(fkeret, state=NORMAL, text="34", command=lambda:foglal_sz34(34))
    szek42.grid(row=5, column=1)
    szek43 = Button(fkeret, state=NORMAL, text="35", command=lambda:foglal_sz35(35))
    szek43.grid(row=5, column=2)
    szek44 = Button(fkeret, state=NORMAL, text="36", command=lambda:foglal_sz36(36))
    szek44.grid(row=5, column=3)
    szek45 = Button(fkeret, state=NORMAL, text="37", command=lambda:foglal_sz37(37))
    szek45.grid(row=5, column=4)
    szek46 = Button(fkeret, state=NORMAL, text="38", command=lambda:foglal_sz38(38))
    szek46.grid(row=5, column=5)
    szek47 = Button(fkeret, state=NORMAL, text="39", command=lambda:foglal_sz39(39))
    szek47.grid(row=5, column=6)
    szek48 = Button(fkeret, state=NORMAL, text="40", command=lambda:foglal_sz40(40))
    szek48.grid(row=5, column=7)
    szek49 = Button(fkeret, state=NORMAL, text="41", command=lambda:foglal_sz41(41))
    szek49.grid(row=5, column=8)
    szek50 = Button(fkeret, state=NORMAL, text="42", command=lambda:foglal_sz42(42))
    szek50.grid(row=5, column=9)
    ffoglal = Button(fkeret, text="Helyet foglalok", bootstyle="info", command= lambda:pdf_godzilla())
    ffoglal.grid(row=6, column=0, columnspan=10, pady=10)

def panda_foglal_ablak():
    fog_ablak = Toplevel(root)
    fog_ablak.geometry("1000x800")
    fog_ablak.title("KUNG FU PANDA 4: Foglalás")

    global pand
    pand=0
    def foglal_sz1(b):
        global pand
        if b==1:
            if pand==0 or pand%2==0:
                szek1.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek1.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand+=1

    global pand2
    pand2=0
    def foglal_sz2(b):
        global pand2
        if b==2:
            if pand2==0 or pand2%2==0:
                szek2.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek2.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand2+=1

    global pand3
    pand3=0
    def foglal_sz3(b):
        global pand3
        if b==3:
            if pand3==0 or pand3%2==0:
                szek3.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek3.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand3+=1

    global pand4
    pand4=0
    def foglal_sz4(b):
        global pand4
        if b==4:
            if pand4==0 or pand4%2==0:
                szek4.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek4.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand4+=1


    global pand5
    pand5=0
    def foglal_sz5(b):
        global pand5
        if b==5:
            if pand5==0 or pand5%2==0:
                szek7.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek7.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand5+=1

    global pand6
    pand6=0
    def foglal_sz6(b):
        global pand6
        if b==6:
            if pand6==0 or pand6%2==0:
                szek8.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek8.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand6+=1

    global pand7
    pand7=0
    def foglal_sz7(b):
        global pand7
        if b==7:
            if pand7==0 or pand7%2==0:
                szek9.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek9.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand7+=1

    global pand8
    pand8=0
    def foglal_sz8(b):
        global pand8
        if b==8:
            if pand8==0 or pand8%2==0:
                szek10.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek10.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand8+=1

#sor2
    global pand9
    pand9=0
    def foglal_sz9(b):
        global pand9
        if b==9:
            if pand9==0 or pand9%2==0:
                szek11.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek11.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand9+=1

    global pand10
    pand10=0
    def foglal_sz10(b):
        global pand10
        if b==10:
            if pand10==0 or pand10%2==0:
                szek12.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek12.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand10+=1

    global pand11
    pand11=0
    def foglal_sz11(b):
        global pand11
        if b==11:
            if pand11==0 or pand11%2==0:
                szek13.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek13.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand11+=1

    global pand12
    pand12=0
    def foglal_sz12(b):
        global pand12
        if b==12:
            if pand12==0 or pand12%2==0:
                szek14.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek14.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand12+=1


    global pand13
    pand13=0
    def foglal_sz13(b):
        global pand13
        if b==13:
            if pand13==0 or pand13%2==0:
                szek17.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek17.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand13+=1

    global pand14
    pand14=0
    def foglal_sz14(b):
        global pand14
        if b==14:
            if pand14==0 or pand14%2==0:
                szek18.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek18.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand14+=1

    global pand15
    pand15=0
    def foglal_sz15(b):
        global pand15
        if b==15:
            if pand15==0 or pand15%2==0:
                szek19.config(bootstyle="warning")
                panda_fog_szek.append(str(b))

            else:
                szek19.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand15+=1

    global pand16
    pand16=0
    def foglal_sz16(b):
        global pand16
        if b==16:
            if pand16==0 or pand16%2==0:
                szek20.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek20.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand16+=1


#sor3
    global pand17
    pand17=0
    def foglal_sz17(b):
        global pand17
        if b==17:
            if pand17==0 or pand17%2==0:
                szek21.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek21.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand17+=1

    global pand18
    pand18=0
    def foglal_sz18(b):
        global pand18
        if b==18:
            if pand18==0 or pand18%2==0:
                szek22.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek22.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand18+=1

    global pand19
    pand19=0
    def foglal_sz19(b):
        global pand19
        if b==19:
            if pand19==0 or pand19%2==0:
                szek23.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek23.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand19+=1

    global pand20
    pand20=0
    def foglal_sz20(b):
        global pand20
        if b==20:
            if pand20==0 or pand20%2==0:
                szek24.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek24.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand20+=1


    global pand21
    pand21=0
    def foglal_sz21(b):
        global pand21
        if b==21:
            if pand21==0 or pand21%2==0:
                szek27.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek27.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand21+=1

    global pand22
    pand22=0
    def foglal_sz22(b):
        global pand22
        if b==22:
            if pand22==0 or pand22%2==0:
                szek28.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek28.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand22+=1

    global pand23
    pand23=0
    def foglal_sz23(b):
        global pand23
        if b==23:
            if pand23==0 or pand23%2==0:
                szek29.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek29.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand23+=1

    global pand24
    pand24=0
    def foglal_sz24(b):
        global pand24
        if b==24:
            if pand24==0 or pand24%2==0:
                szek30.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek30.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand24+=1

#sor4
    
    global pand25
    pand25=0
    def foglal_sz25(b):
        global pand25
        if b==25:
            if pand25==0 or pand25%2==0:
                szek31.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek31.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand25+=1

    global pand26
    pand26=0
    def foglal_sz26(b):
        global pand26
        if b==26:
            if pand26==0 or pand26%2==0:
                szek32.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek32.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand26+=1

    global pand27
    pand27=0
    def foglal_sz27(b):
        global pand27
        if b==27:
            if pand27==0 or pand27%2==0:
                szek33.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek33.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand27+=1

    global pand28
    pand28=0
    def foglal_sz28(b):
        global pand28
        if b==28:
            if pand28==0 or pand28%2==0:
                szek34.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek34.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand28+=1


    global pand29
    pand29=0
    def foglal_sz29(b):
        global pand29
        if b==29:
            if pand29==0 or pand29%2==0:
                szek37.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek37.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand29+=1

    global pand30
    pand30=0
    def foglal_sz30(b):
        global pand30
        if b==30:
            if pand30==0 or pand30%2==0:
                szek38.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek38.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand30+=1

    global pand31
    pand31=0
    def foglal_sz31(b):
        global pand31
        if b==31:
            if pand31==0 or pand31%2==0:
                szek39.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek39.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand31+=1

    global pand32
    pand32=0
    def foglal_sz32(b):
        global pand32
        if b==32:
            if pand32==0 or pand32%2==0:
                szek40.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek40.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand32+=1

#sor5
    global pand33
    pand33=0
    def foglal_sz33(b):
        global pand33
        if b==33:
            if pand33==0 or pand33%2==0:
                szek41.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek41.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand33+=1

    global pand34
    pand34=0
    def foglal_sz34(b):
        global pand34
        if b==34:
            if pand34==0 or pand34%2==0:
                szek42.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek42.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand34+=1

    global pand35
    pand35=0
    def foglal_sz35(b):
        global pand35
        if b==35:
            if pand35==0 or pand35%2==0:
                szek43.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek43.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand35+=1

    global pand36
    pand36=0
    def foglal_sz36(b):
        global pand36
        if b==36:
            if pand36==0 or pand36%2==0:
                szek44.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek44.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand36+=1


    global pand37
    pand37=0
    def foglal_sz37(b):
        global pand37
        if b==37:
            if pand37==0 or pand37%2==0:
                szek45.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek45.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand37+=1

    global pand38
    pand38=0
    def foglal_sz38(b):
        global pand38
        if b==38:
            if pand38==0 or pand38%2==0:
                szek46.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek46.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand38+=1

    global pand39
    pand39=0
    def foglal_sz39(b):
        global pand39
        if b==39:
            if pand39==0 or pand39%2==0:
                szek47.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek47.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand39+=1

    global pand40
    pand40=0
    def foglal_sz40(b):
        global pand40
        if b==40:
            if pand40==0 or pand40%2==0:
                szek48.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek48.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand40+=1

    global pand41
    pand41=0
    def foglal_sz41(b):
        global pand41
        if b==41:
            if pand41==0 or pand41%2==0:
                szek49.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek49.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand41+=1

    global pand42
    pand42=0
    def foglal_sz42(b):
        global pand42
        if b==42:
            if pand42==0 or pand42%2==0:
                szek50.config(bootstyle="warning")
                panda_fog_szek.append(str(b))
            else:
                szek50.config(bootstyle="prpandary")
                panda_fog_szek.remove(str(b))
        pand42+=1

    fcimkeret = LabelFrame(fog_ablak, border=0, padding=0, borderwidth=0)
    fcimkeret.grid(row=0, column=0, columnspan=2)
    Label.columnconfigure(fcimkeret, 1, weight=1)
    fcim = Label(fcimkeret, text="KUNG FU PANDA 4", font=("Terminal", 20, "bold"), justify="center", anchor="center", width=90)
    fcim.grid(row=0, column=0, pady=5, sticky="nesw")

    fkepkeret = LabelFrame(fog_ablak, height=370, border=0, padding=0, borderwidth=0)
    fkepkeret.grid(row=1, column=0, padx=50, pady=100)
    dune_al = Canvas(fkepkeret, width=250, height=370, bg='white')
    dune_al.grid(row=0, column=0)
    dune_al.create_image(0, 0, anchor=NW, image=img7)
    sadas=Meter(fkepkeret,bootstyle="warning")
    sadas.grid(row=1, column=0, pady=10)

    fkeret = LabelFrame(fog_ablak, padding=10)
    fkeret.grid(row=1, column=1)
    fleiras = Label(fkeret, text="Csaknem egy évtized után tavasszal visszatér a legkülönösebb kungfu mester a DreamWorks Animation fergeteges sorozatának új fejezetében. Bátor Sárkányharcosként végigcsinált három halált megvető kalandot, és most a sors újabb feladat elé állítja: pihenjen már egy kicsit. Pontosabban hogy legyen a Békevölgy szellemi vezetője. Ezzel van néhány nyilvánvaló probléma. Egyrészt Po annyit tud a szellemi vezetésről, mint a paleodiétáról, másrészt gyorsan találnia kell egy új Sárkányharcost, és ki kell képeznie, mielőtt átvehetné új, magas beosztását. Ám ami még rosszabb, mostanában láttak felbukkanni egy gonosz, nagyhatalmú varázslónőt, Kaméleont, aki apró gyík létére fel tudja venni bármilyen lény alakját, legyen az nagy vagy kicsi. És Kaméleon ráveti dülledt kis szemét a bölcsesség pálcájára, amivel hatalmában állna megidézni az összes gonosztevőt, akiket Po átküldött a szellemek birodalmába...", font=("Times", 12, "bold"), width=50, justify="left", wraplength=400)
    fleiras.grid(row=0, column=0, columnspan=10)
    szek1 = Button(fkeret, state=NORMAL, text="01" ,command=lambda:foglal_sz1(1))
    szek1.grid(row=1, column=0, pady=10)
    szek2 = Button(fkeret, state=NORMAL, text="02", command=lambda:foglal_sz2(2))
    szek2.grid(row=1, column=1)
    szek3 = Button(fkeret, state=NORMAL, text="03", command=lambda:foglal_sz3(3))
    szek3.grid(row=1, column=2)
    szek4 = Button(fkeret, state=NORMAL, text="04", command=lambda:foglal_sz4(4))
    szek4.grid(row=1, column=3)
    szek5 = Label(fkeret, width=0)
    szek5.grid(row=1, column=4)
    szek6 = Label(fkeret, width=0)
    szek6.grid(row=1, column=5)
    szek7 = Button(fkeret, state=NORMAL, text="05", command=lambda:foglal_sz5(5))
    szek7.grid(row=1, column=6)
    szek8 = Button(fkeret, state=NORMAL, text="06" , command=lambda:foglal_sz6(6))
    szek8.grid(row=1, column=7)
    szek9 = Button(fkeret, state=NORMAL, text="07" , command=lambda:foglal_sz7(7))
    szek9.grid(row=1, column=8)
    szek10 = Button(fkeret, state=NORMAL, text="08", command=lambda:foglal_sz8(8))
    szek10.grid(row=1, column=9)
    szek11 = Button(fkeret, state=NORMAL, text="09", command=lambda:foglal_sz9(9))
    szek11.grid(row=2, column=0, pady=10)
    szek12 = Button(fkeret, state=NORMAL, text="10", command=lambda:foglal_sz10(10))
    szek12.grid(row=2, column=1)
    szek13 = Button(fkeret, state=NORMAL, text="11" , command=lambda:foglal_sz11(11))
    szek13.grid(row=2, column=2)
    szek14 = Button(fkeret, state=NORMAL, text="12", command=lambda:foglal_sz12(12))
    szek14.grid(row=2, column=3)
    szek15 = Label(fkeret, width=0)
    szek15.grid(row=2, column=4)
    szek16 = Label(fkeret, width=0)
    szek16.grid(row=2, column=5)
    szek17 = Button(fkeret, state=NORMAL, text="13" , command=lambda:foglal_sz13(13))
    szek17.grid(row=2, column=6)
    szek18 = Button(fkeret, state=NORMAL, text="14" , command=lambda:foglal_sz14(14))
    szek18.grid(row=2, column=7)
    szek19 = Button(fkeret, state=NORMAL, text="15", command=lambda:foglal_sz15(15))
    szek19.grid(row=2, column=8)
    szek20 = Button(fkeret, state=NORMAL, text="16", command=lambda:foglal_sz16(16))
    szek20.grid(row=2, column=9)
    szek21 = Button(fkeret, state=NORMAL, text="17", command=lambda:foglal_sz17(17))
    szek21.grid(row=3, column=0, pady=10)
    szek22 = Button(fkeret, state=NORMAL, text="18", command=lambda:foglal_sz18(18))
    szek22.grid(row=3, column=1)
    szek23 = Button(fkeret, state=NORMAL, text="19", command=lambda:foglal_sz19(19))
    szek23.grid(row=3, column=2)
    szek24 = Button(fkeret, state=NORMAL, text="20", command=lambda:foglal_sz20(20))
    szek24.grid(row=3, column=3)
    szek25 = Label(fkeret, width=0)
    szek25.grid(row=3, column=4)
    szek26 = Label(fkeret, width=0)
    szek26.grid(row=3, column=5)
    szek27 = Button(fkeret, state=NORMAL, text="21", command=lambda:foglal_sz21(21))
    szek27.grid(row=3, column=6)
    szek28 = Button(fkeret, state=NORMAL, text="22", command=lambda:foglal_sz22(22))
    szek28.grid(row=3, column=7)
    szek29 = Button(fkeret, state=NORMAL, text="23", command=lambda:foglal_sz23(23))
    szek29.grid(row=3, column=8)
    szek30 = Button(fkeret, state=NORMAL, text="24", command=lambda:foglal_sz24(24))
    szek30.grid(row=3, column=9)
    szek31 = Button(fkeret, state=NORMAL, text="25", command=lambda:foglal_sz25(25))
    szek31.grid(row=4, column=0, pady=10)
    szek32 = Button(fkeret, state=NORMAL, text="26", command=lambda:foglal_sz26(26))
    szek32.grid(row=4, column=1)
    szek33 = Button(fkeret, state=NORMAL, text="27", command=lambda:foglal_sz27(27))
    szek33.grid(row=4, column=2)
    szek34 = Button(fkeret, state=NORMAL, text="28", command=lambda:foglal_sz28(28))
    szek34.grid(row=4, column=3)
    szek35 = Label(fkeret, width=0)
    szek35.grid(row=4, column=4)
    szek36 = Label(fkeret, width=0)
    szek36.grid(row=4, column=5)
    szek37 = Button(fkeret, state=NORMAL, text="29" , command=lambda:foglal_sz29(29))
    szek37.grid(row=4, column=6)
    szek38 = Button(fkeret, state=NORMAL, text="30", command=lambda:foglal_sz30(30))
    szek38.grid(row=4, column=7)
    szek39 = Button(fkeret, state=NORMAL, text="31" , command=lambda:foglal_sz31(31))
    szek39.grid(row=4, column=8)
    szek40 = Button(fkeret, state=NORMAL, text="32", command=lambda:foglal_sz32(32))
    szek40.grid(row=4, column=9)
    szek41 = Button(fkeret, state=NORMAL, text="33" , command=lambda:foglal_sz33(33))
    szek41.grid(row=5, column=0, pady=10)
    szek42 = Button(fkeret, state=NORMAL, text="34", command=lambda:foglal_sz34(34))
    szek42.grid(row=5, column=1)
    szek43 = Button(fkeret, state=NORMAL, text="35", command=lambda:foglal_sz35(35))
    szek43.grid(row=5, column=2)
    szek44 = Button(fkeret, state=NORMAL, text="36", command=lambda:foglal_sz36(36))
    szek44.grid(row=5, column=3)
    szek45 = Button(fkeret, state=NORMAL, text="37", command=lambda:foglal_sz37(37))
    szek45.grid(row=5, column=4)
    szek46 = Button(fkeret, state=NORMAL, text="38", command=lambda:foglal_sz38(38))
    szek46.grid(row=5, column=5)
    szek47 = Button(fkeret, state=NORMAL, text="39", command=lambda:foglal_sz39(39))
    szek47.grid(row=5, column=6)
    szek48 = Button(fkeret, state=NORMAL, text="40", command=lambda:foglal_sz40(40))
    szek48.grid(row=5, column=7)
    szek49 = Button(fkeret, state=NORMAL, text="41", command=lambda:foglal_sz41(41))
    szek49.grid(row=5, column=8)
    szek50 = Button(fkeret, state=NORMAL, text="42", command=lambda:foglal_sz42(42))
    szek50.grid(row=5, column=9)
    ffoglal = Button(fkeret, text="Helyet foglalok", bootstyle="info", command= lambda:pdf_panda())
    ffoglal.grid(row=6, column=0, columnspan=10, pady=10)

def szellemirtok_foglal_ablak():
    fog_ablak = Toplevel(root)
    fog_ablak.geometry("1000x800")
    fog_ablak.title("SZELLEMIRTÓK - A BORZONGÁS BIRODALMA: Foglalás")

    global szel
    szel=0
    def foglal_sz1(b):
        global szel
        if b==1:
            if szel==0 or szel%2==0:
                szek1.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek1.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel+=1

    global szel2
    szel2=0
    def foglal_sz2(b):
        global szel2
        if b==2:
            if szel2==0 or szel2%2==0:
                szek2.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek2.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel2+=1

    global szel3
    szel3=0
    def foglal_sz3(b):
        global szel3
        if b==3:
            if szel3==0 or szel3%2==0:
                szek3.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek3.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel3+=1

    global szel4
    szel4=0
    def foglal_sz4(b):
        global szel4
        if b==4:
            if szel4==0 or szel4%2==0:
                szek4.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek4.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel4+=1


    global szel5
    szel5=0
    def foglal_sz5(b):
        global szel5
        if b==5:
            if szel5==0 or szel5%2==0:
                szek7.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek7.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel5+=1

    global szel6
    szel6=0
    def foglal_sz6(b):
        global szel6
        if b==6:
            if szel6==0 or szel6%2==0:
                szek8.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek8.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel6+=1

    global szel7
    szel7=0
    def foglal_sz7(b):
        global szel7
        if b==7:
            if szel7==0 or szel7%2==0:
                szek9.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek9.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel7+=1

    global szel8
    szel8=0
    def foglal_sz8(b):
        global szel8
        if b==8:
            if szel8==0 or szel8%2==0:
                szek10.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek10.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel8+=1

#sor2
    global szel9
    szel9=0
    def foglal_sz9(b):
        global szel9
        if b==9:
            if szel9==0 or szel9%2==0:
                szek11.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek11.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel9+=1

    global szel10
    szel10=0
    def foglal_sz10(b):
        global szel10
        if b==10:
            if szel10==0 or szel10%2==0:
                szek12.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek12.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel10+=1

    global szel11
    szel11=0
    def foglal_sz11(b):
        global szel11
        if b==11:
            if szel11==0 or szel11%2==0:
                szek13.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek13.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel11+=1

    global szel12
    szel12=0
    def foglal_sz12(b):
        global szel12
        if b==12:
            if szel12==0 or szel12%2==0:
                szek14.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek14.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel12+=1


    global szel13
    szel13=0
    def foglal_sz13(b):
        global szel13
        if b==13:
            if szel13==0 or szel13%2==0:
                szek17.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek17.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel13+=1

    global szel14
    szel14=0
    def foglal_sz14(b):
        global szel14
        if b==14:
            if szel14==0 or szel14%2==0:
                szek18.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek18.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel14+=1

    global szel15
    szel15=0
    def foglal_sz15(b):
        global szel15
        if b==15:
            if szel15==0 or szel15%2==0:
                szek19.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek19.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel15+=1

    global szel16
    szel16=0
    def foglal_sz16(b):
        global szel16
        if b==16:
            if szel16==0 or szel16%2==0:
                szek20.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek20.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel16+=1


#sor3
    global szel17
    szel17=0
    def foglal_sz17(b):
        global szel17
        if b==17:
            if szel17==0 or szel17%2==0:
                szek21.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek21.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel17+=1

    global szel18
    szel18=0
    def foglal_sz18(b):
        global szel18
        if b==18:
            if szel18==0 or szel18%2==0:
                szek22.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek22.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel18+=1

    global szel19
    szel19=0
    def foglal_sz19(b):
        global szel19
        if b==19:
            if szel19==0 or szel19%2==0:
                szek23.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek23.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel19+=1

    global szel20
    szel20=0
    def foglal_sz20(b):
        global szel20
        if b==20:
            if szel20==0 or szel20%2==0:
                szek24.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek24.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel20+=1


    global szel21
    szel21=0
    def foglal_sz21(b):
        global szel21
        if b==21:
            if szel21==0 or szel21%2==0:
                szek27.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek27.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel21+=1

    global szel22
    szel22=0
    def foglal_sz22(b):
        global szel22
        if b==22:
            if szel22==0 or szel22%2==0:
                szek28.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek28.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel22+=1

    global szel23
    szel23=0
    def foglal_sz23(b):
        global szel23
        if b==23:
            if szel23==0 or szel23%2==0:
                szek29.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek29.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel23+=1

    global szel24
    szel24=0
    def foglal_sz24(b):
        global szel24
        if b==24:
            if szel24==0 or szel24%2==0:
                szek30.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek30.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel24+=1

#sor4
    
    global szel25
    szel25=0
    def foglal_sz25(b):
        global szel25
        if b==25:
            if szel25==0 or szel25%2==0:
                szek31.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek31.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel25+=1

    global szel26
    szel26=0
    def foglal_sz26(b):
        global szel26
        if b==26:
            if szel26==0 or szel26%2==0:
                szek32.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek32.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel26+=1

    global szel27
    szel27=0
    def foglal_sz27(b):
        global szel27
        if b==27:
            if szel27==0 or szel27%2==0:
                szek33.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek33.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel27+=1

    global szel28
    szel28=0
    def foglal_sz28(b):
        global szel28
        if b==28:
            if szel28==0 or szel28%2==0:
                szek34.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek34.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel28+=1


    global szel29
    szel29=0
    def foglal_sz29(b):
        global szel29
        if b==29:
            if szel29==0 or szel29%2==0:
                szek37.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek37.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel29+=1

    global szel30
    szel30=0
    def foglal_sz30(b):
        global szel30
        if b==30:
            if szel30==0 or szel30%2==0:
                szek38.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek38.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel30+=1

    global szel31
    szel31=0
    def foglal_sz31(b):
        global szel31
        if b==31:
            if szel31==0 or szel31%2==0:
                szek39.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek39.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel31+=1

    global szel32
    szel32=0
    def foglal_sz32(b):
        global szel32
        if b==32:
            if szel32==0 or szel32%2==0:
                szek40.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek40.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel32+=1

#sor5
    global szel33
    szel33=0
    def foglal_sz33(b):
        global szel33
        if b==33:
            if szel33==0 or szel33%2==0:
                szek41.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek41.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel33+=1

    global szel34
    szel34=0
    def foglal_sz34(b):
        global szel34
        if b==34:
            if szel34==0 or szel34%2==0:
                szek42.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek42.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel34+=1

    global szel35
    szel35=0
    def foglal_sz35(b):
        global szel35
        if b==35:
            if szel35==0 or szel35%2==0:
                szek43.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek43.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel35+=1

    global szel36
    szel36=0
    def foglal_sz36(b):
        global szel36
        if b==36:
            if szel36==0 or szel36%2==0:
                szek44.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek44.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel36+=1


    global szel37
    szel37=0
    def foglal_sz37(b):
        global szel37
        if b==37:
            if szel37==0 or szel37%2==0:
                szek45.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek45.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel37+=1

    global szel38
    szel38=0
    def foglal_sz38(b):
        global szel38
        if b==38:
            if szel38==0 or szel38%2==0:
                szek46.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek46.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel38+=1

    global szel39
    szel39=0
    def foglal_sz39(b):
        global szel39
        if b==39:
            if szel39==0 or szel39%2==0:
                szek47.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek47.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel39+=1

    global szel40
    szel40=0
    def foglal_sz40(b):
        global szel40
        if b==40:
            if szel40==0 or szel40%2==0:
                szek48.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek48.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel40+=1

    global szel41
    szel41=0
    def foglal_sz41(b):
        global szel41
        if b==41:
            if szel41==0 or szel41%2==0:
                szek49.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek49.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel41+=1

    global szel42
    szel42=0
    def foglal_sz42(b):
        global szel42
        if b==42:
            if szel42==0 or szel42%2==0:
                szek50.config(bootstyle="warning")
                szellemirtok_fog_szek.append(str(b))
            else:
                szek50.config(bootstyle="prszelary")
                szellemirtok_fog_szek.remove(str(b))
        szel42+=1

    fcimkeret = LabelFrame(fog_ablak, border=0, padding=0, borderwidth=0)
    fcimkeret.grid(row=0, column=0, columnspan=2)
    Label.columnconfigure(fcimkeret, 1, weight=1)
    fcim = Label(fcimkeret, text="SZELLEMIRTÓK - A BORZONGÁS BIRODALMA", font=("Terminal", 20, "bold"), justify="center", anchor="center", width=90)
    fcim.grid(row=0, column=0, pady=5, sticky="nesw")

    fkepkeret = LabelFrame(fog_ablak, height=370, border=0, padding=0, borderwidth=0)
    fkepkeret.grid(row=1, column=0, padx=50, pady=100)
    dune_al = Canvas(fkepkeret, width=250, height=370, bg='white')
    dune_al.grid(row=0, column=0)
    dune_al.create_image(0, 0, anchor=NW, image=img8)
    sadas=Meter(fkepkeret,bootstyle="warning")
    sadas.grid(row=1, column=0, pady=10)


    fkeret = LabelFrame(fog_ablak, padding=10)
    fkeret.grid(row=1, column=1)
    fleiras = Label(fkeret, text="Kit hívsz, ha nagy baj van?  Kihez fordulnál segítségért, amikor szellemek piszkálnak, kísértetek kísérleteznek veled, vagy hazajáró lelkek dúlják fel a házad? A válasz egyértelmű: a Szellemirtókhoz! De ma már nem ugyanaz a négyes száll be a legendás autóba, amikor riasztás érkezik.Viszont a híres New York-i tűzoltótorony nem változott: az új szellemirtók, a Spengler család tagjai itt találkoznak az eredeti csapattal, akik, mint kiderül, nem mentek nyugdíjba: szupertitkos kísérleti laboratóriumot hoztak létre, hogy még magasabb szinten űzhessék a szellemszakmát. Csakhogy rátalálnak egy ősi műtárgyra, amelyből elszabadul egy gonosz erő – és az öregeknek meg a fiataloknak össze kell fogniuk, hogy megmentsék a világot az új, és mindennél fagyosabb jégkorszaktól.", font=("Times", 12, "bold"), width=50, justify="left", wraplength=400)
    fleiras.grid(row=0, column=0, columnspan=10)
    szek1 = Button(fkeret, state=NORMAL, text="01" ,command=lambda:foglal_sz1(1))
    szek1.grid(row=1, column=0, pady=10)
    szek2 = Button(fkeret, state=NORMAL, text="02", command=lambda:foglal_sz2(2))
    szek2.grid(row=1, column=1)
    szek3 = Button(fkeret, state=NORMAL, text="03", command=lambda:foglal_sz3(3))
    szek3.grid(row=1, column=2)
    szek4 = Button(fkeret, state=NORMAL, text="04", command=lambda:foglal_sz4(4))
    szek4.grid(row=1, column=3)
    szek5 = Label(fkeret, width=0)
    szek5.grid(row=1, column=4)
    szek6 = Label(fkeret, width=0)
    szek6.grid(row=1, column=5)
    szek7 = Button(fkeret, state=NORMAL, text="05", command=lambda:foglal_sz5(5))
    szek7.grid(row=1, column=6)
    szek8 = Button(fkeret, state=NORMAL, text="06" , command=lambda:foglal_sz6(6))
    szek8.grid(row=1, column=7)
    szek9 = Button(fkeret, state=NORMAL, text="07" , command=lambda:foglal_sz7(7))
    szek9.grid(row=1, column=8)
    szek10 = Button(fkeret, state=NORMAL, text="08", command=lambda:foglal_sz8(8))
    szek10.grid(row=1, column=9)
    szek11 = Button(fkeret, state=NORMAL, text="09", command=lambda:foglal_sz9(9))
    szek11.grid(row=2, column=0, pady=10)
    szek12 = Button(fkeret, state=NORMAL, text="10", command=lambda:foglal_sz10(10))
    szek12.grid(row=2, column=1)
    szek13 = Button(fkeret, state=NORMAL, text="11" , command=lambda:foglal_sz11(11))
    szek13.grid(row=2, column=2)
    szek14 = Button(fkeret, state=NORMAL, text="12", command=lambda:foglal_sz12(12))
    szek14.grid(row=2, column=3)
    szek15 = Label(fkeret, width=0)
    szek15.grid(row=2, column=4)
    szek16 = Label(fkeret, width=0)
    szek16.grid(row=2, column=5)
    szek17 = Button(fkeret, state=NORMAL, text="13" , command=lambda:foglal_sz13(13))
    szek17.grid(row=2, column=6)
    szek18 = Button(fkeret, state=NORMAL, text="14" , command=lambda:foglal_sz14(14))
    szek18.grid(row=2, column=7)
    szek19 = Button(fkeret, state=NORMAL, text="15", command=lambda:foglal_sz15(15))
    szek19.grid(row=2, column=8)
    szek20 = Button(fkeret, state=NORMAL, text="16", command=lambda:foglal_sz16(16))
    szek20.grid(row=2, column=9)
    szek21 = Button(fkeret, state=NORMAL, text="17", command=lambda:foglal_sz17(17))
    szek21.grid(row=3, column=0, pady=10)
    szek22 = Button(fkeret, state=NORMAL, text="18", command=lambda:foglal_sz18(18))
    szek22.grid(row=3, column=1)
    szek23 = Button(fkeret, state=NORMAL, text="19", command=lambda:foglal_sz19(19))
    szek23.grid(row=3, column=2)
    szek24 = Button(fkeret, state=NORMAL, text="20", command=lambda:foglal_sz20(20))
    szek24.grid(row=3, column=3)
    szek25 = Label(fkeret, width=0)
    szek25.grid(row=3, column=4)
    szek26 = Label(fkeret, width=0)
    szek26.grid(row=3, column=5)
    szek27 = Button(fkeret, state=NORMAL, text="21", command=lambda:foglal_sz21(21))
    szek27.grid(row=3, column=6)
    szek28 = Button(fkeret, state=NORMAL, text="22", command=lambda:foglal_sz22(22))
    szek28.grid(row=3, column=7)
    szek29 = Button(fkeret, state=NORMAL, text="23", command=lambda:foglal_sz23(23))
    szek29.grid(row=3, column=8)
    szek30 = Button(fkeret, state=NORMAL, text="24", command=lambda:foglal_sz24(24))
    szek30.grid(row=3, column=9)
    szek31 = Button(fkeret, state=NORMAL, text="25", command=lambda:foglal_sz25(25))
    szek31.grid(row=4, column=0, pady=10)
    szek32 = Button(fkeret, state=NORMAL, text="26", command=lambda:foglal_sz26(26))
    szek32.grid(row=4, column=1)
    szek33 = Button(fkeret, state=NORMAL, text="27", command=lambda:foglal_sz27(27))
    szek33.grid(row=4, column=2)
    szek34 = Button(fkeret, state=NORMAL, text="28", command=lambda:foglal_sz28(28))
    szek34.grid(row=4, column=3)
    szek35 = Label(fkeret, width=0)
    szek35.grid(row=4, column=4)
    szek36 = Label(fkeret, width=0)
    szek36.grid(row=4, column=5)
    szek37 = Button(fkeret, state=NORMAL, text="29" , command=lambda:foglal_sz29(29))
    szek37.grid(row=4, column=6)
    szek38 = Button(fkeret, state=NORMAL, text="30", command=lambda:foglal_sz30(30))
    szek38.grid(row=4, column=7)
    szek39 = Button(fkeret, state=NORMAL, text="31" , command=lambda:foglal_sz31(31))
    szek39.grid(row=4, column=8)
    szek40 = Button(fkeret, state=NORMAL, text="32", command=lambda:foglal_sz32(32))
    szek40.grid(row=4, column=9)
    szek41 = Button(fkeret, state=NORMAL, text="33" , command=lambda:foglal_sz33(33))
    szek41.grid(row=5, column=0, pady=10)
    szek42 = Button(fkeret, state=NORMAL, text="34", command=lambda:foglal_sz34(34))
    szek42.grid(row=5, column=1)
    szek43 = Button(fkeret, state=NORMAL, text="35", command=lambda:foglal_sz35(35))
    szek43.grid(row=5, column=2)
    szek44 = Button(fkeret, state=NORMAL, text="36", command=lambda:foglal_sz36(36))
    szek44.grid(row=5, column=3)
    szek45 = Button(fkeret, state=NORMAL, text="37", command=lambda:foglal_sz37(37))
    szek45.grid(row=5, column=4)
    szek46 = Button(fkeret, state=NORMAL, text="38", command=lambda:foglal_sz38(38))
    szek46.grid(row=5, column=5)
    szek47 = Button(fkeret, state=NORMAL, text="39", command=lambda:foglal_sz39(39))
    szek47.grid(row=5, column=6)
    szek48 = Button(fkeret, state=NORMAL, text="40", command=lambda:foglal_sz40(40))
    szek48.grid(row=5, column=7)
    szek49 = Button(fkeret, state=NORMAL, text="41", command=lambda:foglal_sz41(41))
    szek49.grid(row=5, column=8)
    szek50 = Button(fkeret, state=NORMAL, text="42", command=lambda:foglal_sz42(42))
    szek50.grid(row=5, column=9)
    ffoglal = Button(fkeret, text="Helyet foglalok", bootstyle="info", command= lambda:pdf_szellemirtok())
    ffoglal.grid(row=6, column=0, columnspan=10, pady=10)


dunenev = "DŰNE - MÁSODIK RÉSZ"
dunehossz = 166
dunedate = "2024-02-29"
dunedesc = "A távoli jövőben, a bolygóközi királyságok korában játszódó történetben két nagyhatalmú uralkodóház harcol az Arrakis bolygó feletti hatalomért, mert az ismert univerzumban egyedül az itteni végtelen sivatagban bányászható az a fűszer, amely lehetővé teszi a csillagközi utazást. A Harkonnenek ura kiirtatta az Atreides családot. De Paul Atreides herceg (Timothée Chalamet) megmenekült: a pusztaságban bujkál egy titokzatos, nomád nép, a fremenek között, ahol megismerkedik egy lánnyal, Csanival (Zendaya). Az a sorsa, hogy bosszút álljon a családjáért, háborúba vezesse a hozzá hű seregeket. Döntenie kell, hogy élete nagy szerelmét választja-e, vagy beteljesíti a végzetét. Az univerzum sorsa múlik azon, hogy mit határoz: és végül olyan útra lép, amely megváltoztathatja azt a szörnyű jövőt, amelyet egyedül ő lát előre."

mostnev = "MOST VAGY SOHA!"
mosthossz = 135
mostdate = "2024-03-14"
mostdesc = "Amikor 1848. március 15-én a lánglelkű költő, Petőfi Sándor költeményével, a Nemzeti Dallal kirobbantja a magyar forradalmat, az osztrák elnyomók egy titkosügynököt bíznak meg a feladattal, hogy állítsa meg a felkelést."

imadlaknev = "IMÁDLAK UTÁLNI"
imadlakhossz = 100
imadlakdate = "2024-01-18"
imadlakdesc = "Találkoztak, együtt töltöttek egy éjszakát, és azóta gyűlölik egymást. Van ilyen. Bea (Sydney Sweeney) és Ben (Glen Powell) biztos, hogy nem illenek össze. Ha néha véletlenül összefutnak valahol, tutira elszabadul a pokol: csak bántani tudják egymást. De lesz egy esküvő Ausztráliában, amin mindkettejüknek részt kell venniük. Nincs kibúvó, nincs duma: utazniuk kell. Néhány napon, néhány bulin, néhány vacsorán keresztül el kell viselniük egymás közelségét, miközben egy gyönyörű tengerparti házban ott kavarog körülöttük egy csomó régi szerelmük, néhány kíváncsi rokonuk és kavarni mindig kész felmenőjük. Szóval, azt teszik, amit két érett, felnőtt, felelősségteljes ember ilyenkor tehet: úgy tesznek, mintha szerelmespár lennének – azt remélik, hogy így mindenkinek könnyebb lesz. Nem is tévedhettek volna nagyobbat.Amikor 1848. március 15-én a lánglelkű költő, Petőfi Sándor költeményével, a Nemzeti Dallal kirobbantja a magyar forradalmat, az osztrák elnyomók egy titkosügynököt bíznak meg a feladattal, hogy állítsa meg a felkelést."

mehesznev = "A MÉHÉSZ"
meheszhossz = 105
meheszdate = "2024-01-11"
meheszdesc = "Egy férfi egyszemélyes, brutális bosszúhadjáratának tétje országos szintűre nő, miután kiderül róla, hogy korábban a Méhészek néven ismert befolyásos és titkos szervezet ügynöke volt."

kingnev = "ARTÚR, A KIRÁLY"
kinghossz = 107
kingdate = "2024-03-21"
kingdesc = "Michael Light (Mark Wahlberg) és elszánt csapata a Dominikai Köztársaság dzsungelében teszi próbára magát egy rendkívüli 10 napos, 700 kilométeres extrémsport-világbajnokságon. A kalandvágyó sportember életében ez az utolsó lehetőség, hogy a régen áhított első helyezést elérje, a túra során azonban váratlanul egy ágrólszakadt kóborkutya szegődik melléjük. Michael és a különös, mégis méltóságteljes állat között hamarosan megbonthatatlan barátság szövődik, és a verseny végére Michael számára a győzelem, a hűség és a barátság jelentése merőben új értelmet nyer."

godzillanev = "GODZILLA X KONG: AZ ÚJ BIRODALOM"
godzillahossz = 115
godzilladate = "2024-03-28"
godzilladesc = "A mindent eldöntő, minden eddiginél nagyobb háború nem ért véget azzal, hogy Kong és Godzilla szembetalálkozott és összemérte az erejét. Mert az ember most már kénytelen belenyugodni, hogy nem ő a legerősebb a földön. És nem ismeri igazán a saját világát: várja még néhány eddig rejtve maradt meglepetés. Bujkál még valami a föld alatt, ami felébredt, és pusztítani akar. Az emberiség képtelen megállítani. Talán Kong is képtelen volna. És Godzilla is. De ha ők ketten összefognának, akkor esetleg megmenekülhetnének ők is és mi is…"

pandanev = "KUNG FU PANDA 4"
pandahossz = 94
pandadate = "2024-03-21"
pandadesc = "Csaknem egy évtized után tavasszal visszatér a legkülönösebb kungfu mester a DreamWorks Animation fergeteges sorozatának baresz új fejezetében. Bátor Sárkányharcosként végigcsinált három halált megvető kalandot, és most a sors újabb feladat elé állítja: pihenjen már egy kicsit. Pontosabban hogy legyen a Békevölgy szellemi vezetője. Ezzel van néhány nyilvánvaló probléma. Egyrészt Po annyit tud a szellemi vezetésről, mint a paleodiétáról, másrészt gyorsan találnia kell egy új Sárkányharcost, és ki kell képeznie, mielőtt átvehetné új, magas beosztását. Ám ami még rosszabb, mostanában láttak felbukkanni egy gonosz, nagy hatalmú varázslónőt, Kaméleont, aki apró gyík létére fel tudja venni bármilyen lény alakját, legyen az nagy vagy kicsi. És Kaméleon ráveti dülledt kis szemét a bölcsesség pálcájára, amivel hatalmában állna megidézni az összes gonosztevőt, akiket Po átküldött a szellemek birodalmába..."

szellemirtoknev = "SZELLEMIRTÓK - A BORZONGÁS BIRODALMA"
szellemirtokhossz = 125
szellemirtokdate = "2024-04-11"
szellemirtokdesc = "Kihez fordulsz nagy bajban? Kitől kérsz segítséget, amikor kísérteties lények vesznek üldözőbe? Az egyértelmű válasz: a Szellemirtókat! A legendás csapat azonban már nem az eredeti felállásban dolgozik. A változás ellenére a híres New York-i tűzoltóság viszont továbbra is működik. Itt találkoznak az új Szellemirtók, a Spengler család tagjai az eredeti csapattal, akik, mint kiderül, nem vonultak vissza, hanem egy titkos kísérleti laboratóriumot hoztak létre, hogy szellemirtó törekvéseiket újabb szintre emeljék. Terveik váratlan fordulatot vesznek, amikor egy ősi ereklyére bukkannak, amely rosszindulatú erőt szabadít fel. Most mind a tapasztalt, mind a fiatal Szellemirtóknak össze kell fogniuk, hogy meghiúsítsák a világ közelgő veszélyét – a közelgő és még inkább dermesztő jégkorszakot. A legendás film szereplőgárdája, köztük Bill Murray és Dan Aykroyd diadalmasan tér vissza, vegyítve a humort a sci-fivel és a hátborzongató találkozásokat a laza tréfálkozással. Hozzájuk csatlakoznak az új generációs színészek, mint Paul Rudd és Finn Wolfhard a szeretett saga folytatásában."

vetites1film = 1
vetites1ido = "Hétfő"
vetites1ar = round(random.randint(2500, 6500), -2)

vetites2film = 2
vetites2ido = "Hétfő"
vetites2ar = round(random.randint(2500, 6500), -2)

vetites3film = 3
vetites3ido = "Hétfő"
vetites3ar = round(random.randint(2500, 6500), -2)

vetites4film = 4
vetites4ido = "Hétfő"
vetites4ar = round(random.randint(2500, 6500), -2)

vetites5film = 6
vetites5ido = "Kedd"
vetites5ar = round(random.randint(2500, 6500), -2)

vetites6film = 3
vetites6ido = "Kedd"
vetites6ar = round(random.randint(2500, 6500), -2)

vetites7film = 6
vetites7ido = "Kedd"
vetites7ar = round(random.randint(2500, 6500), -2)

vetites8film = 8
vetites8ido = "Kedd"
vetites8ar = round(random.randint(2500, 6500), -2)

vetites9film = 2
vetites9ido = "Szerda"
vetites9ar = round(random.randint(2500, 6500), -2)

vetites10film = 7
vetites10ido = "Szerda"
vetites10ar = round(random.randint(2500, 6500), -2)

vetites11film = 4
vetites11ido = "Szerda"
vetites11ar = round(random.randint(2500, 6500), -2)

vetites12film = 8
vetites12ido = "Szerda"
vetites12ar = round(random.randint(2500, 6500), -2)

vetites13film = 1
vetites13ido = "Csütörtök"
vetites13ar = round(random.randint(2500, 6500), -2)

vetites14film = 4
vetites14ido = "Csütörtök"
vetites14ar = round(random.randint(2500, 6500), -2)

vetites15film = 7
vetites15ido = "Csütörtök"
vetites15ar = round(random.randint(2500, 6500), -2)

vetites16film = 6
vetites16ido = "Csütörtök"
vetites16ar = round(random.randint(2500, 6500), -2)

vetites17film = 6
vetites17ido = "Péntek"
vetites17ar = round(random.randint(2500, 6500), -2)

vetites18film = 5
vetites18ido = "Péntek"
vetites18ar = round(random.randint(2500, 6500), -2)

vetites19film = 3
vetites19ido = "Péntek"
vetites19ar = round(random.randint(2500, 6500), -2)

vetites20film = 2
vetites20ido = "Péntek"
vetites20ar = round(random.randint(2500, 6500), -2)

vetites21film = 6
vetites21ido = "Szombat"
vetites21ar = round(random.randint(2500, 6500), -2)

vetites22film = 5
vetites22ido = "Szombat"
vetites22ar = round(random.randint(2500, 6500), -2)

vetites23film = 4
vetites23ido = "Szombat"
vetites23ar = round(random.randint(2500, 6500), -2)

vetites24film = 1
vetites24ido = "Szombat"
vetites24ar = round(random.randint(2500, 6500), -2)

vetites25film = 7
vetites25ido = "Vasárnap"
vetites25ar = round(random.randint(2500, 6500), -2)

vetites26film = 4
vetites26ido = "Vasárnap"
vetites26ar = round(random.randint(2500, 6500), -2)

vetites27film = 2
vetites27ido = "Vasárnap"
vetites27ar = round(random.randint(2500, 6500), -2)

vetites28film = 1
vetites28ido = "Vasárnap"
vetites28ar = round(random.randint(2500, 6500), -2)

adatbazis()



img1 = ImageTk.PhotoImage(Image.open("dune.png")) 
img2 = ImageTk.PhotoImage(Image.open("most.png"))  
img3 = ImageTk.PhotoImage(Image.open("imadlak.png"))  
img4 = ImageTk.PhotoImage(Image.open("mehesz.png"))  
img5 = ImageTk.PhotoImage(Image.open("king.png"))  
img6 = ImageTk.PhotoImage(Image.open("godzilla.png"))  
img7 = ImageTk.PhotoImage(Image.open("panda.png"))  
img8 = ImageTk.PhotoImage(Image.open("szellemirtok.png"))

cimframe=Labelframe(root, border=0, width=1400)
cimframe.pack()

cim=Label(cimframe, text="MoziTown",font=("Terminal","35","bold"),justify=CENTER)
cim.grid(pady=20, padx=615, row=0,column=0, columnspan=2)

def time():
    string = strftime('%H:%M')
    ora.config(text=string)
    ora.after(1000, time)


ora = Label(cimframe, font=('calibri', 20, 'bold'),foreground='white')
ora.grid(row=0, padx=20,column=1)
time()

def hetfo():
    mon.configure(bootstyle="warning")
    tue.configure(bootstyle="warning-outline")
    wed.configure(bootstyle="warning-outline")
    thu.configure(bootstyle="warning-outline")
    fri.configure(bootstyle="warning-outline")
    sat.configure(bootstyle="warning-outline")
    sun.configure(bootstyle="warning-outline")
    musor.configure(text="Műsoron - hétfő")
    dune.create_image(0, 0, anchor=NW, image=img1)
    cim1.configure(text="DŰNE - MÁSODIK RÉSZ")
    buy1.configure(command=lambda: dune_foglal_ablak())

    most.create_image(0, 0, anchor=NW, image=img2)
    cim2.configure(text="MOST VAGY SOHA!")
    buy2.configure(command=lambda: most_foglal_ablak())

    imadlak.create_image(0, 0, anchor=NW, image=img3)
    cim3.configure(text="IMÁDLAK UTÁLNI")
    buy3.configure(command=lambda: imadlak_foglal_ablak())

    mehesz.create_image(0, 0, anchor=NW, image=img4)
    cim4.configure(text="A MÉHÉSZ")
    buy4.configure(command=lambda: mehesz_foglal_ablak())

def kedd():
    global img5
    tue.configure(bootstyle="warning")
    mon.configure(bootstyle="warning-outline")
    wed.configure(bootstyle="warning-outline")
    thu.configure(bootstyle="warning-outline")
    fri.configure(bootstyle="warning-outline")
    sat.configure(bootstyle="warning-outline")
    sun.configure(bootstyle="warning-outline")
    musor.configure(text="Műsoron - kedd")
    dune.create_image(0, 0, anchor=NW, image=img5)
    cim1.configure(text="ARTÚR, A KIRÁLY")
    buy1.configure(command=lambda: king_foglal_ablak())

    most.create_image(0, 0, anchor=NW, image=img3)
    cim2.configure(text="IMÁDLAK UTÁLNI")
    buy2.configure(command=lambda: imadlak_foglal_ablak())

    imadlak.create_image(0, 0, anchor=NW, image=img6)
    cim3.configure(text="GODZILLA X KONG: ...")
    buy3.configure(command=lambda: godzilla_foglal_ablak())

    mehesz.create_image(0, 0, anchor=NW, image=img8)
    cim4.configure(text="SZELLEMIRTÓK ...")
    buy4.configure(command=lambda: szellemirtok_foglal_ablak())

def szerda():
    wed.configure(bootstyle="warning")
    tue.configure(bootstyle="warning-outline")
    mon.configure(bootstyle="warning-outline")
    thu.configure(bootstyle="warning-outline")
    fri.configure(bootstyle="warning-outline")
    sat.configure(bootstyle="warning-outline")
    sun.configure(bootstyle="warning-outline")
    musor.configure(text="Műsoron - szerda")
    dune.create_image(0, 0, anchor=NW, image=img2)
    cim1.configure(text="MOST VAGY SOHA!")
    buy1.configure(command=lambda: most_foglal_ablak())

    most.create_image(0, 0, anchor=NW, image=img7)
    cim2.configure(text="KUNG FU PANDA 4")
    buy2.configure(command=lambda: panda_foglal_ablak())

    imadlak.create_image(0, 0, anchor=NW, image=img4)
    cim3.configure(text="A MÉHÉSZ")
    buy3.configure(command=lambda: mehesz_foglal_ablak())

    mehesz.create_image(0, 0, anchor=NW, image=img8)
    cim4.configure(text="SZELLEMIRTÓK ...")
    buy4.configure(command=lambda: szellemirtok_foglal_ablak())

def csutotok():
    thu.configure(bootstyle="warning")
    tue.configure(bootstyle="warning-outline")
    wed.configure(bootstyle="warning-outline")
    mon.configure(bootstyle="warning-outline")
    fri.configure(bootstyle="warning-outline")
    sat.configure(bootstyle="warning-outline")
    sun.configure(bootstyle="warning-outline")
    musor.configure(text="Műsoron - csütörtök")
    dune.create_image(0, 0, anchor=NW, image=img1)
    cim1.configure(text="DŰNE - MÁSODIK RÉSZ")
    buy1.configure(command=lambda: dune_foglal_ablak())

    most.create_image(0, 0, anchor=NW, image=img4)
    cim2.configure(text="A MÉHÉSZ")
    buy2.configure(command=lambda: mehesz_foglal_ablak())

    imadlak.create_image(0, 0, anchor=NW, image=img7)
    cim3.configure(text="KUNG FU PANDA 4")
    buy3.configure(command=lambda: panda_foglal_ablak())

    mehesz.create_image(0, 0, anchor=NW, image=img6)
    cim4.configure(text="GODZILLA X KONG: ...")
    buy4.configure(command=lambda: godzilla_foglal_ablak())

def pentek():
    fri.configure(bootstyle="warning")
    tue.configure(bootstyle="warning-outline")
    wed.configure(bootstyle="warning-outline")
    thu.configure(bootstyle="warning-outline")
    mon.configure(bootstyle="warning-outline")
    sat.configure(bootstyle="warning-outline")
    sun.configure(bootstyle="warning-outline")
    musor.configure(text="Műsoron - péntek")
    dune.create_image(0, 0, anchor=NW, image=img8)
    cim1.configure(text="GODZILLA X KONG: ...")
    buy1.configure(command=lambda: godzilla_foglal_ablak())

    most.create_image(0, 0, anchor=NW, image=img5)
    cim2.configure(text="ARTÚR, A KIRÁLY")
    buy2.configure(command=lambda: king_foglal_ablak())

    imadlak.create_image(0, 0, anchor=NW, image=img3)
    cim3.configure(text="IMÁDLAK UTÁLNI")
    buy3.configure(command=lambda: imadlak_foglal_ablak())

    mehesz.create_image(0, 0, anchor=NW, image=img2)
    cim4.configure(text="MOST VAGY SOHA!")
    buy4.configure(command=lambda: most_foglal_ablak())

def szombat():
    sat.configure(bootstyle="warning")
    tue.configure(bootstyle="warning-outline")
    wed.configure(bootstyle="warning-outline")
    thu.configure(bootstyle="warning-outline")
    fri.configure(bootstyle="warning-outline")
    mon.configure(bootstyle="warning-outline")
    sun.configure(bootstyle="warning-outline")
    musor.configure(text="Műsoron - szombat")
    dune.create_image(0, 0, anchor=NW, image=img6)
    cim1.configure(text="GODZILLA X KONG: ...",)
    buy1.configure(command=lambda: godzilla_foglal_ablak())

    most.create_image(0, 0, anchor=NW, image=img5)
    cim2.configure(text="ARTÚR, A KIRÁLY")
    buy2.configure(command=lambda: king_foglal_ablak())

    imadlak.create_image(0, 0, anchor=NW, image=img4)
    cim3.configure(text="A MÉHÉSZ")
    buy3.configure(command=lambda: mehesz_foglal_ablak())

    mehesz.create_image(0, 0, anchor=NW, image=img1)
    cim4.configure(text="DŰNE - MÁSODIK RÉSZ")
    buy4.configure(command=lambda: dune_foglal_ablak())

def vasarnap():
    sun.configure(bootstyle="warning")
    tue.configure(bootstyle="warning-outline")
    wed.configure(bootstyle="warning-outline")
    thu.configure(bootstyle="warning-outline")
    fri.configure(bootstyle="warning-outline")
    sat.configure(bootstyle="warning-outline")
    mon.configure(bootstyle="warning-outline")
    musor.configure(text="Műsoron - vasárnap")
    dune.create_image(0, 0, anchor=NW, image=img7)
    cim1.configure(text="KUNG FU PANDA 4")
    buy1.configure(command=lambda: panda_foglal_ablak())

    most.create_image(0, 0, anchor=NW, image=img4)
    cim2.configure(text="A MÉHÉSZ")
    buy2.configure(command=lambda: mehesz_foglal_ablak())

    imadlak.create_image(0, 0, anchor=NW, image=img2)
    cim3.configure(text="MOST VAGY SOHA!")
    buy3.configure(command=lambda: most_foglal_ablak())

    mehesz.create_image(0, 0, anchor=NW, image=img1)
    cim4.configure(text="DŰNE - MÁSODIK RÉSZ")
    buy4.configure(command=lambda: dune_foglal_ablak())


style=ttk.Style().configure("frame_style", background="#181D31")
napokfram=LabelFrame(root, border=0,)
napokfram.pack(pady=10)

mon=Button(napokfram,text="Hétfő", bootstyle="warning", command=hetfo)
mon.grid(row=0, column=0,pady=(0,15),padx=15)
tue=Button(napokfram,text="Kedd", bootstyle="warning-outline", command=kedd)
tue.grid(row=0, column=1,pady=(0,15),padx=15)
wed=Button(napokfram,text="Szerda", bootstyle="warning-outline", command=szerda)
wed.grid(row=0, column=2,pady=(0,15),padx=15)
thu=Button(napokfram,text="Csütörtök", bootstyle="warning-outline", command=csutotok)
thu.grid(row=0, column=3,pady=(0,15),padx=15)
fri=Button(napokfram,text="Péntek", bootstyle="warning-outline",command=pentek)
fri.grid(row=0, column=4,pady=(0,15),padx=15)
sat=Button(napokfram,text="Szombat", bootstyle="warning-outline", command=szombat)
sat.grid(row=0, column=5,pady=(0,15),padx=15)
sun=Button(napokfram,text="Vasárnap", bootstyle="warning-outline", command=vasarnap)
sun.grid(row=0, column=6,pady=(0,15),padx=15)

musor=Label(root,text="Műsoron - hétfő",font=('calibri', 25, 'bold'),background="#181D31")
musor.pack(pady=(0,8))

filmekframe=LabelFrame(root, style="frame_style", )
filmekframe.pack()

film1=LabelFrame(filmekframe, width=240, height=500,border=0)
film1.grid(row=0,column=0, padx=20,pady=0)

film2=LabelFrame(filmekframe,width=240, height=500,border=0)
film2.grid(row=0,column=1, padx=20)

film3=LabelFrame(filmekframe, width=240, height=500,border=0)
film3.grid(row=0,column=2, padx=20)

film4=LabelFrame(filmekframe,width=240, height=500,border=0)
film4.grid(row=0,column=3, padx=20)

dune = Canvas(film1, width=250, height=370, bg='white')
dune.pack()
dune.create_image(0, 0, anchor=NW, image=img1)
cim1=Label(film1,text="DŰNE - MÁSODIK RÉSZ",font=('calibri', 15, 'bold'))
cim1.pack(pady=(6,0))
buy1=Button(film1,text="Vásárlás", bootstyle="warning", command=lambda: dune_foglal_ablak())
buy1.pack(pady=6,padx=15,)

most = Canvas(film2, width=250, height=370, bg='white')
most.pack()
most.create_image(0, 0, anchor=NW, image=img2)
cim2=Label(film2,text="MOST VAGY SOHA!",font=('calibri', 15, 'bold'))
cim2.pack(pady=(6,0))
buy2=Button(film2,text="Vásárlás", bootstyle="warning", command=lambda: most_foglal_ablak())
buy2.pack(pady=6,padx=15,)

imadlak = Canvas(film3, width=250, height=370, bg='white')
imadlak.pack()
imadlak.create_image(0, 0, anchor=NW, image=img3)
cim3=Label(film3,text="IMÁDLAK UTÁLNI",font=('calibri', 15, 'bold'))
cim3.pack(pady=(6,0))
buy3=Button(film3,text="Vásárlás", bootstyle="warning", command=lambda: imadlak_foglal_ablak())
buy3.pack(pady=6,padx=15,)

mehesz = Canvas(film4, width=250, height=370, bg='white')
mehesz.pack()
mehesz.create_image(0, 0, anchor=NW, image=img4)
cim4=Label(film4,text="A MÉHÉSZ",font=('calibri', 15, 'bold'))
cim4.pack(pady=(6,0))
buy4=Button(film4,text="Vásárlás", bootstyle="warning", command=lambda: mehesz_foglal_ablak())
buy4.pack(pady=6,padx=15,)

root.mainloop()