import sys
import sqlite3
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget,
    QPushButton, QLineEdit, QMessageBox, QHeaderView, QLabel, QHBoxLayout, QComboBox
)

class OrderManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Order Manager")
        self.setGeometry(100, 100, 800, 600)

        # Kết nối đến cơ sở dữ liệu
        self.conn = sqlite3.connect('quan_ly_ban_hang.db')
        self.cursor = self.conn.cursor()

        # Tạo bảng hiển thị danh sách đơn hàng
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Khách hàng", "Ngày đặt hàng", "Tổng tiền"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Tạo ô nhập liệu và nhãn
        self.khach_hang_label = QLabel("Khách hàng:")
        self.khach_hang_combo = QComboBox()
        self.ngay_dat_hang_label = QLabel("Ngày đặt hàng:")
        self.ngay_dat_hang_input = QLineEdit()
        self.tong_tien_label = QLabel("Tổng tiền:")
        self.tong_tien_input = QLineEdit()

        # Tạo các nút
        self.add_button = QPushButton("Thêm")
        self.edit_button = QPushButton("Sửa")
        self.delete_button = QPushButton("Xóa")

        # Kết nối các signal với các slot
        self.add_button.clicked.connect(self.add_order)
        self.edit_button.clicked.connect(self.edit_order)
        self.delete_button.clicked.connect(self.delete_order)

        # Tạo layout
        input_layout = QVBoxLayout()
        khach_hang_layout = QHBoxLayout()
        khach_hang_layout.addWidget(self.khach_hang_label)
        khach_hang_layout.addWidget(self.khach_hang_combo)
        input_layout.addLayout(khach_hang_layout)

        ngay_dat_hang_layout = QHBoxLayout()
        ngay_dat_hang_layout.addWidget(self.ngay_dat_hang_label)
        ngay_dat_hang_layout.addWidget(self.ngay_dat_hang_input)
        input_layout.addLayout(ngay_dat_hang_layout)

        tong_tien_layout = QHBoxLayout()
        tong_tien_layout.addWidget(self.tong_tien_label)
        tong_tien_layout.addWidget(self.tong_tien_input)
        input_layout.addLayout(tong_tien_layout)

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

        # Hiển thị dữ liệu đơn hàng và khách hàng
        self.load_orders()
        self.load_customers()

    def load_orders(self):
        self.cursor.execute("SELECT don_hang.don_hang_id, khach_hang.ten_khach_hang, don_hang.ngay_dat_hang, don_hang.tong_tien "
                            "FROM don_hang "
                            "INNER JOIN khach_hang ON don_hang.khach_hang_id = khach_hang.khach_hang_id")
        orders = self.cursor.fetchall()

        self.table.setRowCount(len(orders))
        for row, order in enumerate(orders):
            self.table.setItem(row, 0, QTableWidgetItem(str(order[0])))
            self.table.setItem(row, 1, QTableWidgetItem(order[1]))
            self.table.setItem(row, 2, QTableWidgetItem(order[2]))
            self.table.setItem(row, 3, QTableWidgetItem(str(order[3])))

    def load_customers(self):
        self.cursor.execute("SELECT khach_hang_id, ten_khach_hang FROM khach_hang")
        customers = self.cursor.fetchall()
        self.khach_hang_combo.addItem("", "")  # Thêm lựa chọn rỗng
        for customer in customers:
            self.khach_hang_combo.addItem(customer[1], customer[0])

    def add_order(self):
        khach_hang_id = self.khach_hang_combo.currentData()
        ngay_dat_hang = self.ngay_dat_hang_input.text()
        tong_tien = self.tong_tien_input.text()

        # Kiểm tra dữ liệu nhập vào
        if khach_hang_id and ngay_dat_hang and tong_tien:
            try:
                tong_tien = float(tong_tien)
                self.cursor.execute("INSERT INTO don_hang (khach_hang_id, ngay_dat_hang, tong_tien) VALUES (?, ?, ?)",
                                    (khach_hang_id, ngay_dat_hang, tong_tien))
                self.conn.commit()
                self.load_orders()
                self.clear_inputs()
                QMessageBox.information(self, "Thành công", "Thêm đơn hàng thành công")
            except ValueError:
                QMessageBox.warning(self, "Lỗi", "Tổng tiền phải là số")
        else:
            # Nếu không nhập dữ liệu và nhấn nút "Thêm"
            if not khach_hang_id and not ngay_dat_hang and not tong_tien:
                QMessageBox.warning(self, "Lỗi", "Vui lòng nhập thông tin đơn hàng")
            else:
                QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin")

    def edit_order(self):
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            don_hang_id = self.table.item(selected_row, 0).text()
            khach_hang_id = self.khach_hang_combo.currentData()
            ngay_dat_hang = self.ngay_dat_hang_input.text()
            tong_tien = self.tong_tien_input.text()

            # Kiểm tra dữ liệu nhập vào
            if khach_hang_id and ngay_dat_hang and tong_tien:
                try:
                    tong_tien = float(tong_tien)
                    self.cursor.execute(
                        "UPDATE don_hang SET khach_hang_id = ?, ngay_dat_hang = ?, tong_tien = ? WHERE don_hang_id = ?",
                        (khach_hang_id, ngay_dat_hang, tong_tien, don_hang_id))
                    self.conn.commit()
                    self.load_orders()
                    self.clear_inputs()
                    QMessageBox.information(self, "Thành công", "Sửa đơn hàng thành công")
                except ValueError:
                    QMessageBox.warning(self, "Lỗi", "Tổng tiền phải là số")
            else:
                QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin")
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn một đơn hàng để sửa")

    def delete_order(self):
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            don_hang_id = self.table.item(selected_row, 0).text()
            confirm = QMessageBox.question(self, "Xác nhận",
                                           f"Bạn có chắc chắn muốn xóa đơn hàng có ID {don_hang_id}?",
                                           QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if confirm == QMessageBox.StandardButton.Yes:
                self.cursor.execute("DELETE FROM don_hang WHERE don_hang_id = ?", (don_hang_id,))
                self.conn.commit()
                self.load_orders()
                self.clear_inputs()
                QMessageBox.information(self, "Thành công", "Xóa đơn hàng thành công")
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn một đơn hàng để xóa")

    def clear_inputs(self):
        self.khach_hang_combo.setCurrentIndex(0)  # Chọn lựa chọn rỗng
        self.ngay_dat_hang_input.clear()
        self.tong_tien_input.clear()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    order_manager = OrderManager()
    order_manager.show()
    sys.exit(app.exec())
