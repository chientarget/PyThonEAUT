# Câu 10: Nhập vào một số và kiểm tra xem có phải là số nguyên tố không?
print("\nCâu 10: Nhập vào một số và kiểm tra xem có phải là số nguyên tố không?")
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
