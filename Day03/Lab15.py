
#Câu 15: Tìm số lớn nhất trong danh sách
list = []
n = int(input("Nhập vào số phần tử của danh sách: "))
for i in range(n):
    list.append(int(input("Nhập vào phần tử thứ " + str(i+1) + ": ")))
max = list[0]
for i in list:
    if i > max:
        max = i
print("Số lớn nhất trong danh sách là", max)