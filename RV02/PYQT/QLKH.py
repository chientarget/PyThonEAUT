import sys
import sqlite3
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget,
    QPushButton, QLineEdit, QMessageBox, QHeaderView, QLabel, QHBoxLayout
)

class CustomerManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Customer Manager")
        self.setGeometry(100, 100, 800, 600)

        # Kết nối đến cơ sở dữ liệu
        self.conn = sqlite3.connect('quan_ly_ban_hang.db')
        self.cursor = self.conn.cursor()

        # Tạo bảng hiển thị danh sách khách hàng
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Tên khách hàng", "Email", "Số điện thoại"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Tạo ô nhập liệu và nhãn
        self.ten_khach_hang_label = QLabel("Tên khách hàng:")
        self.ten_khach_hang_input = QLineEdit()
        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()
        self.so_dien_thoai_label = QLabel("Số điện thoại:")
        self.so_dien_thoai_input = QLineEdit()

        # Tạo các nút
        self.add_button = QPushButton("Thêm")
        self.edit_button = QPushButton("Sửa")
        self.delete_button = QPushButton("Xóa")

        # Kết nối các signal với các slot
        self.add_button.clicked.connect(self.add_customer)
        self.edit_button.clicked.connect(self.edit_customer)
        self.delete_button.clicked.connect(self.delete_customer)

        # Tạo layout
        input_layout = QVBoxLayout()
        ten_khach_hang_layout = QHBoxLayout()
        ten_khach_hang_layout.addWidget(self.ten_khach_hang_label)
        ten_khach_hang_layout.addWidget(self.ten_khach_hang_input)
        input_layout.addLayout(ten_khach_hang_layout)

        email_layout = QHBoxLayout()
        email_layout.addWidget(self.email_label)
        email_layout.addWidget(self.email_input)
        input_layout.addLayout(email_layout)

        so_dien_thoai_layout = QHBoxLayout()
        so_dien_thoai_layout.addWidget(self.so_dien_thoai_label)
        so_dien_thoai_layout.addWidget(self.so_dien_thoai_input)
        input_layout.addLayout(so_dien_thoai_layout)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.edit_button)
        button_layout.addWidget(self.delete_button)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addLayout(input_layout)
        layout.addLayout(button_layout)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Hiển thị dữ liệu khách hàng
        self.load_customers()

    def load_customers(self):
        self.cursor.execute("SELECT * FROM khach_hang")
        customers = self.cursor.fetchall()

        self.table.setRowCount(len(customers))
        for row, customer in enumerate(customers):
            self.table.setItem(row, 0, QTableWidgetItem(str(customer[0])))
            self.table.setItem(row, 1, QTableWidgetItem(customer[1]))
            self.table.setItem(row, 2, QTableWidgetItem(customer[2]))
            self.table.setItem(row, 3, QTableWidgetItem(customer[3]))

    def add_customer(self):
        ten_khach_hang = self.ten_khach_hang_input.text()
        email = self.email_input.text()
        so_dien_thoai = self.so_dien_thoai_input.text()

        # Kiểm tra dữ liệu nhập vào
        if ten_khach_hang and email and so_dien_thoai:
            try:
                self.cursor.execute("INSERT INTO khach_hang (ten_khach_hang, email, so_dien_thoai) VALUES (?, ?, ?)",
                                    (ten_khach_hang, email, so_dien_thoai))
                self.conn.commit()
                self.load_customers()
                self.clear_inputs()
                QMessageBox.information(self, "Thành công", "Thêm khách hàng thành công")
            except sqlite3.IntegrityError:
                QMessageBox.warning(self, "Lỗi", "Email đã tồn tại. Vui lòng nhập email khác.")
        else:
            # Nếu không nhập dữ liệu và nhấn nút "Thêm"
            if not ten_khach_hang and not email and not so_dien_thoai:
                QMessageBox.warning(self, "Lỗi", "Vui lòng nhập thông tin khách hàng")
            else:
                QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin")

    def edit_customer(self):
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            khach_hang_id = self.table.item(selected_row, 0).text()
            ten_khach_hang = self.ten_khach_hang_input.text()
            email = self.email_input.text()
            so_dien_thoai = self.so_dien_thoai_input.text()

            # Kiểm tra dữ liệu nhập vào
            if ten_khach_hang and email and so_dien_thoai:
                try:
                    self.cursor.execute(
                        "UPDATE khach_hang SET ten_khach_hang = ?, email = ?, so_dien_thoai = ? WHERE khach_hang_id = ?",
                        (ten_khach_hang, email, so_dien_thoai, khach_hang_id))
                    self.conn.commit()
                    self.load_customers()
                    self.clear_inputs()
                    QMessageBox.information(self, "Thành công", "Sửa khách hàng thành công")
                except sqlite3.IntegrityError:
                    QMessageBox.warning(self, "Lỗi", "Email đã tồn tại. Vui lòng nhập email khác.")
            else:
                QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin")
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn một khách hàng để sửa")

    def delete_customer(self):
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            khach_hang_id = self.table.item(selected_row, 0).text()
            confirm = QMessageBox.question(self, "Xác nhận",
                                           f"Bạn có chắc chắn muốn xóa khách hàng có ID {khach_hang_id}?",
                                           QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if confirm == QMessageBox.StandardButton.Yes:
                self.cursor.execute("DELETE FROM khach_hang WHERE khach_hang_id = ?", (khach_hang_id,))
                self.conn.commit()
                self.load_customers()
                self.clear_inputs()
                QMessageBox.information(self, "Thành công", "Xóa khách hàng thành công")
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn một khách hàng để xóa")

    def clear_inputs(self):
        self.ten_khach_hang_input.clear()
        self.email_input.clear()
        self.so_dien_thoai_input.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    customer_manager = CustomerManager()
    customer_manager.show()
    sys.exit(app.exec())