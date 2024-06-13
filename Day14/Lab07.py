import sqlite3
from tkinter import *

ket_noi = sqlite3.connect('TestScores.db')
con_tro = ket_noi.cursor()
con_tro.execute('''CREATE TABLE IF NOT EXISTS scores
             (name TEXT, grade INTEGER)''')
ket_noi.commit()

def them_diem():
    ten = nhap_ten.get()
    diem = nhap_diem.get()
    if ten and diem:
        try:
            diem = int(diem)
            con_tro.execute("INSERT INTO scores VALUES (?, ?)", (ten, diem))
            ket_noi.commit()
            xoa_nhap_lieu()
        except ValueError:
            pass

def xoa_nhap_lieu():
    nhap_ten.delete(0, END)
    nhap_diem.delete(0, END)

# Tạo GUI
giao_dien = Tk()
giao_dien.title("TestScores")

nhap_ten_label = Label(giao_dien, text="Nhập tên học sinh")
nhap_ten_label.grid(row=0, column=0)
nhap_ten = Entry(giao_dien)
nhap_ten.grid(row=0, column=1)

nhap_diem_label = Label(giao_dien, text="Nhập điểm học sinh")
nhap_diem_label.grid(row=1, column=0)
nhap_diem = Entry(giao_dien)
nhap_diem.grid(row=1, column=1)

them_button = Button(giao_dien, text="Thêm", command=them_diem)
them_button.grid(row=2, column=0)

xoa_button = Button(giao_dien, text="Xóa", command=xoa_nhap_lieu)
xoa_button.grid(row=2, column=1)

thoat_button = Button(giao_dien, text="Thoát", command=giao_dien.quit)
thoat_button.grid(row=2, column=2)

giao_dien.mainloop()

# Đóng kết nối cơ sở dữ liệu
ket_noi.close()