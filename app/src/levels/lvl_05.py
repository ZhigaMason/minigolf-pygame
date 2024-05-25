""" Implementing 6th level """
from util.config import SCREEN_SIZE, DEBUG
from util.level_gen import generate_level
from src.levels_list import levels


lvl = levels[5]
with open(__file__[:-2] + 'txt','r', encoding='utf-8') as f:
    generate_level(f, lvl)

lvl.set_initial_pos(*((i, 25) for i in range(8, 12)))

lvl.set_hole((SCREEN_SIZE[0] // 2 - 32, 80),grid=False)

if DEBUG:
    print(__name__, 'loaded')
