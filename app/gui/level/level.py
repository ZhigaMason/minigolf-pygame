""" Gets together all objects for level and makes wrapper around them """
import pygame
import pymunk
import util.config as cfg
from util.config import GRID_SIZE

from gui.cell.walls import Wall
from gui.cell.floors import Grass
from .hole import Hole

class Level:
    """ 
        Level class have pygame sprites and pymunk space. 
        Both should be treated as immutable objects outside of a class
    """

    def __init__(self, init_pos = [(0, 0) for _ in range(4)]):
        self.sprites = pygame.sprite.Group()
        self.space = pymunk.Space(threaded=True)
        self.grid = [[0 for _ in range(GRID_SIZE[1])] for _ in range(GRID_SIZE[0])]
        self.cell_grid = [[None for _ in range(GRID_SIZE[1])] for _ in range(GRID_SIZE[0])]
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
        """ Adds default borders on edges of level """
        self.set_cells_by_type(Wall, ((0, i) for i in range(cfg.GRID_SIZE[1])))
        self.set_cells_by_type(Wall, ((cfg.GRID_SIZE[0] - 1, i) for i in range(cfg.GRID_SIZE[1])))
        self.set_cells_by_type(Wall, ((i, 0) for i in range(cfg.GRID_SIZE[0])))
        self.set_cells_by_type(Wall, ((i, cfg.GRID_SIZE[1] - 1) for i in range(cfg.GRID_SIZE[0])))

    def add_default_floor(self):
        """ Adds default grass floor onto level """
        self.set_cells_by_type(Grass, ((i, j) for i in range(1, cfg.GRID_SIZE[0] - 1) for j in range(1, cfg.GRID_SIZE[1] - 1)))

    def set_hole(self, pos, grid : bool = True):
        """ Sets a hole in the level, and remove one if there was previously """
        self.hole.remove(self.sprites)
        self.hole = Hole(pos)
        if not grid:
            self.hole.rect.center = pos
        self.hole.add(self.sprites)

    def set_cells_by_coord(self, coords):
        """ Sets cells by a dictionary {grid_pos : type(cell)}"""
        for gpos, cell_type in coords.items():
            self.add_cell(cell_type, *gpos)

    def set_cells_by_type(self, cell_type, pos_list):
        """ Sets cells by cell_type onto positions from pos_list"""
        for pos in pos_list:
            self.add_cell(cell_type, *pos)

    def add_cell(self, cell_type, x, y):
        """ Emplaces cell to all spaces and groups"""
        if self.cell_grid[x][y] is not None:
            self.cell_grid[x][y].remove_from_space(self.space)
        cell = cell_type((x, y))
        cell.add(self.sprites)
        cell.add_to_space(self.space)
        self.grid[x][y] = cell.opp_force
        self.cell_grid[x][y] = cell


    def set_initial_pos(self, pos1, pos2, pos3, pos4):
        """ Sets initial positions for balls, they should not collide"""
        self.initial_pos = [cfg.make_screen_centered(p) for p in (pos1, pos2, pos3, pos4)]
