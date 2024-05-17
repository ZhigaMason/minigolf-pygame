import pygame
import config as cfg
from levels import levels, Level
from enum import Enum
from game_objects import SelectButton
from ball import Ball
from arrow import Arrow

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
        self.len = player_n
        self.cnt = -1 # for the no branching

    def __iter__(self):
        while True:
            yield next(self)
    
    def __next__(self):
        self.cnt += 1
        if self.cnt >= self.len:
            self.cnt = 0
        return self.cnt

class GameManager:

    def __init__(self):
        self.state = GameState.INITIAL_STATE
        self.players = 1
        self.scores = [0 for _ in range(4)]
        self.throws = [0 for _ in range(4)]
        self.current_level = 0
        self.sprites = pygame.sprite.Group()
        self.btns = pygame.sprite.Group()
        self.balls = []
        self.plr_queue = PlayerQueue(1)
        self.current_player = 0
        self.arrow = None

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

    def player_choose(self):
        for btn in self.btns:
            if btn.is_clicked():
                self.players = btn.info
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
        self.update_active_players()
        self.set_ball_positions()

    def update_active_players(self):
        self.plr_queue = PlayerQueue(self.players)
        self.current_player = next(self.plr_queue)

    def next_level(self):
        self.current_level += 1
        if self.current_level >= cfg.NUM_LEVELS:
            self.state = GameState.FINAL_STATE
            return
        self.update_active_players()
        self.set_ball_positions()

    def set_ball_positions(self):
        for idx, ball in enumerate(self.balls):
            ball.rect.center = levels[self.current_level].initial_pos[idx]
            ball.visible = True

    def set_ball_friction(self):
        for ball in self.balls:
            x, y = cfg.make_grid_pos(ball.rect.center)
            ball.friction = self.current_lvl.grid[x][y].friction

    def draw_arrow(self):
        self.arrow = Arrow(self.balls[self.current_player].rect.center)
        self.arrow.add(self.sprites)

    def leave_arrow(self):
        self.arrow.kill()
        self.balls[self.current_player].apply_force(self.arrow.force / 2)
        self.current_player = next(self.plr_queue)
 
    def blit_init(self, screen):
        start_text = cfg.primary_font.render("Minigolf Game", False, cfg.COLORS["WHITE"])
        rect = start_text.get_rect()
        screen.blit(start_text, (cfg.SCREEN_SIZE[0] // 2 - rect.center[0],cfg.SCREEN_SIZE[1] // 2 - rect.center[1]))

    def blit_choose_player(self, screen):
        self.sprites.draw(screen)

    def blit_choose_mode(self, screen):
        self.sprites.draw(screen)

    def blit_current_level(self, screen, tick):
        lvl = levels[self.current_level]
        lvl.group.draw(screen)
        self.set_ball_friction()
        self.sprites.update(tick)
        self.sprites.draw(screen)

    def display_scores(self, screen):
        pass
        raise NotImplementedError()
