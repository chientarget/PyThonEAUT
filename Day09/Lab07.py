from tkinter import *
import csv

def them_so():
    so = nhap_so.get()
    if so.isdigit():
        danh_sach.insert(END, so)
        nhap_so.delete(0, END)
    else:
        nhap_so.delete(0, END)

def xoa_danh_sach():
    danh_sach.delete(0, END)

def luu_danh_sach():
    tmp_list = danh_sach.get(0, END)
    with open('numbers.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for number in tmp_list:
            writer.writerow([number])

cua_so = Tk()
cua_so.title("Lab07")
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

nut_luu = Button(cua_so, text="Lưu danh sách", command=luu_danh_sach)
nut_luu.pack()

cua_so.mainloop()