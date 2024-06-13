import tkinter as tk
from tkinter import ttk


cua_so_chinh = tk.Tk()
cua_so_chinh.title("variable.isdigit()")

danh_sach_so = []

def them_vao_danh_sach():
    so = nhap_lieu.get()
    if so.isdigit():
        danh_sach_so.append(int(so))
        hop_danh_sach.insert(tk.END, so)
        nhap_lieu.delete(0, tk.END)
    else:
        nhap_lieu.delete(0, tk.END)

def xoa_danh_sach():
    danh_sach_so.clear()
    hop_danh_sach.delete(0, tk.END)

nhap_lieu = ttk.Entry(cua_so_chinh)
nhap_lieu.pack(pady=10)

nut_them = ttk.Button(cua_so_chinh, text="Thêm vào danh sách", command=them_vao_danh_sach)
nut_them.pack(pady=5)

hop_danh_sach = tk.Listbox(cua_so_chinh, width=20)
hop_danh_sach.pack(pady=10)

nut_xoa = ttk.Button(cua_so_chinh, text="Xóa danh sách", command=xoa_danh_sach)
nut_xoa.pack(pady=5)

cua_so_chinh.mainloop()