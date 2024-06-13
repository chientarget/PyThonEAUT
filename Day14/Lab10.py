import sqlite3
import tkinter as tk
from tkinter import messagebox

ket_noi = sqlite3.connect('mydatabase.db')
con_tro = ket_noi.cursor()

con_tro.execute('''CREATE TABLE IF NOT EXISTS bang
             (id INTEGER PRIMARY KEY, ten TEXT, tuoi INTEGER)''')

def them_ban_ghi():
    ten = nhap_ten.get()
    tuoi = nhap_tuoi.get()
    con_tro.execute("INSERT INTO bang (ten, tuoi) VALUES (?, ?)", (ten, tuoi))
    ket_noi.commit()
    messagebox.showinfo("Thành công", "Bản ghi đã được thêm thành công!")
    nhap_ten.delete(0, tk.END)
    nhap_tuoi.delete(0, tk.END)


def xem_ban_ghi():
    ban_ghi = con_tro.execute("SELECT * FROM bang").fetchall()
    messagebox.showinfo("Bản ghi", "\n".join([f"ID: {id}, Tên: {ten}, Tuổi: {tuoi}" for id, ten, tuoi in ban_ghi]))


def xoa_ban_ghi():
    id_xoa = nhap_id.get()
    con_tro.execute("DELETE FROM bang WHERE id=?", (id_xoa,))
    ket_noi.commit()
    messagebox.showinfo("Thành công", "Bản ghi đã được xóa thành công!")
    cua_so_xoa.destroy()

def cap_nhat_ban_ghi():
    id_cap_nhat = nhap_id.get()
    ten_moi = nhap_ten.get()
    tuoi_moi = nhap_tuoi.get()
    con_tro.execute("UPDATE bang SET ten=?, tuoi=? WHERE id=?", (ten_moi, tuoi_moi, id_cap_nhat))
    ket_noi.commit()
    messagebox.showinfo("Thành công", "Bản ghi đã được cập nhật thành công!")
    cua_so_cap_nhat.destroy()

cua_so_chinh = tk.Tk()
cua_so_chinh.title("Chào mừng đến với Chương trình của tôi")


nut_xem = tk.Button(cua_so_chinh, text="Xem", command=xem_ban_ghi)
nut_them = tk.Button(cua_so_chinh, text="Thêm", command=lambda: cua_so_them.deiconify())
nut_xoa = tk.Button(cua_so_chinh, text="Xóa", command=lambda: cua_so_xoa.deiconify())
nut_cap_nhat = tk.Button(cua_so_chinh, text="Cập nhật", command=lambda: cua_so_cap_nhat.deiconify())
nut_thoat = tk.Button(cua_so_chinh, text="Thoát", command=cua_so_chinh.quit)


nut_xem.grid(row=0, column=0, padx=10, pady=10)
nut_them.grid(row=0, column=1, padx=10, pady=10)
nut_xoa.grid(row=1, column=0, padx=10, pady=10)
nut_cap_nhat.grid(row=1, column=1, padx=10, pady=10)
nut_thoat.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


cua_so_them = tk.Toplevel(cua_so_chinh)
cua_so_them.title("Thêm Bản ghi")
cua_so_them.withdraw()

nhan_ten = tk.Label(cua_so_them, text="Tên:")
nhap_ten = tk.Entry(cua_so_them)
nhan_tuoi = tk.Label(cua_so_them, text="Tuổi:")
nhap_tuoi = tk.Entry(cua_so_them)
nut_them = tk.Button(cua_so_them, text="Thêm", command=them_ban_ghi)

nhan_ten.grid(row=0, column=0, padx=5, pady=5)
nhap_ten.grid(row=0, column=1, padx=5, pady=5)
nhan_tuoi.grid(row=1, column=0, padx=5, pady=5)
nhap_tuoi.grid(row=1, column=1, padx=5, pady=5)
nut_them.grid(row=2, column=0, columnspan=2, padx=5, pady=5)


cua_so_xoa = tk.Toplevel(cua_so_chinh)
cua_so_xoa.title("Xóa Bản ghi")
cua_so_xoa.withdraw()

nhan_id = tk.Label(cua_so_xoa, text="Nhập ID để xóa:")
nhap_id = tk.Entry(cua_so_xoa)
nut_xoa = tk.Button(cua_so_xoa, text="Xóa", command=xoa_ban_ghi)

nhan_id.pack(padx=10, pady=10)
nhap_id.pack(padx=10, pady=10)
nut_xoa.pack(padx=10, pady=10)

cua_so_cap_nhat = tk.Toplevel(cua_so_chinh)
cua_so_cap_nhat.title("Cập nhật Bản ghi")
cua_so_cap_nhat.withdraw()

nhan_id = tk.Label(cua_so_cap_nhat, text="Nhập ID để cập nhật:")
nhap_id = tk.Entry(cua_so_cap_nhat)
nhan_ten = tk.Label(cua_so_cap_nhat, text="Tên mới:")
nhap_ten = tk.Entry(cua_so_cap_nhat)
nhan_tuoi = tk.Label(cua_so_cap_nhat, text="Tuổi mới:")
nhap_tuoi = tk.Entry(cua_so_cap_nhat)
nut_cap_nhat = tk.Button(cua_so_cap_nhat, text="Cập nhật", command=cap_nhat_ban_ghi)

nhan_id.grid(row=0, column=0, padx=5, pady=5)
nhap_id.grid(row=0, column=1, padx=5, pady=5)
nhan_ten.grid(row=1, column=0, padx=5, pady=5)
nhap_ten.grid(row=1, column=1, padx=5, pady=5)
nhan_tuoi.grid(row=2, column=0, padx=5, pady=5)
nhap_tuoi.grid(row=2, column=1, padx=5, pady=5)
nut_cap_nhat.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

cua_so_chinh.mainloop()

ket_noi.close()