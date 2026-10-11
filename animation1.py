
"""

Controls:
    SPACE  - Pause/resume
    UP/DOWN - Change animation speed
    LEFT/RIGHT - Rotate camera
    R      - Reset animation
    ESC    - Exit
"""

import math
import random
import sys

import pygame

# -------------------- Configuration --------------------

WIDTH, HEIGHT = 1200, 800
FPS = 60
BACKGROUND = (4, 7, 20)
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Solar System Animation")
clock = pygame.time.Clock()

font = pygame.font.SysFont("consolas", 15)
title_font = pygame.font.SysFont("consolas", 25, bold=True)
small_font = pygame.font.SysFont("consolas", 12)

# -------------------- Planet Data --------------------
# name, orbital radius, planet radius, color, speed, orbit tilt

PLANETS = [
    ("Mercury", 75, 5, (170, 165, 155), 1.60, 0.10),
    ("Venus", 112, 8, (235, 180, 95), 1.20, 0.18),
    ("Earth", 153, 9, (55, 130, 255), 0.95, 0.08),
    ("Mars", 195, 7, (235, 75, 65), 0.78, 0.22),
    ("Jupiter", 250, 18, (215, 170, 125), 0.48, 0.12),
    ("Saturn", 305, 15, (225, 205, 145), 0.36, 0.19),
    ("Uranus", 355, 12, (100, 220, 220), 0.25, 0.15),
    ("Neptune", 405, 12, (70, 100, 245), 0.19, 0.10),
]

# -------------------- Background Stars --------------------

random.seed(42)

stars = []
for _ in range(350):
    stars.append((
        random.randrange(WIDTH),
        random.randrange(HEIGHT),
        random.choice([1, 1, 1, 2]),
        random.randint(90, 230),
    ))

# -------------------- 3D Projection --------------------

def project(x, y, z, camera_angle):
    """Convert a 3D point into 2D screen coordinates."""

    # Rotate the solar system around the vertical axis.
    cos_a = math.cos(camera_angle)
    sin_a = math.sin(camera_angle)

    rotated_x = x * cos_a - z * sin_a
    rotated_z = x * sin_a + z * cos_a

    # Tilt the view to create a 3D perspective.
    tilt = 0.62
    screen_y = y * math.cos(tilt) - rotated_z * math.sin(tilt)
    depth = y * math.sin(tilt) + rotated_z * math.cos(tilt)

    # Perspective scaling.
    camera_distance = 1000
    denominator = max(250, camera_distance + depth)
    scale = camera_distance / denominator

    sx = CENTER_X + rotated_x * scale
    sy = CENTER_Y + screen_y * scale

    return int(sx), int(sy), scale, depth


# -------------------- Drawing Functions --------------------

def draw_stars():
    for x, y, radius, brightness in stars:
        pygame.draw.circle(
            screen,
            (brightness, brightness, brightness),
            (x, y),
            radius,
        )


def draw_orbits(camera_angle):
    """Draw the elliptical-looking orbital paths."""

    for _, orbit_radius, _, _, _, orbit_tilt in PLANETS:
        points = []

        for i in range(181):
            angle = math.tau * i / 180

            x = orbit_radius * math.cos(angle)
            z = orbit_radius * math.sin(angle)

            # Slightly tilt each orbital plane.
            y = z * math.sin(orbit_tilt)

            sx, sy, _, _ = project(x, y, z, camera_angle)
            points.append((sx, sy))

        if len(points) > 1:
            pygame.draw.lines(
                screen,
                (37, 45, 68),
                False,
                points,
                1,
            )


def draw_glow(x, y, radius, color):
    """Draw a soft glow around a luminous object."""

    for layer in range(5, 0, -1):
        glow_radius = int(radius * (1 + layer * 0.55))
        alpha_color = tuple(
            min(255, int(component * 0.12))
            for component in color
        )

        pygame.draw.circle(
            screen,
            alpha_color,
            (x, y),
            glow_radius,
            1,
        )


