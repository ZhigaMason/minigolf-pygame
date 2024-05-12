import pygame
pygame.font.init()

SCREEN_SIZE = (1280, 960)
CELL_SIZE = 32
GRID_SIZE  = SCREEN_SIZE[0] // CELL_SIZE, SCREEN_SIZE[1] // CELL_SIZE 

def make_grid_pos(pos):
    return pos[0] // CELL_SIZE, pos[1] // CELL_SIZE

def make_screen_pos(grid_pos):
    return grid_pos[0] * CELL_SIZE, grid_pos[1] * CELL_SIZE

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

BALL_SIZE = 16
BALL_RAD = BALL_SIZE // 2

HOLE_SIZE = 24
HOLE_RAD = HOLE_SIZE // 2

BALL_COLORS = [
    (255, 255, 255), 
    (255, 200, 200), 
    (200, 200, 255), 
    (200, 255, 200), 
]
