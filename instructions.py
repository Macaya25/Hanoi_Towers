import pygame
import sys
from UI import Palette, blit_text


def instructions_page(screen, colors: Palette):
    screen.fill(colors.background_color)

    # Title
    blit_text(screen, "Towers of Hanoi", (320, 60), font_name='sans serif', size=40, color=colors.text_black)

    # Instructions
    instructions = [
        "1. Objective: Move all disks from the left peg to the right peg.",
        "2. Only one disk can be moved at a time.",
        "3. A larger disk cannot be placed on top of a smaller disk.",
        "4. Use the arrow keys to select the disk and peg.",
        "5. Press 'Enter' to move the selected disk.",
        "6. Try to solve the puzzle in the fewest moves possible!",
    ]

    for i, line in enumerate(instructions):
        blit_text(screen, line, (320, 150 + i * 40), font_name='sans serif', size=25, color=colors.text_black)

    # Display a prompt to go back
    blit_text(screen, "Press 'ENTER' to continue", (320, 400), font_name='sans serif', size=30, color=colors.text_1)

    pygame.display.flip()

    # Wait for user input
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return  # Exit instructions page and return to previous screen
