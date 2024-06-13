import sqlite3

def xem_danh_ba(conn):
    conn.execute('SELECT * FROM Name')
    cac_hang = conn.fetchall()
    for hang in cac_hang:
        print(hang)

def them_nguoi(conn, ket_noi):
    id = int(input("Nhập ID: "))
    ho = input("Nhập tên đệm: ")
    ten = input("Nhập tên: ")
    so_dien_thoai = input("Nhập số điện thoại: ")
    conn.execute('INSERT INTO Name VALUES (?, ?, ?, ?)', (id, ho, ten, so_dien_thoai))
    ket_noi.commit()

def tim_kiem_theo_ten_dem(conn):
    ho = input("Nhập tên đệm: ")
    conn.execute('SELECT * FROM Name WHERE Ho = ?', (ho,))
    cac_hang = conn.fetchall()
    for hang in cac_hang:
        print(hang)

def xoa_ban_ghi(conn, ket_noi):
    id = int(input("Nhập ID cần xóa: "))
    conn.execute('DELETE FROM Name WHERE ID = ?', (id,))
    ket_noi.commit()

def chinh():
    ket_noi = sqlite3.connect('PhoneBook.db')
    conn = ket_noi.cursor()

    while True:
        print("1. Xem danh bạ")
        print("2. Thêm người mới")
        print("3. Tìm kiếm theo họ")
        print("4. Xóa bản ghi theo ID")
        print("5. Thoát")
        lua_chon = int(input("Nhập lựa chọn của bạn: "))

        if lua_chon == 1:
            xem_danh_ba(conn)
        elif lua_chon == 2:
            them_nguoi(conn, ket_noi)
        elif lua_chon == 3:
            tim_kiem_theo_ten_dem(conn)
        elif lua_chon == 4:
            xoa_ban_ghi(conn, ket_noi)
        elif lua_chon == 5:
            print("Đang thoát chương trình...")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập một số từ 1 đến 5.")

    ket_noi.close()

if __name__ == "__main__":
    chinh()