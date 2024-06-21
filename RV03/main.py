import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector
from datetime import date

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        port=3308,
        user="root",
        password="",
        database="library"
    )

# FỎM CRUD sách
def open_book_management():
    clear_right_frame()

    def them_sach():
        tieu_de = tieu_de_entry.get()
        tac_gia = tac_gia_entry.get()
        nam_xuat_ban = nam_xuat_ban_entry.get()

        if tieu_de and tac_gia and nam_xuat_ban:
            try:
                conn = connect_db()
                cursor = conn.cursor()
                cursor.execute("INSERT INTO books (title, author, publication_year) VALUES (%s, %s, %s)", (tieu_de, tac_gia, nam_xuat_ban))
                conn.commit()
                conn.close()
                messagebox.showinfo("Thành công", "Thêm sách thành công")
                load_data()
                clear_entries()
            except mysql.connector.Error as err:
                messagebox.showerror("Lỗi", f"Lỗi: {err}")
        else:
            messagebox.showwarning("Lỗi nhập liệu", "Vui lòng điền đầy đủ thông tin")

    def cap_nhat_sach():
        ma_sach = ma_sach_entry.get()
        tieu_de = tieu_de_entry.get()
        tac_gia = tac_gia_entry.get()
        nam_xuat_ban = nam_xuat_ban_entry.get()

        if ma_sach and tieu_de and tac_gia and nam_xuat_ban:
            try:
                conn = connect_db()
                cursor = conn.cursor()
                cursor.execute("UPDATE books SET title=%s, author=%s, publication_year=%s WHERE id=%s", (tieu_de, tac_gia, nam_xuat_ban, ma_sach))
                conn.commit()
                conn.close()
                messagebox.showinfo("Thành công", "Cập nhật sách thành công")
                load_data()
                clear_entries()
            except mysql.connector.Error as err:
                messagebox.showerror("Lỗi", f"Lỗi: {err}")
        else:
            messagebox.showwarning("Lỗi nhập liệu", "Vui lòng điền đầy đủ thông tin")

    def xoa_sach():
        ma_sach = ma_sach_entry.get()

        if ma_sach:
            try:
                conn = connect_db()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM books WHERE id=%s", (ma_sach,))
                conn.commit()
                conn.close()
                messagebox.showinfo("Thành công", "Xóa sách thành công")
                load_data()
                clear_entries()
            except mysql.connector.Error as err:
                messagebox.showerror("Lỗi", f"Lỗi: {err}")
        else:
            messagebox.showwarning("Lỗi nhập liệu", "Vui lòng nhập mã sách")

    def tim_kiem_sach():
        tieu_de = tieu_de_entry.get()
        clear_tree()
        if tieu_de:
            try:
                conn = connect_db()
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM books WHERE title LIKE %s", ('%' + tieu_de + '%',))
                books = cursor.fetchall()
                conn.close()

                for book in books:
                    tree.insert("", tk.END, values=book)
            except mysql.connector.Error as err:
                messagebox.showerror("Lỗi", f"Lỗi: {err}")
        else:
            messagebox.showwarning("Lỗi nhập liệu", "Vui lòng nhập tiêu đề sách")

    def clear_entries():
        ma_sach_entry.delete(0, tk.END)
        tieu_de_entry.delete(0, tk.END)
        tac_gia_entry.delete(0, tk.END)
        nam_xuat_ban_entry.delete(0, tk.END)

    def load_data():
        clear_tree()
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM books")
            books = cursor.fetchall()
            conn.close()
            for book in books:
                tree.insert("", tk.END, values=book)
        except mysql.connector.Error as err:
            messagebox.showerror("Lỗi", f"Lỗi: {err}")

    def clear_tree():
        for item in tree.get_children():
            tree.delete(item)

    form_frame = tk.Frame(right_frame, bg='#e8f6f3')
    form_frame.pack(pady=20)

    tk.Label(form_frame, text="Mã sách", bg='#e8f6f3').grid(row=0, column=0, padx=10, pady=5, sticky='w')
    ma_sach_entry = tk.Entry(form_frame)
    ma_sach_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(form_frame, text="Tiêu đề", bg='#e8f6f3').grid(row=1, column=0, padx=10, pady=5, sticky='w')
    tieu_de_entry = tk.Entry(form_frame)
    tieu_de_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(form_frame, text="Tác giả", bg='#e8f6f3').grid(row=2, column=0, padx=10, pady=5, sticky='w')
    tac_gia_entry = tk.Entry(form_frame)
    tac_gia_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(form_frame, text="Năm xuất bản", bg='#e8f6f3').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    nam_xuat_ban_entry = tk.Entry(form_frame)
    nam_xuat_ban_entry.grid(row=3, column=1, padx=10, pady=5)

    button_frame = tk.Frame(right_frame, bg='#e8f6f3')
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Thêm sách", command=them_sach, bg='#2ecc71', fg='white').grid(row=0, column=0, padx=10, pady=5)
    tk.Button(button_frame, text="Cập nhật sách", command=cap_nhat_sach, bg='#3498db', fg='white').grid(row=0, column=1, padx=10, pady=5)
    tk.Button(button_frame, text="Xóa sách", command=xoa_sach, bg='#e74c3c', fg='white').grid(row=0, column=2, padx=10, pady=5)
    tk.Button(button_frame, text="Tìm kiếm sách", command=tim_kiem_sach, bg='#f39c12', fg='white').grid(row=0, column=3, padx=10, pady=5)
    tk.Button(button_frame, text="Xóa các mục nhập", command=clear_entries, bg='#7f8c8d', fg='white').grid(row=1, column=1, padx=10, pady=5)

    tree_frame = tk.Frame(right_frame, bg='#e8f6f3')
    tree_frame.pack(pady=20)

    columns = ("ID", "Tiêu đề", "Tác giả", "Năm xuất bản", "Có sẵn")
    tree = ttk.Treeview(tree_frame, columns=columns, show='headings')
    tree.pack()

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')

    load_data()

