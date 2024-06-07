# Ex5: Change program Ex4 so that when a new name and gender is added to the list box it is also written to a text file.
# Add another button that will display the entire text file in the main Python shell window.


import tkinter as tk

def them_vao_danh_sach_va_ghi_file():
    ten = nhap_ten.get()
    gioi_tinh = danh_sach_gioi_tinh.get()
    danh_sach.insert(tk.END, f"{ten}, {gioi_tinh}")
    with open('danh_sach.txt', 'a') as f:
        f.write(f"{ten}, {gioi_tinh}\n")

def hien_thi_file():
    danh_sach.delete(0, tk.END)  # Xóa nội dung hiện tại của danh sách
    with open('danh_sach.txt', 'r') as f:
        for dong in f:
            danh_sach.insert(tk.END, dong.strip())  # Thêm từng dòng vào danh sách

goc = tk.Tk()
goc.geometry("500x500")
goc.title("Nhập tên và giới tính")

nhap_ten = tk.Entry(goc)
nhap_ten.pack()

cac_gioi_tinh = ["Nam", "Nữ", "Khác"]
danh_sach_gioi_tinh = tk.StringVar(goc)
danh_sach_gioi_tinh.set(cac_gioi_tinh[0])

menu_tha_xuong = tk.OptionMenu(goc, danh_sach_gioi_tinh, *cac_gioi_tinh)
menu_tha_xuong.pack()

nut_nhan = tk.Button(goc, text="Thêm vào danh sách", command=them_vao_danh_sach_va_ghi_file)
nut_nhan.pack()

nut_hien_thi = tk.Button(goc, text="Hiển thị file", command=hien_thi_file)
nut_hien_thi.pack()

danh_sach = tk.Listbox(goc)
danh_sach.pack()


goc.mainloop()