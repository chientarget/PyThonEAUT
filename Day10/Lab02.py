import tkinter as tk
from tkinter import messagebox
import math
import random
import turtle


def tinh_giai_thua():
    try:
        so = int(nhap_giai_thua.get())
        ket_qua = math.factorial(so)
        messagebox.showinfo("Kết quả", f"Giai thừa của {so} là {ket_qua}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số nguyên hợp lệ")


def tinh_phep_tinh_ngau_nhien():
    so1 = random.randint(1, 100)
    so2 = random.randint(1, 100)
    tong = so1 + so2
    tich = so1 * so2
    hieu = so1 - so2
    if so2 != 0:
        thuong = so1 / so2
    else:
        thuong = "Không thể chia cho 0"
    messagebox.showinfo("Kết quả",
                        f"Số ngẫu nhiên 1: {so1}, Số ngẫu nhiên 2: {so2}\nTổng: {tong}, Tích: {tich}, Hiệu: {hieu}, Thương: {thuong}")


def giai_phuong_trinh_bac_nhat():
    try:
        a = float(nhap_a.get())
        b = float(nhap_b.get())
        if a != 0:
            ket_qua = -b / a
            messagebox.showinfo("Kết quả", f"Giá trị của x là {ket_qua}")
        else:
            messagebox.showerror("Lỗi", "a không được bằng 0")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ")


def tinh_hang_dang_thuc():
    try:
        x = float(nhap_x.get())
        ket_qua1 = (x + 1) ** 2
        ket_qua2 = (x - 1) ** 2
        ket_qua3 = x ** 2 - 1
        ket_qua4 = x ** 2 + 2 * x + 1
        messagebox.showinfo("Kết quả",
                            f"(x+1)^2 = {ket_qua1}, (x-1)^2 = {ket_qua2}, x^2 - 1 = {ket_qua3}, x^2 + 2x + 1 = {ket_qua4}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ")


def ve_tam_giac():
    try:
        a = float(nhap_canh_a.get())
        b = float(nhap_canh_b.get())
        c = float(nhap_canh_c.get())

        if a + b > c and a + c > b and b + c > a:
            A = math.acos((b*b + c*c - a*a) / (2 * b * c))
            B = math.acos((a*a + c*c - b*b) / (2 * a * c))
            C = math.pi - A - B

            t = turtle.Turtle()
            t.reset()

            t.forward(b * 10)
            t.left(180 - math.degrees(C))
            t.forward(a * 10)
            t.left(180 - math.degrees(B))
            t.forward(c * 10)

            turtle.done()
        else:
            messagebox.showerror("Lỗi", "Ba cạnh không hợp lệ để tạo thành một tam giác")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ")


def mo_may_tinh():
    t = turtle.Turtle()
    t.reset()
    t.speed(1)

    # Vẽ màn hình máy tính
    t.penup()
    t.goto(-50, 100)
    t.pendown()
    t.forward(150)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(150)
    t.right(90)
    t.forward(200)

    # Vẽ các nút số
    nut = [
        ('7', -40, 50), ('8', -10, 50), ('9', 20, 50),
        ('4', -40, 20), ('5', -10, 20), ('6', 20, 20),
        ('1', -40, -10), ('2', -10, -10), ('3', 20, -10),
        ('0', -10, -40)
    ]

    for (nhan, x, y) in nut:
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.write(nhan, font=("Arial", 18, "normal"))

    # Vẽ các nút tính toán
    toan_tu = [
        ('+', 50, 50), ('-', 50, 20), ('*', 50, -10), ('/', 50, -40)
    ]

    for (nhan, x, y) in toan_tu:
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.write(nhan, font=("Arial", 18, "normal"))

    turtle.done()


def thoat_chuong_trinh():
    goc.quit()


# Tạo cửa sổ chính
goc = tk.Tk()
goc.title("Ứng dụng tính toán")

# Tính giai thừa
nhap_giai_thua = tk.Entry(goc)
nhap_giai_thua.pack()
nut_giai_thua = tk.Button(goc, text="Tính giai thừa", command=tinh_giai_thua)
nut_giai_thua.pack()

# Phep toan co ban
nut_phep_tinh = tk.Button(goc, text="Tính toán hai số ngẫu nhiên", command=tinh_phep_tinh_ngau_nhien)
nut_phep_tinh.pack()

# Giải phương trình bậc nhất
nhap_a = tk.Entry(goc)
nhap_a.pack()
nhap_b = tk.Entry(goc)
nhap_b.pack()
nut_phuong_trinh = tk.Button(goc, text="Giải phương trình", command=giai_phuong_trinh_bac_nhat)
nut_phuong_trinh.pack()

# Tính hằng đẳng thức
nhap_x = tk.Entry(goc)
nhap_x.pack()
nut_hang_dang_thuc = tk.Button(goc, text="Tính hằng đẳng thức", command=tinh_hang_dang_thuc)
nut_hang_dang_thuc.pack()

# Vẽ tam giác
nhap_canh_a = tk.Entry(goc)
nhap_canh_a.pack()
nhap_canh_b = tk.Entry(goc)
nhap_canh_b.pack()
nhap_canh_c = tk.Entry(goc)
nhap_canh_c.pack()
nut_tam_giac = tk.Button(goc, text="Vẽ Tam giác", command=ve_tam_giac)
nut_tam_giac.pack()

# Mở máy tính
nut_may_tinh = tk.Button(goc, text="Vẽ Máy tính", command=mo_may_tinh)
nut_may_tinh.pack()

# Thoát chương trình
nut_thoat = tk.Button(goc, text="Thoát", command=thoat_chuong_trinh)
nut_thoat.pack()

# Chạy ứng dụng
goc.mainloop()
