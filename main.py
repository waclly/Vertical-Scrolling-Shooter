import pygame
import random

from config import *
from player import Player
from aerolite import Aerolite
from treasure import Treasure
from bullet import Bullet

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(WINDOW_NAME)
clock = pygame.time.Clock()

game_font = pygame.font.Font('04B_19.ttf',40)

def draw_text(surf, text, size, x, y, color = WHITE):
    font = pygame.font.Font(FONT_NAME, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def draw_health(surf, hp, x, y):
    if(hp < 0):
        hp = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (hp / 15) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

sound = pygame.mixer.Sound("sound/music1.mp3")
sound.play(loops=-1)
sound.set_volume(1.0)
hit_sound = pygame.mixer.Sound("sound/hit.mp3")
hit_sound.set_volume(1.0)
hitted_sound = pygame.mixer.Sound("sound/hitted.mp3")
hitted_sound.set_volume(1.0)
restore_sound = pygame.mixer.Sound("sound/restore.wav")
restore_sound.set_volume(1.0)

running = True
show_init = True
while running:
    if(show_init):
        background_img = pygame.image.load("img/opening.png").convert()
        background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
        screen.blit(background_img, (0, 0))

        pygame.display.update()
        waiting = True
        while(waiting):
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    waiting = False
        show_init = False

        all_sprites = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        aerolites = pygame.sprite.Group()
        powers = pygame.sprite.Group()

        player = Player()
        all_sprites.add(player)

        for i in range(16):
            aerolite = Aerolite()
            all_sprites.add(aerolite)
            aerolites.add(aerolite)

        score = 0
        flag = False

        background_img = pygame.image.load("img/background.png")
        # background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))


    clock.tick(FPS)
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot(all_sprites, bullets)
            

    # Update
    all_sprites.update()

    hits = pygame.sprite.spritecollide(player, aerolites, False, pygame.sprite.collide_circle)

    for hit in hits:
        hitted_sound.play()
        player.hp -= abs(hit.id - 3)
        hit.kill()
        if(player.hp <= 0):
            show_init = True
            background_img = pygame.image.load("img/gameover.png").convert()
            background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
            screen.blit(background_img, (0, 0))
            draw_text(screen, str(score), 50, WIDTH // 2 + 150, HEIGHT * 3 // 4 - 77, (116,140,139))
            pygame.display.update()
            pygame.time.wait(1500)

            waiting = True
            while(waiting):
                clock.tick(FPS)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYUP:
                        waiting = False

        aerolite = Aerolite()
        all_sprites.add(aerolite)
        aerolites.add(aerolite)
    
    if(player.hp > 0):
        hits = pygame.sprite.groupcollide(aerolites, bullets, False, True)
        for hit in hits:        
            if(hit.hp > 1):
                hit.hp -= 1
                hit.rect.y -= 10
            elif(hit.hp == 1):
                hit_sound.play()

                if(hit.id == 0):
                    score += 100
                elif(hit.id == 1):
                    score += 80
                else:
                    score += 10
                if(random.random() > 0.9):
                    treasure = Treasure(hit.rect.center)
                    all_sprites.add(treasure)
                    powers.add(treasure)
                hit.kill()
                aerolite = Aerolite()
                all_sprites.add(aerolite)
                aerolites.add(aerolite)


        if(score >= 500 and not flag):
            flag = True
            background_img = pygame.image.load("img/background2.webp").convert()
            # background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
            for i in range(4):
                aerolite = Aerolite()
                all_sprites.add(aerolite)
                aerolites.add(aerolite)
        
        hits = pygame.sprite.spritecollide(player, powers, False)

        for hit in hits:
            restore_sound.play()
            if(hit.id == 0):
                player.hp += 3
                player.hp = min(player.hp, 15)
            if(hit.id == 1):
                Bullet.upgrade()
                player.upgrade()
            hit.kill()

        if(pygame.time.get_ticks() - Bullet.gun_time > 5000 and Bullet.gun_type == 1):
            Bullet.degrade()
            player.degrade()

        # Draw / render
        screen.blit(background_img, (0, 0))
        all_sprites.draw(screen)
        draw_text(screen, "SCORE: " + str(score), 25, WIDTH // 2, 10)
        draw_health(screen, player.hp, 5, 5)
        pygame.display.update()
            
