import sqlite3
from tkinter import *
from tkinter import messagebox

# Connect to SQLite database
conn = sqlite3.connect('thong_tin_sinh_vien.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS thong_tin_ca_nhan (
    id INTEGER PRIMARY KEY,
    ho_ten TEXT,
    tuoi INTEGER,
    lop TEXT,
    ma_sinh_vien TEXT,
    nam_hoc TEXT,
    thanh_tich TEXT,
    so_thich TEXT,
    ghi_chu TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS diem_mon_hoc (
    ma_sinh_vien INTEGER,
    toan REAL,
    ly REAL,
    hoa REAL,
    van REAL,
    su REAL,
    dia REAL,
    cong_dan REAL,
    FOREIGN KEY(ma_sinh_vien) REFERENCES thong_tin_ca_nhan(id)
)
''')

conn.commit()

# Functions for database operations
def them_thong_tin_ca_nhan(ho_ten, tuoi, lop, ma_sinh_vien, nam_hoc, thanh_tich, so_thich, ghi_chu):
    cursor.execute('''
    INSERT INTO thong_tin_ca_nhan (ho_ten, tuoi, lop, ma_sinh_vien, nam_hoc, thanh_tich, so_thich, ghi_chu)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (ho_ten, tuoi, lop, ma_sinh_vien, nam_hoc, thanh_tich, so_thich, ghi_chu))
    conn.commit()

def sua_thong_tin_ca_nhan(ma_sinh_vien, **kwargs):
    fields = ", ".join([f"{key} = ?" for key in kwargs])
    values = list(kwargs.values())
    values.append(ma_sinh_vien)
    cursor.execute(f'''
    UPDATE thong_tin_ca_nhan SET {fields} WHERE ma_sinh_vien = ?
    ''', values)
    conn.commit()

def xoa_thong_tin_ca_nhan(ma_sinh_vien):
    cursor.execute('''
    DELETE FROM thong_tin_ca_nhan WHERE ma_sinh_vien = ?
    ''', (ma_sinh_vien,))
    conn.commit()

