import test_config
import pytest
import app.util.config as cfg
from pymunk import Vec2d
from app.gui.level.level import Level
from app.src.objects.ball import Ball
from app.gui.cell.floors import Grass, Sand, Ice
from app.gui.cell.walls import SilentWall
from math import dist, fabs

DIST_EPS = 10
SCR_W, SCR_H = cfg.SCREEN_SIZE
GRD_W, GRD_H = cfg.GRID_SIZE

@pytest.mark.parametrize(
    'force, exp_min, exp_max',
    [
        (Vec2d(0,100), 100, 1000),
        (Vec2d(0,-100), 100, 1000),
        (Vec2d(100,0), 100, 1000),
        (Vec2d(-100,0), 100, 1000),
        (Vec2d(50, 50), 20, 300),
        (Vec2d(-50, 50), 20, 300),
        (Vec2d(50, -50), 20, 300),
        (Vec2d(-50, -50), 20, 300),
    ]
)
def test_apply_force(force : Vec2d, exp_min : float, exp_max : float):
    ball = Ball(0)
    lvl = Level()
    ball.body.position = SCR_W // 2, SCR_H // 2
    ball.add_to_level(lvl)

    ball.apply_force(force)
    for _ in range(10):
        lvl.space.step(force.length / 100)
    ball.update()
    move = (Vec2d(*ball.rect.center) - Vec2d(SCR_W // 2, SCR_H // 2))
    assert exp_min <= move.length <= exp_max, "Ball behaves too wildly"
    assert (move.projection(force) - move).length <= DIST_EPS, "Ball moves not inline with force"

@pytest.mark.parametrize(
    'ball_pos, force, exp_pos',
    [
        ((cfg.CELL_SIZE * 3, SCR_H // 2),        Vec2d(-80, 0),    ( 60, SCR_H // 2)),
        ((cfg.CELL_SIZE * 5, SCR_H // 2),        Vec2d(-100, 100), ( 80, SCR_H // 2 + 80)),
        ((cfg.CELL_SIZE * 5, SCR_H // 2),        Vec2d(-100, -100),( 80, SCR_H // 2 - 80)),
        ((SCR_W - cfg.CELL_SIZE * 3, SCR_H // 2),Vec2d(80, 0),     ( SCR_W - 60, SCR_H // 2)),
        ((SCR_W - cfg.CELL_SIZE * 5, SCR_H // 2),Vec2d(100, 100),  ( SCR_W - 80, SCR_H // 2 + 80)),
        ((SCR_W - cfg.CELL_SIZE * 5, SCR_H // 2),Vec2d(100, -100), ( SCR_W - 80, SCR_H // 2 - 80)),
        ((SCR_W // 2, cfg.CELL_SIZE * 3),        Vec2d(0, -80),    ( SCR_W // 2, 60)),
        ((SCR_W // 2, cfg.CELL_SIZE * 5),        Vec2d(100, -100), ( SCR_W // 2 + 80, 80)),
        ((SCR_W // 2, cfg.CELL_SIZE * 5),        Vec2d(-100, -100),( SCR_W // 2 - 80, 80)),
        ((SCR_W // 2, SCR_H - cfg.CELL_SIZE * 3),Vec2d(0, 80),     ( SCR_W // 2, SCR_H - 60)),
        ((SCR_W // 2, SCR_H - cfg.CELL_SIZE * 5),Vec2d(100, 100), ( SCR_W // 2 + 80, SCR_H - 80)),
        ((SCR_W // 2, SCR_H - cfg.CELL_SIZE * 5),Vec2d(-100, 100),  ( SCR_W // 2 - 80, SCR_H - 80)),
    ]
)
def test_ricochet(ball_pos : tuple[int, int], force : Vec2d, exp_pos : tuple[int, int]):
    ball = Ball(0)
    lvl = Level()
    ball.body.position = ball_pos
    ball.add_to_level(lvl)

    ball.apply_force(force)
    for _ in range(int(force.length)):
        lvl.space.step(force.length / 1000)
    ball.update()
    print(ball.rect.center)
    assert dist(ball.rect.center, exp_pos) <= DIST_EPS

@pytest.mark.parametrize(
    'ball_pos, force, exp_pos',
    [
        ((cfg.CELL_SIZE * 3, SCR_H // 2),        Vec2d(-80, 0),    ( 40, SCR_H // 2)),
        ((cfg.CELL_SIZE * 5, SCR_H // 2),        Vec2d(-100, 100), ( 40, SCR_H // 2 + 120)),
        ((cfg.CELL_SIZE * 5, SCR_H // 2),        Vec2d(-100, -100),( 40, SCR_H // 2 - 120)),
        ((SCR_W - cfg.CELL_SIZE * 3, SCR_H // 2),Vec2d(80, 0),     ( SCR_W - 40, SCR_H // 2)),
        ((SCR_W - cfg.CELL_SIZE * 5, SCR_H // 2),Vec2d(100, 100),  ( SCR_W - 40, SCR_H // 2 + 120)),
        ((SCR_W - cfg.CELL_SIZE * 5, SCR_H // 2),Vec2d(100, -100), ( SCR_W - 40, SCR_H // 2 - 120)),
        ((SCR_W // 2, cfg.CELL_SIZE * 3),        Vec2d(0, -80),    ( SCR_W // 2, 40)),
        ((SCR_W // 2, cfg.CELL_SIZE * 5),        Vec2d(100, -100), ( SCR_W // 2 + 120, 40)),
        ((SCR_W // 2, cfg.CELL_SIZE * 5),        Vec2d(-100, -100),( SCR_W // 2 - 120, 40)),
        ((SCR_W // 2, SCR_H - cfg.CELL_SIZE * 3),Vec2d(0, 80),     ( SCR_W // 2, SCR_H - 40)),
        ((SCR_W // 2, SCR_H - cfg.CELL_SIZE * 5),Vec2d(100, 100), ( SCR_W // 2 + 120, SCR_H - 40)),
        ((SCR_W // 2, SCR_H - cfg.CELL_SIZE * 5),Vec2d(-100, 100),  ( SCR_W // 2 - 120, SCR_H - 40)),
    ]
)
def test_silent_ricochet(ball_pos : tuple[int, int], force : Vec2d, exp_pos : tuple[int, int]):
    ball = Ball(0)
    lvl = Level()
    lvl.set_cells_by_type(SilentWall, ((i, 0) for i in range(GRD_W)) )
    lvl.set_cells_by_type(SilentWall, ((i, GRD_H - 1) for i in range(GRD_W)) )
    lvl.set_cells_by_type(SilentWall, ((0, i) for i in range(GRD_H)) )
    lvl.set_cells_by_type(SilentWall, ((GRD_W - 1, i) for i in range(GRD_H)) )
    ball.body.position = ball_pos
    ball.add_to_level(lvl)

    ball.apply_force(force)
    for _ in range(int(force.length)):
        lvl.space.step(force.length / 1000)
    ball.update()
    print(ball.rect.center)
    assert dist(ball.rect.center, exp_pos) <= DIST_EPS

@pytest.mark.parametrize(
    'floor, length',
    [
        (Grass, 240),
        (Ice, 920),
        (Sand, 60),
    ]
)
def test_floor(floor, length):
    ball = Ball(0)
    lvl = Level()
    lvl.set_cells_by_type(floor, [(i,j) for i in range(4, 30) for j in range(4, 7)])
    ball.body.position = cfg.make_screen_centered((5,5))
    ball.add_to_level(lvl)

    ball.apply_force(Vec2d(150, 0))
    for _ in range(100):
        lvl.space.step(0.1)
    ball.update()
    assert fabs(dist(cfg.make_screen_centered((5,5)), ball.rect.center) - length) <= DIST_EPS

