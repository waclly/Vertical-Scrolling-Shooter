import pygame
import random 

from config import *

img = []

for i in range(1, 3):
    img.append(pygame.image.load(f"img/treasure{i}.png"))

class Treasure(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        i = random.randrange(0, 2)
        self.id = i
        self.image = img[i]
        if(i == 1):
            self.image = pygame.transform.scale(self.image, (40, 80))
        else:
            self.image = pygame.transform.scale(self.image, (50, 50))
        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()
        self.rect.center = center
    
    def update(self):
        self.rect.y += 2
        if self.rect.top > HEIGHT:
            self.kill()