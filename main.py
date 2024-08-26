import pygame
import sys
import time
import copy
from UI import Palette, blit_text, draw_menu, draw_towers, draw_disks, draw_ptr, draw_game_over
from solver import *

pygame.init()
pygame.display.set_caption("Towers of Hanoi")
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

game_done = False
framerate = 60

# game vars:
steps = 0
n_disks = 3
disks = []
towers_midx = [120, 320, 520]
pointing_at = 0
floating = False
floater = 0
previous_movements = []
first_move = False

# button vars:
button_color = (200, 200, 200)
button_hover_color = (170, 170, 170)
button_rect = pygame.Rect(270, 410, 100, 40)
button_text = "Autosolve"

click_tower_1 = pygame.Rect(40, 200, 160, 220)
click_tower_2 = pygame.Rect(240, 200, 160, 220)
click_tower_3 = pygame.Rect(440, 200, 160, 220)

# colors:
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
gold = (239, 229, 51)
blue = (78, 162, 196)
grey = (170, 170, 170)
green = (77, 206, 145)

current_theme = 1
max_themes = 2
colors = Palette(current_theme)


def draw_button():
    pygame.draw.rect(screen, button_color, button_rect)
    blit_text(screen, button_text, button_rect.center, font_name='sans serif', size=30, color=black)


def menu_screen():  # to be called before starting actual game loop
    global screen, n_disks, game_done, colors, current_theme
    menu_done = False
    while not menu_done:  # every screen/scene/level has its own loop
        draw_menu(screen, n_disks, colors)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    menu_done = True
                    game_done = True
                elif event.key == pygame.K_RETURN:
                    menu_done = True
                elif event.key == pygame.K_UP:
                    n_disks += 1
                    if n_disks > 6:
                        n_disks = 6
                elif event.key == pygame.K_DOWN:
                    n_disks -= 1
                    if n_disks < 1:
                        n_disks = 1
                elif event.key == pygame.K_LEFT:
                    current_theme -= 1
                    if current_theme < 1:
                        current_theme = max_themes
                    colors = Palette(current_theme)
                    draw_menu(screen, n_disks, colors)
                elif event.key == pygame.K_RIGHT:
                    current_theme += 1
                    if current_theme > max_themes:
                        current_theme = 1
                    colors = Palette(current_theme)
                    draw_menu(screen, n_disks, colors)

            elif event.type == pygame.QUIT:
                menu_done = True
                game_done = True
        pygame.display.flip()
        clock.tick(60)


def game_over():  # game over screen
    global screen, steps
    screen.fill(white)
    min_steps = 2**n_disks-1
    blit_text(screen, 'You Won!', (320, 200), font_name='sans serif', size=72, color=gold)
    blit_text(screen, 'You Won!', (322, 202), font_name='sans serif', size=72, color=gold)
    blit_text(screen, 'Your Steps: '+str(steps), (320, 360), font_name='mono', size=30, color=black)
    blit_text(screen, 'Minimum Steps: '+str(min_steps), (320, 390), font_name='mono', size=30, color=red)
    if min_steps == steps:
        blit_text(screen, 'You finished in minumum steps!', (320, 300), font_name='mono', size=26, color=green)
    pygame.display.flip()
    time.sleep(2)   # wait for 2 secs
    pygame.quit()  # pygame exit
    sys.exit()  # console exit


def make_disks():
    global n_disks, disks
    disks = []
    height = 20
    ypos = 397 - height
    width = n_disks * 23
    for i in range(n_disks):
        disk = {}
        disk['rect'] = pygame.Rect(0, 0, width, height)
        disk['rect'].midtop = (120, ypos)
        disk['val'] = n_disks-i
        disk['tower'] = 0
        disks.append(disk)
        ypos -= height+3
        width -= 23


def check_won():
    global disks
    over = True
    for disk in disks:
        if disk['tower'] != 2:
            over = False
    if over:
        time.sleep(0.2)
        game_over()


def reset():
    global steps, pointing_at, floating, floater, first_move
    steps = 0
    pointing_at = 0
    floating = False
    floater = 0
    first_move = False
    menu_screen()
    make_disks()


