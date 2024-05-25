""" This module has the list of all levels """
from util.config import MAX_LEVELS
from gui.level.level import Level

levels = [Level() for _ in range(MAX_LEVELS)]

from .levels import *
