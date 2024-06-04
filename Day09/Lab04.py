from tkinter import *

def them_vao_danh_sach():
    ten = nhap_ten.get()
    if ten:
        danh_sach.insert(END, ten)
        nhap_ten.delete(0, END)

def xoa_danh_sach():
    danh_sach.delete(0, END)

cua_so = Tk()
cua_so.title("Lab04")
cua_so.geometry("200x200")


nhap_ten_label = Label(cua_so, text="Nhập tên:")
nhap_ten_label.pack()

nhap_ten = Entry(cua_so)
nhap_ten.pack()

nut_them = Button(cua_so, text="Thêm vào danh sách", command=them_vao_danh_sach)
nut_them.pack()

danh_sach = Listbox(cua_so)
danh_sach.pack()

nut_xoa = Button(cua_so, text="Xóa danh sách", command=xoa_danh_sach)
nut_xoa.pack()

cua_so.mainloop()