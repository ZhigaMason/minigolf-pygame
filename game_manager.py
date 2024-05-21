import pymunk
import pygame
import config as cfg
from levels import levels, Level
from enum import Enum
from game_objects import SelectButton, RisingLabel, TurnIndecator
from ball import Ball
from arrow import Arrow
from pymunk.pygame_util import DrawOptions
from pygame.math import Vector2

class GameState(Enum):
    INITIAL_STATE = 0
    CHOOSING_PLAYER = 1
    CHOOSING_MODE = 2
    PLAYING = 3
    FINAL_STATE = 4

    def __str__(self):
        return f"{self.name}"

class PlayerQueue:

    def __init__(self, player_n):
        self.ary = [ i for i in range(player_n)]
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
        idx = self.ary.index(n)
        del self.ary[idx]
        if self.cnt >= idx:
            self.cnt -= 1

class GameManager:

    def __init__(self):
        self.state = GameState.INITIAL_STATE
        self.players = 1
        self.scores = [0 for _ in range(4)]
        self.strikes = []
        self.current_level = 0

        self.sprites = pygame.sprite.Group()
        self.btns = pygame.sprite.Group()
        self.decorators = pygame.sprite.Group()

        self.balls = []
        self.plr_queue = PlayerQueue(1)
        self.current_player = 0
        self.arrow = None
        self.was_moving = False
        self.turn_id = None

    @property
    def current_lvl(self) -> Level:
        return levels[self.current_level]

    @property
    def current_plr(self) -> Ball:
        return self.balls[self.current_player]

    def any_movement(self) -> bool:
        return any((b.is_moving() for b in self.balls))

    def pos_in_current_ball(self, pos) -> bool:
        return self.balls[self.current_player].is_inside(pos)

    def movement_stopped(self):
        if self.was_moving and not self.any_movement():
            self.was_moving = False
            return True
        return False

    def add_player_choosing_btns(self):
        for i in range(1, 5):
            text = cfg.secondary_font.render(str(i), False, cfg.COLORS["GREEN"])
            btn = SelectButton(text, i)
            # count place
            btn.rect.center = (i * 300, cfg.SCREEN_SIZE[1] // 2 - btn.rect.h // 2)
            btn.add(self.sprites)
            btn.add(self.btns)

    def add_mode_choosing_btns(self):
        text = cfg.secondary_font.render('1-12', False, cfg.COLORS["BLUE"])
        btn = SelectButton(text, 0, 240, 360)
        btn.rect.center = (cfg.SCREEN_SIZE[0] // 2 - 40 - btn.rect.w // 2 , cfg.SCREEN_SIZE[1] // 2 - btn.rect.h // 2)
        btn.add(self.sprites)
        btn.add(self.btns)
        text = cfg.secondary_font.render('7-12', False, cfg.COLORS["BLUE"])
        btn = SelectButton(text, 6, 240, 360)
        btn.rect.center = (cfg.SCREEN_SIZE[0] // 2 + 40 + btn.rect.w // 2 , cfg.SCREEN_SIZE[1] // 2 - btn.rect.h // 2)
        btn.add(self.sprites)
        btn.add(self.btns)

    def add_score_label(self, score, color):
        label = cfg.ternary_font.render('+' + str(score), False, color)
        txt = RisingLabel(label)
        h = self.current_lvl.hole.rect.center
        txt.rect.center = (h[0], h[1] - cfg.HOLE_SIZE) 
        txt.add(self.sprites)
        txt.add(self.decorators)

    def add_turn_id(self):
        pos = self.current_plr.rect.center
        clr = self.current_plr.clr
        self.turn_id = TurnIndecator(pos, clr)
        self.turn_id.add(self.sprites)

    def remove_turn_id(self):
        self.turn_id.remove(self.sprites)

    def player_choose(self):
        for btn in self.btns:
            if btn.is_clicked():
                self.players = btn.info
                self.strikes = [0 for _ in range(self.players)]
                self.state = GameState.CHOOSING_MODE
                self.sprites.empty()
                self.btns.empty()
                return

    def mode_choose(self):
        for btn in self.sprites:
            if btn.is_clicked():
                self.current_level = btn.info
                self.state = GameState.PLAYING
                self.sprites.empty()
                self.btns.empty()
                return

    def preplay_util(self):
        self.balls = [Ball(x) for x in range(self.players)]
        for ball in self.balls:
            ball.add(self.sprites)
        self.set_ball_positions()
        self.update_active_players()

    def update_active_players(self):
        for ball in self.balls:
            ball.draw_self()
        self.plr_queue = PlayerQueue(self.players)
        self.next_plr()

    def next_plr(self):
        self.current_player, cycled = next(self.plr_queue)
        if self.plr_queue.ary:
            self.add_turn_id()
        if cycled:
            for i in self.plr_queue.ary:
                self.strikes[i] += 1
 

    def next_level(self):
        self.was_moving = False
        self.current_level += 1
        self.strikes = [ 0 for _ in range(self.players)]
        if self.current_level >= cfg.NUM_LEVELS:
            self.state = GameState.FINAL_STATE
            return
        self.clean_level()
        self.set_ball_positions()
        self.update_active_players()

    def clean_level(self):
        for n in self.plr_queue.ary:
            self.balls[n].remove_from_level(self.current_lvl)

    def set_ball_positions(self):
        for idx, ball in enumerate(self.balls):
            ball.body.position = self.current_lvl.initial_pos[idx]
            ball.visible = True
            ball.add_to_level(self.current_lvl)
            ball.update()

    def draw_arrow(self):
        ball = self.current_plr
        self.arrow = Arrow(ball.rect.center, ball.clr)
        self.arrow.add(self.sprites)
        self.remove_turn_id()

    def leave_arrow(self):
        force = self.arrow.force
        self.arrow.kill()
        if force.get_length_sqrd() <= cfg.ARROW_MIN_LENGTH:
            return
        self.current_plr.apply_force(force)
        self.was_moving = True

    def blit_init(self, screen):
        start_text = cfg.primary_font.render("Minigolf Game", False, cfg.COLORS["WHITE"])
        rect = start_text.get_rect()
        screen.blit(start_text, (cfg.SCREEN_SIZE[0] // 2 - rect.center[0],cfg.SCREEN_SIZE[1] // 2 - rect.center[1]))

    def blit_choose_player(self, screen):
        self.sprites.draw(screen)

    def blit_choose_mode(self, screen):
        self.sprites.draw(screen)

    def blit_current_level(self, screen):
        lvl = levels[self.current_level]

        if cfg.DEBUG:
            draw_options = DrawOptions(screen)
            lvl.space.debug_draw(draw_options)
        lvl.sprites.draw(screen)
        self.sprites.draw(screen)

    def update_physics(self):
        self.current_lvl.space.step(1 / (cfg.FPS))

    def update_visuals(self, *args, **kwargs):
        self.sprites.update(*args, **kwargs)

    def update_logic(self):
        hole = self.current_lvl.hole
        for n in self.plr_queue.ary:
            ball = self.balls[n]
            if hole.is_inside(ball):
                n = ball.num
                ball.make_clear()
                ball.remove_from_level(self.current_lvl)
                self.plr_queue.remove(n)
                self.count_score(n)
                print(f'ball #{n} has hit the hole on {self.strikes[n]} strikes')
        if not self.decorators and not self.plr_queue.ary:
            self.next_level()

    def count_score(self, n):
        strk = self.strikes[n]
        board = sorted(list(set(self.strikes)))
        earned = 5 - board.index(strk)
        self.scores[n] += earned
        self.add_score_label(earned, self.balls[n].clr)

    def display_scores(self, screen):
        pass
        raise NotImplementedError()
