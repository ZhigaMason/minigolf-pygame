""" Implementing 9th level """
from util.config import SCREEN_SIZE, DEBUG
from util.level_gen import generate_level
from src.levels_list import levels


lvl = levels[8]
with open(__file__[:-2] + 'txt','r') as f:
    generate_level(f, lvl)

lvl.set_initial_pos((29, 4), (29, 25), (31,7), (31, 22))

lvl.set_hole((SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2),grid=False)

if DEBUG:
    print(__name__, 'loaded')
