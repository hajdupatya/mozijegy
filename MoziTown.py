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
    fog_ablak = Toplevel(root)
    fog_ablak.geometry("1000x700")
    fog_ablak.title("DŰNE - MÁSODIK RÉSZ: Foglalás")

#sor1
    global d
    d=0
    def foglal_sz1(b):
        global d
        if b==1:
            if d==0 or d%2==0:
                szek1.config(bootstyle="warning")
            else:
                szek1.config(bootstyle="primary")
        d+=1

    global d2
    d2=0
    def foglal_sz2(b):
        global d2
        if b==2:
            if d2==0 or d2%2==0:
                szek2.config(bootstyle="warning")
            else:
                szek2.config(bootstyle="primary")
        d2+=1

    global d3
    d3=0
    def foglal_sz3(b):
        global d3
        if b==3:
            if d3==0 or d3%2==0:
                szek3.config(bootstyle="warning")
            else:
                szek3.config(bootstyle="primary")
        d3+=1

    global d4
    d4=0
    def foglal_sz4(b):
        global d4
        if b==4:
            if d4==0 or d4%2==0:
                szek4.config(bootstyle="warning")
            else:
                szek4.config(bootstyle="primary")
        d4+=1


    global d5
    d5=0
    def foglal_sz5(b):
        global d5
        if b==5:
            if d5==0 or d5%2==0:
                szek7.config(bootstyle="warning")
            else:
                szek7.config(bootstyle="primary")
        d5+=1

    global d6
    d6=0
    def foglal_sz6(b):
        global d6
        if b==6:
            if d6==0 or d6%2==0:
                szek8.config(bootstyle="warning")
            else:
                szek8.config(bootstyle="primary")
        d6+=1

    global d7
    d7=0
    def foglal_sz7(b):
        global d7
        if b==7:
            if d7==0 or d7%2==0:
                szek9.config(bootstyle="warning")
            else:
                szek9.config(bootstyle="primary")
        d7+=1

    global d8
    d8=0
    def foglal_sz8(b):
        global d8
        if b==8:
            if d8==0 or d8%2==0:
                szek10.config(bootstyle="warning")
            else:
                szek10.config(bootstyle="primary")
        d8+=1

#sor2
    global d9
    d9=0
    def foglal_sz9(b):
        global d9
        if b==9:
            if d9==0 or d9%2==0:
                szek11.config(bootstyle="warning")
            else:
                szek11.config(bootstyle="primary")
        d9+=1

    global d10
    d10=0
    def foglal_sz10(b):
        global d10
        if b==10:
            if d10==0 or d10%2==0:
                szek12.config(bootstyle="warning")
            else:
                szek12.config(bootstyle="primary")
        d10+=1

    global d11
    d11=0
    def foglal_sz11(b):
        global d11
        if b==11:
            if d11==0 or d11%2==0:
                szek13.config(bootstyle="warning")
            else:
                szek13.config(bootstyle="primary")
        d11+=1

    global d12
    d12=0
    def foglal_sz12(b):
        global d12
        if b==12:
            if d12==0 or d12%2==0:
                szek14.config(bootstyle="warning")
            else:
                szek14.config(bootstyle="primary")
        d12+=1


    global d13
    d13=0
    def foglal_sz13(b):
        global d13
        if b==13:
            if d13==0 or d13%2==0:
                szek17.config(bootstyle="warning")
            else:
                szek17.config(bootstyle="primary")
        d13+=1

    global d14
    d14=0
    def foglal_sz14(b):
        global d14
        if b==14:
            if d14==0 or d14%2==0:
                szek18.config(bootstyle="warning")
            else:
                szek18.config(bootstyle="primary")
        d14+=1

    global d15
    d15=0
    def foglal_sz15(b):
        global d15
        if b==15:
            if d15==0 or d15%2==0:
                szek19.config(bootstyle="warning")
            else:
                szek19.config(bootstyle="primary")
        d15+=1

    global d16
    d16=0
    def foglal_sz16(b):
        global d16
        if b==16:
            if d16==0 or d16%2==0:
                szek20.config(bootstyle="warning")
            else:
                szek20.config(bootstyle="primary")
        d16+=1


