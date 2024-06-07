# Bài 4: Tạo một chương trình sẽ yêu cầu người dùng nhập tên và sau đó chọn giới tính cho người đó từ một danh sách thả xuống.
# Sau đó, nó sẽ thêm tên và giới tính (được phân tách bằng dấu phẩy) vào một hộp danh sách khi người dùng nhấp vào một nút.

import tkinter as tk

def them_vao_danh_sach():
    ten = nhap_ten.get()
    gioi_tinh = danh_sach_gioi_tinh.get()
    danh_sach.insert(tk.END, f"{ten}, {gioi_tinh}")

goc = tk.Tk()
goc.geometry("500x500")
goc.title("Nhập tên và giới tính")

# Tạo trường nhập tên
nhap_ten = tk.Entry(goc)
nhap_ten.pack()

# Tạo danh sách giới tính
cac_gioi_tinh = ["Nam", "Nữ", "Khác"]
danh_sach_gioi_tinh = tk.StringVar(goc)
danh_sach_gioi_tinh.set(cac_gioi_tinh[0])

# Tạo menu thả xuống
menu_tha_xuong = tk.OptionMenu(goc, danh_sach_gioi_tinh, *cac_gioi_tinh)
menu_tha_xuong.pack()

# Tạo nút nhấn
nut_nhan = tk.Button(goc, text="Thêm vào danh sách", command=them_vao_danh_sach)
nut_nhan.pack()

# Tạo hộp danh sách
danh_sach = tk.Listbox(goc)
danh_sach.pack()

goc.mainloop()