# Câu 2: Nhập một danh sách các phần tử (nhập số), và tính tổng và tích của các phần tử đó.


print('-------------------------')
print('Nhập một danh sách các phần tử (nhập số), và tính tổng và tích của các phần tử đó.')
# Câu 2: Nhập một danh sách các phần tử (nhập số), và tính tổng và tích của các phần tử đó.
n = int(input("Nhập số phần tử: "))
lst = []
for i in range(n):
    lst.append(int(input("Nhập phần tử thứ " + str(i + 1) + ": ")))
print("Tổng các phần tử trong danh sách là: ", sum(lst))
tich = 1
for i in lst:
    tich *= i
print("Tích các phần tử trong danh sách là: ", tich)