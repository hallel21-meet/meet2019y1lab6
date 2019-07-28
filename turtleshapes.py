import turtle

num_pts = 36
for i in range(num_pts):
    turtle.left(360/num_pts)
    turtle.forward(10)

turtle.mainloop()
