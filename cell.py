from config import CELL_SIZE, make_screen_pos
import pygame

class Cell(pygame.sprite.Sprite):

    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([CELL_SIZE, CELL_SIZE])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def set_grid_pos(self, grid_pos):
        self.rect.topleft = make_screen_pos(grid_pos)
