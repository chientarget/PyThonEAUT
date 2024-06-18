import tkinter as tk
from tkinter import messagebox, font
import requests
from bs4 import BeautifulSoup

# Định nghĩa URL và ID phần tử cho mỗi chủ đề
thong_tin_chu_de = {
    "Python Comments": {"url": "https://www.w3schools.com/python/python_comments.asp", "element_id": "main"},
    "Python Variables": {"url": "https://www.w3schools.com/python/python_variables.asp", "element_id": "main"},
    "Python Data Types": {"url": "https://www.w3schools.com/python/python_datatypes.asp", "element_id": "main"},
    "Python Strings": {"url": "https://www.w3schools.com/python/python_strings.asp", "element_id": "main"},
    "Python Lists": {"url": "https://www.w3schools.com/python/python_lists.asp", "element_id": "main"},
    "Python Tuples": {"url": "https://www.w3schools.com/python/python_tuples.asp", "element_id": "main"},
    "Python Sets": {"url": "https://www.w3schools.com/python/python_sets.asp", "element_id": "main"},
    "Python Dictionaries": {"url": "https://www.w3schools.com/python/python_dictionaries.asp", "element_id": "main"},
    "Python If ... Else": {"url": "https://www.w3schools.com/python/python_conditions.asp", "element_id": "main"},
    "Python While Loops": {"url": "https://www.w3schools.com/python/python_while_loops.asp", "element_id": "main"},
    "Python For Loops": {"url": "https://www.w3schools.com/python/python_for_loops.asp", "element_id": "main"},
    "Python Functions": {"url": "https://www.w3schools.com/python/python_functions.asp", "element_id": "main"},
    "Python Classes and Objects": {"url": "https://www.w3schools.com/python/python_classes.asp", "element_id": "main"}
}

def lay_va_hien_thi_thong_tin(url, element_id):
    try:
        phan_hoi = requests.get(url)
        phan_hoi.raise_for_status()
        sup = BeautifulSoup(phan_hoi.text, 'html.parser')
        vi_du = sup.find_all(class_="w3-example")
        if vi_du:
            van_ban_thong_tin.delete(1.0, tk.END)
            for vd in vi_du:
                van_ban_thong_tin.insert(tk.END, vd.get_text() + "\n\n")
        else:
            van_ban_thong_tin.delete(1.0, tk.END)
            van_ban_thong_tin.insert(tk.END, "Không tìm thấy nội dung")
    except requests.RequestException as e:
        messagebox.showerror("Lỗi", f"Không thể lấy dữ liệu: {e}")

def hien_thi_thong_tin(chu_de):
    thong_tin = thong_tin_chu_de.get(chu_de)
    if thong_tin:
        lay_va_hien_thi_thong_tin(thong_tin["url"], thong_tin["element_id"])
    else:
        van_ban_thong_tin.delete(1.0, tk.END)
        van_ban_thong_tin.insert(tk.END, "Không có ví dụ")

def thoat_ung_dung():
    goc.destroy()

goc = tk.Tk()
goc.title("Hướng dẫn Python")
goc.geometry("1500x800")

# Đặt màu sắc để phù hợp với W3Schools
goc.configure(bg="#D9EEE1")  # Màu nền
font_tieu_de = font.Font(family="Verdana", size=20, weight="bold")
font_nut = font.Font(family="Verdana", size=12)
font_van_ban = font.Font(family="Consolas", size=14)

# Tiêu đề
nhan_tieu_de = tk.Label(goc, text="HƯỚNG DẪN PYTHON", font=font_tieu_de, bg="#D9EEE1", fg="#4CAF50")
nhan_tieu_de.pack(pady=10)

# Khung cho các nút
khung_nut = tk.Frame(goc, bg="#D9EEE1")
khung_nut.pack(side=tk.LEFT, padx=10, fill=tk.Y)

# Khu vực hiển thị thông tin với thanh cuộn
khung_thong_tin = tk.Frame(goc, relief=tk.RAISED, borderwidth=2, bg="#D9EEE1")
khung_thong_tin.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

thanh_cuon = tk.Scrollbar(khung_thong_tin, bg="#D9EEE1")
thanh_cuon.pack(side=tk.RIGHT, fill=tk.Y)

van_ban_thong_tin = tk.Text(khung_thong_tin, wrap=tk.WORD, font=font_van_ban, yscrollcommand=thanh_cuon.set, bg="#F1F1F1")
van_ban_thong_tin.pack(fill=tk.BOTH, expand=True)
thanh_cuon.config(command=van_ban_thong_tin.yview)

# Danh sách các chủ đề
chu_de = [
    "Python Comments", "Python Variables", "Python Data Types", "Python Strings",
    "Python Lists", "Python Tuples", "Python Sets", "Python Dictionaries",
    "Python If ... Else", "Python While Loops", "Python For Loops",
    "Python Functions", "Python Classes and Objects"
]

# Tạo nút cho mỗi chủ đề
for cd in chu_de:
    nut = tk.Button(khung_nut, text=cd, font=font_nut, width=20, bg="#4CAF50", fg="#FFFFFF",
                    command=lambda t=cd: hien_thi_thong_tin(t))
    nut.pack(pady=5)

# Nút thoát
nut_thoat = tk.Button(goc, text="Thoát", font=font_nut, width=10, bg="#4CAF50", fg="#FFFFFF", command=thoat_ung_dung)
nut_thoat.pack(side=tk.BOTTOM, pady=10)

goc.mainloop()