
import turtle
import math
import colorsys

# Create the screen
screen = turtle.Screen()
screen.setup(900, 800)
screen.bgcolor("black")
screen.title("Aesthetic Butterfly 🦋")
screen.tracer(0)

# Create the turtle pen
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)
pen.hideturtle()

# Butterfly animation settings
first = True
steps = 4000

for i in range(steps):
    t = i * 0.02

    # Butterfly curve
    r = (
        math.exp(math.cos(t))
        - 2 * math.cos(4 * t)
        + math.sin(t / 12) ** 5
    )

    # Calculate coordinates
    x = math.sin(t) * r * 90
    y = math.cos(t) * r * 90

    # Generate rainbow colors
    hue = (i / steps) % 1
    color = colorsys.hsv_to_rgb(hue, 0.8, 1)

    pen.pencolor(color)

    # Draw the butterfly
    if first:
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        first = False
    else:
        pen.goto(x, y)

    # Update the animation
    if i % 2 == 0:
        screen.update()

# Final update
screen.update()

# Keep the window open
turtle.done()
