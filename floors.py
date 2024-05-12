from abc import ABC, abstractmethod
from config import COLORS
from cell import Cell

class Floor(Cell, ABC):

    def __init__(self, color):
        Cell.__init__(self, color)

    @property
    @abstractmethod
    def friction(self) -> float:
        """Returns friction coeficient for this type of floor"""
        pass

class Grass(Floor):
    def __init__(self):
        Floor.__init__(self, COLORS["GREEN"])

    @property
    def friction(self):
        return 0.96

class Ice(Floor):
    def __init__(self):
        Floor.__init__(self, COLORS["BLUE"])

    @property
    def friction(self):
        return 1.0

class Sand(Floor):
    def __init__(self):
        Floor.__init__(self, COLORS["WARM_YELLOW"])

    @property
    def friction(self):
        return 0.7
