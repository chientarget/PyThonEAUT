import tkinter as tk
from tkinter import messagebox

# Hàm thực hiện phép cộng
def cong():
    try:
        so_a = float(nhap_so_a.get())
        so_b = float(nhap_so_b.get())
        ket_qua = so_a + so_b
        nhap_ket_qua.delete(0, tk.END)
        nhap_ket_qua.insert(0, str(ket_qua))
        ghi_nhat_ky(f"{so_a} + {so_b} = {ket_qua}")
    except ValueError:
        messagebox.showerror("Nhập sai", "Vui lòng nhập số hợp lệ")

# Hàm thực hiện phép trừ
def tru():
    try:
        so_a = float(nhap_so_a.get())
        so_b = float(nhap_so_b.get())
        ket_qua = so_a - so_b
        nhap_ket_qua.delete(0, tk.END)
        nhap_ket_qua.insert(0, str(ket_qua))
        ghi_nhat_ky(f"{so_a} - {so_b} = {ket_qua}")
    except ValueError:
        messagebox.showerror("Nhập sai", "Vui lòng nhập số hợp lệ")

# Hàm thực hiện phép nhân
def nhan():
    try:
        so_a = float(nhap_so_a.get())
        so_b = float(nhap_so_b.get())
        ket_qua = so_a * so_b
        nhap_ket_qua.delete(0, tk.END)
        nhap_ket_qua.insert(0, str(ket_qua))
        ghi_nhat_ky(f"{so_a} * {so_b} = {ket_qua}")
    except ValueError:
        messagebox.showerror("Nhập sai", "Vui lòng nhập số hợp lệ")

# Hàm thực hiện phép chia
def chia():
    try:
        so_a = float(nhap_so_a.get())
        so_b = float(nhap_so_b.get())
        if so_b == 0:
            messagebox.showerror("Chia cho số 0", "Không thể chia cho số 0")
            return
        ket_qua = so_a / so_b
        nhap_ket_qua.delete(0, tk.END)
        nhap_ket_qua.insert(0, str(ket_qua))
        ghi_nhat_ky(f"{so_a} / {so_b} = {ket_qua}")
    except ValueError:
        messagebox.showerror("Nhập sai", "Vui lòng nhập số hợp lệ")

# Hàm ghi nhật ký
def ghi_nhat_ky(text):
    nhat_ky.insert(tk.END, text + "\n")

# Hàm thoát ứng dụng
def thoat_ung_dung():
    cua_so_chinh.destroy()

# Tạo cửa sổ chính
cua_so_chinh = tk.Tk()
cua_so_chinh.title("Máy tính")

# Nhãn và nhập liệu cho số a, số b và kết quả
tk.Label(cua_so_chinh, text="Nhập số a:").grid(row=0, column=0, padx=2, pady=10)
nhap_so_a = tk.Entry(cua_so_chinh, width=20)
nhap_so_a.grid(row=0, column=1, padx=10, pady=10)

tk.Label(cua_so_chinh, text="Nhập số b:").grid(row=1, column=0, padx=2, pady=10)
nhap_so_b = tk.Entry(cua_so_chinh, width=20)
nhap_so_b.grid(row=1, column=1, padx=10, pady=10)

tk.Label(cua_so_chinh, text="Kết quả:").grid(row=2, column=0, padx=0, pady=10)
nhap_ket_qua = tk.Entry(cua_so_chinh, width=20)
nhap_ket_qua.grid(row=2, column=1, padx=10, pady=10)

# Tạo Frame cho các nút
khung_nut = tk.Frame(cua_so_chinh)
khung_nut.grid(row=3, column=0, columnspan=5)

tk.Button(khung_nut, text="+", width=5, command=cong, highlightbackground="orange", highlightcolor="orange").grid(row=0, column=0, padx=15, pady=5)
tk.Button(khung_nut, text="-", width=5, command=tru, highlightbackground="orange", highlightcolor="orange").grid(row=0, column=1, padx=15, pady=5)
tk.Button(khung_nut, text="*", width=5, command=nhan, highlightbackground="orange", highlightcolor="orange").grid(row=0, column=2, padx=15, pady=5)
tk.Button(khung_nut, text=":", width=5, command=chia, highlightbackground="orange", highlightcolor="orange").grid(row=0, column=3, padx=15, pady=5)
tk.Button(khung_nut, text="Thoát", width=5, fg="red", command=thoat_ung_dung, highlightbackground="orange", highlightcolor="orange").grid(row=0, column=4, padx=15, pady=5)

# Hộp văn bản để ghi nhật ký
nhat_ky = tk.Text(cua_so_chinh, width=30, height=10)
nhat_ky.grid(row=0, column=2, rowspan=3, padx=10, pady=10)

# Chạy ứng dụng
cua_so_chinh.mainloop()