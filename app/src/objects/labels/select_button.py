import pygame
import util.config as cfg
from .label_sprite import LabelSprite

class SelectButton(LabelSprite):

    def __init__(self, label, info, w = 240, h = 360, color = cfg.COLORS['WHITE']):
        LabelSprite.__init__(self, label, w, h, color)
        self.info = info

    def inrect(self, x, y) -> bool:
        return self.rect.topleft[0] <= x and self.rect.topleft[1] <= y and x <= self.rect.bottomright[0] and y <= self.rect.bottomright[1]

    def is_clicked(self) -> bool:
        return pygame.mouse.get_pressed()[0] and self.inrect(*pygame.mouse.get_pos())

