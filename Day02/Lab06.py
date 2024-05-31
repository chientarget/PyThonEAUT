# Câu 6: Tự ra 4 câu và  tự giải gửi lên đây
# Câu 1: Nhập vào một số n, kiểm tra xem n có phải là số nguyên tố không.
# Câu 2: Nhập vào một số n, kiểm tra xem n có phải là số chính phương không.
# Câu 3: Nhập vào một số n, kiểm tra xem n có phải là số hoàn hảo không.
# Câu 4: Nhập vào một số n, kiểm tra xem n có phải là số thuận nghịch không.

print('-------------------------')
# Câu 6: Tự ra 4 câu và  tự giải gửi lên đây

# Câu 6.1: Nhập vào một số n, kiểm tra xem n có phải là số nguyên tố không.
# Ví dụ Số nguyên tố: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, ...
while True:
    print(" Ví dụ Số nguyên tố: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, ...")
    n = int(input("Nhập số n để check số nguyên tố: "))
    if n < 2:
        print(n, "Có phải là sô nguyên tố đâu ??")
    else:
        check = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                check = False
                break
        if check:
            print(n, "là số nguyên tố")
            break
        else:
            print(n, "Có phải là sô nguyên tố đâu ??")

# Câu 6.2: Nhập vào một số n, kiểm tra xem n có phải là số chính phương không.
#        căn bậc 2 của nó là số nguyên
# Ví dụ số chính phương: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, ...

while True:
    print("Ví dụ số chính phương: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, ...")
    n = int(input("Nhập số n để check số chính phương:"))
    if n < 0:
        print(n, "không phải là số chính phương")
    else:
        if int(n ** 0.5) ** 2 == n:
            print(n, "là số chính phương ")
            break
        else:
            print(n, "Có phải là số chính phương đâu ??")

# Câu 6.3: Nhập vào một số n, kiểm tra xem n có phải là số hoàn hảo không.
#        tổng các ước của nó bằng chính nó
# Ví dụ số hoàn hảo: 6, 28, 496, 8128, ...
while True:
    print("Ví dụ số hoàn hảo: 6, 28, 496, 8128, ...")
    n = int(input("Nhập số hoàn hảo n: "))
    if n < 1:
        print(n, "Có phải là sô hoàn hảo đâu ??")
    else:
        sum = 0
        for i in range(1, n):
            if n % i == 0:
                sum += i
        if sum == n:
            print(n, "là số hoàn hảo")
            break
        else:
            print(n, "có phải là sô hoàn hảo đâu ??")


# Câu 6.4: Nhập vào một số n, kiểm tra xem n có phải là số thuận nghịch không.
#        đọc từ trái sang phải hay từ phải sang trái đều giống nhau
# Ví dụ số thuận nghịch: 121, 12321, 1234321, 123454321, ...
while True:
    print("Ví dụ số thuận nghịch: 121, 12321, 1234321, 123454321, ...")
    n = int(input("Nhập số  thuận nghịch n: "))
    if n < 0:
        print(n, "có phải là số thuận nghịch đâu ??")
    else:
        temp = n
        reverse = 0
        while n > 0:
            reverse = reverse * 10 + n % 10
            n //= 10 # là phép chia lấy phần nguyên
        if temp == reverse:
            print(temp, "là số thuận nghịch")
            break
        else:
            print(temp, "có phải là số thuận nghịch đâu ??")

