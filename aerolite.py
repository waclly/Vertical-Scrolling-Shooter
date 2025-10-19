import pygame
import random 

from config import *

img = []

for i in range(1, 4):
    img.append(pygame.image.load(f"img/jellyfish{i}_resized.png"))

class Aerolite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.image = pygame.Surface((30, 40))
        # self.image.fill(RED)

        i = random.randrange(0, 10)
        self.id = 2
        self.hp = 1
        if(i == 0):
            self.image = img[0]
            # self.image = pygame.transform.scale(self.image, (95, 85))
            self.id = 0
            self.hp = 5
        if(i == 1):
            self.image = img[1]
            # self.image = pygame.transform.scale(self.image, (90, 80))
            self.id = 1
            self.hp = 3
        if(i >= 2):
            self.image = img[2]
            # self.image = pygame.transform.scale(self.image, (65, 55))

        self.image_ori = self.image.copy()
        self.rect = self.image.get_rect()
        self.radius = self.rect.width * 0.6 / 2
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)

        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-200, -self.rect.height)
        self.speedy = random.randrange(3, 5)
        self.speedx = random.randrange(-3, 3)   
        self.rotate_degree = random.randrange(-8, 8)
        self.total_degree = 0
    
    def rotate(self):
        self.total_degree += self.rotate_degree
        self.image = pygame.transform.rotate(self.image_ori, self.total_degree % 360)
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center


    def update(self):
        self.rotate()
        self.rect.y += self.speedy
        self.rect.x += self.speedx

        if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
            self.speedx = random.randrange(-3, 3)