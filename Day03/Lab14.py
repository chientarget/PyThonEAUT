#Câu 14: Tìm số nhỏ nhất trong danh sách
list = []
n = int(input("Nhập vào số phần tử của danh sách: "))
for i in range(n):
    list.append(int(input("Nhập vào phần tử thứ " + str(i+1) + ": ")))
min = list[0]
for i in list:
    if i < min:
        min = i
print("Số nhỏ nhất trong danh sách là", min)