#sor3
    global d17
    d17=0
    def foglal_sz17(b):
        global d17
        if b==17:
            if d17==0 or d17%2==0:
                szek21.config(bootstyle="warning")
            else:
                szek21.config(bootstyle="primary")
        d17+=1

    global d18
    d18=0
    def foglal_sz18(b):
        global d18
        if b==18:
            if d18==0 or d18%2==0:
                szek22.config(bootstyle="warning")
            else:
                szek22.config(bootstyle="primary")
        d18+=1

    global d19
    d19=0
    def foglal_sz19(b):
        global d19
        if b==19:
            if d19==0 or d19%2==0:
                szek23.config(bootstyle="warning")
            else:
                szek23.config(bootstyle="primary")
        d19+=1

    global d20
    d20=0
    def foglal_sz20(b):
        global d20
        if b==20:
            if d20==0 or d20%2==0:
                szek24.config(bootstyle="warning")
            else:
                szek24.config(bootstyle="primary")
        d20+=1


    global d21
    d21=0
    def foglal_sz21(b):
        global d21
        if b==21:
            if d21==0 or d21%2==0:
                szek27.config(bootstyle="warning")
            else:
                szek27.config(bootstyle="primary")
        d21+=1

    global d22
    d22=0
    def foglal_sz22(b):
        global d22
        if b==22:
            if d22==0 or d22%2==0:
                szek28.config(bootstyle="warning")
            else:
                szek28.config(bootstyle="primary")
        d22+=1

    global d23
    d23=0
    def foglal_sz23(b):
        global d23
        if b==23:
            if d23==0 or d23%2==0:
                szek29.config(bootstyle="warning")
            else:
                szek29.config(bootstyle="primary")
        d23+=1

    global d24
    d24=0
    def foglal_sz24(b):
        global d24
        if b==24:
            if d24==0 or d24%2==0:
                szek30.config(bootstyle="warning")
            else:
                szek30.config(bootstyle="primary")
        d24+=1

#sor4
    
    global d25
    d25=0
    def foglal_sz25(b):
        global d25
        if b==25:
            if d25==0 or d25%2==0:
                szek31.config(bootstyle="warning")
            else:
                szek31.config(bootstyle="primary")
        d25+=1

    global d26
    d26=0
    def foglal_sz26(b):
        global d26
        if b==26:
            if d26==0 or d26%2==0:
                szek32.config(bootstyle="warning")
            else:
                szek32.config(bootstyle="primary")
        d26+=1

    global d27
    d27=0
    def foglal_sz27(b):
        global d27
        if b==27:
            if d27==0 or d27%2==0:
                szek33.config(bootstyle="warning")
            else:
                szek33.config(bootstyle="primary")
        d27+=1

    global d28
    d28=0
    def foglal_sz28(b):
        global d28
        if b==28:
            if d28==0 or d28%2==0:
                szek34.config(bootstyle="warning")
            else:
                szek34.config(bootstyle="primary")
        d28+=1


    global d29
    d29=0
    def foglal_sz29(b):
        global d29
        if b==29:
            if d29==0 or d29%2==0:
                szek37.config(bootstyle="warning")
            else:
                szek37.config(bootstyle="primary")
        d29+=1

    global d30
    d30=0
    def foglal_sz30(b):
        global d30
        if b==30:
            if d30==0 or d30%2==0:
                szek38.config(bootstyle="warning")
            else:
                szek38.config(bootstyle="primary")
        d30+=1

    global d31
    d31=0
    def foglal_sz31(b):
        global d31
        if b==31:
            if d31==0 or d31%2==0:
                szek39.config(bootstyle="warning")
            else:
                szek39.config(bootstyle="primary")
        d31+=1

    global d32
    d32=0
    def foglal_sz32(b):
        global d32
        if b==32:
            if d32==0 or d32%2==0:
                szek40.config(bootstyle="warning")
            else:
                szek40.config(bootstyle="primary")
        d32+=1

