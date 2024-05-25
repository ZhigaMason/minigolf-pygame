""" Module with game managment classes """
from enum import Enum
import pygame
import numpy as np
from pymunk.pygame_util import DrawOptions

import util.config as cfg

from src.objects.ball import Ball
from src.objects.arrow import Arrow
from src.objects.scoreboard import ScoreBoard
from src.objects.turn_indecator import TurnIndecator
from src.objects.labels.select_button import SelectButton
from src.objects.labels.rising_label import RisingLabel
from src.levels_list import levels

from gui.level.level import Level

class GameState(Enum):
    """ Enum used to identify game states """
    INITIAL_STATE = 0
    CHOOSING_PLAYER = 1
    CHOOSING_LEVEL = 2
    PLAYING = 3
    FINAL_STATE = 4
    EXIT = 5

    def __str__(self):
        return f"{self.name}"

class PlayerQueue:
    """ Custom generator for player queue"""

    def __init__(self, player_n):
        self.ary = list(range(player_n))
        self.cnt = -1 # for the no branching

    def __iter__(self):
        while True:
            yield next(self)

    def __next__(self):
        if not self.ary:
            return 0, False
        self.cnt += 1
        if self.cnt >= len(self.ary):
            self.cnt = 0
            return self.ary[self.cnt], True
        return self.ary[self.cnt], False

    def remove(self, n):
        """ Removes given player from queue """
        idx = self.ary.index(n)
        del self.ary[idx]
        if self.cnt >= idx:
            self.cnt -= 1

