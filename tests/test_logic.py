import test_config
import pytest
import numpy as np
import app.util.config as cfg
from app.src.game.manager import GameManager
from app.src.objects.ball import Ball

@pytest.mark.parametrize(
    'plr_n, strike_list, exp_pts',
    [
        (4, [[1,2,9,1] ], [5, 4, 3, 5]),
        (3, [[2,2,2]], [5,5,5]),
        (4, [[10, 2, 7, 8]], [2, 5, 4, 3]),
        (2, [[6, 3],[1, 2]], [9, 9]),
        (3, [[1, 3, 2],[6,2,3],[5,5,7]], [13,13,12])
    ]
)
def test_strike_pts_correleation(plr_n :int, strike_list, exp_pts :list[int]):
    man = GameManager()
    man.set_player_number(plr_n)
    man.set_start_level(0)
    man.preplay_util()

    for strikes in strike_list:
        man.strikes = strikes
        for i in range(plr_n):
            man.count_score(i)
        man.next_level()
    assert man.scores == exp_pts

@pytest.mark.parametrize(
    'plr_n',
    [1, 2, 3, 4]
)
def test_hole(plr_n : int):
    man = GameManager()
    man.set_player_number(plr_n)
    man.set_start_level(0)
    man.preplay_util()

    for _ in range(cfg.NUM_LEVELS):
        hole_pos = man.current_lvl.hole.rect.center
        lvl_n = man.current_level
        for i in range(plr_n):
            man.balls[i].body.position = hole_pos
        for _ in range(10):
            man.update_game(10)
        assert lvl_n + 1 == man.current_level
    assert man.scores == [60 for _ in range(plr_n)]