# Form Mượn và trả sách
def open_borrow_return_management():
    clear_right_frame()

    def muon_sach():
        ma_sach = ma_sach_entry.get()
        ten_nguoi_muon = ten_nguoi_muon_entry.get()

        if ma_sach and ten_nguoi_muon:
            try:
                conn = connect_db()
                cursor = conn.cursor()
                cursor.execute("SELECT available FROM books WHERE id=%s", (ma_sach,))
                available = cursor.fetchone()[0]

                if available:
                    cursor.execute("INSERT INTO borrowings (book_id, user_name, borrow_date) VALUES (%s, %s, %s)", (ma_sach, ten_nguoi_muon, date.today()))
                    cursor.execute("UPDATE books SET available=FALSE WHERE id=%s", (ma_sach,))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Thành công", "Mượn sách thành công")
                    load_data()
                    clear_entries()
                else:
                    messagebox.showwarning("Không khả dụng", "Sách hiện không có sẵn")
            except mysql.connector.Error as err:
                messagebox.showerror("Lỗi", f"Lỗi: {err}")
        else:
            messagebox.showwarning("Lỗi nhập liệu", "Vui lòng nhập mã sách và tên người mượn")

    def tra_sach():
        ma_sach = ma_sach_entry.get()

        if ma_sach:
            try:
                conn = connect_db()
                cursor = conn.cursor()
                cursor.execute("UPDATE borrowings SET return_date=%s WHERE book_id=%s AND return_date IS NULL", (date.today(), ma_sach))
                cursor.execute("UPDATE books SET available=TRUE WHERE id=%s", (ma_sach,))
                conn.commit()
                conn.close()
                messagebox.showinfo("Thành công", "Trả sách thành công")
                load_data()
                clear_entries()
            except mysql.connector.Error as err:
                messagebox.showerror("Lỗi", f"Lỗi: {err}")
        else:
            messagebox.showwarning("Lỗi nhập liệu", "Vui lòng nhập mã sách")

    def clear_entries():
        ma_sach_entry.delete(0, tk.END)
        ten_nguoi_muon_entry.delete(0, tk.END)

    def load_data():
        for item in tree.get_children():
            tree.delete(item)
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT borrowings.id, books.title, borrowings.user_name, borrowings.borrow_date, borrowings.return_date 
                FROM borrowings 
                JOIN books ON borrowings.book_id = books.id
            """)
            borrowings = cursor.fetchall()
            conn.close()
            for borrowing in borrowings:
                tree.insert("", tk.END, values=borrowing)
        except mysql.connector.Error as err:
            messagebox.showerror("Lỗi", f"Lỗi: {err}")

    form_frame = tk.Frame(right_frame, bg='#e8f6f3')
    form_frame.pack(pady=20)

    tk.Label(form_frame, text="Mã sách", bg='#e8f6f3').grid(row=0, column=0, padx=10, pady=5, sticky='w')
    ma_sach_entry = tk.Entry(form_frame)
    ma_sach_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(form_frame, text="Tên người mượn", bg='#e8f6f3').grid(row=1, column=0, padx=10, pady=5, sticky='w')
    ten_nguoi_muon_entry = tk.Entry(form_frame)
    ten_nguoi_muon_entry.grid(row=1, column=1, padx=10, pady=5)

    button_frame = tk.Frame(right_frame, bg='#e8f6f3')
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Mượn sách", command=muon_sach, bg='#9b59b6', fg='white').grid(row=0, column=0, padx=10, pady=5)
    tk.Button(button_frame, text="Trả sách", command=tra_sach, bg='#1abc9c', fg='white').grid(row=0, column=1, padx=10, pady=5)
    tk.Button(button_frame, text="Xóa các mục nhập", command=clear_entries, bg='#7f8c8d', fg='white').grid(row=1, column=0, padx=10, pady=5)

    tree_frame = tk.Frame(right_frame, bg='#e8f6f3')
    tree_frame.pack(pady=20)

    columns = ("ID", "Tiêu đề", "Người mượn", "Ngày mượn", "Ngày trả")
    tree = ttk.Treeview(tree_frame, columns=columns, show='headings')
    tree.pack()

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')

    load_data()

# VIEW SÁCH ĐÃ MƯỢN
def open_view_borrowed_books():
    clear_right_frame()

    def load_data():
        for item in tree.get_children():
            tree.delete(item)
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT borrowings.id, books.title, borrowings.user_name, borrowings.borrow_date, borrowings.return_date 
                FROM borrowings 
                JOIN books ON borrowings.book_id = books.id
            """)
            borrowings = cursor.fetchall()
            conn.close()
            for borrowing in borrowings:
                tree.insert("", tk.END, values=borrowing)
        except mysql.connector.Error as err:
            messagebox.showerror("Lỗi", f"Lỗi: {err}")

    button_frame = tk.Frame(right_frame, bg='#e8f6f3')
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Tải lại danh sách", command=load_data, bg='#34495e', fg='white').grid(row=0, column=0, padx=10, pady=5)

    tree_frame = tk.Frame(right_frame, bg='#e8f6f3')
    tree_frame.pack(pady=20)

    columns = ("ID", "Tiêu đề", "Người mượn", "Ngày mượn", "Ngày trả")
    tree = ttk.Treeview(tree_frame, columns=columns, show='headings')
    tree.pack()

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')

    load_data()