#sor5
    global d33
    d33=0
    def foglal_sz33(b):
        global d33
        if b==33:
            if d33==0 or d33%2==0:
                szek41.config(bootstyle="warning")
            else:
                szek41.config(bootstyle="primary")
        d33+=1

    global d34
    d34=0
    def foglal_sz34(b):
        global d34
        if b==34:
            if d34==0 or d34%2==0:
                szek42.config(bootstyle="warning")
            else:
                szek42.config(bootstyle="primary")
        d34+=1

    global d35
    d35=0
    def foglal_sz35(b):
        global d35
        if b==35:
            if d35==0 or d35%2==0:
                szek43.config(bootstyle="warning")
            else:
                szek43.config(bootstyle="primary")
        d35+=1

    global d36
    d36=0
    def foglal_sz36(b):
        global d36
        if b==36:
            if d36==0 or d36%2==0:
                szek44.config(bootstyle="warning")
            else:
                szek44.config(bootstyle="primary")
        d36+=1


    global d37
    d37=0
    def foglal_sz37(b):
        global d37
        if b==37:
            if d37==0 or d37%2==0:
                szek45.config(bootstyle="warning")
            else:
                szek45.config(bootstyle="primary")
        d37+=1

    global d38
    d38=0
    def foglal_sz38(b):
        global d38
        if b==38:
            if d38==0 or d38%2==0:
                szek46.config(bootstyle="warning")
            else:
                szek46.config(bootstyle="primary")
        d38+=1

    global d39
    d39=0
    def foglal_sz39(b):
        global d39
        if b==39:
            if d39==0 or d39%2==0:
                szek47.config(bootstyle="warning")
            else:
                szek47.config(bootstyle="primary")
        d39+=1

    global d40
    d40=0
    def foglal_sz40(b):
        global d40
        if b==40:
            if d40==0 or d40%2==0:
                szek48.config(bootstyle="warning")
            else:
                szek48.config(bootstyle="primary")
        d40+=1

    global d41
    d41=0
    def foglal_sz41(b):
        global d41
        if b==41:
            if d41==0 or d41%2==0:
                szek49.config(bootstyle="warning")
            else:
                szek49.config(bootstyle="primary")
        d41+=1

    global d42
    d42=0
    def foglal_sz42(b):
        global d42
        if b==42:
            if d42==0 or d42%2==0:
                szek50.config(bootstyle="warning")
            else:
                szek50.config(bootstyle="primary")
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
    ffoglal = Button(fkeret, text="Helyet foglalok")
    ffoglal.grid(row=6, column=0, columnspan=10, pady=10)

def most_foglal_ablak():
    fog_ablak = Toplevel(root)
    fog_ablak.geometry("1000x700")
    fog_ablak.title("MOST VAGY SOHA!")

    global mo
    mo=0
    def foglal_sz1(b):
        global mo
        if b==1:
            if mo==0 or mo%2==0:
                szek1.config(bootstyle="warning")
            else:
                szek1.config(bootstyle="primary")
        mo+=1

    global mo2
    mo2=0
    def foglal_sz2(b):
        global mo2
        if b==2:
            if mo2==0 or mo2%2==0:
                szek2.config(bootstyle="warning")
            else:
                szek2.config(bootstyle="primary")
        mo2+=1

    global mo3
    mo3=0
    def foglal_sz3(b):
        global mo3
        if b==3:
            if mo3==0 or mo3%2==0:
                szek3.config(bootstyle="warning")
            else:
                szek3.config(bootstyle="primary")
        mo3+=1

    global mo4
    mo4=0
    def foglal_sz4(b):
        global mo4
        if b==4:
            if mo4==0 or mo4%2==0:
                szek4.config(bootstyle="warning")
            else:
                szek4.config(bootstyle="primary")
        mo4+=1


    global mo5
    mo5=0
    def foglal_sz5(b):
        global mo5
        if b==5:
            if mo5==0 or mo5%2==0:
                szek7.config(bootstyle="warning")
            else:
                szek7.config(bootstyle="primary")
        mo5+=1

    global mo6
    mo6=0
    def foglal_sz6(b):
        global mo6
        if b==6:
            if mo6==0 or mo6%2==0:
                szek8.config(bootstyle="warning")
            else:
                szek8.config(bootstyle="primary")
        mo6+=1

    global mo7
    mo7=0
    def foglal_sz7(b):
        global mo7
        if b==7:
            if mo7==0 or mo7%2==0:
                szek9.config(bootstyle="warning")
            else:
                szek9.config(bootstyle="primary")
        mo7+=1

    global mo8
    mo8=0
    def foglal_sz8(b):
        global mo8
        if b==8:
            if mo8==0 or mo8%2==0:
                szek10.config(bootstyle="warning")
            else:
                szek10.config(bootstyle="primary")
        mo8+=1

