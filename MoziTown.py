from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from ttkbootstrap import *
from tkinter import PhotoImage
import datetime as dt
from time import strftime



root = Window(themename="superhero")
root.title("MoziTown")
root.geometry("1400x762")
root.resizable(False,False)
root.configure(background="#181D31")
date=dt.datetime.now()

img1 = ImageTk.PhotoImage(Image.open("J:\ikt\mozijegy\mozijegy\dune.png")) 
img2 = ImageTk.PhotoImage(Image.open("J:\ikt\mozijegy\mozijegy\most.png"))  
img3 = ImageTk.PhotoImage(Image.open("J:\ikt\mozijegy\mozijegy\imadlak.png"))  
img4 = ImageTk.PhotoImage(Image.open("J:\ikt\mozijegy\mozijegy\mehesz.png"))  
img5 = ImageTk.PhotoImage(Image.open("J:\ikt\mozijegy\mozijegy\king.png"))  
img6 = ImageTk.PhotoImage(Image.open("J:\ikt\mozijegy\mozijegy\godzilla.png"))  
img7 = ImageTk.PhotoImage(Image.open("J:\ikt\mozijegy\mozijegy\panda.png"))  
img8 = ImageTk.PhotoImage(Image.open("J:\ikt\mozijegy\mozijegy\szellemirtok.png")) 

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

def dune_foglal_ablak():
    fog_ablak=Toplevel(root)

def most_foglal_ablak():
    fog_ablak=Toplevel(root)

def imadlak_foglal_ablak():
    fog_ablak=Toplevel(root)

def mehesz_foglal_ablak():
    fog_ablak=Toplevel(root)

def godzilla_foglal_ablak():
    fog_ablak=Toplevel(root)

def king_foglal_ablak():
    fog_ablak=Toplevel(root)

def panda_foglal_ablak():
    fog_ablak=Toplevel(root)

