import pygame
import time

# Initialize pygame
pygame.init()
pygame.mixer.init()

# 🎯 IMPORTANT: Replace with YOUR exact paths
files = {
    "Neutral": "E:/2nd year/research/data/Actor_01/03-01-01-01-01-01-01.wav",
    "Calm":    "E:/2nd year/research/data/Actor_01/03-01-02-01-01-01-01.wav",
    "Happy":   "E:/2nd year/research/data/Actor_01/03-01-03-01-01-01-01.wav",
    "Angry":   "E:/2nd year/research/data/Actor_01/03-01-05-01-01-01-01.wav"
}

print("\n--- Emotion Audio Test Started ---\n")

for emotion, file in files.items():

    print(f"\nPlaying {emotion} tone...")

    try:
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()

        # Wait until audio finishes
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

    except Exception as e:
        print(f"Error playing {emotion}: {e}")

    # Pause before next audio
    time.sleep(1)

print("\n--- All emotions played ---")
