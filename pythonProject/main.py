import pygetwindow as gw
import pyautogui
import time


def click_all_windows(window_title):
    windows = gw.getWindowsWithTitle(window_title)
    for window in windows:
        # Tính toán tọa độ tuyệt đối trong từng cửa sổ
        absolute_x, absolute_y = window.left + 349, window.top + 287

        # Mô phỏng sự kiện mouseDown và mouseUp để không giữ chuột
        pyautogui.mouseDown(x=absolute_x, y=absolute_y)
        time.sleep(0.1)  # Đợi 0.1 giây giữa mouseDown và mouseUp
        pyautogui.mouseUp(x=absolute_x, y=absolute_y)


# Click vào tọa độ (349, 287) trên tất cả các cửa sổ có tên "Đại Tây Du"
click_all_windows("Đại Tây Du")
