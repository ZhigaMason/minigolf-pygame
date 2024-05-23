import test_config
import pytest
import app.util.config as cfg
from app.src.game.manager import GameManager, GameState
from app.src.objects.ball import Ball


@pytest.mark.parametrize(
    'plr_n, starting_lvl, end_state',
    [
        (plr_n, starting_lvl, end_state)
        for plr_n in range(1,5)
        for starting_lvl in range(cfg.NUM_LEVELS - 1)
        for end_state in (GameState.EXIT, GameState.CHOOSING_PLAYER) 
    ]
)
def test_setup_cycle(plr_n : int, starting_lvl : int, end_state : GameState ):
    test_initializing()

    man : GameManager = GameManager()
    man.state = GameState.CHOOSING_PLAYER
    test_set_players(man, plr_n)
    test_set_start_level(man, starting_lvl)
    test_preplay_util(man)
    test_level_progression(man)
    test_set_restart(man, end_state)

def test_initializing():
    man = GameManager()
    assert man.state == GameState.INITIAL_STATE

@pytest.fixture
def man_choosing_plr():
    man : GameManager = GameManager()
    man.state = GameState.CHOOSING_PLAYER
    return man

@pytest.mark.parametrize(
    'plr_n',
    [plr_n for plr_n in range(1, 5)]
)
def test_set_players(man_choosing_plr : GameManager, plr_n):
    man_choosing_plr.set_player_number(plr_n)
    assert man_choosing_plr.players == plr_n
    assert not man_choosing_plr.btns
    assert not man_choosing_plr.sprites
    assert man_choosing_plr.state == GameState.CHOOSING_MODE

@pytest.fixture
def man_choosing_level(man_choosing_plr):
    man_choosing_plr.set_player_number(1)
    return man_choosing_plr

@pytest.mark.parametrize(
    'starting_lvl',
    [lvl for lvl in range(cfg.NUM_LEVELS)]
)
def test_set_start_level(man_choosing_level : GameManager, starting_lvl : int):
    man_choosing_level.set_start_level(starting_lvl)
    assert man_choosing_level.current_level == starting_lvl
    assert not man_choosing_level.btns
    assert not man_choosing_level.sprites
    assert man_choosing_level.state == GameState.PLAYING

@pytest.fixture
def man_finish_choose(man_choosing_level):
    man_choosing_level.set_start_level(10)
    return man_choosing_level

def test_preplay_util(man_finish_choose):
    man_finish_choose.preplay_util()
    assert len(man_finish_choose.plr_queue.ary) == man_finish_choose.players
    assert len(man_finish_choose.balls) == man_finish_choose.players

@pytest.fixture
def man_preplay_util(man_finish_choose):
    man_finish_choose.preplay_util()
    return man_finish_choose

def test_level_progression(man_preplay_util):
    man = man_preplay_util
    starting_lvl = man.current_level
    for _ in range(starting_lvl, cfg.NUM_LEVELS):
        assert man.state == GameState.PLAYING
        man.next_level()
    assert man.state == GameState.FINAL_STATE

@pytest.fixture
def man_played(man_preplay_util):
    man = man_preplay_util
    while man.state != GameState.FINAL_STATE:
        man.next_level()
    return man

@pytest.mark.parametrize(
    'end_state',
    [GameState.EXIT, GameState.CHOOSING_PLAYER]
)
def test_set_restart(man_played, end_state):
    man = man_played
    man.set_restart(end_state)
    assert man.state == end_state
    assert not man.btns
    assert not man.sprites
