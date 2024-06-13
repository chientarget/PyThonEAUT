import sqlite3

def display_books_after_year(cursor, year):
    cursor.execute('SELECT * FROM Books WHERE DatePublished > ? ORDER BY DatePublished', (year,))
    books = cursor.fetchall()
    for book in books:
        print(book)

def main():
    connection = sqlite3.connect('BookInfo.db')
    cursor = connection.cursor()


    year = input("Mời nhập năm xuất bản:")
    display_books_after_year(cursor, year)
    connection.close()

if __name__ == "__main__":
    main()