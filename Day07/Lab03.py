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


def LoHoa():
    color('green', 'green')
    begin_fill()
    circle(50)
    end_fill()

    gotoo(-10, 50)

    pendown()
    begin_fill()
    for _ in range(2):
        forward(20)
        left(90)
        forward(100)
        left(90)
    end_fill()
    penup()
    gotoo(-2, -2)

    pendown()
    begin_fill()
    for _ in range(2):
        forward(10)
        left(90)
        forward(2)
        left(90)
    end_fill()
    penup()
    gotoo(0,0)


def draw_flower():
    gotoo(-50, 250)
    color('red', 'yellow')
    begin_fill()
    for _ in range(36):
        forward(100)
        left(170)

    end_fill()

def draw_vase():
    gotoo(0, 150)
    color('brown', 'brown')
    begin_fill()
    for _ in range(2):
        forward(3)
        left(90)
        forward(100)
        left(90)
    end_fill()
    gotoo(0, 0)

# VetrucToaDo()

def VELOHOA():
    draw_vase()
    LoHoa()
    draw_flower()

VELOHOA()


