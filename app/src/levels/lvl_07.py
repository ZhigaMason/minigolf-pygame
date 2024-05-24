""" Implementing 8th level """
from util.config import SCREEN_SIZE, CELL_SIZE, DEBUG
from util.level_gen import generate_level
from src.levels_list import levels


lvl = levels[7]
with open(__file__[:-2] + 'txt','r') as f:
    generate_level(f, lvl)

lvl.set_initial_pos((7,5), (31, 5), (7, 24), (31, 24))

lvl.set_hole((SCREEN_SIZE[0] // 2 - CELL_SIZE // 2, SCREEN_SIZE[1] // 2 + CELL_SIZE // 2),grid=False)

if DEBUG:
    print(__name__, 'loaded')
