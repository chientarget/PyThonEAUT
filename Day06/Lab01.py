# 1.    Tạo tệp tin số ngẫu nhiên, có phần mở rộng là txt và đọc nội dung của nó.
# 2.    Tạo một tệp tin văn bản mới có phần mở rộng là h5, đọc và ghi dữ liệu vào nó.
# 3.    Thêm nhập và thêm bảng cửu chương vào tệp tin mới với tên file là bangCuuChuong.txt.
# 4.    Sao chép nội dung của một tệp tin văn bản câu 3 sang một tệp tin khác bất kỳ.
# 5.    Di chuyển một tệp tin từ thư mục này sang thư mục khác.
# 6.    Xóa một tệp tin khỏi một thư mục di chuyển ở câu 5.
# 7.    Kiểm tra thông tin tệp tin ở câu 3 và cho biết có bảng cửu chương 5 không?
# 8.    Đổi tên một tệp tin câu 1 thành tên yêu thích của em.
# 9.    Kiểm tra xem một tệp tin có tồn tại hay không.
# 10.    Hãy nhập tự động 100 số vào file và tìm xem số lớn nhất và nhỏ nhất và từ đó tính trung bình giữa chúng.
# 11.    Đọc và ghi dữ liệu vào một tệp tin CSV với thôn tin là hai cột và 2 dòng.
# 12.    Nhập thông tin vào file và kiểm tra có tồn tại thông tin nào là email không? (Email có phần mở rộng là gmail.com).
# 13.    Đưa toàn bộ thông tin về chi tiêu hàng tháng của em vào file, hãy đọc thông tin theo yêu cầu từ bàn phím.
# 14.    Xóa thông tin từ câu 13 theo yêu cầu.
# 15.    Nhập đầy đủ thông tin các câu vào file và đọc từng câu để thực hiện lần lượt.



def clearFile():
    import os
    if os.path.isfile("SoNgauNhien.txt"):
        os.remove("SoNgauNhien.txt")
    if os.path.isfile("FileH5.h5"):
        os.remove("FileH5.h5")
    if os.path.isfile("BangCuuChuong.txt"):
        os.remove("BangCuuChuong.txt")
    if os.path.isfile("CopyBangCuuChuong.txt"):
        os.remove("CopyBangCuuChuong.txt")
    if os.path.isdir("Day06"):
        os.rmdir("Day06")
    if os.path.isfile("YeuThich.txt"):
        os.remove("YeuThich.txt")
    if os.path.isfile("100SoNgauNhien.txt"):
        os.remove("100SoNgauNhien.txt")
    if os.path.isfile("FileCSV.csv"):
        os.remove("FileCSV.csv")
    if os.path.isfile("info.txt"):
        os.remove("info.txt")
    if os.path.isfile("ChiTieuHangThang.txt"):
        os.remove("ChiTieuHangThang.txt")
clearFile()


# 1.    Tạo tệp tin số ngẫu nhiên, có phần mở rộng là txt và đọc nội dung của nó.
def cau1():
    print("Câu 1: Tạo tệp tin số ngẫu nhiên, có phần mở rộng là txt và đọc nội dung của nó.")
    import random
    File = open("SoNgauNhien.txt", "w")
    for i in range(10):
        File.write(str(random.randint(1, 100)) + "\n")
    File.close()
    File = open("SoNgauNhien.txt", "r")
    print(File.read())
    File.close()

cau1()

# 2.    Tạo một tệp tin văn bản mới có phần mở rộng là .h5, đọc và ghi dữ liệu vào nó.
def cau2():
    print("Câu 2: Tạo một tệp tin văn bản mới có phần mở rộng là .h5, đọc và ghi dữ liệu vào nó.")
    File = open("FileH5.h5", "w")
    File.write("ĐÂY LÀ FILE .H5")
    File.close()
    File = open("FileH5.h5", "r")
    print(File.read())
    File.close()
cau2()

# 3.Thêm nhập và thêm bảng cửu chương vào tệp tin mới với tên file là bangCuuChuong.txt. ví dụ nhập 3 thìa ghi thêm bảng nhân 3 kể cả nó đã có ( mặc định không có bảng nào)