class GameManager:
    """
        GameManager class is used as a static circuit runnig game from dynamic main_loop
    """

    def __init__(self):
        self.state = GameState.INITIAL_STATE
        self.players = 1
        self.scores = []
        self.total_strikes = []
        self.strikes = []
        self.current_level_number = 0

        self.sprites = pygame.sprite.Group()
        self.btns = pygame.sprite.Group()
        self.decorators = pygame.sprite.Group()

        self.balls = []
        self.plr_queue = PlayerQueue(1)
        self.current_player_number = 0
        self.arrow = None
        self.was_moving = False
        self.turn_id = None

    def reset(self):
        """ Resets game manager and game with it. Should be called at the end or at the begging"""
        self.current_level_number = 0

        self.sprites = pygame.sprite.Group()
        self.btns = pygame.sprite.Group()
        self.decorators = pygame.sprite.Group()

        self.arrow = None
        self.was_moving = False
        self.turn_id = None

    @property
    def lvl(self) -> Level:
        """ Returns reference to current lvl """
        return levels[self.current_level_number]

    @property
    def plr(self) -> Ball:
        """ Returns reference to current player's ball """
        return self.balls[self.current_player_number]

    def pos_in_current_ball(self, pos):
        return self.plr.is_inside(pos)

    def any_movement(self) -> bool:
        """ Checks if balls are moving """
        return any((b.is_moving() for b in self.balls))

    def movement_stopped(self):
        """ Flag switcher for movement """
        if self.was_moving and not self.any_movement():
            self.was_moving = False
            return True
        return False

    def add_player_choosing_btns(self):
        """ Adds selection buttons for choosing number of players """
        for i in range(1, 5):
            text = cfg.secondary_font.render(str(i), False, cfg.COLORS["BLACK"])
            btn = SelectButton(text, i, *cfg.PLAYER_CHOOSING_BTNS_SIZE)
            btn.rect.center = cfg.PLAYER_CHOOSING_BTNS_POS[i - 1]
            btn.add(self.sprites)
            btn.add(self.btns)

    def add_start_level_choosing_btns(self):
        """ Adds selection buttons for choosing start level """
        text = cfg.secondary_font.render('1-6 TUTORIALS', False, cfg.COLORS["DARK_BLUE"])
        btn = SelectButton(text, (0, 6), *cfg.START_LEVEL_CHOOSING_BTNS_SIZE)
        btn.rect.center = cfg.START_LEVEL_CHOOSING_BTNS_POS[0]
        btn.add(self.sprites)
        btn.add(self.btns)
        text = cfg.secondary_font.render('7-12 GOLFMASTER', False, cfg.COLORS["DARK_RED"])
        btn = SelectButton(text, (7, 12), *cfg.START_LEVEL_CHOOSING_BTNS_SIZE)
        btn.rect.center = cfg.START_LEVEL_CHOOSING_BTNS_POS[1]
        btn.add(self.sprites)
        btn.add(self.btns)

        for i in range(2):
            for j in range(6):
                n = 6*i + j
                text = cfg.secondary_font.render(str(n + 1), False, cfg.COLORS["DARK_BLUE"] if i == 0 else cfg.COLORS["DARK_RED"])
                btn = SelectButton(text, (n, n + 1), *cfg.SINGLE_LEVEL_CHOOSING_BTNS_SIZE)
                pos = cfg.SINGLE_LEVEL_CHOOSING_BTNS_POS
                btn.rect.center = pos[0] + j*cfg.SINGLE_LEVEL_CHOOSING_BTNS_SPACE, pos[1] + i*cfg.SINGLE_LEVEL_CHOOSING_BTNS_SPACE
                btn.add(self.sprites)
                btn.add(self.btns)

    def add_score_label(self, score, color):
        """ Adds rising score on the hole """
        label = cfg.ternary_font.render('+' + str(score), False, color)
        txt = RisingLabel(label)
        h = self.lvl.hole.rect.center
        txt.rect.center = (h[0], h[1] - cfg.HOLE_SIZE)
        txt.add(self.sprites)
        txt.add(self.decorators)

    def add_turn_id(self):
        """ Adds turn indecator to the current player """
        pos = self.plr.rect.center
        clr = self.plr.clr
        self.turn_id = TurnIndecator(pos, clr)
        self.turn_id.add(self.sprites)

    def remove_turn_id(self):
        """ Removes turn indecator from current player """
        self.turn_id.remove(self.sprites)

    def add_score_board(self):
        """ Adds scoreboard to sprites """
        pl = self.players
        sb = ScoreBoard(self.scores[:pl], self.total_strikes[:pl])
        sb.add(self.sprites)

    def add_final_buttons(self):
        """ Adds EXIT and RESTART buttons """
        label = cfg.ternary_font.render('CONTINUE', False, cfg.COLORS['BLACK'])
        btn = SelectButton(label, GameState.CHOOSING_LEVEL, *cfg.SCOREBOARD_BTN_SIZE, color = cfg.COLORS['SCOREBOARD_BG'])
        btn.rect.topright = cfg.SCOREBOARD_BTN_RESTART_TR
        btn.add(self.btns, self.sprites)

        label = cfg.ternary_font.render('EXIT', False, cfg.COLORS['BLACK'])
        btn = SelectButton(label, GameState.EXIT, *cfg.SCOREBOARD_BTN_SIZE, color = cfg.COLORS['SCOREBOARD_BG'])
        btn.rect.topleft = cfg.SCOREBOARD_BTN_EXIT_TL
        btn.add(self.btns, self.sprites)

    def player_choose(self):
        """ Function checking if player number was chosen """
        for btn in self.btns:
            if btn.is_clicked():
                self.set_player_number(btn.info)
                return

    def set_player_number(self, n):
        """ Sets player number """
        self.players = n
        self.scores = [ 0 for _ in range(n)]
        self.strikes = np.ones((n,), dtype=int)
        self.total_strikes = np.zeros((n,), dtype=int)
        self.state = GameState.CHOOSING_LEVEL
        self.sprites.empty()
        self.btns.empty()

    def start_level_choose(self):
        """ Function checking if start level was chosen """
        for btn in self.btns:
            if btn.is_clicked():
                self.set_start_level(*btn.info)
                return

    def set_start_level(self, start_lvl, end_lvl):
        """ Sets start level """
        self.current_level_number = start_lvl
        cfg.NUM_LEVELS = end_lvl
        self.state = GameState.PLAYING
        self.sprites.empty()
        self.btns.empty()

    def restart_choose(self):
        """ Function checking if restart or exit was chosen """
        for btn in self.btns:
            if btn.is_clicked():
                self.set_restart(btn.info)
                return

    def set_restart(self, state):
        """ Restarts or end game """
        self.state = state
        self.sprites.empty()
        self.btns.empty()

    def preplay_util(self):
        """ Function manages player dependent objects before game itself """
        self.balls = [Ball(x) for x in range(self.players)]
        for ball in self.balls:
            ball.add(self.sprites)
        self.set_ball_positions()
        self.update_active_players()

    def update_active_players(self):
        """ Updates player queue """
        for ball in self.balls:
            ball.draw_self()
        self.plr_queue = PlayerQueue(self.players)
        self.next_plr()

    def next_plr(self):
        """ Iterates to the next player """
        self.current_player_number, cycled = next(self.plr_queue)
        if self.plr_queue.ary:
            self.add_turn_id()
        if cycled:
            for i in self.plr_queue.ary:
                self.strikes[i] += 1

    def next_level(self):
        """ Iterates to the next level """
        self.was_moving = False
        self.clean_level()
        self.current_level_number += 1
        self.total_strikes += self.strikes
        self.strikes = np.ones((self.players,), dtype=int)
        if self.current_level_number >= cfg.NUM_LEVELS:
            self.state = GameState.FINAL_STATE
            return
        self.set_ball_positions()
        self.update_active_players()

    def clean_level(self):
        """ Cleanes level, practically removing balls from it """
        for n in self.plr_queue.ary:
            self.balls[n].remove_from_level(self.lvl)

    def set_ball_positions(self):
        """ Sets ball positions according to current level """
        for idx, ball in enumerate(self.balls):
            ball.body.position = self.lvl.initial_pos[idx]
            ball.visible = True
            ball.add_to_level(self.lvl)
            ball.update()

    def draw_arrow(self):
        """ Draws arrow """
        ball = self.plr
        self.arrow = Arrow(ball.rect.center, ball.clr)
        self.arrow.add(self.sprites)
        self.remove_turn_id()

    def leave_arrow(self):
        """ Sends ball flying according to arrow tension """
        force = self.arrow.force
        self.arrow.kill()
        if force.length <= cfg.ARROW_MIN_LENGTH:
            self.add_turn_id()
            return
        self.plr.apply_force(cfg.ARROW_MULTIPLIER * force)
        self.was_moving = True

    def blit_init(self, screen):
        """ Paints initial screen """
        init_display = cfg.initial_bg
        screen.blit(init_display, (0, 0))
        ctc = cfg.secondary_font.render('click to continue', False, cfg.COLORS['BLACK'])
        txt_rect = ctc.get_rect()
        txt_rect.center = cfg.SCREEN_SIZE[0] // 2, 7 * cfg.SCREEN_SIZE[1] // 8
        screen.blit(ctc, txt_rect)


    def blit_choose_player(self, screen):
        """ Paints choosing player number screen """
        screen.fill(cfg.COLORS['DARK_GREEN'])
        txt = cfg.secondary_font.render('CHOOSE NUMBER OF PLAYERS', False, cfg.COLORS['WHITE'])
        txt_rect = txt.get_rect()
        txt_rect.center = cfg.SCREEN_SIZE[0] // 2, cfg.SCREEN_SIZE[1] // 8
        screen.blit(txt, txt_rect)
        self.sprites.draw(screen)

    def blit_choose_mode(self, screen):
        """ Paints starting level screen """
        screen.fill(cfg.COLORS['DARK_GREEN'])
        txt = cfg.secondary_font.render('CHOOSE EPISODE OR LEVEL', False, cfg.COLORS['WHITE'])
        txt_rect = txt.get_rect()
        txt_rect.center = cfg.SCREEN_SIZE[0] // 2, cfg.SCREEN_SIZE[1] // 8
        screen.blit(txt, txt_rect)
        self.sprites.draw(screen)

    def blit_current_level(self, screen):
        """ Paints paints current level onto screen """
        lvl = levels[self.current_level_number]

        if cfg.DEBUG:
            draw_options = DrawOptions(screen)
            lvl.space.debug_draw(draw_options)
        lvl.sprites.draw(screen)
        self.sprites.draw(screen)

    def blit_score_board(self, screen):
        """ Paints scoreboard onto screen """
        self.sprites.draw(screen)

    def update_game(self, *args, **kwargs):
        """ Updates game while playing """
        if self.state != GameState.PLAYING:
            return
        self.update_physics()
        self.update_visuals(*args, **kwargs)
        self.update_logic()

    def update_physics(self):
        """ Runs physical simulation """
        self.lvl.space.step(1 / (cfg.FPS))

    def update_visuals(self, *args, **kwargs):
        """ Updates all visuals """
        self.sprites.update(*args, **kwargs)

    def update_logic(self):
        """ Updates logic such as scores and levels """
        hole = self.lvl.hole
        for n in self.plr_queue.ary:
            ball = self.balls[n]
            if hole.is_inside(ball):
                n = ball.num
                ball.make_clear()
                ball.remove_from_level(self.lvl)
                self.plr_queue.remove(n)
                self.count_score(n)
        if not self.decorators and not self.plr_queue.ary:
            self.next_level()

    def count_score(self, n):
        """ adds proper amount of score to given player """
        strk = self.strikes[n]
        board = sorted(list(set(self.strikes)))
        earned = 5 - board.index(strk)
        self.scores[n] += earned
        self.add_score_label(earned, self.balls[n].clr)
