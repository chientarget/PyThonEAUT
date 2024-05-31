#Câu 4: Nhập vào một số tự nhiên bất kỳ, kiểm tra số chẵn lẻ?
print("\nCâu 4: Nhập vào một số tự nhiên bất kỳ, kiểm tra số chẵn lẻ?")
number = int(input("Nhập vào một số tự nhiên: "))
if number % 2 == 0:
    print("Số", number, "là số chẵn.")
else:
    print("Số", number, "là số lẻ.")