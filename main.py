import config
import pygame

from sprites import Player

pygame.init()
pygame.font.init()

font = pygame.font.Font(pygame.font.get_default_font(), 200)

screen = pygame.display.set_mode((config.Width, config.Height))

clock = pygame.time.Clock()

player = pygame.sprite.Group()
mobs = pygame.sprite.Group()
additional = pygame.sprite.Group()

ticks_from_start = 0
number_mobs = 1

for i in range(number_mobs):
    mobs.add(mobs)

player_entity = Player()
player.add(player_entity)

running = True

while running:
    clock.tick(config.Framerate)
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False

    player.update()

    if player_entity.health == 0:
        running = False

    hits = pygame.sprite.groupcollide(player, mobs, False, True)
    ticks_from_start += 1
    screen.fill(config.BLACK)
    player.draw(screen)
    mobs.draw(screen)
    additional.draw(screen)

    if config.DEBUG:
        for mob in mobs:
            player_cords = player_entity.rect.center
            mob_cords = mob.rect.center
            pygame.draw.aaline(screen, (255, 0, 0), player_cords, mob_cords)
            pygame.display.flip()

    # pygame.init()
    # screen = pygame.display.set_mode((600, 600))
    # running = True
    #
    # while running:
    #    for event in pygame.event.get():
    #        if event.type == pygame.QUIT:
    #            running = False
    #
    #    screen.fill((0, 0, 0))
    #    pygame.draw.rect(screen, (0, 0, 255), (215, 250, 200, 200), 5)
    #    pygame.draw.polygon(screen, (0, 0, 255), [
    #        (160, 250), (320, 70), (330, 80), (460, 250)
    #    ], 5)
    #    pygame.draw.rect(screen, (0, 0, 255), (320, 310, 50, 50), 5)
    #    pygame.draw.rect(screen, (0, 0, 255), (250, 300, 50, 130))
    #    pygame.display.flip()
    pygame.display.flip()
pygame.quit()
