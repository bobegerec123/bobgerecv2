import random
import math

from pygame.sprite import Group
from Sprites.MapSprite import Wall, Ground

import Sprites.MapSprite


def lenght(x1, y1, x2, y2) -> float:
    a = (x1 - x2) ** 2
    b = (y1 - y2) ** 2
    c = math.sqrt(a + b)
    return c


def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b


def get_lenght(x1, y1, x2, y2):
    x = (x1 - x2) ** 2
    y = math.pow(y1 - y2, 2)
    return math.sqrt(x + y)


