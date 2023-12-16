import pygame.key
import pygame
from pygame.sprite import Sprite
from pygame.surface import Surface, image
import config
import utils
import random


class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("assets/Mario.png")
        self.rect = self.image.get_rect()
        self.rect.get_center = (random.randint(0, config.Width - 25) // 2, config.Height - self.rect.height)
        self.speed_y = random.randint(5, 15)
        self.speed_x = random.randint(5, 15)
        self.health = 3
        self.is_jump = False

    def update(self):
        self.speed_x = 0
        self.speed_y += 1

        key = pygame.key.get_pressed()
        # if key[pygame.K_w]:
        # self.rect.y -= self.speed_y
        # if key[pygame.K_s]:
        # self.rect.y += self.speed_y
        if key[pygame.K_a]:
            self.rect.x -= self.speed_x
        if key[pygame.K_d]:
            self.rect.x += self.speed_x
        if key[pygame.K_SPACE] and self.is_jump == False:
            self.speed_y = ...
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


class Map(Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = Surface(
            (config.CELL_SIZE, config.CELL_SIZE)
        )
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.is_wall = False
        self.name = ""


class Platform(MapSprite):
    x = 0
    y = 0

    def __init__(self):
        super().__init__(config.GREEN)
        self.name = "Ground"
        self.rect.x = Platform.x
        self.rect.y = Platform.y
        Platform.x += config.CELL_SIZE
        if Platform.x == config.Width:
            Platform.x = 0
            Platform.y += config.CELL_SIZE
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 500)
        self.rect.y = random.randint(400, 500)
        self.rect.center = (self.rect.x, self.rect.y)