def cau3():
    print("Câu 3: Thêm nhập và thêm bảng cửu chương vào tệp tin mới với tên file là bangCuuChuong.txt. ví dụ nhập 3 thì thêm bảng nhân 3 ( mặc định không có bảng nào)")
    File = open("BangCuuChuong.txt", "w")
    n = int(input("Nhập số cần thêm bảng cửu chương: "))
    for i in range(1, 11):
        File.write(str(n) + " x " + str(i) + " = " + str(n*i) + "\n")
    File.close()
    File = open("BangCuuChuong.txt", "r")
    print(File.read())
    File.close()
cau3()

# 4.Sao chép nội dung của một tệp tin văn bản câu 3 sang một tệp tin khác bất kỳ.
def cau4():
    print("Câu 4: Sao chép nội dung của một tệp tin văn bản câu 3 sang một tệp tin khác bất kỳ.")
    File = open("BangCuuChuong.txt", "r")
    FileCopy = open("CopyBangCuuChuong.txt", "w")
    FileCopy.write(File.read())
    File.close()
    FileCopy.close()
    FileCopy = open("CopyBangCuuChuong.txt", "r")
    print(FileCopy.read())
    FileCopy.close()

cau4()

# 5. Di chuyển một tệp tin từ thư mục này sang thư mục khác.
def cau5():
    print("Câu 5: Di chuyển một tệp tin từ thư mục này sang thư mục khác.")
    import os
    import shutil

    # Check if the file exists
    if not os.path.isfile("CopyBangCuuChuong.txt"):
        print("File 'CopyBangCuuChuong.txt' does not exist.")
        return

    # Check if the directory exists, if not create it
    if not os.path.isdir("Day06"):
        os.mkdir("Day06")

    shutil.move("CopyBangCuuChuong.txt", "Day06/CopyBangCuuChuong.txt")

    # Check if the file exists in the new location
    if os.path.isfile("Day06/CopyBangCuuChuong.txt"):
        print("Chuyển ok")
    else:
        print("Xóa lỗi")

cau5()

# 6.    Xóa một tệp tin khỏi một thư mục di chuyển ở câu 5.
def cau6():
    print("Câu 6: Xóa một tệp tin khỏi một thư mục di chuyển ở câu 5.")
    import os

    # Check if the file exists in the new location
    if not os.path.isfile("Day06/CopyBangCuuChuong.txt"):
        print("File 'Day06/CopyBangCuuChuong.txt' does not exist.")
        return

    os.remove("Day06/CopyBangCuuChuong.txt")

    # Check if the file still exists
    if os.path.isfile("Day06/CopyBangCuuChuong.txt"):
        print("Xóa ok")
    else:
        print("Lỗi xóa")

cau6()

# 7.    Kiểm tra thông tin tệp tin ở câu 3 và cho biết có bảng cửu chương 5 không?
def cau7():
    print("Câu 7: Kiểm tra thông tin tệp tin ở câu 3 và cho biết có bảng cửu chương 5 không?")
    File = open("BangCuuChuong.txt", "r")
    for line in File:
        if "5 x" in line:
            print("Bảng cửu chương 5 tồn tại.")
            break
    else:
        print("Bảng cửu chương 5 không tồn tại.")
    File.close()

cau7()

# 8.    Đổi tên một tệp tin câu 1 thành tên yêu thích của em.
def cau8():
    print("Câu 8: Đổi tên một tệp tin câu 1 thành tên yêu thích của em.")
    import os

    # Check if the file exists
    if not os.path.isfile("SoNgauNhien.txt"):
        print("File 'SoNgauNhien.txt' does not exist.")
        return

    os.rename("SoNgauNhien.txt", "YeuThich.txt")

    # Check if the file still exists
    if os.path.isfile("YeuThich.txt"):
        print("Đổi ok")
    else:
        print("Lỗi")
cau8()

