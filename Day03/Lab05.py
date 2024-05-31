#Câu 5: Tìm số lớn nhất trong 3 số được nhập từ bàn phím
print("\nCâu 5: Tìm số lớn nhất trong 3 số được nhập từ bàn phím")
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))
max = a
if b > max:
    max = b
if c > max:
    max = c
print("Số lớn nhất trong 3 số", a, b, c, "là:", max)