#sor2
    global mo9
    mo9=0
    def foglal_sz9(b):
        global mo9
        if b==9:
            if mo9==0 or mo9%2==0:
                szek11.config(bootstyle="warning")
            else:
                szek11.config(bootstyle="primary")
        mo9+=1

    global mo10
    mo10=0
    def foglal_sz10(b):
        global mo10
        if b==10:
            if mo10==0 or mo10%2==0:
                szek12.config(bootstyle="warning")
            else:
                szek12.config(bootstyle="primary")
        mo10+=1

    global mo11
    mo11=0
    def foglal_sz11(b):
        global mo11
        if b==11:
            if mo11==0 or mo11%2==0:
                szek13.config(bootstyle="warning")
            else:
                szek13.config(bootstyle="primary")
        mo11+=1

    global mo12
    mo12=0
    def foglal_sz12(b):
        global mo12
        if b==12:
            if mo12==0 or mo12%2==0:
                szek14.config(bootstyle="warning")
            else:
                szek14.config(bootstyle="primary")
        mo12+=1


    global mo13
    mo13=0
    def foglal_sz13(b):
        global mo13
        if b==13:
            if mo13==0 or mo13%2==0:
                szek17.config(bootstyle="warning")
            else:
                szek17.config(bootstyle="primary")
        mo13+=1

    global mo14
    mo14=0
    def foglal_sz14(b):
        global mo14
        if b==14:
            if mo14==0 or mo14%2==0:
                szek18.config(bootstyle="warning")
            else:
                szek18.config(bootstyle="primary")
        mo14+=1

    global mo15
    mo15=0
    def foglal_sz15(b):
        global mo15
        if b==15:
            if mo15==0 or mo15%2==0:
                szek19.config(bootstyle="warning")
            else:
                szek19.config(bootstyle="primary")
        mo15+=1

    global mo16
    mo16=0
    def foglal_sz16(b):
        global mo16
        if b==16:
            if mo16==0 or mo16%2==0:
                szek20.config(bootstyle="warning")
            else:
                szek20.config(bootstyle="primary")
        mo16+=1


#sor3
    global mo17
    mo17=0
    def foglal_sz17(b):
        global mo17
        if b==17:
            if mo17==0 or mo17%2==0:
                szek21.config(bootstyle="warning")
            else:
                szek21.config(bootstyle="primary")
        mo17+=1

    global mo18
    mo18=0
    def foglal_sz18(b):
        global mo18
        if b==18:
            if mo18==0 or mo18%2==0:
                szek22.config(bootstyle="warning")
            else:
                szek22.config(bootstyle="primary")
        mo18+=1

    global mo19
    mo19=0
    def foglal_sz19(b):
        global mo19
        if b==19:
            if mo19==0 or mo19%2==0:
                szek23.config(bootstyle="warning")
            else:
                szek23.config(bootstyle="primary")
        mo19+=1

    global mo20
    mo20=0
    def foglal_sz20(b):
        global mo20
        if b==20:
            if mo20==0 or mo20%2==0:
                szek24.config(bootstyle="warning")
            else:
                szek24.config(bootstyle="primary")
        mo20+=1


    global mo21
    mo21=0
    def foglal_sz21(b):
        global mo21
        if b==21:
            if mo21==0 or mo21%2==0:
                szek27.config(bootstyle="warning")
            else:
                szek27.config(bootstyle="primary")
        mo21+=1

    global mo22
    mo22=0
    def foglal_sz22(b):
        global mo22
        if b==22:
            if mo22==0 or mo22%2==0:
                szek28.config(bootstyle="warning")
            else:
                szek28.config(bootstyle="primary")
        mo22+=1

    global mo23
    mo23=0
    def foglal_sz23(b):
        global mo23
        if b==23:
            if mo23==0 or mo23%2==0:
                szek29.config(bootstyle="warning")
            else:
                szek29.config(bootstyle="primary")
        mo23+=1

    global mo24
    mo24=0
    def foglal_sz24(b):
        global mo24
        if b==24:
            if mo24==0 or mo24%2==0:
                szek30.config(bootstyle="warning")
            else:
                szek30.config(bootstyle="primary")
        mo24+=1

