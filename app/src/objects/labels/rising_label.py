import pygame
import util.config as cfg
from .label_sprite import LabelSprite

class RisingLabel(LabelSprite):

    def __init__(self, label, w = 100, h = 50, bg_color = cfg.COLORS['NULL'], alt = 100, acc = 2):
        LabelSprite.__init__(self, label, w, h, bg_color)
        self.alt = alt
        self.vel = 0
        self.acc = acc

    def update(self, dt, *args, **kwargs):
        self.vel += dt * self.acc
        s = dt * self.vel
        self.alt -= s
        self.rect.center = self.rect.center[0], self.rect.center[1] - s
        if self.alt <= 0:
            self.kill()
