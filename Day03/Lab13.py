#Câu 13: Nhập vào một danh sách và cho biết danh sách đó có bao nhiêu số lẻ và số chẵn?
list = []
n = int(input("Nhập vào số phần tử của danh sách: "))
for i in range(n):
    list.append(int(input("Nhập vào phần tử thứ " + str(i+1) + ": ")))
even = 0
odd = 0
for i in list:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Danh sách có", even, "số chẵn và", odd, "số lẻ")
