import pygame.key
import pygame
from pygame.sprite import Sprite
from pygame import Surface, image
import config
import random


class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.health = 5
        self.image = image.load("assets/bird.png")
        self.rect = self.image.get_rect()
        self.speed_y = random.randint(5, 15)
        self.speed_x = random.randint(5, 15)
        self.health = 3
        self.is_jump = False

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.rect.y -= self.speed_y
        if key[pygame.K_s]:
            self.rect.y += self.speed_y
        if key[pygame.K_a]:
            self.rect.x -= self.speed_x
        if key[pygame.K_d]:
            self.rect.x += self.speed_x
        if key[pygame.K_SPACE]:
            self.speed_y = self.speed_x
            self.is_jump = True

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > config.Width - self.rect.width:
            self.rect.x = config.Width - self.rect.width
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > config.Height - self.rect.height:
            self.rect.y = config.Height - self.rect.height


class Mobs(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("assets/Mushroom.png")
        self.rect = self.image.get_rect()
        self.speed_x = random.randint(3, 7)
        self.speed_y = random.randint(3, 7)

    def update(self):
        if self.rect.y + self.rect.height < config.Height:
            self.rect.y += self.speed_y
        else:
            self.kill()


# class Platforms(Sprite):
