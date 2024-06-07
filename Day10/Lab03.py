import tkinter as tk
from tkinter import messagebox

def hien_thi_thong_tin():
    ten = nhap_ten.get()
    tuoi = nhap_tuoi.get()
    email = nhap_email.get()

    if ten and tuoi and email:
        thong_tin = f"Tên: {ten}\nTuổi: {tuoi}\nEmail: {email}"
        messagebox.showinfo("Thông tin cá nhân", thong_tin)
    else:
        messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin.")

goc = tk.Tk()
goc.title("Nhập thông tin cá nhân")

nhap_ten_label = tk.Label(goc, text="Tên:")
nhap_ten_label.pack()
nhap_ten = tk.Entry(goc)
nhap_ten.pack()

nhap_tuoi_label = tk.Label(goc, text="Tuổi:")
nhap_tuoi_label.pack()
nhap_tuoi = tk.Entry(goc)
nhap_tuoi.pack()

nhap_email_label = tk.Label(goc, text="Email:")
nhap_email_label.pack()
nhap_email = tk.Entry(goc)
nhap_email.pack()

nut_gui = tk.Button(goc, text="Hiển thị thông tin", command=hien_thi_thong_tin)
nut_gui.pack()

goc.mainloop()