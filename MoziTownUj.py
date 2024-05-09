from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from ttkbootstrap import *
from tkinter import PhotoImage
import datetime as dt
from time import strftime
import sqlite3
from fpdf import *
import unicodedata
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random

def unicode_normalize(s):
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore')

global img1, img2, img3, img4, img5, img6, img7, img8, email

date = dt.datetime.now()

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
            FOREIGN KEY (vetites_id) REFERENCES vetites(id) );"""
        cur.execute(jegytable)
        add_film(dunenev, dunehossz, dunedate, dunedesc)
        add_film(mostnev, mosthossz, mostdate, mostdesc)
        add_film(imadlaknev, imadlakhossz, imadlakdate, imadlakdesc)
        add_film(kingnev, kinghossz, kingdate, kingdesc)
        add_film(mehesznev, meheszhossz, meheszdate, meheszdesc)
        add_film(pandanev, pandahossz, pandadate, pandadesc)
        add_film(szellemirtoknev, szellemirtokhossz, szellemirtokdate, szellemirtokdesc)
        add_vetites(vetites1film, vetites1ido, vetites1ar)
        add_vetites(vetites2film, vetites2ido, vetites2ar)
        add_vetites(vetites3film, vetites3ido, vetites3ar)
        add_vetites(vetites4film, vetites4ido, vetites4ar)


def add_film(nev: str, hossz: int, date: str, description: str):
    command = f"""INSERT INTO film VALUES (NULL,'{nev}','{hossz}','{date}','{description}')"""
    cur.execute(command)
    con.commit()

def add_vetites(film_id: int, ido: str, jegyar: int):
    command = f"""INSERT INTO vetites VALUES (NULL,'{film_id}','{ido}','{jegyar}')"""
    cur.execute(command)
    con.commit()

def add_jegy(vetites_id: int, nev: str):
    command = f"""INSERT INTO jegy VALUES (NULL,'{vetites_id}', '{nev}')"""
    cur.execute(command)
    con.commit()

def send_email(to_email):
        email_address = "mozitown@gmail.com"
        email_password = "moziTown2000"
        subject = "Sikeres vásárlás"
        body = "Köszönjük a vásárlást!"
        msg = MIMEMultipart()
        msg["From"] = email_address
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(email_address, email_password)
            text = msg.as_string()
            server.sendmail(email_address, to_email, text)
            server.quit()
            messagebox.showinfo("Sikeres vásárlás", "Az e-mail elküldve.")
        except Exception as e:
            messagebox.showerror("Hiba", f"Hiba történt az e-mail küldése közben: {str(e)}")

def pdf_dune():
    title = "Foglalás"
    email = "11c-koban@ipari.vein.hu"
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
            self.multi_cell(0, 10, "Vásárló E-mail címe: " + email + " \nFilm neve: DUNE - MÁSODIK RÉSZ\nFilm hossza: 166 perc\nIdopont: Valamikor\nTerem száma: " + terem +"\nSzékek száma: Sok")
            self.image("dune.png", 130, 75, 70, 100)
            self.ln(40)
            self.set_font("Helvetica", "BU", 15)
            self.cell(0, 5, "Elérhetoségek:")
            self.ln(10)
            self.set_font("Times", "", 13)
            self.multi_cell(0, 10, "Telefonszám: +36208793145\nE-mail cím: mozitown@gmail.com")
            self.ln(10)
            self.set_font("Helvetica", "B", 13)
            self.multi_cell(0, 5, "A jegy módosítására vagy törlésére lehetoséget ajánlunk a jegy megvásárlását követo harmadik napig. Ha a kiválasztott jegy korábbra szól, mint három nap, visszaváltásra csak mozinkban van lehetoség, a film kezdete elott legalább 3 órával.")
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
    send_email(email)

def pdf_most():
    title = "Foglalás"
    email = "11c-koban@ipari.vein.hu"
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
            self.multi_cell(0, 10, "Vásárló E-mail címe: " + email +" \nFilm neve: MOST VAGY SOHA!\nFilm hossza: 135 perc\nIdopont: Valamikor\nTerem száma: " + terem +"\nSzékek száma: Sok")
            self.image("most.png", 130, 75, 70, 100)
            self.ln(40)
            self.set_font("Helvetica", "BU", 15)
            self.cell(0, 5, "Elérhetoségek:")
            self.ln(10)
            self.set_font("Times", "", 13)
            self.multi_cell(0, 10, "Telefonszám: +36208793145\nE-mail cím: mozitown@gmail.com")
            self.ln(10)
            self.set_font("Helvetica", "B", 13)
            self.multi_cell(0, 5, "A jegy módosítására vagy törlésére lehetoséget ajánlunk a jegy megvásárlását követo harmadik napig. Ha a kiválasztott jegy korábbra szól, mint három nap, visszaváltásra csak mozinkban van lehetoség, a film kezdete elott legalább 3 órával.")
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
    email = "11c-koban@ipari.vein.hu"
    if email:
        send_email(email)
    else:
        messagebox.showerror("Hiba", "Kérlek add meg az e-mail címed!")

def pdf_imadlak():
    title = "Foglalás"
    email = "11c-koban@ipari.vein.hu"
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
            self.multi_cell(0, 10, "Vásárló E-mail címe: " + email +" \nFilm neve: IMÁDLAK UTÁLNI\nFilm hossza: 100 perc\nIdopont: Valamikor\nTerem száma:" + terem + "\nSzékek száma: Sok")
            self.image("imadlak.png", 130, 75, 70, 100)
            self.ln(40)
            self.set_font("Helvetica", "BU", 15)
            self.cell(0, 5, "Elérhetoségek:")
            self.ln(10)
            self.set_font("Times", "", 13)
            self.multi_cell(0, 10, "Telefonszám: +36208793145\nE-mail cím: mozitown@gmail.com")
            self.ln(10)
            self.set_font("Helvetica", "B", 13)
            self.multi_cell(0, 5, "A jegy módosítására vagy törlésére lehetoséget ajánlunk a jegy megvásárlását követo harmadik napig. Ha a kiválasztott jegy korábbra szól, mint három nap, visszaváltásra csak mozinkban van lehetoség, a film kezdete elott legalább 3 órával.")
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
    email = "11c-koban@ipari.vein.hu"
    if email:
        send_email(email)
    else:
        messagebox.showerror("Hiba", "Kérlek add meg az e-mail címed!")

def pdf_mehesz():
    title = "Foglalás"
    email = "11c-koban@ipari.vein.hu"
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
            self.multi_cell(0, 10, "Vásárló E-mail címe: " + email +" \nFilm neve: A MÉHÉSZ\nFilm hossza: 105 perc\nIdopont: Valamikor\nTerem száma: " + terem +"\nSzékek száma: Sok")
            self.image("mehesz.png", 130, 75, 70, 100)
            self.ln(40)
            self.set_font("Helvetica", "BU", 15)
            self.cell(0, 5, "Elérhetoségek:")
            self.ln(10)
            self.set_font("Times", "", 13)
            self.multi_cell(0, 10, "Telefonszám: +36208793145\nE-mail cím: mozitown@gmail.com")
            self.ln(10)
            self.set_font("Helvetica", "B", 13)
            self.multi_cell(0, 5, "A jegy módosítására vagy törlésére lehetoséget ajánlunk a jegy megvásárlását követo harmadik napig. Ha a kiválasztott jegy korábbra szól, mint három nap, visszaváltásra csak mozinkban van lehetoség, a film kezdete elott legalább 3 órával.")
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
    email = "11c-koban@ipari.vein.hu"
    if email:
        send_email(email)
    else:
        messagebox.showerror("Hiba", "Kérlek add meg az e-mail címed!")

def pdf_king():
    title = "Foglalás"
    email = "11c-koban@ipari.vein.hu"
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
            self.multi_cell(0, 10, "Vásárló E-mail címe: " + email +" \nFilm neve: ARTÚR, A KIRÁLY\nFilm hossza: 107 perc\nIdopont: Valamikor\nTerem száma: " + terem +"\nSzékek száma: Sok")
            self.image("king.png", 130, 75, 70, 100)
            self.ln(40)
            self.set_font("Helvetica", "BU", 15)
            self.cell(0, 5, "Elérhetoségek:")
            self.ln(10)
            self.set_font("Times", "", 13)
            self.multi_cell(0, 10, "Telefonszám: +36208793145\nE-mail cím: mozitown@gmail.com")
            self.ln(10)
            self.set_font("Helvetica", "B", 13)
            self.multi_cell(0, 5, "A jegy módosítására vagy törlésére lehetoséget ajánlunk a jegy megvásárlását követo harmadik napig. Ha a kiválasztott jegy korábbra szól, mint három nap, visszaváltásra csak mozinkban van lehetoség, a film kezdete elott legalább 3 órával.")
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
    email = "11c-koban@ipari.vein.hu"
    if email:
        send_email(email)
    else:
        messagebox.showerror("Hiba", "Kérlek add meg az e-mail címed!")

def pdf_godzilla():
    title = "Foglalás"
    email = "11c-koban@ipari.vein.hu"
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
            self.multi_cell(0, 10, "Vásárló E-mail címe: " + email +" \nFilm neve: GODZILLA X KONG: AZ ÚJ BIRODALOM\nFilm hossza: 115 perc\nIdopont: Valamikor\nTerem száma: " + terem +"\nSzékek száma: Sok")
            self.image("godzilla.png", 130, 75, 70, 100)
            self.ln(40)
            self.set_font("Helvetica", "BU", 15)
            self.cell(0, 5, "Elérhetoségek:")
            self.ln(10)
            self.set_font("Times", "", 13)
            self.multi_cell(0, 10, "Telefonszám: +36208793145\nE-mail cím: mozitown@gmail.com")
            self.ln(10)
            self.set_font("Helvetica", "B", 13)
            self.multi_cell(0, 5, "A jegy módosítására vagy törlésére lehetoséget ajánlunk a jegy megvásárlását követo harmadik napig. Ha a kiválasztott jegy korábbra szól, mint három nap, visszaváltásra csak mozinkban van lehetoség, a film kezdete elott legalább 3 órával.")
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
    email = "11c-koban@ipari.vein.hu"
    if email:
        send_email(email)
    else:
        messagebox.showerror("Hiba", "Kérlek add meg az e-mail címed!")

def pdf_panda():
    title = "Foglalás"
    email = "11c-koban@ipari.vein.hu"
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
            self.multi_cell(0, 10, "Vásárló E-mail címe: " + email +" \nFilm neve: KUNG FU PANDA 4\nFilm hossza: 94 perc\nIdopont: Valamikor\nTerem száma: " + terem + "\nSzékek száma: Sok")
            self.image("panda.png", 130, 75, 70, 100)
            self.ln(40)
            self.set_font("Helvetica", "BU", 15)
            self.cell(0, 5, "Elérhetoségek:")
            self.ln(10)
            self.set_font("Times", "", 13)
            self.multi_cell(0, 10, "Telefonszám: +36208793145\nE-mail cím: mozitown@gmail.com")
            self.ln(10)
            self.set_font("Helvetica", "B", 13)
            self.multi_cell(0, 5, "A jegy módosítására vagy törlésére lehetoséget ajánlunk a jegy megvásárlását követo harmadik napig. Ha a kiválasztott jegy korábbra szól, mint három nap, visszaváltásra csak mozinkban van lehetoség, a film kezdete elott legalább 3 órával.")
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
    email = "11c-koban@ipari.vein.hu"
    if email:
        send_email(email)
    else:
        messagebox.showerror("Hiba", "Kérlek add meg az e-mail címed!")

def pdf_szellemirtok():
    title = "Foglalás"
    email = "11c-koban@ipari.vein.hu"
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
            self.multi_cell(0, 10, "Vásárló E-mail címe: " + email +" \nFilm neve: SZELLEMIRTÓK - A BORZONGÁS BIRODALMA\nFilm hossza: 125 perc\nIdopont: Valamikor\nTerem száma: " + terem + "\nSzékek száma: Sok")
            self.image("szellemirtok.png", 130, 75, 70, 100)
            self.ln(40)
            self.set_font("Helvetica", "BU", 15)
            self.cell(0, 5, "Elérhetoségek:")
            self.ln(10)
            self.set_font("Times", "", 13)
            self.multi_cell(0, 10, "Telefonszám: +36208793145\nE-mail cím: mozitown@gmail.com")
            self.ln(10)
            self.set_font("Helvetica", "B", 13)
            self.multi_cell(0, 5, "A jegy módosítására vagy törlésére lehetoséget ajánlunk a jegy megvásárlását követo harmadik napig. Ha a kiválasztott jegy korábbra szól, mint három nap, visszaváltásra csak mozinkban van lehetoség, a film kezdete elott legalább 3 órával.")
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
    email = "11c-koban@ipari.vein.hu"
    if email:
        send_email(email)
    else:
        messagebox.showerror("Hiba", "Kérlek add meg az e-mail címed!")

def dune_foglal_ablak():
    fog_ablak = Toplevel(root)
    fog_ablak.geometry("1000x700")
    fog_ablak.title("DŰNE - MÁSODIK RÉSZ: Foglalás")

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

    fkeret = LabelFrame(fog_ablak, padding=10)
    fkeret.grid(row=1, column=1)
    fleiras = Label(fkeret, text="A távoli jövőben, a bolygóközi királyságok korában játszódó történetben két nagyhatalmú uralkodóház harcol az Arrakis bolygó feletti hatalomért, mert az ismert univerzumban egyedül az itteni végtelen sivatagban bányászható az a fűszer, amely lehetővé teszi a csillagközi utazást. A Harkonnenek ura kiirtatta az Atreides családot. De Paul Atreides herceg (Timothée Chalamet) megmenekült: a pusztaságban bujkál egy titokzatos, nomád nép, a fremenek között, ahol megismerkedik egy lánnyal, Csanival (Zendaya). Az a sorsa, hogy bosszút álljon a családjáért, háborúba vezesse a hozzá hű seregeket. Döntenie kell, hogy élete nagy szerelmét választja-e, vagy beteljesíti a végzetét. Az univerzum sorsa múlik azon, hogy mit határoz: és végül olyan útra lép, amely megváltoztathatja azt a szörnyű jövőt, amelyet egyedül ő lát előre.", font=("Times", 12, "bold"), width=50, justify="left", wraplength=400)
    fleiras.grid(row=0, column=0, columnspan=10)
    szek1 = Button(fkeret, state=NORMAL, text="01")
    szek1.grid(row=1, column=0, pady=10)
    szek2 = Button(fkeret, state=NORMAL, text="02")
    szek2.grid(row=1, column=1)
    szek3 = Button(fkeret, state=NORMAL, text="03")
    szek3.grid(row=1, column=2)
    szek4 = Button(fkeret, state=NORMAL, text="04")
    szek4.grid(row=1, column=3)
    szek5 = Label(fkeret, width=0)
    szek5.grid(row=1, column=4)
    szek6 = Label(fkeret, width=0)
    szek6.grid(row=1, column=5)
    szek7 = Button(fkeret, state=NORMAL, text="05")
    szek7.grid(row=1, column=6)
    szek8 = Button(fkeret, state=NORMAL, text="06")
    szek8.grid(row=1, column=7)
    szek9 = Button(fkeret, state=NORMAL, text="07")
    szek9.grid(row=1, column=8)
    szek10 = Button(fkeret, state=NORMAL, text="08")
    szek10.grid(row=1, column=9)
    szek11 = Button(fkeret, state=NORMAL, text="09")
    szek11.grid(row=2, column=0, pady=10)
    szek12 = Button(fkeret, state=NORMAL, text="10")
    szek12.grid(row=2, column=1)
    szek13 = Button(fkeret, state=NORMAL, text="11")
    szek13.grid(row=2, column=2)
    szek14 = Button(fkeret, state=NORMAL, text="12")
    szek14.grid(row=2, column=3)
    szek15 = Label(fkeret, width=0)
    szek15.grid(row=2, column=4)
    szek16 = Label(fkeret, width=0)
    szek16.grid(row=2, column=5)
    szek17 = Button(fkeret, state=NORMAL, text="13")
    szek17.grid(row=2, column=6)
    szek18 = Button(fkeret, state=NORMAL, text="14")
    szek18.grid(row=2, column=7)
    szek19 = Button(fkeret, state=NORMAL, text="15")
    szek19.grid(row=2, column=8)
    szek20 = Button(fkeret, state=NORMAL, text="16")
    szek20.grid(row=2, column=9)
    szek21 = Button(fkeret, state=NORMAL, text="17")
    szek21.grid(row=3, column=0, pady=10)
    szek22 = Button(fkeret, state=NORMAL, text="18")
    szek22.grid(row=3, column=1)
    szek23 = Button(fkeret, state=NORMAL, text="19")
    szek23.grid(row=3, column=2)
    szek24 = Button(fkeret, state=NORMAL, text="20")
    szek24.grid(row=3, column=3)
    szek25 = Label(fkeret, width=0)
    szek25.grid(row=3, column=4)
    szek26 = Label(fkeret, width=0)
    szek26.grid(row=3, column=5)
    szek27 = Button(fkeret, state=NORMAL, text="21")
    szek27.grid(row=3, column=6)
    szek28 = Button(fkeret, state=NORMAL, text="22")
    szek28.grid(row=3, column=7)
    szek29 = Button(fkeret, state=NORMAL, text="23")
    szek29.grid(row=3, column=8)
    szek30 = Button(fkeret, state=NORMAL, text="24")
    szek30.grid(row=3, column=9)
    szek31 = Button(fkeret, state=NORMAL, text="25")
    szek31.grid(row=4, column=0, pady=10)
    szek32 = Button(fkeret, state=NORMAL, text="26")
    szek32.grid(row=4, column=1)
    szek33 = Button(fkeret, state=NORMAL, text="27")
    szek33.grid(row=4, column=2)
    szek34 = Button(fkeret, state=NORMAL, text="28")
    szek34.grid(row=4, column=3)
    szek35 = Label(fkeret, width=0)
    szek35.grid(row=4, column=4)
    szek36 = Label(fkeret, width=0)
    szek36.grid(row=4, column=5)
    szek37 = Button(fkeret, state=NORMAL, text="29")
    szek37.grid(row=4, column=6)
    szek38 = Button(fkeret, state=NORMAL, text="30")
    szek38.grid(row=4, column=7)
    szek39 = Button(fkeret, state=NORMAL, text="31")
    szek39.grid(row=4, column=8)
    szek40 = Button(fkeret, state=NORMAL, text="32")
    szek40.grid(row=4, column=9)
    szek41 = Button(fkeret, state=NORMAL, text="33")
    szek41.grid(row=5, column=0, pady=10)
    szek42 = Button(fkeret, state=NORMAL, text="34")
    szek42.grid(row=5, column=1)
    szek43 = Button(fkeret, state=NORMAL, text="35")
    szek43.grid(row=5, column=2)
    szek44 = Button(fkeret, state=NORMAL, text="36")
    szek44.grid(row=5, column=3)
    szek45 = Button(fkeret, state=NORMAL, text="37")
    szek45.grid(row=5, column=4)
    szek46 = Button(fkeret, state=NORMAL, text="38")
    szek46.grid(row=5, column=5)
    szek47 = Button(fkeret, state=NORMAL, text="39")
    szek47.grid(row=5, column=6)
    szek48 = Button(fkeret, state=NORMAL, text="40")
    szek48.grid(row=5, column=7)
    szek49 = Button(fkeret, state=NORMAL, text="41")
    szek49.grid(row=5, column=8)
    szek50 = Button(fkeret, state=NORMAL, text="42")
    szek50.grid(row=5, column=9)
    ffoglal = Button(fkeret, text="Helyet foglalok", bootstyle="info", command= lambda:pdf_dune())
    ffoglal.grid(row=6, column=0, columnspan=10, pady=10)

def most_foglal_ablak():
    fog_ablak = Toplevel(root)
    fog_ablak.geometry("1000x700")
    fog_ablak.title("MOST VAGY SOHA!: Foglalás")

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

    fkeret = LabelFrame(fog_ablak, padding=10)
    fkeret.grid(row=1, column=1)
    fleiras = Label(fkeret, text="Amikor 1848. március 15-én a lánglelkű költő, Petőfi Sándor költeményével, a Nemzeti Dallal kirobbantja a magyar forradalmat, az osztrák elnyomók egy titkosügynököt bíznak meg a feladattal, hogy állítsa meg a felkelést.", font=("Times", 12, "bold"), width=50, justify="left", wraplength=400)
    fleiras.grid(row=0, column=0, columnspan=10)
    szek1 = Button(fkeret, state=NORMAL, text="01")
    szek1.grid(row=1, column=0, pady=10)
    szek2 = Button(fkeret, state=NORMAL, text="02")
    szek2.grid(row=1, column=1)
    szek3 = Button(fkeret, state=NORMAL, text="03")
    szek3.grid(row=1, column=2)
    szek4 = Button(fkeret, state=NORMAL, text="04")
    szek4.grid(row=1, column=3)
    szek5 = Label(fkeret, width=0)
    szek5.grid(row=1, column=4)
    szek6 = Label(fkeret, width=0)
    szek6.grid(row=1, column=5)
    szek7 = Button(fkeret, state=NORMAL, text="05")
    szek7.grid(row=1, column=6)
    szek8 = Button(fkeret, state=NORMAL, text="06")
    szek8.grid(row=1, column=7)
    szek9 = Button(fkeret, state=NORMAL, text="07")
    szek9.grid(row=1, column=8)
    szek10 = Button(fkeret, state=NORMAL, text="08")
    szek10.grid(row=1, column=9)
    szek11 = Button(fkeret, state=NORMAL, text="09")
    szek11.grid(row=2, column=0, pady=10)
    szek12 = Button(fkeret, state=NORMAL, text="10")
    szek12.grid(row=2, column=1)
    szek13 = Button(fkeret, state=NORMAL, text="11")
    szek13.grid(row=2, column=2)
    szek14 = Button(fkeret, state=NORMAL, text="12")
    szek14.grid(row=2, column=3)
    szek15 = Label(fkeret, width=0)
    szek15.grid(row=2, column=4)
    szek16 = Label(fkeret, width=0)
    szek16.grid(row=2, column=5)
    szek17 = Button(fkeret, state=NORMAL, text="13")
    szek17.grid(row=2, column=6)
    szek18 = Button(fkeret, state=NORMAL, text="14")
    szek18.grid(row=2, column=7)
    szek19 = Button(fkeret, state=NORMAL, text="15")
    szek19.grid(row=2, column=8)
    szek20 = Button(fkeret, state=NORMAL, text="16")
    szek20.grid(row=2, column=9)
    szek21 = Button(fkeret, state=NORMAL, text="17")
    szek21.grid(row=3, column=0, pady=10)
    szek22 = Button(fkeret, state=NORMAL, text="18")
    szek22.grid(row=3, column=1)
    szek23 = Button(fkeret, state=NORMAL, text="19")
    szek23.grid(row=3, column=2)
    szek24 = Button(fkeret, state=NORMAL, text="20")
    szek24.grid(row=3, column=3)
    szek25 = Label(fkeret, width=0)
    szek25.grid(row=3, column=4)
    szek26 = Label(fkeret, width=0)
    szek26.grid(row=3, column=5)
    szek27 = Button(fkeret, state=NORMAL, text="21")
    szek27.grid(row=3, column=6)
    szek28 = Button(fkeret, state=NORMAL, text="22")
    szek28.grid(row=3, column=7)
    szek29 = Button(fkeret, state=NORMAL, text="23")
    szek29.grid(row=3, column=8)
    szek30 = Button(fkeret, state=NORMAL, text="24")
    szek30.grid(row=3, column=9)
    szek31 = Button(fkeret, state=NORMAL, text="25")
    szek31.grid(row=4, column=0, pady=10)
    szek32 = Button(fkeret, state=NORMAL, text="26")
    szek32.grid(row=4, column=1)
    szek33 = Button(fkeret, state=NORMAL, text="27")
    szek33.grid(row=4, column=2)
    szek34 = Button(fkeret, state=NORMAL, text="28")
    szek34.grid(row=4, column=3)
    szek35 = Label(fkeret, width=0)
    szek35.grid(row=4, column=4)
    szek36 = Label(fkeret, width=0)
    szek36.grid(row=4, column=5)
    szek37 = Button(fkeret, state=NORMAL, text="29")
    szek37.grid(row=4, column=6)
    szek38 = Button(fkeret, state=NORMAL, text="30")
    szek38.grid(row=4, column=7)
    szek39 = Button(fkeret, state=NORMAL, text="31")
    szek39.grid(row=4, column=8)
    szek40 = Button(fkeret, state=NORMAL, text="32")
    szek40.grid(row=4, column=9)
    szek41 = Button(fkeret, state=NORMAL, text="33")
    szek41.grid(row=5, column=0, pady=10)
    szek42 = Button(fkeret, state=NORMAL, text="34")
    szek42.grid(row=5, column=1)
    szek43 = Button(fkeret, state=NORMAL, text="35")
    szek43.grid(row=5, column=2)
    szek44 = Button(fkeret, state=NORMAL, text="36")
    szek44.grid(row=5, column=3)
    szek45 = Button(fkeret, state=NORMAL, text="37")
    szek45.grid(row=5, column=4)
    szek46 = Button(fkeret, state=NORMAL, text="38")
    szek46.grid(row=5, column=5)
    szek47 = Button(fkeret, state=NORMAL, text="39")
    szek47.grid(row=5, column=6)
    szek48 = Button(fkeret, state=NORMAL, text="40")
    szek48.grid(row=5, column=7)
    szek49 = Button(fkeret, state=NORMAL, text="41")
    szek49.grid(row=5, column=8)
    szek50 = Button(fkeret, state=NORMAL, text="42")
    szek50.grid(row=5, column=9)
    ffoglal = Button(fkeret, text="Helyet foglalok", bootstyle="info", command= lambda:pdf_most())
    ffoglal.grid(row=6, column=0, columnspan=10, pady=10)

def imadlak_foglal_ablak():
    fog_ablak = Toplevel(root)
    fog_ablak.geometry("1000x700")
    fog_ablak.title("IMÁDLAK UTÁLNI: Foglalás")

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

    fkeret = LabelFrame(fog_ablak, padding=10)
    fkeret.grid(row=1, column=1)
    fleiras = Label(fkeret, text="Találkoztak, együtt töltöttek egy éjszakát, és azóta gyűlölik egymást. Van ilyen. Bea (Sydney Sweeney) és Ben (Glen Powell) biztos, hogy nem illenek össze. Ha néha véletlenül összefutnak valahol, tutira elszabadul a pokol: csak bántani tudják egymást. De lesz egy esküvő Ausztráliában, amin mindkettejüknek részt kell venniük. Nincs kibúvó, nincs duma: utazniuk kell. Néhány napon, néhány bulin, néhány vacsorán keresztül el kell viselniük egymás közelségét, miközben egy gyönyörű tengerparti házban ott kavarog körülöttük egy csomó régi szerelmük, néhány kíváncsi rokonuk és kavarni mindig kész felmenőjük. Szóval, azt teszik, amit két érett, felnőtt, felelősségteljes ember ilyenkor tehet: úgy tesznek, mintha szerelmespár lennének - azt remélik, hogy így mindenkinek könnyebb lesz. Nem is tévedhettek volna nagyobbat.", font=("Times", 12, "bold"), width=50, justify="left", wraplength=400)
    fleiras.grid(row=0, column=0, columnspan=10)
    szek1 = Button(fkeret, state=NORMAL, text="01")
    szek1.grid(row=1, column=0, pady=10)
    szek2 = Button(fkeret, state=NORMAL, text="02")
    szek2.grid(row=1, column=1)
    szek3 = Button(fkeret, state=NORMAL, text="03")
    szek3.grid(row=1, column=2)
    szek4 = Button(fkeret, state=NORMAL, text="04")
    szek4.grid(row=1, column=3)
    szek5 = Label(fkeret, width=0)
    szek5.grid(row=1, column=4)
    szek6 = Label(fkeret, width=0)
    szek6.grid(row=1, column=5)
    szek7 = Button(fkeret, state=NORMAL, text="05")
    szek7.grid(row=1, column=6)
    szek8 = Button(fkeret, state=NORMAL, text="06")
    szek8.grid(row=1, column=7)
    szek9 = Button(fkeret, state=NORMAL, text="07")
    szek9.grid(row=1, column=8)
    szek10 = Button(fkeret, state=NORMAL, text="08")
    szek10.grid(row=1, column=9)
    szek11 = Button(fkeret, state=NORMAL, text="09")
    szek11.grid(row=2, column=0, pady=10)
    szek12 = Button(fkeret, state=NORMAL, text="10")
    szek12.grid(row=2, column=1)
    szek13 = Button(fkeret, state=NORMAL, text="11")
    szek13.grid(row=2, column=2)
    szek14 = Button(fkeret, state=NORMAL, text="12")
    szek14.grid(row=2, column=3)
    szek15 = Label(fkeret, width=0)
    szek15.grid(row=2, column=4)
    szek16 = Label(fkeret, width=0)
    szek16.grid(row=2, column=5)
    szek17 = Button(fkeret, state=NORMAL, text="13")
    szek17.grid(row=2, column=6)
    szek18 = Button(fkeret, state=NORMAL, text="14")
    szek18.grid(row=2, column=7)
    szek19 = Button(fkeret, state=NORMAL, text="15")
    szek19.grid(row=2, column=8)
    szek20 = Button(fkeret, state=NORMAL, text="16")
    szek20.grid(row=2, column=9)
    szek21 = Button(fkeret, state=NORMAL, text="17")
    szek21.grid(row=3, column=0, pady=10)
    szek22 = Button(fkeret, state=NORMAL, text="18")
    szek22.grid(row=3, column=1)
    szek23 = Button(fkeret, state=NORMAL, text="19")
    szek23.grid(row=3, column=2)
    szek24 = Button(fkeret, state=NORMAL, text="20")
    szek24.grid(row=3, column=3)
    szek25 = Label(fkeret, width=0)
    szek25.grid(row=3, column=4)
    szek26 = Label(fkeret, width=0)
    szek26.grid(row=3, column=5)
    szek27 = Button(fkeret, state=NORMAL, text="21")
    szek27.grid(row=3, column=6)
    szek28 = Button(fkeret, state=NORMAL, text="22")
    szek28.grid(row=3, column=7)
    szek29 = Button(fkeret, state=NORMAL, text="23")
    szek29.grid(row=3, column=8)
    szek30 = Button(fkeret, state=NORMAL, text="24")
    szek30.grid(row=3, column=9)
    szek31 = Button(fkeret, state=NORMAL, text="25")
    szek31.grid(row=4, column=0, pady=10)
    szek32 = Button(fkeret, state=NORMAL, text="26")
    szek32.grid(row=4, column=1)
    szek33 = Button(fkeret, state=NORMAL, text="27")
    szek33.grid(row=4, column=2)
    szek34 = Button(fkeret, state=NORMAL, text="28")
    szek34.grid(row=4, column=3)
    szek35 = Label(fkeret, width=0)
    szek35.grid(row=4, column=4)
    szek36 = Label(fkeret, width=0)
    szek36.grid(row=4, column=5)
    szek37 = Button(fkeret, state=NORMAL, text="29")
    szek37.grid(row=4, column=6)
    szek38 = Button(fkeret, state=NORMAL, text="30")
    szek38.grid(row=4, column=7)
    szek39 = Button(fkeret, state=NORMAL, text="31")
    szek39.grid(row=4, column=8)
    szek40 = Button(fkeret, state=NORMAL, text="32")
    szek40.grid(row=4, column=9)
    szek41 = Button(fkeret, state=NORMAL, text="33")
    szek41.grid(row=5, column=0, pady=10)
    szek42 = Button(fkeret, state=NORMAL, text="34")
    szek42.grid(row=5, column=1)
    szek43 = Button(fkeret, state=NORMAL, text="35")
    szek43.grid(row=5, column=2)
    szek44 = Button(fkeret, state=NORMAL, text="36")
    szek44.grid(row=5, column=3)
    szek45 = Button(fkeret, state=NORMAL, text="37")
    szek45.grid(row=5, column=4)
    szek46 = Button(fkeret, state=NORMAL, text="38")
    szek46.grid(row=5, column=5)
    szek47 = Button(fkeret, state=NORMAL, text="39")
    szek47.grid(row=5, column=6)
    szek48 = Button(fkeret, state=NORMAL, text="40")
    szek48.grid(row=5, column=7)
    szek49 = Button(fkeret, state=NORMAL, text="41")
    szek49.grid(row=5, column=8)
    szek50 = Button(fkeret, state=NORMAL, text="42")
    szek50.grid(row=5, column=9)
    ffoglal = Button(fkeret, text="Helyet foglalok", bootstyle="info", command= lambda:pdf_imadlak())
    ffoglal.grid(row=6, column=0, columnspan=10, pady=10)

def mehesz_foglal_ablak():
    fog_ablak = Toplevel(root)
    fog_ablak.geometry("1000x700")
    fog_ablak.title("A MÉHÉSZ: Foglalás")

    fcimkeret = LabelFrame(fog_ablak, border=0, padding=0, borderwidth=0)
    fcimkeret.grid(row=0, column=0, columnspan=2)
    Label.columnconfigure(fcimkeret, 1, weight=1)
    fcim = Label(fcimkeret, text="A MÉHÉSZ", font=("Terminal", 20, "bold"), justify="center", anchor="center", width=90)
    fcim.grid(row=0, column=0, pady=5, sticky="nesw")

    fkepkeret = LabelFrame(fog_ablak, height=370, border=0, padding=0, borderwidth=0)
    fkepkeret.grid(row=1, column=0, padx=50, pady=100)
    dune_al = Canvas(fkepkeret, width=250, height=370, bg='white')
    dune_al.grid(row=0, column=0)
    dune_al.create_image(0, 0, anchor=NW, image=img4)

    fkeret = LabelFrame(fog_ablak, padding=10)
    fkeret.grid(row=1, column=1)
    fleiras = Label(fkeret, text="Egy férfi egyszemélyes, brutális bosszúhadjáratának tétje országos szintűre nő, miután kiderül róla, hogy korábban a Méhészek néven ismert befolyásos és titkos szervezet ügynöke volt.", font=("Times", 12, "bold"), width=50, justify="left", wraplength=400)
    fleiras.grid(row=0, column=0, columnspan=10)
    szek1 = Button(fkeret, state=NORMAL, text="01")
    szek1.grid(row=1, column=0, pady=10)
    szek2 = Button(fkeret, state=NORMAL, text="02")
    szek2.grid(row=1, column=1)
    szek3 = Button(fkeret, state=NORMAL, text="03")
    szek3.grid(row=1, column=2)
    szek4 = Button(fkeret, state=NORMAL, text="04")
    szek4.grid(row=1, column=3)
    szek5 = Label(fkeret, width=0)
    szek5.grid(row=1, column=4)
    szek6 = Label(fkeret, width=0)
    szek6.grid(row=1, column=5)
    szek7 = Button(fkeret, state=NORMAL, text="05")
    szek7.grid(row=1, column=6)
    szek8 = Button(fkeret, state=NORMAL, text="06")
    szek8.grid(row=1, column=7)
    szek9 = Button(fkeret, state=NORMAL, text="07")
    szek9.grid(row=1, column=8)
    szek10 = Button(fkeret, state=NORMAL, text="08")
    szek10.grid(row=1, column=9)
    szek11 = Button(fkeret, state=NORMAL, text="09")
    szek11.grid(row=2, column=0, pady=10)
    szek12 = Button(fkeret, state=NORMAL, text="10")
    szek12.grid(row=2, column=1)
    szek13 = Button(fkeret, state=NORMAL, text="11")
    szek13.grid(row=2, column=2)
    szek14 = Button(fkeret, state=NORMAL, text="12")
    szek14.grid(row=2, column=3)
    szek15 = Label(fkeret, width=0)
    szek15.grid(row=2, column=4)
    szek16 = Label(fkeret, width=0)
    szek16.grid(row=2, column=5)
    szek17 = Button(fkeret, state=NORMAL, text="13")
    szek17.grid(row=2, column=6)
    szek18 = Button(fkeret, state=NORMAL, text="14")
    szek18.grid(row=2, column=7)
    szek19 = Button(fkeret, state=NORMAL, text="15")
    szek19.grid(row=2, column=8)
    szek20 = Button(fkeret, state=NORMAL, text="16")
    szek20.grid(row=2, column=9)
    szek21 = Button(fkeret, state=NORMAL, text="17")
    szek21.grid(row=3, column=0, pady=10)
    szek22 = Button(fkeret, state=NORMAL, text="18")
    szek22.grid(row=3, column=1)
    szek23 = Button(fkeret, state=NORMAL, text="19")
    szek23.grid(row=3, column=2)
    szek24 = Button(fkeret, state=NORMAL, text="20")
    szek24.grid(row=3, column=3)
    szek25 = Label(fkeret, width=0)
    szek25.grid(row=3, column=4)
    szek26 = Label(fkeret, width=0)
    szek26.grid(row=3, column=5)
    szek27 = Button(fkeret, state=NORMAL, text="21")
    szek27.grid(row=3, column=6)
    szek28 = Button(fkeret, state=NORMAL, text="22")
    szek28.grid(row=3, column=7)
    szek29 = Button(fkeret, state=NORMAL, text="23")
    szek29.grid(row=3, column=8)
    szek30 = Button(fkeret, state=NORMAL, text="24")
    szek30.grid(row=3, column=9)
    szek31 = Button(fkeret, state=NORMAL, text="25")
    szek31.grid(row=4, column=0, pady=10)
    szek32 = Button(fkeret, state=NORMAL, text="26")
    szek32.grid(row=4, column=1)
    szek33 = Button(fkeret, state=NORMAL, text="27")
    szek33.grid(row=4, column=2)
    szek34 = Button(fkeret, state=NORMAL, text="28")
    szek34.grid(row=4, column=3)
    szek35 = Label(fkeret, width=0)
    szek35.grid(row=4, column=4)
    szek36 = Label(fkeret, width=0)
    szek36.grid(row=4, column=5)
    szek37 = Button(fkeret, state=NORMAL, text="29")
    szek37.grid(row=4, column=6)
    szek38 = Button(fkeret, state=NORMAL, text="30")
    szek38.grid(row=4, column=7)
    szek39 = Button(fkeret, state=NORMAL, text="31")
    szek39.grid(row=4, column=8)
    szek40 = Button(fkeret, state=NORMAL, text="32")
    szek40.grid(row=4, column=9)
    szek41 = Button(fkeret, state=NORMAL, text="33")
    szek41.grid(row=5, column=0, pady=10)
    szek42 = Button(fkeret, state=NORMAL, text="34")
    szek42.grid(row=5, column=1)
    szek43 = Button(fkeret, state=NORMAL, text="35")
    szek43.grid(row=5, column=2)
    szek44 = Button(fkeret, state=NORMAL, text="36")
    szek44.grid(row=5, column=3)
    szek45 = Button(fkeret, state=NORMAL, text="37")
    szek45.grid(row=5, column=4)
    szek46 = Button(fkeret, state=NORMAL, text="38")
    szek46.grid(row=5, column=5)
    szek47 = Button(fkeret, state=NORMAL, text="39")
    szek47.grid(row=5, column=6)
    szek48 = Button(fkeret, state=NORMAL, text="40")
    szek48.grid(row=5, column=7)
    szek49 = Button(fkeret, state=NORMAL, text="41")
    szek49.grid(row=5, column=8)
    szek50 = Button(fkeret, state=NORMAL, text="42")
    szek50.grid(row=5, column=9)
    ffoglal = Button(fkeret, text="Helyet foglalok", bootstyle="info", command= lambda:pdf_mehesz())
    ffoglal.grid(row=6, column=0, columnspan=10, pady=10)

def king_foglal_ablak():
    fog_ablak = Toplevel(root)
    fog_ablak.geometry("1000x700")
    fog_ablak.title("ARTÚR, A KIRÁLY: Foglalás")

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

    fkeret = LabelFrame(fog_ablak, padding=10)
    fkeret.grid(row=1, column=1)
    fleiras = Label(fkeret, text="Michael Light (Mark Wahlberg) és elszánt csapata a Dominikai Köztársaság dzsungelében teszi próbára magát egy rendkívüli 10 napos, 700 kilométeres extrémsport-világbajnokságon. A kalandvágyó sportember életében ez az utolsó lehetőség, hogy a régen áhított első helyezést elérje, a túra során azonban váratlanul egy ágrólszakadt kóborkutya szegődik melléjük. Michael és a különös, mégis méltóságteljes állat között hamarosan megbonthatatlan barátság szövődik, és a verseny végére Michael számára a győzelem, a hűség és a barátság jelentése merőben új értelmet nyer.", font=("Times", 12, "bold"), width=50, justify="left", wraplength=400)
    fleiras.grid(row=0, column=0, columnspan=10)
    szek1 = Button(fkeret, state=NORMAL, text="01")
    szek1.grid(row=1, column=0, pady=10)
    szek2 = Button(fkeret, state=NORMAL, text="02")
    szek2.grid(row=1, column=1)
    szek3 = Button(fkeret, state=NORMAL, text="03")
    szek3.grid(row=1, column=2)
    szek4 = Button(fkeret, state=NORMAL, text="04")
    szek4.grid(row=1, column=3)
    szek5 = Label(fkeret, width=0)
    szek5.grid(row=1, column=4)
    szek6 = Label(fkeret, width=0)
    szek6.grid(row=1, column=5)
    szek7 = Button(fkeret, state=NORMAL, text="05")
    szek7.grid(row=1, column=6)
    szek8 = Button(fkeret, state=NORMAL, text="06")
    szek8.grid(row=1, column=7)
    szek9 = Button(fkeret, state=NORMAL, text="07")
    szek9.grid(row=1, column=8)
    szek10 = Button(fkeret, state=NORMAL, text="08")
    szek10.grid(row=1, column=9)
    szek11 = Button(fkeret, state=NORMAL, text="09")
    szek11.grid(row=2, column=0, pady=10)
    szek12 = Button(fkeret, state=NORMAL, text="10")
    szek12.grid(row=2, column=1)
    szek13 = Button(fkeret, state=NORMAL, text="11")
    szek13.grid(row=2, column=2)
    szek14 = Button(fkeret, state=NORMAL, text="12")
    szek14.grid(row=2, column=3)
    szek15 = Label(fkeret, width=0)
    szek15.grid(row=2, column=4)
    szek16 = Label(fkeret, width=0)
    szek16.grid(row=2, column=5)
    szek17 = Button(fkeret, state=NORMAL, text="13")
    szek17.grid(row=2, column=6)
    szek18 = Button(fkeret, state=NORMAL, text="14")
    szek18.grid(row=2, column=7)
    szek19 = Button(fkeret, state=NORMAL, text="15")
    szek19.grid(row=2, column=8)
    szek20 = Button(fkeret, state=NORMAL, text="16")
    szek20.grid(row=2, column=9)
    szek21 = Button(fkeret, state=NORMAL, text="17")
    szek21.grid(row=3, column=0, pady=10)
    szek22 = Button(fkeret, state=NORMAL, text="18")
    szek22.grid(row=3, column=1)
    szek23 = Button(fkeret, state=NORMAL, text="19")
    szek23.grid(row=3, column=2)
    szek24 = Button(fkeret, state=NORMAL, text="20")
    szek24.grid(row=3, column=3)
    szek25 = Label(fkeret, width=0)
    szek25.grid(row=3, column=4)
    szek26 = Label(fkeret, width=0)
    szek26.grid(row=3, column=5)
    szek27 = Button(fkeret, state=NORMAL, text="21")
    szek27.grid(row=3, column=6)
    szek28 = Button(fkeret, state=NORMAL, text="22")
    szek28.grid(row=3, column=7)
    szek29 = Button(fkeret, state=NORMAL, text="23")
    szek29.grid(row=3, column=8)
    szek30 = Button(fkeret, state=NORMAL, text="24")
    szek30.grid(row=3, column=9)
    szek31 = Button(fkeret, state=NORMAL, text="25")
    szek31.grid(row=4, column=0, pady=10)
    szek32 = Button(fkeret, state=NORMAL, text="26")
    szek32.grid(row=4, column=1)
    szek33 = Button(fkeret, state=NORMAL, text="27")
    szek33.grid(row=4, column=2)
    szek34 = Button(fkeret, state=NORMAL, text="28")
    szek34.grid(row=4, column=3)
    szek35 = Label(fkeret, width=0)
    szek35.grid(row=4, column=4)
    szek36 = Label(fkeret, width=0)
    szek36.grid(row=4, column=5)
    szek37 = Button(fkeret, state=NORMAL, text="29")
    szek37.grid(row=4, column=6)
    szek38 = Button(fkeret, state=NORMAL, text="30")
    szek38.grid(row=4, column=7)
    szek39 = Button(fkeret, state=NORMAL, text="31")
    szek39.grid(row=4, column=8)
    szek40 = Button(fkeret, state=NORMAL, text="32")
    szek40.grid(row=4, column=9)
    szek41 = Button(fkeret, state=NORMAL, text="33")
    szek41.grid(row=5, column=0, pady=10)
    szek42 = Button(fkeret, state=NORMAL, text="34")
    szek42.grid(row=5, column=1)
    szek43 = Button(fkeret, state=NORMAL, text="35")
    szek43.grid(row=5, column=2)
    szek44 = Button(fkeret, state=NORMAL, text="36")
    szek44.grid(row=5, column=3)
    szek45 = Button(fkeret, state=NORMAL, text="37")
    szek45.grid(row=5, column=4)
    szek46 = Button(fkeret, state=NORMAL, text="38")
    szek46.grid(row=5, column=5)
    szek47 = Button(fkeret, state=NORMAL, text="39")
    szek47.grid(row=5, column=6)
    szek48 = Button(fkeret, state=NORMAL, text="40")
    szek48.grid(row=5, column=7)
    szek49 = Button(fkeret, state=NORMAL, text="41")
    szek49.grid(row=5, column=8)
    szek50 = Button(fkeret, state=NORMAL, text="42")
    szek50.grid(row=5, column=9)
    ffoglal = Button(fkeret, text="Helyet foglalok", bootstyle="info", command= lambda:pdf_king())
    ffoglal.grid(row=6, column=0, columnspan=10, pady=10)

def godzilla_foglal_ablak():
    fog_ablak = Toplevel(root)
    fog_ablak.geometry("1000x700")
    fog_ablak.title("GODZILLA X KONG: AZ ÚJ BIRODALOM: Foglalás")

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

    fkeret = LabelFrame(fog_ablak, padding=10)
    fkeret.grid(row=1, column=1)
    fleiras = Label(fkeret, text="A mindent eldöntő, minden eddiginél nagyobb háború nem ért véget azzal, hogy Kong és Godzilla szembetalálkozott és összemérte az erejét. Mert az ember most már kénytelen belenyugodni, hogy nem ő a legerősebb a földön. És nem ismeri igazán a saját világát: várja még néhány eddig rejtve maradt meglepetés. Bujkál még valami a föld alatt, ami felébredt, és pusztítani akar. Az emberiség képtelen megállítani. Talán Kong is képtelen volna. És Godzilla is. De ha ők ketten összefognának, akkor esetleg megmenekülhetnének ők is és mi is…", font=("Times", 12, "bold"), width=50, justify="left", wraplength=400)
    fleiras.grid(row=0, column=0, columnspan=10)
    szek1 = Button(fkeret, state=NORMAL, text="01")
    szek1.grid(row=1, column=0, pady=10)
    szek2 = Button(fkeret, state=NORMAL, text="02")
    szek2.grid(row=1, column=1)
    szek3 = Button(fkeret, state=NORMAL, text="03")
    szek3.grid(row=1, column=2)
    szek4 = Button(fkeret, state=NORMAL, text="04")
    szek4.grid(row=1, column=3)
    szek5 = Label(fkeret, width=0)
    szek5.grid(row=1, column=4)
    szek6 = Label(fkeret, width=0)
    szek6.grid(row=1, column=5)
    szek7 = Button(fkeret, state=NORMAL, text="05")
    szek7.grid(row=1, column=6)
    szek8 = Button(fkeret, state=NORMAL, text="06")
    szek8.grid(row=1, column=7)
    szek9 = Button(fkeret, state=NORMAL, text="07")
    szek9.grid(row=1, column=8)
    szek10 = Button(fkeret, state=NORMAL, text="08")
    szek10.grid(row=1, column=9)
    szek11 = Button(fkeret, state=NORMAL, text="09")
    szek11.grid(row=2, column=0, pady=10)
    szek12 = Button(fkeret, state=NORMAL, text="10")
    szek12.grid(row=2, column=1)
    szek13 = Button(fkeret, state=NORMAL, text="11")
    szek13.grid(row=2, column=2)
    szek14 = Button(fkeret, state=NORMAL, text="12")
    szek14.grid(row=2, column=3)
    szek15 = Label(fkeret, width=0)
    szek15.grid(row=2, column=4)
    szek16 = Label(fkeret, width=0)
    szek16.grid(row=2, column=5)
    szek17 = Button(fkeret, state=NORMAL, text="13")
    szek17.grid(row=2, column=6)
    szek18 = Button(fkeret, state=NORMAL, text="14")
    szek18.grid(row=2, column=7)
    szek19 = Button(fkeret, state=NORMAL, text="15")
    szek19.grid(row=2, column=8)
    szek20 = Button(fkeret, state=NORMAL, text="16")
    szek20.grid(row=2, column=9)
    szek21 = Button(fkeret, state=NORMAL, text="17")
    szek21.grid(row=3, column=0, pady=10)
    szek22 = Button(fkeret, state=NORMAL, text="18")
    szek22.grid(row=3, column=1)
    szek23 = Button(fkeret, state=NORMAL, text="19")
    szek23.grid(row=3, column=2)
    szek24 = Button(fkeret, state=NORMAL, text="20")
    szek24.grid(row=3, column=3)
    szek25 = Label(fkeret, width=0)
    szek25.grid(row=3, column=4)
    szek26 = Label(fkeret, width=0)
    szek26.grid(row=3, column=5)
    szek27 = Button(fkeret, state=NORMAL, text="21")
    szek27.grid(row=3, column=6)
    szek28 = Button(fkeret, state=NORMAL, text="22")
    szek28.grid(row=3, column=7)
    szek29 = Button(fkeret, state=NORMAL, text="23")
    szek29.grid(row=3, column=8)
    szek30 = Button(fkeret, state=NORMAL, text="24")
    szek30.grid(row=3, column=9)
    szek31 = Button(fkeret, state=NORMAL, text="25")
    szek31.grid(row=4, column=0, pady=10)
    szek32 = Button(fkeret, state=NORMAL, text="26")
    szek32.grid(row=4, column=1)
    szek33 = Button(fkeret, state=NORMAL, text="27")
    szek33.grid(row=4, column=2)
    szek34 = Button(fkeret, state=NORMAL, text="28")
    szek34.grid(row=4, column=3)
    szek35 = Label(fkeret, width=0)
    szek35.grid(row=4, column=4)
    szek36 = Label(fkeret, width=0)
    szek36.grid(row=4, column=5)
    szek37 = Button(fkeret, state=NORMAL, text="29")
    szek37.grid(row=4, column=6)
    szek38 = Button(fkeret, state=NORMAL, text="30")
    szek38.grid(row=4, column=7)
    szek39 = Button(fkeret, state=NORMAL, text="31")
    szek39.grid(row=4, column=8)
    szek40 = Button(fkeret, state=NORMAL, text="32")
    szek40.grid(row=4, column=9)
    szek41 = Button(fkeret, state=NORMAL, text="33")
    szek41.grid(row=5, column=0, pady=10)
    szek42 = Button(fkeret, state=NORMAL, text="34")
    szek42.grid(row=5, column=1)
    szek43 = Button(fkeret, state=NORMAL, text="35")
    szek43.grid(row=5, column=2)
    szek44 = Button(fkeret, state=NORMAL, text="36")
    szek44.grid(row=5, column=3)
    szek45 = Button(fkeret, state=NORMAL, text="37")
    szek45.grid(row=5, column=4)
    szek46 = Button(fkeret, state=NORMAL, text="38")
    szek46.grid(row=5, column=5)
    szek47 = Button(fkeret, state=NORMAL, text="39")
    szek47.grid(row=5, column=6)
    szek48 = Button(fkeret, state=NORMAL, text="40")
    szek48.grid(row=5, column=7)
    szek49 = Button(fkeret, state=NORMAL, text="41")
    szek49.grid(row=5, column=8)
    szek50 = Button(fkeret, state=NORMAL, text="42")
    szek50.grid(row=5, column=9)
    ffoglal = Button(fkeret, text="Helyet foglalok", bootstyle="info", command= lambda:pdf_godzilla())
    ffoglal.grid(row=6, column=0, columnspan=10, pady=10)

def panda_foglal_ablak():
    fog_ablak = Toplevel(root)
    fog_ablak.geometry("1000x700")
    fog_ablak.title("KUNG FU PANDA 4: Foglalás")

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

    fkeret = LabelFrame(fog_ablak, padding=10)
    fkeret.grid(row=1, column=1)
    fleiras = Label(fkeret, text="Csaknem egy évtized után tavasszal visszatér a legkülönösebb kungfu mester a DreamWorks Animation fergeteges sorozatának új fejezetében. Bátor Sárkányharcosként végigcsinált három halált megvető kalandot, és most a sors újabb feladat elé állítja: pihenjen már egy kicsit. Pontosabban hogy legyen a Békevölgy szellemi vezetője. Ezzel van néhány nyilvánvaló probléma. Egyrészt Po annyit tud a szellemi vezetésről, mint a paleodiétáról, másrészt gyorsan találnia kell egy új Sárkányharcost, és ki kell képeznie, mielőtt átvehetné új, magas beosztását. Ám ami még rosszabb, mostanában láttak felbukkanni egy gonosz, nagyhatalmú varázslónőt, Kaméleont, aki apró gyík létére fel tudja venni bármilyen lény alakját, legyen az nagy vagy kicsi. És Kaméleon ráveti dülledt kis szemét a bölcsesség pálcájára, amivel hatalmában állna megidézni az összes gonosztevőt, akiket Po átküldött a szellemek birodalmába...", font=("Times", 12, "bold"), width=50, justify="left", wraplength=400)
    fleiras.grid(row=0, column=0, columnspan=10)
    szek1 = Button(fkeret, state=NORMAL, text="01")
    szek1.grid(row=1, column=0, pady=10)
    szek2 = Button(fkeret, state=NORMAL, text="02")
    szek2.grid(row=1, column=1)
    szek3 = Button(fkeret, state=NORMAL, text="03")
    szek3.grid(row=1, column=2)
    szek4 = Button(fkeret, state=NORMAL, text="04")
    szek4.grid(row=1, column=3)
    szek5 = Label(fkeret, width=0)
    szek5.grid(row=1, column=4)
    szek6 = Label(fkeret, width=0)
    szek6.grid(row=1, column=5)
    szek7 = Button(fkeret, state=NORMAL, text="05")
    szek7.grid(row=1, column=6)
    szek8 = Button(fkeret, state=NORMAL, text="06")
    szek8.grid(row=1, column=7)
    szek9 = Button(fkeret, state=NORMAL, text="07")
    szek9.grid(row=1, column=8)
    szek10 = Button(fkeret, state=NORMAL, text="08")
    szek10.grid(row=1, column=9)
    szek11 = Button(fkeret, state=NORMAL, text="09")
    szek11.grid(row=2, column=0, pady=10)
    szek12 = Button(fkeret, state=NORMAL, text="10")
    szek12.grid(row=2, column=1)
    szek13 = Button(fkeret, state=NORMAL, text="11")
    szek13.grid(row=2, column=2)
    szek14 = Button(fkeret, state=NORMAL, text="12")
    szek14.grid(row=2, column=3)
    szek15 = Label(fkeret, width=0)
    szek15.grid(row=2, column=4)
    szek16 = Label(fkeret, width=0)
    szek16.grid(row=2, column=5)
    szek17 = Button(fkeret, state=NORMAL, text="13")
    szek17.grid(row=2, column=6)
    szek18 = Button(fkeret, state=NORMAL, text="14")
    szek18.grid(row=2, column=7)
    szek19 = Button(fkeret, state=NORMAL, text="15")
    szek19.grid(row=2, column=8)
    szek20 = Button(fkeret, state=NORMAL, text="16")
    szek20.grid(row=2, column=9)
    szek21 = Button(fkeret, state=NORMAL, text="17")
    szek21.grid(row=3, column=0, pady=10)
    szek22 = Button(fkeret, state=NORMAL, text="18")
    szek22.grid(row=3, column=1)
    szek23 = Button(fkeret, state=NORMAL, text="19")
    szek23.grid(row=3, column=2)
    szek24 = Button(fkeret, state=NORMAL, text="20")
    szek24.grid(row=3, column=3)
    szek25 = Label(fkeret, width=0)
    szek25.grid(row=3, column=4)
    szek26 = Label(fkeret, width=0)
    szek26.grid(row=3, column=5)
    szek27 = Button(fkeret, state=NORMAL, text="21")
    szek27.grid(row=3, column=6)
    szek28 = Button(fkeret, state=NORMAL, text="22")
    szek28.grid(row=3, column=7)
    szek29 = Button(fkeret, state=NORMAL, text="23")
    szek29.grid(row=3, column=8)
    szek30 = Button(fkeret, state=NORMAL, text="24")
    szek30.grid(row=3, column=9)
    szek31 = Button(fkeret, state=NORMAL, text="25")
    szek31.grid(row=4, column=0, pady=10)
    szek32 = Button(fkeret, state=NORMAL, text="26")
    szek32.grid(row=4, column=1)
    szek33 = Button(fkeret, state=NORMAL, text="27")
    szek33.grid(row=4, column=2)
    szek34 = Button(fkeret, state=NORMAL, text="28")
    szek34.grid(row=4, column=3)
    szek35 = Label(fkeret, width=0)
    szek35.grid(row=4, column=4)
    szek36 = Label(fkeret, width=0)
    szek36.grid(row=4, column=5)
    szek37 = Button(fkeret, state=NORMAL, text="29")
    szek37.grid(row=4, column=6)
    szek38 = Button(fkeret, state=NORMAL, text="30")
    szek38.grid(row=4, column=7)
    szek39 = Button(fkeret, state=NORMAL, text="31")
    szek39.grid(row=4, column=8)
    szek40 = Button(fkeret, state=NORMAL, text="32")
    szek40.grid(row=4, column=9)
    szek41 = Button(fkeret, state=NORMAL, text="33")
    szek41.grid(row=5, column=0, pady=10)
    szek42 = Button(fkeret, state=NORMAL, text="34")
    szek42.grid(row=5, column=1)
    szek43 = Button(fkeret, state=NORMAL, text="35")
    szek43.grid(row=5, column=2)
    szek44 = Button(fkeret, state=NORMAL, text="36")
    szek44.grid(row=5, column=3)
    szek45 = Button(fkeret, state=NORMAL, text="37")
    szek45.grid(row=5, column=4)
    szek46 = Button(fkeret, state=NORMAL, text="38")
    szek46.grid(row=5, column=5)
    szek47 = Button(fkeret, state=NORMAL, text="39")
    szek47.grid(row=5, column=6)
    szek48 = Button(fkeret, state=NORMAL, text="40")
    szek48.grid(row=5, column=7)
    szek49 = Button(fkeret, state=NORMAL, text="41")
    szek49.grid(row=5, column=8)
    szek50 = Button(fkeret, state=NORMAL, text="42")
    szek50.grid(row=5, column=9)
    ffoglal = Button(fkeret, text="Helyet foglalok", bootstyle="info", command= lambda:pdf_panda())
    ffoglal.grid(row=6, column=0, columnspan=10, pady=10)

def szellemirtok_foglal_ablak():
    fog_ablak = Toplevel(root)
    fog_ablak.geometry("1000x700")
    fog_ablak.title("SZELLEMIRTÓK - A BORZONGÁS BIRODALMA: Foglalás")

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

    fkeret = LabelFrame(fog_ablak, padding=10)
    fkeret.grid(row=1, column=1)
    fleiras = Label(fkeret, text="Kit hívsz, ha nagy baj van?  Kihez fordulnál segítségért, amikor szellemek piszkálnak, kísértetek kísérleteznek veled, vagy hazajáró lelkek dúlják fel a házad? A válasz egyértelmű: a Szellemirtókhoz! De ma már nem ugyanaz a négyes száll be a legendás autóba, amikor riasztás érkezik.Viszont a híres New York-i tűzoltótorony nem változott: az új szellemirtók, a Spengler család tagjai itt találkoznak az eredeti csapattal, akik, mint kiderül, nem mentek nyugdíjba: szupertitkos kísérleti laboratóriumot hoztak létre, hogy még magasabb szinten űzhessék a szellemszakmát. Csakhogy rátalálnak egy ősi műtárgyra, amelyből elszabadul egy gonosz erő – és az öregeknek meg a fiataloknak össze kell fogniuk, hogy megmentsék a világot az új, és mindennél fagyosabb jégkorszaktól.", font=("Times", 12, "bold"), width=50, justify="left", wraplength=400)
    fleiras.grid(row=0, column=0, columnspan=10)
    szek1 = Button(fkeret, state=NORMAL, text="01")
    szek1.grid(row=1, column=0, pady=10)
    szek2 = Button(fkeret, state=NORMAL, text="02")
    szek2.grid(row=1, column=1)
    szek3 = Button(fkeret, state=NORMAL, text="03")
    szek3.grid(row=1, column=2)
    szek4 = Button(fkeret, state=NORMAL, text="04")
    szek4.grid(row=1, column=3)
    szek5 = Label(fkeret, width=0)
    szek5.grid(row=1, column=4)
    szek6 = Label(fkeret, width=0)
    szek6.grid(row=1, column=5)
    szek7 = Button(fkeret, state=NORMAL, text="05")
    szek7.grid(row=1, column=6)
    szek8 = Button(fkeret, state=NORMAL, text="06")
    szek8.grid(row=1, column=7)
    szek9 = Button(fkeret, state=NORMAL, text="07")
    szek9.grid(row=1, column=8)
    szek10 = Button(fkeret, state=NORMAL, text="08")
    szek10.grid(row=1, column=9)
    szek11 = Button(fkeret, state=NORMAL, text="09")
    szek11.grid(row=2, column=0, pady=10)
    szek12 = Button(fkeret, state=NORMAL, text="10")
    szek12.grid(row=2, column=1)
    szek13 = Button(fkeret, state=NORMAL, text="11")
    szek13.grid(row=2, column=2)
    szek14 = Button(fkeret, state=NORMAL, text="12")
    szek14.grid(row=2, column=3)
    szek15 = Label(fkeret, width=0)
    szek15.grid(row=2, column=4)
    szek16 = Label(fkeret, width=0)
    szek16.grid(row=2, column=5)
    szek17 = Button(fkeret, state=NORMAL, text="13")
    szek17.grid(row=2, column=6)
    szek18 = Button(fkeret, state=NORMAL, text="14")
    szek18.grid(row=2, column=7)
    szek19 = Button(fkeret, state=NORMAL, text="15")
    szek19.grid(row=2, column=8)
    szek20 = Button(fkeret, state=NORMAL, text="16")
    szek20.grid(row=2, column=9)
    szek21 = Button(fkeret, state=NORMAL, text="17")
    szek21.grid(row=3, column=0, pady=10)
    szek22 = Button(fkeret, state=NORMAL, text="18")
    szek22.grid(row=3, column=1)
    szek23 = Button(fkeret, state=NORMAL, text="19")
    szek23.grid(row=3, column=2)
    szek24 = Button(fkeret, state=NORMAL, text="20")
    szek24.grid(row=3, column=3)
    szek25 = Label(fkeret, width=0)
    szek25.grid(row=3, column=4)
    szek26 = Label(fkeret, width=0)
    szek26.grid(row=3, column=5)
    szek27 = Button(fkeret, state=NORMAL, text="21")
    szek27.grid(row=3, column=6)
    szek28 = Button(fkeret, state=NORMAL, text="22")
    szek28.grid(row=3, column=7)
    szek29 = Button(fkeret, state=NORMAL, text="23")
    szek29.grid(row=3, column=8)
    szek30 = Button(fkeret, state=NORMAL, text="24")
    szek30.grid(row=3, column=9)
    szek31 = Button(fkeret, state=NORMAL, text="25")
    szek31.grid(row=4, column=0, pady=10)
    szek32 = Button(fkeret, state=NORMAL, text="26")
    szek32.grid(row=4, column=1)
    szek33 = Button(fkeret, state=NORMAL, text="27")
    szek33.grid(row=4, column=2)
    szek34 = Button(fkeret, state=NORMAL, text="28")
    szek34.grid(row=4, column=3)
    szek35 = Label(fkeret, width=0)
    szek35.grid(row=4, column=4)
    szek36 = Label(fkeret, width=0)
    szek36.grid(row=4, column=5)
    szek37 = Button(fkeret, state=NORMAL, text="29")
    szek37.grid(row=4, column=6)
    szek38 = Button(fkeret, state=NORMAL, text="30")
    szek38.grid(row=4, column=7)
    szek39 = Button(fkeret, state=NORMAL, text="31")
    szek39.grid(row=4, column=8)
    szek40 = Button(fkeret, state=NORMAL, text="32")
    szek40.grid(row=4, column=9)
    szek41 = Button(fkeret, state=NORMAL, text="33")
    szek41.grid(row=5, column=0, pady=10)
    szek42 = Button(fkeret, state=NORMAL, text="34")
    szek42.grid(row=5, column=1)
    szek43 = Button(fkeret, state=NORMAL, text="35")
    szek43.grid(row=5, column=2)
    szek44 = Button(fkeret, state=NORMAL, text="36")
    szek44.grid(row=5, column=3)
    szek45 = Button(fkeret, state=NORMAL, text="37")
    szek45.grid(row=5, column=4)
    szek46 = Button(fkeret, state=NORMAL, text="38")
    szek46.grid(row=5, column=5)
    szek47 = Button(fkeret, state=NORMAL, text="39")
    szek47.grid(row=5, column=6)
    szek48 = Button(fkeret, state=NORMAL, text="40")
    szek48.grid(row=5, column=7)
    szek49 = Button(fkeret, state=NORMAL, text="41")
    szek49.grid(row=5, column=8)
    szek50 = Button(fkeret, state=NORMAL, text="42")
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

vetites4film = 5
vetites4ido = "Hétfő"
vetites4ar = round(random.randint(2500, 6500), -2)

vetites5film = 1
vetites5ido = "Kedd"
vetites5ar = round(random.randint(2500, 6500), -2)

vetites6film = 2
vetites6ido = "Kedd"
vetites6ar = round(random.randint(2500, 6500), -2)

vetites7film = 3
vetites7ido = "Kedd"
vetites7ar = round(random.randint(2500, 6500), -2)

vetites8film = 5
vetites8ido = "Kedd"
vetites8ar = round(random.randint(2500, 6500), -2)

vetites9film = 1
vetites9ido = "Szerda"
vetites9ar = round(random.randint(2500, 6500), -2)

vetites10film = 2
vetites10ido = "Szerda"
vetites10ar = round(random.randint(2500, 6500), -2)

vetites11film = 3
vetites11ido = "Szerda"
vetites11ar = round(random.randint(2500, 6500), -2)

vetites12film = 5
vetites12ido = "Szerda"
vetites12ar = round(random.randint(2500, 6500), -2)

vetites13film = 1
vetites13ido = "Csütörtök"
vetites13ar = round(random.randint(2500, 6500), -2)

vetites14film = 2
vetites14ido = "Csütörtök"
vetites14ar = round(random.randint(2500, 6500), -2)

vetites15film = 3
vetites15ido = "Csütörtök"
vetites15ar = round(random.randint(2500, 6500), -2)

vetites16film = 5
vetites16ido = "Csütörtök"
vetites16ar = round(random.randint(2500, 6500), -2)

vetites17film = 1
vetites17ido = "Péntek"
vetites17ar = round(random.randint(2500, 6500), -2)

vetites18film = 2
vetites18ido = "Péntek"
vetites18ar = round(random.randint(2500, 6500), -2)

vetites19film = 3
vetites19ido = "Péntek"
vetites19ar = round(random.randint(2500, 6500), -2)

vetites20film = 5
vetites20ido = "Péntek"
vetites20ar = round(random.randint(2500, 6500), -2)

vetites21film = 1
vetites21ido = "Szombat"
vetites21ar = round(random.randint(2500, 6500), -2)

vetites22film = 2
vetites22ido = "Szombat"
vetites22ar = round(random.randint(2500, 6500), -2)

vetites23film = 3
vetites23ido = "Szombat"
vetites23ar = round(random.randint(2500, 6500), -2)

vetites24film = 5
vetites24ido = "Szombat"
vetites24ar = round(random.randint(2500, 6500), -2)

vetites25film = 1
vetites25ido = "Hétfő"
vetites25ar = round(random.randint(2500, 6500), -2)

vetites26film = 2
vetites26ido = "Hétfő"
vetites26ar = round(random.randint(2500, 6500), -2)

vetites27film = 3
vetites27ido = "Hétfő"
vetites27ar = round(random.randint(2500, 6500), -2)

vetites28film = 5
vetites28ido = "Hétfő"
vetites28ar = round(random.randint(2500, 6500), -2)

adatbazis()

root = Window(themename="superhero")
root.title("MoziTown")
root.geometry("1400x762")
root.resizable(False,False)
root.configure(background="#181D31")
date=dt.datetime.now()

img1 = ImageTk.PhotoImage(Image.open("dune.png")) 
img2 = ImageTk.PhotoImage(Image.open("most.png"))  
img3 = ImageTk.PhotoImage(Image.open("imadlak.png"))  
img4 = ImageTk.PhotoImage(Image.open("mehesz.png"))  
img5 = ImageTk.PhotoImage(Image.open("king.png"))  
img6 = ImageTk.PhotoImage(Image.open("godzilla.png"))  
img7 = ImageTk.PhotoImage(Image.open("panda.png"))  
img8 = ImageTk.PhotoImage(Image.open("szellemirtok.png"))

cimframe=Labelframe(root, border=0, width=1400, )
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