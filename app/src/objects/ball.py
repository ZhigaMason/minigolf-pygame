""" Golfball module """
from math import dist
import pygame
import pymunk
from pymunk.vec2d import Vec2d as v2
import util.config as cfg

from util.config import BALL_SIZE, BALL_RAD, BALL_COLORS, make_grid_pos
from gui.level.level import Level

class Ball(pygame.sprite.Sprite):
    """ Class implementing golfball """

    def __init__(self, player_num):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([BALL_SIZE, BALL_SIZE], pygame.SRCALPHA)
        self.rect = pygame.draw.circle(self.image, BALL_COLORS[player_num], (BALL_RAD, BALL_RAD), BALL_RAD)
        self.num = player_num
        self.visible = True
        self.rect.center = (0, 0)
        self.body = pymunk.Body(cfg.BALL_MASS, cfg.BALL_INERTIA)
        self.shape = pymunk.Circle(self.body, BALL_RAD )
        self.shape.elasticity = cfg.BALL_ELASTICITY
        self.pivot = None

    @property
    def clr(self):
        """ Color of the ball property """
        return BALL_COLORS[self.num]

    def make_clear(self):
        """ Makes ball invisible by setting filling its image with transperent color"""
        self.image.fill(cfg.COLORS['NULL'])

    def draw_self(self):
        """ Draws circle on its own surface """
        pygame.draw.circle(self.image, self.clr, (BALL_RAD, BALL_RAD), BALL_RAD)

    def is_moving(self):
        """ Checks if ball is moving """
        return self.body.velocity.get_length_sqrd() >= 0.01

    def is_inside(self, pos) -> bool:
        """ Checks if given position is inside the ball """
        return dist(self.rect.center, pos) <= BALL_RAD

    def apply_force(self, force : v2):
        """ Applies force to ball as pymunk dynamic body """
        self.body.apply_impulse_at_local_point(force, (0,0))

    def update(self, *args, **kwargs):
        """ Updates sprite part of ball to its pymunk part """
        self.rect.center = self.body.position

    def add_to_level(self, level : Level):
        """ Adds ball to level and creates friction joint """
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

    def remove_from_level(self, level):
        """ Removes ball from level and stops its motion """
        self.body.velocity = v2(0,0)
        self.body.force = v2(0,0)
        level.space.remove(self.body, self.shape, self.pivot)
