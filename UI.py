

class Palette():
    def __init__(self, palette_code):
        match palette_code:
            case 1:
                self.background_color = (245, 245, 220)
                self.title_1 = (139, 69, 19)
                self.title_2 = (139, 69, 25)
                self.text_black = (54, 69, 79)
                self.text_1 = (255, 69, 0)

                self.color_1 = (101, 67, 33)
                self.color_2 = (210, 180, 140)
