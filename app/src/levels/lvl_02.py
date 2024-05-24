""" Implementing 3rd level """
from util.config import GRID_SIZE, DEBUG
from src.levels_list import levels

from gui.cell.walls import Wall, SilentWall
from gui.cell.floors import Grass, Ice, Sand

if DEBUG:
    print(__name__, 'loaded')
