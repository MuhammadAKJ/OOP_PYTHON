import pygame
import os
import sys
import arabic_reshaper
from bidi.algorithm import get_display
from utils.chapters import chapters

pygame.init()

WIDTH, HEIGHT = 640, 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 36

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quran App")
file_path = os.path.dirname(__file__)
audio_base = os.path.join(file_path, 'audios/minshawi')
font_path = os.path.join(file_path, 'fonts/Amiri-Regular.ttf')
font = pygame.font.Font(font_path, FONT_SIZE)
# font = pygame.font.SysFont("Arial", FONT_SIZE)

pygame.mixer.init()

def play(chapter, group_repeat=1, ayat_repeat=0, start_ayat=1, stop_ayat=0):
    queue = []
    chapter_no, no_of_ayat = chapters[chapter]
    assert start_ayat <= no_of_ayat, 'Out of range'
    assert stop_ayat >= start_ayat, 'Range error'
    
    for i in range(start_ayat, stop_ayat + 1):
        queue.append(f"{chapter_no:03}{i:03}")

    for _ in range(group_repeat):
        for file in queue:
            for _ in range(ayat_repeat or 1):
                play_current(file)

def display_ayat(file_name):
    try:
        with open('texts/quran-text.txt', 'r', encoding='UTF-8') as file:
            for line in file:
                if line.startswith(file_name):
                    text = line[6:].strip()
                    break
                # else:
                    # raise ValueError("Ayah not found.")
    except FileNotFoundError:
        print("Error: Quran text file not found.")
        return

    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    text_surface = font.render(bidi_text, True, BLACK)

    screen.fill(WHITE)
    screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, HEIGHT // 2 - text_surface.get_height() // 2))
    pygame.display.flip()

def play_ayat(file_name):
    mp3_filename = f"{file_name}.mp3"
    path = os.path.join(audio_base, mp3_filename)

    try:
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    pygame.quit()
                    sys.exit()
    except pygame.error as e:
        print(f"Audio error: {e}")

def play_current(file_name):
    print(f'Playing {file_name}...')
    display_ayat(file_name)
    play_ayat(file_name)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    play(chapter='At-Takathur', group_repeat=1, ayat_repeat=3, start_ayat=1, stop_ayat=8)
    running = False

pygame.quit()
sys.exit()
