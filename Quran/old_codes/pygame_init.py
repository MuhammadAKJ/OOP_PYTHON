import pygame
import sys
import os
from chapters import chapters
import arabic_reshaper
from bidi.algorithm import get_display

pygame.init()

WIDTH, HEIGHT = 640, 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 36

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quran App")
file_path = os.path.dirname(__file__)
audio_base = file_path + '/audio/minshawi'
font = pygame.font.SysFont("Arial", FONT_SIZE)



def play(chapter: str, group_repeat=1, ayat_repeat=0, start_ayat=1, stop_ayat=0):
    '''
    chapter >> provide chapter name to be played
    group_repeat >> number of times to repeat group play
    surat_repeat >> whether to repeat surah or not.
        options:
            0 > play once
            1 > keep playing the same surah
            2 > keep once and proceed to the next surah
    aya_repeat >> specify how many times to repeat ayah before proceeding to the next (0-N)
    start_ayat >> default is 1 but can be changed (1-No. of ayat in surah)
    stop_ayat >> default is last ayat of the surah but can change (1-No. ayat in surah)
    '''
    queue = []
    chapter_no, no_of_ayat = chapters[chapter]
    assert start_ayat <= no_of_ayat, 'Out of range'
    assert stop_ayat >= start_ayat, 'Range error'
    
    # Create a queue list
    for i in range(start_ayat, stop_ayat + 1):
        queue.append(f'{chapter_no:3}{i:3}')

    
    for _ in range(group_repeat): #loop through group repeat + 1 to make it human readable
        for file in queue: #loop through file
            if ayat_repeat == 0:
                play_current(file)
            elif ayat_repeat > 0:
                for _ in range(ayat_repeat):
                    play_current(file)
            else:
                raise 'invalid range'

def display_ayat(file_name):
    try:
        with open('quran-text.txt', 'r', encoding='UTF-8') as file:
            for line in file.readlines():
                if line.startswith(file_name):
                    text = line[6:].strip()
    except:
        raise FileNotFoundError
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    text_surface = font.render(bidi_text, True, BLACK)
    #fill screen with white
    screen.fill(WHITE)

    #blit text onto the screen
    screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, HEIGHT // 2 - text_surface.get_height() // 2))

    #flip the display
    pygame.display.flip()

def play_ayat(filename):
    mp3_filename = filename + '.mp3'
    path = os.path.join(audio_base, mp3_filename)
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pass

def play_current(file_name):
    print(f'playing {file_name}...')
    display_ayat(file_name)
    play_ayat(file_name)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    play(chapter='An-Nas', group_repeat=1, ayat_repeat=0, start_ayat=1, stop_ayat=2)