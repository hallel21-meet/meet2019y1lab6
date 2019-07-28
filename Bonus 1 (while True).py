import turtle
turtle.tracer(1)
rounds = 10
size = 10
z = turtle.clone()
b = turtle.clone()
turtle.bgcolor("light blue")
turtle.hideturtle()
z.color("white")
b.color("black")
b.goto(5,5)
while True:
    z.forward(size)
    z.left(145)
    b.forward(-size)
    b.left(-145)
    size += 10
turtle.mainloop()
