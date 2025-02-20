import pygame
import arabic_reshaper
from bidi.algorithm import get_display

pygame.init()

# Screen and font setup
WIDTH, HEIGHT = 640, 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 36

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Text Wrapping Sample Code")
font = pygame.font.Font('/home/shadow-walker/Desktop/Codes/OOP_PYTHON/Quran/fonts/Amiri-Bold.ttf', FONT_SIZE)  # None uses the default font


def invert_list(word_list):
    new_list = []
    for i in range(len(word_list)):
        new_list.append(word_list[-i-1])
    return new_list


def wrap_text(text, font, max_width):
    """
    Splits text into lines that fit within max_width.
    """
    words = text.split(' ')
    lines = []
    current_line = ""
    words_inverted = invert_list(words)
    for word in words:
        test_line = f"{current_line} {word}".strip()
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    return lines


def render_wrapped_text(text, font, color, x, y, max_width, line_spacing=5):
    """
    Renders wrapped text onto the Pygame screen.
    """
    reshaped_text = arabic_reshaper.reshape(text)  # Reshape for Arabic
    bidi_text = get_display(reshaped_text)        # Reorder for RTL

    logfile = open('word_wrapping_log.txt', 'a', encoding='UTF-8')
    lines = wrap_text(bidi_text, font, max_width)
    y_offset = 0

    for line in lines:
        logfile.write(f'\nfor loop -> line: {line}\n')
        text_surface = font.render(line, True, color)
        screen.blit(text_surface, (x, y + y_offset))
        y_offset += text_surface.get_height() + line_spacing
    logfile.close()

# Example text
example_text = "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ. قُلْ هُوَ اللَّهُ أَحَدٌ. اللَّهُ الصَّمَدُ."

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Render wrapped text
    render_wrapped_text(
        text=example_text,
        font=font,
        color=BLACK,
        x=20,
        y=20,
        max_width=600  # Maximum width for wrapping
    )

    pygame.display.flip()

pygame.quit()