#sor4
    
    global mo25
    mo25=0
    def foglal_sz25(b):
        global mo25
        if b==25:
            if mo25==0 or mo25%2==0:
                szek31.config(bootstyle="warning")
            else:
                szek31.config(bootstyle="primary")
        mo25+=1

    global mo26
    mo26=0
    def foglal_sz26(b):
        global mo26
        if b==26:
            if mo26==0 or mo26%2==0:
                szek32.config(bootstyle="warning")
            else:
                szek32.config(bootstyle="primary")
        mo26+=1

    global mo27
    mo27=0
    def foglal_sz27(b):
        global mo27
        if b==27:
            if mo27==0 or mo27%2==0:
                szek33.config(bootstyle="warning")
            else:
                szek33.config(bootstyle="primary")
        mo27+=1

    global mo28
    mo28=0
    def foglal_sz28(b):
        global mo28
        if b==28:
            if mo28==0 or mo28%2==0:
                szek34.config(bootstyle="warning")
            else:
                szek34.config(bootstyle="primary")
        mo28+=1


    global mo29
    mo29=0
    def foglal_sz29(b):
        global mo29
        if b==29:
            if mo29==0 or mo29%2==0:
                szek37.config(bootstyle="warning")
            else:
                szek37.config(bootstyle="primary")
        mo29+=1

    global mo30
    mo30=0
    def foglal_sz30(b):
        global mo30
        if b==30:
            if mo30==0 or mo30%2==0:
                szek38.config(bootstyle="warning")
            else:
                szek38.config(bootstyle="primary")
        mo30+=1

    global mo31
    mo31=0
    def foglal_sz31(b):
        global mo31
        if b==31:
            if mo31==0 or mo31%2==0:
                szek39.config(bootstyle="warning")
            else:
                szek39.config(bootstyle="primary")
        mo31+=1

    global mo32
    mo32=0
    def foglal_sz32(b):
        global mo32
        if b==32:
            if mo32==0 or mo32%2==0:
                szek40.config(bootstyle="warning")
            else:
                szek40.config(bootstyle="primary")
        mo32+=1

#sor5
    global mo33
    mo33=0
    def foglal_sz33(b):
        global mo33
        if b==33:
            if mo33==0 or mo33%2==0:
                szek41.config(bootstyle="warning")
            else:
                szek41.config(bootstyle="primary")
        mo33+=1

    global mo34
    mo34=0
    def foglal_sz34(b):
        global mo34
        if b==34:
            if mo34==0 or mo34%2==0:
                szek42.config(bootstyle="warning")
            else:
                szek42.config(bootstyle="primary")
        mo34+=1

    global mo35
    mo35=0
    def foglal_sz35(b):
        global mo35
        if b==35:
            if mo35==0 or mo35%2==0:
                szek43.config(bootstyle="warning")
            else:
                szek43.config(bootstyle="primary")
        mo35+=1

    global mo36
    mo36=0
    def foglal_sz36(b):
        global mo36
        if b==36:
            if mo36==0 or mo36%2==0:
                szek44.config(bootstyle="warning")
            else:
                szek44.config(bootstyle="primary")
        mo36+=1


    global mo37
    mo37=0
    def foglal_sz37(b):
        global mo37
        if b==37:
            if mo37==0 or mo37%2==0:
                szek45.config(bootstyle="warning")
            else:
                szek45.config(bootstyle="primary")
        mo37+=1

    global mo38
    mo38=0
    def foglal_sz38(b):
        global mo38
        if b==38:
            if mo38==0 or mo38%2==0:
                szek46.config(bootstyle="warning")
            else:
                szek46.config(bootstyle="primary")
        mo38+=1

    global mo39
    mo39=0
    def foglal_sz39(b):
        global mo39
        if b==39:
            if mo39==0 or mo39%2==0:
                szek47.config(bootstyle="warning")
            else:
                szek47.config(bootstyle="primary")
        mo39+=1

    global mo40
    mo40=0
    def foglal_sz40(b):
        global mo40
        if b==40:
            if mo40==0 or mo40%2==0:
                szek48.config(bootstyle="warning")
            else:
                szek48.config(bootstyle="primary")
        mo40+=1

    global mo41
    mo41=0
    def foglal_sz41(b):
        global mo41
        if b==41:
            if mo41==0 or mo41%2==0:
                szek49.config(bootstyle="warning")
            else:
                szek49.config(bootstyle="primary")
        mo41+=1

    global mo42
    mo42=0
    def foglal_sz42(b):
        global mo42
        if b==42:
            if mo42==0 or mo42%2==0:
                szek50.config(bootstyle="warning")
            else:
                szek50.config(bootstyle="primary")
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
    ffoglal = Button(fkeret, text="Helyet foglalok")
    ffoglal.grid(row=6, column=0, columnspan=10, pady=10)

