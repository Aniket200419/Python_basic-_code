
import pygame
import math

pygame.init()

# Window settings
WIDTH = 800
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Animation")

clock = pygame.time.Clock()

# Ball settings
x, y = 200, 200
radius = 25
speed_x, speed_y = 5, 4
angle = 0

# Colors
background = (15, 20, 40)
ball_color = (0, 255, 180)
white = (255, 255, 255)

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move ball
    x += speed_x
    y += speed_y
    angle += 0.08

    # Bounce from walls
    if x - radius <= 0 or x + radius >= WIDTH:
        speed_x *= -1

    if y - radius <= 0 or y + radius >= HEIGHT:
        speed_y *= -1

    # Animated background
    screen.fill(background)

    # Pulsating glow
    glow_radius = radius + int(
        8 + 4 * math.sin(angle)
    )

    pygame.draw.circle(
        screen, (20, 90, 90),
        (x, y), glow_radius + 8
    )

    # Draw ball
    pygame.draw.circle(
        screen, ball_color,
        (x, y), radius
    )

    # Highlight
    pygame.draw.circle(
        screen, white,
        (x - 8, y - 8), 6
    )

    # Title
    font = pygame.font.Font(None, 32)
    text = font.render(
        "Python Bouncing Ball Animation",
        True, white
    )
    screen.blit(text, (20, 20))

    pygame.display.flip()

pygame.quit()
