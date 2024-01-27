from tkinter import *
import locale
from tkinter import filedialog
import tkinter as tk
import main
from threading import Thread

locale.setlocale(locale.LC_ALL, locale.setlocale(locale.LC_TIME, "tr_TR.utf8"))
import ttkbootstrap as ttk
girdiler = []
path = "wordlist.txt"
def get_text_from_entry(entry):
    text = entry.get("1.0", tk.END)
    if text != "":
        girdiler.append(text)
    else:
        print("Alan boş.")

def open_folder_dialog():
    folder_path = filedialog.askdirectory()
    if folder_path:
        text_box.delete("1.0", tk.END)  # Mevcut içeriği temizle
        text_box.insert(tk.END, folder_path)

#fonksiyonlar
def cikis():
    master.destroy()

def create():
    if var_sayi == 1:
        bool_sayi = True
    else:
        bool_sayi = False
    if var_ozel == 1:
        bool_ozel = True
    else:
        bool_ozel = False
    path = text_box.get("1.0", tk.END)
    path += "/wordlist.txt"
    print(path)
    get_text_from_entry(text_box01)
    get_text_from_entry(text_box02)
    get_text_from_entry(text_box03)
    get_text_from_entry(text_box04)
    get_text_from_entry(text_box05)
    get_text_from_entry(text_box06)
    get_text_from_entry(text_box07)
    get_text_from_entry(text_box08)
    get_text_from_entry(text_box09)
    temp = main.split_and_flatten(main.tahmin(girdiler))
    t = Thread(target=main.generate_wordlist, args=(temp, bool_sayi, bool_ozel))
    t.start()
    main.generate_wordlist(words=temp, use_numbers=bool_sayi, use_special_chars=bool_ozel)

# Fontlar
Font_tuple = ("Bodoni", 16)

# Temel Grafik Birimleri Oluşturma
master = Tk()
master.title("Siber Ajanda")
master.attributes('-fullscreen', True)
master.configure(bg='black')
#master.iconbitmap("hacker.png")
canvas = Canvas(master, height = 450, width = 750)
canvas.configure(bg='black')
canvas.pack(fill=BOTH, expand=True)
frame_sol = Frame(master,bg = "#4A484A" , highlightbackground="#6973ff", highlightthickness=3)
frame_sol.place(relx = 0.05, rely = 0.05, relwidth = 0.2, relheight = 0.75)
frame_orta = Frame(master,bg = "#4A484A" , highlightbackground="#6973ff", highlightthickness=3)
frame_orta.place(relx = 0.27, rely = 0.05, relwidth = 0.7, relheight = 0.9)
frame_cikis = Frame(master,bg = "#4A484A" , highlightbackground="#6973ff", highlightthickness=3)
frame_cikis.place(relx = 0.05, rely = 0.825, relwidth = 0.2, relheight = 0.125)

#Scrollbar Özellikleri
style = ttk.Style('darkly')
scrollbar = ttk.Scrollbar(frame_orta, bootstyle='info-round')
scrollbar.pack(pady=10,side=RIGHT, fill='y')
scrollbar.set(0.1,0.9)



#Text Özellikleri
text = Text(frame_orta)
text.configure(font=Font_tuple, foreground="white",state="normal",yscrollcommand=scrollbar.set)
scrollbar.config( command = text.yview )



# Metin ekranı
text_box = tk.Text(frame_sol, height=1, width=40)
text_box.pack(anchor=NW, pady=5, padx=15)
button = tk.Button(frame_sol, text="Klasör Seç", command=open_folder_dialog)
button.place(x=280,y=10)

# Buton Tanımlamaları
var_ozel = IntVar()
R1=Checkbutton(frame_sol,text="Özel karakterler", variable = var_ozel, onvalue=1, offvalue=0, font="Verdana 12")
R1.pack(anchor=NW, pady=5, padx=15)

var_sayi = IntVar()
R2=Checkbutton(frame_sol,text="Sayılar", variable = var_sayi, onvalue=1, offvalue=0, font="Verdana 12")
R2.pack(anchor=NW, pady=5, padx=15)

var_benzer = IntVar()
R3=Checkbutton(frame_sol,text="Benzer kelimeleri getirme", variable = var_benzer, onvalue=1, offvalue=0, font="Verdana 12")
R3.pack(anchor=NW, pady=5, padx=15)




cikis_buton = Button(frame_cikis, text = "Çıkış", command = cikis)
cikis_buton.place(relx = 0.05, rely = 0.15, relwidth = 0.9, relheight = 0.7)


text_box01 = tk.Text(frame_orta, height=1, width=150)
text_box01.pack(anchor=NW, pady=30, padx=150)
text_box02 = tk.Text(frame_orta, height=1, width=150)
text_box02.pack(anchor=NW, pady=30, padx=150)
text_box03 = tk.Text(frame_orta, height=1, width=150)
text_box03.pack(anchor=NW, pady=30, padx=150)
text_box04 = tk.Text(frame_orta, height=1, width=150)
text_box04.pack(anchor=NW, pady=30, padx=150)
text_box05 = tk.Text(frame_orta, height=1, width=150)
text_box05.pack(anchor=NW, pady=30, padx=150)
text_box06 = tk.Text(frame_orta, height=1, width=150)
text_box06.pack(anchor=NW, pady=30, padx=150)
text_box07 = tk.Text(frame_orta, height=1, width=150)
text_box07.pack(anchor=NW, pady=30, padx=150)
text_box08 = tk.Text(frame_orta, height=1, width=150)
text_box08.pack(anchor=NW, pady=30, padx=150)
text_box09 = tk.Text(frame_orta, height=1, width=150)
text_box09.pack(anchor=NW, pady=30, padx=150)
basla_buton = Button(frame_orta, text = "Başlat", command = create, width=50, height=5)
basla_buton.pack(anchor=NW, pady=30, padx=450)

master.mainloop()
