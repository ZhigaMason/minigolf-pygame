""" Module with floor classes used in levels """
from util.config import COLORS
from .base_cell import Cell

class AbstractFloor(Cell):
    """ AbstractFloor class, from which all floors must inherit """

    def __init__(self, color, grid_pos):
        Cell.__init__(self, color, grid_pos)

    @property
    def opp_force(self) -> int:
        """ Returns opp_force coeficient for this type of floor """
        raise NotImplementedError('Calling opp_force on generic floor')

class Grass(AbstractFloor):
    """ Grass floor represents 'common' floor """
    def __init__(self, grid_pos):
        AbstractFloor.__init__(self, COLORS["GRASS_GREEN"], grid_pos)

    @property
    def opp_force(self):
        """ Returns maximal opposite force for grass """
        return 100

class Ice(AbstractFloor):
    """ Ice floor is more slippery than grass floor """
    def __init__(self, grid_pos):
        AbstractFloor.__init__(self, COLORS["ICE_BLUE"], grid_pos)

    @property
    def opp_force(self):
        """ Returns maximal opposite force for ice """
        return 10

class Sand(AbstractFloor):
    """ Sand floor is a floor to dig into """
    def __init__(self, grid_pos):
        AbstractFloor.__init__(self, COLORS["SAND_YELLOW"], grid_pos)

    @property
    def opp_force(self):
        """ Returns maximal opposite force for sand """
        return 500
