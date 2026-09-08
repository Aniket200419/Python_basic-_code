import pygame
import time

# Initialize pygame mixer
pygame.mixer.init()

# Load song
pygame.mixer.music.load("song.mp3")

# Play song
pygame.mixer.music.play()

print("🎵 Song is playing...")

# Keep program running while song plays
while pygame.mixer.music.get_busy():
    time.sleep(1)

print("🎵 Song finished.")