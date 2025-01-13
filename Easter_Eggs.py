import turtle
screen = turtle.Screen()
      
screen.bgcolor("pink")
turtle.speed(0)
turtle.hideturtle()

def draw_egg(x, y, size, tilt):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    turtle.setheading(270 + tilt)
    turtle.color("red")
    turtle.circle(size, 180)
    turtle.color("blue")
    turtle.circle(size*2, 45)
    turtle.color("green")
    turtle.circle(0.6*size, 90)
    turtle.color("blue")
    turtle.circle(2*size, 45)

draw_egg(-50, -50, 50, -90)
draw_egg(0, 100, 60, 180)
draw_egg(100, 0, 25, 20)

screen.mainloop()