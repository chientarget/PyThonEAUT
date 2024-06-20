import sys
import sqlite3
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget,
    QPushButton, QTextEdit, QMessageBox, QHeaderView, QLabel, QHBoxLayout, QComboBox
)

class AdminFeedbackForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Admin Feedback Form")
        self.setGeometry(100, 100, 800, 600)

        # Kết nối đến cơ sở dữ liệu
        self.conn = sqlite3.connect('quan_ly_ban_hang.db')
        self.cursor = self.conn.cursor()

        # Tạo bảng hiển thị danh sách phản hồi
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Người dùng", "Nội dung phản hồi", "Phản hồi lại"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Tạo ô nhập liệu và nhãn
        self.feedback_label = QLabel("Phản hồi:")
        self.feedback_input = QTextEdit()
        self.reply_label = QLabel("Phản hồi lại:")
        self.reply_input = QTextEdit()

        # Tạo các nút
        self.add_button = QPushButton("Thêm")
        self.edit_button = QPushButton("Sửa")
        self.delete_button = QPushButton("Xóa")
        self.save_button = QPushButton("Lưu")

        # Kết nối các signal với các slot
        self.add_button.clicked.connect(self.add_feedback)
        self.edit_button.clicked.connect(self.edit_feedback)
        self.delete_button.clicked.connect(self.delete_feedback)
        self.save_button.clicked.connect(self.save_feedback)
        self.table.currentCellChanged.connect(self.display_feedback)

        # Tạo layout
        input_layout = QVBoxLayout()
        feedback_layout = QHBoxLayout()
        feedback_layout.addWidget(self.feedback_label)
        feedback_layout.addWidget(self.feedback_input)
        input_layout.addLayout(feedback_layout)

        reply_layout = QHBoxLayout()
        reply_layout.addWidget(self.reply_label)
        reply_layout.addWidget(self.reply_input)
        input_layout.addLayout(reply_layout)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.edit_button)
        button_layout.addWidget(self.delete_button)
        button_layout.addWidget(self.save_button)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addLayout(input_layout)
        layout.addLayout(button_layout)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Hiển thị dữ liệu phản hồi
        self.load_feedback()

    def load_feedback(self):
        self.cursor.execute(
            "SELECT phan_hoi.phan_hoi_id, users.username, phan_hoi.noi_dung_phan_hoi, phan_hoi.phan_hoi_lai "
            "FROM phan_hoi "
            "INNER JOIN users ON phan_hoi.user_id = users.user_id")
        feedback = self.cursor.fetchall()

        self.table.setRowCount(len(feedback))
        for row, feedback_item in enumerate(feedback):
            self.table.setItem(row, 0, QTableWidgetItem(str(feedback_item[0])))
            self.table.setItem(row, 1, QTableWidgetItem(feedback_item[1]))
            self.table.setItem(row, 2, QTableWidgetItem(feedback_item[2]))
            self.table.setItem(row, 3, QTableWidgetItem(str(feedback_item[3])))

    def add_feedback(self):
        self.feedback_input.clear()
        self.reply_input.clear()
        self.table.clearSelection()

    def edit_feedback(self):
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            feedback_id = int(self.table.item(selected_row, 0).text())
            self.cursor.execute("SELECT noi_dung_phan_hoi, phan_hoi_lai FROM phan_hoi WHERE phan_hoi_id = ?",
                                (feedback_id,))
            feedback_data = self.cursor.fetchone()
            self.feedback_input.setPlainText(feedback_data[0])
            self.reply_input.setPlainText(str(feedback_data[1]))
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn một phản hồi để sửa")

    def delete_feedback(self):
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            feedback_id = int(self.table.item(selected_row, 0).text())
            confirm = QMessageBox.question(self, "Xác nhận", f"Bạn có muốn xóa phản hồi có ID {feedback_id}?",
                                           QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if confirm == QMessageBox.StandardButton.Yes:
                self.cursor.execute("DELETE FROM phan_hoi WHERE phan_hoi_id = ?", (feedback_id,))
                self.conn.commit()
                self.load_feedback()
                QMessageBox.information(self, "Thành công", "Phản hồi đã được xóa")
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn một phản hồi để xóa")

    def save_feedback(self):
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            feedback_id = int(self.table.item(selected_row, 0).text())
            feedback_content = self.feedback_input.toPlainText()
            reply_content = self.reply_input.toPlainText()
            self.cursor.execute("UPDATE phan_hoi SET noi_dung_phan_hoi = ?, phan_hoi_lai = ? WHERE phan_hoi_id = ?",
                                (feedback_content, reply_content, feedback_id))
            self.conn.commit()
            self.load_feedback()
            QMessageBox.information(self, "Thành công", "Phản hồi đã được cập nhật")
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn một phản hồi để sửa")

    def display_feedback(self, row, column):
        feedback_id = int(self.table.item(row, 0).text())
        self.cursor.execute("SELECT noi_dung_phan_hoi, phan_hoi_lai FROM phan_hoi WHERE phan_hoi_id = ?",
                            (feedback_id,))
        feedback_data = self.cursor.fetchone()
        self.feedback_input.setPlainText(feedback_data[0])
        self.reply_input.setPlainText(str(feedback_data[1]))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    admin_feedback_form = AdminFeedbackForm()
    admin_feedback_form.show()
    sys.exit(app.exec())
