from tkinter import *

def hien_thi_ten():
    ten = nhap_ten.get()
    thong_bao.config(text="Heloo!   " + ten, bg="lightgreen", fg="blue")

cua_so = Tk()
cua_so.title("Lab01")
cua_so.geometry("400x200")

nhap_ten_label = Label(cua_so, text="Nhập tên của bạn:")
nhap_ten_label.pack()

nhap_ten = Entry(cua_so)
nhap_ten.pack()

nut_gui = Button(cua_so, text="Submit", command=hien_thi_ten)
nut_gui.pack()

thong_bao = Label(cua_so, text="")
thong_bao.pack()

cua_so.mainloop()