# Câu 3: Nhập vào một list các phần tử.
# - Thêm phần tử vào danh sách
# - Xóa phần tử từ danh sách
# - Thay thế phần tử từ danh sách
# - Sắp xếp phần tử


print('-------------------------')
print('CRUD phần tử in Danh Sách')
# Câu 3: Nhập vào một list các phần tử.
# - Thêm phần tử vào danh sách
# - Xóa phần tử từ danh sách
# - Thay thế phần tử từ danh sách
# - Sắp xếp phần tử
lst = [1, 2, 3, 4, 5]
print("Danh sách ban đầu: ", lst)

# - Thêm phần tử vào danh sách
them = int(input("Nhập phần tử cần thêm: "))
lst.append(them)
print(f"Danh sách sau khi thêm phần tử {them} : ", lst)

# - Xóa phần tử từ danh sách
xoa = int(input("Nhập phần tử cần xóa: "))
lst.remove(xoa)
print(f'Danh sách sau khi xóa phần tử: {xoa}', lst)


# - Thay thế phần tử từ danh sách

indexthay= int(input("Nhập vị trí cần thay thế: "))
giatri = int(input("Nhập giá trị thay thế: "))
lst[indexthay] = giatri
print(f"Danh sách sau khi thay thế phần tử thứ {indexthay} bằng {giatri}: ", lst)

# - Sắp xếp phần tử
lst.sort()
print("Danh sách sau khi sắp xếp: ", lst)


