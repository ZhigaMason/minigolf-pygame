import pygame

DEBUG = 0
pygame.font.init()

FPS = 60
DIV = 10
NUM_LEVELS = 1

SCREEN_SIZE = (1280, 960)
CELL_SIZE = 32
GRID_SIZE  = SCREEN_SIZE[0] // CELL_SIZE, SCREEN_SIZE[1] // CELL_SIZE 

def make_grid_pos(pos):
    return int(pos[0] // CELL_SIZE), int(pos[1] // CELL_SIZE)

def make_screen_pos(grid_pos):
    return grid_pos[0] * CELL_SIZE, grid_pos[1] * CELL_SIZE

def make_screen_centered(grid_pos):
    return grid_pos[0] * CELL_SIZE + CELL_SIZE // 2, grid_pos[1] * CELL_SIZE + CELL_SIZE // 2

primary_font = pygame.font.SysFont('Arial', 120)
secondary_font = pygame.font.SysFont('Papyrus', 50)
ternary_font = pygame.font.SysFont('Helvetica', 30)
scoreboard_font1 = pygame.font.SysFont('Helvetica', 50)
scoreboard_font2 = pygame.font.SysFont('Helvetica', 35)
scoreboard_font3 = pygame.font.SysFont('Helvetica', 30)

COLORS = { 
    "BLACK" : (0, 0, 0),
    "WHITE" : (255, 255, 255),
    "RED" : (255, 0, 0),
    "GREEN" : (0, 255, 0),
    "BLUE" : (0, 0, 255),
    "CYAN" : (0, 200, 200),
    "WARM_YELLOW" : "#F4E98C",
    "NULL" : (0, 0, 0, 0),

    "WALL_GREY" : (120, 120, 120),
    "WALL_BLUE" : (100, 100, 140),
    "GRASS_GREEN" : (100, 200, 100),
    "SAND_YELLOW" : (250,234,128),
    "ICE_BLUE" : (153,238,255),

    "SCOREBOARD_BG" : (255,254,210),
    "SCOREBOARD_BLACK" : (0,0,0, 100),
    "SCOREBOARD_PRP" : (77,0,51, 100),
}

BALL_SIZE = 16
BALL_RAD = BALL_SIZE // 2
BALL_MASS = 0.5
BALL_INERTIA = 1
BALL_ELASTICITY = 0.99999

BALL_COLORS = [
    (255, 255, 255), 
    (255, 200, 200), 
    (200, 200, 255), 
    (200, 255, 200),
]

TURN_ID_STROKES = 6
TURN_ID_SIZE = (6*BALL_SIZE, 6*BALL_SIZE)
TURN_ID_CENTER = (TURN_ID_SIZE[0] // 2,TURN_ID_SIZE[1] // 2)
TURN_ID_WIDTH = 4
TURN_ID_RAD = 2 * BALL_SIZE
TURN_ID_SPEED = 5

HOLE_SIZE = 24
HOLE_RAD = HOLE_SIZE // 2

ARROW_MAX_LENGTH = 180
ARROW_MIN_LENGTH = 2*BALL_SIZE
ARROW_BOX_SIZE = 600, 600
ARROW_BALL_GAP = ARROW_MIN_LENGTH

SCOREBOARD_SIZE = 2 * SCREEN_SIZE[0] // 3, 2 * SCREEN_SIZE[1] // 3
SCOREBOARD_POS =  SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2
SCOREBOARD_GAP = 10

SCOREBOARD_BTN_GAP = 20
SCOREBOARD_BTN_SB_GAP = 10
SCOREBOARD_BTN_SIZE = SCOREBOARD_SIZE[0] // 2 - SCOREBOARD_BTN_GAP, 50
SCOREBOARD_BTN_Y = SCOREBOARD_SIZE[1] // 2 + SCOREBOARD_POS[1] + SCOREBOARD_BTN_SB_GAP
SCOREBOARD_BTN_EXIT_TL = SCREEN_SIZE[0] // 2 + SCOREBOARD_BTN_GAP, SCOREBOARD_BTN_Y
SCOREBOARD_BTN_RESTART_TR = SCREEN_SIZE[0] // 2 - SCOREBOARD_BTN_GAP, SCOREBOARD_BTN_Y