def them_diem_mon_hoc(ma_sinh_vien, toan, ly, hoa, van, su, dia, cong_dan):
    cursor.execute('''
    INSERT INTO diem_mon_hoc (ma_sinh_vien, toan, ly, hoa, van, su, dia, cong_dan)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (ma_sinh_vien, toan, ly, hoa, van, su, dia, cong_dan))
    conn.commit()

def tim_sinh_vien_diem_cao_nhat():
    cursor.execute('''
    SELECT ma_sinh_vien FROM diem_mon_hoc
    WHERE (toan + ly + hoa + van + su + dia + cong_dan)/7 > 8
    ''')
    return cursor.fetchall()

def tim_sinh_vien_diem_thap_nhat():
    cursor.execute('''
    SELECT ma_sinh_vien FROM diem_mon_hoc
    WHERE (toan + ly + hoa + van + su + dia + cong_dan)/7 < 5
    ''')
    return cursor.fetchall()

def tim_sinh_vien_diem_trung_binh_duoi_5():
    cursor.execute('''
    SELECT ma_sinh_vien FROM diem_mon_hoc
    WHERE (toan + ly + hoa + van + su + dia + cong_dan)/7 < 5
    ''')
    return cursor.fetchall()

def them_ghi_chu_thi_lai():
    sinh_vien_diem_thap = tim_sinh_vien_diem_trung_binh_duoi_5()
    for sinh_vien in sinh_vien_diem_thap:
        cursor.execute('''
        UPDATE thong_tin_ca_nhan SET ghi_chu = 'Thi Lai' WHERE id = ?
        ''', (sinh_vien[0],))
    conn.commit()

def tim_sinh_vien_khong_mon_duoi_7():
    cursor.execute('''
    SELECT ma_sinh_vien FROM diem_mon_hoc
    WHERE toan >= 7 AND ly >= 7 AND hoa >= 7 AND van >= 7 AND su >= 7 AND dia >= 7 AND cong_dan >= 7
    ''')
    return cursor.fetchall()

def tim_sinh_vien_khong_mon_tren_8():
    cursor.execute('''
    SELECT ma_sinh_vien FROM diem_mon_hoc
    WHERE toan < 8 AND ly < 8 AND hoa < 8 AND van < 8 AND su < 8 AND dia < 8 AND cong_dan < 8
    ''')
    return cursor.fetchall()

def sua_thi_lai_sinh_vien():
    cursor.execute('''
    UPDATE thong_tin_ca_nhan SET ghi_chu = 'Thi Lai'
    WHERE id IN (SELECT ma_sinh_vien FROM diem_mon_hoc WHERE toan = 3 AND ly = 3 AND hoa = 3)
    ''')
    conn.commit()

def xoa_du_lieu_sinh_vien(ma_sinh_vien):
    cursor.execute('''
    DELETE FROM diem_mon_hoc WHERE ma_sinh_vien = ?
    ''', (ma_sinh_vien,))
    cursor.execute('''
    DELETE FROM thong_tin_ca_nhan WHERE id = ?
    ''', (ma_sinh_vien,))
    conn.commit()

def dong_chuong_trinh():
    conn.close()
    root.quit()

# Tkinter GUI setup
root = Tk()
root.title("He thong thong tin sinh vien")
root.geometry("500x500")

# Personal Information Form
def form_thong_tin_ca_nhan():
    form = Toplevel(root)
    form.title("Thong tin ca nhan")
    form.geometry("500x500")

    Label(form, text="Ho ten").grid(row=0, column=0)
    ho_ten = Entry(form)
    ho_ten.grid(row=0, column=1)

    Label(form, text="Tuoi").grid(row=1, column=0)
    tuoi = Entry(form)
    tuoi.grid(row=1, column=1)

    Label(form, text="Lop").grid(row=2, column=0)
    lop = Entry(form)
    lop.grid(row=2, column=1)

    Label(form, text="Ma sinh vien").grid(row=3, column=0)
    ma_sinh_vien = Entry(form)
    ma_sinh_vien.grid(row=3, column=1)

    Label(form, text="Nam hoc").grid(row=4, column=0)
    nam_hoc = Entry(form)
    nam_hoc.grid(row=4, column=1)

    Label(form, text="Thanh tich").grid(row=5, column=0)
    thanh_tich = Entry(form)
    thanh_tich.grid(row=5, column=1)

    Label(form, text="So thich").grid(row=6, column=0)
    so_thich = Entry(form)
    so_thich.grid(row=6, column=1)

    Label(form, text="Ghi chu").grid(row=7, column=0)
    ghi_chu = Entry(form)
    ghi_chu.grid(row=7, column=1)

    def luu_thong_tin_ca_nhan():
        them_thong_tin_ca_nhan(ho_ten.get(), tuoi.get(), lop.get(), ma_sinh_vien.get(), nam_hoc.get(), thanh_tich.get(), so_thich.get(), ghi_chu.get())
        messagebox.showinfo("Success", "Thong tin ca nhan da duoc luu!")
        form.destroy()

    Button(form, text="Luu", command=luu_thong_tin_ca_nhan).grid(row=8, column=1)

# Subject Scores Form
def form_diem_mon_hoc():
    form = Toplevel(root)
    form.title("Diem mon hoc")
    form.geometry("500x500")

    Label(form, text="Ma sinh vien").grid(row=0, column=0)
    ma_sinh_vien = Entry(form)
    ma_sinh_vien.grid(row=0, column=1)

    Label(form, text="Toan").grid(row=1, column=0)
    toan = Entry(form)
    toan.grid(row=1, column=1)

    Label(form, text="Ly").grid(row=2, column=0)
    ly = Entry(form)
    ly.grid(row=2, column=1)

    Label(form, text="Hoa").grid(row=3, column=0)
    hoa = Entry(form)
    hoa.grid(row=3, column=1)

    Label(form, text="Van").grid(row=4, column=0)
    van = Entry(form)
    van.grid(row=4, column=1)

    Label(form, text="Su").grid(row=5, column=0)
    su = Entry(form)
    su.grid(row=5, column=1)

    Label(form, text="Dia").grid(row=6, column=0)
    dia = Entry(form)
    dia.grid(row=6, column=1)

    Label(form, text="Cong dan").grid(row=7, column=0)
    cong_dan = Entry(form)
    cong_dan.grid(row=7, column=1)

    def luu_diem_mon_hoc():
        them_diem_mon_hoc(ma_sinh_vien.get(), float(toan.get()), float(ly.get()), float(hoa.get()), float(van.get()), float(su.get()), float(dia.get()), float(cong_dan.get()))
        messagebox.showinfo("Success", "Diem mon hoc da duoc luu!")
        form.destroy()

    Button(form, text="Luu", command=luu_diem_mon_hoc).grid(row=8, column=1)

# Query Functions
def chay_truy_van():
    form = Toplevel(root)
    form.title("Truy van")
    form.geometry("500x500")

    def hien_ket_qua(results):
        result_form = Toplevel(form)
        result_form.title("Ket qua truy van")
        result_text = Text(result_form)
        result_text.pack()
        for result in results:
            result_text.insert(END, f"Ma sinh vien: {result[0]}\n")

    Button(form, text="Diem cao nhat", command=lambda: hien_ket_qua(tim_sinh_vien_diem_cao_nhat())).pack()
    Button(form, text="Diem thap nhat", command=lambda: hien_ket_qua(tim_sinh_vien_diem_thap_nhat())).pack()
    Button(form, text="Diem trung binh duoi 5", command=lambda: hien_ket_qua(tim_sinh_vien_diem_trung_binh_duoi_5())).pack()
    Button(form, text="Them ghi chu Thi Lai", command=them_ghi_chu_thi_lai).pack()
    Button(form, text="Khong mon duoi 7", command=lambda: hien_ket_qua(tim_sinh_vien_khong_mon_duoi_7())).pack()
    Button(form, text="Khong mon tren 8", command=lambda: hien_ket_qua(tim_sinh_vien_khong_mon_tren_8())).pack()
    Button(form, text="Sua thi lai sinh vien", command=sua_thi_lai_sinh_vien).pack()

# Main GUI
Button(root, text="Nhap thong tin ca nhan", command=form_thong_tin_ca_nhan).pack()
Button(root, text="Nhap diem mon hoc", command=form_diem_mon_hoc).pack()
Button(root, text="Chay truy van", command=chay_truy_van).pack()
Button(root, text="Dong chuong trinh", command=dong_chuong_trinh).pack()

root.mainloop()
