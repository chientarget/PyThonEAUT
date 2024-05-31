# Câu 8: Viết chương trình chuyển đôi qua lại giữ Km -> mm
print("\nCâu 8: Viết chương trình chuyển đôi qua lại giữ Km -> mm")
Input1 = input("Nhập đơn vị câần chuyển (KM ,dm, m, cm, mm: ")
Input2 = input("Nhập đơn vị cần chuyển đến (KM ,dm, m, cm, mm: ")
Value = float(input("Nhập giá trị cần chuyển: "))
if Input1 == "km" and Input2 == "mm":
    print(Value * 1000000)
elif Input1 == "dm" and Input2 == "mm":
    print(Value * 100)
elif Input1 == "m" and Input2 == "mm":
    print(Value * 1000)
elif Input1 == "cm" and Input2 == "mm":
    print(Value * 10)
elif Input1 == "mm" and Input2 == "km":
    print(Value / 1000000)
elif Input1 == "mm" and Input2 == "dm":
    print(Value / 100)
elif Input1 == "mm" and Input2 == "m":
    print(Value / 1000)
elif Input1 == "mm" and Input2 == "cm":
    print(Value / 10)
else:
    print("Oh sai đâu rồi anh bạn !!!!!1")
