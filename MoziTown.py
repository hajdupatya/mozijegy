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

    sz1=False
    sz2=False
    sz3=False
    sz4=False
    sz5=False
    sz6=False
    sz7=False
    sz8=False
    sz9=False
    sz10=False
    sz11=False
    sz12=False
    sz13=False
    sz14=False
    sz15=False
    sz16=False
    sz17=False
    sz18=False
    sz19=False
    sz20=False
    sz21=False
    sz22=False
    sz23=False
    sz24=False
    sz25=False
    sz26=False
    sz27=False
    sz28=False
    sz29=False
    sz30=False
    sz31=False
    sz32=False
    sz33=False
    sz34=False
    sz35=False
    sz36=False
    sz37=False
    sz38=False
    sz39=False
    sz40=False
    sz41=False
    sz42=False


    def foglal_sz1 (sz1):
        if sz1==False:
            sz1=True


 




    def foglal_sz2 (sz2):
        if sz2 ==False:
            sz2 =True
        else:
            sz2 =False
    def foglal_sz3 (sz3):
        if sz3 ==False:
            sz3 =True
        else:
            sz3 =False
    def foglal_sz4 (sz4):
        if sz4 ==False:
            sz4 =True
        else:
            sz4 =False
    def foglal_sz5 (sz5):
        if sz5 ==False:
            sz5 =True
        else:
            sz5 =False
    def foglal_sz6 (sz6):
        if sz6 ==False:
            sz6 =True
        else:
            sz6 =False
    def foglal_sz7 (sz7):
        if sz7 ==False:
            sz7 =True
        else:
            sz7 =False
    def foglal_sz8 (sz8):
        if sz8 ==False:
            sz8 =True
        else:
            sz8 =False
    def foglal_sz9 (sz9):
        if sz9 ==False:
            sz9 =True
        else:
            sz9 =False
    def foglal_sz10 (sz10):
        if sz10 ==False:
            sz10 =True
        else:
            sz10 =False
    def foglal_sz11 (sz11):
        if sz11 ==False:
            sz11 =True
        else:
            sz11 =False
    def foglal_sz12 (sz12):
        if sz12 ==False:
            sz12 =True
        else:
            sz12 =False
    def foglal_sz13 (sz13):
        if sz13 ==False:
            sz13 =True
        else:
            sz13 =False
    def foglal_sz14 (sz14):
        if sz14 ==False:
            sz14 =True
        else:
            sz14 =False
    def foglal_sz15 (sz15):
        if sz15 ==False:
            sz15 =True
        else:
            sz15 =False
    def foglal_sz16 (sz16):
        if sz16 ==False:
            sz16 =True
        else:
            sz16 =False
    def foglal_sz17 (sz17):
        if sz17 ==False:
            sz17 =True
        else:
            sz17 =False
    def foglal_sz18 (sz18):
        if sz18 ==False:
            sz18 =True
        else:
            sz18 =False
    def foglal_sz19 (sz19):
        if sz19 ==False:
            sz19 =True
        else:
            sz19 =False
    def foglal_sz20 (sz20):
        if sz20 ==False:
            sz20 =True
        else:
            sz20 =False
    def foglal_sz21 (sz21):
        if sz21 ==False:
            sz21 =True
        else:
            sz21 =False
    def foglal_sz22 (sz22):
        if sz22 ==False:
            sz22 =True
        else:
            sz22 =False
    def foglal_sz23 (sz23):
        if sz23 ==False:
            sz23 =True
        else:
            sz23 =False
    def foglal_sz24(sz24):
        if sz24 ==False:
            sz24 =True
        else:
            sz24 =False
    def foglal_sz25 (sz25):
        if sz25 ==False:
            sz25 =True
        else:
            sz25 =False
    def foglal_sz26 (sz26):
        if sz26 ==False:
            sz26 =True
        else:
            sz26 =False
    def foglal_sz27 (sz27):
        if sz27 ==False:
            sz27 =True
        else:
            sz27 =False
    def foglal_sz28 (sz28):
        if sz28 ==False:
            sz28 =True
        else:
            sz28 =False
    def foglal_sz29 (sz29):
        if sz29 ==False:
            sz29 =True
        else:
            sz29 =False
    def foglal_sz30 (sz30):
        if sz30 ==False:
            sz30 =True
        else:
            sz30 =False
    def foglal_sz31 (sz31):
        if sz31 ==False:
            sz31 =True
        else:
            sz31 =False
    def foglal_sz32 (sz32):
        if sz32 ==False:
            sz32 =True
        else:
            sz32 =False
    def foglal_sz33 (sz33):
        if sz33 ==False:
            sz33 =True
        else:
            sz33 =False
    def foglal_sz34 (sz34):
        if sz34 ==False:
            sz34 =True
        else:
            sz34 =False
    def foglal_sz35 (sz35):
        if sz35 ==False:
            sz35 =True
        else:
            sz35 =False
    def foglal_sz36 (sz36):
        if sz36 ==False:
            sz36 =True
        else:
            sz36 =False
    def foglal_sz37 (sz37):
        if sz37 ==False:
            sz37 =True
        else:
            sz37 =False
    def foglal_sz38 (sz38):
        if sz38 ==False:
            sz38 =True
        else:
            sz38 =False
    def foglal_sz39 (sz39):
        if sz39 ==False:
            sz39 =True
        else:
            sz39 =False
    def foglal_sz40 (sz40):
        if sz40 ==False:
            sz40 =True
        else:
            sz40 =False
    def foglal_sz41 (sz41):
        if sz41 ==False:
            sz41 =True
        else:
            sz41 =False
    def foglal_sz42 (sz42):
        if sz42 ==False:
            sz42 =True
        else:
            sz42 =False


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
    szek1 = Button(fkeret, state=NORMAL, text="01" ,command=lambda:foglal_sz1(sz1))
    szek1.grid(row=1, column=0, pady=10)
    szek2 = Button(fkeret, state=NORMAL, text="02", command=lambda:foglal_sz2(sz2))
    szek2.grid(row=1, column=1)
    szek3 = Button(fkeret, state=NORMAL, text="03", command=lambda:foglal_sz3(sz3))
    szek3.grid(row=1, column=2)
    szek4 = Button(fkeret, state=NORMAL, text="04", command=lambda:foglal_sz4(sz4))
    szek4.grid(row=1, column=3)
    szek5 = Label(fkeret, width=0)
    szek5.grid(row=1, column=4)
    szek6 = Label(fkeret, width=0)
    szek6.grid(row=1, column=5)
    szek7 = Button(fkeret, state=NORMAL, text="05", command=lambda:foglal_sz5(sz5))
    szek7.grid(row=1, column=6)
    szek8 = Button(fkeret, state=NORMAL, text="06" , command=lambda:foglal_sz6(sz6))
    szek8.grid(row=1, column=7)
    szek9 = Button(fkeret, state=NORMAL, text="07" , command=lambda:foglal_sz7(sz7))
    szek9.grid(row=1, column=8)
    szek10 = Button(fkeret, state=NORMAL, text="08", command=lambda:foglal_sz8(sz8))
    szek10.grid(row=1, column=9)
    szek11 = Button(fkeret, state=NORMAL, text="09", command=lambda:foglal_sz9(sz9))
    szek11.grid(row=2, column=0, pady=10)
    szek12 = Button(fkeret, state=NORMAL, text="10", command=lambda:foglal_sz10(sz10))
    szek12.grid(row=2, column=1)
    szek13 = Button(fkeret, state=NORMAL, text="11" , command=lambda:foglal_sz11(sz11))
    szek13.grid(row=2, column=2)
    szek14 = Button(fkeret, state=NORMAL, text="12", command=lambda:foglal_sz12(sz12))
    szek14.grid(row=2, column=3)
    szek15 = Label(fkeret, width=0)
    szek15.grid(row=2, column=4)
    szek16 = Label(fkeret, width=0)
    szek16.grid(row=2, column=5)
    szek17 = Button(fkeret, state=NORMAL, text="13" , command=lambda:foglal_sz13(sz13))
    szek17.grid(row=2, column=6)
    szek18 = Button(fkeret, state=NORMAL, text="14" , command=lambda:foglal_sz14(sz14))
    szek18.grid(row=2, column=7)
    szek19 = Button(fkeret, state=NORMAL, text="15", command=lambda:foglal_sz15(sz15))
    szek19.grid(row=2, column=8)
    szek20 = Button(fkeret, state=NORMAL, text="16", command=lambda:foglal_sz16(sz16))
    szek20.grid(row=2, column=9)
    szek21 = Button(fkeret, state=NORMAL, text="17", command=lambda:foglal_sz17(sz17))
    szek21.grid(row=3, column=0, pady=10)
    szek22 = Button(fkeret, state=NORMAL, text="18", command=lambda:foglal_sz18(sz18))
    szek22.grid(row=3, column=1)
    szek23 = Button(fkeret, state=NORMAL, text="19", command=lambda:foglal_sz19(sz19))
    szek23.grid(row=3, column=2)
    szek24 = Button(fkeret, state=NORMAL, text="20", command=lambda:foglal_sz20(sz20))
    szek24.grid(row=3, column=3)
    szek25 = Label(fkeret, width=0)
    szek25.grid(row=3, column=4)
    szek26 = Label(fkeret, width=0)
    szek26.grid(row=3, column=5)
    szek27 = Button(fkeret, state=NORMAL, text="21", command=lambda:foglal_sz21(sz21))
    szek27.grid(row=3, column=6)
    szek28 = Button(fkeret, state=NORMAL, text="22", command=lambda:foglal_sz22(sz22))
    szek28.grid(row=3, column=7)
    szek29 = Button(fkeret, state=NORMAL, text="23", command=lambda:foglal_sz23(sz23))
    szek29.grid(row=3, column=8)
    szek30 = Button(fkeret, state=NORMAL, text="24", command=lambda:foglal_sz24(sz24))
    szek30.grid(row=3, column=9)
    szek31 = Button(fkeret, state=NORMAL, text="25", command=lambda:foglal_sz25(sz25))
    szek31.grid(row=4, column=0, pady=10)
    szek32 = Button(fkeret, state=NORMAL, text="26", command=lambda:foglal_sz26(sz26))
    szek32.grid(row=4, column=1)
    szek33 = Button(fkeret, state=NORMAL, text="27", command=lambda:foglal_sz27(sz27))
    szek33.grid(row=4, column=2)
    szek34 = Button(fkeret, state=NORMAL, text="28", command=lambda:foglal_sz28(sz28))
    szek34.grid(row=4, column=3)
    szek35 = Label(fkeret, width=0)
    szek35.grid(row=4, column=4)
    szek36 = Label(fkeret, width=0)
    szek36.grid(row=4, column=5)
    szek37 = Button(fkeret, state=NORMAL, text="29" , command=lambda:foglal_sz29(sz29))
    szek37.grid(row=4, column=6)
    szek38 = Button(fkeret, state=NORMAL, text="30", command=lambda:foglal_sz30(sz30))
    szek38.grid(row=4, column=7)
    szek39 = Button(fkeret, state=NORMAL, text="31" , command=lambda:foglal_sz31(sz31))
    szek39.grid(row=4, column=8)
    szek40 = Button(fkeret, state=NORMAL, text="32", command=lambda:foglal_sz32(sz32))
    szek40.grid(row=4, column=9)
    szek41 = Button(fkeret, state=NORMAL, text="33" , command=lambda:foglal_sz33(sz33))
    szek41.grid(row=5, column=0, pady=10)
    szek42 = Button(fkeret, state=NORMAL, text="34", command=lambda:foglal_sz34(sz34))
    szek42.grid(row=5, column=1)
    szek43 = Button(fkeret, state=NORMAL, text="35", command=lambda:foglal_sz35(sz35))
    szek43.grid(row=5, column=2)
    szek44 = Button(fkeret, state=NORMAL, text="36", command=lambda:foglal_sz36(sz36))
    szek44.grid(row=5, column=3)
    szek45 = Button(fkeret, state=NORMAL, text="37", command=lambda:foglal_sz37(sz37))
    szek45.grid(row=5, column=4)
    szek46 = Button(fkeret, state=NORMAL, text="38", command=lambda:foglal_sz38(sz38))
    szek46.grid(row=5, column=5)
    szek47 = Button(fkeret, state=NORMAL, text="39", command=lambda:foglal_sz39(sz39))
    szek47.grid(row=5, column=6)
    szek48 = Button(fkeret, state=NORMAL, text="40", command=lambda:foglal_sz40(sz40))
    szek48.grid(row=5, column=7)
    szek49 = Button(fkeret, state=NORMAL, text="41", command=lambda:foglal_sz41(sz41))
    szek49.grid(row=5, column=8)
    szek50 = Button(fkeret, state=NORMAL, text="42", command=lambda:foglal_sz42(sz42))
    szek50.grid(row=5, column=9)
    ffoglal = Button(fkeret, text="Helyet foglalok")
    ffoglal.grid(row=6, column=0, columnspan=10, pady=10)







def most_foglal_ablak():
    fog_ablak = Toplevel(root)
    fog_ablak.geometry("1000x700")
    fog_ablak.title("MOST VAGY SOHA!")

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