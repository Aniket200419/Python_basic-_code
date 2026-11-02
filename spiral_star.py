import turtle
import colorsys

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")

# Turtle setup
t = turtle.Turtle()
t.speed(0)
t.width(2)

# Generate colors
h = 0

for i in range(360):
    color = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(color)

    t.forward(i * 2)
    t.left(59)

    # Draw small star
    for j in range(5):
        t.forward(20)
        t.right(144)

    h += 0.005

turtle.done()