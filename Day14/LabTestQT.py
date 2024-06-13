import sys

from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QApplication


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Đăng nhập")
        self.setFixedSize(300, 200)

        # Tạo các widget
        self.label_username = QLabel("Tên đăng nhập:")
        self.line_edit_username = QLineEdit()
        self.label_password = QLabel("Mật khẩu:")
        self.line_edit_password = QLineEdit()
        self.line_edit_password.setEchoMode(QLineEdit.Password)
        self.button_login = QPushButton("Đăng nhập")

        # Tạo layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_username)
        layout.addWidget(self.line_edit_username)
        layout.addWidget(self.label_password)
        layout.addWidget(self.line_edit_password)
        layout.addWidget(self.button_login)

        # Tạo một widget chứa layout
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())