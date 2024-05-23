from util.config import COLORS
from .base_cell import Cell

class AbstractFloor(Cell):

    def __init__(self, color, grid_pos):
        Cell.__init__(self, color, grid_pos)

    @property
    def opp_force(self) -> int:
        """Returns opp_force coeficient for this type of floor"""
        raise NotImplementedError('Calling opp_force on generic floor')

class Grass(AbstractFloor):
    def __init__(self, grid_pos):
        AbstractFloor.__init__(self, COLORS["GRASS_GREEN"], grid_pos)

    @property
    def opp_force(self):
        return 100

class Ice(AbstractFloor):
    def __init__(self, grid_pos):
        AbstractFloor.__init__(self, COLORS["ICE_BLUE"], grid_pos)

    @property
    def opp_force(self):
        return 10

class Sand(AbstractFloor):
    def __init__(self, grid_pos):
        AbstractFloor.__init__(self, COLORS["SAND_YELLOW"], grid_pos)

    @property
    def opp_force(self):
        return 500
