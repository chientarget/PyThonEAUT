import tkinter as tk
import sqlite3

# Tạo cửa sổ chính
cua_so_chinh = tk.Tk()
cua_so_chinh.title("Đăng nhập")

# Tạo hàm xử lý khi nhấn nút Đăng nhập
def luu_dang_nhap():
    ten_dang_nhap = nhap_ten_dang_nhap.get()
    mat_khau = nhap_mat_khau.get()

    # Kết nối đến cơ sở dữ liệu SQLite
    ket_noi = sqlite3.connect('dang_nhap.db')
    con_tro = ket_noi.cursor()

    # Tạo bảng nếu nó chưa tồn tại
    con_tro.execute('''CREATE TABLE IF NOT EXISTS dang_nhap
                 (ten_dang_nhap TEXT, mat_khau TEXT)''')

    # Chèn dữ liệu vào bảng
    con_tro.execute("INSERT INTO dang_nhap VALUES (?, ?)", (ten_dang_nhap, mat_khau))

    # Xác nhận thay đổi và đóng kết nối
    ket_noi.commit()
    ket_noi.close()
    # Xóa các trường nhập
    nhap_ten_dang_nhap.delete(0, tk.END)
    nhap_mat_khau.delete(0, tk.END)

# Tạo nhãn và trường nhập
nhan_ten_dang_nhap = tk.Label(cua_so_chinh, text="Tên đăng nhập:")
nhan_ten_dang_nhap.pack()
nhap_ten_dang_nhap = tk.Entry(cua_so_chinh)
nhap_ten_dang_nhap.pack()

nhan_mat_khau = tk.Label(cua_so_chinh, text="Mật khẩu:")
nhan_mat_khau.pack()
nhap_mat_khau = tk.Entry(cua_so_chinh, show="*")
nhap_mat_khau.pack()

# Tạo nút
nut_dang_nhap = tk.Button(cua_so_chinh, text="Đăng nhập", command=luu_dang_nhap)
nut_dang_nhap.pack(side=tk.LEFT, padx=10, pady=10)

nut_thoat = tk.Button(cua_so_chinh, text="Thoát", command=cua_so_chinh.quit)
nut_thoat.pack(side=tk.LEFT, padx=10, pady=10)

# Bắt đầu vòng lặp sự kiện chính
cua_so_chinh.mainloop()