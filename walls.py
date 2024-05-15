import numpy as np
from abc import ABC, abstractmethod
from config import COLORS
from cell import Cell
from pygame import Vector2


class AbstractWall(Cell, ABC):

    def __init__(self, color, grid_pos):
        Cell.__init__(self, color, grid_pos)

    def get_ricochet(self, vel : Vector2, pos, radius) -> Vector2:
        """returns ricocheted vector of velocity"""
        id = self.has_ball_collision(pos, radius)
        match(id):
            case 0:
                return Vector2(-self.backfire * vel[0], -self.backfire * vel[1])
            case 1:
                return Vector2(self.backfire * vel[0], -self.backfire * vel[1])
            case -1:
                return Vector2(-self.backfire * vel[0], self.backfire * vel[1])
        return vel
        

    @property
    @abstractmethod
    def backfire(self) -> float:
        pass

    def inrect(self, x, y) -> bool:
        return all((self.rect.topleft[0] <= x, self.rect.topleft[1] <= y, x <= self.rect.bottomright[0], y <= self.rect.bottomright[1]))

    def has_ball_collision(self, pos, radius):
        pos = np.asarray(pos)
        cent = np.asarray(self.rect.center)
        vect = cent - pos
        h = np.hypot(*vect)
        vect = radius * vect / h
        vect += pos
        
        if not self.inrect(*vect):
            return None
        vect = vect - pos + cent
        vect = [[1, -1], [1, 1]] @ vect
        
        return np.sign(vect[0] * vect[1])

class Wall(AbstractWall):
    
    def __init__(self, grid_pos):
        AbstractWall.__init__(self, COLORS["WALL_GREY"], grid_pos)

    @property
    def backfire(self) -> float:
        return 1.0

class SilentWall(AbstractWall):
    
    def __init__(self, grid_pos):
        AbstractWall.__init__(self, COLORS["WALL_BLUE"], grid_pos)

    @property
    def backfire(self) -> float:
        return 0.6
