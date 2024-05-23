from util.config import GRID_SIZE, DEBUG
from src.levels_list import levels

from gui.cell.walls import Wall, SilentWall
from gui.cell.floors import Grass, Ice, Sand

levels[1].set_cells_by_type(Sand, ((i, j) for i in range(4, 30) for j in range(4, 7)))
levels[1].set_initial_pos(*((5,5) for _ in range(4)))

if DEBUG:
    print(__name__, 'loaded')
