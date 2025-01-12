import turtle
screen = turtle.Screen()
for i in range(36):
    turtle.forward(18)
    turtle.right(10)

for i in range(36):
    turtle.forward(12)
    turtle.left(10)

turtle.penup()
turtle.goto(0,138)
turtle.pendown()

for i in range(36):
    turtle.forward(9)
    turtle.left(10)

turtle.penup()
turtle.goto(20,200)
turtle.pendown()
turtle.circle(6)

turtle.penup()
turtle.goto(-15,200)
turtle.pendown()
turtle.circle(6)

turtle.penup()
turtle.goto(-20,180)
turtle.pendown()
turtle.right(90)
for i in range(20):
    turtle.forward(4)
    turtle.left(10)

turtle.hideturtle()








screen.mainloop()