""" Button to select """
import pygame
import util.config as cfg
from .label_sprite import LabelSprite

class SelectButton(LabelSprite):
    """ Detects when is clicked. Contains any info in self.info """

    def __init__(self, label, info, w = 240, h = 360, color = cfg.COLORS['WHITE']):
        LabelSprite.__init__(self, label, w, h, color)
        r = pygame.Rect(cfg.SELECT_BTN_FRAME_GAP,cfg.SELECT_BTN_FRAME_GAP,w - 2*cfg.SELECT_BTN_FRAME_GAP, h- 2*cfg.SELECT_BTN_FRAME_GAP)
        pygame.draw.rect(self.image, cfg.COLORS['BLACK'], r, width = 4)
        self.info = info

    def inrect(self, x, y) -> bool:
        """ Checks if (x, y) is in button """
        return all((self.rect.topleft[0] <= x, self.rect.topleft[1] <= y, x <= self.rect.bottomright[0], y <= self.rect.bottomright[1]))

    def is_clicked(self) -> bool:
        """ Checks if button is clicked """
        return pygame.mouse.get_pressed()[0] and self.inrect(*pygame.mouse.get_pos())
