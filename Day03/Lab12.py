
#Câu 12: Viết chương trình trò chơi đoán số vừa nhập, cho đoán tối đa 5 lần.
import random
number = random.randint(1, 100)
# print("Số cần đoán là: ", number)
count = 0
while count < 5:
    count += 1
    guess = int(input("Hãy đoán số từ 1 đến 100: "))
    if guess < number:
        print("Số bạn đoán nhỏ hơn số cần đoán")
    elif guess > number:
        print("Số bạn đoán lớn hơn số cần đoán")
    else:
        print("Chúc mừng, bạn đã đoán đúng số cần tìm")
        break
