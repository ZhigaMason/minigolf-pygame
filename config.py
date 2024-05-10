import pygame
pygame.font.init()

SCREEN_SIZE = (1280, 960)
CELL_SIZE = 16
GRID_SIZE  = SCREEN_SIZE[0] // CELL_SIZE, SCREEN_SIZE[1] // CELL_SIZE 

NUM_LEVELS = 12

primary_font = pygame.font.SysFont('Arial', 50)
