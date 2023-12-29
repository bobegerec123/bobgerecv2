import pygame
import config
import utils
import Sprites.Sprites
from Sprites.Sprites import Player, Mob, Mushroom
from Sprites.MapSprite import Ground

pygame.init()
pygame.font.init()

background = pygame.image.load("assets/Map.png")
background = pygame.transform.scale(background, (config.WIDTH, config.HEIGHT))

font = pygame.font.SysFont(pygame.font.get_default_font(), 37)

screen = pygame.display.set_mode(
    (config.WIDTH, config.HEIGHT)
)

player = pygame.sprite.Group()
player.add(Player())

player_entity = Player()
player.add(player_entity)
running = True

__map = []

for i in range(config.CELL_ON_HEIGHT):
    __map.append(pygame.sprite.Group())
    for j in range(config.CELL_ON_WIDTH):
        group = __map[i]
        group.add(Ground())


mobs = pygame.sprite.Group()
n_mobs = 0
for i in range(n_mobs):
    mobs.add(Mob())

mushrooms = pygame.sprite.Group()
n_mushrooms = 1
for i in range(n_mushrooms):
    mushrooms.add(Mushroom())

clock = pygame.time.Clock()
running = True

while running:
    player_entity.time_for_mushroom += 1
    player_entity.points_alive += 1
    clock.tick(config.Framerate)
    if player_entity.resist > 0:
        player_entity.resist -= 1
    if player_entity.health == 0:
        running = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#    for mob in mobs:
#        mob.compute_move(player_entity)

    player.update()
    mobs.update()
    mushrooms.update()

    if len(mobs) < n_mobs:
        mobs.add(Mob())

    hits = pygame.sprite.groupcollide(player, mobs, False, True)
    if hits and player_entity.resist <= 0:
        player_entity.health -= 1
        player_entity.resist += 180

    if player_entity.time_for_mushroom == 360:
        player_entity.health -= 1

    if player_entity.time_for_mushroom == 180:
        mushrooms.add(Mushroom())

    hits_for_mushrooms = pygame.sprite.groupcollide(player, mushrooms, False, True)

    if hits_for_mushrooms:
        player_entity.time_for_mushroom = 0
        player_entity.points += 1

    screen.blit(background, (0, 0))
    text = font.render(f"Points:{player_entity.points}", False, (255, 0, 0))
    screen.blit(text, (0, 0))
    text = font.render(f"Health:{player_entity.health}", False, (255, 255, 255))
    screen.blit(text, (60, 30))
    text = font.render(f"Shield:{player_entity.resist // 60}", False, (0, 0, 0))
    screen.blit(text, (0, 60))
    text = font.render(f"Time Before Spawn:{player_entity.points_alive // 60}", False, (0, 0, 255))
    screen.blit(text, (60, 90))
    text = font.render(f"Time Before Mushroom spawned:{player_entity.time_for_mushroom // 60}", False, (255, 255, 255))
    screen.blit(text, (0, 120))
    player.draw(screen)
    mobs.draw(screen)
    mushrooms.draw(screen)
    pygame.display.flip()

pygame.quit()
print("АЛО ГРИБ, АЛО!")
