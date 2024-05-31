
#Câu 2: Tính diện tích hình chữ nhật, hình vuông, hình bình hành và hình thang cân.
print("\nCâu 2: Tính diện tích hình chữ nhật, hình vuông, hình bình hành và hình thang cân.")
print("1. Tính diện tích hình chữ nhật")
width = float(input("Nhập chiều rộng hình chữ nhật: "))
height = float(input("Nhập chiều cao hình chữ nhật: "))
area = width * height
print("Diện tích hình chữ nhật là: ", area)

print("\n2. Tính diện tích hình vuông")
side = float(input("Nhập cạnh hình vuông: "))
area = side * side
print("Diện tích hình vuông là: ", area)

print("\n3. Tính diện tích hình bình hành")
base = float(input("Nhập đáy hình bình hành: "))
height = float(input("Nhập chiều cao hình bình hành: "))
area = base * height
print("Diện tích hình bình hành là: ", area)

print("\n4. Tính diện tích hình thang cân")
base1 = float(input("Nhập đáy nhỏ hình thang cân: "))
base2 = float(input("Nhập đáy lớn hình thang cân: "))
height = float(input("Nhập chiều cao hình thang cân: "))
area = (base1 + base2) * height / 2
print("Diện tích hình thang cân là: ", area)
