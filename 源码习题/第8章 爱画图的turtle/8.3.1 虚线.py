import turtle

#虚线
for i in range(40):
    turtle.pendown()
    turtle.forward(5)
    turtle.penup()
    turtle.forward(5)

#虚线的圆
for i in range(0,40):
    turtle.pendown()
    turtle.circle(50,360/40/2)
    turtle.penup()
    turtle.circle(50,360/40/2)
turtle.done()
