import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Hanoi Towers')

game_run = True
while game_run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False

pygame.quit()
