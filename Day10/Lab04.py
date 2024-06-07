import tkinter as tk

def hien_thi_thong_tin_san_pham():
    ten_san_pham = nhap_ten.get()
    gia_san_pham = nhap_gia.get()
    mo_ta_san_pham = nhap_mo_ta.get("1.0", "end-1c")

    van_ban_thong_tin.delete("1.0", "end")
    van_ban_thong_tin.insert("1.0", f"Tên sản phẩm: {ten_san_pham}\n")
    van_ban_thong_tin.insert("end", f"Giá: {gia_san_pham}\n")
    van_ban_thong_tin.insert("end", f"Mô tả: {mo_ta_san_pham}")

goc = tk.Tk()
goc.title("Thông tin sản phẩm")

nhap_ten_label = tk.Label(goc, text="Tên sản phẩm:")
nhap_ten_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
nhap_ten = tk.Entry(goc)
nhap_ten.grid(row=0, column=1, padx=5, pady=5)

nhap_gia_label = tk.Label(goc, text="Giá:")
nhap_gia_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
nhap_gia = tk.Entry(goc)
nhap_gia.grid(row=1, column=1, padx=5, pady=5)

nhap_mo_ta_label = tk.Label(goc, text="Mô tả:")
nhap_mo_ta_label.grid(row=2, column=0, padx=5, pady=5, sticky="nw")
nhap_mo_ta = tk.Text(goc, height=5, width=30)
nhap_mo_ta.grid(row=2, column=1, padx=5, pady=5)

nut_hien_thi = tk.Button(goc, text="Hiển thị thông tin", command=hien_thi_thong_tin_san_pham)
nut_hien_thi.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

van_ban_thong_tin = tk.Text(goc, height=10, width=40)
van_ban_thong_tin.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

goc.mainloop()