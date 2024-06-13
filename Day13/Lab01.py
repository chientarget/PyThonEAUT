import sqlite3


ket_noi = sqlite3.connect('PhoneBook.db')
conn = ket_noi.cursor()

du_lieu = [
    (1, 'Nguyen', 'Van A', '0123456789'),
    (2, 'Tran', 'Van B', '0987654321'),
    (3, 'Le', 'Van C', '0123456789'),
    (4, 'Pham', 'Van D', '0987654321'),
    (5, 'Hoang', 'Van E', '0123456789')
]

conn.execute('CREATE TABLE Name (ID INTEGER PRIMARY KEY, Ho TEXT, Ten TEXT, SoDienThoai TEXT)')
conn.executemany('INSERT INTO Name VALUES (?, ?, ?, ?)', du_lieu)
ket_noi.commit()
