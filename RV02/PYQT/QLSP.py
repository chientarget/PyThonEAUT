import sys
import sqlite3
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget,
    QPushButton, QLineEdit, QMessageBox, QHeaderView, QLabel, QHBoxLayout
)

class ProductManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quản lý sản phẩm")
        self.setGeometry(100, 100, 800, 600)

        # Kết nối đến cơ sở dữ liệu
        self.conn = sqlite3.connect('quan_ly_ban_hang.db')
        self.cursor = self.conn.cursor()

        # Tạo bảng hiển thị danh sách sản phẩm
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Tên sản phẩm", "Giá", "Số lượng"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Tạo ô nhập liệu và nhãn
        self.ten_san_pham_label = QLabel("Tên sản phẩm:")
        self.ten_san_pham_input = QLineEdit()
        self.gia_label = QLabel("Giá:")
        self.gia_input = QLineEdit()
        self.so_luong_label = QLabel("Số lượng:")
        self.so_luong_input = QLineEdit()

        # Tạo các nút
        self.add_button = QPushButton("Thêm")
        self.edit_button = QPushButton("Sửa")
        self.delete_button = QPushButton("Xóa")

        # Kết nối các signal với các slot
        self.add_button.clicked.connect(self.add_product)
        self.edit_button.clicked.connect(self.edit_product)
        self.delete_button.clicked.connect(self.delete_product)

        # Tạo layout
        input_layout = QVBoxLayout()
        ten_san_pham_layout = QHBoxLayout()
        ten_san_pham_layout.addWidget(self.ten_san_pham_label)
        ten_san_pham_layout.addWidget(self.ten_san_pham_input)
        input_layout.addLayout(ten_san_pham_layout)

        gia_layout = QHBoxLayout()
        gia_layout.addWidget(self.gia_label)
        gia_layout.addWidget(self.gia_input)
        input_layout.addLayout(gia_layout)

        so_luong_layout = QHBoxLayout()
        so_luong_layout.addWidget(self.so_luong_label)
        so_luong_layout.addWidget(self.so_luong_input)
        input_layout.addLayout(so_luong_layout)

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

        # Hiển thị dữ liệu sản phẩm
        self.load_products()

    def load_products(self):
        self.cursor.execute("SELECT * FROM san_pham")
        products = self.cursor.fetchall()

        self.table.setRowCount(len(products))
        for row, product in enumerate(products):
            self.table.setItem(row, 0, QTableWidgetItem(str(product[0])))
            self.table.setItem(row, 1, QTableWidgetItem(product[1]))
            self.table.setItem(row, 2, QTableWidgetItem(str(product[2])))
            self.table.setItem(row, 3, QTableWidgetItem(str(product[3])))

    def add_product(self):
        ten_san_pham = self.ten_san_pham_input.text()
        gia = self.gia_input.text()
        so_luong = self.so_luong_input.text()

        # Kiểm tra dữ liệu nhập vào
        if ten_san_pham and gia and so_luong:
            try:
                gia = float(gia)
                so_luong = int(so_luong)
                self.cursor.execute("INSERT INTO san_pham (ten_san_pham, gia, so_luong) VALUES (?, ?, ?)",
                                    (ten_san_pham, gia, so_luong))
                self.conn.commit()
                self.load_products()
                self.clear_inputs()
                QMessageBox.information(self, "Thành công", "Thêm sản phẩm thành công")
            except ValueError:
                QMessageBox.warning(self, "Lỗi", "Giá và số lượng phải là số")
        else:
            # Nếu không nhập dữ liệu và nhấn nút "Thêm"
            if not ten_san_pham and not gia and not so_luong:
                QMessageBox.warning(self, "Lỗi", "Vui lòng nhập thông tin sản phẩm")
            else:
                QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin")

    def edit_product(self):
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            san_pham_id = self.table.item(selected_row, 0).text()
            ten_san_pham = self.ten_san_pham_input.text()
            gia = self.gia_input.text()
            so_luong = self.so_luong_input.text()

            # Kiểm tra dữ liệu nhập vào
            if ten_san_pham and gia and so_luong:
                try:
                    gia = float(gia)
                    so_luong = int(so_luong)
                    self.cursor.execute(
                        "UPDATE san_pham SET ten_san_pham = ?, gia = ?, so_luong = ? WHERE san_pham_id = ?",
                        (ten_san_pham, gia, so_luong, san_pham_id))
                    self.conn.commit()
                    self.load_products()
                    self.clear_inputs()
                    QMessageBox.information(self, "Thành công", "Sửa sản phẩm thành công")
                except ValueError:
                    QMessageBox.warning(self, "Lỗi", "Giá và số lượng phải là số")
            else:
                QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin")
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn một sản phẩm để sửa")

    def delete_product(self):
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            san_pham_id = self.table.item(selected_row, 0).text()
            confirm = QMessageBox.question(self, "Xác nhận", f"Bạn có chắc chắn muốn xóa sản phẩm có ID {san_pham_id}?",
                                           QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if confirm == QMessageBox.StandardButton.Yes:
                self.cursor.execute("DELETE FROM san_pham WHERE san_pham_id = ?", (san_pham_id,))
                self.conn.commit()
                self.load_products()
                self.clear_inputs()
                QMessageBox.information(self, "Thành công", "Xóa sản phẩm thành công")
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn một sản phẩm để xóa")

    def clear_inputs(self):
        self.ten_san_pham_input.clear()
        self.gia_input.clear()
        self.so_luong_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    product_manager = ProductManager()
    product_manager.show()
    sys.exit(app.exec())