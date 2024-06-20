import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QMenuBar, QMenu
)
from PyQt6.QtGui import QAction
from QLSP import ProductManager
from QLKH import CustomerManager
from QLDH import OrderManager
from Report import ReportForm
from User_DanhGia import FeedbackForm

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quản lý bán hàng")
        self.setGeometry(100, 100, 800, 600)

        # Tạo menu
        menu_bar = QMenuBar()
        self.setMenuBar(menu_bar)

        # Menu Quản lý
        quan_ly_menu = QMenu("&Quản lý", self)
        menu_bar.addMenu(quan_ly_menu)

        # Tạo các tùy chọn trong menu Quản lý
        ql_san_pham_action = QAction("&Quản lý sản phẩm", self)
        ql_san_pham_action.triggered.connect(self.show_qlsp_form)
        quan_ly_menu.addAction(ql_san_pham_action)

        ql_khach_hang_action = QAction("&Quản lý khách hàng", self)
        ql_khach_hang_action.triggered.connect(self.show_qlkh_form)
        quan_ly_menu.addAction(ql_khach_hang_action)

        ql_don_hang_action = QAction("&Quản lý đơn hàng", self)
        ql_don_hang_action.triggered.connect(self.show_qldh_form)
        quan_ly_menu.addAction(ql_don_hang_action)

        # Menu Báo cáo
        bao_cao_menu = QMenu("&Báo cáo", self)
        menu_bar.addMenu(bao_cao_menu)

        bao_cao_action = QAction("&Xuất báo cáo", self)
        bao_cao_action.triggered.connect(self.show_baocao_form)
        bao_cao_menu.addAction(bao_cao_action)

        # Menu Đánh giá
        danh_gia_menu = QMenu("&Đánh giá", self)
        menu_bar.addMenu(danh_gia_menu)

        danh_gia_action = QAction("&Gửi đánh giá", self)
        danh_gia_action.triggered.connect(self.show_danhgia_form)
        danh_gia_menu.addAction(danh_gia_action)

        # Khởi tạo các form
        self.qlsp_form = ProductManager()
        self.qlkh_form = CustomerManager()
        self.qldh_form = OrderManager()
        self.baocao_form = ReportForm()
        self.danhgia_form = FeedbackForm()

    def show_qlsp_form(self):
        self.qlsp_form.show()

    def show_qlkh_form(self):
        self.qlkh_form.show()

    def show_qldh_form(self):
        self.qldh_form.show()

    def show_baocao_form(self):
        self.baocao_form.show()

    def show_danhgia_form(self):
        self.danhgia_form.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())