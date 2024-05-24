""" Implementing 1st level """
from util.config import GRID_SIZE, DEBUG
from src.levels_list import levels

from gui.cell.walls import Wall, SilentWall
from gui.cell.floors import Grass, Ice, Sand

levels[0].set_initial_pos((10,10), (6,10), (7,10), (8,10))
levels[0].set_cells_by_type(SilentWall, [ (i, 3) for i in range(1, GRID_SIZE[0] - 1)])
levels[0].set_cells_by_type(Ice, [ (i, j) for i in range(4, 8) for j in range(10, 25)])
levels[0].set_cells_by_type(Sand, [ (i, j) for i in range(10, 15) for j in range(18, 23)])
levels[0].set_hole((15, 15))

if DEBUG:
    print(__name__, 'loaded')
