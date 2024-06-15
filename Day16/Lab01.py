import mysql.connector

# Kết nối tới cơ sở dữ liệu MySQL
def connect_to_db():
    conn = mysql.connector.connect(
        host="localhost",
        port="3306",
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

# Thay điểm một sinh viên bất kỳ
def update_random_student_point(id, new_point):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET point=%s WHERE id=%s", (new_point, id))
    conn.commit()
    conn.close()

# Tính tổng điểm toàn bộ sinh viên
def calculate_total_points():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(CAST(point AS UNSIGNED)) FROM students")
    total_points = cursor.fetchone()[0]
    print("Total Points:", total_points)
    conn.close()

# Tạo bảng và thêm dữ liệu ban đầu
def setup_database():
    create_table()
    students = [
        ("Alice", 20, "Computer Science", "85", "có"),
        ("Bob", 21, "Mathematics", "90", "không"),
        ("Charlie", 22, "Physics", "78", "có"),
        ("David", 23, "Engineering", "88", "không"),
        ("Eve", 20, "Biology", "92", "có")
    ]
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO students (name, age, major, point, note) VALUES (%s, %s, %s, %s, %s)", students)
    conn.commit()
    conn.close()

# Thực hiện thiết lập cơ sở dữ liệu ban đầu
setup_database()

# Ví dụ sử dụng các chức năng
add_student("Frank", 24, "Chemistry", "80", "không")
update_student(1, "Alice", 21, "Computer Science", "86", "không")
delete_student(2)
query_all_students()
query_students_by_name_or_major(name="Charlie")
sort_students_by_name()
find_students_with_same_name("Alice")
delete_students_with_note_có()
display_students_with_same_age(20)
find_highest_and_lowest_point()
update_random_student_point(3, "95")
calculate_total_points()
