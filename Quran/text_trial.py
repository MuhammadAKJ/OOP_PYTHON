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
pygame.display.set_caption("Text Wrapping Example")
font = pygame.font.Font('/home/shadow-walker/Desktop/Codes/OOP_PYTHON/Quran/fonts/Amiri-Bold.ttf', FONT_SIZE)  # Default system font

def wrap_text_rtl(text, font, max_width):
    """
    Properly wraps Arabic text from right to left within max_width.
    """
    reshaped_text = arabic_reshaper.reshape(text)  # Correct Arabic shaping
    bidi_text = get_display(reshaped_text)         # Correct right-to-left order

    words = bidi_text.split(' ')  # Split words by space
    lines = []
    current_line = ""

    for word in words:
        test_line = f"{current_line} {word}".strip()
        if font.size(test_line)[0] <= max_width:  # Check width in pixels
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    return lines[::-1]  # Reverse to maintain RTL order

def render_wrapped_text_rtl(text, font, color, x, y, max_width, line_spacing=5):
    """
    Renders properly wrapped Arabic text onto the Pygame screen (Right to Left).
    """
    lines = wrap_text_rtl(text, font, max_width)
    y_offset = 0

    for line in lines:
        text_surface = font.render(line, True, color)
        text_width = text_surface.get_width()
        screen.blit(text_surface, (x + max_width - text_width, y + y_offset))  # Align Right
        y_offset += text_surface.get_height() + line_spacing

# Example Arabic text
example_text = "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ. قُلْ هُوَ اللَّهُ أَحَدٌ. اللَّهُ الصَّمَدُ."

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Render wrapped Arabic text correctly
    render_wrapped_text_rtl(
        text=example_text,
        font=font,
        color=BLACK,
        x=20,
        y=20,
        max_width=600  # Maximum width for wrapping
    )

    pygame.display.flip()

pygame.quit()
