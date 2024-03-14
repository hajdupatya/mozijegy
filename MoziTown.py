from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from ttkbootstrap import *
from tkinter import PhotoImage
import datetime as dt
from time import strftime

root = Window(themename="superhero")
root.geometry("1400x762")
root.resizable(False,False)
root.configure(background="#181D31")
date=dt.datetime.now()

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


def kedd():
    tue.configure(bootstyle="warning")
    mon.configure(bootstyle="warning-outline")
    wed.configure(bootstyle="warning-outline")
    thu.configure(bootstyle="warning-outline")
    fri.configure(bootstyle="warning-outline")
    sat.configure(bootstyle="warning-outline")
    sun.configure(bootstyle="warning-outline")


def szerda():
    wed.configure(bootstyle="warning")
    tue.configure(bootstyle="warning-outline")
    mon.configure(bootstyle="warning-outline")
    thu.configure(bootstyle="warning-outline")
    fri.configure(bootstyle="warning-outline")
    sat.configure(bootstyle="warning-outline")
    sun.configure(bootstyle="warning-outline")


def csutotok():
    thu.configure(bootstyle="warning")
    tue.configure(bootstyle="warning-outline")
    wed.configure(bootstyle="warning-outline")
    mon.configure(bootstyle="warning-outline")
    fri.configure(bootstyle="warning-outline")
    sat.configure(bootstyle="warning-outline")
    sun.configure(bootstyle="warning-outline")


def pentek():
    fri.configure(bootstyle="warning")
    tue.configure(bootstyle="warning-outline")
    wed.configure(bootstyle="warning-outline")
    thu.configure(bootstyle="warning-outline")
    mon.configure(bootstyle="warning-outline")
    sat.configure(bootstyle="warning-outline")
    sun.configure(bootstyle="warning-outline")


def szombat():
    sat.configure(bootstyle="warning")
    tue.configure(bootstyle="warning-outline")
    wed.configure(bootstyle="warning-outline")
    thu.configure(bootstyle="warning-outline")
    fri.configure(bootstyle="warning-outline")
    mon.configure(bootstyle="warning-outline")
    sun.configure(bootstyle="warning-outline")


def vasarnap():
    sun.configure(bootstyle="warning")
    tue.configure(bootstyle="warning-outline")
    wed.configure(bootstyle="warning-outline")
    thu.configure(bootstyle="warning-outline")
    fri.configure(bootstyle="warning-outline")
    sat.configure(bootstyle="warning-outline")
    mon.configure(bootstyle="warning-outline")

napokfram=LabelFrame(root, border=0,)
napokfram.pack(pady=10)

mon=Button(napokfram,text="Hétfő", bootstyle="warning-outline", command=hetfo)
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

if(f"{date:%A}"=="hétfő"):
    mon.configure(bootstyle="warning")
elif(f"{date:%A}"=="kedd"):
    tue.configure(bootstyle="warning")
elif(f"{date:%A}"=="szerda"):
    wed.configure(bootstyle="warning")    
elif(f"{date:%A}"=="csütörtök"):
    thu.configure(bootstyle="warning")
elif(f"{date:%A}"=="péntek"):
    fri.configure(bootstyle="warning")
elif(f"{date:%A}"=="szombat"):
    sat.configure(bootstyle="warning")
else:
    sun.configure(bootstyle="warning")

musor=Label(root,text="Műsoron",font=('calibri', 25, 'bold'),background="#181D31")
musor.pack()

img = PhotoImage(file="/pics/dune.png")
kep1=Label(root, image=img)
kep1.pack()
root.mainloop()