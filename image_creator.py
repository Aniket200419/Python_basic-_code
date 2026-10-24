from PIL import Image, ImageDraw, ImageFont
import random

# Image dimensions
WIDTH = 1000
HEIGHT = 700

# Create background
image = Image.new("RGB", (WIDTH, HEIGHT), "#101827")
draw = ImageDraw.Draw(image)

# Load fonts
try:
    title_font = ImageFont.truetype("arial.ttf", 48)
    text_font = ImageFont.truetype("arial.ttf", 25)
except OSError:
    title_font = ImageFont.load_default()
    text_font = ImageFont.load_default()

# Create a gradient background
for y in range(HEIGHT):
    ratio = y / HEIGHT
    r = int(16 + ratio * 35)
    g = int(24 + ratio * 10)
    b = int(39 + ratio * 80)
    draw.line((0, y, WIDTH, y), fill=(r, g, b))

# Draw random stars
for _ in range(150):
    x = random.randint(0, WIDTH - 1)
    y = random.randint(0, HEIGHT - 1)
    radius = random.randint(1, 3)
    draw.ellipse(
        (x, y, x + radius, y + radius),
        fill="white"
    )

# Draw decorative circles
draw.ellipse((100, 180, 300, 380), outline="#38BDF8", width=5)
draw.ellipse((700, 200, 900, 400), outline="#A78BFA", width=5)

# Add title and description
title = "MY IMAGE CREATOR"
subtitle = "Created with Python"

# Center the title
bbox = draw.textbbox((0, 0), title, font=title_font)
title_width = bbox[2] - bbox[0]
title_x = (WIDTH - title_width) // 2

draw.text(
    (title_x, 270),
    title,
    fill="#FFFFFF",
    font=title_font
)

bbox = draw.textbbox((0, 0), subtitle, font=text_font)
subtitle_width = bbox[2] - bbox[0]

draw.text(
    ((WIDTH - subtitle_width) // 2, 340),
    subtitle,
    fill="#38BDF8",
    font=text_font
)

# Add footer
draw.text(
    (20, HEIGHT - 45),
    "Generated using Python Pillow",
    fill="#FFFFFF",
    font=text_font
)

# Save image
filename = "created_image.png"
image.save(filename)

print("Image created successfully!")
print(f"Saved as: {filename}")

# Open the generated image
image.show()
