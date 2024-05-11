import pygame
pygame.font.init()

SCREEN_SIZE = (1280, 960)
CELL_SIZE = 16
GRID_SIZE  = SCREEN_SIZE[0] // CELL_SIZE, SCREEN_SIZE[1] // CELL_SIZE 

PLAYER_BTN_SIZE = (240, 240)
NUM_LEVELS = 12

primary_font = pygame.font.SysFont('Arial', 120)
secondary_font = pygame.font.SysFont('Papyrus', 50)

COLORS = { 
    "BLACK" : (0, 0, 0),
    "WHITE" : (255, 255, 255),
    "RED" : (255, 0, 0),
    "GREEN" : (0, 255, 0),
    "BLUE" : (0, 0, 255),
    "CYAN" : (0, 200, 200),
    "WARM_YELLOW" : "#F4E98C",
}
