import tkinter as tk
from tkinter import messagebox
import random


BG_COLOR = "#2E4053"
TEXT_COLOR = "#FDFFFC"
ACCENT_COLOR = "#E94560"

class TroChoiDoanSo:
    def __init__(self, goc):
        self.goc = goc
        self.goc.title("Trò chơi đoán số")
        self.goc.geometry("600x400")
        self.goc.configure(bg=BG_COLOR)

        self.so_muc_tieu = random.randint(1, 100)
        print(self.so_muc_tieu)
        self.so_lan_thu = 5
        self.lan_doan = []

        # Thiết kế giao diện
        self.tieu_de = tk.Label(goc, text="Đoán một số từ 1 đến 100", fg=TEXT_COLOR, bg=BG_COLOR, font=("Arial", 20, "bold"))
        self.tieu_de.pack(pady=20)

        self.nhap = tk.Entry(goc, font=("Arial", 16), fg=TEXT_COLOR, bg=ACCENT_COLOR, insertbackground=TEXT_COLOR)
        self.nhap.pack(pady=10, padx=50)

        self.lan_doan_frame = tk.Frame(goc, bg=BG_COLOR)
        self.lan_doan_frame.pack(pady=5)

        self.nut = tk.Button(goc, text="Đoán", command=self.kiem_tra_doan, bg=ACCENT_COLOR, fg=TEXT_COLOR, font=("Arial", 14))
        self.nut.pack(pady=10)

        self.phan_hoi = tk.Label(goc, text="", fg=TEXT_COLOR, bg=BG_COLOR, font=("Arial", 14))
        self.phan_hoi.pack(pady=10)

    def kiem_tra_doan(self):
        try:
            doan = int(self.nhap.get())
        except ValueError:
            messagebox.showwarning("Nhập không hợp lệ", "Vui lòng nhập một số hợp lệ.", parent=self.goc)
            return

        if doan < 1 or doan > 100:
            messagebox.showwarning("Ngoài giới hạn", "Vui lòng đoán một số từ 1 đến 100.", parent=self.goc)
            return

        self.so_lan_thu -= 1
        self.lan_doan.append(doan)

        if doan == self.so_muc_tieu:
            messagebox.showinfo("Chúc mừng", "Bạn đã đoán đúng số!", parent=self.goc)
            self.khoi_dong_lai_tro_choi()
        else:
            if self.so_lan_thu > 0:
                self.phan_hoi.config(text=f"Sai! Bạn còn {self.so_lan_thu} lần thử.")
            else:
                messagebox.showinfo("Trò chơi kết thúc", f"Bạn đã hết lần thử! Số đúng là {self.so_muc_tieu}.", parent=self.goc)
                self.khoi_dong_lai_tro_choi()

        self.hien_thi_lan_doan()

    def hien_thi_lan_doan(self):
        for widget in self.lan_doan_frame.winfo_children():
            widget.destroy()

        for i, doan in enumerate(self.lan_doan):
            label = tk.Label(self.lan_doan_frame, text=str(doan), fg=TEXT_COLOR, bg=BG_COLOR, font=("Arial", 12), padx=5)
            label.grid(row=0, column=i, padx=2)

    def khoi_dong_lai_tro_choi(self):
        self.so_muc_tieu = random.randint(1, 100)
        self.so_lan_thu = 5
        self.phan_hoi.config(text="")
        self.nhap.delete(0, tk.END)
        self.lan_doan = []
        self.hien_thi_lan_doan()

if __name__ == "__main__":
    goc = tk.Tk()
    tro_choi = TroChoiDoanSo(goc)
    goc.mainloop()