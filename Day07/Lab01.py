from turtle import *

# Đặt tốc độ vẽ
speed(1000)


def gotoo(x, y):
    penup()
    goto(x, y)
    pendown()


def VetrucToaDo():
    # Vẽ trục y
    penup()
    goto(0, -1000)  # Điểm bắt đầu của trục y
    pendown()
    goto(0, 1000)  # Điểm kết thúc của trục y

    # Vẽ trục x
    penup()
    goto(-1000, 0)  # Điểm bắt đầu của trục x
    pendown()
    goto(1000, 0)  # Điểm kết thúc của trục x
    penup()
    goto(0, 0)
    pendown()


def VeHinhVuong():
    gotoo(10, 10)

    # vẽ hình vuông A viền màu đỏ
    color("red")
    pensize(20)
    for i in range(4):
        forward(100)
        left(90)
    end_fill()

    # vẽ hình vuông B nhỏ hơn bên trong hình vuông A, viền màu xanh
    gotoo(20, 20)
    color("blue")
    pensize(5)
    for i in range(4):
        forward(80)  # vẽ 80 bước
        left(90)  # quay 90 độ
    end_fill()

    # vẽ hình vuông C nhỏ  bên ngoài hình vuông A, viền màu CAM
    gotoo(0, 0)
    color("orange")
    pensize(5)
    for i in range(4):
        forward(120)  # vẽ 120 bước
        left(90)  # quay 90 độ
    end_fill()


def VeDuongThang(toadoX1, toadoY1, toadoX2, toadoY2, colorLine="green", size=5):
    penup()
    goto(toadoX1, toadoY1)
    pendown()
    color(colorLine)
    pensize(size)
    goto(toadoX2, toadoY2)



def Bai02():


    VeDuongThang(2.04, -151.5, 2.04, -1.5, "black", 3)
    VeDuongThang(0, -151.5, 100, -151.5, "black", 3)
    VeDuongThang(0, -1.5, 100, -1.5, "black", 3)
    VeDuongThang(98.55, -0.61, 98.55, -62.66, "black", 3)
    VeDuongThang(97.06, -62.66, 120.56, -62.66, "black", 3)
    VeDuongThang(98.55, -90.68, 98.55, -152.74, "black", 3)
    VeDuongThang(97.06, -89.45, 120.56, -89.45, "black", 3)
    VeDuongThang(119.15, -49.77, 119.15, -63.55, "black", 3)
    VeDuongThang(122.04, -87.72, 122.04, -101.51, "black", 3)
    VeDuongThang(118.41, -51.31, 161.49, -77, "black", 3)
    VeDuongThang(122.23, -99.74, 160.1, -76.77, "black", 3)

    # Vẽ tam giác màu đỏ
    color("red")
    begin_fill()
    gotoo(50, -64.25)
    gotoo(31.95, -97.55)
    gotoo(68.05, -97.55)
    gotoo(50, -64.25)
    end_fill()

def VeHinhChuNhat(toadoX, toadoY, width, height, colorFill):
    color(colorFill)
    penup()
    goto(toadoX, toadoY)
    pendown()
    begin_fill()
    for _ in range(2):
        forward(width)
        right(90)
        forward(height)
        right(90)
    end_fill()

def VeHinhTron(x, y, radius, colorLine, size):
    penup()
    goto(x, y - radius)
    pendown()
    color(colorLine)
    pensize(size)
    circle(radius)


def Bai03():
    # Vẽ các hình chữ nhật xanh lá cây
    VeHinhChuNhat(-50, 200, 500, 300, "#00a651")
    VeHinhChuNhat(450, 40, 80, 140, "#00a651")

    # cửa sổ 1
    VeDuongThang(151.5, 2.04, 1.5, 2.04, "red", 3)
    VeDuongThang(151.5, 0, 151.5, 100, "red", 3)
    VeDuongThang(1.5, 0, 1.5, 100, "red", 3)
    VeDuongThang(0.61, 98.55, 62.66, 98.55, "red", 3)
    VeDuongThang(62.66, 97.06, 62.66, 120.56, "red", 3)
    VeDuongThang(90.68, 98.55, 152.74, 98.55, "red", 3)
    VeDuongThang(89.45, 97.06, 89.45, 120.56, "red", 3)
    VeDuongThang(49.77, 119.15, 63.55, 119.15, "red", 3)
    VeDuongThang(87.72, 122.04, 101.51, 122.04, "red", 3)
    VeDuongThang(51.31, 118.41, 77, 161.49, "red", 3)
    VeDuongThang(99.74, 122.23, 76.77, 160.1, "red", 3)

    # cửa sổ 2
    VeDuongThang(401.5, 2.04, 251.5, 2.04, "red", 3)
    VeDuongThang(401.5, 0, 401.5, 100, "red", 3)
    VeDuongThang(251.5, 0, 251.5, 100, "red", 3)
    VeDuongThang(250.61, 98.55, 312.66, 98.55, "red", 3)
    VeDuongThang(312.66, 97.06, 312.66, 120.56, "red", 3)
    VeDuongThang(340.68, 98.55, 402.74, 98.55, "red", 3)
    VeDuongThang(339.45, 97.06, 339.45, 120.56, "red", 3)
    VeDuongThang(299.77, 119.15, 313.55, 119.15, "red", 3)
    VeDuongThang(337.72, 122.04, 351.51, 122.04, "red", 3)
    VeDuongThang(301.31, 118.41, 327, 161.49, "red", 3)
    VeDuongThang(349.74, 122.23, 326.77, 160.1, "red", 3)

    # bánh xe 1
    VeHinhTron(50, -100, 41, "#2e3192", 5)
    VeHinhTron(50, -100, 36, "#27aae1", 5)
    VeHinhTron(50, -100, 32, "#2e3192", 5)
    # bánh xe 2
    VeHinhTron(350, -100, 41, "#2e3192", 5)
    VeHinhTron(350, -100, 36, "#27aae1", 5)
    VeHinhTron(350, -100, 32, "#2e3192", 5)


def draw_heart():
    color("red")

    penup()
    goto(0, -100)
    pendown()

    begin_fill()
    left(120)
    forward(180)
    circle(-100, 200)
    left(100)
    circle(-100, 200)
    forward(180)
    end_fill()

    penup()
    home()

def draw_heart2():
    color("#c44e97")

    penup()
    goto(300, -100)

    begin_fill()
    left(140)
    forward(180)
    circle(-100, 200)
    left(120)
    circle(-100, 200)
    forward(180)
    end_fill()

    penup()
    home()

draw_heart()
# draw_heart2()
VetrucToaDo()
done()
