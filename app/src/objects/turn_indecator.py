import pygame
import pygame.gfxdraw
import util.config as cfg

class TurnIndecator(pygame.sprite.Sprite):

    def __init__(self, pos, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(cfg.TURN_ID_SIZE, pygame.SRCALPHA)
        self.image.fill(cfg.COLORS['NULL'])
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.clr = color
        self.ang_offset = 0
        self.draw_self()

    def draw_self(self):
        self.image.fill(cfg.COLORS['NULL'])
        r = cfg.TURN_ID_RAD
        c = cfg.TURN_ID_CENTER
        ang_seg = int(120 / cfg.TURN_ID_STROKES)
        for i in range(cfg.TURN_ID_STROKES):
            a = 3*i*ang_seg + int(self.ang_offset)
            b = (3*i+1)*ang_seg + int(self.ang_offset)
            for w in range(cfg.TURN_ID_WIDTH):
                pygame.gfxdraw.arc(self.image, *c, r - w, a, b, self.clr)

    def update(self, dt, *args, **kwargs):
        self.ang_offset += cfg.TURN_ID_SPEED*dt
        self.draw_self()
