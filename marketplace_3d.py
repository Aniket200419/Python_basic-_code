import tkinter as tk
import math

# ============================================================
# 3D MARKETPLACE - SINGLE PYTHON FILE
# ============================================================

WIDTH = 1200
HEIGHT = 750

root = tk.Tk()
root.title("3D Marketplace")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(False, False)

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, highlightthickness=0)
canvas.pack()


# ------------------------------------------------------------
# Background
# ------------------------------------------------------------
canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="#87CEEB", outline="")

# Sun
canvas.create_oval(980, 60, 1060, 140, fill="#FFD54F", outline="")

# Clouds
def cloud(x, y):
    canvas.create_oval(x, y, x+70, y+35, fill="white", outline="")
    canvas.create_oval(x+35, y-20, x+105, y+35, fill="white", outline="")
    canvas.create_oval(x+70, y, x+140, y+35, fill="white", outline="")

cloud(100, 80)
cloud(400, 120)


# ------------------------------------------------------------
# Distant buildings
# ------------------------------------------------------------
def building(x, y, w, h, color):
    # Front
    canvas.create_rectangle(
        x, y, x+w, y+h,
        fill=color,
        outline="#333333",
        width=2
    )

    # Roof
    canvas.create_polygon(
        x, y,
        x+w/2, y-45,
        x+w, y,
        fill="#5D4037",
        outline="#333333"
    )

    # Windows
    for row in range(3):
        for col in range(3):
            wx = x + 20 + col * 45
            wy = y + 25 + row * 55

            canvas.create_rectangle(
                wx, wy,
                wx+25, wy+30,
                fill="#B3E5FC",
                outline="#263238"
            )

building(40, 220, 150, 250, "#E57373")
building(220, 190, 170, 280, "#BA68C8")
building(430, 230, 150, 240, "#FFB74D")
building(620, 180, 180, 290, "#81C784")
building(840, 215, 160, 255, "#64B5F6")


# ------------------------------------------------------------
# Ground
# ------------------------------------------------------------
canvas.create_polygon(
    0, 470,
    WIDTH, 470,
    WIDTH, HEIGHT,
    0, HEIGHT,
    fill="#66BB6A",
    outline=""
)

# Road
canvas.create_polygon(
    0, 600,
    WIDTH, 500,
    WIDTH, 650,
    0, 750,
    fill="#555555",
    outline=""
)

# Road lines
for i in range(7):
    x1 = i * 210
    y1 = 665 - i * 18
    x2 = x1 + 100
    y2 = y1 - 12

    canvas.create_line(
        x1, y1,
        x2, y2,
        fill="#FFFFFF",
        width=6
    )


# ------------------------------------------------------------
# Shop function
# ------------------------------------------------------------
def shop(x, y, w, h, front_color, roof_color, name):
    # Shadow
    canvas.create_polygon(
        x+15, y+h+20,
        x+w+35, y+h+20,
        x+w+55, y+h+40,
        x+35, y+h+40,
        fill="#3E4A3E",
        outline=""
    )

    # Side wall for 3D effect
    canvas.create_polygon(
        x+w, y,
        x+w+35, y+25,
        x+w+35, y+h,
        x+w, y+h,
        fill="#795548",
        outline="#333333",
        width=2
    )

    # Main wall
    canvas.create_rectangle(
        x, y,
        x+w, y+h,
        fill=front_color,
        outline="#333333",
        width=3
    )

    # Roof
    canvas.create_polygon(
        x-15, y,
        x+w/2, y-55,
        x+w+15, y,
        fill=roof_color,
        outline="#333333",
        width=3
    )

    # Roof depth
    canvas.create_polygon(
        x+w/2, y-55,
        x+w+15, y,
        x+w+35, y+25,
        x+w/2+10, y-25,
        fill="#6D4C41",
        outline="#333333"
    )

    # Shop name
    canvas.create_rectangle(
        x+15, y+15,
        x+w-15, y+55,
        fill="#FFF3E0",
        outline="#333333"
    )

    canvas.create_text(
        x+w/2,
        y+35,
        text=name,
        font=("Arial", 14, "bold"),
        fill="#263238"
    )

    # Door
    canvas.create_rectangle(
        x+w/2-25,
        y+h-100,
        x+w/2+25,
        y+h,
        fill="#4E342E",
        outline="#222222",
        width=2
    )

    # Door knob
    canvas.create_oval(
        x+w/2+10,
        y+h-55,
        x+w/2+16,
        y+h-49,
        fill="#FFD54F",
        outline=""
    )

    # Windows
    for wx in [x+25, x+w-70]:
        canvas.create_rectangle(
            wx, y+80,
            wx+45, y+130,
            fill="#81D4FA",
            outline="#263238",
            width=2
        )

        canvas.create_line(
            wx+22, y+80,
            wx+22, y+130,
            fill="#263238",
            width=2
        )

        canvas.create_line(
            wx, y+105,
            wx+45, y+105,
            fill="#263238",
            width=2
        )


