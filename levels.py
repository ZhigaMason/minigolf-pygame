import pygame
import config as cfg
from config import GRID_SIZE, NUM_LEVELS, COLORS
from enum import Enum
from cell import Cell
from walls import AbstractWall, Wall, SilentWall
from floors import AbstractFloor, Grass, Ice, Sand
from hole import Hole

class CellType(Enum):
    FLOOR = 0
    WALL = 1

class Level:

    def __init__(self, init_pos = [(0, 0) for _ in range(4)]):
        self.grid = [[Cell(COLORS["WHITE"], (j, i)) for i in range(GRID_SIZE[1])] for j in range(GRID_SIZE[0]) ]
        self.group = pygame.sprite.Group()
        self.initial_pos = init_pos
        self.add_borders()
        self.add_default_floor()
        self.hole = Hole((0,0))

    def add_borders(self):
        for i in range(GRID_SIZE[0]):
            self.grid[i][0] = Wall((i, 0))
            self.grid[i][0].add(self.group)
            self.grid[i][GRID_SIZE[1] - 1] = Wall((i, GRID_SIZE[1] - 1))
            self.grid[i][GRID_SIZE[1] - 1].add(self.group)

        for j in range(GRID_SIZE[1]):
            self.grid[0][j] = Wall((0, j))
            self.grid[0][j].add(self.group)
            self.grid[GRID_SIZE[0] - 1][j] = Wall((GRID_SIZE[0] - 1, j))
            self.grid[GRID_SIZE[0] - 1][j].add(self.group)

    def add_default_floor(self):
        for i in range(1, GRID_SIZE[0] - 1):
            for j in range(1, GRID_SIZE[1] - 1):
                self.grid[i][j] = Grass((i, j))
                self.grid[i][j].add(self.group)

    def get_cell_action(self, xgrid, ygrid):
        obj = self.grid[xgrid][ygrid]
        if issubclass(obj, AbstractWall):
            return CellType.WALL
        return obj.friction()
    
    def set_hole(self, grid_pos):
        self.hole = Hole(grid_pos)
        self.hole.add(self.group)

    def set_cells_by_coord(self, coords):
        for gpos, cell in coords.items():
            x, y = gpos[0], gpos[1]
            self.grid[x][y] = cell((x, y))
            self.grid[x][y].add(self.group)

    def set_cells_by_type(self, cell_type, pos_list : list = []):
        for pos in pos_list:
            x, y = pos[0], pos[1]
            self.grid[x][y] = cell_type(pos)
            self.grid[x][y].add(self.group)

    def set_initial_pos(self, pos1, pos2, pos3, pos4):
        self.initial_pos = [cfg.make_screen_pos(p) for p in (pos1, pos2, pos3, pos4)]
#

levels = [Level() for _ in range(NUM_LEVELS)]

levels[0].set_hole((15, 15))
levels[0].set_initial_pos((10,10), (6,10), (7,10), (8,10))
levels[0].set_cells_by_type(Wall, [ (i, 3) for i in range(1, GRID_SIZE[0] - 1)])
levels[0].set_cells_by_type(Ice, [ (i, 4) for i in range(1, GRID_SIZE[0] - 1)])
levels[0].set_cells_by_type(Sand, [ (10, i) for i in range(5, GRID_SIZE[1] - 1)])
levels[0].set_cells_by_type(Ice, [ (i, 10) for i in range(1, GRID_SIZE[0] - 1)])
levels[1].set_hole((26, 6))
levels[1].set_cells_by_coord({
    (1,1) : Wall,
    (1,2) : SilentWall,
    (1,3) : Grass,
    (1,4) : Sand,
    (1,5) : Ice,
})
levels[1].set_initial_pos(*((i, i) for i in range(4)))

levels[2].set_hole((8,10))
levels[2].set_cells_by_type(Wall, [ (i, 3) for i in range(1, GRID_SIZE[0] - 1)])
levels[2].set_cells_by_type(Ice, [ (i, 4) for i in range(1, GRID_SIZE[0] - 1)])
levels[2].set_cells_by_type(Sand, [ (10, i) for i in range(5, GRID_SIZE[1] - 1)])
levels[1].set_initial_pos(*((i, 20) for i in range(4)))
