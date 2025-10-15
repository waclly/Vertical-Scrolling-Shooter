import pygame
from config import *
from bullet import Bullet


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.image = pygame.Surface((50, 40))
        # self.image.fill(GREEN)
        self.image = pygame.image.load("img/player1_resized.png")
        # self.image = pygame.transform.scale(self.image, (120, 80))
        self.rect = self.image.get_rect()
        self.radius = self.rect.width * 0.7 / 2
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        
        self.hp = 15

        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speed = 4
        self.speedx = self.speed
        self.speedy = self.speed

        # self.rect.x = 200
        # self.rect.y = 200

    def update(self):
        key_pressed = pygame.key.get_pressed()
        
        if key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speedx
        if key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speedx
        if key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]:
            self.rect.y -= self.speedy
        if key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]:
            self.rect.y += self.speedy

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
    
    def shoot(self, all_sprites, bullets):
        if(Bullet.gun_type == 1):
            bullet1 = Bullet(self.rect.centerx - 20, self.rect.top)
            bullet2 = Bullet(self.rect.centerx + 20, self.rect.top)
            all_sprites.add(bullet1)
            all_sprites.add(bullet2)
            bullets.add(bullet1)
            bullets.add(bullet2)
        else:
            bullet = Bullet(self.rect.centerx, self.rect.top)

            all_sprites.add(bullet)
            bullets.add(bullet)
    
    def upgrade(self):
        center = self.rect.center
        self.image = pygame.image.load("img/player2_resized.png")
        self.rect = self.image.get_rect()
        self.rect.center = center
        # self.image = pygame.transform.scale(self.image, (80, 100))

    def degrade(self):
        center = self.rect.center
        self.image = pygame.image.load("img/player1_resized.png")
        self.rect = self.image.get_rect()
        self.rect.center = center
        # self.image = pygame.transform.scale(self.image, (120, 80))
    
    