def imadlak_foglal_ablak():
    fog_ablak = Toplevel(root)
    fog_ablak.geometry("1000x700")
    fog_ablak.title("IMÁDLAK UTÁLNI")

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
    fleiras = Label(fkeret, text="Találkoztak, együtt töltöttek egy éjszakát, és azóta gyűlölik egymást. Van ilyen. Bea (Sydney Sweeney) és Ben (Glen Powell) biztos, hogy nem illenek össze. Ha néha véletlenül összefutnak valahol, tutira elszabadul a pokol: csak bántani tudják egymást. De lesz egy esküvő Ausztráliában, amin mindkettejüknek részt kell venniük. Nincs kibúvó, nincs duma: utazniuk kell. Néhány napon, néhány bulin, néhány vacsorán keresztül el kell viselniük egymás közelségét, miközben egy gyönyörű tengerparti házban ott kavarog körülöttük egy csomó régi szerelmük, néhány kíváncsi rokonuk és kavarni mindig kész felmenőjük. Szóval, azt teszik, amit két érett, felnőtt, felelősségteljes ember ilyenkor tehet: úgy tesznek, mintha szerelmespár lennének – azt remélik, hogy így mindenkinek könnyebb lesz. Nem is tévedhettek volna nagyobbat.", font=("Times", 12, "bold"), width=50, justify="left", wraplength=400)
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
    ffoglal = Button(fkeret, text="Helyet foglalok")
    ffoglal.grid(row=6, column=0, columnspan=10, pady=10)

def mehesz_foglal_ablak():
    fog_ablak = Toplevel(root)
    fog_ablak.geometry("1000x700")
    fog_ablak.title("A MÉHÉSZ")

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
    ffoglal = Button(fkeret, text="Helyet foglalok")
    ffoglal.grid(row=6, column=0, columnspan=10, pady=10)

def godzilla_foglal_ablak():
    fog_ablak = Toplevel(root)
    fog_ablak.geometry("1000x700")
    fog_ablak.title("GODZILLA X KONG: AZ ÚJ BIRODALOM")

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
    ffoglal = Button(fkeret, text="Helyet foglalok")
    ffoglal.grid(row=6, column=0, columnspan=10, pady=10)

def king_foglal_ablak():
    fog_ablak = Toplevel(root)
    fog_ablak.geometry("1000x700")
    fog_ablak.title("ARTÚR, A KIRÁLY")

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
    ffoglal = Button(fkeret, text="Helyet foglalok")
    ffoglal.grid(row=6, column=0, columnspan=10, pady=10)

def panda_foglal_ablak():
    fog_ablak = Toplevel(root)
    fog_ablak.geometry("1000x700")
    fog_ablak.title("KUNG FU PANDA 4")

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
    fleiras = Label(fkeret, text="Bátor Sárkányharcosként végigcsinált három halált megvető kalandot, és most a sors újabb feladat elé állítja: pihenjen már egy kicsit. Pontosabban hogy legyen a Békevölgy szellemi vezetője. Ezzel van néhány nyilvánvaló probléma. Egyrészt Po annyit tud a szellemi vezetésről, mint a paleodiétáról, másrészt gyorsan találnia kell egy új Sárkányharcost, és ki kell képeznie, mielőtt átvehetné új, magas beosztását. Ám ami még rosszabb, mostanában láttak felbukkanni egy gonosz, nagyhatalmú varázslónőt, Kaméleont, aki apró gyík létére fel tudja venni bármilyen lény alakját, legyen az nagy vagy kicsi. És Kaméleon ráveti dülledt kis szemét a bölcsesség pálcájára, amivel hatalmában állna megidézni az összes gonosztevőt, akiket Po átküldött a szellemek birodalmába…", font=("Times", 12, "bold"), width=50, justify="left", wraplength=400)
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
    ffoglal = Button(fkeret, text="Helyet foglalok")
    ffoglal.grid(row=6, column=0, columnspan=10, pady=10)

def szellemirtok_foglal_ablak():
    fog_ablak = Toplevel(root)
    fog_ablak.geometry("1000x700")
    fog_ablak.title("SZELLEMIRTÓK - A BORZONGÁS BIRODALMA")

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
    ffoglal = Button(fkeret, text="Helyet foglalok")
    ffoglal.grid(row=6, column=0, columnspan=10, pady=10)



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
    dune.create_image(0, 0, anchor=NW, image=img6)
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