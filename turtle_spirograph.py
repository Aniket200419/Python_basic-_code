from turtle import *
from colorsys import *
import math

bgcolor("black")
speed(0)
pensize(2)
tracer(5)

h = 0.3
R = 220
r = 70

for layer in range(3):
    d = 90 + layer * 15
    penup()
    for i in range(600):
        theta = i * (600) * 2 * math.pi
        x = (R - r) * math.cos(theta) + d * math.cos((R - r) / r * theta)
        y = (R - r) * math.sin(theta) - d * math.sin((R - r) / r * theta)
        goto(x, y)
        color(hsv_to_rgb(h, 1, 1))
        pendown()
        h += 1 / 600
    penup()
    h += 1 / 600 * 1

hideturtle()
done()
