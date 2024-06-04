from tkinter import *
import csv

def tao_file():
    global ten_file
    ten_file = nhap_ten_file.get()
    if not ten_file.endswith('.csv'):
        ten_file += '.csv'
    with open(ten_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age"])
    nhap_ten_file.delete(0, END)

def them_du_lieu():
    ten = nhap_ten.get()
    tuoi = nhap_tuoi.get()
    with open(ten_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([ten, tuoi])
    nhap_ten.delete(0, END)
    nhap_tuoi.delete(0, END)

def hien_thi_du_lieu():
    danh_sach.delete(0, END)
    with open(ten_file, 'r') as f:
        reader = csv.reader(f)
        headers = next(reader, None)  # get the headers
        for row in reader:
            for header, value in zip(headers, row):
                danh_sach.insert(END, f'{header}: {value}')  # format and insert each value

cua_so = Tk()
cua_so.title("Tạo và thêm dữ liệu vào file .csv")
cua_so.geometry("300x500")

nhap_ten_file_label = Label(cua_so, text="Nhập tên file:")
nhap_ten_file_label.pack()

nhap_ten_file = Entry(cua_so)
nhap_ten_file.pack()

nut_tao_file = Button(cua_so, text="Tạo file", command=tao_file)
nut_tao_file.pack()

nhap_ten_label = Label(cua_so, text="Nhập tên:")
nhap_ten_label.pack()

nhap_ten = Entry(cua_so)
nhap_ten.pack()

nhap_tuoi_label = Label(cua_so, text="Nhập tuổi:")
nhap_tuoi_label.pack()

nhap_tuoi = Entry(cua_so)
nhap_tuoi.pack()

nut_them = Button(cua_so, text="Thêm vào file", command=them_du_lieu)
nut_them.pack()

danh_sach = Listbox(cua_so)
danh_sach.pack()

nut_hien_thi = Button(cua_so, text="Hiển thị dữ liệu", command=hien_thi_du_lieu)
nut_hien_thi.pack()

cua_so.mainloop()