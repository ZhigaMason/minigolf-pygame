import pytest
import test_config
import app.util.config as cfg
from app.gui.level.level import Level
from app.gui.cell.base_cell import Cell
from app.gui.cell.floors import Grass, Sand, Ice
from app.gui.cell.walls import Wall, SilentWall
from random import randint

def rand_pos():
    return randint(0, cfg.GRID_SIZE[0] - 1), randint(0, cfg.GRID_SIZE[1] - 1)
LVL_TEST_GRID = Level()
@pytest.mark.parametrize(
    'cell, exp',
    [
        (Wall, 0),
        (SilentWall, 0),
        (Grass, 100),
        (Sand, 500),
        (Ice, 10),
    ]
)
def test_grid(cell, exp : int):
    LVL_TEST_GRID = Level()
    LVL_TEST_GRID.set_cells_by_coord({(10, 10) : cell})
    assert LVL_TEST_GRID.grid[10][10] == exp

LVL_TEST_CELL_GRID = Level()
@pytest.mark.parametrize(
    'cell, pos',
    [
        (Wall, (10, 10)),
        (SilentWall, (0,0)),
        (Grass, (12, 1)),
        (Sand, (20, 29)),
        (Ice, (17, 16)),
        (Wall, rand_pos()),
        (SilentWall, rand_pos()),
        (Sand, rand_pos()),
        (Ice, rand_pos()),
        (Grass, rand_pos()),
    ]
)
def test_cell_grid(cell, pos):
    LVL_TEST_CELL_GRID = Level()
    LVL_TEST_CELL_GRID.set_cells_by_coord({pos : cell})
    assert type(LVL_TEST_CELL_GRID.cell_grid[pos[0]][pos[1]]) == cell

LVL_TEST_HOLE = Level()
@pytest.mark.parametrize(
    'pos',
    [
        (10,17),
        (8,29),
        (18,12),
        (10,13),
        (38,24),
        rand_pos(),
        rand_pos()
    ]
)
def test_hole_positioning(pos):
    LVL_TEST_HOLE.set_hole(pos)
    assert cfg.make_grid_pos(LVL_TEST_HOLE.hole.rect.center) == pos
