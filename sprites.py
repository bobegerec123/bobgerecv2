import pygame.key
from pygame.sprite import Sprite
from pygame.surface import Surface, image
import config
import utils
import random


class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("assets/.... .png")
        self.rect = self.image.get_rect()
        self.rect.get_center =(random.randint(0, config.Width - 25) //2, config.Height - self.rect.height)
        self.speed_y = random.randint(5, 15)
        self.speed_x = random.randint(5, 15)
        self.health = 3

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

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > config.Width - self.rect.width:
            self.rect.x = config.Width - self.rect.width
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > config.Height - self.rect.height:
            self.rect.y = config.Height - self.rect.height


class mobs(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("assets/..... .png")
        self.rect = self.image.get_rect()
        self.speed_x = random.randint(3, 7)
        self.speed_y = random.randint(3, 7)

    def update(self):
        if self.rect.y + self.rect.height < config.Height:
            self.rect.y += self.speed_y
        else:
            self.kill()
