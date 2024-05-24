""" Button to select """
import pygame
import util.config as cfg
from .label_sprite import LabelSprite

class SelectButton(LabelSprite):
    """ Detects when is clicked. Contains any info in self.info """

    def __init__(self, label, info, w = 240, h = 360, color = cfg.COLORS['WHITE']):
        LabelSprite.__init__(self, label, w, h, color)
        self.info = info

    def inrect(self, x, y) -> bool:
        """ Checks if (x, y) is in button """
        return all((self.rect.topleft[0] <= x, self.rect.topleft[1] <= y, x <= self.rect.bottomright[0], y <= self.rect.bottomright[1]))

    def is_clicked(self) -> bool:
        """ Checks if button is clicked """
        return pygame.mouse.get_pressed()[0] and self.inrect(*pygame.mouse.get_pos())
