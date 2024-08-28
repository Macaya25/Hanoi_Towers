import pygame


def play_music(file: str):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.play(-1)


def play_sound(sound_route: str):
    sound = pygame.mixer.Sound(sound_route)
    sound.set_volume(0.1)
    sound.play()
