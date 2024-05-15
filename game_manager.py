import pygame
import config
from levels import levels, Level
from enum import Enum
from game_objects import SelectButton
from ball import Ball

class GameState(Enum):
    INITIAL_STATE = 0
    CHOOSING_PLAYER = 1
    CHOOSING_MODE = 2
    PLAYING = 3
    FINAL_STATE = 4

    def __str__(self):
        return f"{self.name}"

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
        self.active_players = []

    def get_curr_lvl(self) -> Level:
        return levels[self.current_level]

    def add_player_choosing_btns(self):
        for i in range(1, 5):
            text = config.secondary_font.render(str(i), False, config.COLORS["GREEN"])
            btn = SelectButton(text, i)
            # count place
            btn.rect.center = (i * 300, config.SCREEN_SIZE[1] // 2 - btn.rect.h // 2)
            btn.add(self.sprites)
            btn.add(self.btns)

    def add_mode_choosing_btns(self):
        text = config.secondary_font.render('1-12', False, config.COLORS["BLUE"])
        btn = SelectButton(text, 0, 240, 360)
        btn.rect.center = (config.SCREEN_SIZE[0] // 2 - 40 - btn.rect.w // 2 , config.SCREEN_SIZE[1] // 2 - btn.rect.h // 2)
        btn.add(self.sprites)
        btn.add(self.btns)
        text = config.secondary_font.render('7-12', False, config.COLORS["BLUE"])
        btn = SelectButton(text, 6, 240, 360)
        btn.rect.center = (config.SCREEN_SIZE[0] // 2 + 40 + btn.rect.w // 2 , config.SCREEN_SIZE[1] // 2 - btn.rect.h // 2)
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
        self.active_players = [ i for i in range(self.players)]

    def next_level(self):
        self.current_level += 1
        print(self.current_level)
        if self.current_level >= config.NUM_LEVELS:
            self.state = GameState.FINAL_STATE
            return
        self.set_ball_positions()

    def set_ball_positions(self):
        for idx, ball in enumerate(self.balls):
            ball.rect.center = levels[self.current_level].initial_pos[idx]
            ball.visible = True
 
    def blit_init(self, screen):
        start_text = config.primary_font.render("Minigolf Game", False, config.COLORS["WHITE"])
        rect = start_text.get_rect()
        screen.blit(start_text, (config.SCREEN_SIZE[0] // 2 - rect.center[0],config.SCREEN_SIZE[1] // 2 - rect.center[1]))

    def blit_choose_player(self, screen):
        self.sprites.draw(screen)

    def blit_choose_mode(self, screen):
        self.sprites.draw(screen)

    def blit_current_level(self, screen):
        lvl = levels[self.current_level]
        lvl.group.draw(screen)
        self.sprites.draw(screen)

    def display_scores(self, screen):
        raise NotImplementedError()
