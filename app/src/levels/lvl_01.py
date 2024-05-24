""" Implementing 2nd level """
from util.config import DEBUG, SCREEN_SIZE
from util.level_config import print_quote, GRD_W, GRD_H
from src.levels_list import levels

from gui.cell.walls import Wall, SilentWall
from gui.cell.floors import Sand

lvl = levels[1]

lvl.set_cells_by_type(Wall, ((i, GRD_H - 9) for i in range(GRD_W)))
lvl.set_cells_by_type(Wall, ((i, j) for i in (5, 15, 24, 34) for j in range(1, 15)))
lvl.set_cells_by_type(Wall, ((i, j) for i in ( 10, 29 ) for j in range(5, GRD_H - 9)))
lvl.set_cells_by_type(Sand, ((i, j) for i in range(1, GRD_W - 1) for j in range(GRD_H - 8, GRD_H - 1)))
print_quote('BOUNCING', (1, GRD_H - 8), lvl, cell=SilentWall)

lvl.set_initial_pos((2,5),(37, 5),(3, 5), (36, 5))
lvl.set_hole(( SCREEN_SIZE[0] // 2, 200), grid=False)
if DEBUG:
    print(__name__, 'loaded')
