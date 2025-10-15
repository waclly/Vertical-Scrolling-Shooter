import pygame
import random

from config import *


class Bullet(pygame.sprite.Sprite):
    gun_type = 0
    gun_time = 0
    image = pygame.image.load("img/net.png")
    image = pygame.transform.scale(image, (40, 80))

    def __init__(self, x, y):
        super().__init__()
        self.image = Bullet.image
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10

    @classmethod
    def upgrade(cls):
        cls.image = pygame.image.load("img/treasure2.png")
        cls.image = pygame.transform.scale(cls.image, (40, 80))
        cls.gun_type = 1
        cls.gun_time = pygame.time.get_ticks()

    @classmethod
    def degrade(cls):
        cls.image = pygame.image.load("img/net.png")
        cls.image = pygame.transform.scale(cls.image, (40, 80))
        cls.gun_type = 0

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()