menu_screen()
make_disks()
# main game loop:
while not game_done:
    mouse_pos = pygame.mouse.get_pos()
    blit_text(screen, button_text, button_rect.center, font_name='sans serif', size=30, color=black)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if (floating):
                if (click_tower_1.collidepoint(mouse_pos)):
                    for disk in disks[::-1]:
                        if disk['tower'] == 0 and disks.index(disk) != floater:
                            if disk['val'] > disks[floater]['val']:
                                floating = False
                                disks[floater]['rect'].midtop = (towers_midx[0], disk['rect'].top-23)
                                disks[floater]['tower'] = 0
                                print("origin", disks)
                                steps += 1
                            break
                    else:
                        floating = False
                        disks[floater]['rect'].midtop = (towers_midx[0], 400-23)
                        disks[floater]['tower'] = 0
                        steps += 1
                if (click_tower_2.collidepoint(mouse_pos)):
                    for disk in disks[::-1]:
                        if disk['tower'] == 1 and disks.index(disk) != floater:
                            if disk['val'] > disks[floater]['val']:
                                floating = False
                                disks[floater]['rect'].midtop = (towers_midx[1], disk['rect'].top-23)
                                disks[floater]['tower'] = 1
                                print("origin", disks)
                                steps += 1
                            break
                    else:
                        floating = False
                        disks[floater]['rect'].midtop = (towers_midx[1], 400-23)
                        disks[floater]['tower'] = 1
                        steps += 1
                if (click_tower_3.collidepoint(mouse_pos)):
                    for disk in disks[::-1]:
                        if disk['tower'] == 2 and disks.index(disk) != floater:
                            if disk['val'] > disks[floater]['val']:
                                floating = False
                                disks[floater]['rect'].midtop = (towers_midx[2], disk['rect'].top-23)
                                disks[floater]['tower'] = 2
                                steps += 1
                            break
                    else:
                        floating = False
                        disks[floater]['rect'].midtop = (towers_midx[2], 400-23)
                        disks[floater]['tower'] = 2
                        print("entro3", disks)
                        steps += 1

            elif (not floating):
                if (click_tower_1.collidepoint(mouse_pos)):
                    for disk in disks[::-1]:
                        if disk['tower'] == 0:
                            previos_disks = copy.deepcopy(disks)
                            previous_movements.append(previos_disks)
                            floating = True
                            floater = disks.index(disk)
                            disk['rect'].midtop = (towers_midx[0], 100)
                            break
                if (click_tower_2.collidepoint(mouse_pos)):
                    for disk in disks[::-1]:
                        if disk['tower'] == 1:
                            previos_disks = copy.deepcopy(disks)
                            previous_movements.append(previos_disks)
                            floating = True
                            floater = disks.index(disk)
                            disk['rect'].midtop = (towers_midx[1], 100)
                            break
                if (click_tower_3.collidepoint(mouse_pos)):
                    for disk in disks[::-1]:
                        if disk['tower'] == 2:
                            previos_disks = copy.deepcopy(disks)
                            previous_movements.append(previos_disks)
                            floating = True
                            floater = disks.index(disk)
                            disk['rect'].midtop = (towers_midx[2], 100)
                            break
        if event.type == pygame.QUIT:
            game_done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_u:
                if len(previous_movements) > 0:
                    latest_disk = previous_movements[-1]
                    previous_movements.pop()
                    disks = latest_disk
                    steps -= 1
            if event.key == pygame.K_s:
                print(previous_movements)
            if event.key == pygame.K_ESCAPE:
                reset()
            if event.key == pygame.K_q:
                game_done = True
            if event.key == pygame.K_RIGHT:
                pointing_at = (pointing_at+1) % 3
                if floating:
                    disks[floater]['rect'].midtop = (towers_midx[pointing_at], 100)
                    disks[floater]['tower'] = pointing_at
            if event.key == pygame.K_LEFT:
                pointing_at = (pointing_at-1) % 3
                if floating:
                    disks[floater]['rect'].midtop = (towers_midx[pointing_at], 100)
                    disks[floater]['tower'] = pointing_at
            if event.key == pygame.K_UP and not floating:
                previos_disks = copy.deepcopy(disks)
                previous_movements.append(previos_disks)
                for disk in disks[::-1]:
                    if disk['tower'] == pointing_at:
                        floating = True
                        floater = disks.index(disk)
                        disk['rect'].midtop = (towers_midx[pointing_at], 100)
                        break

            if event.key == pygame.K_DOWN and floating:
                for disk in disks[::-1]:
                    if disk['tower'] == pointing_at and disks.index(disk) != floater:
                        if disk['val'] > disks[floater]['val']:
                            floating = False
                            disks[floater]['rect'].midtop = (towers_midx[pointing_at], disk['rect'].top-23)
                            first_move = True
                            steps += 1
                        break
                else:
                    floating = False
                    disks[floater]['rect'].midtop = (towers_midx[pointing_at], 400-23)
                    steps += 1

        # Solver
        if event.type == pygame.MOUSEBUTTONDOWN and not first_move:
            if button_rect.collidepoint(mouse_pos):
                move_set = []
                hanoi_solver(n_disks, 0, 2, 1, move_set)
                print("output :", move_set)
                for move in move_set:
                    print(move)
                    auto_move(move["start"], move["finish"], towers_midx, disks, steps)

                first_move = True  # Button disappears after the first click

    screen.fill(white)
    draw_towers(screen, towers_midx, colors)
    draw_disks(screen, disks, colors)
    draw_ptr(screen, towers_midx, pointing_at, colors)
    if not first_move:
        draw_button()
    blit_text(screen, 'Steps: '+str(steps), (320, 20), font_name='mono', size=30, color=black)
    pygame.display.flip()
    if not floating and first_move:
        check_won()
    clock.tick(framerate)
