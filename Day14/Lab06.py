import sqlite3

def luu_sach_cua_tac_gia_vao_file(con_tro, ten_tac_gia, ten_file):
    con_tro.execute('SELECT * FROM Books WHERE Author = ?', (ten_tac_gia,))
    sach = con_tro.fetchall()

    with open(ten_file, 'w') as f:
        for sach in sach:
            f.write('-'.join(str(truong) for truong in sach))
            f.write('\n')

def main():
    ket_noi = sqlite3.connect('BookInfo.db')
    conn = ket_noi.cursor()

    ten_tac_gia = input("Nhập tên tác giả: ")
    ten_file = 'sach_cua_tac_gia.txt'

    luu_sach_cua_tac_gia_vao_file(conn, ten_tac_gia, ten_file)

    ket_noi.close()

    # Mở file để kiểm tra nội dung
    with open(ten_file, 'r') as f:
        print(f.read())

if __name__ == "__main__":
    main()