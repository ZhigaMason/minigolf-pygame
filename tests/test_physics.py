import test_config
import pytest
import app.util.config as cfg
from pymunk import Vec2d
from app.gui.level.level import Level
from app.src.objects.ball import Ball
from math import dist

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
