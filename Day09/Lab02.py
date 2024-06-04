from tkinter import *
import random

def xuc_xac():
    ket_qua = random.randint(1, 6)
    hien_thi_ket_qua.config(text=str(ket_qua))

cua_so = Tk()
cua_so.title("Lab02")
cua_so.geometry("400x200")

nut_xuc_xac = Button(cua_so, text="Roll", command=xuc_xac)
nut_xuc_xac.pack()

hien_thi_ket_qua = Label(cua_so, text="")
hien_thi_ket_qua.pack()

cua_so.mainloop()