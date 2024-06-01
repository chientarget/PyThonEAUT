import random
from turtle import *

speed(1000)


def gotoo(x, y):
    penup()
    goto(x, y)
    pendown()


def VetrucToaDo():
    # Vẽ trục y
    penup()
    goto(0, -1000)
    pendown()
    goto(0, 1000)

    # Vẽ trục x
    penup()
    goto(-1000, 0)
    pendown()
    goto(1000, 0)
    penup()
    goto(0, 0)
    pendown()

def VeVuon():

    gotoo(-1000, 0)
    color("green", "green")
    begin_fill()
    for _ in range(2):
        forward(1000)
        left(90)
        forward(1000)
        left(90)
    end_fill()


def VeMatTroi():
    penup()
    goto(-400, 350)  # Đặt tọa độ cho mặt trời
    pendown()
    color("yellow")  # Màu vàng cho mặt trời
    begin_fill()
    circle(50)  # Vẽ một hình tròn với bán kính là 50
    end_fill()
def VeNha():
    # Vẽ thân nhà (hình chữ nhật)
    gotoo(-300, 150)  # Tăng tọa độ y từ 50 lên 150
    color("black", "lightblue")
    begin_fill()
    for _ in range(2):
        forward(200)
        left(90)
        forward(150)
        left(90)
    end_fill()

    # Vẽ mái nhà (hình tam giác)
    gotoo(-300, 300)  # Tăng tọa độ y từ 200 lên 300
    color("black", "brown")
    begin_fill()
    forward(200)
    left(120)
    forward(200)
    left(120)
    forward(200)
    left(120)
    end_fill()

    # Vẽ cửa chính
    gotoo(-230, 150)  # Tăng tọa độ y từ 50 lên 150
    color("black", "darkred")
    begin_fill()
    for _ in range(2):
        forward(60)
        left(90)
        forward(100)
        left(90)
    end_fill()

    # Vẽ cửa sổ bên trái
    gotoo(-280, 250)  # Tăng tọa độ y từ 150 lên 250
    color("black", "white")
    begin_fill()
    for _ in range(4):
        forward(40)
        right(90)
    end_fill()

    # Vẽ cửa sổ bên phải
    gotoo(-160, 250)  # Tăng tọa độ y từ 150 lên 250
    color("black", "white")
    begin_fill()
    for _ in range(4):
        forward(40)
        right(90)
    end_fill()




def VeHangRao():
    # Rào dài ngang 1
    gotoo(-500, 10)
    color("black", "brown")
    pensize(1)
    begin_fill()
    for _ in range(2):
        forward(500)
        left(90)
        forward(10)
        left(90)
    end_fill()

    # Rào dài ngang 2
    gotoo(-500, 30)
    color("black", "brown")
    pensize(1)
    begin_fill()
    for _ in range(2):
        forward(500)
        left(90)
        forward(10)
        left(90)
    end_fill()

    # Vẽ cột hàng rào
    for x in range(-500, 0, 30):
        gotoo(x, 0)
        color("black", "brown")
        begin_fill()
        for _ in range(2):
            forward(10)
            left(90)
            forward(50)
            left(90)
        end_fill()






# vẽ đường đi x= -1000, y= -350 dến x= 1000 y = -150
def VeDuongDi():
    gotoo(-1000, -150)
    color("brown")
    pensize(100)
    begin_fill()
    forward(2000)
    end_fill()
    gotoo(0,0)

def VeXeOto():
    pensize(5)
    gotoo(-150, -150)
    color("black", "red")
    begin_fill()
    forward(300)
    left(90)
    forward(60)
    left(90)
    forward(300)
    left(90)
    forward(60)
    left(90)
    end_fill()

    # Vẽ nóc xe (hình chữ nhật nhỏ hơn)
    gotoo(-100, -90)
    color("black", "orange")
    begin_fill()
    forward(200)
    left(90)
    forward(40)
    left(90)
    forward(200)
    left(90)
    forward(40)
    left(90)
    end_fill()

    # Vẽ bánh xe (hình tròn)
    gotoo(-100, -160)
    color("black", "black")
    begin_fill()
    circle(20)
    end_fill()

    gotoo(90, -160)
    begin_fill()
    circle(20)
    end_fill()


def VeSong():
    speed(0)
    hideturtle()
    penup()
    goto(-500, -400)
    pendown()
    fillcolor("blue")
    begin_fill()

    # Draw the zigzag river
    for x in range(-500, 501, 100):
        if (x // 100) % 2 == 0:
            goto(x, -300)
        else:
            goto(x, -400)


    goto(500, -400)
    goto(500, -300)
    goto(-500, -300)
    end_fill()



def VeCau():
    penup()
    goto(-100, -400)  # Start at the left side of the river
    pendown()
    fillcolor("brown")
    begin_fill()


    goto(-100, -300)  # Up
    goto(100, -300)   # Right
    goto(100, -400)   # Down
    goto(-100, -400)  # Left
    end_fill()



VetrucToaDo()

VeVuon()
VeMatTroi()
VeNha()
VeHangRao()

VeDuongDi()

VeXeOto()
VeSong()
VeCau()

done()

