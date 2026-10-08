import turtle as tur
import colorsys as cs

tur.speed(0)          # Fastest drawing speed
tur.bgcolor('black')  # Background color
tur.width(2)          # Line thickness

for i in range(180):
    # Generate color using HSV model
    tur.color(cs.hsv_to_rgb(abs(i-180)/180, 1, 1))
    
    tur.forward(100)
    tur.left(60)
    tur.forward(60)
    tur.right(120)
    tur.circle(50)
    tur.forward(100)
    tur.left(60)
    tur.forward(100)
    tur.left(122)

tur.done()
