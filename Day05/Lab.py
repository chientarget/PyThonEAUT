# Nguyễn Huy Chiến
# Câu 1: Em hãy tạo một file là tên của em, trong file có đầy đủ thông tin cá nhân. (Thông tin nhập từ bàn phím)
# Câu 2: Từ câu 1, em hãy thêm thông tin của bạn em và đọc toàn bộ thông tin có trong file.
# Câu 3: Nhập thông tin hai số a và b vào file, tính tổng, hiệu, tích và thương của hai số đấy.
# Câu 4: Vẽ một hình mặt cười vào file và đọc mặt cười đấy.
# Câu 5: Nhập vào 1 dãy số tự động vào file, tính tổng và tích các số lẽ và số chẵn từ file đó.
# Câu 6: Nhập đầy đủ thông tin cá nhân của em và đếm ký tự của file đấy.
# Câu 7: Nhập vào sô tự nhiên n vào file, tính giai thừa của số đấy.
# Câu 8: Nhập vào điểm của 5 sinh viên với 5 môn học khác nhau, Tính tổng và trung bình của mỗi em.
# Tìm ra sinh viên có điểm trung bình cao nhất và thấp nhất.
# Câu 9: Tạo một danh sách thư mời đến bữa tiệc sinh nhật,Hãy xóa một thành viên có trong thư mời đó bất kỳ.
# Câu 10: Tự ra 2 câu và giải liên quan đến tệp tin bất kỳ.
# Câu 13: Tạp menu để làm tất cả các câu trên bằng chức năng.

# Câu 1: Em hãy tạo một file là tên của em, trong file có đầy đủ thông tin cá nhân. (Thông tin nhập từ bàn phím)

def cau1():
    print("Câu 1: Em hãy tạo một file là tên của em, trong file có đầy đủ thông tin cá nhân. (Thông tin nhập từ bàn phím)")
    ten = input("Nhập tên của bạn: ")
    tuoi = input("Nhập tuổi của bạn: ")
    gioitinh = input("Nhập giới tính của bạn: ")
    diachi = input("Nhập địa chỉ của bạn: ")
    sdt = input("Nhập số điện thoại của bạn: ")

    File = open("NguyenHuyChien.txt", "w")
    File.write("Tên: " + ten + "\n")
    File.write("Tuổi: " + tuoi + "\n")
    File.write("Giới tính: " + gioitinh + "\n")
    File.write("Địa chỉ: " + diachi + "\n")
    File.write("Số điện thoại: " + sdt + "\n")
    File.close()
    print("Đã tạo file thành công!")

# cau1()



# Câu 2: Từ câu 1, em hãy thêm thông tin của bạn em và đọc toàn bộ thông tin có trong file.
# Thêm mã sinh viên  , lớp
def cau2():
    print("Câu 2: Từ câu 1, em hãy thêm thông tin của bạn em và đọc toàn bộ thông tin có trong file.")
    File = open("NguyenHuyChien.txt", "a")
    masv = input("Nhập mã sinh viên của bạn: ")
    lop = input("Nhập lớp của bạn: ")

    File.write("Mã sinh viên: " + masv + "\n")
    File.write("Lớp: " + lop + "\n")
    File.close()

    File = open("NguyenHuyChien.txt", "r")
    print(File.read())
    File.close()

# cau2()

# Câu 3: Nhập thông tin hai số a và b vào file, tính tổng, hiệu, tích và thương của hai số đấy.
def cau3():
    print("Câu 3: Nhập thông tin hai số a và b vào file, tính tổng, hiệu, tích và thương của hai số đấy.")
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))

    File = open("Caculate.txt", "a")
    File.write("Số a: " + str(a) + "\n")
    File.write("Số b: " + str(b) + "\n")
    File.write("Tổng: " + str(a+b) + "\n")
    File.write("Hiệu: " + str(a-b) + "\n")
    File.write("Tích: " + str(a*b) + "\n")
    File.write("Thương: " + str(a/b) + "\n")
    File.close()

    File = open("Caculate.txt", "r")
    print(File.read())
    File.close()
# cau3()

