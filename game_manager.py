import pygame
from levels import levels
from enum import Enum
import config

class GameState(Enum):
    INITIAL_STATE = 0
    CHOOSING_PLAYER = 1
    CHOOSING_MODE = 2
    PLAYING = 3

    def __str__(self):
        return f"{self.name}"

class GameManager:

    def __init__(self):
        self.state = GameState.INITIAL_STATE
        self.players = 1
        self.scores = [0 for _ in range(4)]
        self.throws = [0 for _ in range(4)]
        self.levels = levels 

    def in_state(self, state) -> bool:
        return self.state == state
    

    def blit_init(self, screen):
        start_text = config.primary_font.render("Minigolf Game", False, (255, 0, 0))
        rect = start_text.get_rect()
        screen.blit(start_text, (config.SCREEN_SIZE[0] // 2 - rect.center[0],config.SCREEN_SIZE[1] // 2 - rect.center[1]))
    
