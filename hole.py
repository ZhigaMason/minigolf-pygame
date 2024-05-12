import pygame
import config as cfg
from ball import Ball
from math import dist

class Hole(pygame.sprite.Sprite):

    def __init__(self, grid_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([cfg.HOLE_SIZE, cfg.HOLE_SIZE])
        self.rect = pygame.draw.circle(self.image, cfg.COLORS["BLACK"], (cfg.CELL_SIZE // 2, cfg.CELL_SIZE // 2), cfg.HOLE_RAD)

        pos = cfg.make_screen_pos(grid_pos)
        self.rect.center = (pos[0] + cfg.CELL_SIZE // 2, pos[1] + cfg.CELL_SIZE // 2)

    def is_inside(self, ball : Ball):
        return dist(ball.rect.center, self.rect.center) <= cfg.BALL_RAD
