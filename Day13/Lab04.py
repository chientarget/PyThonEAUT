import sqlite3

def View_TacGia(cursor):
    cursor.execute('SELECT * FROM Authors')
    authors = cursor.fetchall()
    for author in authors:
        print(author)

def View_Sach(cursor, birthplace):
    cursor.execute('SELECT Books.Title, Books.DatePublished, Authors.Name FROM Books INNER JOIN Authors ON Books.Author = Authors.Name WHERE Authors.Birth = ?', (birthplace,))
    books = cursor.fetchall()
    for book in books:
        print(book)

def main():
    connection = sqlite3.connect('BookInfo.db')
    cursor = connection.cursor()

    View_TacGia(cursor)

    birthplace = input("Mời nhập năm sinh của tác giả:")

    View_Sach(cursor, birthplace)

    connection.close()

if __name__ == "__main__":
    main()