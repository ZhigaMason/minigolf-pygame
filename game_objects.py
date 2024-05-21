import pygame
import config as cfg

class TextSprite(pygame.sprite.Sprite):
    def __init__(self, label, w, h, bg_color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([w, h], pygame.SRCALPHA)
        self.image.fill(bg_color)
        lrect = label.get_rect();
        self.image.blit(label, (w // 2 - lrect.w // 2, h // 2 - lrect.h // 2 ))
        self.rect = self.image.get_rect()

class SelectButton(TextSprite):

    def __init__(self, label, info, w = 240, h = 360, color = cfg.COLORS['WHITE']):
        TextSprite.__init__(self, label, w, h, color)
        self.info = info

    def inrect(self, x, y) -> bool:
        return self.rect.topleft[0] <= x and self.rect.topleft[1] <= y and x <= self.rect.bottomright[0] and y <= self.rect.bottomright[1]

    def is_clicked(self) -> bool:
        print(self.rect, pygame.mouse.get_pos())
        return pygame.mouse.get_pressed()[0] and self.inrect(*pygame.mouse.get_pos())

class RisingText(TextSprite):

    def __init__(self, label, w = 100, h = 50, bg_color = cfg.COLORS['NULL'], alt = 100, acc = 2):
        TextSprite.__init__(self, label, w, h, bg_color)
        self.alt = alt
        self.vel = 0
        self.acc = acc

    def update(self, dt, *args, **kwargs):
        self.vel += dt * self.acc
        s = dt * self.vel
        self.alt -= s
        self.rect.center = self.rect.center[0], self.rect.center[1] - s
        if self.alt <= 0:
            self.kill()
