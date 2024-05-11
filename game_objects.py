import pygame
from config import COLORS

class SelectButton(pygame.sprite.Sprite):

    def __init__(self, label, info, w = 240, h = 240, color = COLORS["WHITE"]):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([w, h])
        self.image.fill(color)
        lrect = label.get_rect();
        self.image.blit(label, (w // 2 - lrect.w // 2, h // 2 - lrect.h // 2 ))
        self.rect = self.image.get_rect()
        self.info = info

    def inrect(self, x, y) -> bool:
        return self.rect.topleft[0] <= x and self.rect.topleft[1] <= y and x <= self.rect.bottomright[0] and y <= self.rect.bottomright[1]

    def is_clicked(self) -> bool:
        print(self.rect, pygame.mouse.get_pos())
        return pygame.mouse.get_pressed()[0] and self.inrect(*pygame.mouse.get_pos())
