"""
    Module containg base Cell class.
    All static objects, that will be interacting with ball physics
    should inherit Cell
"""
import pymunk
import pygame
from util.config import CELL_SIZE, make_screen_centered

class Cell(pygame.sprite.Sprite):
    """
        Class representing abstract cell in the level
    """

    def __init__(self, color, grid_pos):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([CELL_SIZE, CELL_SIZE])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.body = pymunk.Body(1,1, body_type=pymunk.Body.STATIC)
        self.body.position = make_screen_centered(grid_pos)
        self.rect.center = self.body.position.x, self.body.position.y

    def add_to_space(self, space : pymunk.Space):
        """
            Methods adds cell to pymunk space
        """
        space.add(self.body)

    def remove_from_space(self, space):
        """
            Methods removes cell from pymunk space
        """
        space.remove(self.body)

    @property
    def opp_force(self) -> int:
        """
            Returns maximal oppositional force that cell can provide
            when ball rolls on it.

            It set to zero for all unspecified cells.
        """
        return 0