# 9.    Kiểm tra xem một tệp tin có tồn tại hay không.
def cau9():
    print("Câu 9: Kiểm tra xem một tệp tin có tồn tại hay không.")
    import os

    if os.path.isfile("YeuThich.txt"):
        print("File 'YeuThich.txt' tồn tại.")
    else:
        print("File 'YeuThich.txt' không tồn tại.")
cau9()

# 10.    Hãy nhập tự động 100 số vào file và tìm xem số lớn nhất và nhỏ nhất và từ đó tính trung bình giữa chúng.
def cau10():
    print("Câu 10: Hãy nhập tự động 100 số vào file và tìm xem số lớn nhất và nhỏ nhất và từ đó tính trung bình giữa chúng.")
    import random

    File = open("100SoNgauNhien.txt", "w")
    for i in range(100):
        File.write(str(random.randint(1, 100)) + "\n")
    File.close()

    File = open("100SoNgauNhien.txt", "r")
    numbers = [int(line) for line in File]
    File.close()

    print("Số lớn nhất:", max(numbers))
    print("Số nhỏ nhất:", min(numbers))
    print("Trung bình:", sum(numbers) / len(numbers))

cau10()

# 11.    Đọc và ghi dữ liệu vào một tệp tin CSV với thôn tin là hai cột và 2 dòng.
def cau11():
    print("Câu 11: Đọc và ghi dữ liệu vào một tệp tin CSV với thôn tin là hai cột và 2 dòng.")
    import csv

    with open("FileCSV.csv", "w", newline="") as File:
        writer = csv.writer(File)
        writer.writerow(["Name", "Age"])
        writer.writerow(["John", 25])

    with open("FileCSV.csv", "r") as File:
        reader = csv.reader(File)
        for row in reader:
            print(row)
cau11()

# 12. Nhập thông tin vào file và kiểm tra có tồn tại thông tin nào là email không? (Email có phần mở rộng là gmail.com).

def cau12():
    # Nhập thông tin vào file
    with open('info.txt', 'w') as f:
        info = input("Nhập thông tin cho câu 12:")
        f.write(info)

    # Đọc thông tin từ file
    with open('info.txt', 'r') as f:
        content = f.read()

    # Kiểm tra xem có tồn tại thông tin nào là email không
    if '@gmail.com' in content:
        print("Có Mail")
    else:
        print("Không có mail")

cau12()

# 13.    Đưa toàn bộ thông tin về chi tiêu hàng tháng của em vào file, hãy đọc thông tin theo yêu cầu từ bàn phím.
def cau13():
    print("Câu 13: Đưa toàn bộ thông tin về chi tiêu hàng tháng của em vào file, hãy đọc thông tin theo yêu cầu từ bàn phím.")
    with open("ChiTieuHangThang.txt", "w") as File:
        while True:
            chi_tieu = input("Nhập chi tiêu hàng tháng (nhấn Enter để kết thúc): ")
            if chi_tieu == "":
                break
            File.write(chi_tieu + "\n")

    with open("ChiTieuHangThang.txt", "r") as File:
        print(File.read())

    # Đọc thông tin theo yêu cầu từ bàn phím
    loai_chi_tieu = input("Nhập loại chi tiêu muốn xem: ")
    with open("ChiTieuHangThang.txt", "r") as File:
        for line in File:
            if loai_chi_tieu in line:
                print(line)

cau13()

# 14.    Xóa thông tin từ câu 13 theo yêu cầu.
def cau14():
    print("Câu 14: Xóa thông tin từ câu 13 theo yêu cầu.")
    with open("ChiTieuHangThang.txt", "r") as File:
        lines = File.readlines()

    loai_chi_tieu = input("Nhập loại chi tiêu muốn xóa: ")
    with open("ChiTieuHangThang.txt", "w") as File:
        for line in lines:
            if loai_chi_tieu not in line:
                File.write(line)

    with open("ChiTieuHangThang.txt", "r") as File:
        print(File.read())

cau14()

# 15.    Nhập đầy đủ thông tin các câu vào file và đọc từng câu để thực hiện lần lượt.
