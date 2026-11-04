import turtle
import colorsys

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")

# Turtle setup
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)
pen.hideturtle()

# Create colorful pattern
n = 180

for i in range(n):
    color = colorsys.hsv_to_rgb(i / n, 1, 1)
    pen.pencolor(color)

    for j in range(5):
        pen.forward(120)
        pen.right(144)

    pen.right(2)

turtle.done()