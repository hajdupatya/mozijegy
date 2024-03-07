from tkinter import *
from tkinter import messagebox
from ttkbootstrap import *
import datetime as dt


root = Window(themename="superhero")
root.geometry("1400x762")
root.resizable(False,False)
root.configure(background="#181D31")

cim=Label(root, text="MoziTown",background="#181D31",font=("Terminal","35","bold"))
cim.pack(pady=20)
date=dt.datetime.now()


napokfram=LabelFrame(root, border=0,)
napokfram.pack()

mon=Button(napokfram,text="Hétfő", bootstyle="warning-outline")
mon.grid(row=0, column=0,pady=(0,15),padx=15)
tue=Button(napokfram,text="Kedd", bootstyle="warning-outline")
tue.grid(row=0, column=1,pady=(0,15),padx=15)
wed=Button(napokfram,text="Szerda", bootstyle="warning-outline")
wed.grid(row=0, column=2,pady=(0,15),padx=15)
thu=Button(napokfram,text="Csütörtök", bootstyle="warning-outline")
thu.grid(row=0, column=3,pady=(0,15),padx=15)
fri=Button(napokfram,text="Péntek", bootstyle="warning-outline")
fri.grid(row=0, column=4,pady=(0,15),padx=15)
sat=Button(napokfram,text="Szombat", bootstyle="warning-outline")
sat.grid(row=0, column=5,pady=(0,15),padx=15)
sun=Button(napokfram,text="Vasárnap", bootstyle="warning-outline")
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
root.mainloop()