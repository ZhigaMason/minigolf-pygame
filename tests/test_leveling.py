import pytest
import test_config
import app.util.config as cfg
from app.gui.level.level import Level
from app.gui.cell.base_cell import Cell
from app.gui.cell.floors import Grass, Sand, Ice
from app.gui.cell.walls import Wall, SilentWall

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
    lvl = Level()
    lvl.set_cells_by_coord({(10, 10) : cell})
    assert lvl.grid[10][10] == exp
