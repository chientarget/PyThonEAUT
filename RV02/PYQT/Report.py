import sys
import sqlite3
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QComboBox,
    QPushButton, QTableWidget, QTableWidgetItem, QHeaderView
)
from PyQt6.QtCore import Qt

class ReportForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Xuất báo cáo và thống kê")
        self.setGeometry(100, 100, 800, 600)

        # Kết nối đến cơ sở dữ liệu
        self.conn = sqlite3.connect('quan_ly_ban_hang.db')
        self.cursor = self.conn.cursor()

        # Tạo combo box để chọn loại báo cáo
        self.report_label = QLabel("Chọn loại báo cáo:")
        self.report_combo = QComboBox()
        self.report_combo.addItem("Doanh thu theo ngày")
        self.report_combo.addItem("Sản phẩm bán chạy nhất")
        self.report_combo.addItem("Khách hàng mua nhiều nhất")

        # Tạo nút để tạo báo cáo
        self.generate_button = QPushButton("Tạo báo cáo")
        self.generate_button.clicked.connect(self.generate_report)

        # Tạo bảng để hiển thị báo cáo
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "Tên", "Giá trị"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Tạo layout
        layout = QVBoxLayout()
        report_layout = QVBoxLayout()
        report_layout.addWidget(self.report_label)
        report_layout.addWidget(self.report_combo)
        report_layout.addWidget(self.generate_button)
        layout.addLayout(report_layout)
        layout.addWidget(self.table)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def generate_report(self):
        report_type = self.report_combo.currentText()

        if report_type == "Doanh thu theo ngày":
            self.cursor.execute("SELECT don_hang.don_hang_id, don_hang.ngay_dat_hang, SUM(san_pham.gia * chi_tiet_don_hang.so_luong) AS doanh_thu "
                                "FROM don_hang "
                                "INNER JOIN chi_tiet_don_hang ON don_hang.don_hang_id = chi_tiet_don_hang.don_hang_id "
                                "INNER JOIN san_pham ON chi_tiet_don_hang.san_pham_id = san_pham.san_pham_id "
                                "GROUP BY don_hang.don_hang_id, don_hang.ngay_dat_hang "
                                "ORDER BY don_hang.ngay_dat_hang")
            report_data = self.cursor.fetchall()

        elif report_type == "Sản phẩm bán chạy nhất":
            self.cursor.execute("SELECT san_pham.san_pham_id, san_pham.ten_san_pham, SUM(chi_tiet_don_hang.so_luong) AS so_luong_ban "
                                "FROM san_pham "
                                "INNER JOIN chi_tiet_don_hang ON san_pham.san_pham_id = chi_tiet_don_hang.san_pham_id "
                                "GROUP BY san_pham.san_pham_id "
                                "ORDER BY so_luong_ban DESC "
                                "LIMIT 1")
            report_data = self.cursor.fetchone()

        elif report_type == "Khách hàng mua nhiều nhất":
            self.cursor.execute("SELECT khach_hang.khach_hang_id, khach_hang.ten_khach_hang, SUM(san_pham.gia * chi_tiet_don_hang.so_luong) AS tong_chi_tieu "
                                "FROM khach_hang "
                                "INNER JOIN don_hang ON khach_hang.khach_hang_id = don_hang.khach_hang_id "
                                "INNER JOIN chi_tiet_don_hang ON don_hang.don_hang_id = chi_tiet_don_hang.don_hang_id "
                                "INNER JOIN san_pham ON chi_tiet_don_hang.san_pham_id = san_pham.san_pham_id "
                                "GROUP BY khach_hang.khach_hang_id "
                                "ORDER BY tong_chi_tieu DESC "
                                "LIMIT 1")
            report_data = self.cursor.fetchone()

        self.display_report(report_data, report_type)

    def display_report(self, report_data, report_type):
        self.table.setRowCount(0)  # Xóa dữ liệu cũ

        if report_type == "Doanh thu theo ngày":
            self.table.setColumnCount(3)
            self.table.setHorizontalHeaderLabels(["ID đơn hàng", "Ngày đặt hàng", "Doanh thu"])
            for row, data in enumerate(report_data):
                self.table.insertRow(row)
                self.table.setItem(row, 0, QTableWidgetItem(str(data[0])))
                self.table.setItem(row, 1, QTableWidgetItem(data[1]))
                self.table.setItem(row, 2, QTableWidgetItem(str(data[2])))

        elif report_type == "Sản phẩm bán chạy nhất":
            self.table.setColumnCount(3)
            self.table.setHorizontalHeaderLabels(["ID sản phẩm", "Tên sản phẩm", "Số lượng bán"])
            self.table.insertRow(0)
            self.table.setItem(0, 0, QTableWidgetItem(str(report_data[0])))
            self.table.setItem(0, 1, QTableWidgetItem(report_data[1]))
            self.table.setItem(0, 2, QTableWidgetItem(str(report_data[2])))

        elif report_type == "Khách hàng mua nhiều nhất":
            self.table.setColumnCount(3)
            self.table.setHorizontalHeaderLabels(["ID khách hàng", "Tên khách hàng", "Tổng chi tiêu"])
            self.table.insertRow(0)
            self.table.setItem(0, 0, QTableWidgetItem(str(report_data[0])))
            self.table.setItem(0, 1, QTableWidgetItem(report_data[1]))
            self.table.setItem(0, 2, QTableWidgetItem(str(report_data[2])))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    report_form = ReportForm()
    report_form.show()
    sys.exit(app.exec())