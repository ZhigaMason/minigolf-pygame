from util.config import CELL_SIZE, make_screen_centered
import pymunk
import pygame

class Cell(pygame.sprite.Sprite):

    def __init__(self, color, grid_pos):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([CELL_SIZE, CELL_SIZE])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.body = pymunk.Body(1,1, body_type=pymunk.Body.STATIC)
        self.body.position = make_screen_centered(grid_pos) 
        self.set_grid_pos(grid_pos)

    def set_grid_pos(self, grid_pos):
        self.rect.center = self.body.position.x, self.body.position.y

    def add_to_space(self, space):
        space.add(self.body)
