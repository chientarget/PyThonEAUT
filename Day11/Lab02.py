import tkinter as tk
from PIL import Image, ImageTk
import random

# Tạo hai số ngẫu nhiên và lưu tổng của chúng
def tao_cau_hoi():
    global dap_an
    so1 = random.randint(10, 50)
    so2 = random.randint(10, 50)
    dap_an = so1 + so2
    nhan_cau_hoi.config(text=f"{so1} + {so2} = ?")

# Kiểm tra câu trả lời của người dùng
def kiem_tra_cau_tra_loi():
    cau_tra_loi_nguoi_dung = int(nhap_cau_tra_loi.get())
    if cau_tra_loi_nguoi_dung == dap_an:
        hinh_anh = Image.open("Flat_tick_icon.png")
    else:
        hinh_anh = Image.open("cross.png")
    hinh_anh = hinh_anh.resize((200, 200))
    hinh_anh = ImageTk.PhotoImage(hinh_anh)
    nhan_hinh_anh.config(image=hinh_anh)
    nhan_hinh_anh.image = hinh_anh

# Xóa trường nhập và tạo một câu hỏi mới
def cau_hoi_tiep_theo():
    nhap_cau_tra_loi.delete(0, 'end')
    tao_cau_hoi()

goc = tk.Tk()
goc.title("Trắc nghiệm Toán")
goc.geometry("600x300")

# Khung bên trái cho câu hỏi, ô nhập và nút bấm
khung_trai = tk.Frame(goc, padx=20, pady=20)
khung_trai.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

nhan_cau_hoi = tk.Label(khung_trai, text="", font=("Arial", 16))
nhan_cau_hoi.pack(pady=(0, 20))

nhap_cau_tra_loi = tk.Entry(khung_trai, font=("Arial", 14))
nhap_cau_tra_loi.pack(pady=(0, 10))

nut_kiem_tra = tk.Button(khung_trai, text="Kiểm tra", command=kiem_tra_cau_tra_loi, font=("Arial", 12))
nut_kiem_tra.pack(pady=(0, 10))

nut_tiep_theo = tk.Button(khung_trai, text="Tiếp theo", command=cau_hoi_tiep_theo, font=("Arial", 12))
nut_tiep_theo.pack()

# Khung bên phải cho hình ảnh
khung_phai = tk.Frame(goc, padx=20, pady=20, bg="white")
khung_phai.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

nhan_hinh_anh = tk.Label(khung_phai, bg="white")
nhan_hinh_anh.pack(fill=tk.BOTH, expand=True)

tao_cau_hoi()

goc.mainloop()