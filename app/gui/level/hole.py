""" Golfhole is a essential part of a game """
from math import dist
import pygame
import util.config as cfg

class Hole(pygame.sprite.Sprite):
    """ Class representing golfhole """

    def __init__(self, grid_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([cfg.HOLE_SIZE, cfg.HOLE_SIZE], pygame.SRCALPHA)
        self.rect = pygame.draw.circle(self.image, cfg.COLORS["BLACK"], (cfg.HOLE_SIZE // 2, cfg.HOLE_SIZE // 2), cfg.HOLE_RAD)

        pos = cfg.make_screen_pos(grid_pos)
        self.rect.center = (pos[0] + cfg.CELL_SIZE // 2, pos[1] + cfg.CELL_SIZE // 2)

    def is_inside(self, ball):
        """ Checks if ball is inside the whole (meaning fully)"""
        return dist(ball.rect.center, self.rect.center) <= cfg.BALL_RAD

    def pos(self):
        """Fancy getter for position"""
        return self.rect.center
