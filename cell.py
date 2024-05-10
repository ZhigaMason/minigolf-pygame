from config import CELL_SIZE
import pygame

class Cell(pygame.sprite.Sprite):

    def __init__(self, color = (255,255,102)):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([CELL_SIZE, CELL_SIZE])
        self.image.fill(color)
        self.rect = self.image.get_rect()
