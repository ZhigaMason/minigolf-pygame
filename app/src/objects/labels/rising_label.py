""" Rising Label is used for displaying temporary information """
import util.config as cfg
from .label_sprite import LabelSprite

class RisingLabel(LabelSprite):
    """ Rising Label is used for displaying temporary information """

    def __init__(self, label, w = 100, h = 50, bg_color = cfg.COLORS['NULL'], alt = 100, acc = 2):
        LabelSprite.__init__(self, label, w, h, bg_color)
        self.alt = alt
        self.vel = 0
        self.acc = acc

    def update(self, dt, *args, **kwargs):
        """ Rises and kills an object after alt * vel / dt seconds"""
        self.vel += dt * self.acc
        s = dt * self.vel
        self.alt -= s
        self.rect.center = self.rect.center[0], self.rect.center[1] - s
        if self.alt <= 0:
            self.image.fill(cfg.COLORS['NULL'])
        if self.alt <= -10:
            self.kill()

    def get_altitude(self):
        """ Return altitude """
        return self.alt
