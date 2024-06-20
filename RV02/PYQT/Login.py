
import sqlite3
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QVBoxLayout, QLineEdit, QLabel, QPushButton, \
    QWidget

class FormDangNhap(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Dang nhap')
        self.setGeometry(100, 100, 280, 80)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.label_ten_dang_nhap = QLabel('Ten dang nhap:')
        self.layout.addWidget(self.label_ten_dang_nhap)

        self.text_ten_dang_nhap = QLineEdit(self)
        self.layout.addWidget(self.text_ten_dang_nhap)

        self.label_mat_khau = QLabel('Mat khau:')
        self.layout.addWidget(self.label_mat_khau)

        self.text_mat_khau = QLineEdit(self)
        self.text_mat_khau.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.text_mat_khau)

        self.button_dang_nhap = QPushButton('Dang nhap', self)
        self.button_dang_nhap.clicked.connect(self.kiem_tra_dang_nhap)
        self.layout.addWidget(self.button_dang_nhap)

        self.central_widget.setLayout(self.layout)

    def kiem_tra_dang_nhap(self):
        ten_dang_nhap = self.text_ten_dang_nhap.text()
        mat_khau = self.text_mat_khau.text()

        conn = sqlite3.connect('quan_ly_ban_hang.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (ten_dang_nhap, mat_khau))

        if cursor.fetchone():
            QMessageBox.information(self, 'Thanh cong', 'Dang nhap thanh cong')
            # Chuyển đến giao diện chính sau khi đăng nhập thành công
        else:
            QMessageBox.warning(self, 'Loi', 'Ten dang nhap hoac mat khau sai')

        conn.close()


app = QApplication(sys.argv)
form_dang_nhap = FormDangNhap()
form_dang_nhap.show()
sys.exit(app.exec_())