# Câu 4: Vẽ một hình mặt cười vào file và đọc mặt cười đấy.
def cau4():
    print("Câu 4: Vẽ một hình mặt cười vào file và đọc mặt cười đấy.")
    File = open("Smile.txt", "w")

    File.write("  _____  "+ "\n")
    File.write(" /     \ "+ "\n")
    File.write("|  _ _  |"+ "\n")
    File.write("|   *   |"+ "\n")
    File.write("\ \___/ /"+ "\n")
    File.write(" \_____/ "+ "\n")

    File.close()

    File = open("Smile.txt", "r")
    print(File.read())
    File.close()

# cau4()

# Câu 5: Nhập vào 1 dãy số tự động vào file, tính tổng và tích các số lẽ và số chẵn từ file đó.
def cau5():
    print("Câu 5: Nhập vào 1 dãy số tự động vào file, tính tổng và tích các số lẽ và số chẵn từ file đó.")
    n = int(input("Nhập số lượng số: "))

    File = open("Number.txt", "w")
    for i in range(0,n):
        File.write(str(i+1) + "\n")
    File.close()

    File = open("Number.txt", "r")
    data = File.readlines()
    tongchan = 0
    tongle = 0
    tichchan = 1
    tichle = 1
    for i in data:
        if int(i) % 2 == 0:
            tongchan += int(i)
            tichchan *= int(i)
        else:
            tongle += int(i)
            tichle *= int(i)
    print("Tổng số chẵn: ", tongchan)
    print("Tích số chẵn: ", tichchan)
    print("Tổng số lẻ: ", tongle)
    print("Tích số lẻ: ", tichle)
    File.close()
#
# cau5()

# Câu 6: Nhập đầy đủ thông tin cá nhân của em và đếm ký tự của file đấy.
def cau6():
    print("Câu 6: Nhập đầy đủ thông tin cá nhân của em và đếm ký tự")
    ten = input("Nhập tên của bạn: ")

    File = open("NguyenHuyChien.txt", "w")
    File.write(ten )
    File.close()

    File = open("NguyenHuyChien.txt", "r")
    data = File.read()
    print("Số ký tự trong file: ", len(data))
    File.close()
# cau6()

# Câu 7: Nhập vào sô tự nhiên n vào file, tính giai thừa của số đấy.
def cau7():
    print("Câu 7: Nhập vào sô tự nhiên n vào file, tính Zai thừa của số đấy.")
    n = int(input("Nhập số tự nhiên n: "))

    File = open("ZaiThua.txt", "w")
    File.write(str(n))
    File.close()

    File = open("ZaiThua.txt", "r")
    data = File.read()
    n = int(data)

    giaithua = 1
    for i in range(1,n+1):
        giaithua *= i
    print("Zai thừa của ", n, " là: ", giaithua)
    File.close()
# cau7()


# Câu 8: Nhập vào điểm của 5 sinh viên với 5 môn học khác  nhau (Toán, Ngữ Văn, Lý, Hóa, Sinh), Tính tổng và trung bình của mỗi em.
# Tìm ra sinh viên có điểm trung bình cao nhất và thấp nhất.

def cau8():
    print("Câu 8: Nhập vào điểm của 5 sinh viên với 5 môn học khác nhau (Toán, Ngữ Văn, Lý, Hóa, Sinh), Tính tổng và trung bình của mỗi em. Tìm ra sinh viên có điểm trung bình cao nhất và thấp nhất.")
    File = open("DiemSinhVien.txt", "w")
    for i in range(1,6):
        ten = input(f"Nhập tên sinh viên {i}: ")
        toan = float(input("Nhập điểm Toán: "))
        van = float(input("Nhập điểm Ngữ Văn: "))
        ly = float(input("Nhập điểm Lý: "))
        hoa = float(input("Nhập điểm Hóa: "))
        sinh = float(input("Nhập điểm Sinh: "))

        File.write(ten + "\n")
        File.write("Toán: " + str(toan) + "\n")
        File.write("Ngữ Văn: " + str(van) + "\n")
        File.write("Lý: " + str(ly) + "\n")
        File.write("Hóa: " + str(hoa) + "\n")
        File.write("Sinh: " + str(sinh) + "\n")

    File.close()

    File = open("DiemSinhVien.txt", "r")
    data = File.readlines()
    max = 0
    min = 100
    for i in range(0, len(data), 6):
        ten = data[i]
        toan = float(data[i+1].split(": ")[1])
        van = float(data[i+2].split(": ")[1])
        ly = float(data[i+3].split(": ")[1])
        hoa = float(data[i+4].split(": ")[1])
        sinh = float(data[i+5].split(": ")[1])

        tong = toan + van + ly + hoa + sinh
        tb = tong / 5
        print("Tên: ", ten)
        print("Tổng điểm: ", tong)
        print("Điểm trung bình: ", tb)
        if tb > max:
            max = tb

