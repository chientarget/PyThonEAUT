import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk

def them_vao_danh_sach():
    phan_tu = nhap.get()
    if phan_tu:
        hop_danh_sach.insert(tk.END, phan_tu)
        nhap.delete(0, tk.END)
    else:
        messagebox.showwarning("Lỗi nhập", "Vui lòng nhập thông tin")

def xoa_danh_sach():
    hop_danh_sach.delete(0, tk.END)

def luu_danh_sach():
    duong_dan_tep = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Tep van ban", "*.txt"), ("Tat ca tep", "*.*")])
    if duong_dan_tep:
        with open(duong_dan_tep, 'w') as tep:
            phan_tu = hop_danh_sach.get(0, tk.END)
            for item in phan_tu:
                tep.write(item + '\n')

def thoat_chuong_trinh():
    goc.destroy()

def mo_anh(chi_so_nguoi):
    duong_dan_anh = [
        "AnhBB/bb1.png",
        "AnhBB/bb2.png",
        "AnhBB/bb3.png",
        "AnhBB/bb4.png",
        "AnhBB/bb5.png",
        "AnhBB/bb6.png"
    ]
    if 0 <= chi_so_nguoi < len(duong_dan_anh):
        anh = Image.open(duong_dan_anh[chi_so_nguoi])
        anh = anh.resize((300, 300), Image.Resampling.LANCZOS)
        anh = ImageTk.PhotoImage(anh)
        nhan_anh.config(image=anh)
        nhan_anh.image = anh

goc = tk.Tk()
goc.title("Lab02")
goc.geometry("600x500")
goc.configure(bg='#0d8b59')  # Yellow background

khung_tren = tk.Frame(goc, bg='#0d8b59')
khung_tren.pack(fill=tk.X, padx=20, pady=20)

nhan_nhap = tk.Label(khung_tren, text="Nhập thông tin:", bg='#0d8b59')
nhan_nhap.grid(row=0, column=0, sticky='w')
nhap = tk.Entry(khung_tren)
nhap.grid(row=0, column=1, pady=5, sticky='w')

nhan_hop_danh_sach = tk.Label(khung_tren, text="Danh Sách:", bg='#0d8b59')
nhan_hop_danh_sach.grid(row=1, column=0, sticky='nw', pady=(10, 0))
hop_danh_sach = tk.Listbox(khung_tren, width=30, height=10)
hop_danh_sach.grid(row=1, column=1, pady=5, sticky='w')

khung_nut = tk.Frame(khung_tren, bg='#0d8b59')
khung_nut.grid(row=0, column=2, rowspan=2, padx=20, sticky='n')

nut_them = tk.Button(khung_nut, text="Thêm vào danh sách", command=them_vao_danh_sach)
nut_them.pack(pady=5, fill=tk.X)

nut_xoa = tk.Button(khung_nut, text="Xóa danh sách", command=xoa_danh_sach)
nut_xoa.pack(pady=5, fill=tk.X)

nut_luu = tk.Button(khung_nut, text="Lưu danh sách", command=luu_danh_sach)
nut_luu.pack(pady=5, fill=tk.X)

nut_thoat = tk.Button(khung_nut, text="Thoát", command=thoat_chuong_trinh)
nut_thoat.pack(pady=5, fill=tk.X)

khung_duoi = tk.Frame(goc, bg='#0d8b59')
khung_duoi.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

khung_nut_anh = tk.Frame(khung_duoi, bg='#0d8b59')
khung_nut_anh.pack(side=tk.LEFT)

nut_nguoi = [
    tk.Button(khung_nut_anh, text="Bạn bè 01", command=lambda: mo_anh(0)),
    tk.Button(khung_nut_anh, text="Bạn bè 02", command=lambda: mo_anh(1)),
    tk.Button(khung_nut_anh, text="Bạn bè 03", command=lambda: mo_anh(2)),
    tk.Button(khung_nut_anh, text="Bạn bè 04", command=lambda: mo_anh(3)),
    tk.Button(khung_nut_anh, text="Bạn bè 05", command=lambda: mo_anh(4)),
    tk.Button(khung_nut_anh, text="Bạn bè 06", command=lambda: mo_anh(5)),
]

for nut in nut_nguoi:
    nut.pack(pady=5, fill=tk.X)

nhan_anh = tk.Label(khung_duoi, bg='#0d8b59')
nhan_anh.pack(side=tk.RIGHT, padx=20)

goc.mainloop()