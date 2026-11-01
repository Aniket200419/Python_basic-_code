import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colorful Turtle Art")

# Turtle setup
t = turtle.Turtle()
t.speed(0)
t.width(2)

colors = ["red", "green", "blue", "yellow"]

# Draw pattern
for i in range(200):
    t.pencolor(colors[i % 4])
    t.forward(i * 2)
    t.left(91)

turtle.done()