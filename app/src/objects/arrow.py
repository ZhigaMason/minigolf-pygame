""" Arrow showing direction and force with which the ball will be hit """
import pygame
from pymunk.vec2d import Vec2d as v2
import util.config as cfg

class Arrow(pygame.sprite.Sprite):
    """ Arrow showing direction and force with which the ball will be hit """

    def __init__(self, pos, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(cfg.ARROW_BOX_SIZE, pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.force = v2(0,0)
        self.clr = color

    def update(self, *args, **kwargs):
        """ Updating redraws arrow according to mouse position """
        self.image.fill((0,0,0,0))
        cent = v2(*self.rect.center)
        mpos = v2(*pygame.mouse.get_pos())
        s = v2(*cfg.ARROW_BOX_SIZE)/2
        farrow = cent - mpos
        if farrow.length >= cfg.ARROW_MAX_LENGTH:
            farrow = farrow.scale_to_length(cfg.ARROW_MAX_LENGTH)
        if farrow.length <= cfg.ARROW_MIN_LENGTH:
            self.force = v2(0, 0)
            return
        self.force = farrow
        tail = cfg.ARROW_BALL_GAP*(farrow.scale_to_length(1)) + s
        head = 1.1*farrow + tail
        self.draw_arrow(tail, head, farrow)

    def draw_arrow(self, tail, head, farrow):
        """ Redraws self, used in update method """
        h = 0.1*farrow.perpendicular()
        p0 = head + h
        p1 = head - h
        pygame.draw.polygon(self.image, self.clr, (tail, p0, p1))
        pygame.draw.circle(self.image, self.clr, head, h.length)
