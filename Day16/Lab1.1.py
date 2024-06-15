import mysql.connector

# Kết nối tới cơ sở dữ liệu MySQL
def connect_to_db():
    conn = mysql.connector.connect(
        host="localhost",
        port="3308",
        user="root",
        password="",
        database="ABC_University"
    )
    return conn

# Tạo bảng "students" nếu chưa tồn tại
def create_table():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            age INT,
            major VARCHAR(255),
            point VARCHAR(255),
            note VARCHAR(255)
        )
    """)
    conn.commit()
    conn.close()

# Thêm sinh viên mới vào bảng
def add_student(name, age, major, point, note):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, major, point, note) VALUES (%s, %s, %s, %s, %s)", (name, age, major, point, note))
    conn.commit()
    conn.close()

# Cập nhật thông tin sinh viên dựa trên ID
def update_student(id, name, age, major, point, note):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET name=%s, age=%s, major=%s, point=%s, note=%s WHERE id=%s", (name, age, major, point, note, id))
    conn.commit()
    conn.close()

# Xóa sinh viên dựa trên ID
def delete_student(id):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=%s", (id,))
    conn.commit()
    conn.close()

# Truy vấn tất cả sinh viên trong bảng
def query_all_students():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)
    conn.close()

# Truy vấn sinh viên theo tên hoặc chuyên ngành
def query_students_by_name_or_major(name=None, major=None):
    conn = connect_to_db()
    cursor = conn.cursor()
    if name and major:
        cursor.execute("SELECT * FROM students WHERE name=%s OR major=%s", (name, major))
    elif name:
        cursor.execute("SELECT * FROM students WHERE name=%s", (name,))
    elif major:
        cursor.execute("SELECT * FROM students WHERE major=%s", (major,))
    for row in cursor.fetchall():
        print(row)
    conn.close()

# Sắp xếp sinh viên theo tên
def sort_students_by_name():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students ORDER BY name")
    for row in cursor.fetchall():
        print(row)
    conn.close()

# Tìm kiếm sinh viên có cùng tên
def find_students_with_same_name(name):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name=%s", (name,))
    for row in cursor.fetchall():
        print(row)
    conn.close()

# Xóa toàn bộ sinh viên có ghi chú là "có"
def delete_students_with_note_có():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE note='có'")
    conn.commit()
    conn.close()

# Hiển thị danh sách sinh viên có cùng tuổi
def display_students_with_same_age(age):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE age=%s", (age,))
    for row in cursor.fetchall():
        print(row)
    conn.close()

# Tìm sinh viên có điểm cao nhất và thấp nhất
def find_highest_and_lowest_point():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students ORDER BY CAST(point AS UNSIGNED)")
    students = cursor.fetchall()
    print("Lowest Point:", students[0])
    print("Highest Point:", students[-1])
    conn.close()


# Tính tổng điểm toàn bộ sinh viên
def calculate_total_points():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(CAST(point AS UNSIGNED)) FROM students")
    total_points = cursor.fetchone()[0]
    print("Total Points:", total_points)
    conn.close()


def setup_database():
    create_table()
    students = [
        ("Nguyễn Văn A", 20, "Công nghệ thông tin", 8.5, "Có"),
        ("Trần Thị B", 21, "Toán học", 9.0, "Không"),
        ("Lê Văn C", 22, "Vật lý", 7.8, "Có"),
        ("Phạm Thị D", 23, "Kỹ thuật", 8.8, "Không"),
        ("Hoàng Ngọc E", 20, "Sinh học", 9.2, "Có")
    ]
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO students (name, age, major, point, note) VALUES (%s, %s, %s, %s, %s)", students)
    conn.commit()
    conn.close()



# Ví dụ sử dụng các chức năng
while True:
    print("\n--- Menu ---")
    print("1. Thêm sinh viên")
    print("2. Cập nhật thông tin sinh viên")
    print("3. Xóa sinh viên")
    print("4. Hiển thị tất cả sinh viên")
    print("5. Tìm kiếm sinh viên theo tên hoặc chuyên ngành")
    print("6. Sắp xếp sinh viên theo tên")
    print("7. Tìm kiếm sinh viên có cùng tên")
    print("8. Xóa sinh viên có ghi chú 'có'")
    print("9. Hiển thị sinh viên có cùng tuổi")
    print("10. Tìm sinh viên có điểm cao nhất và thấp nhất")
    print("11. Cập nhật điểm cho sinh viên")
    print("12. Tính tổng điểm của tất cả sinh viên")
    print("99.Setup database")
    print("0. Thoát")

    choice = input("Nhập lựa chọn của bạn (0-12): ")

    if choice == "1":
        name = input("Nhập tên: ")
        age = int(input("Nhập tuổi: "))
        major = input("Nhập chuyên ngành: ")
        point = input("Nhập điểm: ")
        note = input("Nhập ghi chú: ")
        add_student(name, age, major, point, note)
    elif choice == "2":
        id = int(input("Nhập ID sinh viên: "))
        name = input("Nhập tên mới: ")
        age = int(input("Nhập tuổi mới: "))
        major = input("Nhập chuyên ngành mới: ")
        point = input("Nhập điểm mới: ")
        note = input("Nhập ghi chú mới: ")
        update_student(id, name, age, major, point, note)
    elif choice == "3":
        id = int(input("Nhập ID sinh viên: "))
        delete_student(id)
    elif choice == "4":
        query_all_students()
    elif choice == "5":
        name = input("Nhập tên: ")
        major = input("Nhập chuyên ngành: ")
        query_students_by_name_or_major(name, major)
    elif choice == "6":
        sort_students_by_name()
    elif choice == "7":
        name = input("Nhập tên: ")
        find_students_with_same_name(name)
    elif choice == "8":
        delete_students_with_note_có()
    elif choice == "9":
        age = int(input("Nhập tuổi: "))
        display_students_with_same_age(age)
    elif choice == "10":
        find_highest_and_lowest_point()
    elif choice == "11":
        id = int(input("Nhập ID sinh viên: "))
        new_point = input("Nhập điểm mới: ")
    elif choice == "12":
        calculate_total_points()
    elif choice == "0":
        break
    elif choice == "99":
        setup_database()
    else:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại.")