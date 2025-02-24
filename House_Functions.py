import turtle
turtle.speed(10)
screen = turtle.Screen()
screen.setup(600, 1000)

def my_window(c):
    turtle.color(c)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill()

def my_house(c):
    turtle.color(c)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(300)
        turtle.left(90)
    turtle.end_fill()

def my_door(c):
    turtle.color(c)
    turtle.begin_fill()
    for i in range(2):
        turtle.left(90)
        turtle.forward(150)
        turtle.left(90)
        turtle.forward(60)
    turtle.end_fill()

def house_top(c):
    turtle.setheading(0)
    turtle.color(c)
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(300)
        turtle.left(120)
    turtle.end_fill()

def grass(c):
    turtle.setheading(90)
    turtle.color(c)
    turtle.begin_fill()
    for i in range(23):
        turtle.forward(50)
        turtle.right(165)
        turtle.forward(51.7)
        turtle.left(165)
    turtle.end_fill()

def pen(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

pen(-100, -100)
my_house("pink") 
pen(50, -100)
my_door("yellow")
pen(80, 70)
my_window("light blue")
pen(-100, -110)
grass("green")
pen(-100, 200)
house_top("yellow")

screen.mainloop()