import sys

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

# pip install pyqt6

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Đăng nhập")
        self.setFixedSize(400, 300)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
            QLabel {
                font-size: 14px;
                color: #333333;
                
            }
            QLineEdit {
                padding: 8px;
                border: 1px solid #cccccc;
                border-radius: 4px;
                font-size: 14px;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 4px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #45a049;
                
            }
        """)

        # Tạo logo
        logo_label = QLabel()
        logo_pixmap = QPixmap("logo.png")  # Thay đổi đường dẫn logo tùy ý
        logo_label.setPixmap(logo_pixmap.scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio))

        # Tạo các widget
        self.label_username = QLabel("Tên đăng nhập:")
        self.line_edit_username = QLineEdit()
        self.label_password = QLabel("Mật khẩu:")
        self.line_edit_password = QLineEdit()
        self.line_edit_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.button_login = QPushButton("Đăng nhập")

        # Tạo layout
        layout = QVBoxLayout()
        layout.addWidget(logo_label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label_username)
        layout.addWidget(self.line_edit_username)
        layout.addWidget(self.label_password)
        layout.addWidget(self.line_edit_password)
        layout.addWidget(self.button_login, alignment=Qt.AlignmentFlag.AlignCenter)

        # Tạo một widget chứa layout
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())