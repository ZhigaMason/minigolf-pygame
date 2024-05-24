""" Generic label """
import pygame

class LabelSprite(pygame.sprite.Sprite):
    """ Generic label """

    def __init__(self, label, w, h, bg_color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([w, h], pygame.SRCALPHA)
        self.image.fill(bg_color)
        lrect = label.get_rect()
        self.image.blit(label, (w // 2 - lrect.w // 2, h // 2 - lrect.h // 2 ))
        self.rect = self.image.get_rect()

    def get_rect(self):
        """ Returns labels rectangle """
        return self.rect

    def set_image(self, img):
        """ Sets new image. Keeps label's center in the same position"""
        center = self.rect.center
        self.rect = img.get_rect()
        self.image = img
        self.rect.center = center
