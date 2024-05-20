import pygame
import pymunk
import config as cfg
from config import BALL_SIZE, BALL_RAD, BALL_COLORS, make_grid_pos
from math import dist
from levels import Level

class Ball(pygame.sprite.Sprite):

    def __init__(self, player_num):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([BALL_SIZE, BALL_SIZE], pygame.SRCALPHA)
        self.rect = pygame.draw.circle(self.image, BALL_COLORS[player_num], (BALL_RAD, BALL_RAD), BALL_RAD)
        self.clr = BALL_COLORS[player_num]
        self.set_default()
        self.body = pymunk.Body(cfg.BALL_MASS, cfg.BALL_INERTIA)
        self.shape = pymunk.Circle(self.body, BALL_RAD )
        self.shape.elasticity = cfg.BALL_ELASTICITY
        self.pivot = None

    def set_default(self, pos = (0, 0), visible = True):
        self.visible = visible
        self.rect.center = pos

    def is_moving(self):
        return self.body.get_length_sqrd() >= 0.01

    def is_inside(self, pos) -> bool:
        return dist(self.rect.center, pos) <= BALL_RAD
    
    def apply_force(self, force):
        self.body.apply_impulse_at_local_point(force, (0,0))

    def update(self, *args, **kwargs):
        self.rect.center = self.body.position

    def add_to_level(self, level : Level):
        space = level.space
        pivot = pymunk.PivotJoint(space.static_body, self.body, (0,0), (0,0))
        pivot.max_bias = 0
        pivot.grid = level.grid
        
        def pre_solve_fn(c, _):
            gx, gy = make_grid_pos(c.b.position)
            c.max_force = c.grid[gx][gy]
        
        pivot.pre_solve = pre_solve_fn
        self.pivot = pivot
        space.add(self.body, self.shape, self.pivot)

    def remove_from_level(self, space):
        space.remove(self.body, self.shape, self.pivot)