def draw_sun(camera_angle, elapsed):
    sx, sy, scale, _ = project(0, 0, 0, camera_angle)
    radius = max(8, int(27 * scale))

    # Animated solar glow.
    pulse = 2 * math.sin(elapsed * 2.0)
    draw_glow(sx, sy, radius + int(pulse), (255, 165, 20))

    pygame.draw.circle(screen, (255, 120, 20), (sx, sy), radius + 3)
    pygame.draw.circle(screen, (255, 195, 35), (sx, sy), radius)
    pygame.draw.circle(
        screen,
        (255, 235, 125),
        (sx - radius // 4, sy - radius // 4),
        max(2, radius // 2),
    )


def draw_planet(name, orbit_radius, planet_radius,
                color, angle, orbit_tilt, camera_angle):

    x = orbit_radius * math.cos(angle)
    z = orbit_radius * math.sin(angle)
    y = z * math.sin(orbit_tilt)

    sx, sy, scale, depth = project(x, y, z, camera_angle)
    radius = max(2, int(planet_radius * scale))

    # Basic sphere shading.
    pygame.draw.circle(screen, color, (sx, sy), radius)

    highlight = tuple(min(255, c + 65) for c in color)
    shadow = tuple(max(0, int(c * 0.48)) for c in color)

    if radius >= 4:
        pygame.draw.circle(
            screen,
            highlight,
            (sx - radius // 3, sy - radius // 3),
            max(1, radius // 3),
        )

        pygame.draw.arc(
            screen,
            shadow,
            (sx - radius, sy - radius,
             radius * 2, radius * 2),
            math.pi / 2,
            math.pi * 1.5,
            max(1, radius // 4),
        )

    # Saturn's rings.
    if name == "Saturn":
        ring_rect = pygame.Rect(
            sx - int(radius * 1.8),
            sy - int(radius * 0.65),
            int(radius * 3.6),
            int(radius * 1.3),
        )

        pygame.draw.ellipse(screen, (170, 145, 95), ring_rect, 2)

        inner_ring = ring_rect.inflate(
            -max(2, radius // 2),
            -max(2, radius // 3),
        )

        pygame.draw.ellipse(screen, (235, 215, 165), inner_ring, 2)

    # Labels.
    label = font.render(name, True, (225, 232, 245))
    screen.blit(label, (sx + radius + 7, sy - 8))

    return depth


def draw_hud(speed, paused, camera_angle):
    title = title_font.render("3D SOLAR SYSTEM", True, (110, 200, 255))
    screen.blit(title, (22, 18))

    subtitle = small_font.render(
        "PERSPECTIVE VIEW | LIVE ORBIT SIMULATION",
        True,
        (140, 155, 180),
    )
    screen.blit(subtitle, (24, 50))

    status = "PAUSED" if paused else "ANIMATING"
    lines = [
        f"STATUS: {status}",
        f"SPEED: {speed:.1f}x",
        f"CAMERA: {math.degrees(camera_angle) % 360:.0f} degrees",
        "SPACE: Pause / Resume",
        "UP/DOWN: Animation Speed",
        "LEFT/RIGHT: Camera Rotation",
        "R: Reset | ESC: Exit",
    ]

    for i, line in enumerate(lines):
        text_surface = font.render(line, True, (175, 195, 220))
        screen.blit(text_surface, (24, HEIGHT - 145 + i * 19))


# -------------------- Main Animation Loop --------------------

def main():
    running = True
    paused = False
    speed = 1.0
    camera_angle = 0.0
    elapsed = 0.0
    planet_angles = [random.random() * math.tau for _ in PLANETS]

    while running:
        dt = min(clock.tick(FPS) / 1000.0, 0.05)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                elif event.key == pygame.K_SPACE:
                    paused = not paused

                elif event.key == pygame.K_UP:
                    speed = min(5.0, speed + 0.2)

                elif event.key == pygame.K_DOWN:
                    speed = max(0.1, speed - 0.2)

                elif event.key == pygame.K_LEFT:
                    camera_angle -= 0.12

                elif event.key == pygame.K_RIGHT:
                    camera_angle += 0.12

                elif event.key == pygame.K_r:
                    elapsed = 0.0
                    speed = 1.0
                    camera_angle = 0.0
                    planet_angles = [
                        random.random() * math.tau
                        for _ in PLANETS
                    ]

        if not paused:
            elapsed += dt * speed

            for i, planet in enumerate(PLANETS):
                planet_angles[i] += planet[4] * dt * speed

            # Slowly rotate the camera automatically.
            camera_angle += dt * 0.08

        screen.fill(BACKGROUND)
        draw_stars()
        draw_orbits(camera_angle)

        # Draw planets in depth order.
        objects = []

        for i, planet in enumerate(PLANETS):
            name, orbit, radius, color, orbital_speed, tilt = planet

            x = orbit * math.cos(planet_angles[i])
            z = orbit * math.sin(planet_angles[i])
            y = z * math.sin(tilt)

            _, _, _, depth = project(x, y, z, camera_angle)
            objects.append((depth, i))

        # Farther objects are drawn first.
        for _, i in sorted(objects, reverse=True):
            draw_planet(*PLANETS[i][:4],
                        planet_angles[i],
                        PLANETS[i][5],
                        camera_angle)

        draw_sun(camera_angle, elapsed)
        draw_hud(speed, paused, camera_angle)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
