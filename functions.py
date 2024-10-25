# defining the players moves
import turtle
circle = turtle.Turtle()
circle.penup()
circle.hideturtle()
circle.speed(0)
circle.color('red')
circle.width(4)
x = turtle.Turtle()
x.penup()
x.hideturtle()
x.speed(0)
x.color('black')
x.width(4)


def A10():
    circle.setposition(-137.5, 165.5)
    circle.pendown()
    for i in range(120):
        circle.fd(2)
        circle.right(3)
    circle.penup()


def A20():
    circle.setposition(0, 165.5)
    circle.width(4)
    circle.pendown()
    for i in range(120):
        circle.fd(2)
        circle.right(3)
    circle.penup()


def A30():
    circle.setposition(137.5, 165.5)
    circle.pendown()
    for i in range(120):
        circle.fd(2)
        circle.right(3)
    circle.penup()


def B10():
    circle.setposition(-137.5, 27.5)
    circle.pendown()
    for i in range(120):
        circle.fd(2)
        circle.right(3)
    circle.penup()


def B20():
    circle.setposition(0, 27.5)
    circle.pendown()
    for i in range(120):
        circle.fd(2)
        circle.right(3)
    circle.penup()


def B30():
    circle.setposition(137.5, 27.5)
    circle.pendown()
    for i in range(120):
        circle.fd(2)
        circle.right(3)
    circle.penup()


def C10():
    circle.setposition(-137.5, -165.5)
    circle.pendown()
    for i in range(120):
        circle.fd(2)
        circle.left(3)
    circle.penup()


def C20():
    circle.setposition(0, -165.5)
    circle.pendown()
    for i in range(120):
        circle.fd(2)
        circle.left(3)
    circle.penup()


def C30():
    circle.setposition(137.5, -165.5)
    circle.pendown()
    for i in range(120):
        circle.fd(2)
        circle.left(3)
    circle.penup()


def A1X():
    x.setposition(-168.75, 165.5)
    x.pendown()
    x.setheading(-45)
    x.fd(75)
    x.penup()
    x.setheading(0)
    x.bk(50)
    x.setheading(45)
    x.pendown()
    x.fd(75)
    x.penup()


def A2X():
    x.setposition(-28.5, 165.5)
    x.pendown()
    x.setheading(-45)
    x.fd(75)
    x.penup()
    x.setheading(0)
    x.bk(50)
    x.setheading(45)
    x.pendown()
    x.fd(75)
    x.penup()


def A3X():
    x.setposition(110.5, 165.5)
    x.pendown()
    x.setheading(-45)
    x.fd(75)
    x.penup()
    x.setheading(0)
    x.bk(50)
    x.setheading(45)
    x.pendown()
    x.fd(75)
    x.penup()


def B1X():
    x.setposition(-168.75, 27.5)
    x.pendown()
    x.setheading(-45)
    x.fd(75)
    x.penup()
    x.setheading(0)
    x.bk(50)
    x.setheading(45)
    x.pendown()
    x.fd(75)
    x.penup()


def B2X():
    x.setposition(-28.5, 27.5)
    x.pendown()
    x.setheading(-45)
    x.fd(75)
    x.penup()
    x.setheading(0)
    x.bk(50)
    x.setheading(45)
    x.pendown()
    x.fd(75)
    x.penup()


def B3X():
    x.setposition(110.5, 27.5)
    x.pendown()
    x.setheading(-45)
    x.fd(75)
    x.penup()
    x.setheading(0)
    x.bk(50)
    x.setheading(45)
    x.pendown()
    x.fd(75)
    x.penup()


def C1X():
    x.setposition(-168.75, -110.5)
    x.pendown()
    x.setheading(-45)
    x.fd(75)
    x.penup()
    x.setheading(0)
    x.bk(50)
    x.setheading(45)
    x.pendown()
    x.fd(75)
    x.penup()


def C2X():
    x.setposition(-25, -110.5)
    x.pendown()
    x.setheading(-45)
    x.fd(75)
    x.penup()
    x.setheading(0)
    x.bk(50)
    x.setheading(45)
    x.pendown()
    x.fd(75)
    x.penup()


def C3X():
    x.setposition(110.5, -110.5)
    x.pendown()
    x.setheading(-45)
    x.fd(75)
    x.penup()
    x.setheading(0)
    x.bk(50)
    x.setheading(45)
    x.pendown()
    x.fd(75)
    x.penup()


def clear_o():
    circle.clear()


def clear_x():
    x.clear()