# cau8()

# Câu 9: Tạo một danh sách thư mời đến bữa tiệc sinh nhật,Hãy xóa một thành viên có trong thư mời đó bất kỳ.
def cau9():
    print("Câu 9: Tạo một danh sách thư mời đến bữa tiệc sinh nhật,Hãy xóa một thành viên có trong thư mời đó bất kỳ.")
    File = open("Thumoi.txt", "w")
    for i in range(1,6):
        ten = input(f"Nhập tên thành viên {i}: ")
        File.write(ten + "\n")
    File.close()

    File = open("Thumoi.txt", "r")
    data = File.readlines()
    print("Danh sách thư mời: ")
    for i in data:
        print(i)

    xoa = input("Nhập tên thành viên muốn xóa: ")
    data.remove(xoa + "\n")

    File = open("Thumoi.txt", "w")
    for i in data:
        File.write(i)
    File.close()

    File = open("Thumoi.txt", "r")
    data = File.readlines()
    print("Danh sách thư mời sau khi xóa: ")
    for i in data:
        print(i)
    File.close()
# cau9()


# Câu 10: Tự ra 2 câu và giải liên quan đến tệp tin bất kỳ basic.
# Câu 11: Gom tất cả nội dung trong file txt vaào 1 file txt khác ( Get all file .txt )
# Câu 12: Đổi tên file gom vừa tạo thành tên mới


def cau11():
    print("Câu 11: Gom tất cả nội dung trong file txt vaào 1 file txt khác ( Get all file .txt )")
    FileMoi = open("Gom.txt", "w")
    File = open("NguyenHuyChien.txt", "r")
    File2 = open("Caculate.txt", "r")
    File3 = open("Diem.txt", "r")
    FileMoi.write(File.read())
    FileMoi.write(File2.read())
    FileMoi.write(File3.read())
    File.close()
    File2.close()
    File3.close()
    FileMoi.close()
    print("Đã gom file thành công!")






# cau11()
def cau12():
    print("Câu 12: Đổi tên file gom vừa tạo thành tên mới")
    import os
    os.rename("Gom.txt", "AllFile.txt")
    print("Đã đổi tên file thành công!")

# cau12()

#Cauf 13: Tạo menu để chọn các câu trên
def menu():
    while True:
        print("1. Câu 1")
        print("2. Câu 2")
        print("3. Câu 3")
        print("4. Câu 4")
        print("5. Câu 5")
        print("6. Câu 6")
        print("7. Câu 7")
        print("8. Câu 8")
        print("9. Câu 9")
        print("10. Câu 10")
        print("11. Câu 11")
        print("12. Câu 12")
        print("13. Thoát")

        chon = int(input("Chọn câu: "))
        if chon == 1:
            cau1()
        elif chon == 2:
            cau2()
        elif chon == 3:
            cau3()
        elif chon == 4:
            cau4()
        elif chon == 5:
            cau5()
        elif chon == 6:
            cau6()
        elif chon == 7:
            cau7()
        elif chon == 8:
            cau8()
        elif chon == 9:
            cau9()
        elif chon == 11:
            cau11()
        elif chon == 12:
            cau12()
        elif chon == 13:
            break
            exit()
        else:
            print("Nhập sai! Vui lòng chọn lại!")

menu()


























