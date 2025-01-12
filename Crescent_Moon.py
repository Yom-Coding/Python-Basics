import turtle 
screen = turtle.Screen()
turtle.speed(10)
screen.bgcolor("dark blue")

turtle.penup()
turtle.goto(0,-200)
turtle.color("orange")

turtle.begin_fill()
turtle.circle(200)
turtle.end_fill()

turtle.penup()
turtle.goto(50,-200)
turtle.color("dark blue")

turtle.begin_fill()
turtle.circle(200)
turtle.end_fill()

screen.mainloop()












