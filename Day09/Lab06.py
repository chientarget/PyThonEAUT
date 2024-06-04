from tkinter import *

def them_so():
    so = nhap_so.get()
    if so.isdigit():
        danh_sach.insert(END, so)
        nhap_so.delete(0, END)
    else:
        nhap_so.delete(0, END)

def xoa_danh_sach():
    danh_sach.delete(0, END)

cua_so = Tk()
cua_so.title("Lab06")
cua_so.geometry("300x350")

nhap_so_label = Label(cua_so, text="Nhập số:")
nhap_so_label.pack()

nhap_so = Entry(cua_so)
nhap_so.pack()

nut_them = Button(cua_so, text="Thêm vào danh sách", command=them_so)
nut_them.pack()

danh_sach = Listbox(cua_so)
danh_sach.pack()

nut_xoa = Button(cua_so, text="Xóa danh sách", command=xoa_danh_sach)
nut_xoa.pack()

cua_so.mainloop()