# Sử dụng Hàm và MENU để thực hiện
# 1.    Tính tổng số tiền của 250 000 con Gà cần mua vào mỗi mùa với số Gà được nhập từ SG (giá 15 nghìn/con):
# Biết:
# + Mua vào mùa Xuân: giá tăng 15%
# + Mua vào mùa Hè: giá giảm 10%
# + Mua vào mùa Thu: giá tăng 25%
# + Mua vào mùa Đông: giá giảm 40%
# Từ đó hãy cho biết nên mua gà vào mùa nào là hợp lý?
# 2.    Tính Tổng và Hiệu của các số chắn và số lẻ được nhập từ bàn phím với 10 số.
# 3.    Tính số lượng gà và chuột biết có tổng 50 con và 100 chân.
# 4.    Tính số lượng Chó và Gà biết có Hiệu giữa chúng là 72 con và có 100 chân với Số Gà nhiều hơn Chó.
# 5.    Chuyển đổi nhiệt độ từ độ C sang độ F và ngược lại.
# 6.    Kiểm tra xem một năm sinh của bạn có phải là năm nhuận hay không và cho biết tuổi của bạn.
# 7.    Tìm ước số chung lớn nhất và bội số chung nhỏ nhất của 2 số.
# 8.    Chuyển đổi giữa hệ thập phân sang nhị phân, và ngược lại.
# 9.    Viết chương trình tìm giao điểm của 2 đường thẳng
# 10.    Tìm số xuất hiện nhiều và ít nhất trong một danh sách.
# 11.    Tìm số lớn thứ 2 và nhỏ thứ 2 trong một danh sách.
# 12.    Tính toán diện tích và chu vi các hình học khác như hình thang, hình bình hành.
# 13.    Viết chương trình tính tổng, tích, trung bình của các số trong một danh sách.
# 14.    Viết chương trình đọc số, ví dụ nhập 1 hiển thị là Một (sử dụng switch).
# 15.     Viết chương trình để giải bậc nhất
# 16.    Viết chương trình để giải phương trình bậc 2
# 17.     Bổ sung thêm 5 câu và tự giản
#


#Bài 1
def mua_ga():
    SG = int(input("Nhập số gà: "))
    mua_xuan = SG * 15000 * 1.15
    mua_he = SG * 15000 * 0.9
    mua_thu = SG * 15000 * 1.25
    mua_dong = SG * 15000 * 0.6
    print(f"Mua vào mùa Xuân: {mua_xuan}")
    print(f"Mua vào mùa Hè: {mua_he}")
    print(f"Mua vào mùa Thu: {mua_thu}")
    print(f"Mua vào mùa Đông: {mua_dong}")
    if mua_xuan < mua_he and mua_xuan < mua_thu and mua_xuan < mua_dong:
        print("Nên mua vào mùa Xuân")
    elif mua_he < mua_xuan and mua_he < mua_thu and mua_he < mua_dong:
        print("Nên mua vào mùa Hè")
    elif mua_thu < mua_xuan and mua_thu < mua_he and mua_thu < mua_dong:
        print("Nên mua vào mùa Thu")
    else:
        print("Nên mua vào mùa Đông")

#Bài 2
def tong_hieu_chan_le():
    tong_chan = 0
    tong_le = 0
    hieu_chan = 0
    hieu_le = 0
    for i in range(10):
        n = int(input(f"Nhập số thứ {i + 1}: "))
        if n % 2 == 0:
            tong_chan += n
            hieu_chan -= n
        else:
            tong_le += n
            hieu_le -= n

    print(f"Tổng số chẵn: {tong_chan}")
    print(f"Tổng số lẻ: {tong_le}")

    print(f"Hiệu số chẵn: {hieu_chan}")
    print(f"Hiệu số lẻ: {hieu_le}")


#Bài 3
def ga_chuot():
    sl = 50
    tc = 160
    for ga in range(1, 51):
        chuot = sl - ga
        if ga * 2 + chuot * 4 == tc:
            print(f"Số gà: {ga}")
            print(f"Số chuột: {chuot}")
            break


