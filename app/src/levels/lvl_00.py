""" Implementing 1st level """
from util.config import GRID_SIZE, SCREEN_SIZE, DEBUG
from src.levels_list import levels
from util.level_config import print_quote

from gui.cell.walls import Wall, SilentWall
from gui.cell.floors import Sand

lvl = levels[0]
GRD_W, GRD_H = GRID_SIZE

lvl.set_cells_by_type(Wall, ( (i, j) for i in range(10) for j in range(9, GRD_H - 8) ))
lvl.set_cells_by_type(Wall, ( (i, j) for i in range(GRD_W - 10, GRD_W) for j in range(9, GRD_H - 8) ))
lvl.set_cells_by_type(Wall, ( (i, j) for i in range(GRD_W) for j in (8, GRD_H - 9)))

lvl.set_cells_by_type(Sand, ( (i, j) for i in range(GRD_W) for j in range(1, 8)))
lvl.set_cells_by_type(Sand, ( (i, j) for i in range(GRD_W) for j in range(GRD_H - 8, GRD_H - 1)))


print_quote('PUSH BALL', (0, 1), lvl, cell=SilentWall)
print_quote('INTO HOLE', (0, GRD_H - 8), lvl, cell=SilentWall)

lvl.set_initial_pos(*( (i, j) for i in (11, GRD_W - 12) for j in (10, GRD_H - 11 )))
lvl.set_hole((SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 2), grid=False)
if DEBUG:
    print(__name__, 'loaded')
