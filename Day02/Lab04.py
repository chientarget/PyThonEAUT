# Câu 4: Nhập vào số tự nhiên a từ 1-10, hiển thị bảng cửu chương của nó.


print('-------------------------')
print('Bảng cửu chương của số a (1-10')
# Câu 4: Nhập vào số tự nhiên a từ 1-10, hiển thị bảng cửu chương của nó.
while True:
    a = int(input("Nhập số a từ 1-10: "))
    if a < 1 or a > 10:
        print("Số a không hợp lệ")
    else:
        for i in range(1, 11):
            print(a, "x", i, "=", a * i)



