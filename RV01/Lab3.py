import tkinter as tk
from tkhtmlview import HTMLLabel

def main():
    # Tạo cửa sổ chính
    root = tk.Tk()
    root.title("Nhúng Giao Diện Web vào Tkinter")

    # Tạo một khung để chứa HTML
    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    # URL của trang web cần nhúng
    html_content = """
    <html>
    <head>
        <title>Trang Web Mẫu</title>
    </head>
    <body>
        <h1>Chào mừng đến với trang web của tôi</h1>
        <p>Đây là một đoạn văn bản mẫu được nhúng vào giao diện Tkinter.</p>
        <a href="https://www.example.com">Liên kết đến Example.com</a>
    </body>
    </html>
    """

    # Tạo HTMLLabel và nhúng HTML vào
    html_label = HTMLLabel(frame, html=html_content)
    html_label.pack(fill="both", expand=True)

    # Chạy vòng lặp chính của Tkinter
    root.mainloop()

if __name__ == "__main__":
    main()
