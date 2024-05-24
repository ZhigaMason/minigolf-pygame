""" Module with walls used in levels """
from abc import ABC, abstractmethod
import pymunk
from util.config import COLORS, CELL_SIZE
from .base_cell import Cell

class AbstractWall(Cell, ABC):
    """ Abstract Wall, from which all walls must inherit """

    def __init__(self, color, grid_pos):
        Cell.__init__(self, color, grid_pos)
        self.shape = pymunk.Poly.create_box(self.body, (CELL_SIZE, CELL_SIZE) )
        self.rect.center = self.body.position
        self.shape.elasticity = self.elasticity()

    def add_to_space(self, space):
        """ Overrides base class' method, due to walls having shape """
        Cell.add_to_space(self, space)
        space.add(self.shape)

    def remove_from_space(self, space):
        """ Overrides base class' method, due to walls having shape """
        Cell.remove_from_space(self, space)
        space.remove(self.shape)

    @abstractmethod
    def elasticity(self) -> float:
        """ Method that must be implemented in non-abstract wall """

class Wall(AbstractWall):
    """ Common Wall with nearly perfect bounce """

    def __init__(self, grid_pos):
        AbstractWall.__init__(self, COLORS["WALL_GREY"], grid_pos)

    def elasticity(self) -> float:
        """ Wall method """
        return 0.99

class SilentWall(AbstractWall):
    """ Wall with much less bounce """

    def __init__(self, grid_pos):
        AbstractWall.__init__(self, COLORS["WALL_BLUE"], grid_pos)

    def elasticity(self) -> float:
        """ Wall method """
        return 0.2
