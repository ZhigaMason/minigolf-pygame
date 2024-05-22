import util.config as cfg
import pygame
from pymunk.vec2d import Vec2d as v2

class Arrow(pygame.sprite.Sprite):

    def __init__(self, pos, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(cfg.ARROW_BOX_SIZE, pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.force = v2(0,0)
        self.clr = color

    def update(self, *args, **kwargs):
        self.image.fill((0,0,0,0))
        cent = v2(*self.rect.center)
        mpos = v2(*pygame.mouse.get_pos())
        s = v2(*cfg.ARROW_BOX_SIZE)/2
        dir = cent - mpos
        if dir.length >= cfg.ARROW_MAX_LENGTH:
            dir = dir.scale_to_length(cfg.ARROW_MAX_LENGTH)
        if dir == v2(0,0):
            return
        self.force = dir
        tail = cfg.ARROW_BALL_GAP*(dir.scale_to_length(1)) + s
        head = dir + tail
        self.draw_arrow(tail, head, dir)

    def draw_arrow(self, tail, head, dir):
        h = 0.1*dir.perpendicular()
        p0 = head + h
        p1 = head - h
        pygame.draw.polygon(self.image, self.clr, (tail, p0, p1))
        pygame.draw.circle(self.image, self.clr, head, h.length)
