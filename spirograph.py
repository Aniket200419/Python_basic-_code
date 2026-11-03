import numpy as np
import matplotlib.pyplot as plt

# Create figure with black background
fig, ax = plt.subplots(figsize=(8, 8), facecolor='black')
ax.set_facecolor('black')

# Generate colorful spirograph pattern
for i in range(30):
    t = np.linspace(0, 20 * np.pi, 5000)

    r = 5 + np.sin(15 * t + i * 0.2)
    x = r * np.cos(t)
    y = r * np.sin(t)

    color = plt.cm.hsv(i / 30)
    ax.plot(x, y, color=color, linewidth=1)

# Remove axes
ax.axis('off')
ax.set_aspect('equal')

plt.show()