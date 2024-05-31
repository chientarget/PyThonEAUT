#Câu 11: Tính giai thừa của n, với n nhập từ bàn phím.
import math
n = int(input("Nhập vào số n: "))
def giaiThua(n):
    if n == 0:
        return 1
    else:
        return n * giaiThua(n-1)

print("Giai thừa của", n, "là", giaiThua(n))
