""" Implementing 7th level """
from util.config import SCREEN_SIZE, DEBUG
from util.level_gen import generate_level
from util.level_config import GRD_W, GRD_H
from src.levels_list import levels


lvl = levels[6]
with open(__file__[:-2] + 'txt','r') as f:
    generate_level(f, lvl)

lvl.set_initial_pos(*((i, j) for i in (2, GRD_W - 3) for j in (2, GRD_H - 3)))

lvl.set_hole((SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2),grid=False)

if DEBUG:
    print(__name__, 'loaded')
