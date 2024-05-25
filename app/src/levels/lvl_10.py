""" Implementing 9th level """
from util.config import DEBUG
from util.level_gen import generate_level
from src.levels_list import levels


lvl = levels[10]
with open(__file__[:-2] + 'txt','r', encoding='utf-8') as f:
    generate_level(f, lvl)

lvl.set_initial_pos((25, 4), (32, 5), (37, 9), (22, 2))

lvl.set_hole((5, 24))

if DEBUG:
    print(__name__, 'loaded')
