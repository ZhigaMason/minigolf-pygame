""" Implementing 4th level """
from util.config import DEBUG
from util.level_config import GRD_W, GRD_H
from src.levels_list import levels

from gui.cell.walls import Wall
from gui.cell.floors import Sand

lvl = levels[3]

lvl.set_cells_by_type(Wall, ((i,j) for i in range(GRD_W // 2 - 9, GRD_W // 2 + 9) for j in range(GRD_H // 2 - 4, GRD_H // 2 + 4)))
lvl.set_cells_by_type(Sand, ((i,j) for i in range(GRD_W // 2 - 7, GRD_W // 2 + 7) for j in range(GRD_H // 2 + 4, GRD_H - 1)))

lvl.set_cells_by_coord({
    (1,1) : Wall,
    (1,2) : Wall,
    (1,3) : Wall,
    (1,4) : Wall,
    (2,1) : Wall,
    (3,1) : Wall,
    (4,1) : Wall,
    (2,2) : Wall,

    (GRD_W - 2,1) : Wall,
    (GRD_W - 2,2) : Wall,
    (GRD_W - 2,3) : Wall,
    (GRD_W - 2,4) : Wall,
    (GRD_W - 3,1) : Wall,
    (GRD_W - 4,1) : Wall,
    (GRD_W - 5,1) : Wall,
    (GRD_W - 3,2) : Wall,
})

lvl.set_initial_pos(*((5, i) for i in range(22, 26)))
lvl.set_hole((34, 24))
if DEBUG:
    print(__name__, 'loaded')
