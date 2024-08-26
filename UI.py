import pygame


class Palette():
    def __init__(self, palette_code):
        match palette_code:
            case 1:
                self.background_color = (245, 245, 220)
                self.title_1 = (139, 69, 19)
                self.title_2 = (139, 69, 25)
                self.text_black = (54, 69, 79)
                self.text_1 = (255, 69, 0)

                self.tower_1 = (101, 67, 33)
                self.tower_2 = (210, 180, 140)

                self.disk = (78, 162, 196)

            case 2:
                self.background_color = (25, 25, 112)
                self.title_1 = (255, 165, 0)
                self.title_2 = (255, 165, 10)
                self.text_black = (255, 255, 255)
                self.text_1 = (255, 20, 147)

                self.tower_1 = (77, 77, 255)
                self.tower_2 = (77, 77, 255)

                self.disk = (57, 255, 20)


def blit_text(screen, text, midtop, aa=True, font=None, font_name=None, size=None, color=(255, 0, 0)):
    if font is None:                                    # font option is provided to save memory if font is
        font = pygame.font.SysFont(font_name, size)     # already loaded and needs to be reused many times
    font_surface = font.render(text, aa, color)
    font_rect = font_surface.get_rect()
    font_rect.midtop = midtop
    screen.blit(font_surface, font_rect)


def draw_menu(screen, n_disks, colors: Palette):
    screen.fill(colors.background_color)
    blit_text(screen, 'Towers of Hanoi', (323, 122), font_name='sans serif', size=90, color=colors.title_1)
    blit_text(screen, 'Towers of Hanoi', (320, 120), font_name='sans serif', size=90, color=colors.title_2)
    blit_text(screen, "Use up or down arrows to select difficulty:", (320, 220),
              font_name='sans serif', size=30, color=colors.text_black)
    blit_text(screen, str(n_disks), (320, 260), font_name='sans serif', size=40, color=colors.text_1)
    blit_text(screen, 'Press ENTER to continue', (320, 320), font_name='sans_serif',
              size=30, color=colors.text_black)


def draw_towers(screen, towers_midx, colors: Palette):
    for xpos in range(40, 460+1, 200):
        pygame.draw.rect(screen, colors.tower_1, pygame.Rect(xpos, 400, 160, 20))
        pygame.draw.rect(screen, colors.tower_2, pygame.Rect(xpos+75, 200, 10, 200))
    blit_text(screen, 'Start', (towers_midx[0], 403), font_name='mono', size=14, color=colors.background_color)
    blit_text(screen, 'Finish', (towers_midx[2], 403), font_name='mono', size=14, color=colors.background_color)


def draw_disks(screen, disks, colors: Palette):
    for disk in disks:
        pygame.draw.rect(screen, colors.disk, disk['rect'], border_radius=7)
        # pygame.draw.ellipse(screen, colors.disk, disk['rect'])


def draw_ptr(screen, towers_midx, pointing_at, colors: Palette):
    ptr_points = [(towers_midx[pointing_at]-7, 440), (towers_midx[pointing_at]+7, 440), (towers_midx[pointing_at], 433)]
    pygame.draw.polygon(screen, colors.disk, ptr_points)


def draw_game_over(screen, steps, n_disks, colors: Palette):
    screen.fill(colors.background_color)
    min_steps = 2**n_disks - 1
    blit_text(screen, 'You Won!', (320, 200), font_name='sans serif', size=72, color=colors.title_1)
    blit_text(screen, 'You Won!', (322, 202), font_name='sans serif', size=72, color=colors.title_2)
    blit_text(screen, 'Your Steps: '+str(steps), (320, 360), font_name='mono', size=30, color=colors.text_black)
    blit_text(screen, 'Minimum Steps: '+str(min_steps), (320, 390), font_name='mono', size=30, color=colors.disk)
    if min_steps == steps:
        blit_text(screen, 'You finished in minumum steps!', (320, 300), font_name='mono', size=26, color=colors.disk)
    pygame.display.flip()
