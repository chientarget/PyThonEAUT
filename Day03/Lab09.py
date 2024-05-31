# Câu 9: In ra bảng cửu chương theo phong cách của bạn?
print("\nCâu 9: In ra bảng cửu chương theo phong cách của bạn?")
while True:
    a = int(input("Nhập số a từ 1-10: "))
    if a < 1 or a > 10:
        print("Số a không hợp lệ")
    else:
        for i in range(1, 11):
            print(a, "x", i, "=", a * i)