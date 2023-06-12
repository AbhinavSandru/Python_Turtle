import turtle
turtle.bgcolor("pink")
turtle.color("red")
turtle.pensize(10)
for angle in range(0,360,30):
    turtle.seth(angle)
    turtle.circle(100)
