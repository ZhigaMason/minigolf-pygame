import pygame
from config import BALL_SIZE, BALL_RAD, BALL_COLORS, make_grid_pos
from pygame import Vector2

class Ball(pygame.sprite.Sprite):

    def __init__(self, player_num):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([BALL_SIZE, BALL_SIZE], pygame.SRCALPHA)
        self.rect = pygame.draw.circle(self.image, BALL_COLORS[player_num], (BALL_RAD, BALL_RAD), BALL_RAD)
        self.set_default()

    def set_default(self, pos = (0, 0), visible = True):
        self.visible = visible
        self.rect.center = pos
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)
        self.friction = 1.0

    def is_moving(self):
        return self.vel.length_squared() >= 0.1
    
    def apply_force(self, force):
        self.acc += force

    def move(self, t):
        self.vel += self.acc * t
        self.vel *= self.friction
        self.rect.center += self.vel * t

    def grid_coord(self):
        return make_grid_pos(self.rect.center)
