import pygame

class LabelSprite(pygame.sprite.Sprite):

    def __init__(self, label, w, h, bg_color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([w, h], pygame.SRCALPHA)
        self.image.fill(bg_color)
        lrect = label.get_rect();
        self.image.blit(label, (w // 2 - lrect.w // 2, h // 2 - lrect.h // 2 ))
        self.rect = self.image.get_rect()
