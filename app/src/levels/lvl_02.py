""" Implementing 3rd level """
from util.config import DEBUG
from util.level_config import GRD_W, GRD_H
from src.levels_list import levels

from gui.cell.walls import Wall, SilentWall
from gui.cell.floors import Grass, Ice, Sand

lvl = levels[2]

lvl.set_cells_by_type(SilentWall, ((i,j) for i in range(1, GRD_W - 1) for j in (7, 24)))
lvl.set_cells_by_type(SilentWall, ((i,j) for i in range(1, GRD_W - 1) for j in range(24, GRD_H - 1)))
lvl.set_cells_by_type(SilentWall, ((i,j) for i in range(1, GRD_W - 1) for j in range(1,7)))
lvl.set_cells_by_type(SilentWall, ((i,j) for i in (1, GRD_W - 2) for j in range(7, 24)))
lvl.set_cells_by_type(SilentWall, ((i,j) for i in (7, 33) for j in range(9, 23)))
lvl.set_cells_by_type(SilentWall, ((i,j) for i in range(14, 27) for j in range(7, 24)))
lvl.set_cells_by_type(Grass, ((i, 15) for i in range(14, 27)))

lvl.set_initial_pos(*((4, i) for i in (13, 14, 16, 17)))
lvl.set_hole((GRD_W - 4, 15))
if DEBUG:
    print(__name__, 'loaded')
