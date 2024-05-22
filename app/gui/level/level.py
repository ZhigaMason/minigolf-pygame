import pygame
import pymunk
import util.config as cfg
from enum import Enum

from util.config import GRID_SIZE, NUM_LEVELS, COLORS, make_grid_pos

from gui.cell.walls import Wall, SilentWall
from gui.cell.floors import AbstractFloor, Grass, Ice, Sand
from gui.level.hole import Hole

class Level:

    def __init__(self, init_pos = [(0, 0) for _ in range(4)]):
        self.sprites = pygame.sprite.Group()
        self.space = pymunk.Space(threaded=True)
        self.grid = [[0 for _ in range(GRID_SIZE[1])] for _ in range(GRID_SIZE[0])]
        self.space.threads = 2
        self.space.iterations = cfg.FPS * cfg.DIV
        self.initial_pos = init_pos
        self.hole = Hole((0,0))
        self.balls = []
        self.add_borders()
        self.add_default_floor()
        self.set_hole((10, 16))
        self.set_initial_pos(*((20, i) for i in range(15, 19)))

    def add_borders(self):
        self.set_cells_by_type(Wall, ((0, i) for i in range(cfg.GRID_SIZE[1])))
        self.set_cells_by_type(Wall, ((cfg.GRID_SIZE[0] - 1, i) for i in range(cfg.GRID_SIZE[1])))
        self.set_cells_by_type(Wall, ((i, 0) for i in range(cfg.GRID_SIZE[0])))
        self.set_cells_by_type(Wall, ((i, cfg.GRID_SIZE[1] - 1) for i in range(cfg.GRID_SIZE[0])))

    def add_default_floor(self):
        self.set_cells_by_type(Grass, ((i, j) for i in range(1, cfg.GRID_SIZE[0] - 1) for j in range(1, cfg.GRID_SIZE[1] - 1)))
    
    def set_hole(self, grid_pos):
        self.hole.remove(self.sprites)
        self.hole = Hole(grid_pos)
        self.hole.add(self.sprites)
        #could be needed to add hole to pymunk space as static body

    def set_cells_by_coord(self, coords):
        for gpos, cell_type in coords.items():
            self.add_cell(cell_type, *gpos)

    def set_cells_by_type(self, cell_type, pos_list):
        for pos in pos_list:
            self.add_cell(cell_type, *pos)

    def add_cell(self, cell_type, x, y):
        cell = cell_type((x, y))
        cell.add(self.sprites)
        cell.add_to_space(self.space)
        if isinstance(cell, AbstractFloor):
            self.grid[x][y] = cell.opp_force

    def set_initial_pos(self, pos1, pos2, pos3, pos4):
        self.initial_pos = [cfg.make_screen_pos(p) for p in (pos1, pos2, pos3, pos4)]
#

levels = [Level() for _ in range(NUM_LEVELS)]
levels[0].set_initial_pos((10,10), (6,10), (7,10), (8,10))
levels[0].set_cells_by_type(SilentWall, [ (i, 3) for i in range(1, GRID_SIZE[0] - 1)])
levels[0].set_cells_by_type(Ice, [ (i, j) for i in range(4, 8) for j in range(10, 25)])
levels[0].set_cells_by_type(Sand, [ (i, j) for i in range(10, 15) for j in range(18, 23)])
levels[0].set_hole((15, 15))
#print(levels[0].grid)