# VIEW SÁCH ĐANG DĐƯỢC MƯỢN
def open_view_borrowing_books():
    clear_right_frame()

    def load_data():
        for item in tree.get_children():
            tree.delete(item)
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT books.id, books.title, books.author, books.publication_year 
                FROM books 
                JOIN borrowings ON books.id = borrowings.book_id 
                WHERE borrowings.return_date IS NULL
            """)
            borrowings = cursor.fetchall()
            conn.close()
            for borrowing in borrowings:
                tree.insert("", tk.END, values=borrowing)
        except mysql.connector.Error as err:
            messagebox.showerror("Lỗi", f"Lỗi: {err}")

    button_frame = tk.Frame(right_frame, bg='#e8f6f3')
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Tải lại danh sách", command=load_data, bg='#34495e', fg='white').grid(row=0, column=0, padx=10, pady=5)

    tree_frame = tk.Frame(right_frame, bg='#e8f6f3')
    tree_frame.pack(pady=20)

    columns = ("ID", "Tiêu đề", "Tác giả", "Năm xuất bản")
    tree = ttk.Treeview(tree_frame, columns=columns, show='headings')
    tree.pack()

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')

    load_data()

# VIEW SÁCH TỒN TẠI
def open_check_books():
    clear_right_frame()

    def load_data():
        for item in tree.get_children():
            tree.delete(item)
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM books WHERE available=TRUE")
            books = cursor.fetchall()
            conn.close()
            for book in books:
                tree.insert("", tk.END, values=book)
        except mysql.connector.Error as err:
            messagebox.showerror("Lỗi", f"Lỗi: {err}")

    button_frame = tk.Frame(right_frame, bg='#e8f6f3')
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Tải lại danh sách", command=load_data, bg='#3498db', fg='white').grid(row=0, column=0, padx=10, pady=5)

    tree_frame = tk.Frame(right_frame, bg='#e8f6f3')
    tree_frame.pack(pady=20)

    columns = ("ID", "Tiêu đề", "Tác giả", "Năm xuất bản", "Có sẵn")
    tree = ttk.Treeview(tree_frame, columns=columns, show='headings')
    tree.pack()

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')

    load_data()

# GỬI YẾU CẦU
def open_user_request():
    clear_right_frame()

    def gui_yeu_cau():
        ten_nguoi_muon = ten_nguoi_muon_entry.get()
        yeu_cau = yeu_cau_entry.get()

        if ten_nguoi_muon and yeu_cau:
            try:
                conn = connect_db()
                cursor = conn.cursor()
                cursor.execute("INSERT INTO user_requests (user_name, request, request_date) VALUES (%s, %s, %s)", (ten_nguoi_muon, yeu_cau, date.today()))
                conn.commit()
                conn.close()
                messagebox.showinfo("Thành công", "Gửi yêu cầu thành công")
                clear_entries()
            except mysql.connector.Error as err:
                messagebox.showerror("Lỗi", f"Lỗi: {err}")
        else:
            messagebox.showwarning("Lỗi nhập liệu", "Vui lòng nhập tên người mượn và yêu cầu")

    def load_data():
        for item in tree.get_children():
            tree.delete(item)
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM user_requests")
            requests = cursor.fetchall()
            conn.close()
            for request in requests:
                tree.insert("", tk.END, values=request)
        except mysql.connector.Error as err:
            messagebox.showerror("Lỗi", f"Lỗi: {err}")

    def clear_entries():
        ten_nguoi_muon_entry.delete(0, tk.END)
        yeu_cau_entry.delete(0, tk.END)

    form_frame = tk.Frame(right_frame, bg='#e8f6f3')
    form_frame.pack(pady=20)

    tk.Label(form_frame, text="Tên người mượn", bg='#e8f6f3').grid(row=0, column=0, padx=10, pady=5, sticky='w')
    ten_nguoi_muon_entry = tk.Entry(form_frame)
    ten_nguoi_muon_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(form_frame, text="Yêu cầu", bg='#e8f6f3').grid(row=1, column=0, padx=10, pady=5, sticky='w')
    yeu_cau_entry = tk.Entry(form_frame)
    yeu_cau_entry.grid(row=1, column=1, padx=10, pady=5)

    button_frame = tk.Frame(right_frame, bg='#e8f6f3')
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Gửi yêu cầu", command=gui_yeu_cau, bg='#e74c3c', fg='white').grid(row=0, column=0, padx=10, pady=5)
    tk.Button(button_frame, text="Tải lại danh sách", command=load_data, bg='#f39c12', fg='white').grid(row=0, column=1, padx=10, pady=5)

    tree_frame = tk.Frame(right_frame, bg='#e8f6f3')
    tree_frame.pack(pady=20)

    columns = ("ID", "Tên người mượn", "Yêu cầu", "Ngày yêu cầu")
    tree = ttk.Treeview(tree_frame, columns=columns, show='headings')
    tree.pack()

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')

    load_data()

# CLEAR right_frame
def clear_right_frame():
    for widget in right_frame.winfo_children():
        widget.destroy()


root = tk.Tk()
root.title("Hệ thống quản lý thư viện")
root.geometry("1000x600")
root.configure(bg='#e8f6f3')

left_frame = tk.Frame(root, bg='#34495e', width=200)
left_frame.pack(side=tk.LEFT, fill=tk.Y)

right_frame = tk.Frame(root, bg='#e8f6f3')
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

tk.Button(left_frame, text="Quản lý sách", command=open_book_management, bg='#2ecc71', fg='white', width=20).pack(pady=10)
tk.Button(left_frame, text="Mượn và Trả sách", command=open_borrow_return_management, bg='#3498db', fg='white', width=20).pack(pady=10)
tk.Button(left_frame, text="Xem thông tin sách đã mượn", command=open_view_borrowed_books, bg='#e74c3c', fg='white', width=20).pack(pady=10)
tk.Button(left_frame, text="Xem danh sách sách đang mượn", command=open_view_borrowing_books, bg='#f39c12', fg='white', width=20).pack(pady=10)
tk.Button(left_frame, text="Kiểm tra sách còn tồn", command=open_check_books, bg='#1abc9c', fg='white', width=20).pack(pady=10)
tk.Button(left_frame, text="Gửi yêu cầu", command=open_user_request, bg='#9b59b6', fg='white', width=20).pack(pady=10)
tk.Button(left_frame, text="Đóng", command=root.quit, bg='#e74c3c', fg='white', width=20).pack(pady=10)

root.mainloop()
