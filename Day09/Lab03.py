from tkinter import *

def cong_vao_tong():
    global tong
    so = nhap_so.get()
    if so.isdigit():
        tong += int(so)
        hien_thi_tong.config(text="Tổng: " + str(tong))
        nhap_so.delete(0, END)

def dat_lai_tong():
    global tong
    tong = 0
    hien_thi_tong.config(text="Tổng: " + str(tong))
    nhap_so.delete(0, END)

tong = 0

cua_so = Tk()
cua_so.title("Lab03")
cua_so.geometry("400x200")

nhap_so_label = Label(cua_so, text="Nhập số:")
nhap_so_label.pack()

nhap_so = Entry(cua_so)
nhap_so.pack()

nut_cong = Button(cua_so, text="Thêm", command=cong_vao_tong)
nut_cong.pack()

nut_dat_lai = Button(cua_so, text="Đặt lại tổng", command=dat_lai_tong)
nut_dat_lai.pack()

hien_thi_tong = Label(cua_so, text="Tổng: " + str(tong))
hien_thi_tong.pack()

cua_so.mainloop()