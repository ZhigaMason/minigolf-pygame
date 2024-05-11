import pygame
import config
from levels import levels
from enum import Enum
from game_objects import SelectButton

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
        self.levels = levels 
        self.sprites = pygame.sprite.Group()

    def add_player_choosing_btns(self):
        for i in range(1, 5):
            text = config.secondary_font.render(str(i), False, config.COLORS["GREEN"])
            btn = SelectButton(text, i)
            # count place
            btn.rect.center = (i * 300, config.SCREEN_SIZE[0] // 2 - btn.rect.h // 2)
            btn.add(self.sprites)

    def player_choose(self):
        for btn in self.sprites:
            if btn.is_clicked():
                self.players = btn.info
                self.state = GameState.CHOOSING_MODE
                self.sprites.empty()
                return
 
    def blit_init(self, screen):
        start_text = config.primary_font.render("Minigolf Game", False, config.COLORS["WHITE"])
        rect = start_text.get_rect()
        screen.blit(start_text, (config.SCREEN_SIZE[0] // 2 - rect.center[0],config.SCREEN_SIZE[1] // 2 - rect.center[1]))

    def blit_choose_player(self, screen):
        self.sprites.draw(screen)
