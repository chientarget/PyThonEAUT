import sqlite3

connection = sqlite3.connect('BookInfo.db')
cursor = connection.cursor()

cursor.execute('CREATE TABLE Authors (Name TEXT PRIMARY KEY, Birth TEXT )')
cursor.execute('CREATE TABLE Books (ID INTEGER PRIMARY KEY, Title TEXT, Author TEXT, DatePublished TEXT, FOREIGN KEY(Author) REFERENCES Authors(Name)   )')

authors = [
    ('Nguyen Nhat Anh', '1955'),
    ('To Hoai', '1920'),
    ('Nam Cao', '1915'),
]

books = [
    (1, 'Cho Toi Xin Mot Ve Di Tuoi Tho', 'Nguyen Nhat Anh', '1987'),
    (2, 'De Men Phieu Luu Ky', 'To Hoai', '1957'),
    (3, 'Truyen Kieu', 'Nam Cao', '1941'),
]

cursor.executemany('INSERT INTO Authors VALUES (?, ?)', authors)
cursor.executemany('INSERT INTO Books VALUES (?, ?, ?, ?)', books)

connection.commit()
connection.close()
