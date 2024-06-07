# Bài tập 6: Lưu nhiều hình ảnh trong cùng một thư mục với chương trình của bạn và đặt tên chúng là 1.gif, 2.gif, 3.gif, v.v.
# Đảm bảo rằng tất cả đều là các tệp .gif. Hiển thị một hình ảnh trong cửa sổ và yêu cầu người dùng nhập một số.
# Sau đó, chương trình sẽ sử dụng số đó để chọn tên tệp chính xác và hiển thị hình ảnh tương ứng.


import tkinter as tk
from PIL import Image, ImageTk

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Hiển thị hình ảnh")
window.geometry("400x600")
# Tạo label để hiển thị hình ảnh
image_label = tk.Label(window)
image_label.pack()


def load_image():
    # Lấy số từ người dùng
    number = entry.get()

    try:
        # Tạo tên tệp hình ảnh
        image_file = f"{number}.gif"

        # Mở và hiển thị hình ảnh
        image = Image.open(image_file)
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo  # Giữ tham chiếu để tránh bị thu gom rác
    except FileNotFoundError:
        image_label.config(text=f"Không tìm thấy hình ảnh {image_file}")


# Tạo entry để nhập số
entry_label = tk.Label(window, text="Nhập số hình ảnh (1, 2, 3, ...):")
entry_label.pack()
entry = tk.Entry(window)
entry.pack()

# Tạo nút để tải hình ảnh
load_button = tk.Button(window, text="Tải hình ảnh", command=load_image)
load_button.pack()

# Chạy chương trình
window.mainloop()