import csv

def tao_file():
    """Tạo một file CSV mới"""
    ten_file = input("Nhập tên file (ví dụ: du_lieu): ")
    if not ten_file.endswith('.csv'):
        ten_file += '.csv'
    with open(ten_file, 'w', newline='') as file:
        ghi = csv.writer(file)
        ghi.writerow(["Ten", "Tuoi"])
    print(f"File mới '{ten_file}' đã được tạo thành công.")
    return ten_file

def them_du_lieu(ten_file):
    """Thêm tên và tuổi vào file CSV"""
    ten = input("Nhập tên: ")
    tuoi = input("Nhập tuổi: ")
    with open(ten_file, 'a', newline='') as file:
        ghi = csv.writer(file)
        ghi.writerow([ten, tuoi])
    print("Dữ liệu đã được thêm thành công.")

def chinh():
    """Hàm chính để chạy chương trình"""
    ten_file = tao_file()
    while True:
        lua_chon = input("Bạn có muốn thêm dữ liệu không? (y/n): ")
        if lua_chon.lower() == 'y':
            them_du_lieu(ten_file)
        else:
            print("Tạm biệt!")
            break

if __name__ == "__main__":
    chinh()