# ------------------------------------------------------------
# Marketplace Shops
# ------------------------------------------------------------
shop(90, 350, 190, 190, "#FFCC80", "#E65100", "FRUIT SHOP")
shop(320, 340, 200, 200, "#90CAF9", "#1565C0", "GROCERY")
shop(560, 350, 200, 190, "#A5D6A7", "#2E7D32", "CLOTH SHOP")
shop(800, 340, 200, 200, "#CE93D8", "#6A1B9A", "CAFE")


# ------------------------------------------------------------
# Fruit boxes
# ------------------------------------------------------------
def fruit_box(x, y):
    canvas.create_rectangle(
        x, y,
        x+65, y+45,
        fill="#8D6E63",
        outline="#4E342E",
        width=2
    )

    # Apples
    for dx, dy, color in [
        (10, 5, "#E53935"),
        (30, 8, "#43A047"),
        (48, 5, "#FDD835"),
        (20, 22, "#FB8C00"),
        (43, 24, "#E53935")
    ]:
        canvas.create_oval(
            x+dx, y+dy,
            x+dx+16, y+dy+16,
            fill=color,
            outline=""
        )

fruit_box(120, 490)
fruit_box(205, 490)


# ------------------------------------------------------------
# Cafe tables
# ------------------------------------------------------------
def table(x, y):
    canvas.create_oval(
        x, y,
        x+55, y+25,
        fill="#795548",
        outline="#3E2723",
        width=2
    )

    canvas.create_line(
        x+27, y+20,
        x+27, y+60,
        fill="#3E2723",
        width=5
    )

    # Chairs
    canvas.create_rectangle(
        x-15, y+25,
        x, y+55,
        fill="#D84315",
        outline="#3E2723"
    )

    canvas.create_rectangle(
        x+55, y+25,
        x+70, y+55,
        fill="#D84315",
        outline="#3E2723"
    )

table(850, 510)
table(920, 510)


# ------------------------------------------------------------
# People
# ------------------------------------------------------------
def person(x, y, shirt="#1976D2"):
    # Shadow
    canvas.create_oval(
        x-15, y+70,
        x+20, y+80,
        fill="#444444",
        outline=""
    )

    # Head
    canvas.create_oval(
        x-10, y,
        x+12, y+25,
        fill="#FFCC80",
        outline="#5D4037"
    )

    # Hair
    canvas.create_arc(
        x-10, y,
        x+12, y+20,
        start=0,
        extent=180,
        fill="#4E342E",
        outline=""
    )

    # Body
    canvas.create_polygon(
        x-15, y+25,
        x+17, y+25,
        x+22, y+60,
        x-20, y+60,
        fill=shirt,
        outline="#263238"
    )

    # Legs
    canvas.create_line(
        x-8, y+60,
        x-12, y+80,
        fill="#263238",
        width=6
    )

    canvas.create_line(
        x+8, y+60,
        x+13, y+80,
        fill="#263238",
        width=6
    )

    # Arms
    canvas.create_line(
        x-13, y+30,
        x-30, y+50,
        fill="#FFCC80",
        width=5
    )

    canvas.create_line(
        x+14, y+30,
        x+30, y+50,
        fill="#FFCC80",
        width=5
    )


person(270, 570, "#F44336")
person(510, 590, "#FF9800")
person(780, 570, "#3F51B5")
person(1040, 570, "#009688")


# ------------------------------------------------------------
# Trees
# ------------------------------------------------------------
def tree(x, y):
    # Shadow
    canvas.create_oval(
        x-35, y+55,
        x+45, y+75,
        fill="#4E6B50",
        outline=""
    )

    # Trunk
    canvas.create_rectangle(
        x-10, y+20,
        x+10, y+70,
        fill="#795548",
        outline="#4E342E"
    )

    # Leaves
    canvas.create_oval(
        x-45, y-25,
        x+25, y+45,
        fill="#2E7D32",
        outline="#1B5E20"
    )

    canvas.create_oval(
        x-15, y-45,
        x+55, y+35,
        fill="#388E3C",
        outline="#1B5E20"
    )

    canvas.create_oval(
        x-65, y-5,
        x+5, y+55,
        fill="#43A047",
        outline="#1B5E20"
    )


tree(50, 510)
tree(1100, 500)


# ------------------------------------------------------------
# Market Sign
# ------------------------------------------------------------
canvas.create_polygon(
    430, 80,
    770, 80,
    800, 125,
    400, 125,
    fill="#6D4C41",
    outline="#3E2723",
    width=4
)

canvas.create_text(
    600, 103,
    text="WELCOME TO CITY MARKET",
    font=("Arial", 25, "bold"),
    fill="#FFFFFF"
)


# ------------------------------------------------------------
# Small decorative lights
# ------------------------------------------------------------
for x in range(430, 780, 50):
    canvas.create_line(
        x, 130,
        x, 160,
        fill="#333333",
        width=2
    )

    canvas.create_oval(
        x-7, 155,
        x+7, 169,
        fill="#FFD54F",
        outline="#795548"
    )


# ------------------------------------------------------------
# Title
# ------------------------------------------------------------
canvas.create_text(
    600, 720,
    text="3D MARKETPLACE • PYTHON GRAPHICS",
    font=("Arial", 18, "bold"),
    fill="white"
)


root.mainloop()