""" Implementing 5th level """
from util.config import DEBUG
from util.level_config import GRD_W, GRD_H, print_quote
from src.levels_list import levels

from gui.cell.walls import Wall
from gui.cell.floors import Ice

lvl = levels[4]
lvl.set_cells_by_type(Ice, ((i,j) for i in range(1, GRD_W - 1) for j in range(1, GRD_H - 1)))

for i in range(5, GRD_H - 1):
    lvl.set_cells_by_type(Wall, ((j,i) for j in range(1, 1 + i - 5)))

for i in range(0, GRD_H - 6):
    lvl.set_cells_by_type(Wall, ((j,i) for j in range(i + 5, GRD_W if i < 12 else GRD_W - i + 12)))

for k in range(4):
    lvl.set_cells_by_type(Wall, ((35 + k, i) for i in range(14, 19 + k)))


lvl.set_cells_by_type(Wall, ((GRD_W - 2, GRD_H - 2), (GRD_W - 3, GRD_H - 2), (GRD_W - 2, GRD_H - 3), ))
lvl.set_cells_by_type(Wall, (*((1, i) for i in range(1, 4)), *((2,i) for i in range(1, 3)), (3, 1)))

print_quote('ICE', (16, 2), lvl, cell=Ice)
print_quote('ICE', (24, 10), lvl, cell=Ice)

lvl.set_initial_pos(*((4 + i, 9 - i) for i in range(1, 5) ))
lvl.set_hole((34, 24))
if DEBUG:
    print(__name__, 'loaded')
