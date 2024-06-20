import sqlite3
import sys


# region CRUD Sẳn phẩm
def tao_bang():
    conn = sqlite3.connect('PYQT/quan_ly_ban_hang.db')
    cursor = conn.cursor()

    # Tạo bảng users
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    ''')

    # Tạo bảng products
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS san_pham (
        san_pham_id INTEGER PRIMARY KEY AUTOINCREMENT,
        ten_san_pham TEXT NOT NULL,
        gia REAL NOT NULL,
        so_luong INTEGER NOT NULL
    )
    ''')

    # Tạo bảng customers
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS khach_hang (
        khach_hang_id INTEGER PRIMARY KEY AUTOINCREMENT,
        ten_khach_hang TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        so_dien_thoai TEXT NOT NULL
    )
    ''')

    # Tạo bảng orders
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS don_hang (
        don_hang_id INTEGER PRIMARY KEY AUTOINCREMENT,
        khach_hang_id INTEGER,
        ngay_dat_hang TEXT,
        tong_tien REAL,
        FOREIGN KEY(khach_hang_id) REFERENCES khach_hang(khach_hang_id)
    )
    ''')

    # Tạo bảng order_items
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS chi_tiet_don_hang (
        chi_tiet_don_hang_id INTEGER PRIMARY KEY AUTOINCREMENT,
        don_hang_id INTEGER,
        san_pham_id INTEGER,
        so_luong INTEGER,
        FOREIGN KEY(don_hang_id) REFERENCES don_hang(don_hang_id),
        FOREIGN KEY(san_pham_id) REFERENCES san_pham(san_pham_id)
    )
    ''')

    # Tạo bảng feedback
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS phan_hoi (
        phan_hoi_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        noi_dung_phan_hoi TEXT,
        phan_hoi_lai TEXT,
        FOREIGN KEY(user_id) REFERENCES users(user_id)
    )
    ''')

    conn.commit()
    conn.close()
def them_san_pham(ten_san_pham, gia, so_luong):
    conn = sqlite3.connect('PYQT/quan_ly_ban_hang.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO san_pham (ten_san_pham, gia, so_luong) VALUES (?, ?, ?)
    ''', (ten_san_pham, gia, so_luong))
    conn.commit()
    conn.close()
def sua_san_pham(san_pham_id, ten_san_pham, gia, so_luong):
    conn = sqlite3.connect('PYQT/quan_ly_ban_hang.db')
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE san_pham SET ten_san_pham = ?, gia = ?, so_luong = ? WHERE san_pham_id = ?
    ''', (ten_san_pham, gia, so_luong, san_pham_id))
    conn.commit()
    conn.close()
def tim_kiem_san_pham(ten_san_pham):
    conn = sqlite3.connect('PYQT/quan_ly_ban_hang.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM san_pham WHERE ten_san_pham LIKE ?
    ''', ('%' + ten_san_pham + '%',))
    ket_qua = cursor.fetchall()
    conn.close()
    return ket_qua
def xoa_san_pham(san_pham_id):
    conn = sqlite3.connect('PYQT/quan_ly_ban_hang.db')
    cursor = conn.cursor()
    cursor.execute('''
    DELETE FROM san_pham WHERE san_pham_id = ?
    ''', (san_pham_id,))
    conn.commit()
    conn.close()


# tao_bang()
# xoa_san_pham(1)
# sua_san_pham(1, 'San pham cap nhat', 12.0, 150)
them_san_pham('San pham mau', 10.0, 100)
print(tim_kiem_san_pham('San pham'))

#end region CRUD Sẳn phẩm


# region CRUD Khách hàng
def them_khach_hang(ten_khach_hang, email, so_dien_thoai):
    conn = sqlite3.connect('PYQT/quan_ly_ban_hang.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO khach_hang (ten_khach_hang, email, so_dien_thoai) VALUES (?, ?, ?)
    ''', (ten_khach_hang, email, so_dien_thoai))
    conn.commit()
    conn.close()
def sua_khach_hang(khach_hang_id, ten_khach_hang, email, so_dien_thoai):
    conn = sqlite3.connect('PYQT/quan_ly_ban_hang.db')
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE khach_hang SET ten_khach_hang = ?, email = ?, so_dien_thoai = ? WHERE khach_hang_id = ?
    ''', (ten_khach_hang, email, so_dien_thoai, khach_hang_id))
    conn.commit()
    conn.close()
def xoa_khach_hang(khach_hang_id):
    conn = sqlite3.connect('PYQT/quan_ly_ban_hang.db')
    cursor = conn.cursor()
    cursor.execute('''
    DELETE FROM khach_hang WHERE khach_hang_id = ?
    ''', (khach_hang_id,))
    conn.commit()
    conn.close()
def tim_kiem_khach_hang(ten_khach_hang):
    conn = sqlite3.connect('PYQT/quan_ly_ban_hang.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM khach_hang WHERE ten_khach_hang LIKE ?
    ''', ('%' + ten_khach_hang + '%',))
    ket_qua = cursor.fetchall()
    conn.close()
    return ket_qua

print(tim_kiem_khach_hang('Nguyen'))
# xoa_khach_hang(1)
them_khach_hang('Nguyen Van A', 'a@example.com', '0123456789')
# sua_khach_hang(1, 'Nguyen Van B', 'b@example.com', '0987654321')



# endregion CRUD Khách hàng


# region CRUD Đơn hàng
def tao_don_hang(khach_hang_id, ngay_dat_hang, tong_tien):
    conn = sqlite3.connect('PYQT/quan_ly_ban_hang.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO don_hang (khach_hang_id, ngay_dat_hang, tong_tien) VALUES (?, ?, ?)
    ''', (khach_hang_id, ngay_dat_hang, tong_tien))
    don_hang_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return don_hang_id
def cap_nhat_don_hang(don_hang_id, khach_hang_id, ngay_dat_hang, tong_tien):
    conn = sqlite3.connect('PYQT/quan_ly_ban_hang.db')
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE don_hang SET khach_hang_id = ?, ngay_dat_hang = ?, tong_tien = ? WHERE don_hang_id = ?
    ''', (khach_hang_id, ngay_dat_hang, tong_tien, don_hang_id))
    conn.commit()
    conn.close()
def them_phan_hoi(user_id, noi_dung_phan_hoi):
    conn = sqlite3.connect('PYQT/quan_ly_ban_hang.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO phan_hoi (user_id, noi_dung_phan_hoi) VALUES (?, ?)
    ''', (user_id, noi_dung_phan_hoi))
    conn.commit()
    conn.close()
def cap_nhat_phan_hoi(phan_hoi_id, phan_hoi_lai):
    conn = sqlite3.connect('PYQT/quan_ly_ban_hang.db')
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE phan_hoi SET phan_hoi_lai = ? WHERE phan_hoi_id = ?
    ''', (phan_hoi_lai, phan_hoi_id))
    conn.commit()
    conn.close()

# cap_nhat_phan_hoi(1, 'Phan hoi da duoc tiep nhan.')
don_hang_id = tao_don_hang(1, '2024-06-20', 100.0)
# cap_nhat_don_hang(don_hang_id, 1, '2024-06-21', 120.0)
them_phan_hoi(1, 'Day la mot phan hoi.')


# endregion CRUD Đơn hàng




