import pygame.key
from pygame.sprite import Sprite
from pygame import Surface, image, transform
import config
import random
import utils


class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.time_for_mushroom = 0
        self.points_alive = 0
        self.index = 0

        self.images = [
            image.load("assets/bird.png")
        ]
        self.images = list(map(
            lambda x: transform.scale(x, (64, 64)),
            self.images
        ))

        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (config.WIDTH / 2, config.HEIGHT / 2)

        self.health = 5
        self.points = 0
        self.resist = 5

        self.speed_x = 0
        self.speed_y = 0
        self.is_jump = True

    def update(self):

        self.speed_x = 0
        self.speed_y += 1
        self.update_image_move(0)

        key = pygame.key.get_pressed()
        # if key[pygame.K_w]:
        # self.speed_y = -5
        # if key[pygame.K_s]:
        # self.speed_y = 5
        if key[pygame.K_j] and self.points >= 5:
            self.health += 1
            self.points -= 5
        if key[pygame.K_a]:
            self.speed_x = -5
            self.update_image_move(-1)
        if key[pygame.K_d]:
            self.speed_x = 5
            self.update_image_move(1)
        if key[pygame.K_SPACE] and self.is_jump == False:
            self.speed_y = -17
            self.is_jump = True

        self.rect.x += self.speed_x
        if self.rect.x > config.WIDTH - self.rect.width or self.rect.x < 0:
            self.rect.x -= self.speed_x
            # self.is_jump = False
            # self.speed_x *= 0.95

        self.rect.y += self.speed_y
        if self.rect.y > config.HEIGHT - self.rect.height or self.rect.y < 0:
            self.rect.y -= self.speed_y
            self.is_jump = False
            # self.speed_y *= 0.95

    def update_image(self, index):
        if self.index != index:
            self.index = index
            self.image = self.images[self.index]

    def update_image_move(self, move: int):
        angle = 45 * move
        # image = transform.rotate(self.images[self.index], angle)
        image = self.images[self.index]
        if move < 0:
            image = transform.flip(image, 1, 0)
        self.image = image

    def reverse_speed_x(self):
        self.speed_x = -self.speed_x

    def reverse_speed_y(self):
        self.speed_y = -self.speed_y

    def get_knockback(self):
        self.rect.x += -self.speed_x
        self.rect.y += -self.speed_y


class Mob(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.speed_y = -random.randint(7, 8)
        self.speed_x = random.randint(5, 6)

        self.index = 0
        self.images = [
            image.load("assets/bird.2.png"),
            image.load("assets/bird.2.png")
        ]
        self.images = list(map(
            lambda x: transform.scale(x, (40, 40)),
            self.images
        ))
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(0, config.WIDTH - 50),
            random.randint(0, 10)
        )
        # self.rect.x = random.randint(100, 500)
        # self.rect.y = random.randint(100, 500)
        self.rect.center = (self.rect.x, self.rect.y)
        # self.rect.center = (config.WIDTH / 5, config.HEIGHT / 3)

    def update(self):
        if self.rect.y + self.rect.height < config.HEIGHT:
            self.rect.y -= self.speed_y
        else:
            self.kill()

#    def compute_move(self, player: Player):
#        x_player, y_player = player.rect.center  # (10, 20)
#        x_mob, y_mob = self.rect.center
#
#        move_right = utils.lenght(x_player, y_player, x_mob + self.speed_x, y_mob)
#        move_left = utils.lenght(x_player, y_player, x_mob - self.speed_x, y_mob)
#        stay_here = utils.lenght(x_player, y_player, x_mob, y_mob)
#
#        min_len = min(move_left, move_right, stay_here)
#        if min_len == move_left:
#            self.rect.x -= self.speed_x
#        if min_len == move_right:
#            self.rect.x += self.speed_x


# тут у нас будет что то что лежит на полу и коцает нас
class Mushroom(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.index = 0

        self.images = [
            image.load("assets/Mushroom.2.png"),
            image.load("assets/Mushroom.2.png")
        ]
        self.images = list(map(
            lambda x: transform.scale(x, (64, 64)),
            self.images
        ))

        self.image = self.images[self.index]

        self.rect = self.image.get_rect()
        self.rect.y = random.randint(500, 650)
        self.rect.x = random.randint(0, 600)
        self.rect.center = self.rect.x, self.rect.y

        self.speed_x = 0
        self.speed_y = 0
