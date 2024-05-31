# Câu 5: Nhập vào một Dictionarycác phần tử.
# - Thêm phần tử vào Dictionary
# - Xóa phần tử từ Dictionary
# - Thay thế phần tử từ Dictionary
# - Sắp xếp phần tử theo key của Dictionary



print('-------------------------')
print('CRUD phần tử in Dictionary')
# Câu 5: Nhập vào một Dictionary các phần tử.
# - Thêm phần tử vào Dictionary
# - Xóa phần tử từ Dictionary
# - Thay thế phần tử từ Dictionary
# - Sắp xếp phần tử theo key của Dictionary


dic = {"a": 1, "b": 2, "c": 3}
print("Dictionary ban đầu: ", dic)
dic["d"] = 4
print("Dictionary sau khi thêm phần tử d: ", dic)
del dic["d"]
print("Dictionary sau khi xóa phần tử d: ", dic)
dic["c"] = 4
print("Dictionary sau khi thay thế phần tử c bằng 4: ", dic)
dic = dict(sorted(dic.items()))
print("Dictionary sau khi sắp xếp: ", dic)

