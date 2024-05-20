import pymunk
import numpy as np
from abc import ABC, abstractmethod
from config import COLORS, make_screen_centered, CELL_SIZE
from cell import Cell
from pygame import Vector2


class AbstractWall(Cell, ABC):

    def __init__(self, color, grid_pos):
        Cell.__init__(self, color, grid_pos)
        self.shape = pymunk.Poly.create_box(self.body, (CELL_SIZE, CELL_SIZE) )
        self.rect.center = self.body.position
        self.shape.elasticity = self.elasticity()

    def add_to_space(self, space):
        Cell.add_to_space(self, space)
        space.add(self.shape)

    @abstractmethod
    def elasticity(self) -> float:
        pass

class Wall(AbstractWall):
    
    def __init__(self, grid_pos):
        AbstractWall.__init__(self, COLORS["WALL_GREY"], grid_pos)

    def elasticity(self) -> float:
        return 0.99

class SilentWall(AbstractWall):
    
    def __init__(self, grid_pos):
        AbstractWall.__init__(self, COLORS["WALL_BLUE"], grid_pos)

    def elasticity(self) -> float:
        return 0.1
