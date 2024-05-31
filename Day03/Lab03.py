#Câu 3: Tính chu vi và diện tích hình tròn, hình tam giác. Kiểm tra điều kiện của chúng.
print("\nCâu 3: Tính chu vi và diện tích hình tròn, hình tam giác. Kiểm tra điều kiện của chúng.")
import math
print("1. Tính chu vi và diện tích hình tròn")
radius = float(input("Nhập bán kính hình tròn: "))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print("Chu vi hình tròn là: ", perimeter)
print("Diện tích hình tròn là: ", area)

print("\n2. Tính chu vi và diện tích hình tam giác")
a = float(input("Nhập cạnh a của tam giác: "))
b = float(input("Nhập cạnh b của tam giác: "))
c = float(input("Nhập cạnh c của tam giác: "))
Chuvi = a + b + c
print("Chu vi hình tam giác là: ", Chuvi)
p = Chuvi / 2
area = math.sqrt(p * (p - a) * (p - b) * (p - c))
print("Diện tích hình tam giác là: ", area)
