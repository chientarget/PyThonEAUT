import sys
import sqlite3
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit, QPushButton, QMessageBox,
    QLabel, QHBoxLayout, QComboBox
)

class FeedbackForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Feedback Form")
        self.setGeometry(100, 100, 400, 300)

        # Kết nối đến cơ sở dữ liệu
        self.conn = sqlite3.connect('quan_ly_ban_hang.db')
        self.cursor = self.conn.cursor()

        # Tạo ô nhập liệu và nhãn
        self.user_label = QLabel("Người dùng:")
        self.user_combo = QComboBox()
        self.feedback_label = QLabel("Phản hồi:")
        self.feedback_input = QTextEdit()

        # Tạo nút
        self.send_button = QPushButton("Gửi")

        # Kết nối signal với slot
        self.send_button.clicked.connect(self.send_feedback)

        # Tạo layout
        input_layout = QVBoxLayout()
        user_layout = QHBoxLayout()
        user_layout.addWidget(self.user_label)
        user_layout.addWidget(self.user_combo)
        input_layout.addLayout(user_layout)

        feedback_layout = QHBoxLayout()
        feedback_layout.addWidget(self.feedback_label)
        feedback_layout.addWidget(self.feedback_input)
        input_layout.addLayout(feedback_layout)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.send_button)

        layout = QVBoxLayout()
        layout.addLayout(input_layout)
        layout.addLayout(button_layout)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Hiển thị dữ liệu người dùng
        self.load_users()

    def load_users(self):
        self.cursor.execute("SELECT user_id, username FROM users")
        users = self.cursor.fetchall()
        self.user_combo.addItem("", "")  # Thêm lựa chọn rỗng
        for user in users:
            self.user_combo.addItem(user[1], user[0])

    def send_feedback(self):
        user_id = self.user_combo.currentData()
        feedback_content = self.feedback_input.toPlainText()

        # Kiểm tra dữ liệu nhập vào
        if user_id and feedback_content:
            self.cursor.execute("INSERT INTO phan_hoi (user_id, noi_dung_phan_hoi) VALUES (?, ?)",
                                (user_id, feedback_content))
            self.conn.commit()
            self.feedback_input.clear()
            QMessageBox.information(self, "Thành công", "Phản hồi đã được gửi")
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn người dùng và nhập nội dung phản hồi")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    feedback_form = FeedbackForm()
    feedback_form.show()
    sys.exit(app.exec())