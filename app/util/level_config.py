""" Config file for level creating """
from gui.level.level import Level
import util.config as cfg

LETTERS = {
    'D' : (5, (*((0, j) for j in range (0, 7)), (1, 0), (2, 0), (1, 6), (2, 6), *((3, j) for j in range(1, 6)))),
    'R' : (5, (*((0, j) for j in range (0, 7)), (1, 0), (2, 0), (1, 3), (2, 3), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6))),
    'A' : (5, (*((0, j) for j in range (1, 7)), (1, 0), (2, 0), (1, 3), (2, 3), *((3, j) for j in range (1, 7)))),
    'G' : (5, (*((0, j) for j in range (1, 6)), (1, 0), (2, 0), (1, 6), (2, 6), *((3, j) for j in (1, 4, 5)), (2, 4))),
    ' ' : (1, ()),
    'B' : (5, (*((0, j) for j in range (0, 7)), *( (i, j) for i in (1,2) for j in (0, 3, 6)), *((3, j) for j in (1,2,4,5)))),
    'L' : (5, (*((0, j) for j in range (0, 7)), *((i, 6) for i in range(4)))),
    'H' : (5, (*((0, j) for j in range (0, 7)), (1, 3), (2, 3), *((3, j) for j in range (0, 7)),)),
    'E' : (5, (*((0, j) for j in range (0, 7)), *((i, j) for i in (1, 2, 3) for j in (0,3,6)))),
    'T' : (6, (*((2, j) for j in range (1, 7)), *((i, 0) for i in range(5)))),
    'I' : (4, (*((1, j) for j in range(1, 6)),*((i,j) for i in range(3) for j in (0, 6)))),
    'O' : (5, (*((i, j) for i in (0, 3) for j in range(1, 6)), *((i,j) for i in (1, 2) for j in (0, 6)))),
    'N' : (5, (*((i, j) for i in (0, 3) for j in range(0, 7)), (1,1), (1,2), (2,3), (2, 4))),
    'P' : (5, (*((0, j) for j in range(7)), *( (i,j) for i in (1,2) for j in (0, 3)), (3,1), (3,2))),
    'U' : (5, (*((i, j) for i in (0, 3) for j in range(6)), (1, 6), (2,6))),
    'S' : (5, (*((0, j) for j in (1, 2, 5)), *((i,j) for i in (1,2) for j in (0, 3, 6)),*((3, j) for j in (1, 4, 5)))),
    'C' : (5, (*((0, j) for j in range(1, 6)), *( (i,j) for i in (1,2) for j in (0, 6)), (3,1), (3,5))),
}
def print_quote(quote : str, ofs : tuple[int, int], level : Level, *, cell):
    """ Prints quote onto level """
    stack_ofs = 0
    for char in quote:
        add_ofs = LETTERS[char][0]
        level.set_cells_by_type(cell, ( (ofs[0] + stack_ofs + x, ofs[1] + y) for x, y in LETTERS[char][1]))
        stack_ofs += add_ofs

GRD_W, GRD_H = cfg.GRID_SIZE
