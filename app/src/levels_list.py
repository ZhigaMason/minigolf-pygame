from util.config import NUM_LEVELS
from gui.level.level import Level

levels = [Level() for _ in range(NUM_LEVELS)]

from .levels import *
