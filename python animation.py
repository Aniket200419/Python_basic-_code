
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# ---------- Settings (change as you like) ----------
BG_COLOR = "#0d1117"      # GitHub dark background
LINE_COLOR = "#58a6ff"    # wave color
DOT_COLOR = "#f78166"     # dot color
FRAMES = 120
FPS = 30
OUTPUT = "animation.gif"
# ---------------------------------------------------

fig, ax = plt.subplots(figsize=(8, 3), dpi=100)
fig.patch.set_facecolor(BG_COLOR)
ax.set_facecolor(BG_COLOR)
ax.set_xlim(0, 4 * np.pi)
ax.set_ylim(-1.6, 1.6)
ax.axis("off")

x = np.linspace(0, 4 * np.pi, 400)
(line,) = ax.plot([], [], color=LINE_COLOR, lw=3)
(dot,) = ax.plot([], [], "o", color=DOT_COLOR, markersize=12)
title = ax.text(
    2 * np.pi, 1.35, "Hello, GitHub! \U0001F44B",
    color="white", fontsize=16, ha="center", fontweight="bold",
)


def update(frame):
    phase = 2 * np.pi * frame / FRAMES
    y = np.sin(x - phase) * np.cos(0.5 * x)
    line.set_data(x, y)

    # the dot travels along the wave
    idx = int((frame / FRAMES) * (len(x) - 1))
    dot.set_data([x[idx]], [y[idx]])
    return line, dot, title


anim = FuncAnimation(fig, update, frames=FRAMES, interval=1000 / FPS, blit=True)
anim.save(OUTPUT, writer=PillowWriter(fps=FPS), savefig_kwargs={"facecolor": BG_COLOR})
print(f"Done! '{OUTPUT}' has been created.")