#Bài 4: Tính số lượng Chó và Gà biết có Hiệu giữa chúng là 72 con và có 100 chân với Số Gà nhiều hơn Chó.

def cho_ga():
    for cho in range(1, 50):
        ga = cho + 72
        if ga * 2 + cho * 4 == 150 and ga - cho == 72:
            print(f"Số gà: {ga}")
            print(f"Số chó: {cho}")
            break



#Bài 5: Chuyển đổi nhiệt độ từ độ C sang độ F và ngược lại.
def doC_to_doF():
    doC = float(input("Nhập độ C: "))
    doF = doC * 9 / 5 + 32
    print(f"{doC} độ C = {doF} độ F")

def doF_to_doC():
    doF = float(input("Nhập độ F: "))
    doC = (doF - 32) * 5 / 9
    print(f"{doF} độ F = {doC} độ C")

#Bài 6: Kiểm tra xem một năm sinh của bạn có phải là năm nhuận hay không và cho biết tuổi của bạn.
def nam_nhuan():
    nam = int(input("Nhập năm sinh: "))
    tuoi = 2024 - nam
    if nam % 4 == 0 or nam % 400 == 0:
        print("Năm nhuận")
    else:
        print("Năm không nhuận")
    print(f"Tuổi của bạn: {tuoi}")


#Bai 07:: Tìm ước số chung lớn nhất và bội số chung nhỏ nhất của 2 số.
def uscln(a, b):
    if a == 0 or b == 0:
        return a + b
    while a != b:
        if a > b:
            a -= b

        else:
            b -= a

    print(a)
    return a

def bscnn(a, b):
    return a * b / uscln(a, b)


#Bai 08: Chuyển đổi giữa hệ thập phân sang nhị phân, và ngược lại.
def thap_phan_to_nhi_phan():
    n = int(input("Nhập số thập phân: "))
    print(bin(n)[2:])

def nhi_phan_to_thap_phan():
    n = input("Nhập số nhị phân: ")
    print(int(n, 2))


#Bai 10: Tìm số xuất hiện nhiều và ít nhất trong một danh sách.

def nhieu_it():
    n = int(input("Nhập số phần tử: "))
    a = []
    for i in range(n):
        a.append(int(input(f"Nhập số thứ {i + 1}: ")))

    max = 0
    min = 0
    for i in range(n):
        if a.count(a[i]) > a.count(a[max]):
            max = i

        if a.count(a[i]) < a.count(a[min]):
            min = i

    print(f"Số xuất hiện nhiều nhất: {a[max]}")
    print(f"Số xuất hiện ít nhất: {a[min]}")


def main_menu():
    while True:
        print("1. Mua gà")
        print("2. Tổng và hiệu số chẵn, số lẻ")
        print("3. Tính số lượng gà và chuột")
        print("4. Tính số lượng chó và gà")
        print("5. Chuyển đổi nhiệt độ")
        print("6. Kiểm tra năm nhuận và tuổi")
        print("7. Tìm ước số chung lớn nhất và bội số chung nhỏ nhất")
        print("8. Chuyển đổi giữa hệ thập phân sang nhị phân, và ngược lại")
        print("9. Tìm giao điểm của 2 đường thẳng")
        print("10. Tìm số xuất hiện nhiều và ít nhất trong một danh sách")
        print("0. Thoát")

        choice = int(input("Chọn một lựa chọn: "))

        if choice == 1:
            mua_ga()
        elif choice == 2:
            tong_hieu_chan_le()
        elif choice == 3:
            ga_chuot()
        elif choice == 4:
            cho_ga()
        elif choice == 5:
            doC_to_doF()
            doF_to_doC()
        elif choice == 6:
            nam_nhuan()
        elif choice == 7:
            a = int(input("Nhập số a: "))
            b = int(input("Nhập số b: "))
            print("Ước số chung lớn nhất: ", uscln(a, b))
            print("Bội số chung nhỏ nhất: ", bscnn(a, b))
        elif choice == 8:
            thap_phan_to_nhi_phan()
            nhi_phan_to_thap_phan()

        elif choice == 10:
            nhieu_it()
        elif choice == 0:
            print("Thoát chương trình")
            return
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

main_menu()