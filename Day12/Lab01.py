from tkinter import *
from tkinter import messagebox
import math

def giai_pt_bac_nhat():
    he_so_a = float(nhap_he_so_a.get())
    he_so_b = float(nhap_he_so_b.get())
    if he_so_a == 0:
        if he_so_b == 0:
            messagebox.showinfo("Kết quả", "Phương trình vô số nghiệm")
        else:
            messagebox.showinfo("Kết quả", "Phương trình vô nghiệm")
    else:
        nghiem_x = -he_so_b/he_so_a
        messagebox.showinfo("Kết quả", "Phương trình có nghiệm x = " + str(nghiem_x))


def giai_pt_bac_hai():
    he_so_a = float(nhap_he_so_a.get())
    he_so_b = float(nhap_he_so_b.get())
    he_so_c = float(nhap_he_so_c.get())
    if he_so_a == 0:
        if he_so_b == 0:
            if he_so_c == 0:
                messagebox.showinfo("Kết quả", "Phương trình vô số nghiệm")
            else:
                messagebox.showinfo("Kết quả", "Phương trình vô nghiệm")
        else:
            nghiem_x = -he_so_c/he_so_b
            messagebox.showinfo("Kết quả", "Phương trình có nghiệm x = " + str(nghiem_x))
    else:
        delta = he_so_b*he_so_b - 4*he_so_a*he_so_c
        if delta < 0:
            messagebox.showinfo("Kết quả", "Phương trình vô nghiệm")
        elif delta == 0:
            nghiem_x = -he_so_b/(2*he_so_a)
            messagebox.showinfo("Kết quả", "Phương trình có nghiệm kép x = " + str(nghiem_x))
        else:
            nghiem_x1 = (-he_so_b + math.sqrt(delta))/(2*he_so_a)
            nghiem_x2 = (-he_so_b - math.sqrt(delta))/(2*he_so_a)
            messagebox.showinfo("Kết quả", "Phương trình có 2 nghiệm x1 = " + str(nghiem_x1) + ", x2 = " + str(nghiem_x2))

goc = Tk()
goc.title("Giải phương trình bậc nhất và bậc 2")

khung = Frame(goc)
khung.pack()

nhap_he_so_a = Label(khung, text="Nhập a:")
nhap_he_so_a.grid(row=0, column=0)
nhap_he_so_a = Entry(khung)
nhap_he_so_a.grid(row=0, column=1)

nhap_he_so_b = Label(khung, text="Nhập b:")
nhap_he_so_b.grid(row=1, column=0)
nhap_he_so_b = Entry(khung)
nhap_he_so_b.grid(row=1, column=1)

nhap_he_so_c = Label(khung, text="Nhập c:")
nhap_he_so_c.grid(row=2, column=0)
nhap_he_so_c = Entry(khung)
nhap_he_so_c.grid(row=2, column=1)

nut_giai_pt_bac_nhat = Button(khung, text="Giải phương trình bậc nhất", command=giai_pt_bac_nhat)
nut_giai_pt_bac_nhat.grid(row=3, column=0)

nut_giai_pt_bac_hai = Button(khung, text="Giải phương trình bậc hai", command=giai_pt_bac_hai)
nut_giai_pt_bac_hai.grid(row=3, column=1)

goc.mainloop()