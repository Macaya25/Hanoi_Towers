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


def blit_text(screen, text, midtop, aa=True, font=None, font_name=None, size=None, color=(255, 0, 0)):
    if font is None:                                    # font option is provided to save memory if font is
        font = pygame.font.SysFont(font_name, size)     # already loaded and needs to be reused many times
    font_surface = font.render(text, aa, color)
    font_rect = font_surface.get_rect()
    font_rect.midtop = midtop
    screen.blit(font_surface, font_rect)


def draw_towers(screen, towers_midx, colors: Palette):
    for xpos in range(40, 460+1, 200):
        pygame.draw.rect(screen, colors.tower_1, pygame.Rect(xpos, 400, 160, 20))
        pygame.draw.rect(screen, colors.tower_2, pygame.Rect(xpos+75, 200, 10, 200))
    blit_text(screen, 'Start', (towers_midx[0], 403), font_name='mono', size=14, color=colors.background_color)
    blit_text(screen, 'Finish', (towers_midx[2], 403), font_name='mono', size=14, color=colors.background_color)


def draw_disks(screen, disks, colors: Palette):
    for disk in disks:
        pygame.draw.rect(screen, colors.disk, disk['rect'])
    return


def draw_ptr(screen, towers_midx, pointing_at, colors: Palette):
    ptr_points = [(towers_midx[pointing_at]-7, 440), (towers_midx[pointing_at]+7, 440), (towers_midx[pointing_at], 433)]
    pygame.draw.polygon(screen, colors.disk, ptr_points)
    return
