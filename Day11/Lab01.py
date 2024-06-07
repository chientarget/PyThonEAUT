import tkinter as tk
from PIL import Image, ImageTk

def hien_thi_loi_chao():
    ten = nhap_ten.get()
    loi_chao.delete("1.0", "end")
    loi_chao.insert("1.0", f"Xin chào {ten}")

goc = tk.Tk()
goc.geometry("500x500")
goc.title("Ứng dụng của tôi")
goc.iconbitmap('Flat_tick_icon.ico')

# Mở hình ảnh và thay đổi kích thước
hinh_anh_goc = Image.open("avt.jpg")
hinh_anh = ImageTk.PhotoImage(hinh_anh_goc.resize((200, 200)))

# Tạo một nhãn để hiển thị hình ảnh
nhap_hinh_anh = tk.Label(goc, image=hinh_anh)
nhap_hinh_anh.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

nhap_ten_label = tk.Label(goc, text="Nhập tên của bạn:")
nhap_ten_label.grid(row=1, column=0, padx=10, pady=10)

nhap_ten = tk.Entry(goc)
nhap_ten.grid(row=1, column=1, padx=10, pady=10)

nut_chao = tk.Button(goc, text="Nhấn vào đây", command=hien_thi_loi_chao)
nut_chao.grid(row=2, column=0,  padx=10, pady=10)

loi_chao = tk.Text(goc, height=15, width=30)
loi_chao.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

goc.mainloop()