# Bài 3: Tạo một chương trình đơn giản hiển thị một danh sách thả xuống chứa một số màu sắc và một nút Click Me.
# Khi người dùng chọn một màu từ danh sách và nhấp vào nút, nó nên thay đổi màu nền của cửa sổ thành màu đó.
# Để thách thức thêm, hãy cố gắng tránh sử dụng câu lệnh if để làm điều này.


import tkinter as tk

def thay_doi_mau_nen():
    mau = danh_sach_mau.get()
    goc.configure(bg=mau)

goc = tk.Tk()
goc.geometry("300x300")
goc.title("Thay đổi màu nền")

# Tạo danh sách màu
cac_mau = ["red", "blue", "green", "yellow", "pink", "orange"]
danh_sach_mau = tk.StringVar(goc)
danh_sach_mau.set(cac_mau[0])

# Tạo menu thả xuống
menu_tha_xuong = tk.OptionMenu(goc, danh_sach_mau, *cac_mau)
menu_tha_xuong.pack()


nut_nhan = tk.Button(goc, text="Click Me", command=thay_doi_mau_nen)
nut_nhan.pack()

goc.mainloop()