def szellemirtok_foglal_ablak():
    fog_ablak=Toplevel(root)

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
    buy1.configure(command=dune_foglal_ablak)

    most.create_image(0, 0, anchor=NW, image=img2)
    cim2.configure(text="MOST VAGY SOHA!")
    buy2.configure(command=most_foglal_ablak)

    imadlak.create_image(0, 0, anchor=NW, image=img3)
    cim3.configure(text="IMÁDLAK UTÁLNI")
    buy3.configure(command=imadlak_foglal_ablak)

    mehesz.create_image(0, 0, anchor=NW, image=img4)
    cim4.configure(text="A MÉHÉSZ")
    buy4.configure(command=mehesz_foglal_ablak)

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
    buy1.configure(command=king_foglal_ablak)

    most.create_image(0, 0, anchor=NW, image=img3)
    cim2.configure(text="IMÁDLAK UTÁLNI")
    buy2.configure(command=imadlak_foglal_ablak)

    imadlak.create_image(0, 0, anchor=NW, image=img6)
    cim3.configure(text="GODZILLA X KONG: ...")
    buy3.configure(command=godzilla_foglal_ablak)

    mehesz.create_image(0, 0, anchor=NW, image=img8)
    cim4.configure(text="SZELLEMIRTÓK ...")
    buy4.configure(command=szellemirtok_foglal_ablak)

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
    buy1.configure(command=most_foglal_ablak)

    most.create_image(0, 0, anchor=NW, image=img7)
    cim2.configure(text="KUNG FU PANDA 4")
    buy2.configure(command=panda_foglal_ablak)

    imadlak.create_image(0, 0, anchor=NW, image=img4)
    cim3.configure(text="A MÉHÉSZ")
    buy3.configure(command=mehesz_foglal_ablak)

    mehesz.create_image(0, 0, anchor=NW, image=img8)
    cim4.configure(text="SZELLEMIRTÓK ...")
    buy4.configure(command=szellemirtok_foglal_ablak)


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
    buy1.configure(command=dune_foglal_ablak)

    most.create_image(0, 0, anchor=NW, image=img4)
    cim2.configure(text="A MÉHÉSZ")
    buy2.configure(command=mehesz_foglal_ablak)

    imadlak.create_image(0, 0, anchor=NW, image=img7)
    cim3.configure(text="KUNG FU PANDA 4")
    buy3.configure(command=panda_foglal_ablak)

    mehesz.create_image(0, 0, anchor=NW, image=img6)
    cim4.configure(text="GODZILLA X KONG: ...")
    buy4.configure(command=godzilla_foglal_ablak)


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
    buy1.configure(command=godzilla_foglal_ablak)

    most.create_image(0, 0, anchor=NW, image=img5)
    cim2.configure(text="ARTÚR, A KIRÁLY")
    buy2.configure(command=king_foglal_ablak)

    imadlak.create_image(0, 0, anchor=NW, image=img3)
    cim3.configure(text="IMÁDLAK UTÁLNI")
    buy3.configure(command=imadlak_foglal_ablak)

    mehesz.create_image(0, 0, anchor=NW, image=img2)
    cim4.configure(text="MOST VAGY SOHA!")
    buy4.configure(command=most_foglal_ablak)

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
    buy1.configure(command=godzilla_foglal_ablak)

    most.create_image(0, 0, anchor=NW, image=img5)
    cim2.configure(text="ARTÚR, A KIRÁLY")
    buy2.configure(command=king_foglal_ablak)

    imadlak.create_image(0, 0, anchor=NW, image=img4)
    cim3.configure(text="A MÉHÉSZ")
    buy3.configure(command=mehesz_foglal_ablak)

    mehesz.create_image(0, 0, anchor=NW, image=img1)
    cim4.configure(text="DŰNE - MÁSODIK RÉSZ")
    buy4.configure(command=dune_foglal_ablak)


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
    buy1.configure(command=panda_foglal_ablak)

    most.create_image(0, 0, anchor=NW, image=img4)
    cim2.configure(text="A MÉHÉSZ")
    buy2.configure(command=mehesz_foglal_ablak)

    imadlak.create_image(0, 0, anchor=NW, image=img2)
    cim3.configure(text="MOST VAGY SOHA!")
    buy3.configure(command=most_foglal_ablak)

    mehesz.create_image(0, 0, anchor=NW, image=img1)
    cim4.configure(text="DŰNE - MÁSODIK RÉSZ")
    buy4.configure(command=dune_foglal_ablak)


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
buy1=Button(film1,text="Vásárlás", bootstyle="warning",command=dune_foglal_ablak)
buy1.pack(pady=6,padx=15,)

most = Canvas(film2, width=250, height=370, bg='white')
most.pack()
most.create_image(0, 0, anchor=NW, image=img2)
cim2=Label(film2,text="MOST VAGY SOHA!",font=('calibri', 15, 'bold'))
cim2.pack(pady=(6,0))
buy2=Button(film2,text="Vásárlás", bootstyle="warning",command=most_foglal_ablak)
buy2.pack(pady=6,padx=15,)

imadlak = Canvas(film3, width=250, height=370, bg='white')
imadlak.pack()
imadlak.create_image(0, 0, anchor=NW, image=img3)
cim3=Label(film3,text="IMÁDLAK UTÁLNI",font=('calibri', 15, 'bold'))
cim3.pack(pady=(6,0))
buy3=Button(film3,text="Vásárlás", bootstyle="warning",command=imadlak_foglal_ablak)
buy3.pack(pady=6,padx=15,)

mehesz = Canvas(film4, width=250, height=370, bg='white')
mehesz.pack()
mehesz.create_image(0, 0, anchor=NW, image=img4)
cim4=Label(film4,text="A MÉHÉSZ",font=('calibri', 15, 'bold'))
cim4.pack(pady=(6,0))
buy4=Button(film4,text="Vásárlás", bootstyle="warning",command=mehesz_foglal_ablak)
buy4.pack(pady=6,padx=15,)
root.mainloop()